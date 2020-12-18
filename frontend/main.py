from flask import Flask, render_template, request
import json
import requests
from config import *

# create the object of Flask
app = Flask(__name__, static_folder="./templates/assets", template_folder="./templates")


# creating our routes
@app.route("/")
def index():
    data = "Codeloop"
    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def login():
    user = request.form["urlContent"]
    # try:
    r = requests.post(f"{settings.backendURL}/", json={"url": user})
    data = json.loads(r.content)
    newShortCode = str(data["short"])
    _url = f"{settings.finalURL}/{newShortCode}"
    return render_template("sucess.html", results=_url)
    # except:
    #     return render_template(
    #         "failed.html", results="There is an error please contact the admin 🐛"
    #     )


# run flask app
if __name__ == "__main__":
    app.run(host=settings.exposeHost, port=settings.exposePort, debug=True)
