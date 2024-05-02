from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import books
from core.settings import settings

app = FastAPI(
    title=settings.project_name,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.include_router(books.router, prefix="/api/v1/book", tags=["Book Ops"])
