import base64
import os

import pytest

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
