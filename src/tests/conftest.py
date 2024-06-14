import pytest_asyncio
from httpx import AsyncClient

from app import app, lifespan
from services.books import BookService, get_book_service
from .mocks import MockedBooksDB
from io_file_managers.managers import IOTorFileManager

def override_storage_dependency() -> BookService:
    return BookService(storage=MockedBooksDB(), file_manager=IOTorFileManager())

def mocked_lifespan():
    yield

@pytest_asyncio.fixture(scope="session")
async def client():
    test_app = app
    test_app.dependency_overrides[get_book_service] = override_storage_dependency # mocking storage
    test_app.dependency_overrides[lifespan] = mocked_lifespan
    async with AsyncClient(app=test_app, base_url="http://testserver") as client:
        yield client
