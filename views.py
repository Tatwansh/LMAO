from flask import render_template, flash, request
from app import app
from arx_api import retr

# Route Decorators
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)
    retr(msg)



# Custom Error Page #
# Invalid URL
@app.errorhandler(404)
def the4o4(e):
    return render_template("4o4.html"), 404


# InternalServerError
@app.errorhandler(500)
def the5oo(e):
    return render_template("5oo.html"), 500

