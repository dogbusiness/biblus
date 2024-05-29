from abc import ABC, abstractmethod
from typing import AsyncGenerator, IO, Any


class IOFileManagerABC(ABC):

    @abstractmethod
    async def download_file(self, path: str) -> None:
        ...

    @abstractmethod
    async def stream_file(self, path: str) -> AsyncGenerator[IO[Any], None, None]:
        ...
