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

    def test_arith_ops(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(int(f(11)), 5)

    def test_logical_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f(4), (False, True, False))
        self.assertTupleEqual(f(3), (False, True, True))

    def test_comp_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f(5), (True, False, False, False, True, True))

    def test_identity_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f(None), (True, False))

    def test_member_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f(3,[3,4,5]), (True, False))

    def test_bitwise_ops(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(11), -16)

    def test_dataType(self):
        f = self.loads(self.obj["f"])
        o = f()
        self.assertEqual(o[0],"test")
        self.assertEqual(o[1],5)
        self.assertAlmostEqual(o[2],4.3)
        self.assertEqual(o[3],complex(3,4))
        self.assertTupleEqual(o[4:7], ([1,2,3],(1,2),range(4)))
        self.assertDictEqual(o[7], {"a":3})
        self.assertSetEqual(o[8], set([1,2,3]))
        self.assertSetEqual(o[9], frozenset([1,2,3]))
        self.assertTupleEqual(o[10:12], (True, False))
        self.assertEqual(o[12], b'test')
        self.assertEqual(o[13], bytearray(b'test'))
        self.assertEqual(o[14].tobytes(), b'test')
        self.assertEqual(o[15], None)

    def test_typeCast(self):
        f = self.loads(self.obj["f"])
        o = f(3.4)
        self.assertEqual(o[0], 3)
        self.assertAlmostEqual(o[1], 3.4)
        self.assertEqual(o[2], '3.4')

    def test_list_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f([1,2,3,4]),
            ([5, 4, 3], [1, 5, 4, 3, 3, 2, 1, 1, 2, 3], [5, 5, 5, 5], 1, 4, 4, [2]))

    def test_tuple_ops(self):
        f = self.loads(self.obj["f"])
        self.assertTupleEqual(f((1,2,3,4)),
            ((1, 2, 3, 4), (1, 2, 3, 4), 1, 4, 4, (2,), 1, 2, 3))

    def test_set_ops(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(set([1,2,3,4])),
            ({1, 2, 3, 4}, True, True, 5, 1, {4}, {1, 2, 3}, False, {4}, {1, 2, 3, 4}))

    def test_dict_ops(self):
        f = self.loads(self.obj["f"])
        d = {"a":10, "b":9, "c":8}
        o = f(d)
        self.assertDictEqual(o[0], {'a': 10, 'b': 12, 'c': 8, 'x': {'xx': 13}})
        self.assertTupleEqual(o[1:3], (10, 10))
        self.assertListEqual(list(o[3]), list(['a', 'b', 'c', 'x']))
        # Ignore o[4] since it may be random.

    def test_loop(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(10), 30)

    def test_condition(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(5), -11)

    def test_func(self):
        f1 = self.loads(self.obj["f1"])
        self.assertEqual(f1(5), 14)
        f2 = self.loads(self.obj["f2"])
        f2_f = f2(5)
        self.assertEqual(f2_f(), 10)
        f3 = self.loads(self.obj["f3"])
        # No need to check result for f3
        self.assertIsNone(f3("a","b",c="c",d="d"))
        f4 = self.loads(self.obj["f4"])
        self.assertEqual(f4(5), 15)

    def test_lambda(self):
        f = self.loads(self.obj["f"])
        self.assertEqual(f(5), 54)

    def test_import(self):
        f1 = self.loads(self.obj["f1"])
        # Lazy to check result of external modules
        self.assertIsNotNone(f1())
        f2 = self.loads(self.obj["f2"])
        self.assertIsNotNone(f2())
        f3 = self.loads(self.obj["f3"])
        self.assertIsNotNone(f3())
        f4 = self.loads(self.obj["f4"])
        self.assertIsNotNone(f4())

    def test_context(self):
        f = self.loads(self.obj["f"])
        from decimal import Decimal
        self.assertEqual(f(), Decimal('0.0238095238095238095238095238095238095238095'))

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