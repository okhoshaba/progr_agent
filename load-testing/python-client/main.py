import asyncio
import utils
import sync_mode
import async_mode

URL, RPS_SEQUENCE, DELTA_T, DURATION, RPS_SEQUENCE_REPEAT, RPS_REPEAT_DELAY, LOAD_TEST_MODE = utils.getEnvConfig()

globalReqId = 0

async def main():
    print('LOAD_TEST_MODE: ', LOAD_TEST_MODE)
    if LOAD_TEST_MODE == 'async':
        await async_mode.run_async_repeat()
    else:
        await sync_mode.run_sync_repeat()


if __name__ == "__main__":
    asyncio.run(main())
