from flask import Flask, render_template, request
from flask import Flask, redirect, url_for, request
from flask_bootstrap import Bootstrap
import json
import requests
from config import backendURL

# create the object of Flask
app = Flask(__name__, static_folder="./templates/assets", template_folder="./templates")


bootstrap = Bootstrap(app)

# creating our routes
@app.route("/")
def index():
    data = "Codeloop"
    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def login():
    user = request.form["urlContent"]
    r = requests.post(f"{backendURL}/", json={"url": user})
    data = json.loads(r.content)
    print(data["short"])
    return render_template("sucess.html", results=str(data["short"]))


# run flask app
if __name__ == "__main__":
    app.run(debug=True)