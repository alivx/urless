import uuid
import redis
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from config import settings
import uvicorn
import sys
import socket

print("Getting Server info..")
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"Hostname: {host_name}, IP: {host_ip}")
except Exception:
    print("Unable to get Hostname and IP")

app = FastAPI()
rds = redis.Redis(host=settings.redisHost, port=settings.redisPort)
hostname = socket.gethostname()
print(f"Hostname: {hostname}")
print("Checking Redis Connection...")


try:
    pingValue = rds.ping()
    print("Redis is working fine.")
except Exception:
    print("Redis is not working.")
    sys.exit(1)


class Item(BaseModel):
    url: str
    custom_target: str = None
    ttl: int = -1


@app.get("/")
def read_root():
    """Retrun welcome message

    Returns:
        json: welcome message
    """
    print("Backend Home page access.")
    return {"message": "Welcome to url shortening app"}

@app.get("/{short}")
async def redirect_urless(short: str):
    """Redirect fetch URL

    Args:
        short (str): short URL

    Returns:
        redirect: origin url
    """
    print(f"Getting value of key {short}")
    try:
        key = rds.get(short).decode("utf8")
        print("Redirect request [{0}] to ({1})".format(short, key))
        return RedirectResponse(url=key)
    except Exception:
        print(f"Could not find the key {short}.")
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
        print(f"New key name is {new_name}")
        if rds.set(new_name, url):
            if not ttl == -1:
                rds.expire(new_name, ttl)
                print(f"Setting TTL {ttl} for {new_name}")
            print(f"Key addedd successfully: {new_name} -- {url} ")
            return {"url": url, "short": new_name}
        else:
            return {"message": "failed"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.exposeHost, port=settings.exposePort, log_level="info"
    )
