import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../mcl"))

from mcl import mcl_init, CurveType


class CurvesTests(unittest.TestCase):
    def testBn254(self):
        mcl_init(CurveType.MCL_BN254)
    
    # def testBn381_1(self):
    #     mcl_init(CurveType.MCL_BN381_1)
    
    # def testBn381_2(self):
    #     mcl_init(CurveType.MCL_BN381_2)
    
    # def testBn462(self):
    #     mcl_init(CurveType.MCL_BN462)
    
    def testBnSNARK1(self):
        mcl_init(CurveType.MCL_BN_SNARK1)
    
    def testBnBLS12_381(self):
        mcl_init(CurveType.MCL_BLS12_381)
    
    def testBn160(self):
        mcl_init(CurveType.MCL_BN160)
