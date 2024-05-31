from abc import ABC, abstractmethod
from typing import IO, Any, AsyncGenerator


class IOFileManagerABC(ABC):

    @abstractmethod
    async def download_file(self, path: str) -> None: ...  # noqa: E704

    @abstractmethod
    async def stream_file(  # noqa: E704
        self, path: str
    ) -> AsyncGenerator[IO[Any], None]: ...
