#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper

def dummy(i):
    return i

def dummy_kw(x=2):
    return x

def dummy_arg(*args):
    return args

def dummy_kwargs(**kwargs):
    return kwargs

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

##### Specific test on OP #####

def rotTwoThree():
    # ROT_TWO and ROT_THREE.
    a,b,c = 1,2,3
    c,b,a = a,b,c
    return a,b,c

def dup():
    # DUP_TOP
    a,b,c = 1,2,3
    while (a < b < c):
        b += 1
    return a

def dupTopTwo():
    # DUP_TOP_TWO
    a = [1,[2,3]]
    a[1] += [4]

def bin_matmul():
    # BINARY_MATRIX_MULTIPLY
    pass

def inplace_matmul():
    # INPLACE_MATRIX_MULTIPLY
    pass

def bin_pow(x,y):
    # BINARY_POWER
    a = bin(x)
    b = bin(y)
    return a**b

def bin_mul(x,y):
    # BINARY_MULTIPLY
    a = bin(x)
    b = bin(y)
    return a*b

def bin_mod(x,y):
    # BINARY_MODULO
    a = bin(x)
    b = bin(y)
    return a % b

def bin_add(x,y):
    # BINARY_ADD
    a = bin(x)
    b = bin(y)
    return a + b

def bin_sub(x,y):
    # BINARY_SUBTRACT
    a = bin(x)
    b = bin(y)
    return a - b

def bin_floordivide(x,y):
    # BINARY_FLOOR_DIVIDE
    a = bin(x)
    b = bin(y)
    return a // b

def bin_truedivide(x,y):
    # BINARY_TRUE_DIVIDE
    a = bin(x)
    b = bin(y)
    return a / b

def inplace_floor_divide(y):
    # INPLACE_FLOOR_DIVIDE
    x = [17]
    x[0] //= y
    return x[0]

def inplace_true_divide(y):
    # INPLACE_TRUE_DIVIDE
    x = [17]
    x[0] /= y

def getlen(a):
    # GET_LEN
    match a:
        case len([1,2,3]): 
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

def push_exc_info():
    # PUSH_EXC_INFO
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def check_exc_match():
    # CHECK_EXC_MATCH
    pass

def check_eg_match():
    # CHECK_EG_MATCH
    pass

def reraise():
    # RERAISE
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def with_except_start():
    # WITH_EXCEPT_START
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def begin_finally():
    # BEGIN_FINALLY
    pass

def before_with():
    # BEFORE_WITH
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

async def end_async_for():
    # END_ASYNC_FOR
    a = 0
    async for i in range(10):
        a += i
    return a

def inplace_add(y):
    # INPLACE_ADD
    x = [17]
    x[0] += y
    return x[0]

def inplace_sub(y):
    # INPLACE_SUBTRACT
    x = [17]
    x[0] -= y
    return x[0]

def inplace_mul(y):
    # INPLACE_MULTIPLY
    x = [17]
    x[0] *= y
    return x[0]

def inplace_mod(y):
    # INPLACE_MODULO
    x = [17]
    x[0] %= y
    return x[0]

def bin_lshift(x,y):
    # BINARY_LSHIFT
    a = bin(x)
    b = bin(y)
    return a << b

def bin_rshift(x,y):
    # BINARY_RSHIFT
    a = bin(x)
    b = bin(y)
    return a >> b

def bin_and(x,y):
    # BINARY_AND
    a = bin(x)
    b = bin(y)
    return a & b

def bin_xor(x,y):
    # BINARY_XOR
    a = bin(x)
    b = bin(y)
    return a ^ b

def bin_or(x,y):
    # BINARY_OR
    a = bin(x)
    b = bin(y)
    return a | b

def inplace_pow(y):
    # INPLACE_POWER
    x = [17]
    x[0] **= y
    return x[0]

def reader():
    for i in range(4):
        yield i

def yield_from(g):
    # YIELD_FROM
    yield from g

'''
wrap = yield_from(reader())
for i in wrap:
    print(i) # 1 to 4
'''

async def afunc(x):
    return x

async def get_awaitable(x):
    # GET_AWAITABLE
    x = await afunc(x)

def load_assert_err(x):
    # LOAD_ASSERTION_ERROR
    assert 0, ((s for s in x) + 1)
    pass

def inplace_lshift(y):
    # INPLACE_LSHIFT
    x = [17]
    x[0] <<= y
    return x[0]

async def return_generator():
    # RETURN_GENERATOR
    a = 0
    async for i in range(10):
        a += i
    return a

def inplace_rshift(y):
    # INPLACE_RSHIFT
    x = [17]
    x[0] >>= y
    return x[0]

def inplace_and(y):
    # INPLACE_AND
    x = [17]
    x[0] &= y
    return x[0]

def inplace_xor(y):
    # INPLACE_XOR
    x = [17]
    x[0] ^= y
    return x[0]

def inplace_or(y):
    # INPLACE_OR
    x = [17]
    x[0] |= y
    return x[0]

def break_loop(x):
    # BREAK_LOOP
    while True:
        if x:
            break

def with_cleanup_start():
    # WITH_CLEANUP_START
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def with_cleanup_finish():
    # WITH_CLEANUP_FINISH
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def list_to_tuple():
    # LIST_TO_TUPLE
    ll = [1,2,3]
    return (*ll,)

def pop_block():
    # POP_BLOCK
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

async def async_gen_wrap():
    # ASYNC_GEN_WRAP
    yield 1

def end_finally():
    # END_FINALLY
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def prep_reraise_star():
    # PREP_RERAISE_STAR
    try:
        pass
    except* Exception:
        pass

def rot_n():
    # ROT_N
    assert(0)

def swap():
    # SWAP
    assert(0)

def jump_abs():
    # JUMP_ABSOLUTE
    for i in range(5):
        continue
    return i

def pop_jump_if_false(i):
    # POP_JUMP_IF_FALSE
    if i == 0:
        return 0
    return pop_jump_if_false(i-1) + i

def pop_jump_forward_if_else(i):
    # POP_JUMP_FORWARD_IF_FALSE
    if i == 0:
        return 0
    return pop_jump_forward_if_else(i-1) + i

def pop_jump_if_true(i):
    # POP_JUMP_IF_TRUE
    if not i == 0:
        return 0
    return pop_jump_if_true(i-1) + i

def pop_jump_forward_if_true(i):
    # POP_JUMP_FORWARD_IF_TRUE
    if not i == 0:
        return 0
    return pop_jump_forward_if_true(i-1) + i

def is_op(x,y):
    # IS_OP
    return x is y

def contain_op(x,y):
    # CONTAINS_OP
    return x in y

def continue_loop():
    # CONTINUE_LOOP
    x = 0
    for i in range(5):
        try:
            1/0
        except:
            continue
        finally:
            x += 1
    return x

# RERAISE dup with OP_48

def setup_loop():
    # SETUP_LOOP
    x = 0
    for i in range(3):
        x += i
    return x

def copy(b):
    # COPY
    try:
        return 1
    finally:
        b()

def setup_except():
    # SETUP_EXCEPT
    try:
        1/0
    except:
        x = 5
    return x

def jump_if_not_exc_match():
    # JUMP_IF_NOT_EXC_MATCH
    try:
        1/0
    except Exception as e:
        tb = e.__traceback__
    return tb

def setup_finally():
    # SETUP_FINALLY
    try:
        1/0
    except:
        return 5

def bin_op(i):
    # BINARY_OP
    if i == 0:
        return 0
    return bin_op(i-1) + i

def send(g):
    # SEND
    # Check compile.c, this op is probably exactly same as 'YIELD_FROM'
    yield from g

def pop_jump_forward_if_not_none(x):
    # POP_JUMP_FORWARD_IF_NOT_NONE
    if x is None:
        return 1
    return 2

def gen_start():
    # GEN_START
    yield 1

def pop_jump_forward_if_none(x):
    # POP_JUMP_FORWARD_IF_NONE
    if not x is None:
        return 1
    return 2

def call_func():
    # CALL_FUNCTION
    return dummy(5)

# GET_AWAITABLE - already declared in OP_73

async def jump_backward_no_interrupt(i):
    # JUMP_BACKWARD_NO_INTERRUPT
    if i == 0:
        return i
    return await jump_backward_no_interrupt(i-1)

def load_closure(x):
    # LOAD_CLOSURE
    # pickle.dumps(load_closure)
    def test2(y):
        return x+y
    return test2

def make_cell(x):
    # MAKE_CELL
    # pickle.dumps(make_cell)
    def test2(y):
        return x+y
    return test2

# The OP_num shift by 1 number for 3.11

def load_deref(x):
    # LOAD_DEREF
    # pickle.dumps(load_deref(5))
    def test2(y):
        return x+y
    return test2

def store_deref(x):
    # STORE_DEREF
    # pickle.dumps(store_deref(5))
    def test2(y):
        nonlocal x
        x = y
        return x
    return test2

def delete_deref(x):
    # DELETE_DEREF
    # pickle.dumps(store_deref(5))
    def test2(y):
        nonlocal x
        del x
    return test2

def jump_backward():
    # JUMP_BACKWARD
    for i in range(1,10):
        pass
    return i

def call_func_kw():
    # CALL_FUNCTION_KW
    return dummy_kw(x=5)

def setup_with():
    # SETUP_WITH
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def build_list_unpack(*args):
    # BUILD_LIST_UNPACK
    x = [*args]
    return x

def copy_free_vars(y):
    # COPY_FREE_VARS
    # pickle.dumps(copy_free_vars(5))
    def foo(x):
        '''funcdoc'''
        return [x + z for z in y]
    return foo

def build_map_unpack(**kwargs):
    # BUILD_MAP_UNPACK
    x = {**kwargs}
    return x

def build_map_unpack_with_call(a, b):
    # BUILD_MAP_UNPACK_WITH_CALL
    return dummy_kwargs(**a, **b)

def resume():
    # RESUME
    return 1

def build_tuple_unpack(a, b):
    # BUILD_TUPLE_UNPACK
    return dummy_arg(*a, *b)

def match_class(typ):
    # MATCH_CLASS
    match typ():
        case object():
            return 1
    return 5

def build_set_unpack(x,y):
    # BUILD_SET_UNPACK
    return dummy_arg({*x, *y})

async def setup_async_with():
    # SETUP_ASYNC_WITH
    from decimal import Decimal, localcontext
    async with localcontext() as ctx:
        ctx.prec = 42
        x = Decimal("1") / Decimal("42")
    return x

def build_tuple_unpack_with_call(x,y):
    # BUILD_TUPLE_UNPACK_WITH_CALL
    return dummy_arg(*x, *y)

def call_method():
    # CALL_METHOD
    pass

def call_finally():
    # CALL_FINALLY
    pass

def list_extend():
    # LIST_EXTEND
    pass

def pop_finally():
    # POP_FINALLY
    pass

def set_update():
    # SET_UPDATE
    pass

def dict_merge():
    # DICT_MERGE
    pass

def dict_update():
    # DICT_UPDATE
    pass

def precall(i):
    # PRECALL
    if i == 0:
        return 0
    return precall(i-1) + i

def call(i):
    # CALL
    if i == 0:
        return 0
    return call(i-1) + i

def kw_names():
    # KW_NAMES
    pass

def pop_jump_backward_if_not_none():
    # POP_JUMP_BACKWARD_IF_NOT_NONE
    pass

def pop_jump_backward_if_none():
    # POP_JUMP_BACKWARD_IF_NONE
    pass

def pop_jump_backward_if_false():
    # POP_JUMP_BACKWARD_IF_FALSE
    pass

def pop_jump_backward_if_true():
    # POP_JUMP_BACKWARD_IF_TRUE
    pass

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

    def test_closure(self):
        self.obj["f"] = self.dumps(closure)
        c = closure(10)
        self.obj["c"] = self.dumps(c)

    def test_op_rot(self):
        self.obj["rot"] = self.dumps(rotTwoThree)
        self.obj["rotN"] = self.dumps(rot_n)
        self.obj["swap"] = self.dumps(swap)

    def test_op_dup(self):
        self.obj["dupTop"] = self.dumps(dup)
        self.obj["dupTopTwo"] = self.dumps(dupTopTwo)

    def test_op_bin(self):
        self.obj["binmatmul"] = self.dumps(bin_matmul)
        self.obj["binpow"] = self.dumps(bin_pow)
        self.obj["binmul"] = self.dumps(bin_mul)
        self.obj["binmod"] = self.dumps(bin_mod)
        self.obj["binadd"] = self.dumps(bin_add)
        self.obj["binsub"] = self.dumps(bin_sub)
        self.obj["binfloordivide"] = self.dumps(bin_floordivide)
        self.obj["bintruedivide"] = self.dumps(bin_truedivide)
        self.obj["binlshift"] = self.dumps(bin_lshift)
        self.obj["binrfshift"] = self.dumps(bin_rshift)
        self.obj["binand"] = self.dumps(bin_and)
        self.obj["binxor"] = self.dumps(bin_xor)
        self.obj["binor"] = self.dumps(bin_or)

    def test_op_inplace(self):
        self.obj["inplace_matmul"] = self.dumps(inplace_matmul)
        self.obj["inplace_floor_divide"] = self.dumps(inplace_floor_divide)
        self.obj["inplace_true_divide"] = self.dumps(inplace_true_divide)
        self.obj["inplace_add"] = self.dumps(inplace_add)
        self.obj["inplace_sub"] = self.dumps(inplace_sub)
        self.obj["inplace_mul"] = self.dumps(inplace_mul)
        self.obj["inplace_mod"] = self.dumps(inplace_mod)
        self.obj["inplace_pow"] = self.dumps(inplace_pow)
        self.obj["inplace_lshift"] = self.dumps(inplace_lshift)
        self.obj["inplace_rshift"] = self.dumps(inplace_rshift)
        self.obj["inplace_and"] = self.dumps(inplace_and)
        self.obj["inplace_xor"] = self.dumps(inplace_xor)
        self.obj["inplace_or"] = self.dumps(inplace_or)

    def test_op_getlen(self):
        self.obj["f"] = self.dumps(getlen)

    def test_op_match(self):
        self.obj["match_mapping"] = self.dumps(match_mapping)
        self.obj["match_seq"] = self.dumps(match_sequence)
        self.obj["match_keys"] = self.dumps(match_keys)
        self.obj["match_class"] = self.dumps(match_class)

    def test_op_copy_dict_no_keys(self):
        self.obj["f"] = self.dumps(copy_dict_without_keys)

    def test_op_exc(self):
        self.obj["push_exc"] = self.dumps(push_exc_info)
        self.obj["check_exc"] = self.dumps(check_exc_match)

    def test_op_eg_match(self):
        self.obj["check_eg_match"] = self.dumps(check_eg_match)

    def test_op_context_except(self):
        self.obj["reraise"] = self.dumps(reraise)
        self.obj["with_except_start"] = self.dumps(with_except_start)
        self.obj["prep_reraise_star"] = self.dumps(prep_reraise_star)
        self.obj["setup_except"] = self.dumps(setup_except)

    def test_op_context_async(self):
        self.obj["end_async_for"] = self.dumps(end_async_for)
        self.obj["setup_async_with"] = self.dumps(setup_async_with)

    def test_op_context(self):
        self.obj["before_with"] = self.dumps(before_with)
        self.obj["begin_finally"] = self.dumps(begin_finally)
        self.obj["end_finally"] = self.dumps(end_finally)
        self.obj["setup_finally"] = self.dumps(setup_finally)
        self.obj["setup_with"] = self.dumps(setup_with)

    def test_op_async(self):
        self.obj["yield_from"] = self.dumps(yield_from)
        self.obj["get_awaitable"] = self.dumps(get_awaitable)
    
    def test_op_assert(self):
        self.obj["load_assert_err"] = self.dumps(load_assert_err)

    def test_op_return_gen(self):
        self.obj["return_generator"] = self.dumps(return_generator)

    def test_op_loop(self):
        self.obj["break_loop"] = self.dumps(break_loop)
        self.obj["continue_loop"] = self.dumps(continue_loop)
        self.obj["setup_loop"] = self.dumps(setup_loop)

    def test_op_cleanup(self):
        self.obj["with_cleanup_start"] = self.dumps(with_cleanup_start)
        self.obj["with_cleanup_finish"] = self.dumps(with_cleanup_finish)

    def test_op_list(self):
        self.obj["list_to_tuple"] = self.dumps(list_to_tuple)
        self.obj["list_extend"] = self.dumps(list_extend)

    def test_op_pop_block(self):
        self.obj["f"] = self.dumps(pop_block)

    def test_op_async_gen_wrap(self):
        self.obj["f"] = self.dumps(async_gen_wrap)

    def test_op_jump(self):
        self.obj["jump_abs"] = self.dumps(jump_abs)
        self.obj["pop_jump_if_else"] = self.dumps(pop_jump_if_else)
        self.obj["pop_jump_forward_if_else"] = self.dumps(pop_jump_forward_if_else)
        self.obj["pop_jump_if_true"] = self.dumps(pop_jump_if_true)
        self.obj["pop_jump_forward_if_true"] = self.dumps(pop_jump_forward_if_true)
        self.obj["jump_if_not_exc_match"] = self.dumps(jump_if_not_exc_match)
        self.obj["pop_jump_forward_if_not_none"] = self.dumps(pop_jump_forward_if_not_none)
        self.obj["pop_jump_forward_if_none"] = self.dumps(pop_jump_forward_if_none)
        self.obj["jump_backward_no_interrupt"] = self.dumps(jump_backward_no_interrupt)
        self.obj["jump_backward"] = self.dumps(jump_backward)
        self.obj["pop_jump_backward_if_not_none"] = self.dumps(pop_jump_backward_if_not_none)
        self.obj["pop_jump_backward_if_none"] = self.dumps(pop_jump_backward_if_none)
        self.obj["pop_jump_backward_if_false"] = self.dumps(pop_jump_backward_if_false)
        self.obj["pop_jump_backward_if_true"] = self.dumps(pop_jump_backward_if_true)

    def test_op_op(self):
        self.obj["is_op"] = self.dumps(is_op)
        self.obj["contain_op"] = self.dumps(contain_op)
        self.obj["bin_op"] = self.dumps(bin_op)

    def test_op_copy(self):
        self.obj["f"] = self.dumps(copy)

    def test_op_send(self):
        self.obj["f"] = self.dumps(send)

    def test_op_gen_start(self):
        self.obj["f"] = self.dumps(gen_start)

    def test_op_call(self):
        self.obj["call_func"] = self.dumps(call_func)
        self.obj["call_func_kw"] = self.dumps(call_func_kw)
        self.obj["call_method"] = self.dumps(call_method)
        self.obj["call_finally"] = self.dumps(call_finally)
        self.obj["precall"] = self.dumps(precall)
        self.obj["call"] = self.dumps(call)

    def test_op_closure(self):
        self.obj["load_closure"] = self.dumps(load_closure)
        self.obj["make_cell"] = self.dumps(make_cell)
        self.obj["load_deref"] = self.dumps(load_deref)
        self.obj["store_deref"] = self.dumps(store_deref)
        self.obj["delete_deref"] = self.dumps(delete_deref)
        self.obj["copy_free_vars"] = self.dumps(copy_free_vars)
        
    def test_op_unpack(self):
        self.obj["build_list_unpack"] = self.dumps(build_list_unpack)
        self.obj["build_map_unpack"] = self.dumps(build_map_unpack)
        self.obj["build_map_unpack_with_call"] = self.dumps(build_map_unpack_with_call)
        self.obj["build_tuple_unpack"] = self.dumps(build_tuple_unpack)
        self.obj["build_set_unpack"] = self.dumps(build_set_unpack)
        self.obj["build_tuple_unpack_with_call"] = self.dumps(build_tuple_unpack_with_call)

    def test_op_resume(self):
        self.obj["resume"] = self.dumps(resume)

    def test_op_pop_finally(self):
        self.obj["pop_finally"] = self.dumps(pop_finally)

    def test_op_set(self):
        self.obj["set_update"] = self.dumps(set_update)

    def test_op_dict(self):
        self.obj["dict_merge"] = self.dumps(dict_merge)
        self.obj["dict_update"] = self.dumps(dict_update)

    def test_op_kw_names(self):
        self.obj["kw_names"] = self.dumps(kw_names)

if __name__ == "__main__":
    unittest.main()