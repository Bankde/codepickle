#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper
import pytest

def check_eg_match():
    # CHECK_EG_MATCH
    try:
        1/0
        a = 5
    except* Exception as e:
        a = 1
    return a

def prep_reraise_star():
    # PREP_RERAISE_STAR
    try:
        1/0
        a = 5
    except* Exception:
        a = 1
    return a

def swap():
    # SWAP
    try:
        1/0
        a = 2
    except* Exception as e:
        a = 5
    return a

class Test_311(helper.PickleTestDump):

    def test_op_context_except_star(self):
        self.obj["check_eg_match"] = self.dumps(check_eg_match)
        self.obj["prep_reraise_star"] = self.dumps(prep_reraise_star)
        self.obj["swap"] = self.dumps(swap)

if __name__ == "__main__":
    unittest.main()