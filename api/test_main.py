from fastapi.testclient import TestClient
import uuid
from main import app
import json

client = TestClient(app)
rarendom = uuid.uuid4()
testURL = f"http://localhost/{rarendom}"
data = {"url": testURL, "ttl": -1}
dataJson = json.dumps(data)
short = 0


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to url shortening app"}


def test_create_new_short():
    global short
    response = client.post("/", dataJson)
    assert response.status_code == 200
    returnData = response.json()
    short = str(returnData["short"])
    assert len(returnData["short"]) == 6


def test_get_url():
    response = client.get(f"/{short}")
    assert response.status_code == 200
