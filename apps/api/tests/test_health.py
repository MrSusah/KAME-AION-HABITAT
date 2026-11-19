from fastapi.testclient import TestClient

from aion_api.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "kame-aion-habitat-api",
        "version": "0.1.0",
    }


def test_dashboard_summary_reports_unconfigured_services():
    response = client.get("/api/v1/dashboard/summary")

    assert response.status_code == 200

    data = response.json()

    assert data["agents"]["total"] == 0
    assert data["runtime"] == "not_started"
    assert data["integrations"]["database"] == "not_configured"
    assert data["integrations"]["ai_gateway"] == "not_configured"
    assert data["integrations"]["tool_gateway"] == "not_configured"