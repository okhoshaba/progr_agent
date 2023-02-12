from dotenv import load_dotenv
import os
import json

load_dotenv()

URL = os.getenv('LOAD_TEST_URL')

if not URL:
    raise print(
        ".env variables not found, please read README and create correct .env file")

RPS_SEQUENCE = json.loads(os.getenv('LOAD_TEST_RPS_SEQUENCE'))
DELTA_T = float(os.getenv('LOAD_TEST_DELTA_T'))
DURATION = len(RPS_SEQUENCE) * DELTA_T

RPS_SEQUENCE_REPEAT = int(os.getenv('LOAD_TEST_RPS_SEQUENCE_REPEAT'))
RPS_REPEAT_DELAY = float(os.getenv('LOAD_TEST_RPS_REPEAT_DELAY'))
LOAD_TEST_MODE = os.getenv('LOAD_TEST_MODE')

def getEnvConfig():
    return URL, RPS_SEQUENCE, DELTA_T, DURATION, RPS_SEQUENCE_REPEAT, RPS_REPEAT_DELAY, LOAD_TEST_MODE