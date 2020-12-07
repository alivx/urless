import uuid
import redis
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse


app = FastAPI()
rds = redis.Redis()


class Item(BaseModel):
    url: str
    custom_target: str = None
    ttl: int = -1


@app.get("/")
def read_root():
    """ Retrun welcome message

    Returns:
        json: welcome message
    """
    return {"message": "Welcome to url shortening app"}


@app.get("/get")
def get_all_urls():
    """ Get short code URL from DB

    Returns:
        str: URL
    """
    data = []
    for key in rds.keys():
        data.append({key.decode("utf8"): rds.get(key).decode("utf8")})
    return data


@app.get("/{short}")
def redirect_urless(short: str):
    """ Redirect fetch URL

    Args:
        short (str): short URL

    Returns:
        redirect: origin url
    """
    for key in rds.keys():
        if rds.get(key).decode("utf8") == short:
            print(rds.get(key))
            return RedirectResponse(url=key.decode("utf8"))

    return {"message": "URL not defined"}


@app.post("/")
def urless(item: Item):
    """ Short given URL

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
        print(ttl)
        if rds.set(url, new_name):
            if not ttl == -1:
                rds.expire(url, ttl)
            return {"url": url, "short": rds.get(url)}
        else:
            return {"message": "failed"}
    return {"message": "URL already exists", "short": rds.get(url)}
