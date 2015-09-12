from __future__ import print_function
import math

def slice_size(s):
    raw = (s.stop - s.start) / float(s.step or 1)
    return max(int(math.ceil(raw)),0)

class Sequence(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.updates = 0

    def __setitem__(self, i, y):
        if isinstance(i,slice):
            self.updates += slice_size(i)
        else:
            self.updates += 1
        list.__setitem__(self,i,y)

    #called in python 2 for 'simple' slices
    def __setslice__(self,i,j,y):
        self.updates += j - i
        list.__setslice__(self,i,j,y)

