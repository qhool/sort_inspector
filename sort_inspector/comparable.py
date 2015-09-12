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

    def __lt__(self,other):
        self.comparisons += 1
        return self.val < other.val

    def __le__(self,other):
        self.comparisons += 1
        return self.val <= other.val

    def __repr__(self):
        return str(self.val);

    def reset(self):
        self.comparisons = 0
