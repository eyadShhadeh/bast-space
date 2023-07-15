from typing import Union
from fastapi import FastAPI, Request
from src.util.log import log_config, CustomizeLogger
from src.controllers import route_collector


def create_app() -> FastAPI:
    app = FastAPI(title='bast_space')
    logger = CustomizeLogger.make_logger()
    app.logger = logger

    return app


app = create_app()


app.include_router(route_collector,)


@app.get("/")
async def read_root():
    return "welcome to bast space, your perfect  companion :D"
