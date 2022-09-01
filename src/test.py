# #!/usr/local/bin/python3.5
import asyncio
import time
from urllib import response
import config
import aiohttp
import asyncio
import string
import random

conf = config.Config('config.json');

httpServeConf = (conf.hostName, conf.hostPort)
url = 'http://%s:%s' % (conf.hostName, conf.hostPort)

print(time.asctime(), "Test Agent Starts - ", url)

messageCounter = 0

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


messageLength = 10

def get_random_string_list():
    res = []
    for n in range(10):
        res.append(get_random_string(messageLength))
    return res

messageList = []
# messageList.append("from 0 to 0")
# messageList.extend(get_random_string_list())

# messageList.append("from 100 to 3")
messageList.extend(get_random_string_list())

# messageList.append("from 5 to 5")
# messageList.extend(get_random_string_list())

async def sendMessage(session, url, message):
    global messageCounter
    mId = messageCounter 
    messageCounter += 1

    requestTimeNs = time.time() * 1000

    # print(time.asctime(), "Send message - id:", mId, url, message)
    async with session.post(url, data=message) as resp:
        text = await resp.text()
        responseTimeNs = time.time() * 1000
        print(time.asctime(), "Response message id:", mId, message, " -> ", text)
        print(time.asctime(), "Execution time id:", mId, responseTimeNs - requestTimeNs, "ms")
        return text;

async def main():

    async with aiohttp.ClientSession() as session:
        tasks = []
        for message in messageList:
            tasks.append(asyncio.ensure_future(sendMessage(session, url, message)))

        original_pokemon = await asyncio.gather(*tasks)

asyncio.run(main())

