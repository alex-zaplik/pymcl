import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.pairing import pairing, millerLoop, G1, G2
from mcl.structures.fr import Fr


class PairingTests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testPairing(self):
        P = G1.hashAndMapTo(b"abc")
        Q = G2.hashAndMapTo(b"abc")

        a = Fr(123)
        b = Fr(456)

        self.assertEqual(pairing(P * a, Q * b), pairing(P, Q) ** (a * b))

        self.assertEqual(pairing(P * a, Q * b), pairing(P * a, Q) ** b)
        self.assertEqual(pairing(P * a, Q * b), pairing(P, Q * b) ** a)

        self.assertEqual(pairing(P * a, Q * b), pairing(P, Q * a * b))
        self.assertEqual(pairing(P * a, Q * b), pairing(P * a * b, Q))
