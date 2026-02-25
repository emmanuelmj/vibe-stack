# System Architecture Documentation
**Project:** Vibe-Stack Base Template
**Version:** 1.0.0
**Context:** This document outlines the decoupled, highly scalable architecture of Vibe-Stack. AI agents must use this document to understand service separation, data flow, and where new features should be implemented.



## 1. High-Level Architecture
Vibe-Stack assumes a strict separation of concerns. The architecture is designed for both rapid startup MVPs and enterprise production scalability. 

### 1.1. Core Components
- **Client (Frontend):** NextJS application deployed on a CDN/Edge network. It is strictly responsible for UI, routing, and client-side state.
- **API Gateway (Backend):** FastAPI application running in a Docker container. It acts as the stateless brain of the operation, handling business logic, input validation (via Pydantic), and authorization.
- **Database Layer:** PostgreSQL (via Supabase) handling persistent storage, relational data, and vector embeddings.
- **Automation / AI Worker Layer:** n8n running in a separate container to handle asynchronous workflows, webhooks, and third-party AI integrations.

## 2. Service Separation & Data Flow
Agents must respect these flow paradigms when designing new features.

### 2.1. Synchronous Flow (Standard CRUD)
Used for immediate user actions (e.g., logging in, fetching profile data).
1. User interacts with NextJS UI.
2. NextJS executes an API call to the FastAPI Gateway (`/api/v1/...`).
3. FastAPI validates the request payload using Pydantic.
4. FastAPI queries PostgreSQL via SQLAlchemy.
5. FastAPI returns the response (e.g., JWT token or JSON payload).
6. NextJS updates the client state.

### 2.2. Asynchronous Flow (Heavy Compute / AI)
Used for non-blocking operations (e.g., Image processing like Plant Disease Detection CNN, generating LLM summaries).
1. User uploads data/image via NextJS.
2. FastAPI stores the raw file in Supabase Storage.
3. FastAPI publishes an event payload to a queue/webhook and immediately returns a `202 Accepted` to the client.
4. n8n picks up the webhook event.
5. n8n orchestrates external API calls (e.g., OpenAI, Groq) to process the data.
6. n8n writes the processed result back to the PostgreSQL database.
7. Frontend polls or receives a WebSocket update with the final result.

## 3. Scalability Mechanisms
By enforcing stateless backend services (FastAPI) and utilizing containerization, the architecture is designed to scale horizontally.
- **Backend:** Multiple FastAPI instances can be spun up behind a load balancer.
- **Database Bottlenecks:** Mitigated by standard PostgreSQL indexing and connection pooling (e.g., PgBouncer), which must be configured in production deployments.

## 4. Agentic Architecture (Vibe Coding)
Vibe-Stack's development environment is an architecture in itself, built for high-bandwidth context transfer.

### 4.1. The AI Context System
- **Human Architect:** Acts as the API Gateway between agents, determining the DB schemas and high-level requirements.
- **IDE Agents:** Utilize Antigravity Skills (located in `skills/`) to execute file generation and local terminal commands autonomously.
- **Model Context Protocol (MCP):** Configured in the `mcp/` directory. Provides secure access for AI models to query the local PostgreSQL database, read the `docs/` directory, and inspect the filesystem without human copy-pasting.

### 4.2. Tooling & Skills Flow
- **`prompts/`:** Contains parameterized templates (e.g., `generate_crud_endpoint.txt`) to maintain generation consistency.
- **`skills/`:** Contains Python or JS scripts that give agents specific local abilities (e.g., `seed_test_data.py`, `trigger_n8n_workflow.py`).

## 5. Directory Mapping to Architecture
When an AI agent modifies a system layer, it must only modify files in the corresponding directory:
- **Frontend Changes:** `frontend/src/`
- **Backend Logic:** `backend/app/api/` and `backend/app/core/`
- **Database Schemas:** `backend/app/models/` and `docs/DB_SCHEMA.md`
- **Infrastructure:** `docker/` and `scripts/`