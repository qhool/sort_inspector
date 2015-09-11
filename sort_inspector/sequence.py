class Sequence(list):
    def __init__(self, *args):
        list.__init__(self, *args)
        self.updates = 0

    def __setitem__(self, i, y):
        self.updates += 1
        list.__setitem__(self,i,y)

    def __setslice__(self,i,j,y):
        self.updates += j - i
        list.__setslice__(self,i,j,y)


