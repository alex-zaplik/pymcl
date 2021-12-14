from mcl import *


def hashG1(text: str) -> G1:
    # Hash into G1
    return G1.hashAndMapTo(text.encode())


def hashG2(text: str) -> G1:
    # Hash into G2
    return G2.hashAndMapTo(text.encode())


def keyGen(P: G1, Q: G2):
    # Generate the private key and G1/G2 public keys
    x = Fr()
    x.setByCSPRNG()
    return x, P * x, Q * x


# This class simulates the signing party
class Signer:
    def __init__(self, P: G1, Q: G2, x: Fr):
        self.P = P
        self.Q = Q
        self.x = x
    
    def signG1(self, text: str) -> G1:
        # Creates a G1 signature
        H = hashG1(text)
        return H * self.x


    def signG2(self, text: str) -> G2:
        # Creates a G2 signature
        H = hashG2(text)
        return H * self.x


# This class simulates the verifying party
class Verifier:
    def __init__(self, P: G1, Q: G2, X1: G1, X2: G2):
        self.P = P
        self.Q = Q
        self.X1 = X1
        self.X2 = X2

    def verify(self, text: str, s):
        # Check the signature type and verify
        if isinstance(s, G1):
            e1 = pairing(s, self.Q)              # e(H * x, Q)
            e2 = pairing(hashG1(text), self.X2)  # e(H, Q * x)
            return e1 == e2
        elif isinstance(s, G2):
            e1 = pairing(self.P, s)              # e(P, H * x)
            e2 = pairing(self.X1, hashG2(text))  # e(P * X, H)
            return e1 == e2
        else:
            return False


if __name__ == "__main__":
    # Initialize the library
    # mcl_init(CurveType.MCL_BN254)
    # mcl_init(CurveType.MCL_BN381_1)
    # mcl_init(CurveType.MCL_BN381_2)
    # mcl_init(CurveType.MCL_BN_SNARK1)
    mcl_init(CurveType.MCL_BLS12_381)
    # mcl_init(CurveType.MCL_BN160)

    # Prepare generators
    P = G1.hashAndMapTo(b"abc")
    Q = G2.hashAndMapTo(b"abc")

    # Init scheme
    x, X1, X2 = keyGen(P, Q)

    # Create Signer and Verifier instances
    signer = Signer(P, Q, x)
    verifier = Verifier(P, Q, X1, X2)

    # Sign some text with G1/G2 signatures
    text = "Hello world!"
    s1 = signer.signG1(text)
    s2 = signer.signG2(text)

    # Verify the signatures
    print("Verified S1:", verifier.verify(text, s1))
    print("Verified S2:", verifier.verify(text, s2))
    
    # Use an incorrect private key
    x = x + Fr(10)
    print()

    # Create Signer and Verifier instances
    signer = Signer(P, Q, x)
    verifier = Verifier(P, Q, X1, X2)

    # Sign some text with G1/G2 signatures
    text = "Hello world!"
    s1 = signer.signG1(text)
    s2 = signer.signG2(text)

    # Verify the signatures
    print("Verified S1:", verifier.verify(text, s1))
    print("Verified S2:", verifier.verify(text, s2))
