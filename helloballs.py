from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, popo!</p>"

@app.get("/foo")
def foo_get():
    return "<p>This is foo</p>"

@app.post("/foo")
def foo_post():
    return "<p>This is marios little balls</p>"