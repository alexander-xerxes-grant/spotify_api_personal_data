# spotify_api_personal_data/spotify_api.py

"""Client for interacting with the Spotify API.

This module contains classes for handling both authentication and
basic API requests to Spotify's Web API.
It supports getting user authorization, refreshing access tokens,
and retrieving saved tracks for a user.
"""


import base64
import os
from urllib.parse import urlencode

import requests


class SpotifyAuth:
    @staticmethod
    def _get_auth_header() -> dict:
        """Generate the authorisation header"""
        client_id = os.environ.get("SPOTIFY_CLIENT_ID")
        client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

        # Base64 encode the client ID and client secret
        client_creds = base64.b64encode(
            f"{client_id}:{client_secret}".encode()
        ).decode()

        return {
            "Authorization": f"Basic {client_creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

    @staticmethod
    def get_auth_url() -> str:
        params = {
            "client_id": os.environ.get("SPOTIFY_CLIENT_ID"),
            "response_type": "code",
            "redirect_uri": "http://localhost:5000/callback",
            "state": "state",
            "scope": "user-read-private user-read-email user-library-read",
        }
        url = "https://accounts.spotify.com/authorize?" + urlencode(params)

        return url

    @staticmethod
    def get_access_token(code: str) -> tuple[str, str]:
        """Get the Spotify access token."""
        headers = SpotifyAuth._get_auth_header()
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": "http://localhost:5000/callback",
        }

        response = requests.post(
            "https://accounts.spotify.com/api/token", headers=headers, data=data
        )
        response.raise_for_status()
        response_data = response.json()
        access_token = response_data["access_token"]
        refresh_token = response_data["refresh_token"]

        return access_token, refresh_token

    @staticmethod
    def store_refresh_token(refresh_token: str):
        """Store the refresh token in a file."""
        with open("refresh_token.txt", "w") as f:
            f.write(refresh_token)

    @staticmethod
    def refresh_access_token() -> str:
        """Refresh the Spotify access token from the refresh token stored in a file."""
        # Read refresh token from file
        with open("refresh_token.txt") as f:
            refresh_token = f.read().strip()

        headers = SpotifyAuth._get_auth_header()
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        }
        response = requests.post(
            "https://accounts.spotify.com/api/token", headers=headers, data=data
        )
        response.raise_for_status()
        return response.json()["access_token"]


class SpotifyAPI:
    def get_users_saved_tracks(self, access_token, market=None, limit=20, offset=0):
        endpoint = "https://api.spotify.com/v1/me/tracks"

        headers = {"Authorization": f"Bearer {access_token}"}

        params = {"market": market, "limit": limit, "offset": offset}

        response = requests.get(endpoint, headers=headers, params=params)

        if response.status_code == 200:
            response.json()

        else:
            raise Exception(response.status_code, response.text)
