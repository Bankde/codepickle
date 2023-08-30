#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper

def get_tb():
    def _error():
        try:
            1 / 0
        except Exception as e:
            tb = e.__traceback__
        return tb

    tb = _error()
    while tb.tb_next:
        tb = tb.tb_next
    return tb

TRACEBACK_CODE = get_tb().tb_frame.f_code

class _C:
    def __init__(self, x):
        self.x = x == 1

    @staticmethod
    def sm(x):
        x = x == 1

    @classmethod
    def cm(cls, x):
        cls.x = x == 1

def _f(a):
    print(a)
    return 1

def bug708901():
    for res in range(1,
                     10):
        pass

def bug1333982(x=[]):
    assert 0, ([s for s in x] +
              [1])
    pass

def bug42562():
    None

def stmt_str():
    x = 5
    x + 1
    x = x + 1
    x: int = 1
    y: _f(1)
    lst = [0]*5
    lst[_f(0)]: int = 1
    x = 0
    while 1:
        x += 1
        # Insert if-break to stop execution while conserving jump absolute
        if x > 5:
            break
    return x, lst[_f(0)]

def _fstring(a, b, c, d):
    return f'{a} {b:4} {c!r} {d!r:4}'

def _tryfinally(a, b):
    try:
        return a
    finally:
        b()

def _tryfinallyconst(b):
    try:
        return 1
    finally:
        b()

def _tryfinallyreal(a, b):
    try:
        a
    finally:
        return b()

def _g(x):
    yield x

async def _ag(x):
    yield x

async def _co(x):
    async for item in _ag(x):
        pass

def _h(y):
    def foo(x):
        '''funcdoc'''
        return [x + z for z in y]
    return foo

def load_test(x, y=0):
    a, b = x, y
    return a, b

def loop_test():
    for i in [1, 2, 3] * 3:
        load_test(i)

def extended_arg_quick():
    *_, _ = ...

class Test(helper.PickleTestDump):
    def test_bug_708901(self):
        self.obj["f"] = self.dumps(bug708901)

    def test_bug_1333982(self):
        self.obj["f"] = self.dumps(bug1333982)
        
    def test_bug_42562(self):
        self.obj["f"] = self.dumps(bug42562)

    def test_disassemble_str(self):
        self.obj["f"] = self.dumps(stmt_str)

    def test_disassemble_bytes(self):
        self.obj["f"] = self.dumps(_f)

    def test_disassemble_class(self):
        self.obj["C"] = self.dumps(_C)

    def test_disassemble_instance_method(self):
        self.obj["inst"] = self.dumps(_C.__init__)

    def test_disassemble_static_method(self):
        self.obj["sm"] = self.dumps(_C.sm)

    def test_disassemble_class_method(self):
        self.obj["cm"] = self.dumps(_C.cm)

    def test_disassemble_generator(self):
        self.obj["g"] = self.dumps(_g)

    def test_disassemble_async_generator(self):
        self.obj["ag"] = self.dumps(_ag)

    def test_disassemble_coroutine(self):
        self.obj["co"] = self.dumps(_co)

    def test_disassemble_fstring(self):
        self.obj["fstr"] = self.dumps(_fstring)

    def test_disassemble_try_finally(self):
        self.obj["ftf"] = self.dumps(_tryfinally)
        self.obj["ftfc"] = self.dumps(_tryfinallyconst)
        self.obj["ftfr"] = self.dumps(_tryfinallyreal)

if __name__ == "__main__":
    unittest.main()