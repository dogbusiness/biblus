from http import HTTPStatus

import pytest

from .conftest import BOOK_SEARCH_SUCCESS, GET_BOOK_BY_ID_SUCCESS


class TestBook:
    @pytest.mark.parametrize(
        "url,status_code,response_json",
        [
            (
                "/api/v1/book/search/?author=Dostoev&title=Crime&page_number=1&page_size=10",
                HTTPStatus.OK,
                BOOK_SEARCH_SUCCESS,
            ),
            (
                "/api/v1/book/0ad94e7c-27d5-47ad-81d4-6b6edf764ad0/",
                HTTPStatus.OK,
                GET_BOOK_BY_ID_SUCCESS,
            ),
        ],
    )
    @pytest.mark.asyncio
    async def test_get_details(self, client, url, status_code, response_json):
        response = await client.get(url)

        assert response.status_code == status_code, response.text
        assert response.json() == response_json
