import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.structures.g2 import G2, Fr


class G2Tests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testClear(self):
        a = G2(10)
        a.clear()
        self.assertEqual(a, G2("0"))
    
    def testSerialize(self):
        a = G2.hashAndMapTo(b"abc")
        s = a.serialize()
        b = G2(s)
        self.assertEqual(a, b)
    
    def testStr(self):
        a = G2("1 0 10 0 0")
        self.assertEqual(a.getStr(), "1 0 10 0 0")
        self.assertEqual(a.getStr(io_mode=IoMode.HEX), "1 0 a 0 0")
    
    def testCopy(self):
        a = G2("1 0 10 0 0")
        b = G2(a)
        a.clear()
        self.assertEqual(b, G2("1 0 10 0 0"))

    # TODO: Test hashAndMapTo

    # Checks

    def testIsValid(self):
        self.assertFalse(G2("1 0 10 0 0").isValid())
    
    def testIsValidOrder(self):
        self.assertFalse(G2("1 0 15 0 0").isValidOrder())
    
    def testIsEqual(self):
        self.assertTrue(G2("1 0 10 0 0") == G2("1 0 10 0 0"))
        self.assertTrue(G2("1 0 10 0 0") != G2("1 0 15 0 0"))

    def testIsZero(self):
        self.assertTrue(G2("0").isZero())
        self.assertFalse(G2("1 0 10").isZero())

    # Arithmetic operators

    def testNeg(self):
        self.assertEqual(-G2("1 0 15 0 0").neg(), G2("1 0 15 0 0"))
    
    def testAddDbl(self):
        self.assertEqual(G2("1 0 15 0 0").dbl(), G2("1 0 15 0 0") + G2("1 0 15 0 0"))
    
    def testSubDbl(self):
        self.assertEqual(G2("1 0 15 0 0").dbl() - G2("1 0 15 0 0"), G2("1 0 15 0 0"))
    
    def testNormalize(self):
        self.assertEqual(G2("1 0 10 0 0").normalize(), G2("1 0 10 0 0"))

    def testMul(self):
        self.assertEqual(G2("1 0 15 0 0") * Fr(2), G2("1 0 15 0 0").dbl())

