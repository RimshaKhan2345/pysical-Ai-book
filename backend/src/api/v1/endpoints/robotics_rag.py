from fastapi import APIRouter, HTTPException, Depends, Request
from typing import Optional
from uuid import UUID
import logging
from ....models.robotics_book_content import (
    RAGQueryCreate, 
    Response as ResponseModel,
    RoboticsBookContent
)
from ....services.robotics_rag_service import RoboticsRAGService
from ....services.robotics_book_content_service import RoboticsBookContentService
from ....core.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)

# Initialize services
rag_service = RoboticsRAGService()
content_service = RoboticsBookContentService()

@router.on_event("startup")
async def startup_event():
    await rag_service.initialize_collection()
    logger.info("RAG service initialized")

@router.post("/robotics/query", response_model=ResponseModel)
async def query_robotics_content(
    request: Request,
    query_data: RAGQueryCreate
):
    """
    Submit a query about robotics concepts to the RAG system and receive a response.
    """
    try:
        # Get client IP for rate limiting
        client_ip = request.client.host
        
        # Use the query text, selected text, and topic from the request
        response = await rag_service.query_full_book(
            query_text=query_data.query_text,
            selected_text=query_data.query_text  # In a real implementation, selected text would come from a different field
        )
        
        # Log the interaction
        logger.info(f"Query from {client_ip}: {query_data.query_text[:50]}...")
        
        return response
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing query")

@router.get("/robotics/topics")
async def get_robotics_topics():
    """
    Get a list of available robotics topics covered in the book.
    """
    topics = [
        {"id": "ros2", "name": "ROS 2", "description": "Robot Operating System 2"},
        {"id": "gazebo", "name": "Gazebo", "description": "Robot Simulation Framework"},
        {"id": "unity", "name": "Unity", "description": "Digital Twin Simulation"},
        {"id": "nvidia-isaac", "name": "NVIDIA Isaac", "description": "AI-Robot Brain Platform"},
        {"id": "vla", "name": "VLA", "description": "Vision-Language-Action Models"}
    ]
    
    return {
        "topics": topics
    }

@router.get("/robotics/content/{content_id}")
async def get_content_by_id(content_id: UUID):
    """
    Retrieve specific content by its ID
    """
    content = await content_service.get_content_by_id(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.get("/robotics/content/")
async def get_all_content():
    """
    Retrieve all robotics book content
    """
    contents = await content_service.get_all_content()
    return contents