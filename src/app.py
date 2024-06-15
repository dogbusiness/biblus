from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from api.v1 import books
from core.logging import logger
from core.settings import settings
from io_file_managers.managers import IOTorFileManager
from services.books import BookService, get_book_service
from tests.mocks import MockedBooksDB


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(settings.redis_host, port=settings.redis_port)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    logger.info("Success")
    yield


def override_storage_dependency() -> BookService:
    return BookService(storage=MockedBooksDB(), file_manager=IOTorFileManager())


@asynccontextmanager
def mocked_lifespan():
    yield


app = FastAPI(
    title=settings.app_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(books.router, prefix="/api/v1/book", tags=["Book Ops"])

app.dependency_overrides[get_book_service] = (
    override_storage_dependency  # mocking storage
)
app.dependency_overrides[lifespan] = mocked_lifespan
