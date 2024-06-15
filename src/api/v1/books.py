from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, responses, status

from core.exceptions import EmptyFields, NotFound, StreamFail
from core.logging import logger
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
    try:
        return await book_service.search_book(
            author, title, pagination, sort, sort_option
        )
    except EmptyFields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=EmptyFields.detail
        )


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
    try:
        return await book_service.get_book_by_id(book_id)
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=NotFound.detail
        )


@router.get(
    "/download/{book_id}/",
    response_model=Book,
    summary="Download book by id",
    description="Download a book by book_id",
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
    format: str,
    book_service: BookServiceABC = Depends(get_book_service),
) -> responses.StreamingResponse:
    try:
        book_link, func = await book_service.download_book_by_id(book_id, format)
    except NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Such book or format not found",
        )
    try:
        return responses.StreamingResponse(
            func(book_link), media_type="text/event-stream"
        )
    except StreamFail:
        logger.error(f"StreamFail:{StreamFail}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, detail="Download interrupted"
        )
