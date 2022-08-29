from distutils.command.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import time
import config
import logging

conf = config.Config('config.json');

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        print(time.asctime(), "Recive message")
        self.send_response(200)
        self.send_header("Content-type", "text/html".encode())
        self.end_headers()
        conf.changeCounter()
        text = "Test Agent conter: {} !".format(conf.counter)
        self.wfile.write(text.encode())

httpServeConf = (conf.hostName, conf.hostPort)
myServer = HTTPServer(httpServeConf, MyServer)
print(time.asctime(), "Program Agent Starts - %s:%s" % httpServeConf)

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Program Agent Stops - %s:%s" % httpServeConf)

