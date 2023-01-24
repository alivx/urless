from flask import Flask, render_template, request
import json
import requests
from config import *
import socket
import logging


# setup loggers

logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s %(module)s %(funcName)s:%(levelname)s:%(message)s"
)
ch.setFormatter(formatter)
logger.addHandler(ch)

print("Getting Server info..")
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    logger.info(f"Hostname: {host_name}, IP: {host_ip}")
except:
    logger.info("Unable to get Hostname and IP")

# create the object of Flask
app = Flask(__name__, static_folder="./templates/assets", template_folder="./templates")

# creating our routes
@app.route("/")
def index():
    data = "Codeloop"
    logger.info("Accessing Home page /")
    return render_template("index.html", data=data)


@app.route("/", methods=["POST"])
def login():
    user = request.form["urlContent"]
    ttl = request.form["urlDate"]
    if ttl == None:
        ttl = -1
    r = requests.post(f"{settings.backendURL}:{settings.backendPort}/", json={"url": user, "ttl": ttl})
    data = json.loads(r.content)
    try:
        newShortCode = str(data["short"])
    except Exception as e:
        logger.error("URL invlide or TTL is not set")
        return render_template(
            "failed.html",
            results="I can't see any URL :(, please make sure to put one.",
        )
    else:
        _url = f"{settings.domainName}/{newShortCode}"
        logger.info(f"Sucessfully addedd {_url}")
        print(_url)
        return render_template("sucess.html", results=_url)


# run flask app
if __name__ == "__main__":
    app.run(host=settings.exposeHost, port=settings.exposePort, debug=True)
