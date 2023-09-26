#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper

def arithmetic_ops(i):
    j = 3
    j = 4+2
    i += j
    i -= 5
    i *= 4
    i /= 2
    i = i % 9
    i = i ** 2
    i = i // 7
    return i

def logical_ops(i):
    x = i < 3 and i < 5
    y = i < 3 or i < 5
    z = not(i > 3)
    return (x,y,z)

def comp_ops(i):
    a = (i == 5)
    b = (i != 5)
    c = (i < 5)
    d = (i > 5)
    e = (i <= 5)
    f = (i >= 5)
    return (a,b,c,d,e,f)

def identity_ops(i):
    a = (i is None)
    b = (i is not None)
    return (a,b)

def member_ops(i, arr):
    a = (i in arr)
    b = (i not in arr)
    return (a,b)

def bitwise_ops(i):
    i &= 5
    i |= 4
    i ^= 3
    i = ~i
    i >>= 3
    i <<= 4
    return i

def dataType():
    a = "test"
    b,c,d = 5, 4.3, complex(3,4)
    e,f,g = [1,2,3], (1,2), range(4)
    h = {"a": 3}
    i,j = set([1,2,3]), frozenset([1,2,3])
    k,l = True, False
    m,n,o = b'test', bytearray(b'test'), memoryview(b"test")
    p = None
    return (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)

def typeCasting(x):
    a = int(x)
    b = float(x)
    c = str(x)
    return (a,b,c)

def list_ops(ll):
    a = ll[0]
    b = ll[-1]
    c = len(ll)
    d = ll[1:2]
    ll[1] = 3
    ll.insert(1, 5)
    ll.append(3)
    ll.extend([3,2,1])
    ll.extend((1,2,3))
    ll.remove(3)
    ll.pop(2)
    ll2 = ll.copy()
    ll.clear()
    ll = ll + [3,4,5]
    ll.reverse()
    ll3 = [ll[0]]*4
    return (ll, ll2, ll3, a,b,c,d)

def tuple_ops(ll):
    a = ll[0]
    b = ll[-1]
    c = len(ll)
    d = ll[1:2]
    ll2 = tuple(ll)
    e,f,g = ll[:3]
    return (ll, ll2, a,b,c,d,e,f,g)

def set_ops(s):
    a = 1 in s
    s.add(10)
    b = 10 in s
    c = 0
    for i in s:
        c += 1
    s.remove(10)
    s.discard(12343543)
    s2 = set([1])
    d = s2.pop()
    s2.clear()
    del s2
    s3 = set([1,2,3])
    e = s.difference(s3)
    f = s.intersection(s3)
    g = s.issubset(s3)
    h = s.symmetric_difference(s3)
    i = s.union(s3)
    return (s, a,b,c,d,e,f,g,h,i)

def dict_ops(dic):
    a = dic["a"]
    b = dic.get("a")
    c = dic.keys()
    dic["b"] = 12
    dic.update({"x":{"xx": 13}, "y":14, "z":15})
    dic.pop("y")
    d = dic.popitem()
    return (dic, a,b,c,d)

def loop(i):
    t = 0
    for idx in range(i):
        t *= idx
    while t > 10:
        t += 2
        t //= 4
    for idx in range(i):
        if t > 20:
            break
        elif t == 15:
            t += 1
            continue
        t += 10
    return t

def condition(i):
    a = 0
    if i > 5:
        a += 5
    if i > 3:
        a += 3
    elif i > 0:
        a -= 3
    else:
        a = 0
    a = a + 4 if a > 4 else a - 4
    if a > 10:
        pass
        a += 10
    else:
        a -= 10
    return a

def tmp_func(i, j=0):
    return i+j

def func_chain(i):
    return tmp_func(i) + tmp_func(i, 4)

def func_nested(i):
    def tmp_func():
        return i + 5
    return tmp_func

def tmp_func_kwargs(**kwargs):
    for k in kwargs:
        print(k, kwargs[k])

def func_arg_kwarg(*args, **kwargs):
    print(*args)
    tmp_func_kwargs(**kwargs)

def func_recursion(i):
    if i <= 0:
        return 0
    return i + func_recursion(i-1)

def func_with_lambda(i):
    x = lambda j,k: (j+i)*k
    return x(13, 3)

def func_with_import_1():
    import numpy
    return numpy.array([1,2,3])

def func_with_import_2():
    import numpy as np
    return np.array([1,2,3])

def func_with_import_3():
    from numpy import random
    return random.randint(1,2)

def func_with_import_4():
    from numpy.random import randint
    return randint(1,2)

def func_with_context():
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

class TClass:
    def __init__(self, x):
        self.x = x == 1

    @staticmethod
    def sm(x):
        x = x == 1

    @classmethod
    def cm(cls, x):
        cls.x = x == 1

def gen(x):
    yield x

async def async_gen(x):
    yield x

async def coroutine(x):
    async for item in async_gen(x):
        pass

def format_string(a, b, c, d):
    return f'{a} {b:4} {c!r} {d!r:4}'

def try_catch(i):
    try:
        i / 0
    except Exception as e:
        tb = e.__trace__back
    while tb.tb_next:
        tb = tb.tb_next
    return tb

def try_finally(a, b):
    try:
        return a
    finally:
        b()

def try_finallyconst(b):
    try:
        return 1
    finally:
        b()

def try_finallyreal(a, b):
    try:
        a
    finally:
        return b()

def closure(y):
    def foo(x):
        '''funcdoc'''
        return [x + z for z in y]
    return foo

class Test(helper.PickleTestDump):

    def test_arith_ops(self):
        self.obj["f"] = self.dumps(arithmetic_ops)

    def test_logical_ops(self):
        self.obj["f"] = self.dumps(logical_ops)

    def test_comp_ops(self):
        self.obj["f"] = self.dumps(comp_ops)

    def test_identity_ops(self):
        self.obj["f"] = self.dumps(identity_ops)

    def test_member_ops(self):
        self.obj["f"] = self.dumps(member_ops)

    def test_bitwise_ops(self):
        self.obj["f"] = self.dumps(bitwise_ops)

    def test_dataType(self):
        self.obj["f"] = self.dumps(dataType)

    def test_typeCast(self):
        self.obj["f"] = self.dumps(typeCasting)

    def test_list_ops(self):
        self.obj["f"] = self.dumps(list_ops)

    def test_tuple_ops(self):
        self.obj["f"] = self.dumps(tuple_ops)

    def test_set_ops(self):
        self.obj["f"] = self.dumps(set_ops)

    def test_dict_ops(self):
        self.obj["f"] = self.dumps(dict_ops)

    def test_loop(self):
        self.obj["f"] = self.dumps(loop)

    def test_condition(self):
        self.obj["f"] = self.dumps(condition)

    def test_func(self):
        self.obj["f1"] = self.dumps(func_chain)
        self.obj["f2"] = self.dumps(func_nested)
        self.obj["f3"] = self.dumps(func_arg_kwarg)
        self.obj["f4"] = self.dumps(func_recursion)

    def test_lambda(self):
        self.obj["f"] = self.dumps(func_with_lambda)

    def test_import(self):
        self.obj["f1"] = self.dumps(func_with_import_1)
        self.obj["f2"] = self.dumps(func_with_import_2)
        self.obj["f3"] = self.dumps(func_with_import_3)
        self.obj["f4"] = self.dumps(func_with_import_4)

    def test_context(self):
        self.obj["f"] = self.dumps(func_with_context)

    def test_disassemble_class(self):
        self.obj["C"] = self.dumps(TClass)

    def test_disassemble_instance_method(self):
        self.obj["inst"] = self.dumps(TClass.__init__)

    def test_disassemble_static_method(self):
        self.obj["sm"] = self.dumps(TClass.sm)

    def test_disassemble_class_method(self):
        self.obj["cm"] = self.dumps(TClass.cm)

    def test_disassemble_generator(self):
        self.obj["g"] = self.dumps(gen)

    def test_disassemble_async_generator(self):
        self.obj["ag"] = self.dumps(async_gen)

    def test_disassemble_coroutine(self):
        self.obj["co"] = self.dumps(coroutine)

    def test_disassemble_fstring(self):
        self.obj["fstr"] = self.dumps(format_string)

    def test_disassemble_try_finally(self):
        self.obj["ftf"] = self.dumps(try_finally)
        self.obj["ftfc"] = self.dumps(try_finallyconst)
        self.obj["ftfr"] = self.dumps(try_finallyreal)

if __name__ == "__main__":
    unittest.main()