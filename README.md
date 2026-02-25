<h1 align="center">⚡ Vibe-Stack</h1>

<div align="center">
  <h3>The AI-First Hackathon Engine & Professional Template Repository</h3>
  <p>Engineered for high-bandwidth context transfer between a human architect and large language models within the Antigravity IDE.</p>

  <p>
    <a href="https://github.com/emmanuelmj/vibe-stack/stargazers"><img src="https://img.shields.io/github/stars/emmanuelmj/vibe-stack?style=for-the-badge&color=yellow" alt="Stars"></a>
    <a href="https://github.com/emmanuelmj/vibe-stack/network/members"><img src="https://img.shields.io/github/forks/emmanuelmj/vibe-stack?style=for-the-badge&color=blue" alt="Forks"></a>
    <a href="https://github.com/emmanuelmj/vibe-stack/issues"><img src="https://img.shields.io/github/issues/emmanuelmj/vibe-stack?style=for-the-badge&color=red" alt="Issues"></a>
    <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
    <img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge" alt="License">
  </p>
</div>

---

## The Vision: "Vibe Coding"

Traditional frameworks are built for human hands typing every character. **Vibe-Stack** is built for AI agents. 

Vibe Coding is a paradigm shift where the developer acts as the architect and reviewer, while AI agents handle boilerplate, CRUD operations, and UI generation. To prevent AI hallucinations, Vibe-Stack enforces a rigid **Database-First Development Approach**:

> **Docs → Database → Backend → Frontend → Agents → Automation → Deployment**

By treating markdown files (`PRD.md`, `DB_SCHEMA.md`) as executable context, Vibe-Stack provides a deterministic environment that bridges the gap between rapid, competitive hackathon prototyping and scalable, production-grade applications.

---

## Architecture & Tech Stack

Vibe-Stack assumes a decoupled, highly scalable architecture. Code that works on your local Docker setup works identically in production.

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Next.js (App Router), Tailwind, Shadcn | SSR, static generation, and inline AI styling. |
| **Backend** | FastAPI, Python, SQLAlchemy | Async API gateway, rigid Pydantic typing for AI integrity. |
| **Database** | PostgreSQL (Supabase ready) | Relational data and vector storage. Alembic for migrations. |
| **Agentic Layer**| Antigravity Skills, MCP, n8n | Autonomous task execution, local IDE skills, and async workflows. |
| **Infrastructure**| Docker & Docker Compose | Guaranteed environment parity and single-command startup. |

---

## The 10-Minute Hackathon Quickstart

Battle-tested for competitive hackathons. Go from a blank canvas to a running full-stack application instantly.

### 1. Clone the Template

```bash
git clone https://github.com/emmanuelmj/vibe-stack.git my-hackathon-project
cd my-hackathon-project
```

### 2. Run the Setup Automation

*(Assumes Docker is running)*

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### 3. Spin Up the Stack

```bash
docker compose -f docker/docker-compose.yml up -d
```

Your PostgreSQL database, FastAPI backend (`localhost:8000/docs`), Next.js frontend (`localhost:3000`), and n8n instance (`localhost:5678`) are now live.

---

## Antigravity IDE Integration

Vibe-Stack is uniquely optimized for the Antigravity IDE. Instead of manually executing commands, you can orchestrate development using your agent skills.

Ensure you have linked the Antigravity Awesome Skills repository to your environment.

### Example IDE Prompts:

- 🧠 **"Read `docs/DB_SCHEMA.md`. Use the file-generation skill to create the SQLAlchemy models in the backend."**
- 🛠️ **"Use the terminal execution skill to run `alembic upgrade head`."**
- 🌐 **"Use the MCP testing skill to verify the filesystem server can read `docs/API.md`, then generate the Next.js React hooks for those endpoints."**

---

## Directory Blueprint

A predictable structure prevents AI pathing errors. Keep context where the AI expects it.

```text
vibe-stack/
├── docs/               # 🧠 The Brain: PRD, Architecture, API, & Schema rules
├── backend/            # ⚙️ FastAPI app, Pydantic schemas, Alembic migrations
├── frontend/           # 🎨 Next.js app, Shadcn components, Tailwind
├── docker/             # 🐳 Container configurations (dev & prod)
├── scripts/            # 📜 Bash automation (setup, DB seeding)
├── n8n/                # 🤖 Exported async workflows (JSON)
├── agents/             # 🕵️ Custom agent orchestration scripts
├── skills/             # 🪄 Reusable Antigravity IDE capabilities
├── prompts/            # 📝 Parameterized template prompts
└── mcp/                # 🔌 Model Context Protocol server configs
```

---

## Contributing & Open Source

This repository is designed as a foundational blueprint for open-source clubs, developer communities, and hackathon teams. We welcome contributions that improve the agentic workflow or add new reusable AI skills!

### How to Contribute

1. **Fork the Project**
2. **Create your Feature Branch:** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes:** (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push to the Branch:** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

<br>

<div align="center">
  <p>Built with ☕ and AI for the next generation of software architects.</p>
</div>