import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.structures.gt import GT, Fr


class GTTests(unittest.TestCase):
    def setUp(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testClear(self):
        a = GT(10)
        a.clear()
        self.assertEqual(a, GT(0))
    
    def testSerialize(self):
        a = GT(10)
        s = a.serialize()
        b = GT(s)
        self.assertEqual(a, b)
    
    def testStr(self):
        a = GT("10")
        self.assertEqual(a, GT(10))
        self.assertEqual(a.getStr(), "10 0 0 0 0 0 0 0 0 0 0 0")
        self.assertEqual(a.getStr(io_mode=IoMode.HEX), "a 0 0 0 0 0 0 0 0 0 0 0")
    
    def testCopy(self):
        a = GT("10")
        b = GT(a)
        a.clear()
        self.assertEqual(b, GT("10"))

    # Checks
    
    def testIsEqual(self):
        self.assertTrue(GT(10) == GT(10))
        self.assertTrue(GT(10) != GT(15))

    def testIsZero(self):
        self.assertTrue(GT(0).isZero())
        self.assertFalse(GT(1).isZero())

    def testIsOne(self):
        self.assertTrue(GT(1).isOne())
        self.assertFalse(GT(0).isOne())

    # Unary arithmetic operators

    def testNeg(self):
        self.assertEqual(-GT(15).neg(), GT(15))
        self.assertNotEqual(-GT(15), GT(15))
    
    def testInv(self):
        self.assertEqual(GT(15).inv().inv(), GT(15))
        self.assertNotEqual(GT(15).inv(), GT(15))
    
    def testSqr(self):
        self.assertEqual(GT(10).sqr(), GT(100))

    # Binary arithmetic operators

    def testAdd(self):
        self.assertEqual(GT(15) + GT(10), GT(25))
    
    def testSub(self):
        self.assertEqual(GT(15) - GT(10), GT(5))

    def testMul(self):
        self.assertEqual(GT(15) * GT(10), GT(150))
    
    def testDiv(self):
        self.assertEqual(GT(150) / GT(10), GT(15))
    
    def testPow(self):
        self.assertEqual(GT(10) ** Fr(2), GT(100))

