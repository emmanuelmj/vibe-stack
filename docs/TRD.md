# Technical Requirements Document (TRD)
**Project:** Vibe-Stack Base Template
**Version:** 1.0.0
**Context:** This document defines the technological boundaries, architectural decisions, and infrastructure requirements for the Vibe-Stack repository. AI agents must strictly adhere to these constraints to prevent hallucinations and ensure production parity.

## 1. System Architecture
Vibe-Stack assumes a decoupled, highly scalable architecture suitable for both startup MVPs and enterprise production.



- **Client (Frontend):** Deployed on a CDN/Edge network. Handles UI, routing, and client-side state.
- **API Gateway (Backend):** Stateless application running in a container. Handles business logic, input validation, and authorization.
- **Database:** Relational data and vector storage handling persistent state.
- **Asynchronous Worker Layer:** Manages AI integrations, webhooks, and heavy compute tasks outside the main request-response cycle.

## 2. Technology Stack

### 2.1. Backend
- **Framework:** FastAPI (Python). Chosen for native async support, strict Python type hints, and automatic OpenAPI (Swagger) documentation which acts as the ultimate context mechanism for AI.
- **ORM & Migrations:** SQLAlchemy for database interactions. Alembic for schema migrations.
- **Validation:** Pydantic. Acts as a rigid boundary to prevent AI-generated frontend code from breaking the backend with malformed payloads.
- **Performance Extension (Optional):** Go modules communicating via gRPC or REST for hyper-performance microservices.

### 2.2. Frontend
- **Framework:** Next.js (App Router) for Server-Side Rendering (SSR) and static generation.
- **Styling:** Tailwind CSS. Utility-first CSS is optimal for AI agents styling components inline without managing separate files.
- **Components:** Shadcn UI. Unstyled, accessible, copy-and-paste components that AI can directly manipulate without fighting rigid third-party libraries.

### 2.3. Database & Storage
- **Primary Database:** PostgreSQL (via Supabase). Standard SQL and SQLAlchemy are preferred over the Supabase JS client for core backend logic to maintain portability.
- **Authentication:** Managed via Supabase Auth flows and JWT generation to offload security risks from AI-generated code.
- **Object Storage:** S3-compatible storage for user uploads.

### 2.4. Agentic & Automation Layer
- **Workflow Automation:** n8n. Used for building asynchronous AI workflows (document summarization, queue processing) without polluting the core codebase.
- **AI Infrastructure:** Cloud-based frontier models (OpenAI GPT-4o, Anthropic Claude 3.5 Sonnet, Gemini). Selected for their massive context windows (200k+ tokens) required for full-stack Vibe Coding.
- **Local Tooling:** Antigravity IDE integration utilizing modular "skills" and Model Context Protocol (MCP) servers (Supabase, Filesystem, GitHub, Docs).

## 3. Deployment & Infrastructure
Vibe-Stack enforces zero-friction deployment. Code that works on a local Docker setup must work exactly the same in production.

### 3.1. Containerization
- Every service (Frontend, Backend, DB, n8n) is containerized via Docker and orchestrated with Docker Compose. This ensures environment parity and reliable AI-generated `Dockerfile` dependencies.

### 3.2. Hosting Options
- **Development:** Local Docker via `docker-compose.yml`.
- **MVP Production:** PaaS (Railway / Render / Fly.io).
- **Enterprise Production:** VPS / Cloud VM (AWS EC2, DigitalOcean) with Docker Swarm or Kubernetes.

### 3.3. Production Configuration
- **Application Servers:** NextJS runs as a standalone output. FastAPI is served via Uvicorn behind a Gunicorn process manager.
- **Reverse Proxy:** Nginx or Traefik handles SSL termination and routing.
- **Environment Variables:** Strictly separated. `.env.local` for dev. Secrets (API keys) must be accessed via `os.getenv()` or `process.env`. Never commit `.env` files.

### 3.4. CI/CD Pipeline
GitHub Actions workflow (`.github/workflows/deploy.yml`) containing:
1. Pytest (Backend) and Jest (Frontend) suites.
2. CodeRabbit AI code analysis.
3. Automated Docker image builds upon passing tests.
4. Container registry push and production webhook triggers.

## 4. Environment & Development Constraints
- **Vibe Coding Git Workflow:** Create a new branch for *every* AI prompt session. If the AI hallucinates, run `git reset --hard` or delete the branch.
- **Testing Mandate:** AI agents must write tests *before* or *alongside* the implementation.