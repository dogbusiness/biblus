from abc import ABC, abstractmethod
from uuid import UUID

from models.books import Book, ShortBook
from models.customs import BookSearchType


class BookServiceABC(ABC):

    @abstractmethod
    async def search_book(  # noqa: E704
        self,
        search_type: BookSearchType,
        query: str,
        sort: BookSearchType | None = None,
    ) -> list[ShortBook]: ...

    @abstractmethod
    async def get_book_by_id(self, book_id: UUID) -> Book: ...  # noqa: E704

    @abstractmethod
    async def download_book_by_id(
        self, book_id: UUID
    ) -> Book:  # не уверен будем отдавать именно Book
        ...
