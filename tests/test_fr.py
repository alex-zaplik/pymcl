import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.structures.fr import Fr

class FrTests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testClear(self):
        a = Fr(10)
        a.clear()
        self.assertEqual(a, Fr(0))
    
    def testSerialize(self):
        a = Fr(10)
        s = a.serialize()
        b = Fr(s)
        self.assertEqual(a, b)
    
    def testStr(self):
        a = Fr("10")
        self.assertEqual(a, Fr(10))
        self.assertEqual(a.getStr(), "10")
        self.assertEqual(a.getStr(io_mode=IoMode.HEX), "a")

    def testOther(self):
        a = Fr()
        a.setByCSPRNG()
        a.setHashOf("Hello")

    # Checks

    def testIsValid(self):
        self.assertTrue(Fr(10).isValid())
    
    def testIsEqual(self):
        self.assertTrue(Fr(10) == Fr(10))
        self.assertTrue(Fr(10) != Fr(15))

    def testIsZero(self):
        self.assertTrue(Fr(0).isZero())
        self.assertFalse(Fr(1).isZero())

    def testIsOne(self):
        self.assertTrue(Fr(1).isOne())
        self.assertFalse(Fr(0).isOne())
    
    def testIsOdd(self):
        self.assertTrue(Fr(1).isOdd())
        self.assertFalse(Fr(2).isOdd())

    def testIsNegative(self):
        self.assertTrue(Fr(-1).isNegative())
        self.assertFalse(Fr(1).isNegative())

    # Unary arithmetic operators

    def testNeg(self):
        self.assertEqual(-Fr(15).neg(), Fr(15))
        self.assertNotEqual(-Fr(15), Fr(15))
    
    def testInv(self):
        self.assertEqual(Fr(15).inv().inv(), Fr(15))
        self.assertNotEqual(Fr(15).inv(), Fr(15))
    
    def testSqr(self):
        self.assertEqual(Fr(10).sqr(), Fr(100))
    
    def testSquareRoot(self):
        self.assertEqual(Fr(100).squareRoot(), Fr(10))

    # Binary arithmetic operators

    def testAdd(self):
        self.assertEqual(Fr(15) + Fr(10), Fr(25))
    
    def testSub(self):
        self.assertEqual(Fr(15) - Fr(10), Fr(5))

    def testMul(self):
        self.assertEqual(Fr(15) * Fr(10), Fr(150))
    
    def testDiv(self):
        self.assertEqual(Fr(150) / Fr(10), Fr(15))

