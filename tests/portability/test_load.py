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

def reader():
    # For YIELD_FROM
    for i in range(4):
        yield i

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
        self.assertEqual(f(), '0.02380952381')

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

    def test_closure(self):
        f = self.loads(self.obj["f"])
        fo = f([1,2,3])
        self.assertListEqual(fo(5), [6,7,8])
        c = self.loads(self.obj["c"])
        self.assertListEqual(c(5), [6,7,8])

    def test_op_rot(self):
        rot = self.loads(self.obj["rot"])
        self.assertTupleEqual(rot(), (3,2,1))

    def test_op_dup(self):
        dupTop = self.loads(self.obj["dupTop"])
        self.assertEqual(dupTop(), 1)
        dupTopTwo = self.loads(self.obj["dupTopTwo"])
        self.assertListEqual(dupTopTwo(), [1, [2, 3, 4]])

    def test_op_bin(self):
        import numpy as np
        bin_matmul = self.loads(self.obj["bin_matmul"])
        self.assertEqual(str(bin_matmul()), str(np.array([[11,16],[19,28]])))
        bin_pow = self.loads(self.obj["bin_pow"])
        self.assertEqual(bin_pow(8,3), 512)
        bin_mul = self.loads(self.obj["bin_mul"])
        self.assertEqual(bin_mul(8,3), 24)
        bin_mod = self.loads(self.obj["bin_mod"])
        self.assertEqual(bin_mod(8,3), 2)
        bin_add = self.loads(self.obj["bin_add"])
        self.assertEqual(bin_add(8,3), 11)
        bin_sub = self.loads(self.obj["bin_sub"])
        self.assertEqual(bin_sub(8,3), 5)
        bin_floordivide = self.loads(self.obj["bin_floordivide"])
        self.assertEqual(bin_floordivide(8,3), 2)
        bin_truedivide = self.loads(self.obj["bin_truedivide"])
        self.assertAlmostEqual(bin_truedivide(6,3), 2)
        bin_lshift = self.loads(self.obj["bin_lshift"])
        self.assertEqual(bin_lshift(8,3), 64)
        bin_rshift = self.loads(self.obj["bin_rshift"])
        self.assertEqual(bin_rshift(8,3), 1)
        bin_and = self.loads(self.obj["bin_and"])
        self.assertEqual(bin_and(8,3), 0)
        bin_xor = self.loads(self.obj["bin_xor"])
        self.assertEqual(bin_xor(8,3), 11)
        bin_or = self.loads(self.obj["bin_or"])
        self.assertEqual(bin_or(8,3), 11)

    def test_op_inplace(self):
        import numpy as np
        inplace_matmul = self.loads(self.obj["inplace_matmul"])
        self.assertEqual(str(inplace_matmul()), str(np.array([[10,13],[22,29]])))
        inplace_floor_divide = self.loads(self.obj["inplace_floor_divide"])
        self.assertEqual(inplace_floor_divide(6), 2)
        inplace_true_divide = self.loads(self.obj["inplace_true_divide"])
        self.assertAlmostEqual(inplace_true_divide(17), 1)
        inplace_add = self.loads(self.obj["inplace_add"])
        self.assertEqual(inplace_add(6), 23)
        inplace_sub = self.loads(self.obj["inplace_sub"])
        self.assertEqual(inplace_sub(6), 11)
        inplace_mul = self.loads(self.obj["inplace_mul"])
        self.assertEqual(inplace_mul(6), 102)
        inplace_mod = self.loads(self.obj["inplace_mod"])
        self.assertEqual(inplace_mod(6), 5)
        inplace_pow = self.loads(self.obj["inplace_pow"])
        self.assertEqual(inplace_pow(6), 24137569)
        inplace_lshift = self.loads(self.obj["inplace_lshift"])
        self.assertEqual(inplace_lshift(6), 1088)
        inplace_rshift = self.loads(self.obj["inplace_rshift"])
        self.assertEqual(inplace_rshift(6), 0)
        inplace_and = self.loads(self.obj["inplace_and"])
        self.assertEqual(inplace_and(6), 0)
        inplace_xor = self.loads(self.obj["inplace_xor"])
        self.assertEqual(inplace_xor(6), 23)
        inplace_or = self.loads(self.obj["inplace_or"])
        self.assertEqual(inplace_or(6), 23)

    def test_op_getlen(self):
        getlen = self.loads(self.obj["getlen"])
        self.assertEqual(getlen([1,2,3]), 1)

    def test_op_match(self):
        match_mapping = self.loads(self.obj["match_mapping"])
        self.assertEqual(match_mapping({"A":"B"}), 1)
        match_sequence = self.loads(self.obj["match_sequence"])
        self.assertEqual(match_sequence([1,2,3]), 1)
        match_keys = self.loads(self.obj["match_keys"])
        self.assertEqual(match_keys({"A":"B"}), 1)
        match_mapping = self.loads(self.obj["match_mapping"])
        self.assertEqual(match_mapping({"A":"B"}), 1)
        match_class = self.loads(self.obj["match_class"])
        self.assertEqual(match_class(str), 1)

    def test_op_copy_dict_no_keys(self):
        copy_dict_without_keys = self.loads(self.obj["copy_dict_without_keys"])
        self.assertEqual(copy_dict_without_keys({"A":"B", "C":"D"}, {"C":"D"}), 1)

    def test_op_except(self):
        push_exc_info = self.loads(self.obj["push_exc_info"])
        self.assertEqual(push_exc_info(), 1)
        check_exc_match = self.loads(self.obj["check_exc_match"])
        self.assertEqual(check_exc_match(), 1)
        check_eg_match = self.loads(self.obj["check_eg_match"])
        self.assertEqual(check_eg_match(), 1)

    def test_op_context_except(self):
        reraise = self.loads(self.obj["reraise"])
        self.assertEqual(reraise(), 1)
        with_except_start = self.loads(self.obj["with_except_start"])
        self.assertEqual(with_except_start(), '0.02380952381')
        prep_reraise_star = self.loads(self.obj["prep_reraise_star"])
        self.assertEqual(prep_reraise_star(), 1)
        setup_except = self.loads(self.obj["setup_except"])
        self.assertEqual(setup_except(), 1)

    def test_op_context_async(self):
        end_async_for = self.loads(self.obj["end_async_for"])
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(end_async_for())
        self.assertEqual(r, 45)
        setup_async_with = self.loads(self.obj["setup_async_with"])
        r = loop.run_until_complete(setup_async_with())
        self.assertEqual(r, 1)

    def test_op_context_with(self):
        before_with = self.loads(self.obj["before_with"])
        self.assertEqual(before_with(), '0.02380952381')
        setup_with = self.loads(self.obj["setup_with"])
        self.assertEqual(setup_with(), '0.02380952381')

    def test_op_context_finally(self):
        begin_finally = self.loads(self.obj["begin_finally"])
        self.assertEqual(begin_finally(), 3)
        end_finally = self.loads(self.obj["end_finally"])
        self.assertEqual(end_finally(), '0.02380952381')
        setup_finally = self.loads(self.obj["setup_finally"])
        self.assertEqual(setup_finally(), 5)

    def test_op_async(self):
        yield_from = self.loads(self.obj["yield_from"])
        wrap = yield_from(reader())
        for i in wrap:
            self.assertEqual(i, [0,1,2,3][i])
        get_awaitable = self.loads(self.obj["get_awaitable"])
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(get_awaitable(5))
        print(r)
        self.assertEqual(r, 5)
    
    def test_op_assert(self):
        load_assert_err = self.loads(self.obj["load_assert_err"])
        self.assertEqual(load_assert_err(0), 1)

    def test_op_return_gen(self):
        return_generator = self.loads(self.obj["return_generator"])
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(return_generator())
        self.assertEqual(r, 45)

    def test_op_loop(self):
        break_loop = self.loads(self.obj["break_loop"])
        self.assertEqual(break_loop(True), 1)
        continue_loop = self.loads(self.obj["continue_loop"])
        self.assertEqual(continue_loop(), 5)
        setup_loop = self.loads(self.obj["setup_loop"])
        self.assertEqual(setup_loop(), 3)

    def test_op_cleanup(self):
        with_cleanup_start = self.loads(self.obj["with_cleanup_start"])
        self.assertEqual(with_cleanup_start(), '0.02380952381')
        with_cleanup_finish = self.loads(self.obj["with_cleanup_finish"])
        self.assertEqual(with_cleanup_finish(), '0.02380952381')

    def test_op_list(self):
        list_to_tuple = self.loads(self.obj["list_to_tuple"])
        self.assertTupleEqual(list_to_tuple(), (1,2,3))
        list_extend = self.loads(self.obj["list_extend"])
        self.assertListEqual(list_extend(), [1,2,3])

    def test_op_pop_block(self):
        pop_block = self.loads(self.obj["pop_block"])
        self.assertEqual(pop_block(), '0.02380952381')

    def test_op_async_gen_wrap(self):
        async_gen_wrap = self.loads(self.obj["async_gen_wrap"])
        g = async_gen_wrap()
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(anext(g))
        self.assertEqual(r, 1)

    def test_op_rotN(self):
        rot_n = self.loads(self.obj["rot_n"])
        self.assertEqual(rot_n(), 0)

    def test_op_swap(self):
        swap = self.loads(self.obj["swap"])
        self.assertEqual(swap(), 5)

    def test_op_jump(self):
        jump_abs = self.loads(self.obj["jump_abs"])
        self.assertEqual(jump_abs(), 4)
        pop_jump_if_false = self.loads(self.obj["pop_jump_if_false"])
        self.assertEqual(pop_jump_if_false(5), 15)
        pop_jump_forward_if_false = self.loads(self.obj["pop_jump_forward_if_false"])
        self.assertEqual(pop_jump_forward_if_false(5), 15)
        pop_jump_if_true = self.loads(self.obj["pop_jump_if_true"])
        self.assertEqual(pop_jump_if_true(5), 0)
        pop_jump_forward_if_true = self.loads(self.obj["pop_jump_forward_if_true"])
        self.assertEqual(pop_jump_forward_if_true(5), 0)
        jump_if_not_exc_match = self.loads(self.obj["jump_if_not_exc_match"])
        self.assertEqual(jump_if_not_exc_match(), 1)
        pop_jump_forward_if_not_none = self.loads(self.obj["pop_jump_forward_if_not_none"])
        self.assertEqual(pop_jump_forward_if_not_none(3), 2)
        pop_jump_forward_if_none = self.loads(self.obj["pop_jump_forward_if_none"])
        self.assertEqual(pop_jump_forward_if_none(None), 2)
        jump_backward_no_interrupt = self.loads(self.obj["jump_backward_no_interrupt"])
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(jump_backward_no_interrupt(5))
        self.assertEqual(r, 0)
        jump_backward = self.loads(self.obj["jump_backward"])
        self.assertEqual(jump_backward(), 9)
        pop_jump_backward_if_not_none = self.loads(self.obj["pop_jump_backward_if_not_none"])
        self.assertEqual(pop_jump_backward_if_not_none(3), 3)
        pop_jump_backward_if_none = self.loads(self.obj["pop_jump_backward_if_none"])
        self.assertEqual(pop_jump_backward_if_none(None), 3)
        pop_jump_backward_if_false = self.loads(self.obj["pop_jump_backward_if_false"])
        self.assertEqual(pop_jump_backward_if_false(False), 3)
        pop_jump_backward_if_true = self.loads(self.obj["pop_jump_backward_if_true"])
        self.assertEqual(pop_jump_backward_if_true(True), 3)

    def test_op_op(self):
        is_op = self.loads(self.obj["is_op"])
        self.assertEqual(is_op(3,3), True)
        contain_op = self.loads(self.obj["contain_op"])
        self.assertEqual(contain_op(3, [1,2,3]), True)
        bin_op = self.loads(self.obj["bin_op"])
        self.assertEqual(bin_op(5), 15)

    def test_op_copy(self):
        copy = self.loads(self.obj["copy"])
        self.assertEqual(copy(lambda: 5), 1)

    def test_op_send(self):
        send = self.loads(self.obj["send"])
        wrap = send(reader())
        for i in wrap:
            self.assertEqual(i, [0,1,2,3][i])

    def test_op_gen_start(self):
        gen_start = self.loads(self.obj["gen_start"])
        g = gen_start()
        self.assertEqual(next(g), 1)

    def test_op_call(self):
        call_func = self.loads(self.obj["call_func"])
        self.assertEqual(call_func(), 5)
        call_func_kw = self.loads(self.obj["call_func_kw"])
        self.assertEqual(call_func_kw(), 5)
        call_method = self.loads(self.obj["call_method"])
        self.assertEqual(call_method("abc"), "ABC")
        call_finally = self.loads(self.obj["call_finally"])
        self.assertEqual(call_finally(), 5)
        precall = self.loads(self.obj["precall"])
        self.assertEqual(precall(5), 15)
        call = self.loads(self.obj["call"])
        self.assertEqual(call(5), 15)

    def test_op_closure(self):
        load_closure = self.loads(self.obj["load_closure"])
        load_closure_f = self.loads(self.obj["load_closure_f"])
        self.assertEqual(load_closure(5)(7), 12)
        self.assertEqual(load_closure_f(7), 12)
        make_cell = self.loads(self.obj["make_cell"])
        make_cell_f = self.loads(self.obj["make_cell_f"])
        self.assertEqual(make_cell(5)(7), 12)
        self.assertEqual(make_cell_f(7), 12)
        load_deref = self.loads(self.obj["load_deref"])
        load_deref_f = self.loads(self.obj["load_deref_f"])
        self.assertEqual(load_deref(5)(7), 12)
        self.assertEqual(load_deref_f(7), 12)
        store_deref = self.loads(self.obj["store_deref"])
        store_deref_f = self.loads(self.obj["store_deref_f"])
        self.assertEqual(store_deref(5)(7), 7)
        self.assertEqual(store_deref_f(7), 7)
        delete_deref = self.loads(self.obj["delete_deref"])
        delete_deref_f = self.loads(self.obj["delete_deref_f"])
        self.assertEqual(load_closure(5)(7), 7)
        self.assertEqual(load_closure_f(7), 7)
        copy_free_vars = self.loads(self.obj["copy_free_vars"])
        copy_free_vars_f = self.loads(self.obj["copy_free_vars_f"])
        self.assertListEqual(copy_free_vars([1,2,3])(7), [8,9,10])
        self.assertListEqual(copy_free_vars_f(7), [8,9,10])
        
    def test_op_unpack(self):
        build_list_unpack = self.loads(self.obj["build_list_unpack"])
        self.assertListEqual(build_list_unpack(1,2,3), [1,2,3])
        build_map_unpack = self.loads(self.obj["build_map_unpack"])
        self.assertDictEqual(build_map_unpack(a=1,b=2), {"a":1, "b":2})
        build_map_unpack_with_call = self.loads(self.obj["build_map_unpack_with_call"])
        self.assertDictEqual(build_map_unpack_with_call({"A":1}, {"B":2}), {"A":1,"B":2})
        build_tuple_unpack = self.loads(self.obj["build_tuple_unpack"])
        self.assertTupleEqual(build_tuple_unpack([1,2], [3,4]), (1,2,3,4))
        build_set_unpack = self.loads(self.obj["build_set_unpack"])
        self.assertSetEqual(build_set_unpack([1,2], [3,4]), {1,2,3,4})
        build_tuple_unpack_with_call = self.loads(self.obj["build_tuple_unpack_with_call"])
        self.assertTupleEqual(build_tuple_unpack_with_call([1,2], [3,4]), (1,2,3,4))

    def test_op_resume(self):
        resume = self.loads(self.obj["resume"])
        self.assertEqual(resume(), 1)

    def test_op_pop_finally(self):
        pop_finally = self.loads(self.obj["pop_finally"])
        self.assertEqual(pop_finally(), 5)

    def test_op_set(self):
        set_update = self.loads(self.obj["set_update"])
        self.assertSetEqual(set_update(), {1,2,3})

    def test_op_dict(self):
        dict_merge = self.loads(self.obj["dict_merge"])
        self.assertDictEqual(dict_merge({"A":1}, {"B":2}), {"A":1, "B":2})
        dict_update = self.loads(self.obj["dict_update"])
        self.assertDictEqual(dict_update({"A":1}, {"B":2}), {"A":1, "B":2})

    def test_op_kw_names(self):
        kw_names = self.loads(self.obj["kw_names"])
        self.assertDictEqual(kw_names(), {'a': 'b'})

if __name__ == "__main__":
    unittest.main()