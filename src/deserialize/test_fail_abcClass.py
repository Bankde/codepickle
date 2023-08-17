import unittest
tc = unittest.TestCase()

import abc
class TestClass():
    def testObj(self, obj):
        Cls = obj
        inst = Cls()
        tc.assertEqual(inst.some_method(), 'it works!')
        tc.assertEqual(Cls.some_classmethod(), 'it works!')
        tc.assertEqual(Cls.some_staticmethod(), 'it works!')
        tc.assertEqual(inst.some_property, 'it works!')