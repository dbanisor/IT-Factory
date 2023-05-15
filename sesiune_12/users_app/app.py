from flask import Flask, jsonify, abort, request

from sesiune_12.users_app.users_repo import UsersRepo

app = Flask(__name__)

user_repo = UsersRepo("./users.csv")

@app.route("/")
def home():
    return "Hello"


@app.route("/users")
def get_all():
    users = user_repo.read()
    return jsonify(users)


@app.route("/users/<name>")
def get_one(name):
    user = user_repo.find_one(name)
    if user:
        return jsonify(user)
    abort(404, "User not found")

@app.route("/users", methods=["POST"])
def create_user():
    user_repo.create(request.json)
    return "Ok", 201

@app.route("/users/update/<name>", methods=["PATCH"])
def update_age(name):
    user_repo.update(name, request.json)
    return "Ok", 201


if __name__ == '__main__':
    app.run(debug=True)
