import unittest
tc = unittest.TestCase()

class TestClass():
    def testObj(self, obj):
        f1, f2 = obj
        tc.assertEqual(f1(), 301)
        tc.assertEqual(f2(), 602)
        tc.assertEqual(f1(), 603)
        tc.assertEqual(f1(), 604)
        tc.assertEqual(f2(), 1208)

class TestClass2():
    def testObj(self, obj):
        f1, f2 = obj(300)
        tc.assertEqual(f1(), 301)
        tc.assertEqual(f2(), 602)
        tc.assertEqual(f1(), 603)
        tc.assertEqual(f2(), 1206)