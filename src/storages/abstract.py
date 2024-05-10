from abc import ABC, abstractmethod
from typing import Hashable, Iterable, Mapping
from uuid import UUID


class StorageABC(ABC):

    @abstractmethod
    async def get_object_by_id(  # noqa: E704
        self,
        table: str,
        id: UUID,
    ) -> Mapping[str, Hashable] | None: ...

    @abstractmethod
    async def search_objects(  # noqa: E704
        self,
        table: str,
        fields_and_values: dict[str, Hashable],
        objects_per_page: int,
        page: int,
        order_by: str | None,
        order_option: str | None,
    ) -> Iterable[Mapping[str, Hashable]] | Iterable[None]: ...
