# KAME AION HABITAT - AION Office

Frontend application for KAME AION HABITAT.

AION Office is the web interface for the supervised-autonomy AI Agent Office.

## Technology

- React
- TypeScript
- Vite
- ESLint

## Requirements

- Node.js
- npm
- KAME AION HABITAT API

## Development

Run `npm install` to install dependencies.

Run `npm run dev` to start the development server.

Local address: http://127.0.0.1:5173/

## Backend Connection

The frontend communicates with the API through `/api`.

Vite proxies development requests to http://127.0.0.1:8000.

The FastAPI backend must run separately.

## Commands

- `npm run dev` - Start development server
- `npm run build` - TypeScript check and production build
- `npm run lint` - Run ESLint
- `npm run preview` - Preview production build

## Implemented

- AION Office dashboard
- Responsive dashboard layout
- Dashboard summary API integration
- API connection status
- Virtual Office visual preview
- Development API proxy

## Not Yet Implemented

- Authentication and authorization
- Agent runtime and management
- Project and task execution
- AI Gateway and Tool Gateway
- Approval workflows
- PostgreSQL integration
- Persistent application data
- Interactive 2D Virtual Office

## Security

The development server binds to 127.0.0.1.

The Vite proxy is for development only.

Authentication, authorization, and security enforcement belong to the backend.