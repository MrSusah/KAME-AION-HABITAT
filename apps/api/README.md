# KAME AION HABITAT API

Backend API for AION Office, built with Python and FastAPI.

## Requirements

- Python 3.12+
- WSL Ubuntu 24.04 (recommended development environment)

## Setup

From the repository root:

```bash
cd apps/api
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Run development server

From `apps/api`:

```bash
.venv/bin/uvicorn aion_api.main:app --app-dir src --host 127.0.0.1 --port 8000 --reload
```

The development API listens on `http://127.0.0.1:8000`.

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/health` | API health check |
| GET | `/api/v1/dashboard/summary` | Initial dashboard summary |

Interactive API documentation is available at `/docs` while the development server is running.

## Tests

From `apps/api`:

```bash
.venv/bin/python -m pytest -v
```

## Current implementation status

- FastAPI application scaffold: implemented.
- Health endpoint: implemented.
- Initial dashboard summary endpoint: implemented.
- PostgreSQL integration: not configured.
- AI Gateway: not configured.
- Tool Gateway: not configured.
- Authentication and authorization: not implemented.

This is a local development scaffold, not a production-ready or remotely accessible service.
