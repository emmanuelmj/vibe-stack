from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserResponse, UserUpdate
from app.api.deps import get_current_user
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UserResponse)
def update_user_me(
    user_in: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if user_in.full_name is not None:
        current_user.full_name = user_in.full_name
    if user_in.bio is not None:
        current_user.bio = user_in.bio
        
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return current_user
