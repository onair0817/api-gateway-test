import logging
from fastapi import FastAPI
from fastapi.logger import logger as fastapi_logger
from prometheus_fastapi_instrumentator import Instrumentator

# Set up logging
logging.basicConfig(level=logging.INFO)
fastapi_logger.addHandler(logging.StreamHandler())

app = FastAPI()


@app.get("/")
def read_root():
    fastapi_logger.info("Green")
    return {"Hello": "Green"}


Instrumentator().instrument(app).expose(app, include_in_schema=False)
