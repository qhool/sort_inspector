import unittest
from functools import reduce

from sort_inspector import Comparable

class ComparableTest(unittest.TestCase):

    def test_init(self):
        a = Comparable(1)
        b = Comparable(2)
        c = Comparable("foo")

    def assertComparisons(self,items,n):
        total = reduce( lambda count,x: count + x.comparisons, items, 0 )
        self.assertEqual(total,n)

    def test_comparisons(self):
        a = Comparable(1)
        b = Comparable(2)
        ab = [a,b]

        self.assertTrue(a < b)

        self.assertComparisons(ab,1)

        self.assertFalse(a == b)
        self.assertComparisons(ab,2)

        self.assertTrue(a != b)
        self.assertFalse(a > b)
        self.assertFalse(a >= b)
        self.assertTrue(a < b)
        self.assertTrue(a <= b)

        self.assertComparisons(ab,7)

        self.assertFalse(b < a)
        self.assertComparisons(ab,8)

    def test_reset(self):
        a = Comparable("foo")
        b = Comparable("bar")

        a > b
        b > a

        self.assertEqual(a.comparisons,1)
        self.assertEqual(b.comparisons,1)
        a.reset()
        self.assertEqual(a.comparisons,0)


if __name__ == '__main__':
    unittest.main()
