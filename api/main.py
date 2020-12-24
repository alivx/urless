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
except:
    print("Unable to get Hostname and IP")

app = FastAPI()
rds = redis.Redis(host=settings.redisHost, port=settings.redisPort)
hostname = socket.gethostname()
print(f"Hostname: {hostname}")
print("Checking Redis Connection...")


try:
    pingValue = rds.ping()
    print("Redis is working fine.")
except:
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


@app.get("/get")
def get_all_urls():
    """Get short code URL from DB

    Returns:
        str: URL
    """
    data = []
    print("Getting all keys from redis.")
    for key in rds.keys():
        data.append({key.decode("utf8"): rds.get(key).decode("utf8")})
    return data


@app.get("/{short}")
def redirect_urless(short: str):
    """Redirect fetch URL

    Args:
        short (str): short URL

    Returns:
        redirect: origin url
    """
    print(f"Getting value of key {short}")
    for key in rds.keys():
        if rds.get(key).decode("utf8") == short:
            print(f"Getting Key from Redis: {key}")
            valueOfKey = rds.get(key)
            print(f"Redirect request [{short}] to ({valueOfKey})")
            return RedirectResponse(url=key.decode("utf8"))
    print("Could not find the key.")
    return {"message": "URL not defined"}


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
        print(ttl)
        if rds.set(url, new_name):
            if not ttl == -1:
                rds.expire(url, ttl)
                print(f"Setting TTL {ttl} for {new_name}")
            print("Key addedd successfully: {new_name} -- {url} ")
            return {"url": url, "short": rds.get(url)}
        else:
            return {"message": "failed"}
    # TO DO: allow deplicate values
    print("URL already exists..")
    return {"message": "URL already exists", "short": rds.get(url)}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.exposeHost, port=settings.exposePort, log_level="info"
    )
