import asyncio
import aiohttp

class AsyncRequest:
  async def get_all(self, *urls: str):
    """Make GET request to all the given urls and wait for their responses in parallel"""
    async with aiohttp.ClientSession() as session:
      return await asyncio.gather(*[
        self.__fetch(session, url) for url in urls
      ])

  async def __fetch(self, session: aiohttp.ClientSession , url: str):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.json()