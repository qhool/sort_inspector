class Comparable:
    def __init__(self,val):
        self.comparisons = 0
        self.val = val

    def __eq__(self,other):
        self.comparisons += 1
        return self.val == other.val

    def __ne__(self,other):
        self.comparisons += 1
        return self.val != other.val

    def __cmp__(self,other):
        self.comparisons += 1
        if self.val < other.val:
            return -1
        if self.val > other.val:
            return 1
        else:
            return 0

    def __repr__(self):
        return str(self.val);

    def reset(self):
        self.comparisons = 0
