import datetime
from typing import Optional

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
    download_links: list[dict[str: str]]  # extension:link
    # tor_link: dict[str: str]  # extension:link
