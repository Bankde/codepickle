import unittest
tc = unittest.TestCase()

'''
Fail of using non local
'''

class TestClass():
    def testObj(self, obj):
        f1, f2 = obj
        tc.assertEqual(f1(), 4)
        tc.assertEqual(f1(), 7)
        tc.assertEqual(f2(), 8)
        tc.assertEqual(f2(), 11)
        tc.assertEqual(f1(), 10)
