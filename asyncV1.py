import asyncio
import ssl
import aiohttp
import json

from requests import session


items = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
url = 'https://fakestoreapi.com/products/{}'
result = []



async def getSymbols():
    async with aiohttp.ClientSession() as session:
        for item in items:
            print(item)
            print(f'Working with {item} by url - "https://fakestoreapi.com/products/{item}" now.')
            response = await session.get(url.format(item), ssl=False)
            result.append( await response.json() )

asyncio.run(getSymbols())
