#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import subprocess
import re
from collections import defaultdict
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=int, choices=[0,1], required=True, help="0 to serialize, 1 to deserialize")
parser.add_argument('--pkg', type=int, choices=[0,1], default=0, help="0 for cloudpickle, 1 to codepickle")
args = parser.parse_args()

code = args.pkg
mode = args.mode

print("Testing version: ", sys.version)

dir_path = os.path.dirname(os.path.realpath(__file__))
test_folder = os.path.join(dir_path, "serialize")
testname_re = re.compile("test_(.*).py")
errorTxt = set() # Remove duplicate error
files = os.listdir(test_folder)

if mode == 0: #serialize
    for file in files:
        m = re.match(testname_re, file)
        if m == None: continue
        testset = m.group(1)
        testFileName = file

        try:
            print("-----------------")
            print(testFileName)
            subprocess.check_output(['python', os.path.join(dir_path, 'serialize.py'), str(code), testFileName])
        except Exception as e:
            print(e)
            print("%s: Fail (serialize)" % (testset))
            continue

if mode == 1: # deserialize
    for file in files:
        m = re.match(testname_re, file)
        if m == None: continue
        testset = m.group(1)
        testFileName = file
        
        try:
            subprocess.check_output(['python', os.path.join(dir_path, 'deserialize.py'), str(code), testFileName])
        except:
            print("%s: Fail (deserialize)" % (testset))
            continue

        print("%s: Pass" % (testset))