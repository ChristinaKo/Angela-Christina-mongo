from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    return render_template("index.html")


@app.route("/about", methods=["POST","GET"])
def about():
    return render_template("about.html")

@app.route("/login", methods=["POST","GET"])
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
