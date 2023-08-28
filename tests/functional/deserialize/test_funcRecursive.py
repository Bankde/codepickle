import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        tc.assertEqual(obj(5), 15)

class TestClass2():
    def testObj(self, obj):
        tc.assertEqual(obj(6), 150)