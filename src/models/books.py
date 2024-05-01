import datetime
from typing import Optional

from pydantic import FileUrl

from .customs import Extension
from .mixins import BookIdMixin


class ShortBook(BookIdMixin):
    title: str
    author: str


class Book(ShortBook):
    year: datetime.datetime
    pages: Optional[int]
    size: Optional[str]
    published_by: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    download_links: list[dict[Extension: FileUrl] | None]
    # tor_link: dict[Extension: FileUrl]
