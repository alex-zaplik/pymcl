from mcl import *


if __name__ == "__main__":
    # Initialize the library (otherwise you'll get a segmentation fault)
    mcl_init(CurveType.MCL_BLS12_381)

    # Create two generators
    P = G1.hashAndMapTo(b"abc")
    Q = G2.hashAndMapTo(b"abc")

    # Create two exponents
    a = Fr(123)
    b = Fr(456)

    # Compute some pairings
    check1 = pairing(P * a, Q * b) == pairing(P        , Q        ) ** (a * b)
    check2 = pairing(P * a, Q * b) == pairing(P * a    , Q        ) ** b
    check3 = pairing(P * a, Q * b) == pairing(P        , Q * b    ) ** a
    check4 = pairing(P * a, Q * b) == pairing(P        , Q * a * b)
    check5 = pairing(P * a, Q * b) == pairing(P * a * b, Q        )

    # Check that the pairings are equal
    print(f"e(aP, bQ) == e(  P,   Q)^(ab) -> {check1}")
    print(f"e(aP, bQ) == e( aP,   Q)^b    -> {check2}")
    print(f"e(aP, bQ) == e(  P,  bQ)^a    -> {check3}")
    print(f"e(aP, bQ) == e(  P, abQ)      -> {check4}")
    print(f"e(aP, bQ) == e(abP,   Q)      -> {check5}")
