#!/usr/bin/python3
from flask import Flask, jsonify, request
app = Flask(__name__)


users = {}


# Route decorator tells Flask what
# URL should trigger function.
@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    #  Returns list of all usernames stored in API
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
