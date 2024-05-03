from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from core.pagination import PaginateQueryParams
from models.books import Book, ShortBook
from models.customs import BookSortOption, BookSortType
from services.abract import BookServiceABC
from services.books import get_book_service

router = APIRouter()


@router.get(
    "/search/",
    response_model=list[ShortBook],
    summary="Search book by author or title",
    description="Search a book by an author or a title",
    responses={
        status.HTTP_401_UNAUTHORIZED: {"description": "Missing token or inactive user."}
    },
)
async def search_book(
    author: str | None,
    title: str | None,
    pagination: PaginateQueryParams = Depends(PaginateQueryParams),
    sort: BookSortType | None = None,
    sort_option: BookSortOption | None = None,
    book_service: BookServiceABC = Depends(get_book_service),
) -> list[ShortBook]:
    # Полнотекстовый поиск ????
    return await book_service.search_book(author, title, pagination, sort, sort_option)


@router.get(
    "/{book_id}/",
    response_model=Book,
    summary="Get book by id",
    description="Get information about book by book_id",
    response_description="book_id is from POST /search-book/",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Missing token or inactive user."
        },
        status.HTTP_404_NOT_FOUND: {"description:": "Book not found"},
    },
)
async def get_book(
    book_id: UUID,
    book_service: BookServiceABC = Depends(get_book_service),
) -> Book:
    book = await book_service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found"
        )
    return book


@router.get(
    "/download/{book_id}/",
    response_model=Book,
    summary="Get book by id",
    description="Get information about book by book_id",
    response_description="book_id is from POST /search-book/",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Missing token or inactive user."
        },
        status.HTTP_404_NOT_FOUND: {"description:": "Book not found"},
    },
)
async def download_book(
    book_id: UUID,
    book_service: BookServiceABC = Depends(get_book_service),
) -> Book:
    book = await book_service.download_book_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found"
        )
    # пока не знаю как возвращать - файл или что-то еще
    return book
