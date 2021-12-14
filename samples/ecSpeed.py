from mcl import *

import time


curves = [
    CurveType.MCL_BN254,
    CurveType.MCL_BN381_1,
    CurveType.MCL_BN381_2,
    CurveType.MCL_BN_SNARK1,
    CurveType.MCL_BLS12_381,
    CurveType.MCL_BN160,

    CurveType.MCL_SECP192K1,
    CurveType.MCL_SECP224K1,
    CurveType.MCL_SECP256K1,
    CurveType.MCL_SECP384R1,
    CurveType.MCL_NIST_P192,
    CurveType.MCL_NIST_P224,
    CurveType.MCL_NIST_P256,
    CurveType.MCL_SECP160K1,
    CurveType.MCL_P160_1
]

names = [
    "MCL_BN254",
    "MCL_BN381_1",
    "MCL_BN381_2",
    "MCL_BN_SNARK1",
    "MCL_BLS12_381",
    "MCL_BN160",

    "MCL_SECP192K1",
    "MCL_SECP224K1",
    "MCL_SECP256K1",
    "MCL_SECP384R1",
    "MCL_NIST_P192",
    "MCL_NIST_P224",
    "MCL_NIST_P256",
    "MCL_SECP160K1",
    "MCL_P160_1"
]


def runSchnorr():
    # Set up
    G = G1.hashAndMapTo(b"abc")
    a = Fr(); a.setByCSPRNG()
    A = G * a

    # Commit
    x = Fr(); x.setByCSPRNG()
    X = G * x

    # Challenge
    c = Fr(); c.setByCSPRNG()

    # Response
    s = x + a * c

    # Verification
    return G * s == X + A * c


def test_curve(iters=2500):
    s = time.time()
    for _ in range(iters):
        runSchnorr()
    e = time.time()

    return e - s


if __name__ == "__main__":
    for i in range(len(curves)):
        print(f"Curve:\t{names[i]}")

        mcl_init(curves[i])
        t = test_curve()

        print(f"Time:\t{t}s")
        print()
