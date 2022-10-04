import aiohttp
import logging
from ppgee.http import HttpClient
from ppgee.pages import FrequencyPage

logger = logging.getLogger(__name__)


class PPGEE:
    def __init__(self, user: str, password: str) -> None:
        self.user = user
        self.password = password
        self.session: aiohttp.ClientSession
        self.http: HttpClient

    async def start(self):
        self.session = aiohttp.ClientSession()
        self.http = HttpClient(self.session)

    async def close(self):
        if self.session:
            await self.session.close()

    async def __aenter__(self):
        await self.start()
        await self.login()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.logoff()
        await self.close()

    async def login(self) -> str:
        logger.info("Logging in...")
        return await self.http.login(self.user, self.password)

    async def frequency(self) -> FrequencyPage:
        logger.info("Requesting frequency page...")
        html = await self.http.frequency()
        return FrequencyPage(html, self.http.frequency_confirmation)

    async def logoff(self) -> str:
        logger.info("Logging off...")
        return await self.http.logoff()
