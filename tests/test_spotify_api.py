import base64
import os

import requests

from spotify_api_personal_data.spotify_api import SpotifyAuth


class TestSpotifyAuth:
    def test_get_auth_header_structure(self, mocker):
        # Arrange
        mocker.patch.dict(
            os.environ,
            {
                "SPOTIFY_CLIENT_ID": "test_client_id",
                "SPOTIFY_CLIENT_SECRET": "test_client_secret",
            },
        )

        # Act
        auth_header = SpotifyAuth._get_auth_header()

        # Assert
        assert "Authorization" in auth_header
        assert "Content-Type" in auth_header
        assert auth_header["Authorization"].startswith("Basic ")
        assert auth_header["Content-Type"] == "application/x-www-form-urlencoded"

    def test_get_auth_header_base64_encoding(self, mocker):
        # Arrange
        mocker.patch.dict(
            os.environ,
            {
                "SPOTIFY_CLIENT_ID": "test_client_id",
                "SPOTIFY_CLIENT_SECRET": "test_client_secret",
            },
        )

        # Act
        auth_header = SpotifyAuth._get_auth_header()

        # Assert
        encoded_creds = auth_header["Authorization"].split(" ")[1]
        decoded_creds = base64.b64decode(encoded_creds).decode()
        assert decoded_creds == "test_client_id:test_client_secret"

    def test_get_auth_url(self, mocker):
        # Arrange
        client_id = "test_client_id"
        mocker.patch.dict(
            os.environ,
            {"SPOTIFY_CLIENT_ID": client_id},
        )
        expected_url = (
            "https://accounts.spotify.com/authorize?"
            "client_id=test_client_id&response_type=code"
            "&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback&state=state"
            "&scope=user-read-private+user-read-email+user-library-read"
        )

        # Act
        auth_url = SpotifyAuth.get_auth_url()

        # Assert
        assert auth_url == expected_url

    def test_get_access_token(self, mocker):
        # Arrange
        code = "test_code"
        access_token = "test_access_token"
        refresh_token = "test_refresh_token"
        mocker.patch("requests.post").return_value.json.return_value = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        # Act
        result = SpotifyAuth.get_access_token(code)

        # Assert
        assert result == (access_token, refresh_token)
        requests.post.assert_called_once_with(
            "https://accounts.spotify.com/api/token",
            headers=SpotifyAuth._get_auth_header(),
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": "http://localhost:5000/callback",
            },
        )

    def test_store_access_token(self, mocker):
        # Arrange
        refresh_token = "test_refresh_token"
        mock_open = mocker.patch("builtins.open", mocker.mock_open())

        # Act
        SpotifyAuth.store_refresh_token(refresh_token)

        # Assert
        mock_open.assert_called_once_with("refresh_token.txt", "w")
        mock_open().write.assert_called_once_with(refresh_token)
