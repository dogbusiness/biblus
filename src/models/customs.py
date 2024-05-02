from enum import Enum
from typing import Annotated

from pydantic import BaseModel, StringConstraints

Extension = Annotated[str, StringConstraints(pattern=r"\.*")]


class BookSearchTypeEnum(str, Enum):
    author = "author"
    title = "title"


class BookSearchType(BaseModel):
    search_type: BookSearchTypeEnum = BookSearchTypeEnum.title

    def __init__(self, **data):
        super().__init__(**data)
        self.search_type.value.lower()
