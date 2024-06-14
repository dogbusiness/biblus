from http import HTTPStatus

import pytest


BOOK_SEARCH_SUCCESS = [
    {
    "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
    "title": "Crime and Punishment",
    "author": "Fyodor Dostoevskiy",
    "year": 1866,
    "pages": 435
    }
]

GET_BOOK_BY_ID_SUCCESS = {
    "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
    "author": "Fyodor Dostoevskiy",
    "title": "Crime and Punishment",
    "published_by": None,
    "year": 1866,
    "pages": 435,
    "size": "1mb",
    "description": "Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, an old woman who stores money and valuable objects in her flat.",
    "cover": "https://en.wikipedia.org/wiki/Crime_and_Punishment#/media/File:Crimeandpunishmentcover.png",
    "download_links": [{".pdf": ["https://somelink.com/crime_punish.pdf"]}],
    "tor_link": {".pdf": "http://someonionlink.onion/crime_punish.pdf"}
}

class TestBook:
    @pytest.mark.parametrize(
        'url,status_code,response_json',
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
            # (
            #     "/api/v1/films/0311ed51-8833-413f-bff5-0e139c11264a",
            #     HTTPStatus.NOT_FOUND,
            #     films_responses.FILM_DETAILED_NOTFOUND,
            # ),
        ],
    )
    @pytest.mark.asyncio
    async def test_get_details(self, client, url, status_code, response_json):
        response = await client.get(url)

        assert response.status_code == status_code, response.text
        assert response.json() == response_json

    # @pytest.mark.parametrize(
    #     'url,status_code,count',
    #     [
    #         (
    #             "/api/v1/films/?sort=-imdb_rating&page_size=10&page_number=1",
    #             HTTPStatus.OK,
    #             10,
    #         )
    #     ],
    # )
    # async def test_get_film_list(self, client, url, status_code, count):
    #     response = await client.get(url)
    #     assert response.status_code == status_code, response.text
    #     assert len(response.json()) == count