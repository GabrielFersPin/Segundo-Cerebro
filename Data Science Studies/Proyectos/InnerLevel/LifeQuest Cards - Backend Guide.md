
## ☁️ Overview

The backend utilizes a **Microservice-like Hybrid Architecture** running two distinct servers concurrently to handle different responsibilities. This separation allows the use of Python's superior ecosystem for AI/LLM tasks while using Node.js for robust Stripe integration.

  

## 🐍 Service 1: Python AI Engine

**Primary Responsibility**: The "brain" of the application, generating RPG content.

  

* **Location**: `/ai_engine`

* **Entry Point**: `ai_engine/main.py`

* **Port**: `5000`

* **Tech Stack**:

* **Framework**: FastAPI (High performance, easy async).

* **Server**: Uvicorn.

* **AI**: OpenAI API (`gpt-4o-mini`).

  

### Key Endpoints

| Method | Endpoint | Description |

|--------|----------|-------------|

| `POST` | `/api/generate-daily-cards` | Core feature. Receives user context (stats, class, goals) and returns 3 personalized RPG cards. |

| `GET` | `/health` | Health check (`{"status": "ok", "service": "ai-engine-python"}`). |

  

### Workflow

1. Receives JSON payload with User Class, Energy Level, and Time Available.

2. `prompt_builder.py`: Constructs a complex system prompt tailored to the user's RPG class.

3. Calls OpenAI to generate a structured JSON response.

4. Validates and returns the array of "Cards".

  

---

  

## 🟢 Service 2: Node.js Utility Server

**Primary Responsibility**: Infrastructure, payments, and legacy integration.

  

* **Location**: `/server`

* **Entry Point**: `server/server.js`

* **Port**: `3000`

* **Tech Stack**:

* **Framework**: Express.js.

* **Payments**: Stripe SDK.

  

### Key Endpoints

| Method | Endpoint | Description |

|--------|----------|-------------|

| `POST` | `/create-checkout-session` | Initiates a Stripe subscription flow. Returns a checkout URL. |

| `POST` | `/stripe-webhook` | Listens for `checkout.session.completed` events to update user status to Premium in Supabase. |

| `POST` | `/api/openai` | **Legacy/Secondary**. Proxy for direct OpenAI calls if needed (mostly replaced by Python engine). |

| `GET` | `/health` | Health check (`{"status": "OK", ...}`). |

  

### Access Control

- **Supabase Auth Middleware**: Most endpoints (like `/api/openai`) verify the `Authorization: Bearer <token>` header to ensure the user is logged in.

  

---

  

## 🗄️ Database (Supabase)

The backend does **not** maintain its own database. It connects to **Supabase** (PostgreSQL).

  

* **Tables**:

* `user_extensions` / `user_data`: Stores game state (XP, Level).

* `user_profiles`: Stores identity and premium status.

* **Integration**:

* **Frontend**: Connects directly via Client Key (REST/Realtime).

* **Node Server**: Connects via Service Role Key (for admin tasks like Webhook processing).

  

## 🔐 Environment Variables

Review `.env` in the root directory.

  

| Variable | Service | Purpose |

|----------|---------|---------|

| `OPENAI_API_KEY` | Python & Node | Authentication with OpenAI. |

| `STRIPE_SECRET_KEY` | Node | Authentication with Stripe. |

| `SUPABASE_URL` | Node | Database connection URL. |

| `SUPABASE_SERVICE_ROLE_KEY` | Node | Admin access for webhooks (bypassing RLS). |

  

## 🛠️ Development & Deployment

* **Local Run**: `npm run dev:all` starts both servers using `concurrently`.

* **Deployment**:

* Currently configured for local development.

* For production, these would likely be deployed as two separate services (e.g., two Railway services or Render webservices) with the Frontend deployed to Vercel/Netlify.