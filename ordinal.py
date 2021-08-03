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
        self.subordinates: List[Ordinal] = None
        if type(subordinates) is Ordinal:
            self.subordinates: List[Ordinal] = [subordinates]
        else:
            self.subordinates: List[Ordinal] = subordinates            
        if calc_rank_on_init:
            self.rank: int = self.get_rank()
        else:
            self.rank: int = None

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
                equals += [subordinate]
                continue
            # if not, get some return from the subordinate when asking rank
            rank = subordinate.get_rank(superiors_asking=superiors_asking + [self])
            # assess the return we got from asking rank
            if type(rank) is int:
                if rank >= result:
                    result = rank + 1
            else:
                if rank[0] >= result:
                    result = rank[0]
                equals += rank[1]
                # this subordinate continues the chain of confusion if it answers to superiors
                if len(superiors_asking) > 0:
                    confused = True                
        # decide what to return based on confusion
        if confused and self not in equals:
            return [result, equals]
        return result

# # Uncomment to test it out

# def test():
#     # See: https://imgur.com/Wf7CW7F for the example
#     A = Ordinal()
#     B = Ordinal()
#     C = Ordinal()
#     D = Ordinal(C)
#     E = Ordinal(D)
#     F = Ordinal(E)
#     G = Ordinal(F)
#     E.subordinates.append(G)
#     H = Ordinal([B, G])
#     I = Ordinal([A, H])
#     J = Ordinal(I)
#     K = Ordinal([J, E])
#     I.subordinates.append(K)
#     return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K}
# ordinals = test()

# letter = "I"
# print(ordinals[letter].get_rank())
