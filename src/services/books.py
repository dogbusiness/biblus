from functools import lru_cache
from typing import Annotated
from uuid import UUID

from models.books import Book, ShortBook

from .abract import BookServiceABC


class BookService(BookServiceABC):

    def __init__(self):
        self.storage = None

    async def search_book(
        self,
        author: str | None,
        title: str | None,
        pagination: Annotated[
            object, hasattr(object, "page_number"), hasattr(object, "page_size")
        ],
        sort: Annotated[object, hasattr(object, "sort_type")] | None = None,
        sort_option: Annotated[object, hasattr(object, "sort_option")] | None = None,
    ) -> list[ShortBook]:
        pass

    async def get_book_by_id(self, book_id: UUID) -> Book:
        pass

    async def download_book_by_id(
        self, book_id: UUID
    ) -> Book:  # не уверен будем отдавать именно Book
        pass


@lru_cache
def get_book_service() -> BookService:
    return BookService()
