# coding: utf-8

import flask
from flask import request


app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "Home"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World"


@app.route("/hello", methods=["POST"])
def hello_post():
    for k, v in request.headers.items():
        print("%s | %s" % (k, v))

    print("=================================================")

    # print("request.args=%s" % request.args)
    # print("request.form=%s" % request.form)
    # print("request.values=%s" % request.values)  # args, form

    # print("Content-Type=%s" % request.headers["Content-Type"])
    print("data=%s" % request.data.decode("utf-8"))
    return "Hello Flask"


@app.route("/greet", methods=["GET", "POST"])
def greet():
    for k, v in request.headers.items():
        print("%s | %s" % (k, v))

    print("=================================================")

    # print("request.args=%s" % request.args)
    # print("request.form=%s" % request.form)
    # print("request.values=%s" % request.values)  # args, form

    # print("Content-Type=%s" % request.headers["Content-Type"])
    print("data=%s" % request.data.decode("utf-8"))
    return "Greet Flask"


if __name__ == "__main__":
    app.run()