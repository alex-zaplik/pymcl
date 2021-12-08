from mcl import *


if __name__ == "__main__":
    # Initialize the library
    # mcl_init(CurveType.MCL_BN254)
    # mcl_init(CurveType.MCL_BN381_1)
    # mcl_init(CurveType.MCL_BN381_2)
    # mcl_init(CurveType.MCL_BN462)
    # mcl_init(CurveType.MCL_BN_SNARK1)
    mcl_init(CurveType.MCL_BLS12_381)
    # mcl_init(CurveType.MCL_BN160)

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

    # Print some of the values
    print(pairing(P * a, Q * b), "\n")

    # Check that the pairings are equal
    print(f"e(aP, bQ) == e(  P,   Q)^(ab) -> {check1}")
    print(f"e(aP, bQ) == e( aP,   Q)^b    -> {check2}")
    print(f"e(aP, bQ) == e(  P,  bQ)^a    -> {check3}")
    print(f"e(aP, bQ) == e(  P, abQ)      -> {check4}")
    print(f"e(aP, bQ) == e(abP,   Q)      -> {check5}")
