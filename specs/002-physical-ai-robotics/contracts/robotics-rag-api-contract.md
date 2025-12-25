# API Contract: Robotics RAG Chatbot Service

## Base URL
`https://api.yourdomain.com` (to be implemented with FastAPI)

## Endpoints

### POST /api/v1/robotics/query
Submit a query about robotics concepts to the RAG system and receive a response.

#### Request
```json
{
  "query": "How does ROS 2 handle communication between nodes?",
  "session_id": "optional-session-id",
  "selected_text": "optional selected text from the page",
  "robotics_topic": "ROS2"
}
```

#### Response
```json
{
  "id": "uuid-of-the-response",
  "query_id": "uuid-of-the-original-query",
  "answer": "ROS 2 uses a DDS (Data Distribution Service) implementation for communication...",
  "confidence_score": 0.92,
  "sources": [
    {
      "content_id": "uuid-of-source-content",
      "title": "Chapter 1: The Robotic Nervous System",
      "section": "ROS2",
      "excerpt": "Relevant excerpt from the content about ROS 2 communication..."
    }
  ],
  "created_at": "2025-06-13T10:30:00Z"
}
```

#### Error Responses
- `400 Bad Request`: Invalid query format
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Processing error

### GET /api/v1/robotics/topics
Get a list of available robotics topics covered in the book.

#### Response
```json
{
  "topics": [
    {"id": "ros2", "name": "ROS 2", "description": "Robot Operating System 2"},
    {"id": "gazebo", "name": "Gazebo", "description": "Robot Simulation Framework"},
    {"id": "unity", "name": "Unity", "description": "Digital Twin Simulation"},
    {"id": "nvidia-isaac", "name": "NVIDIA Isaac", "description": "AI-Robot Brain Platform"},
    {"id": "vla", "name": "VLA", "description": "Vision-Language-Action Models"}
  ],
  "timestamp": "2025-06-13T10:30:00Z"
}
```

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

### POST /api/v1/robotics/feedback
Submit feedback on a query response.

#### Request
```json
{
  "query_id": "uuid-of-the-original-query",
  "rating": "positive|negative",
  "robotics_topic": "ROS2",
  "comment": "optional comment about the response accuracy for robotics concepts"
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

## Robotics Content Filtering
The API ensures that responses adhere to the content scope:
- Responses will not include information about real hardware deployments
- Responses will not include custom ML training information
- Responses will not include tool/vendor comparison information