from flask import Flask, jsonify, request

add = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@add.route("/")
def home():
    return "Welcome to the Flask API!"

@add.route("/data")
def data():
    return jsonify(list(users.keys()))

@add.route("/status")
def status():
    return "OK"

@add.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@add.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    add.run(debug=True)
