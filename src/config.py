from distutils.command.config import config
import json

class Config:
    def __init__(self, path):
        f = open(path)
        config = json.load(f)
        f.close()

        self.json = config

        self.hostName = config['hostName']
        self.hostPort = config['hostPort']

        self.counter = 0
    
    def changeCounter(self):
        self.counter += 1