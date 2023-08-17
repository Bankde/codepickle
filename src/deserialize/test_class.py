import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        inst = obj()
        tc.assertEqual(inst.it_work(), 123)