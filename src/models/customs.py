from enum import Enum
from typing import Annotated

from pydantic import BaseModel, StringConstraints

Extension = Annotated[str, StringConstraints(pattern=r"\.*")]


class BookSortTypeEnum(str, Enum):
    author = "author"
    title = "title"
    pages = "pages"
    year = "year"


class BookSortOptionEnum(str, Enum):
    asc = "asc"
    desc = "desc"


class BookSortType(BaseModel):
    sort_type: BookSortTypeEnum = BookSortTypeEnum.title

    # def __init__(self, **data):
    #     super().__init__(**data)
    #     self.search_type.value.lower()


class BookSortOption(BaseModel):
    sort_option: BookSortOptionEnum = BookSortOptionEnum.asc
