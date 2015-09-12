import unittest

from sort_inspector import Sequence
from sort_inspector.sequence import slice_size

import random

# bubble sort, manually instrumented
# used to test swap/comparison counting
def bubble(t):
    swaps = 0
    compares = 0
    done = False
    while not done:
        done = True
        for i in range(1,len(t)):
            compares += 1
            if t[i] < t[i-1]:
                done = False
                swaps += 1
                t[i-1],t[i] = t[i],t[i-1]
    return (swaps,compares)

class SequenceTest(unittest.TestCase):

    def test_init(self):
        t = Sequence([1,2,3])
        u = Sequence([])

    def test_counts(self):
        t = Sequence(range(10))
        for i in range(1,10):
            t[i-1], t[i] = t[i], t[i-1]
        self.assertEqual(t.updates,18)

    def test_slice(self):
        t = Sequence(range(20))
        t[0:10] = range(10,0,-1)
        self.assertEqual(t.updates,10)

    def test_slice_size(self):
        t = range(50)
        for i in range(50):
            for j in range(50):
                for st in range(1,6):
                    for sgn in [-1,1]:
                        s = slice(i,j,sgn*st)
                        sz = slice_size(s)
                        self.assertEqual(len(t[s]),sz)

    def test_counts(self):
        for n in range(1,20):
            for i in range(5):
                t = Sequence([ random.randrange(20) for x in range(n) ])
                (swaps,comps) = bubble(t)
                self.assertEqual(t.count_comparisons(),comps)
                self.assertEqual(t.count_swaps(),swaps)

if __name__ == '__main__':
    unittest.main()
