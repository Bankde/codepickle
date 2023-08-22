import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        tc.assertEqual(obj(4), 30)