from typing import Optional

from pydantic import HttpUrl

from .customs import Extension
from .mixins import BookIdMixin


class ShortBook(BookIdMixin):
    title: str
    author: str
    year: int
    pages: Optional[int]


class Book(ShortBook):
    size: Optional[str]
    published_by: Optional[str] = None
    description: Optional[str] = None
    cover: Optional[str] = None
    download_links: list[dict[Extension, list[HttpUrl]] | None]
    tor_link: dict[Extension, HttpUrl] | None
