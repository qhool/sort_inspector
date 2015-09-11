import unittest

from sort_inspector import Comparable

class ComparableTest(unittest.TestCase):

    def test_init(self):
        a = Comparable(1)
        b = Comparable(2)
        c = Comparable("foo")

    def test_comparisons(self):
        a = Comparable(1)
        b = Comparable(2)

        self.assertTrue(a < b)

        self.assertEqual(a.comparisons,1)
        self.assertEqual(b.comparisons,0)

        self.assertFalse(a == b)
        self.assertTrue(a != b)
        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)

        self.assertEqual(a.comparisons,7)
        self.assertEqual(b.comparisons,0)

        self.assertFalse(b < a)

        self.assertEqual(a.comparisons,7)
        self.assertEqual(b.comparisons,1)

    def test_reset(self):
        a = Comparable("foo")
        b = Comparable("bar")

        a > b

        self.assertEqual(a.comparisons,1)
        a.reset()
        self.assertEqual(a.comparisons,0)
