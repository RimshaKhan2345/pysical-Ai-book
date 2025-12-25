# Data Model: AI/Spec-Driven Book with Embedded RAG Chatbot

## Entities

### Book Content
- **id**: UUID (Primary Key)
- **title**: String (255 characters)
- **content**: Text (Markdown format)
- **section**: String (255 characters)
- **chapter**: Integer
- **order**: Integer
- **created_at**: DateTime
- **updated_at**: DateTime
- **metadata**: JSONB (Additional content attributes)

**Relationships**: None

**Validation**: 
- title and content are required
- chapter and order must be positive integers
- Each content item must have a unique combination of section and order

### RAG Query
- **id**: UUID (Primary Key)
- **query_text**: Text
- **user_ip**: String (45 characters max for IPv6)
- **session_id**: String (255 characters, optional)
- **created_at**: DateTime
- **query_vector**: Vector (for similarity search in Qdrant)

**Relationships**: None (stored in Qdrant for vector search)

**Validation**:
- query_text is required
- user_ip must be a valid IP address format
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
- **interaction_type**: Enum (query, navigation, feedback)
- **target_id**: UUID (ID of the target entity)
- **metadata**: JSONB (Additional interaction data)
- **created_at**: DateTime

**Relationships**: None

**Validation**:
- user_ip and interaction_type are required
- created_at defaults to current timestamp

## State Transitions

### RAG Query Lifecycle
1. **Created**: When a user submits a query
2. **Processing**: When the system is generating a response
3. **Completed**: When the response is generated and returned
4. **Failed**: If the query processing fails (with error details)

## Constraints

### Performance Constraints
- Book content should be chunked to optimize vector search (max 1000 tokens per chunk)
- Query response time should be under 5 seconds (95th percentile)

### Data Retention
- Query history stored for 30 days as per specification
- User interaction logs stored for 30 days as per specification

### Rate Limiting
- Maximum 1,000 queries per IP address per month
- Implementation using sliding window counter in Neon Postgres