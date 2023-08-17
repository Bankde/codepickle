import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        o = obj("First", "Last")
        tc.assertEqual(o.getName(), "First Last")
        tc.assertEqual(o.getHeight(), 160)

class TestClass2():
    def testObj(self, obj):
        o = obj
        tc.assertEqual(o.getName(), "First Last")
        tc.assertEqual(o.getHeight(), 160)