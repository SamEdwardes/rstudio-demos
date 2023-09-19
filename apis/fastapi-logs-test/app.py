from typing import Optional, List
from loguru import logger

from fastapi import FastAPI


app = FastAPI()


@app.get("/test")
def index():
    print("This line was printed using `print`.")
    logger.info("This is a test.")
    logger.debug("This is a test.")
    logger.error("This is a test.")
    return {"The": "index"}


@app.get("/hello")
def hello():
    print("This line was printed using `print`.")
    logger.info("Hello world!")
    logger.debug("Hello world!")
    logger.error("Hello world!")
    return {"Hello": "world"}