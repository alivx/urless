from flask import Flask, render_template, request
import json
import requests
from config import *
from netifaces import interfaces, ifaddresses, AF_INET


print("Starting Server..")

for ifaceName in interfaces():
    addresses = [
        i["addr"]
        for i in ifaddresses(ifaceName).setdefault(AF_INET, [{"addr": "No IP addr"}])
    ]
    print("Host network info: %s: %s" % (ifaceName, ", ".join(addresses)))

# create the object of Flask
app = Flask(__name__, static_folder="./templates/assets", template_folder="./templates")

# creating our routes
@app.route("/")
def index():
    data = "Codeloop"
    print("Accessing Home page /")
    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def login():
    user = request.form["urlContent"]
    # try:
    r = requests.post(f"{settings.backendURL}/", json={"url": user})
    data = json.loads(r.content)
    newShortCode = str(data["short"])
    _url = f"{settings.finalURL}/{newShortCode}"
    print(f"Sucessfully addedd {_url}")
    return render_template("sucess.html", results=_url)
    # except:
    #     return render_template(
    #         "failed.html", results="There is an error please contact the admin 🐛"
    #     )


# run flask app
if __name__ == "__main__":
    app.run(host=settings.exposeHost, port=settings.exposePort, debug=True)
