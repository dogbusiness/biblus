from pydantic import BaseModel


class BookIdMixin(BaseModel):
    book_id: int
