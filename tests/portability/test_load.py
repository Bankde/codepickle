#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper
import pytest
import asyncio

def make_skel_obj(prop={}):
    return type('obj', (object,), prop)

def make_skel_class(prop={}):
    class A():
        pass
    for k in prop:
        setattr(A, k, prop[k])
    return A

def dummy_function(x=1):
    return x + 1

class Test(helper.PickleTestLoad):
    def test_bug_708901(self):
        f = self.loads(self.obj["f"])
        f()

    def test_bug_1333982(self):
        f = self.loads(self.obj["f"])
        with pytest.raises(Exception) as e_info:
            f()

    def test_bug_42562(self):
        f = self.loads(self.obj["f"])
        f()

    def test_disassemble_str(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(), (6, 1))
        
    def test_disassemble_bytes(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(3), 1)

    def test_disassemble_class(self):
        C = self.loads(self.obj["C"])
        C.sm(1)
        C.sm(2)
        C.cm(1)
        self.assertEqual(C.x, True)
        C.cm(2)
        self.assertEqual(C.x, False)

    def test_disassemble_instance_method(self):
        inst = self.loads(self.obj["inst"])
        o = make_skel_obj({"x": None})
        inst(o, 1)
        self.assertEqual(o.x, True)

    def test_disassemble_static_method(self):
        sm = self.loads(self.obj["sm"])
        sm(1)
        sm(3)

    def test_disassemble_class_method(self):
        cm = self.loads(self.obj["cm"])
        cls = make_skel_class()
        cls.cm = cm
        # Unable to check original cls class
        cls.cm(1)
        cls.cm(3)

    def test_disassemble_generator(self):
        g = self.loads(self.obj["g"])
        gi = g(3)
        self.assertEqual(next(gi), 3)
        with pytest.raises(StopIteration) as e_info:
            next(gi)

    def test_disassemble_generator(self):
        g = self.loads(self.obj["g"])
        gi = g(3)
        self.assertEqual(next(gi), 3)
        with pytest.raises(StopIteration) as e_info:
            next(gi)

    def test_disassemble_async_generator(self):
        ag = self.loads(self.obj["ag"])
        loop = asyncio.get_event_loop()
        agi = ag(3)
        fut = anext(agi)
        res = loop.run_until_complete(fut)
        self.assertEqual(res, 3)
        with pytest.raises(StopAsyncIteration) as e_info:
            fut = anext(agi)
            loop.run_until_complete(fut)

    def test_disassemble_coroutine(self):
        co = self.loads(self.obj["co"])
        coro = co(1)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro)

    def test_disassemble_fstring(self):
        fstr = self.loads(self.obj["fstr"])
        self.assertEqual(fstr(12, 34, [], []), '12   34 [] []  ')

    def test_disassemble_try_finally(self):
        ftf = self.loads(self.obj["ftf"])
        ftfc = self.loads(self.obj["ftfc"])
        ftfr = self.loads(self.obj["ftfr"])
        self.assertEqual(ftf(3, dummy_function), 3)
        self.assertEqual(ftfc(dummy_function), 1)
        self.assertEqual(ftfr(5, dummy_function), 2)

if __name__ == "__main__":
    unittest.main()