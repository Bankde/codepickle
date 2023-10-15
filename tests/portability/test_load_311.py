#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper
import pytest
import asyncio

class Test(helper.PickleTestLoad):
    
    def test_op_context_except_star(self):
        check_eg_match = self.loads(self.obj["check_eg_match"])
        self.assertEqual(check_eg_match(), 1)
        prep_reraise_star = self.loads(self.obj["prep_reraise_star"])
        self.assertEqual(prep_reraise_star(), 1)
        swap = self.loads(self.obj["swap"])
        self.assertEqual(swap(), 5)

if __name__ == "__main__":
    unittest.main()