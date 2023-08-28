import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        tc.assertEqual(obj(17,18), 35)

class TestClass2():
    def testObj(self, obj):
        tc.assertEqual(obj(17), 22)