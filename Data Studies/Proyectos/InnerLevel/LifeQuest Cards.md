# LifeQuest Cards - Project Summary

  

## 📖 Overview

**LifeQuest Cards** (formerly InnerLevel) is a gamified productivity application that RPG-ifies real-life tasks. Users play as different character classes (Strategist, Warrior, Creator, Connector, Sage) and complete "Cards" (tasks) to gain XP and level up.

  

## 🏗️ Technical Architecture

  

### 1. Frontend

- **Framework**: React 18 with TypeScript.

- **Build Tool**: Vite.

- **Styling**: Tailwind CSS (v3.3).

- **State Management**: Hybrid approach using React Context API (`AppContext`, `AuthContext`) and React Query (`@tanstack/react-query`).

- **Key Libraries**: `lucide-react` (icons), `framer-motion` (animations), `canvas-confetti`.

  

### 2. Backend (Dual Service)

The project runs two backend services concurrently to handle different responsibilities. Proxies in `vite.config.ts` route frontend requests to the correct service.

  

* **Python AI Engine**

* **Path**: `ai_engine/main.py`

* **Framework**: FastAPI / Uvicorn.

* **Port**: **5000**.

* **Responsibilities**: Handles the core "Mystic Forge" feature via `/api/generate-daily-cards`. Generates RPG-themed cards using OpenAI.

* **Status**: Active.

  

* **Node.js Server (Payments & Utilities)**

* **Path**: `server/server.js`

* **Framework**: Express.js.

* **Port**: **3000**.

* **Responsibilities**: Handles Stripe payments via `/create-checkout-session` and `/webhook`. Also provides secondary OpenAI endpoints (`/api/openai`) for quota tracking.

* **Status**: Active.

  

### 3. Database & Auth

- **Supabase**: Handles all user authentication and persistent data storage (`user_data`, `user_profiles`, `user_usages`, `guilds`).

- **Connection**: Frontend connects directly using `@supabase/supabase-js`.

  

## ⚙️ How It Works (Development Flow)

  

### Service Orchestration

The command `npm run dev:all` uses `concurrently` to start three processes:

1. **Vite Frontend** (`localhost:5173`): The UI your user interacts with.

2. **AI Engine** (`localhost:5000`): Listens for AI generation requests.

3. **Payment Server** (`localhost:3000`): Listens for payment and webhook events.

  

### Key Data Flows

  

#### A. The "Mystic Forge" (AI Generation)

1. User clicks "Forge Cards" in the UI.

2. Frontend (`ArcaneEngine.ts`) sends `POST /api/generate-daily-cards`.

3. **Vite Proxy** forwards this to `http://localhost:5000` (Python).

4. Python backend constructs a prompt and calls OpenAI via `gpt-4o-mini`.

5. Structured RPG card data is returned to the frontend.

  

#### B. Premium Upgrade (Payments)

1. User clicks "Upgrade" in `PaymentModal.tsx`.

2. Frontend sends `POST /create-checkout-session`.

3. **Vite Proxy** forwards this to `http://localhost:3000` (Node.js).

4. Node.js backend interacts with Stripe APIs to create a session.

5. User is redirected to Stripe Checkout.

  

#### C. User Progression

1. All user data (XP, Level, Cards) is stored in Supabase.

2. `AppContext` loads this data on startup.

3. When a card is completed, updates are optimistically applied to the UI and pushed to Supabase tables (`user_data`).

  

## ⚠️ Development Considerations

  

### 1. RPG Transformation

The project utilizes a script (`CLAUDE.md` / `transform-to-rpg.js`) to enforce RPG terminology (e.g., "AI" -> "Mystic Forge", "Generate" -> "Forge"). Ensure new code adheres to this "Magical/Fantasy" naming convention to maintain immersion.

  

### 2. State Migration

The codebase is in the process of migrating from heavy `Context` usage to `React Query` for server state. New data fetching features should use `api.ts` and React Query hooks instead of adding to `AppContext`.

  

## 🚀 Getting Started

1. **Install Dependencies**:

- `npm install` (Root)

- `pip install -r requirements.txt` (in `ai_engine`, if exists)

2. **Environment Variables**:

- Ensure `.env` contains `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `OPENAI_API_KEY`, and `STRIPE_SECRET_KEY`.

3. **Run Development Environment**:

- `npm run dev:all`

- Starts Frontend (5173), Python Backend (5000), and Node Backend (3000).