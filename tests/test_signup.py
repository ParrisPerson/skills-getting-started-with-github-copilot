def test_signup_success(client):
    # Arrange
    email = "testuser@mergington.edu"
    activity = "Art Club"
    # Ensure clean state
    client.delete(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["message"].startswith("Signed up")
    # Clean up
    client.delete(f"/activities/{activity}/signup?email={email}")

def test_signup_duplicate(client):
    # Arrange
    email = "testuser2@mergington.edu"
    activity = "Art Club"
    client.delete(f"/activities/{activity}/signup?email={email}")
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]
    # Clean up
    client.delete(f"/activities/{activity}/signup?email={email}")

def test_signup_nonexistent_activity(client):
    # Arrange
    email = "testuser3@mergington.edu"
    activity = "Nonexistent Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Activity not found"
