import asyncio
from typing import List, Dict, Any, Optional
from uuid import UUID
from openai import AsyncOpenAI
from qdrant_client import AsyncQdrantClient
from qdrant_client.http import models
from ..models.robotics_book_content import RAGQuery, Response, RoboticsBookContent
from ..core.config import settings

class RoboticsRAGService:
    def __init__(self):
        self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.qdrant_client = AsyncQdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = settings.ROBOTICS_CONTENT_COLLECTION
        
    async def initialize_collection(self):
        """
        Initialize the Qdrant collection for robotics content
        """
        try:
            # Check if collection exists
            await self.qdrant_client.get_collection(self.collection_name)
        except:
            # Create collection if it doesn't exist
            await self.qdrant_client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=1536,  # Size for OpenAI embeddings
                    distance=models.Distance.COSINE
                )
            )
    
    async def embed_text(self, text: str) -> List[float]:
        """
        Create an embedding for the given text using OpenAI
        """
        response = await self.openai_client.embeddings.create(
            input=text,
            model=settings.ROBOTICS_EMBEDDING_MODEL
        )
        return response.data[0].embedding
    
    async def store_content(self, content: RoboticsBookContent):
        """
        Store content in the vector database
        """
        # Create embedding for the content
        embedding = await self.embed_text(content.content)
        
        # Store in Qdrant
        await self.qdrant_client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(
                    id=str(content.id),
                    vector=embedding,
                    payload={
                        "title": content.title,
                        "content": content.content,
                        "section": content.section,
                        "chapter_number": content.chapter_number,
                        "order": content.order,
                        "metadata": content.metadata
                    }
                )
            ]
        )
    
    async def query_content(self, query_text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Query the vector database for relevant content
        """
        # Create embedding for the query
        query_embedding = await self.embed_text(query_text)
        
        # Search in Qdrant
        search_results = await self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=top_k
        )
        
        # Format results
        results = []
        for result in search_results:
            results.append({
                "id": UUID(result.id),
                "title": result.payload["title"],
                "content": result.payload["content"],
                "section": result.payload["section"],
                "chapter_number": result.payload["chapter_number"],
                "order": result.payload["order"],
                "metadata": result.payload["metadata"],
                "score": result.score
            })
        
        return results
    
    async def generate_response(self, query: RAGQuery) -> Response:
        """
        Generate a response to the user's query using RAG
        """
        # Find relevant content
        relevant_contents = await self.query_content(query.query_text)
        
        if not relevant_contents:
            # If no relevant content found, return a default response
            return Response(
                id=UUID(int=0),  # Placeholder ID
                query_id=query.id,
                response_text="I couldn't find any relevant information in the robotics book to answer your question.",
                confidence_score=0.0,
                sources=[],
                created_at=None  # Will be set by the database
            )
        
        # Format the context for the LLM
        context_parts = []
        for content in relevant_contents:
            context_parts.append(f"Section: {content['section']}\nTitle: {content['title']}\nContent: {content['content'][:500]}...")  # Limit content length
        
        context = "\n\n".join(context_parts)
        
        # Create the prompt for the LLM
        prompt = f"""
        You are an assistant for the Physical AI & Humanoid Robotics book. 
        Answer the user's question based on the provided context from the book.
        If the context doesn't contain enough information to answer the question, 
        say so and suggest related topics from the book.
        
        Context:
        {context}
        
        Question: {query.query_text}
        
        Answer:
        """
        
        # Generate response using OpenAI
        response = await self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant for the Physical AI & Humanoid Robotics book. Provide accurate answers based on the book content."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.3
        )
        
        # Create response object
        response_obj = Response(
            id=UUID(int=0),  # Placeholder ID
            query_id=query.id,
            response_text=response.choices[0].message.content,
            confidence_score=0.9,  # Placeholder - in a real implementation, this would be calculated
            sources=[
                {
                    "content_id": str(content["id"]),
                    "title": content["title"],
                    "section": content["section"],
                    "excerpt": content["content"][:200] + "..." if len(content["content"]) > 200 else content["content"]
                }
                for content in relevant_contents
            ],
            created_at=None  # Will be set by the database
        )
        
        return response_obj
    
    async def query_full_book(self, query_text: str, selected_text: Optional[str] = None) -> Response:
        """
        Query the full robotics book content, potentially with selected text context
        """
        # If selected text is provided, combine it with the query
        if selected_text:
            full_query = f"Regarding this text: '{selected_text}', {query_text.lower()}"
        else:
            full_query = query_text
        
        # Create a temporary query object
        from ..models.robotics_book_content import RAGQueryCreate
        temp_query = RAGQueryCreate(
            query_text=full_query,
            user_ip="temp",
            session_id="temp"
        )
        
        # Generate response
        response = await self.generate_response(temp_query)
        return response