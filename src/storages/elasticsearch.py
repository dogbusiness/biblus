from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator
from uuid import UUID

from elasticsearch import AsyncElasticsearch
from fastapi_cache.decorator import cache

from core.settings import settings

from .abstract import StorageABC


class ElasticStorage(StorageABC):

    @asynccontextmanager
    async def call_client(self) -> AsyncGenerator[AsyncElasticsearch, None]:
        client = AsyncElasticsearch(
            settings.elastic_url,
            basic_auth=(settings.elastic_user, settings.elastic_password),
        )
        yield client
        await client.close()

    def _parse_search_resp(
        self, resp: dict[str, Any]
    ) -> list[dict[str, Any]] | list[None]:
        if resp["hits"]["hits"]["_source"]["response"]["status_code"] == 200:
            return [hit["_source"] for hit in resp["hits"]["hits"]]
        else:
            return []

    @cache(expire=settings.cache_expire)
    async def get_object_by_id(  # noqa: E704
        self,
        table: str,
        id: UUID,
    ) -> dict[str, Any] | None:
        return await self.call_client().get_source(index=table, id=id)

    @cache(expire=settings.cache_expire)
    async def search_objects(  # noqa: E704
        self,
        table: str,
        fields_and_values: dict[str, Any],
        order_by: str | None,
        order_option: str | None = "desc",
        objects_per_page: int = 10,
        page: int = 0,
    ) -> list[dict[str, Any]] | list[None]:
        sorting = f"{order_by}:{order_option}" if order_by else None
        query = {
            "match": {key: {"query": val} for key, val in fields_and_values.items()}
        }
        body = {"from": page, "size": objects_per_page, "query": query}
        resp = await self.call_client().search(index=table, body=body, sort=sorting)
        return self._parse_search_resp(resp)
