import base64
import os

import requests


def get_spotify_auth_token():
    "Get Spotify authorization token."
    client_id = os.environ.get("SPOTIFY_CLIENT_ID")
    client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

    if not client_id or not client_secret:
        raise EnvironmentError(
            "Please set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET\
            environment variables."
        )

    message = f"{client_id}:{client_secret}"
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    headers = {"Authorization": f"Basic {base64_message}"}

    payload = {"grant_type": "client_credentials"}

    auth_response = requests.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=payload
    )

    auth_response_data = auth_response.json()

    return auth_response_data
