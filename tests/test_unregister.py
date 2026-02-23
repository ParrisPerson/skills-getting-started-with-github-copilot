def test_unregister_success(client):
    # Arrange
    email = "testuser4@mergington.edu"
    activity = "Drama Club"
    client.post(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["message"].startswith("Removed")

def test_unregister_not_signed_up(client):
    # Arrange
    email = "testuser5@mergington.edu"
    activity = "Drama Club"
    client.delete(f"/activities/{activity}/signup?email={email}")

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "not signed up" in data["detail"]

def test_unregister_nonexistent_activity(client):
    # Arrange
    email = "testuser6@mergington.edu"
    activity = "Nonexistent Club"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Activity not found"
