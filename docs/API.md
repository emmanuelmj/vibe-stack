# API Specifications (API.md)
**Project:** Vibe-Stack Base Template
**Version:** 1.0.0
**Context:** This document is the strict source of truth for all backend endpoints. AI agents generating FastAPI routers or NextJS fetch hooks MUST strictly adhere to the paths, methods, and payload structures defined here.



## 1. Global API Configuration
- **Base URL (Local):** `http://localhost:8000/api/v1`
- **Content-Type:** `application/json`
- **Authentication:** JWT Bearer Token. Secured endpoints must include the header: `Authorization: Bearer <token>`

---

## 2. Health & System
Endpoints to verify backend status and database connectivity.

### `GET /health`
- **Description:** Verifies that the API gateway is running and successfully connected to the PostgreSQL database.
- **Auth Required:** No
- **Response (200 OK):**
  ```json
  {
    "status": "healthy",
    "database": "connected",
    "timestamp": "2026-02-25T12:00:00Z"
  }
3. Authentication Module (/auth)
Handles user registration, login, and session token generation.

POST /auth/register
Description: Creates a new user account and hashes the password securely.

Auth Required: No

Request Body:

JSON
{
  "email": "user@example.com",
  "password": "securepassword123",
  "full_name": "John Doe"
}
Response (201 Created):

JSON
{
  "id": "uuid-v4",
  "email": "user@example.com",
  "full_name": "John Doe",
  "created_at": "2026-02-25T12:00:00Z"
}
POST /auth/login
Description: Authenticates a user and returns a JWT access token. (Note: FastAPI typically uses form-data for OAuth2 strictly, but for Vibe-Stack JSON is preferred for simpler AI consumption).

Auth Required: No

Request Body:

JSON
{
  "email": "user@example.com",
  "password": "securepassword123"
}
Response (200 OK):

JSON
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR...",
  "token_type": "bearer"
}
4. Users Module (/users)
Handles profile retrieval and updates for the authenticated user.

GET /users/me
Description: Retrieves the profile information of the currently authenticated user.

Auth Required: Yes

Response (200 OK):

JSON
{
  "id": "uuid-v4",
  "email": "user@example.com",
  "full_name": "John Doe",
  "bio": "Software Engineer",
  "is_active": true
}
PUT /users/me
Description: Updates the profile information of the currently authenticated user.

Auth Required: Yes

Request Body: (All fields optional)

JSON
{
  "full_name": "Johnathan Doe",
  "bio": "Senior Software Architect"
}
Response (200 OK):

JSON
{
  "id": "uuid-v4",
  "email": "user@example.com",
  "full_name": "Johnathan Doe",
  "bio": "Senior Software Architect",
  "is_active": true
}
5. Agentic Webhooks (/webhooks)
Endpoints specifically designed to receive payloads from or trigger n8n asynchronous workflows.

POST /webhooks/n8n/trigger
Description: Generic endpoint for the frontend to request a heavy compute/AI task. FastAPI immediately returns a 202 and forwards the payload to the local n8n container.

Auth Required: Yes

Request Body:

JSON
{
  "workflow_id": "document-summary",
  "payload_data": {
    "text": "Extremely long text to be summarized..."
  }
}
Response (202 Accepted):

JSON
{
  "status": "processing",
  "job_id": "job-uuid-v4",
  "message": "Workflow triggered successfully."
}

***

Let me know when this is saved in your project, and I will generate the final and most foundational file: **`DB_SCHEMA.md`**.