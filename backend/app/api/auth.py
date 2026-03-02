from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from svix.webhooks import Webhook, WebhookVerificationError
import os

from app.core.database import get_db
from app.models import User
from app.core.config import settings
from app.main import limiter

router = APIRouter(prefix="/auth", tags=["auth"])

CLERK_WEBHOOK_SECRET = os.getenv("CLERK_WEBHOOK_SECRET", "")

@router.post("/webhooks/clerk")
async def clerk_webhook(request: Request, db: Session = Depends(get_db)):
    """
    Handle Clerk webhooks, specifically user.created.
    Creates a new user record in the local database when they sign up via Clerk.
    """
    if not CLERK_WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="CLERK_WEBHOOK_SECRET is not configured")

    # Get the raw body for Svix signature verification
    payload = await request.body()
    headers = request.headers

    # Extract Svix headers
    svix_id = headers.get("svix-id")
    svix_timestamp = headers.get("svix-timestamp")
    svix_signature = headers.get("svix-signature")
    
    if not svix_id or not svix_timestamp or not svix_signature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Missing required Svix headers"
        )

    wh = Webhook(CLERK_WEBHOOK_SECRET)
    try:
        # Verify the payload signature
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Invalid webhook signature: {str(e)}"
        )
        
    # Process the verified event
    event_type = event.get("type", "")
    data = event.get("data", {})
    
    if event_type == "user.created":
        clerk_id = data.get("id")
        
        # Match the primary email address
        primary_email_id = data.get("primary_email_address_id")
        email_addresses = data.get("email_addresses", [])
        email = None
        for email_obj in email_addresses:
            if email_obj.get("id") == primary_email_id:
                email = email_obj.get("email_address")
                break
                
        # Fallback to the first email if primary not matched
        if not email and email_addresses:
            email = email_addresses[0].get("email_address")
            
        if not clerk_id or not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Missing essential user data from Clerk payload"
            )
            
        first_name = data.get("first_name") or ""
        last_name = data.get("last_name") or ""
        full_name = f"{first_name} {last_name}".strip()
        
        # Check if user already exists (by clerk_id or email)
        existing_user = db.query(User).filter(
            (User.clerk_id == clerk_id) | (User.email == email)
        ).first()
        
        if not existing_user:
            new_user = User(
                clerk_id=clerk_id,
                email=email,
                full_name=full_name if full_name else None
            )
            db.add(new_user)
            db.commit()
            
    return {"status": "success"}
