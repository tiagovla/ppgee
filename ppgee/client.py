import aiohttp
import asyncio
import logging
from ppgee.errors import RequestException

logger = logging.getLogger(__name__)


class PPGEE:
    def __init__(self, user: str, password: str) -> None:
        self.user = user
        self.password = password
        self.session: aiohttp.ClientSession

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        await self.login()
        return self

    async def _request(self, method: str, url: str, **kwargs) -> str:
        async with self.session.request(method, url, **kwargs) as resp:
            if resp.status != 200:
                raise RequestException(
                    f"Request to url {url} with method {method} failed with status code {resp.status}."
                )
            return await resp.text()

    async def login(self) -> str:
        logger.debug("Sending request to login.")
        data = {"login": self.user, "senha": self.password}
        return await self._request(
            "post", "https://www.ppgee.ufmg.br/ppgeenet/login.php", data=data
        )

    async def frequency(self) -> str:
        logger.debug("Sending request to frequency.")
        return await self._request(
            "get", "https://www.ppgee.ufmg.br/ppgeenet/afreq.php"
        )

    async def logoff(self) -> str:
        logger.debug("Sending request to logoff.")
        return await self._request(
            "get", "https://www.ppgee.ufmg.br/ppgeenet/logoff.php"
        )

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.logoff()
        await asyncio.sleep(1)
        if self.session:
            await self.session.close()
