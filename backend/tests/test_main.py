def test_health_check(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["database"] == "connected"

def test_trigger_webhook_unauthorized(client):
    response = client.post(
        "/api/v1/webhooks/n8n/trigger",
        json={"workflow_id": "test", "payload_data": {}}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

def test_clerk_webhook_missing_headers(client):
    response = client.post("/api/v1/webhooks/clerk", json={
        "type": "user.created",
        "data": {"id": "test_clerk_id"}
    })
    # Should fail because of missing svix headers
    assert response.status_code == 400
    assert "Missing required Svix headers" in response.json()["detail"]
