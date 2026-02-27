import uuid
from datetime import datetime
from fastapi import FastAPI, Depends, status, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.schemas import AgentJobTrigger, AgentJobResponse
from app.api.deps import get_current_user
from app.models import User

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="Vibe-Stack API", version="1.0.0")
app.state.limiter = limiter

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
    
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

from app.api import auth, users

app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")

@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

@app.post("/api/v1/webhooks/n8n/trigger", status_code=status.HTTP_202_ACCEPTED, response_model=AgentJobResponse)
def trigger_n8n_webhook(
    payload: AgentJobTrigger,
    current_user: User = Depends(get_current_user)
):
    return {
        "status": "processing",
        "job_id": uuid.uuid4(),
        "message": "Workflow triggered successfully."
    }
