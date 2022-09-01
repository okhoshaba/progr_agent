from distutils.command.config import config
import json
from random import random

class Config:
    def __init__(self, path):
        f = open(path)
        config = json.load(f)
        f.close()

        self.json = config

        self.hostName = config['ip']
        self.hostPort = config['port']

        self.delayFrom = config['from']
        self.delayTo = config['to']

        self.counter = 0
    
    def changeDelay(self, delayFrom, delayTo):
        self.delayFrom = delayFrom
        self.delayTo = delayTo

    def getDelay(self):
        delay = self.delayTo + ( self.delayTo - self.delayFrom ) * random()
        return delay / 1000