   
from ordinal import Ordinal


def test():
    # See: https://imgur.com/Wf7CW7F for the example
    A = Ordinal()
    B = Ordinal()
    C = Ordinal()
    D = Ordinal(C)
    E = Ordinal(D)
    F = Ordinal(E)
    G = Ordinal(F)
    E.subordinates.append(G)
    H = Ordinal([B, G])
    I = Ordinal([A, H])
    J = Ordinal(I)
    K = Ordinal([J, E])
    I.subordinates.append(K)
    return {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K}
ordinals = test()

letter = "I"
print(ordinals[letter].get_rank())
