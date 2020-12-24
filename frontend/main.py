from flask import Flask, render_template, request
import json
import requests
from config import *
import socket

print("Getting Server info..")
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"Hostname: {host_name}, IP: {host_ip}")
except:
    print("Unable to get Hostname and IP")

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
    ttl = request.form["urlDate"]
    if ttl == None:
        ttl = -1
    r = requests.post(f"{settings.backendURL}/", json={"url": user, "ttl": ttl})
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
