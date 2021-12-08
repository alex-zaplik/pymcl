from typing import IO
from mcl import *


def keyGen(Q: G2):
    a = Fr()
    a.setByCSPRNG()
    A = Q * a
    return a, A


class Prover:
    def __init__(self, a: Fr, A: G1, P: G1, Q: G2):
        self.a = a
        self.A = A
        self.P = P
        self.Q = Q

        self.x = Fr()
        self.X = G2()
    
    def commit(self) -> G2:
        self.x.setByCSPRNG()
        self.X = self.Q * self.x
        return self.X
    
    def respond(self, c: Fr) -> G1:
        H = G1.hashAndMapTo(self.X.serialize() + c.serialize())
        S = self.a * c
        S = self.x + S
        S = H * (self.x + self.a * c)
        self.x.clear()
        self.X.clear()
        return S


class Verifier:
    def __init__(self, A: G1, P: G1, Q: G2):
        self.A = A
        self.P = P
        self.Q = Q

        self.X = G1()
        self.c = Fr()
    
    def challenge(self, X: G2) -> Fr:
        self.c.setByCSPRNG()
        self.X = G2(X)
        return self.c
    
    def verify(self, S: G1) -> bool:
        H = G1.hashAndMapTo(self.X.serialize() + self.c.serialize())
        lhs = pairing(S, self.Q)
        rhs = pairing(H, self.X + self.A * self.c)
        self.X.clear()
        self.c.clear()
        return lhs == rhs


if __name__ == "__main__":
    # Initialize the library
    # mcl_init(CurveType.MCL_BN254)
    # mcl_init(CurveType.MCL_BN381_1)
    # mcl_init(CurveType.MCL_BN381_2)
    # mcl_init(CurveType.MCL_BN462)
    # mcl_init(CurveType.MCL_BN_SNARK1)
    mcl_init(CurveType.MCL_BLS12_381)
    # mcl_init(CurveType.MCL_BN160)

    # Create generatora
    P = G1.hashAndMapTo(b"abc")
    Q = G2.hashAndMapTo(b"abc")

    # Generate keys
    a, A = keyGen(Q)

    # Initialize participants
    prover = Prover(a, A, P, Q)
    verifier = Verifier(A, P, Q)

    # Simulate an execution
    X = prover.commit()
    c = verifier.challenge(X)
    S = prover.respond(c)
    R = verifier.verify(S)

    print("Verfied:", R)

    # Use an incrorrect private key
    a = a + Fr(10)
    print()

    # Initialize participants
    prover = Prover(a, A, P, Q)
    verifier = Verifier(A, P, Q)

    # Simulate an execution
    X = prover.commit()
    c = verifier.challenge(X)
    S = prover.respond(c)
    R = verifier.verify(S)

    print("Verfied:", R)