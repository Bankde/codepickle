#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper
import pytest

async def async_gen(x):
    yield x

def getlen(a):
    # GET_LEN
    match a:
        case [1,2,3]: 
            return 1
        
def match_mapping(a):
    # MATCH_MAPPING
    match a:
        case {"A":"B"}: 
            return 1

def match_sequence(a):
    # MATCH_SEQUENCE
    match a:
        case [1,2,3]: 
            return 1

def match_keys(a):
    # MATCH_KEYS
    match a:
        case {"A":"B"}:
            return 1

def copy_dict_without_keys(a, b):
    # COPY_DICT_WITHOUT_KEYS
    match a:
        case {"A":"B", **b}:
            return 1
        
def match_class(typ):
    # MATCH_CLASS
    match typ():
        case object():
            return 1
    return 5

async def async_gen_wrap():
    # ASYNC_GEN_WRAP
    yield 1

def rot_n():
    # ROT_N
    x = {"y": 1}
    z = 1
    match x:
        case {"y": (0 as y) | (1 as y)}:
            z = 0
    return z

class Test_310(helper.PickleTestDump):

    def test_disassemble_async_generator(self):
        self.obj["ag"] = self.dumps(async_gen)

    def test_op_match(self):
        self.obj["getlen"] = self.dumps(getlen)
        self.obj["match_mapping"] = self.dumps(match_mapping)
        self.obj["match_sequence"] = self.dumps(match_sequence)
        self.obj["match_keys"] = self.dumps(match_keys)
        self.obj["match_class"] = self.dumps(match_class)

    def test_op_copy_dict_no_keys(self):
        self.obj["copy_dict_without_keys"] = self.dumps(copy_dict_without_keys)

    def test_op_async_gen_wrap(self):
        self.obj["async_gen_wrap"] = self.dumps(async_gen_wrap)

    def test_op_rotN(self):
        self.obj["rot_n"] = self.dumps(rot_n)

if __name__ == "__main__":
    unittest.main()