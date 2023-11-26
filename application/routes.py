from flask import*

from application import app

@app.route("/")
def home():
    return "<h2>Hello World </h2>"
