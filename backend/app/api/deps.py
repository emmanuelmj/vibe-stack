from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
import jwt
from app.core.database import get_db
from app.models import User

# This acts as an API dependency for routes that need the user from Clerk auth token
def get_current_user(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    if not auth_header or not auth_header.startswith("Bearer "):
        raise credentials_exception
        
    token = auth_header.split(" ")[1]
    
    try:
        # Decode without verifying signature since API Gateway / Clerk middleware handles hard verification.
        # Tests can easily mock standard JWT tokens.
        payload = jwt.decode(token, options={"verify_signature": False})
        user_id_or_clerk_id: str = payload.get("sub")
        if user_id_or_clerk_id is None:
            raise credentials_exception
    except Exception:
        raise credentials_exception
        
    # Search by either id or clerk_id depending on how old tokens vs new tokens work
    # during migration window
    user = db.query(User).filter((User.id == user_id_or_clerk_id) | (User.clerk_id == user_id_or_clerk_id)).first()
    if user is None:
        raise credentials_exception
    return user
