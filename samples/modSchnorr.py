from typing import IO
from mcl import *

import random


def keyGen(Q: G2):
    a = Fr()
    a.setByCSPRNG()
    A = Q * a
    return a, A


class Prover:
    def __init__(self, a: Fr, A: G1, P: G1, Q: G2, r: int):
        self.a = a
        self.A = A
        self.P = P
        self.Q = Q
        self.r = r

        self.x = Fr()
        self.X = G2()
    
    def commit(self) -> G2:
        self.x = Fr(random.randint(1, self.r - 1))
        self.X = self.Q * self.x
        return self.X
    
    def respond(self, c: Fr) -> G1:
        text = self.X.getStr(io_mode=IoMode.HEX) + c.getStr(io_mode=IoMode.HEX)
        H = G1.hashAndMapTo(text)
        S = H * (self.x + self.a * c)
        self.x.clear()
        self.X.clear()
        return S


class Verifier:
    def __init__(self, A: G1, P: G1, Q: G2, r: int):
        self.A = A
        self.P = P
        self.Q = Q
        self.r = r

        self.X = G1()
        self.c = Fr()
    
    def challenge(self, X: G2) -> Fr:
        self.c = Fr(random.randint(1, self.r - 1))
        self.X = G2(X)
        return self.c
    
    def verify(self, S: G1) -> bool:
        text = self.X.getStr(io_mode=IoMode.HEX) + self.c.getStr(io_mode=IoMode.HEX)
        H = G1.hashAndMapTo(text)
        lhs = pairing(S, self.Q)
        rhs = pairing(H, self.X + self.A * self.c)
        self.X.clear()
        self.c.clear()
        return lhs == rhs


if __name__ == "__main__":
    # Initialize the library (otherwise you'll get a segmentation fault)
    mcl_init(CurveType.MCL_BLS12_381)

    # Create generatora
    P = G1.hashAndMapTo("abc")
    Q = G2.hashAndMapTo("abc")

    # Generate keys
    a, A = keyGen(Q)

    # Initialize participants
    prover = Prover(a, A, P, Q, 2 ** 64)
    verifier = Verifier(A, P, Q, 2 ** 64)

    # Simulate an execution
    X = prover.commit()
    c = verifier.challenge(X)
    S = prover.respond(c)
    R = verifier.verify(S)

    print("Verfied:", R)