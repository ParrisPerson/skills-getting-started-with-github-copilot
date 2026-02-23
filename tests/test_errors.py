def test_signup_missing_email(client):
    # Arrange
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup")

    # Assert
    assert response.status_code == 422  # Unprocessable Entity (missing required query param)

def test_unregister_missing_email(client):
    # Arrange
    activity = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity}/signup")

    # Assert
    assert response.status_code == 422

def test_method_not_allowed(client):
    # Arrange
    activity = "Chess Club"
    email = "testuser7@mergington.edu"

    # Act
    response = client.put(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 405  # Method Not Allowed
