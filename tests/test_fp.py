import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl
from mcl.mcl import mcl_init, CurveType
from mcl.defines import CurveType, IoMode
from mcl.structures.fp import Fp, G1


class FpTests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testClear(self):
        a = Fp(10)
        a.clear()
        self.assertEqual(a, Fp(0))
    
    def testSerialize(self):
        a = Fp(10)
        s = a.serialize()
        b = Fp(s)
        self.assertEqual(a, b)
    
    def testStr(self):
        a = Fp("10")
        self.assertEqual(a, Fp(10))
        self.assertEqual(a.getStr(), "10")
        self.assertEqual(a.getStr(io_mode=IoMode.HEX), "a")

    def testOther(self):
        a = Fp()
        a.setByCSPRNG()
        a.setHashOf(b"Hello")

    def testMapToG1(self):
        a = Fp(10)
        b = a.mapToG1()
        self.assertTrue(isinstance(b, G1))
    
    def testCopy(self):
        a = Fp("10")
        b = Fp(a)
        a.clear()
        self.assertEqual(b, Fp("10"))

    # Checks

    def testIsValid(self):
        self.assertTrue(Fp(10).isValid())
    
    def testIsEqual(self):
        self.assertTrue(Fp(10) == Fp(10))
        self.assertTrue(Fp(10) != Fp(15))

    def testIsZero(self):
        self.assertTrue(Fp(0).isZero())
        self.assertFalse(Fp(1).isZero())

    def testIsOne(self):
        self.assertTrue(Fp(1).isOne())
        self.assertFalse(Fp(0).isOne())
    
    def testIsOdd(self):
        self.assertTrue(Fp(1).isOdd())
        self.assertFalse(Fp(2).isOdd())

    def testIsNegative(self):
        self.assertTrue(Fp(-1).isNegative())
        self.assertFalse(Fp(1).isNegative())

    # Unary arithmetic operators

    def testNeg(self):
        self.assertEqual(-Fp(15).neg(), Fp(15))
        self.assertNotEqual(-Fp(15), Fp(15))
    
    def testInv(self):
        self.assertEqual(Fp(15).inv().inv(), Fp(15))
        self.assertNotEqual(Fp(15).inv(), Fp(15))
    
    def testSqr(self):
        self.assertEqual(Fp(10).sqr(), Fp(100))
    
    def testSquareRoot(self):
        self.assertEqual(Fp(100).squareRoot(), Fp(10))

    # Binary arithmetic operators

    def testAdd(self):
        self.assertEqual(Fp(15) + Fp(10), Fp(25))
    
    def testSub(self):
        self.assertEqual(Fp(15) - Fp(10), Fp(5))

    def testMul(self):
        self.assertEqual(Fp(15) * Fp(10), Fp(150))
    
    def testDiv(self):
        self.assertEqual(Fp(150) / Fp(10), Fp(15))

