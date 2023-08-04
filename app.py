from flask import Flask, request, abort, make_response
from generator import *

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, the service powered by Flask!"


@app.route("/login", methods=["POST"])
def login():
    token = request.cookies.get("Token")
    username = request.json["username"]
    password = request.json["password"]
    if len(password) > 10:
        abort(400, "The password must be at least 10 characters")
    response = make_response(
        {"username": username, "password": password, "token": token}
    )
    token = tokenGenerator(username)
    response.set_cookie("Token", token)
    return {"username": username, "password": password, "token": token}


@app.route("/profile")
def profile():
    return "Something here..."


@app.route("/info")
def info():
    uid = request.args.get("uid")
    return f"Can't find the information of user '{uid}'"
