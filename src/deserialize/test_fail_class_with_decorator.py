import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        tc.assertEqual(obj.test_sm(), "sm works")
        tc.assertEqual(obj.test_cm(), "cm works")