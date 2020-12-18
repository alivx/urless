# urless
URL Shortener `API` Service

self-hostable open-source URL shortening web API service with a Fast API. It allows you to host your own URL shortenerur less easy to use.


## Quickstart

Urless is written in Python, using Redis as its primary database.( TODO redisgears + mysql)


## Installation
Download the latest version of URLess via this image 'alivx/urless:latest'.
To to container:
```Bash
docker run --rm -ti  -p 8000:8000 alivx/urless:latest
```
* install redis-server or use the below docker command:
```Bash
docker run -ti --rm --network host -p 6379:6379 redis:latest
```
OR docker-compose
```Bash
docker-compose pull
docker-compose up
```

To test service run CURL command:
```Bash
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'Content-Type: application/json' \
--data-raw '{"url":"www.google.com"}'
```

## Configs
To Deal with config for each app, you have two method.
1. settings.yaml
2. enviromnet varables. (This will override settings.yaml value)

In point 2, just use `DYNACONF_[valueName]`, for exmaple, in our API there is a config called `exposePort`, to override it use this value `DYNACONF_exposePort`. such as `export DYNACONF_exposePort=1991`