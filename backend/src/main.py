from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.endpoints import robotics_rag
from .api.v1.endpoints import health
from .core.config import settings

app = FastAPI(
    title="Physical AI & Humanoid Robotics RAG API",
    description="API for robotics-focused RAG chatbot",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(health.router, prefix="/api/v1", tags=["health"])
app.include_router(robotics_rag.router, prefix="/api/v1", tags=["robotics-rag"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)