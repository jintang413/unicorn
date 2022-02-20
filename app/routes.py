from turtle import title
from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Summer"}
    items = [
        {"product": {"name": "SPEEDY BANDOULIÈRE 20"}, "status": True},
        {"product": {"name": "PRECIOUS TIGER REYKJAVIK SCARF"}, "status": False},
    ]
    return render_template("index.html", title="Louis Vuitton", user=user, items=items)
