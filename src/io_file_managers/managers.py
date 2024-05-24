from typing import AsyncGenerator

import aiohttp
import aiofiles
from aiohttp_socks import ProxyConnector

from core.settings import settings
from core.exceptions import StreamFail
from .abstract import IOFileManagerABC

class IOTorFileManager(IOFileManagerABC):

    def __init__(self):
        self.headers = {"Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Encoding": r"gzip, deflate, br", "Connection": "keep-alive"}

    async def download_file(self, url: str) -> None:
        socks_conn = ProxyConnector(host=settings.proxy_host, port=settings.proxy_port)
        async with aiohttp.ClientSession(connector=socks_conn) as tor_session:
            async with tor_session.get(url,
                                   headers=self.headers):
                async with aiofiles.open(hash(url), 'wb') as f:
                    async for chunk in tor_session.content.iter_chunked(settings.chunk_size):
                        await f.write(chunk)

    async def stream_file(self, url: str) -> AsyncGenerator[bytes, None, None]:
        socks_conn = ProxyConnector(host=settings.proxy_host, port=settings.proxy_port)
        async with aiohttp.ClientSession(connector=socks_conn) as tor_session:
            async with tor_session.get(url,
                                   headers=self.headers):
                async for chunk in tor_session.content.iter_chunked(settings.chunk_size):
                    try:
                        yield chunk
                    except Exception:
                        raise StreamFail(detail=Exception)