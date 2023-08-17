import unittest
tc = unittest.TestCase()

# This works because we wrap both text() and decorator() into the sourcecode
# There will be no pickled on runtime text() or UpperDecorator()

class TestClass():
    def testObj(self, obj):
        func = obj()
        tc.assertEqual(func(), "HELLO WORLD 1")

class TestClass2():
    def testObj(self, obj):
        func = obj()
        tc.assertEqual(func(), "HELLO WORLD 1")