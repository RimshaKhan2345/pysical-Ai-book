# API Contract: RAG Chatbot Service

## Base URL
`https://api.yourdomain.com` (to be implemented with FastAPI)

## Endpoints

### POST /api/v1/query
Submit a query to the RAG system and receive a response.

#### Request
```json
{
  "query": "What are the best practices for RAG implementation?",
  "session_id": "optional-session-id",
  "selected_text": "optional selected text from the page"
}
```

#### Response
```json
{
  "id": "uuid-of-the-response",
  "query_id": "uuid-of-the-original-query",
  "answer": "The best practices for RAG implementation include...",
  "confidence_score": 0.85,
  "sources": [
    {
      "content_id": "uuid-of-source-content",
      "title": "Chapter Title",
      "section": "Section Name",
      "excerpt": "Relevant excerpt from the content..."
    }
  ],
  "created_at": "2025-06-13T10:30:00Z"
}
```

#### Error Responses
- `400 Bad Request`: Invalid query format
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Processing error

### GET /api/v1/health
Check the health status of the API.

#### Response
```json
{
  "status": "healthy",
  "timestamp": "2025-06-13T10:30:00Z",
  "version": "1.0.0"
}
```

### POST /api/v1/feedback
Submit feedback on a query response.

#### Request
```json
{
  "query_id": "uuid-of-the-original-query",
  "rating": "positive|negative",
  "comment": "optional comment about the response"
}
```

#### Response
```json
{
  "status": "feedback recorded",
  "query_id": "uuid-of-the-original-query"
}
```

## Rate Limiting
All endpoints are subject to rate limiting:
- Maximum 1,000 requests per IP address per month
- Requests are tracked by IP address with a sliding window

## Authentication
No authentication required. Rate limiting is performed by IP address.