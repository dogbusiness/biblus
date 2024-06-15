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
            "tor_link": {
                ".pdf": "http://libgenfrialc7tguyjywa36vtrdcplwpxaw43h6o63dmmwhvavo5rqqd.onion/LG/0447000/f67efa147708e1e007638075acd7863b/Fyodor%20Dostoyevsky%20-%20Crimen%20Y%20Castigo%20%20%20Crime%20and%20Punishment%20%28Literatura%20%20%20Literature%29%20%28Spanish%20Edition%29-Alianza%20%282006%29.pdf"
            },
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
