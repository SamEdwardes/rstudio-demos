from typing import Optional, List
from loguru import logger

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    print("This line was printed using `print`.")
    logger.info("The index/root of the site.")
    logger.debug("The index/root of the site.")
    logger.error("The index/root of the site.")
    return {"The": "index"}


@app.get("/hello")
def hello():
    print("This line was printed using `print`.")
    logger.info("Hello world!")
    logger.debug("Hello world!")
    logger.error("Hello world!")
    return {"Hello": "world"}