"""Main module for spotify_data_visualizer."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/token", methods=["GET"])
# def get_token():
#     try:
#         # token_info = get_spotify_auth_token()
#         # return jsonify(token_info), 200
#     except Exception as e:
#         response = {"error": str(e), "description": e.__class__.__name__}
#         return jsonify(response), 500
