# 🌟 Vibe-Stack Features Directory

**Vibe-Stack** is not just a boilerplate; it is a comprehensive, AI-first development engine. This document outlines every feature, module, and system built into the template out of the box.



---

## 1. 🤖 Agentic & Vibe Coding Features
Designed specifically for the Antigravity IDE to allow AI to generate features without hallucinating.

* **Rigid Context System:** A dedicated `docs/` folder (`PRD.md`, `TRD.md`, `ARCHITECTURE.md`, `API.md`, `DB_SCHEMA.md`) acts as executable memory for AI agents.
* **Antigravity Skills Integration:** A dedicated `skills/` directory ready to house Python and JS scripts that grant IDE agents local execution capabilities (e.g., DB seeding, file creation).
* **Model Context Protocol (MCP) Ready:** Pre-configured `mcp/` directory to host JSON configurations for Supabase, Filesystem, and GitHub MCP servers.
* **Parameterized Prompts:** A `prompts/` directory for storing reusable text templates (e.g., `generate_crud_endpoint.txt`) to maintain code generation consistency.
* **Agentic Webhooks:** Pre-built `/webhooks` endpoints in the FastAPI backend designed to immediately return a `202 Accepted` and offload heavy AI processing to an asynchronous queue.

---

## 2. ⚡ Backend Features (FastAPI + Python)
The stateless, highly-typed brain of the application.

* **JWT Authentication Flow:** Fully functional `/auth/register` and `/auth/login` endpoints utilizing secure bcrypt password hashing and JSON Web Tokens.
* **Strict Payload Validation:** Pydantic schemas enforce rigid data validation, preventing AI-generated frontend code from breaking the backend with malformed requests.
* **Auto-Generated OpenAPI Docs:** FastAPI automatically generates interactive Swagger documentation at `/docs`, which serves as dynamic context for AI agents.
* **PostgreSQL ORM Integration:** SQLAlchemy set up with a base `users` model, optimized for relational data and ready for Supabase vector embeddings.
* **Automated Schema Migrations:** Alembic is pre-configured in the `backend/alembic/` directory to manage database evolution safely.
* **Health & Connectivity Checks:** A `/health` endpoint to instantly verify API gateway and database status.

---

## 3. 🎨 Frontend Features (NextJS + React)
A lightning-fast, edge-ready client built for easy AI styling.

* **Next.js App Router:** Modern Server-Side Rendering (SSR) and static site generation setup.
* **Tailwind CSS:** Utility-first styling configured out of the box, optimal for AI agents generating inline styles.
* **Shadcn UI Ready:** Pre-configured for unstyled, accessible copy-and-paste components that AI can easily manipulate.
* **Protected Routes System:** Client-side architecture to verify JWT tokens and guard the private Dashboard page from unauthenticated users.
* **User Profile Dashboard:** A boilerplate private dashboard hooked up to the `/users/me` backend endpoint to view and update profile data.
* **Custom API Hooks:** Abstractions in `src/lib/` for seamless, typed communication with the FastAPI backend.

---

## 4. 🔄 Automation & Async Worker Features (n8n)
Offloads complex tasks outside the main request-response cycle.

* **Local n8n Container:** A fully functional n8n instance bundled in the Docker Compose stack for building fair-code workflow automations.
* **Workflow Export Directory:** An `n8n/` folder specifically for committing `.json` workflow exports so teammate IDEs and production servers can sync automations.
* **Asynchronous Job Tracking:** A base `agent_jobs` database schema designed to track the status of long-running n8n/AI tasks (pending, processing, completed).

---

## 5. 🐳 Infrastructure & Developer Experience (DX)
Zero-friction setup designed for 10-minute hackathon starts.

* **1-Click Docker Compose:** `docker-compose.yml` spins up PostgreSQL, FastAPI, NextJS, and n8n simultaneously on an isolated bridge network.
* **Production-Ready Dockerfiles:** Optimized, multi-stage Dockerfiles for both frontend and backend to guarantee environment parity.
* **Automated Bash Scripts:** * `scripts/setup.sh`: Installs all core dependencies.
    * `scripts/run_dev.sh`: Launches local dev servers for rapid UI iteration.
    * `scripts/seed_db.sh`: Drops, migrates, and seeds the database with test data.
* **CI/CD Pipeline Ready:** Prepared `.github/workflows/` directory structure for Pytest, Jest, CodeRabbit AI analysis, and Docker registry pushing.
* **Strict Environment Variable Management:** Clear separation of development (`.env.local`) and production secrets handling.