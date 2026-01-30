## 🖥️ Overview

The frontend is a **Single Page Application (SPA)** built with React 18, designed to provide an immersive, RPG-themed productivity experience. It uses **Vite** for fast development and building.

  

## 🛠️ Technology Stack

- **Core**: React 18, TypeScript.

- **Build**: Vite.

- **Styling**: Tailwind CSS v3.3 (Utility-first), CSS Modules for specific animations.

- **Icons**: `lucide-react`, `@fontsource` (Pixel fonts: 'Press Start 2P', 'VT323').

- **State Management**:

- **Global/UI State**: React Context (`AppContext`, `AuthContext`).

- **Server State**: React Query (`@tanstack/react-query`) - *In adoption*.

  

## 📂 Architecture & Directory Structure (`/src`)

  

### Key Directories

| Directory | Purpose |

|-----------|---------|

| `components/` | Reusable UI blocks. Organized by feature (e.g., `cards/`, `dashboard/`). |

| `pages/` | Main route views (`LandingPage`, `Dashboard`, `Profile`). |

| `context/` | Global providers. `AppContext.tsx` is the massive central store (refactor target). |

| `services/` | API interaction layer. Separates logic from UI. |

| `hooks/` | Custom hooks (e.g., `useAuth`, `useSound`, `useToast`). |

| `assets/` | Static images, sounds, and global CSS. |

| `types/` | TypeScript interfaces shared across the app. |

  

## 🧠 State Management Strategy

  

### 1. AppContext (Legacy/Current)

Currently, `AppContext` handles most data:

- **User Data**: XP, Level, Gold, Class.

- **Inventory**: Lists of active and collected cards.

- **Logic**: Functions like `completeCard`, `addGold` are defined here.

> **Note**: This is being migrated to React Query for better performance and caching.

  

### 2. React Query (Target)

Used for asynchronous data fetching (Supabase operations).

- **Hooks**: `useQuery` for fetching user profile, `useMutation` for updates.

- **Services**: `src/services/api.ts` contains the query implementations.

  

## 🔌 API Integration (`src/services/`)

  

The frontend never connects to the backend servers directly for logic; it uses the **Vite Proxy** to avoid CORS issues.

  

### 1. ArcaneEngine (`arcaneEngine.ts`)

Handles "Mystic Forge" (AI) operations.

- **Function**: `generateDailyCards(userContext)`

- **Flow**: Frontend -> `POST /api/generate-daily-cards` -> **Vite Proxy** -> **Python Backend (5000)**.

  

### 2. Payment Integration

- **Component**: `PaymentModal.tsx`

- **Flow**: User clicks Upgrade -> `POST /create-checkout-session` -> **Vite Proxy** -> **Node Backend (3000)**.

  

### 3. Database (Supabase)

- **Direct Connection**: The frontend uses `@supabase/supabase-js` to speak directly to the database for CRUD operations on `user_data`.

- **Security**: Row Level Security (RLS) policies on the database ensure users can only access their own data.

  

## 🎨 Design System

The app follows a "Techno-Magical" pixel art aesthetic.

- **Glassmorphism**: Heavy use of `bg-opacity-10`, `backdrop-blur`.

- **Neon Accents**: `border-purple-500`, `shadow-[0_0_15px_rgba(...)]`.

- **Responsiveness**: Mobile-first design using Tailwind breakpoints (`md:`, `lg:`).

  

## 🚀 Development Workflow

1. **Run**: `npm run dev` (Usually via `npm run dev:all`).

2. **Lint**: `npm run lint`.

3. **Build**: `npm run build` (Outputs to `dist/`).