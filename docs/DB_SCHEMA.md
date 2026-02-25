# Database Schema (DB_SCHEMA.md)
**Project:** Vibe-Stack Base Template
**Version:** 1.0.0
**Context:** This document is the absolute source of truth for the PostgreSQL database structure. AI agents must generate SQLAlchemy models (`models.py`) and Alembic migrations strictly based on these tables. Do not hallucinate additional columns unless instructed by the human architect.

## 1. Global Database Conventions
- **Database Engine:** PostgreSQL
- **Primary Keys:** UUID v4 (Standardized across all tables)
- **Timestamps:** Every table must include `created_at` and `updated_at` (timestamp with time zone, defaulting to `now()`).
- **Naming Convention:** `snake_case` for all table names and column names.

---

## 2. Core Tables

### Table: `users`
**Purpose:** Stores core user authentication and profile data. 
**Relationships:** Base table. (Will have One-to-Many relationships as hackathon features are added).

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID | PRIMARY KEY | Unique identifier for the user. |
| `email` | VARCHAR(255) | UNIQUE, NOT NULL | User's email address (used for login). |
| `hashed_password` | VARCHAR(255) | NOT NULL | Bcrypt hashed password. |
| `full_name` | VARCHAR(100) | NULLABLE | The user's displayed name. |
| `bio` | TEXT | NULLABLE | A short biography for the user's profile. |
| `is_active` | BOOLEAN | DEFAULT TRUE | Used for soft-deleting or banning users. |
| `is_superuser` | BOOLEAN | DEFAULT FALSE | Grants admin dashboard access. |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Record creation timestamp. |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Record update timestamp. |

---

### Table: `agent_jobs` (Optional/Agentic Base)
**Purpose:** Tracks asynchronous tasks sent to n8n or external AI APIs to prevent request timeouts on the frontend.
**Relationships:** Belongs to `users` (Foreign Key).

| Column Name | Data Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | UUID | PRIMARY KEY | Unique identifier for the job. |
| `user_id` | UUID | FOREIGN KEY (`users.id`) | The user who triggered the job. |
| `workflow_id` | VARCHAR(100) | NOT NULL | Identifies which n8n workflow is handling this. |
| `status` | VARCHAR(50) | DEFAULT 'pending' | Enum: `pending`, `processing`, `completed`, `failed`. |
| `result_payload`| JSONB | NULLABLE | Stores the output from the AI/n8n workflow. |
| `created_at` | TIMESTAMPTZ | DEFAULT NOW() | Record creation timestamp. |
| `updated_at` | TIMESTAMPTZ | DEFAULT NOW() | Record update timestamp. |

---

## 3. Extension Guidelines for AI Agents
When the human architect requests a new feature (e.g., "Add a posts table"):
1. The AI must first append the new table definition to this `DB_SCHEMA.md` file.
2. The AI must specify the Foreign Key relationships explicitly.
3. Once the human approves the schema update, the AI will generate the Alembic revision and SQLAlchemy models.