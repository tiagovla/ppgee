import aiohttp
import asyncio
import logging
from ppgee.http import HttpClient

logger = logging.getLogger(__name__)


class PPGEE:
    def __init__(self, user: str, password: str) -> None:
        self.user = user
        self.password = password
        self.session: aiohttp.ClientSession
        self.http: HttpClient

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        self.http = HttpClient(self.session)
        await self.login()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.logoff()
        await asyncio.sleep(1)
        if self.session:
            await self.session.close()

    async def login(self) -> str:
        return await self.http.login(self.user, self.password)

    async def frequency(self) -> str:
        return await self.http.frequency()

    async def frequency_confirmation(self) -> str:
        return await self.http.frequency_confirmation()

    async def logoff(self) -> str:
        return await self.http.logoff()
