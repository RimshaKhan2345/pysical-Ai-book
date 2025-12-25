import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Physical AI & Humanoid Robotics RAG API"
    
    # Database settings
    NEON_DATABASE_URL: str = os.getenv("NEON_DATABASE_URL", "")
    
    # Qdrant settings
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY", "")
    
    # OpenAI settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = 10  # For development
    RATE_LIMIT_PER_MONTH: int = 1000  # As per requirements
    
    # CORS
    ALLOWED_ORIGINS: list = ["*"]  # Should be configured properly for production
    
    # Robotics-specific settings
    ROBOTICS_CONTENT_COLLECTION: str = "robotics_content"
    ROBOTICS_EMBEDDING_MODEL: str = "text-embedding-3-small"  # OpenAI embedding model
    
    class Config:
        env_file = ".env"

settings = Settings()