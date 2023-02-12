import aiohttp
import asyncio
import math
import time
from dotenv import load_dotenv
import threading
import utils

URL, RPS_SEQUENCE, DELTA_T, DURATION, RPS_SEQUENCE_REPEAT, RPS_REPEAT_DELAY, LOAD_TEST_MODE = utils.getEnvConfig()

globalReqId = 0

def req_log(reqId, message):
    print("t: ", "{:10.6f} s | req_id: {:10.0f} | {}".format(
        time.time(), reqId, message))


async def make_request(t, id):
    # global globalReqId
    reqId = 1
    # globalReqId += 1

    message = "Req =>> | iteration_t: {:10.3f} s | iteration_id: {}".format(t, id)
    req_log(reqId, message)

    async with aiohttp.ClientSession() as session:
        sendTime = time.time()
        try:
            async with session.get(URL) as resp:
                respTime = int((time.time() - sendTime) * 1000)
                message = "Res <<= | iteration_t: {:10.3f} s | iteration_id: {} | respTime: {} ms".format(
                    t, id, respTime)
                req_log(reqId, message)
        except Exception as e:
            req_log(reqId, "Req fail")

async def make_request_sync(session, t, id):
    # global globalReqId
    reqId = 1
    # globalReqId += 1

    message = "Req =>> | iteration_t: {:10.3f} s | iteration_id: {}".format(t, id)
    req_log(reqId, message)

    sendTime = time.time()
    try:
        async with session.get(URL) as resp:
            respTime = int((time.time() - sendTime) * 1000)
            message = "Res <<= | iteration_t: {:10.3f} s | iteration_id: {} | respTime: {} ms".format(
                t, id, respTime)
            req_log(reqId, message)
    except Exception as e:
        req_log(reqId, "Req fail")


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

async def run_sync_rps(delta):
    async with aiohttp.ClientSession() as session:

        t = 0

        for rps in RPS_SEQUENCE:

            print("\nNew iteration rps count:", rps)

            t_start = time.time()
            i = 0
            stopwatch = time.time() - t_start
            while i < rps and stopwatch < delta:
                await asyncio.create_task(make_request_sync(session, t, i))
                i += 1
                stopwatch = time.time() - t_start

    
            print('Drop requests: {}'.format(rps - i))

            t += delta

            await asyncio.sleep(max(0, delta - (time.time() - t_start)))


async def run_sync_repeat():
    for i in range(RPS_SEQUENCE_REPEAT):

        print("\nStart sequence id: {}".format(i))

        await run_sync_rps(DELTA_T)

        print("\nEnd sequence id: {}".format(i))
        print("sleep {:10.3f} sec".format(RPS_REPEAT_DELAY))
        await asyncio.sleep(RPS_REPEAT_DELAY)


async def main():
    print('LOAD_TEST_MODE: ', LOAD_TEST_MODE)
    if LOAD_TEST_MODE == 'async':
        await run_async_repeat()
    else:
        await run_sync_repeat()


if __name__ == "__main__":
    asyncio.run(main())
