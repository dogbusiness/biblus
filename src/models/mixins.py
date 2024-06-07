from uuid import UUID

from pydantic import BaseModel


class BookIdMixin(BaseModel):
    book_id: UUID
