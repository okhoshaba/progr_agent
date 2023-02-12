import utils
import aiohttp
import asyncio
import time

URL, RPS_SEQUENCE, DELTA_T, DURATION, RPS_SEQUENCE_REPEAT, RPS_REPEAT_DELAY, LOAD_TEST_MODE = utils.getEnvConfig()

globalReqId = 0

async def make_request_sync(session, t, id):
    global globalReqId
    reqId = globalReqId
    globalReqId += 1

    message = "Req =>> | iteration_t: {:10.3f} s | iteration_id: {}".format(t, id)
    utils.req_log(reqId, message)

    sendTime = time.time()
    try:
        async with session.get(URL) as resp:
            respTime = int((time.time() - sendTime) * 1000)
            message = "Res <<= | iteration_t: {:10.3f} s | iteration_id: {} | respTime: {} ms".format(
                t, id, respTime)
            utils.req_log(reqId, message)
    except Exception as e:
        utils.req_log(reqId, "Req fail")

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