from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from svix.webhooks import Webhook, WebhookVerificationError

from app.core.database import get_db
from app.models import User
from app.core.config import settings

router = APIRouter(prefix="/webhooks", tags=["webhooks"])

@router.post("/clerk")
async def clerk_webhook(request: Request, db: Session = Depends(get_db)):
    if not settings.CLERK_WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="CLERK_WEBHOOK_SECRET is not configured")

    payload = await request.body()
    headers = request.headers

    svix_id = headers.get("svix-id")
    svix_timestamp = headers.get("svix-timestamp")
    svix_signature = headers.get("svix-signature")
    
    if not svix_id or not svix_timestamp or not svix_signature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Missing required Svix headers"
        )

    wh = Webhook(settings.CLERK_WEBHOOK_SECRET)
    try:
        event = wh.verify(payload, headers)
    except WebhookVerificationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f"Invalid webhook signature: {str(e)}"
        )
        
    event_type = event.get("type", "")
    data = event.get("data", {})
    
    if event_type == "user.created":
        clerk_id = data.get("id")
        email_addresses = data.get("email_addresses", [])
        
        email = None
        if email_addresses:
            email = email_addresses[0].get("email_address")
            
        if not clerk_id or not email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Missing essential user data from Clerk payload"
            )
            
        first_name = data.get("first_name") or ""
        last_name = data.get("last_name") or ""
        full_name = f"{first_name} {last_name}".strip()
        
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
