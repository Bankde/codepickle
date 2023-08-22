import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        tc.assertEqual(obj(11), 415)

class TestClass2():
    def testObj(self, obj):
        tc.assertEqual(obj(16), 431)

class TestClass3():
    def testObj(self, obj):
        tc.assertEqual(obj(16), 431)