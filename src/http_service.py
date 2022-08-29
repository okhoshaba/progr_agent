import asyncio
from concurrent.futures import thread
from distutils.command.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
from tokenize import String
from urllib.parse import urlparse
import time
import config
import logging

conf = config.Config('config.json');

from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name + str(conf.counter)

    conf.changeCounter()

    if(conf.counter % 2):
        print(conf.counter)
        await asyncio.sleep(10)
    

    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle)])

print(time.asctime(), "Program Agent Starts - %s:%s" % (conf.hostName, conf.hostPort))

web.run_app(app, host=conf.hostName, port=conf.hostPort)
print(time.asctime(), "Program Agent Stops - %s:%s" % (conf.hostName, conf.hostPort))
