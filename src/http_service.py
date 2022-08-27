from distutils.command.config import config
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import config

conf = config.Config('config.json');

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
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

