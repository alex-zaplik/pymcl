import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.structures.g1 import G1, Fr


class G1Tests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testClear(self):
        a = G1(10)
        a.clear()
        self.assertEqual(a, G1("0"))
    
    def testSerialize(self):
        a = G1(10)
        s = a.serialize()
        b = G1(s)
        self.assertEqual(a, b)
    
    def testStr(self):
        a = G1("1 0 10")
        self.assertEqual(a.getStr(), "1 0 10")
        self.assertEqual(a.getStr(io_mode=IoMode.HEX), "1 0 a")

    # TODO: Test hashAndMapTo

    # Checks

    def testIsValid(self):
        self.assertFalse(G1("1 0 10").isValid())
    
    def testIsValidOrder(self):
        self.assertFalse(G1("1 0 15").isValidOrder())
    
    def testIsEqual(self):
        self.assertTrue(G1("1 0 10") == G1("1 0 10"))
        self.assertTrue(G1("1 0 10") != G1("1 0 15"))

    def testIsZero(self):
        self.assertTrue(G1("0").isZero())
        self.assertFalse(G1("1 0 10").isZero())

    # Arithmetic operators

    def testNeg(self):
        self.assertEqual(-G1("1 0 15").neg(), G1("1 0 15"))
        self.assertNotEqual(-G1("1 0 15"), G1("1 0 15"))
    
    def testAddDbl(self):
        self.assertEqual(G1("1 0 15").dbl(), G1("1 0 15") + G1("1 0 15"))
    
    def testDubDbl(self):
        self.assertEqual(G1("1 0 15").dbl() - G1("1 0 15"), G1("1 0 15"))
    
    def testNormalize(self):
        self.assertEqual(G1("1 0 10").normalize(), G1("1 0 10"))

    def testMul(self):
        self.assertEqual(G1("1 0 15") * Fr(2), G1("1 0 15").dbl())

