"""
Author: ZR000X
Dated: 2021-08-02
License: MIT
Source: https://github.com/ZR000X/Nodes
"""


from typing import List


class Ordinal():
    """
    An ordinal is simply a set of all things it is greater than.
    """
    def __init__(self, subordinates=None, calc_rank_on_init=False) -> None:
        self.subordinates: List[Ordinal] = subordinates
        if calc_rank_on_init:
            self.rank = self.get_rank()
        else:
            self.rank = None

    def __in__(self, other):
        return other in self.subordinates

    def __ge__(self, other):
        return other in self.subordinates

    def __le__(self, other):
        return self in other.subordinates

    def equals(self, other):
        return self >= other and other >= self

    def __iter__(self):
        return iter(self.subordinates)

    def __len__(self):
        return len(self.subordinates)
    
    def __str__(self):
        if self.rank_captured:
            return str(self.rank)
        else:
            return str(self.get_rank()) 

    def get_rank(self, superiors_asking=[]) -> int:
        """
        returns the index attached to this ordinal
        """
        # deal with empty lists
        if self.subordinates is None or len(self) == 0:
            return 0 
        # Loop through subordinates
        confused = False
        equals = []
        result = 0
        for subordinate in self:
            # check that subordinate is not contradictory
            # Note: the original asker can never be confused
            if subordinate in superiors_asking:
                confused = True
                equals.append(subordinate)
                continue
            # if not, get some return from the subordinate when asking rank
            if subordinate.rank_captured:
                rank = subordinate.rank
            else:
                rank = subordinate.get_rank(superiors_asking=superiors_asking + [self])
            # assess the return we got from asking rank
            if type(rank) is int:
                if rank >= result:
                    result = rank + 1
            else:
                if rank[0] >= result:
                    result = rank[0]
                equals += rank[1] + [subordinate]
                # this subordinate continues the chain of confusion if it answers to superiors
                if len(superiors_asking) > 0:
                    confused = True                
        # decide what to return based on confusion
        if confused:
            return [result, equals]
        return result
