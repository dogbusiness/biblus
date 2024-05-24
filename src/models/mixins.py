from pydantic import BaseModel
from uuid import UUID

class BookIdMixin(BaseModel):
    book_id: UUID
