import aiohttp
import asyncio
import math
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('LOAD_TEST_RPS_SEQUENCE'))

URL = os.getenv('LOAD_TEST_URL')
RPS_SEQUENCE = json.loads(os.getenv('LOAD_TEST_RPS_SEQUENCE'))
DURATION = len(RPS_SEQUENCE)
DELTA_T = int(os.getenv('LOAD_TEST_DELTA_T'))

globalReqId = 0

def req_log(reqId, message):
    print("t", "{:10.6f}".format(time.time()),
          "|", "req_id", reqId, "|", message)


async def make_request(session, t, id):
    global globalReqId
    reqId = globalReqId
    globalReqId += 1

    message = "Req =>> | iteration_t: {} s | iteration_id: {}".format(t, id)
    req_log(reqId, message)

    sendTime = time.time()
    try:
        async with session.get(URL) as resp:
            respTime = int((time.time() - sendTime) * 1000)
            message = "Res <<= | iteration_t: {} s | iteration_id: {} | respTime: {} ms".format(t, id, respTime)
            req_log(reqId, message)
    except Exception as e:
        req_log(reqId, "Req fail")


def rpsFunction(t):
    rps_index = math.floor(t)
    if (len(RPS_SEQUENCE) <= rps_index):
        return RPS_SEQUENCE[len(RPS_SEQUENCE) - 1]

    return RPS_SEQUENCE[rps_index]


async def loop(duration, delta):
    async with aiohttp.ClientSession() as session:
        t = 0
        tasks = []

        while (t < duration):

            tms = time.time()

            print()

            rps = rpsFunction(t)
            print("New iteration rps count:", rpsFunction(t))

            for i in range(rps):
                task = asyncio.create_task(make_request(session, t, i))
                tasks.append(task)

            t += delta

            await asyncio.sleep(delta - (time.time() - tms))

        await asyncio.wait(tasks)

asyncio.run(loop(DURATION, DELTA_T))
