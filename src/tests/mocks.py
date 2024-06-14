class MockedBooksDB:

    async def get_object_by_id(self, table: str, id) -> dict | None:
        return {
            "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
            "author": "Fyodor Dostoevskiy",
            "title": "Crime and Punishment",
            "year": 1866,
            "pages": 435,
            "size": "1mb",
            "description": "Crime and Punishment follows the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who plans to kill an unscrupulous pawnbroker, an old woman who stores money and valuable objects in her flat.",
            "cover": "https://en.wikipedia.org/wiki/Crime_and_Punishment#/media/File:Crimeandpunishmentcover.png",
            "download_links": [{".pdf": ["https://somelink.com/crime_punish.pdf"]}],
            "tor_link": {".pdf": "http://someonionlink.onion/crime_punish.pdf"},
        }

    async def search_objects(  # noqa: E704
        self,
        table: str,
        fields_and_values: dict,
        order_by: str | None,
        order_option: str | None = "desc",
        objects_per_page: int = 10,
        page: int = 0,
    ) -> list[dict] | list[None]:
        return [
            {
                "book_id": "0ad94e7c-27d5-47ad-81d4-6b6edf764ad0",
                "title": "Crime and Punishment",
                "author": "Fyodor Dostoevskiy",
                "year": 1866,
                "pages": 435,
            }
        ]
