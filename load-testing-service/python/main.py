import aiohttp
import asyncio
import random
import math
import time


URL = 'http://localhost:8080/'
RPS_SEQUENCE = [5, 7, 8, 9, 8, 7, 5, 3, 2, 1, 2, 3, 5]
DURATION = len(RPS_SEQUENCE)  # sec
DELTA_T = 1  # sec

globalReqId = 0

def req_log(reqId, message):
    print("t", "{:10.4f}".format(time.time()),
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

            print(tms)

            rps = rpsFunction(t)
            print("New iteration rps count:", rpsFunction(t))

            for i in range(rps):
                task = asyncio.create_task(make_request(session, t, i))
                tasks.append(task)

            t += delta

            await asyncio.sleep(delta - (time.time() - tms))

        await asyncio.wait(tasks)

asyncio.run(loop(DURATION, DELTA_T))
