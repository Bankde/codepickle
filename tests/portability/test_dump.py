#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import unittest
import helper

class Test(helper.PickleTestDump):
    def test_sequence_unpacking_error(self):
        def func():
            return (1, -1) or (-1, 1)
        self.obj["f1"] = self.dumps(func)

    def test_import(self):
        succeed = [
            'import sys',
            'import os, sys',
            'import os as bar',
            'import os.path as bar',
            'from sys import stdin, stderr, stdout',
            'from sys import (stdin, stderr,\nstdout)',
            'from sys import (stdin, stderr,\nstdout,)',
            'from sys import (stdin\n, stderr, stdout)',
            'from sys import (stdin\n, stderr, stdout,)',
            'from sys import stdin as si, stdout as so, stderr as se',
            'from sys import (stdin as si, stdout as so, stderr as se)',
            'from sys import (stdin as si, stdout as so, stderr as se,)',
            ]
        for idx, stmt in enumerate(succeed):
            func_code = "def f():\n    " + stmt + "\n    return 1"
            ld = {}
            exec(func_code, globals(), ld)
            func = ld["f"]
            self.obj[str(idx)] = self.dumps(func)

    def test_subscripts(self):
        class str_map(object):
            def __init__(self):
                self.data = {}
            def __getitem__(self, key):
                return self.data[str(key)]
            def __setitem__(self, key, value):
                self.data[str(key)] = value
            def __delitem__(self, key):
                del self.data[str(key)]
            def __contains__(self, key):
                return str(key) in self.data
        self.obj["c"] = self.dumps(str_map)

    def test_single_statement(self):
        def f1():
            1+2
        def f2():
            1+2 # One plus two
        def f3():
            1;2
        def f4():
            import sys; sys
        def f5():
            pass
        def f6():
            while False:
                pass
        def d1(x):
            pass
        def d2(x):
            pass
        def f7(x=0):
            if x:
                d1(x)
        def f8(x=0):
            if x:
                d1(x)
            else:
                d2(x)
        class C:
            pass
        def f9():
            c = '''
                a=1
                b=2
                c=3
                '''
        self.obj["f1"] = self.dumps(f1)
        self.obj["f2"] = self.dumps(f2)
        self.obj["f3"] = self.dumps(f3)
        self.obj["f4"] = self.dumps(f4)
        self.obj["f5"] = self.dumps(f5)
        self.obj["f6"] = self.dumps(f6)
        self.obj["f7"] = self.dumps(f7)
        self.obj["f8"] = self.dumps(f8)
        self.obj["c"] = self.dumps(C)
        self.obj["f9"] = self.dumps(f9)



if __name__ == "__main__":
    unittest.main()