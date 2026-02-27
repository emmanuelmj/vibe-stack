import uuid
from pydantic import BaseModel, EmailStr
from typing import Optional, Any, Dict
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class AgentJobTrigger(BaseModel):
    workflow_id: str
    payload_data: Dict[str, Any]

class AgentJobResponse(BaseModel):
    status: str
    job_id: uuid.UUID
    message: str
