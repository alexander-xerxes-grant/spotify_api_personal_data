"""Main module for spotify_data_visualizer."""


from flask import Flask, jsonify

from .auth import get_spotify_auth_token

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Spotify Top Tracks!"


@app.route("/token", methods=["GET"])
def get_token():
    token_info = get_spotify_auth_token()
    return jsonify(token_info)
