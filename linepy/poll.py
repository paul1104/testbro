<<<<<<< HEAD
# -*- coding: utf-8 -*-
from .client import LineClient
from types import *

import os, sys, threading

class LinePoll(object):
    OpInterrupt = {}
    client = None

    def __init__(self, client):
        if type(client) is not LineClient:
            raise Exception("You need to set LineClient instance to initialize LinePoll")
        self.client = client
    
    def fetchOperation(self, revision, count=1):
        return self.client.poll.fetchOperations(revision, count)

    def addOpInterruptWithDict(self, OpInterruptDict):
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc
        
    def execute(self, op, threading=False):
        try:
            if threading:
                _td = threading.Thread(target=self.OpInterrupt[op.type](op))
                _td.daemon = False
                _td.start()
            else:
                self.OpInterrupt[op.type](op)
        except Exception as e:
            self.client.log(str(e))
    
    def trace(self):
        try:
            operations = self.fetchOperation(self.client.revision)
        except KeyboardInterrupt:
            exit()
        except:
            return
        
        for op in operations:
            if op.type in self.OpInterrupt.keys():
                self.execute(op, False)
=======
# -*- coding: utf-8 -*-
from .client import LineClient
from types import *

import os, sys, threading

class LinePoll(object):
    OpInterrupt = {}
    client = None
    _poll = None

    def __init__(self, client):
        if type(client) is not LineClient:
            raise Exception("You need to set LineClient instance to initialize LinePoll")
        self.client = client
        self._poll = self.client.poll
    
    def fetchOperation(self, revision, count=1):
        return self._poll.fetchOperations(revision, count)

    def addOpInterruptWithDict(self, OpInterruptDict):
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc
        
    def execute(self, op):
        try:
            thd_exec = threading.Thread(target=self.OpInterrupt[op.type](op))
            thd_exec.daemon = True
            thd_exec.start()
        except Exception as e:
            self.client.log(str(e))
    
    def trace(self):
        try:
            operations = self.fetchOperation(self.client.revision)
        except KeyboardInterrupt:
            exit()
        except:
            return
        
        for op in operations:
            if op.type in self.OpInterrupt.keys():
                self.execute(op)
            
>>>>>>> 9965d22e728aef2765228b3c149e500e6d16b7c3
            self.client.revision = max(op.revision, self.client.revision)