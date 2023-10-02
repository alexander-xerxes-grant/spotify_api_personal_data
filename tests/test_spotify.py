# """Tests for spotify module."""

# import os
# from unittest.mock import patch

# import pytest

# from spotify_api_personal_data.spotify import app


# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client


# def test_get_token(client):
#     response = client.get("/token")
#     assert response.status_code == 200
#     assert "access_token" in response.get_json()


# def test_get_spotify_auth_token_without_env_vars():
#     # Unset the environment variables if they exist
#     with patch.dict(os.environ, {"SPOTIFY_CLIENT_ID": "", "SPOTIFY_CLIENT_SECRET": ""}):
#         with pytest.raises(EnvironmentError):
#             auth.get_spotify_auth_token()


# def test_index(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert "playlists" in response.get_json()
