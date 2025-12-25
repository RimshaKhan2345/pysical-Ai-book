from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
import uuid

class RoboticsTopic(str, Enum):
    ROS2 = "ROS2"
    GAZEBO = "Gazebo"
    UNITY = "Unity"
    NVIDIA_ISAAC = "NVIDIA Isaac"
    VLA = "VLA"
    GENERAL = "General"

class InteractionType(str, Enum):
    QUERY = "query"
    NAVIGATION = "navigation"
    FEEDBACK = "feedback"
    CONTENT_VIEW = "content_view"

class RoboticsBookContentBase(BaseModel):
    title: str
    content: str
    section: str
    chapter_number: int
    order: int
    metadata: Optional[Dict[str, Any]] = {}

class RoboticsBookContentCreate(RoboticsBookContentBase):
    pass

class RoboticsBookContentUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    section: Optional[str] = None
    chapter_number: Optional[int] = None
    order: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None

class RoboticsBookContent(RoboticsBookContentBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class RAGQueryBase(BaseModel):
    query_text: str
    user_ip: Optional[str] = None
    session_id: Optional[str] = None
    robotics_topic: Optional[RoboticsTopic] = None

class RAGQueryCreate(RAGQueryBase):
    pass

class RAGQuery(RAGQueryBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True

class ResponseBase(BaseModel):
    query_id: uuid.UUID
    response_text: str
    confidence_score: float
    sources: List[Dict[str, Any]]

class ResponseCreate(ResponseBase):
    pass

class Response(ResponseBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True

class UserInteractionBase(BaseModel):
    user_ip: str
    interaction_type: InteractionType
    target_id: uuid.UUID
    robotics_topic: Optional[RoboticsTopic] = None
    metadata: Optional[Dict[str, Any]] = {}

class UserInteractionCreate(UserInteractionBase):
    pass

class UserInteraction(UserInteractionBase):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True