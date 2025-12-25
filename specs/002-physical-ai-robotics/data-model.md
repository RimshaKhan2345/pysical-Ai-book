# Data Model: Physical AI & Humanoid Robotics Book with Embedded RAG Chatbot

## Entities

### Robotics Book Content
- **id**: UUID (Primary Key)
- **title**: String (255 characters)
- **content**: Text (Markdown format)
- **section**: String (255 characters) - Values: "intro", "chapter-1", "chapter-2", "chapter-3", "chapter-4"
- **chapter_number**: Integer - Values: 0 (intro), 1, 2, 3, 4
- **order**: Integer
- **created_at**: DateTime
- **updated_at**: DateTime
- **metadata**: JSONB (Additional content attributes, robotics-specific tags)

**Relationships**: None

**Validation**: 
- title and content are required
- chapter_number must be between 0 and 4
- section must be one of the allowed values
- Each content item must have a unique combination of section and order

### RAG Query (Robotics-focused)
- **id**: UUID (Primary Key)
- **query_text**: Text
- **user_ip**: String (45 characters max for IPv6)
- **session_id**: String (255 characters, optional)
- **created_at**: DateTime
- **query_vector**: Vector (for similarity search in Qdrant)
- **robotics_topic**: String (255 characters, optional) - Values: "ROS2", "Gazebo", "Unity", "NVIDIA Isaac", "VLA", "General"

**Relationships**: None (stored in Qdrant for vector search)

**Validation**:
- query_text is required
- user_ip must be a valid IP address format
- robotics_topic must be one of the allowed values if provided
- created_at defaults to current timestamp

### Response
- **id**: UUID (Primary Key)
- **query_id**: UUID (Foreign Key to RAG Query)
- **response_text**: Text
- **confidence_score**: Decimal (0.0 to 1.0)
- **sources**: JSONB (List of content IDs and snippets)
- **created_at**: DateTime

**Relationships**: 
- Belongs to RAG Query

**Validation**:
- query_id is required and must reference an existing query
- response_text is required
- confidence_score must be between 0.0 and 1.0

### User Interaction
- **id**: UUID (Primary Key)
- **user_ip**: String (45 characters max for IPv6)
- **interaction_type**: Enum (query, navigation, feedback, content_view)
- **target_id**: UUID (ID of the target entity)
- **robotics_topic**: String (255 characters, optional) - Values: "ROS2", "Gazebo", "Unity", "NVIDIA Isaac", "VLA", "General"
- **metadata**: JSONB (Additional interaction data)
- **created_at**: DateTime

**Relationships**: None

**Validation**:
- user_ip and interaction_type are required
- created_at defaults to current timestamp
- robotics_topic must be one of the allowed values if provided

## State Transitions

### RAG Query Lifecycle
1. **Created**: When a user submits a query about robotics concepts
2. **Processing**: When the system is generating a response using robotics-focused embeddings
3. **Completed**: When the response is generated and returned
4. **Failed**: If the query processing fails (with error details)

## Constraints

### Performance Constraints
- Robotics book content should be chunked to optimize vector search (max 1000 tokens per chunk)
- Query response time should be under 5 seconds (95th percentile)

### Data Retention
- Query history stored for 30 days as per specification
- User interaction logs stored for 30 days as per specification

### Rate Limiting
- Maximum 1,000 queries per IP address per month
- Implementation using sliding window counter in Neon Postgres

### Robotics-Specific Constraints
- Content must not include information about real hardware deployments
- Content must not include custom ML training information
- Content must not include tool/vendor comparison sections