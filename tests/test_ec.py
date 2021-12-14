import unittest
import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType, IoMode
from mcl.structures.g1 import G1, Fr


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


def runBadSchnorr():
    # Set up
    G = G1.hashAndMapTo(b"abc")
    a = Fr(); a.setByCSPRNG()
    A = G * a

    # Break the key
    a = a + Fr(10)

    # Commit
    x = Fr(); x.setByCSPRNG()
    X = G * x

    # Challenge
    c = Fr(); c.setByCSPRNG()

    # Response
    s = x + a * c

    # Verification
    return G * s == X + A * c


class G1Tests(unittest.TestCase):
    def testMCL_SECP192K1(self):
        mcl_init(CurveType.MCL_SECP192K1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())

    def testMCL_SECP224K1(self):
        mcl_init(CurveType.MCL_SECP224K1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    def testMCL_SECP256K1(self):
        mcl_init(CurveType.MCL_SECP256K1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
    
    def testMCL_SECP384R1(self):
        mcl_init(CurveType.MCL_SECP384R1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    # def testMCL_SECP521R1(self):
    #     mcl_init(CurveType.MCL_SECP521R1)
    #     self.assertTrue(runSchnorr())
    #     self.assertFalse(runBadSchnorr())
        
    def testMCL_NIST_P192(self):
        mcl_init(CurveType.MCL_NIST_P192)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    def testMCL_NIST_P224(self):
        mcl_init(CurveType.MCL_NIST_P224)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    def testMCL_NIST_P256(self):
        mcl_init(CurveType.MCL_NIST_P256)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    def testMCL_SECP160K1(self):
        mcl_init(CurveType.MCL_SECP160K1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        
    def testMCL_P160_1(self):
        mcl_init(CurveType.MCL_P160_1)
        self.assertTrue(runSchnorr())
        self.assertFalse(runBadSchnorr())
        

