"""Main module for spotify_data_visualizer."""


from flask import Flask, jsonify, render_template

from .auth import get_spotify_auth_token

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/token", methods=["GET"])
def get_token():
    token_info = get_spotify_auth_token()
    return jsonify(token_info)
