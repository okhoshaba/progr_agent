import asyncio
from concurrent.futures import thread
from distutils.command.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
from random import random
from tokenize import String
from urllib.parse import urlparse
import time
import config
import logging
from aiohttp import web

conf = config.Config('config.json');

messageCounter = 0

def isCommand(sMessage):
    if(len(sMessage) != 4):
        return False

    if(sMessage[0] != 'from' and sMessage[2] != 'to'):
        return False
    
    return True

def handleCommand(sMessage):
    delayFrom = int(sMessage[1])
    delayTo = int(sMessage[3])

    res = 'error'

    if(delayFrom <= delayTo):
        conf.changeDelay(delayFrom, delayTo)
        res = 'ok'

    return web.Response(text= res)

async def handle(request):
    global messageCounter

    messageId = messageCounter
    messageCounter += 1

    print(time.asctime(), "Start handle message number - ", messageId)

    message = await request.text()
    sMessage = message.split(' ')

    print(time.asctime(), "Message #", messageId, message)

    if(isCommand(sMessage)):
        print(time.asctime(), "Message #", messageId, message, "is command")
        return handleCommand(sMessage)

    delay = conf.getDelay()
    print(time.asctime(), "Message #", messageId, "delay", delay)

    await asyncio.sleep(delay)
    
    return web.Response(text= await request.text())

app = web.Application()
app.add_routes([web.post('/', handle)])

print(time.asctime(), "Program Agent Starts - %s:%s" % (conf.hostName, conf.hostPort))

web.run_app(app, host=conf.hostName, port=conf.hostPort)
print(time.asctime(), "Program Agent Stops - %s:%s" % (conf.hostName, conf.hostPort))
