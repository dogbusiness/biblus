from functools import lru_cache
from uuid import UUID

from models.books import Book, ShortBook
from models.customs import BookSearchType

from .abract import BookServiceABC


class BookService(BookServiceABC):

    def __init__(self):
        self.storage = None
        self.manager = None

    async def search_book(
        self,
        search_type: BookSearchType,
        query: str,
        sort: BookSearchType | None = None,
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
