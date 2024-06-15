import pytest_asyncio
from httpx import AsyncClient

from app import app, lifespan
from io_file_managers.managers import IOTorFileManager
from services.books import BookService, get_book_service

from .mocks import MockedBooksDB


def override_storage_dependency() -> BookService:
    return BookService(storage=MockedBooksDB(), file_manager=IOTorFileManager())


def mocked_lifespan():
    yield


@pytest_asyncio.fixture(scope="session")
async def client():
    test_app = app
    test_app.dependency_overrides[get_book_service] = (
        override_storage_dependency  # mocking storage
    )
    test_app.dependency_overrides[lifespan] = mocked_lifespan
    async with AsyncClient(app=test_app, base_url="http://testserver") as client:
        yield client


BOOK_SEARCH_SUCCESS = [
    {
        "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevskiy",
        "year": 1866,
        "pages": 435,
    }
]

GET_BOOK_BY_ID_SUCCESS = {
    "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
    "author": "Fyodor Dostoevskiy",
    "title": "Crime and Punishment",
    "published_by": None,
    "year": 1866,
    "pages": 435,
    "size": "1mb",
    "description": "Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, an old woman who stores money and valuable objects in her flat.",
    "cover": "https://en.wikipedia.org/wiki/Crime_and_Punishment#/media/File:Crimeandpunishmentcover.png",
    "download_links": [{".pdf": ["https://somelink.com/crime_punish.pdf"]}],
    "tor_link": {
        ".pdf": "http://libgenfrialc7tguyjywa36vtrdcplwpxaw43h6o63dmmwhvavo5rqqd.onion/LG/0447000/f67efa147708e1e007638075acd7863b/Fyodor%20Dostoyevsky%20-%20Crimen%20Y%20Castigo%20%20%20Crime%20and%20Punishment%20%28Literatura%20%20%20Literature%29%20%28Spanish%20Edition%29-Alianza%20%282006%29.pdf"
    },
}
