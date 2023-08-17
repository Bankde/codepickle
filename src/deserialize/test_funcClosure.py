import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        f = obj(4)
        tc.assertEqual(f(11), 15)

class TestClass2():
    def testObj(self, obj):
        tc.assertEqual(obj(11), 15)