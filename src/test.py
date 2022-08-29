# #!/usr/local/bin/python3.5
import asyncio
import time
import config
import aiohttp
import asyncio

conf = config.Config('config.json');

httpServeConf = (conf.hostName, conf.hostPort)
url = 'http://%s:%s' % (conf.hostName, conf.hostPort)

print(time.asctime(), "Test Agent Starts - ", url)

messageCounter = 0

async def get_pokemon(session, url):
    print(time.asctime(), "Send message - ", url)
    async with session.get(url) as resp:
        text = await resp.text()
        print(text)
        return text;

async def main():

    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 20):
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        original_pokemon = await asyncio.gather(*tasks)

asyncio.run(main())

