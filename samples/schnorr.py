from mcl import *


def keyGen(G: G1):
    a = Fr()
    a.setByCSPRNG()
    A = G * a
    return a, A


class Prover:
    def __init__(self, a: Fr, A: G1, G: G1):
        self.a = a
        self.A = A
        self.G = G

        self.x = Fr()
    
    def commit(self) -> G1:
        self.x.setByCSPRNG()
        X = self.G * self.x
        return X
    
    def respond(self, c: Fr) -> Fr:
        s = self.x + self.a * c
        self.x.clear()
        return s


class Verifier:
    def __init__(self, A: G1, G: G1):
        self.A = A
        self.G = G

        self.X = G1()
        self.c = Fr()
    
    def challenge(self, X: G1) -> Fr:
        self.c.setByCSPRNG()
        self.X = X
        return self.c
    
    def verify(self, s: Fr) -> bool:
        lhs = self.G * s
        rhs = self.X + self.A * self.c
        self.X.clear()
        self.c.clear()
        return lhs == rhs


if __name__ == "__main__":
    # Initialize the library (otherwise you'll get a segmentation fault)
    mcl_init(CurveType.MCL_BLS12_381)

    # Create a generator
    G = G1.hashAndMapTo("abc")

    # Generate keys
    a, A = keyGen(G)

    # Initialize participants
    prover = Prover(a, A, G)
    verifier = Verifier(A, G)

    # Simulate an execution
    X = prover.commit()
    c = verifier.challenge(X)
    s = prover.respond(c)
    R = verifier.verify(s)

    print("Verfied:", R)
