import os
import requests

from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channels = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/channel")
def channel():
    return render_template("channel.html")

@socketio.on("send message")
def handle_message(message):
    print('received message: ' + message)
    emit("send message", message, broadcast=True)

@socketio.on("session_username")
def keep_user():
