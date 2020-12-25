<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/logo.png" alt="logo" style="zoom:50%;" />
![Docker Image CI](https://github.com/alivx/urless/workflows/Docker%20Image%20CI/badge.svg)
# URLess

URL Shortener `API` Service

self-hostable open-source URL shortening web API service with a Fast API. It allows you to host your own URL shorten easy to use.


## Screenshots

<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/sample1.png" alt="sample1" style="zoom:50%;" />

## Quickstart

Urless is written in Python, using Redis as its primary database.( TODO redisgears + mysql)


## Installation
Download the latest version of URLess via this image 'alivx/urless'.

```Bash
docker-compose build #To build project
docker-compose up #To run project, You can use `-d` option to run it in the background.
```

To test service run CURL command:
```Bash
curl --location --request POST 'http://127.0.0.1:8000/' \
--header 'Content-Type: application/json' \
--data-raw '{"url":"www.google.com"}'
```
OR
from browser open `localhost` and start testing the system.

## Configs
To Deal with config for each app, you have two method.
1. settings.yaml
2. enviromnet varables. (This will override settings.yaml value)

In point 2, just use `DYNACONF_[valueName]`, for example, in our API there is a config called `exposePort`, to override it use this value `DYNACONF_exposePort`. such as `export DYNACONF_exposePort=1991`



If you want to use a custom config under docker-compose, just add it under `environment` section as explained above.

<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/docker-compose-env-vars.png" alt="docker-compose-env-vars" style="zoom:40%;" />

You can change value for each service config under file `settings.yaml`

<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/frontend-config.png" alt="frontend-config" style="zoom:40%;" />

For nginx, you must change the config file under `infrastructure/nginx/urless.conf` if you changes `frontend` container name or port.

<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/nginx.png" alt="nginx" style="zoom:40%;" />


----
You can check the API documntion by `/docs`
<img src="https://raw.githubusercontent.com/alivx/urless/master/resources/BackendAPI.png" alt="APiDocs" style="zoom:50%;" />
