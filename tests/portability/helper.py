#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys
import time
from enum import Enum

if os.getenv("PickleLib"):
    import importlib
    pickle = importlib.import_module(os.getenv("PickleLib"))
else: # Default for testing
    import cloudpickle as pickle
if pickle.__name__ == "dill":
    pickle.settings['recurse'] = True

filename = "/tmp/data.tmp"

def savePickle(obj):
    # Prevent importing whole module as much as possible
    from pickle import dumps
    from base64 import b64encode
    f = open(filename, 'wb+')
    f.write(b64encode(dumps(obj)))
    f.close()

def loadPickle():
    from pickle import loads
    from base64 import b64decode
    f = open(filename, 'rb')
    data = f.readline()
    f.close()
    return loads(b64decode(data))

'''
We use this setUp and tearDown pattern so writing testcase can be simple 
as there is no need to consider duplicated obj key across the different tests
The process run like this:
    setUpClass -> (setUp -> tearDown)* -> tearDownClass
'''
class PickleTestMain(unittest.TestCase):
    def dumps(self, *args, **kwargs):
        return pickle.dumps(*args, **kwargs)

    def loads(self, *args, **kwargs):
        return pickle.loads(*args, **kwargs)
    
class PickleTestDump(PickleTestMain):
    @classmethod
    def setUpClass(cls):
        cls.main_obj = {}

    def setUp(self):
        # Clear previous data
        self.obj = {}

    def tearDown(self):
        # Save pickled data from obj to main_obj
        new_main_obj_key = "_func_" + self._testMethodName + "_"
        for key in self.obj.keys():
            self.main_obj[new_main_obj_key + key] = self.obj[key]

    @classmethod
    def tearDownClass(cls):
        savePickle(cls.main_obj)

class PickleTestLoad(PickleTestMain):
    @classmethod
    def setUpClass(cls):
        cls.main_obj = loadPickle()

    def setUp(self):
        # Clear previous data
        self.obj = {}
        # Move respective pickled data from main_obj to obj
        cur_key = "_func_" + self._testMethodName + "_"
        for key in self.main_obj.keys():
            if key.startswith(cur_key):
                new_obj_key = key[len(cur_key):]
                self.obj[new_obj_key] = self.main_obj[key]