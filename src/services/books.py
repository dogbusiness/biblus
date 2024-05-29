from functools import lru_cache
from typing import Annotated, AsyncGenerator, Callable, Sequence
from uuid import UUID

from core.exceptions import EmptyFields, NotFound
from core.settings import settings
from io_file_managers.abstract import IOFileManagerABC
from io_file_managers.managers import IOTorFileManager
from models.books import Book, ShortBook
from storages.abstract import StorageABC
from storages.elasticsearch import ElasticStorage

from .abract import BookServiceABC


class BookService(BookServiceABC):

    def __init__(self, storage: StorageABC, file_manager: IOFileManagerABC):
        self.storage = storage
        self.file_manager = file_manager

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
        fields = {}
        if author:
            fields["author"] = author
        if title:
            fields["title"] = author
        if fields == {}:
            raise EmptyFields()
        books = await self.storage.search_objects(
            settings.books_index,
            fields,
            pagination.page_size,
            pagination.page_number,
            sort.sort_type,
            sort_option.sort_option,
        )
        if books == []:
            raise NotFound()
        return [ShortBook(**book) for book in books]

    async def get_book_by_id(self, book_id: UUID) -> Book:
        book = await self.storage.get_object_by_id(settings.books_index, book_id)
        if not book:
            raise NotFound()
        return Book(**book)

    async def download_book_by_id(
        self, book_id: UUID
    ) -> Sequence[str, Callable[[str], AsyncGenerator[bytes, None, None]]]:
        book = await self.get_book_by_id(book_id)
        if not book:
            raise NotFound()
        book_link = book.model_dump()[settings.book_dwld_option_field]
        if not book_link:
            raise NotFound()
        return book_link, self.file_manager.stream_file


@lru_cache
def get_book_service() -> BookService:
    return BookService(storage=ElasticStorage(), file_manager=IOTorFileManager())
