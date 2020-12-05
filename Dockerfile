from python:3.9-alpine3.12
COPY ./api /api
WORKDIR /api
RUN pip install --no-cache-dir fastapi==0.61.2 redis==3.2.1 uvicorn==0.12.2 nose requests virtualenv
EXPOSE 8000
ENTRYPOINT [ "ash","entrypoint.bash"]