#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper
import pytest
import asyncio

class Test(helper.PickleTestLoad):
    
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

    def test_op_match(self):
        getlen = self.loads(self.obj["getlen"])
        self.assertEqual(getlen([1,2,3]), 1)
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

    def test_op_async_gen_wrap(self):
        async_gen_wrap = self.loads(self.obj["async_gen_wrap"])
        g = async_gen_wrap()
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(anext(g))
        self.assertEqual(r, 1)

    def test_op_rotN(self):
        rot_n = self.loads(self.obj["rot_n"])
        self.assertEqual(rot_n(), 0)

if __name__ == "__main__":
    unittest.main()