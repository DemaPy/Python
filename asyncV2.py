import asyncio
import aiohttp
import json

from requests import session


items = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
url = 'https://fakestoreapi.com/products/{}'
result = []

def getTasks(session):
    tasks = []
    for item in items:
        tasks.append(session.get(url.format(item), ssl=False))
    return tasks

async def getSymbols():
    async with aiohttp.ClientSession() as session:
        tasks = getTasks(session)
        responses = await asyncio.gather(*tasks)
        for res in responses:
            result.append( await res.json() )
        
        print(result)


asyncio.run(getSymbols())
