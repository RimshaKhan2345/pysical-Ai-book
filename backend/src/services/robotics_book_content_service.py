from typing import List, Optional, Dict, Any
from uuid import UUID
from ..models.robotics_book_content import (
    RoboticsBookContent,
    RoboticsBookContentCreate,
    RoboticsBookContentUpdate
)
from ..core.config import settings

class RoboticsBookContentService:
    def __init__(self):
        # In a real implementation, this would connect to a database
        # For now, we'll use an in-memory store for demonstration
        self.contents: Dict[UUID, RoboticsBookContent] = {}
    
    async def create_content(self, content: RoboticsBookContentCreate) -> RoboticsBookContent:
        """
        Create a new robotics book content entry
        """
        # In a real implementation, this would save to a database
        # For now, we'll create a mock entry
        import uuid
        from datetime import datetime
        
        new_content = RoboticsBookContent(
            id=uuid.uuid4(),
            title=content.title,
            content=content.content,
            section=content.section,
            chapter_number=content.chapter_number,
            order=content.order,
            metadata=content.metadata,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        self.contents[new_content.id] = new_content
        return new_content
    
    async def get_content_by_id(self, content_id: UUID) -> Optional[RoboticsBookContent]:
        """
        Retrieve a specific content by its ID
        """
        return self.contents.get(content_id)
    
    async def get_content_by_section(self, section: str) -> List[RoboticsBookContent]:
        """
        Retrieve all content for a specific section
        """
        return [content for content in self.contents.values() if content.section == section]
    
    async def get_all_content(self) -> List[RoboticsBookContent]:
        """
        Retrieve all robotics book content
        """
        return list(self.contents.values())
    
    async def update_content(self, content_id: UUID, content_update: RoboticsBookContentUpdate) -> Optional[RoboticsBookContent]:
        """
        Update a specific content entry
        """
        if content_id not in self.contents:
            return None
        
        existing_content = self.contents[content_id]
        
        # Update fields that are provided
        update_data = content_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(existing_content, field, value)
        
        # Update the timestamp
        from datetime import datetime
        existing_content.updated_at = datetime.utcnow()
        
        return existing_content
    
    async def delete_content(self, content_id: UUID) -> bool:
        """
        Delete a specific content entry
        """
        if content_id in self.contents:
            del self.contents[content_id]
            return True
        return False