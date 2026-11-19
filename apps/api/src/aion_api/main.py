from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="KAME AION HABITAT API",
    description="Backend API for AION Office.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)


@app.get("/api/v1/health", tags=["System"])
async def health():
    return {
        "status": "ok",
        "service": "kame-aion-habitat-api",
        "version": app.version,
    }


@app.get("/api/v1/dashboard/summary", tags=["Dashboard"])
async def dashboard_summary():
    return {
        "agents": {
            "total": 0,
            "active": 0,
        },
        "tasks": {
            "running": 0,
        },
        "approvals": {
            "pending": 0,
        },
        "runtime": "not_started",
        "integrations": {
            "database": "not_configured",
            "ai_gateway": "not_configured",
            "tool_gateway": "not_configured",
        },
    }
