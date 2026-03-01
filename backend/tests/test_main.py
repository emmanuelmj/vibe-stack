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
    assert response.json()["detail"] == "Not authenticated"

def test_register_user(client):
    response = client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "password": "testpassword",
        "full_name": "Test User"
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_login_user(client):
    # Register first
    client.post("/api/v1/auth/register", json={
        "email": "login@example.com",
        "password": "testpassword",
        "full_name": "Login User"
    })
    
    # Attempt login
    response = client.post("/api/v1/auth/login", json={
        "email": "login@example.com",
        "password": "testpassword"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
