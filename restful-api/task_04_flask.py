#!/usr/bin/python3
"""
Simple Flask API
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """Return API status"""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return a list of all usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data by username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the dictionary"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
