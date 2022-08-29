import requests
import time
import config

conf = config.Config('config.json');

httpServeConf = (conf.hostName, conf.hostPort)
url = 'http://%s:%s' % (conf.hostName, conf.hostPort)

print(time.asctime(), "Test Agent Starts - ", url)

messageCounter = 0
session = requests.Session()

try:
    while True:
        print(time.asctime(), "Send message")
        r = session.get(url, verify=False, timeout=0.01)  
        messageCounter += 1
        print(time.asctime(), "Response -", r.content)
except KeyboardInterrupt:
    pass


