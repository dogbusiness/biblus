from contextlib import asynccontextmanager

import stem
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import books
from core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start taking requests
    tor_process = stem.process.launch_tor_with_config(
        config={
            "SocksPort": str(settings.proxy_port),
        }
        # ToDo write logging for bootstrapping tor (init_msg_handler kwrd)
    )
    yield
    # finishing requests
    tor_process.kill()


app = FastAPI(
    title=settings.app_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(books.router, prefix="/api/v1/book", tags=["Book Ops"])
