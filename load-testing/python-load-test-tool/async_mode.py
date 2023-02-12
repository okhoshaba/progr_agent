import utils
import aiohttp
import asyncio
import time
import threading
import math

URL, RPS_SEQUENCE, DELTA_T, DURATION, RPS_SEQUENCE_REPEAT, RPS_REPEAT_DELAY, LOAD_TEST_MODE = utils.getEnvConfig()

globalReqId = 0

async def make_request(t, id):
    global globalReqId
    reqId = globalReqId
    globalReqId += 1

    message = "Req =>> | iteration_t: {:10.3f} s | iteration_id: {}".format(t, id)
    utils.req_log(globalReqId, message)

    async with aiohttp.ClientSession() as session:
        sendTime = time.time()
        try:
            async with session.get(URL) as resp:
                respTime = int((time.time() - sendTime) * 1000)
                message = "Res <<= | iteration_t: {:10.3f} s | iteration_id: {} | respTime: {} ms".format(
                    t, id, respTime)
                utils.req_log(reqId, message)
        except Exception as e:
            utils.req_log(reqId, "Req fail")

def rps_function(t):
    rps_index = math.floor(t / DURATION * len(RPS_SEQUENCE))
    if (len(RPS_SEQUENCE) <= rps_index):
        return RPS_SEQUENCE[len(RPS_SEQUENCE) - 1]

    return RPS_SEQUENCE[rps_index]


async def run_async_rps(duration, delta):
    print("Run rps sequence in async mode")

    async with aiohttp.ClientSession() as session:
        t = 0
        threads = []

        while (t < duration):

            tms = time.time()

            print()

            rps = rps_function(t)
            print("New iteration rps count:", rps_function(t))

            for i in range(rps):
                req_thread = threading.Thread(target=make_request_thread, args=(t, i))
                req_thread.start()
                threads.append(req_thread)

            t += delta

            await asyncio.sleep(delta - (time.time() - tms))

        for t in threads:
            t.join()

async def run_async_repeat():
    for i in range(RPS_SEQUENCE_REPEAT):
        print("\nStart sequence id: {}".format(i))
        await run_async_rps(DURATION, DELTA_T)

        print("\nEnd sequence id: {}".format(i))
        print("sleep {:10.3f} sec".format(RPS_REPEAT_DELAY))
        await asyncio.sleep(RPS_REPEAT_DELAY)

def make_request_thread(t, i):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(make_request(t, i))
    loop.close()