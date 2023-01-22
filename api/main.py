import uuid
import redis
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from config import settings
import uvicorn
import sys
import socket
from dynaconf import Dynaconf
import structlog
import time


# Config handler
settings = Dynaconf(
    envvar_prefix="DYNACONF_",
    settings_files=["settings.yaml", ".secrets.yaml"],
)

# Logs handler
structlog.configure(logger_factory=structlog.stdlib.LoggerFactory())
logger = structlog.get_logger()

#
logger.info("Getting Server info..")
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    logger.info(f"Hostname: {host_name}, IP: {host_ip}")
except Exception:
    logger.ERROR("Unable to get Hostname and IP")

app = FastAPI()

rds = redis.Redis(host=settings.redisHost, port=settings.redisPort)
hostname = socket.gethostname()
logger.info(f"Hostname: {hostname}")
logger.info("Checking Redis Connection...")


try:
    pingValue = rds.ping()
    logger.info("Redis is working fine.")
except Exception:
    logger.error("Redis is not working.")
    sys.exit(1)


class Item(BaseModel):
    url: str
    custom_target: str = None
    ttl: int = -1

# Health check endpoint


@app.get("/ping")
def health_end_point(response: Response):
    try:
        logger.info("Health check request pass.")
        rds.ping()
        response.status_code = status.HTTP_200_OK
        return {"msg": "Pong", "Time": time.time()}
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        logger.error("Health Check failed")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"msg": "Error"}


@app.get("/")
def read_root():
    """Retrun welcome message

    Returns:
        json: welcome message
    """
    logger.info("Backend Home page access.")
    return {"message": "Welcome to url shortening app"}


@app.get("/{short}")
def redirect_urless(short: str):
    """Redirect fetch URL

    Args:
        short (str): short URL

    Returns:
        redirect: origin url
    """
    logger.info(f"Getting value of key {short}")
    try:
        key = rds.get(short).decode("utf8")
        logger.info("Redirect request [{0}] to ({1})".format(short, key))
        logger.info(f"Getting key for {short}")
        return RedirectResponse(url=key)
    except Exception:
        logger.warn(f"Could not find the key {short}.")
        return {"message": f"URL ({short}) not found"}


@app.post("/")
def urless(item: Item):
    """Short given URL

    Args:
        item (Item): Full URL

    Returns:
        json : URL, and shorten URL
    """
    url = item.url
    ttl = item.ttl
    cname = item.custom_target
    if rds.get(url) is None:
        new_name = cname or str(uuid.uuid4())[-6:]
        logger.info(f"New key name is {new_name}")
        if rds.set(new_name, url):
            if not ttl == -1:
                rds.expire(new_name, ttl)
                logger.info(f"Setting TTL {ttl} for {new_name}")
            logger.info(f"Key addedd successfully: {new_name} -- {url} ")
            return {"url": url, "short": new_name}
        else:
            logger.error(f"Error setting key {new_name}")
            return {"message": "failed"}


if __name__ == "__main__":
    logger.info(f"Starting the server on port {settings.exposePort}")
    uvicorn.run(
        "main:app", host=settings.exposeHost, port=settings.exposePort, log_level="info"
    )
