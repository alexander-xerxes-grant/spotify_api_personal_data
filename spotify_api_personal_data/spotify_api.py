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


import base64
import os
from typing import Tuple
import requests
from urllib.parse import urlencode


class SpotifyAuth:
    """
    A class representing the Spotify API Authentication.

    Attributes:
        None

    Methods:
        _get_auth_header() -> dict: Generates the authorisation header.
        get_auth_url() -> str: Generates the authorisation url.
        get_access_token(code: str) -> Tuple[str, str]: Get the Spotify access token.
        store_refresh_token(refresh_token: str) -> None: Store the refresh token in a file.
        refresh_access_token() -> str: Refresh the Spotify access token from the refresh token stored in a file.
    """
    
    @staticmethod
    def _get_auth_header() -> dict:
        """
        Generate the authorization header.

        Returns:
            A dictionary containing the authorization header.
        """
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
        """
        Generate the authorization url.

        Returns:
            A string containing the authorization url.

        Example:
            >>> from spotify_api_personal_data.spotify_api import SpotifyAuth
            >>> auth_url = SpotifyAuth.get_auth_url()
            >>> bool(auth_url)
            True
        """
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
    def get_access_token(code: str) -> Tuple[str, str]:
        """
        Get the Spotify access token.

        Args:
            code: A string containing the authorization code.

        Returns:
            A tuple containing the access token and refresh token.
        """
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
    def store_refresh_token(refresh_token: str) -> None:
        """
        Store the refresh token in a file.

        Args:
            refresh_token: A string containing the refresh token.
        """
        with open("refresh_token.txt", "w") as f:
            f.write(refresh_token)

    @staticmethod
    def refresh_access_token() -> str:
        """
        Refresh the Spotify access token from the refresh token stored in a file.

        Returns:
            A string containing the refreshed access token.
        """
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


import requests

class SpotifyAPI:
    """
    A class representing the Spotify API.

    Attributes:
        None

    Methods:
        get_users_saved_tracks: Returns a list of the user's saved tracks.
    """

    def get_users_saved_tracks(self, access_token, market=None, limit=20, offset=0):
        """
        Returns a list of the user's saved tracks.

        Args:
            access_token (str): A string representing the user's access token.
            market (str, optional): A string representing the market to retrieve the tracks from. Defaults to None.
            limit (int, optional): An integer representing the maximum number of tracks to retrieve. Defaults to 20.
            offset (int, optional): An integer representing the index of the first track to retrieve. Defaults to 0.

        Returns:
            list: A list of the user's saved tracks.

        Raises:
            Exception: If the request to the Spotify API fails.
        """
        endpoint = "https://api.spotify.com/v1/me/tracks"

        headers = {"Authorization": f"Bearer {access_token}"}

        params = {"market": market, "limit": limit, "offset": offset}

        response = requests.get(endpoint, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()

        else:
            raise Exception(response.status_code, response.text)
