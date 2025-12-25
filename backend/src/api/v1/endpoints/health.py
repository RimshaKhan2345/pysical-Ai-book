from fastapi import APIRouter
from typing import Dict
import time

router = APIRouter()

@router.get("/health")
async def health_check() -> Dict:
    """
    Health check endpoint to verify the API is running
    """
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0"
    }

@router.get("/ready")
async def readiness_check() -> Dict:
    """
    Readiness check to verify the API is ready to serve requests
    """
    # In a real implementation, you would check database connections,
    # external service availability, etc.
    return {
        "status": "ready",
        "timestamp": time.time()
    }