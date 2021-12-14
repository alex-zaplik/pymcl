from enum import Enum

# Compiler specific defines
# For now there values are fixed for BLS 12_381
MCLBN_FR_UNIT_SIZE = 4
MCLBN_FP_UNIT_SIZE = 6

FR_SIZE = MCLBN_FR_UNIT_SIZE
FP_SIZE = MCLBN_FP_UNIT_SIZE
G1_SIZE = MCLBN_FP_UNIT_SIZE * 3
G2_SIZE = MCLBN_FP_UNIT_SIZE * 6
GT_SIZE = MCLBN_FP_UNIT_SIZE * 12

MCLBN_COMPILED_TIME_VAR = (MCLBN_FR_UNIT_SIZE * 10) + MCLBN_FP_UNIT_SIZE

G2_AVAILABLE = True


# Library defines
class CurveType(Enum):
    MCL_BN254       = 0
    MCL_BN381_1     = 1
    MCL_BN381_2     = 2
    # MCL_BN462       = 3
    MCL_BN_SNARK1   = 4
    MCL_BLS12_381   = 5
    MCL_BN160       = 6

    MCL_SECP192K1   = 100
    MCL_SECP224K1   = 101
    MCL_SECP256K1   = 102
    MCL_SECP384R1   = 103
    # MCL_SECP521R1   = 104
    MCL_NIST_P192   = 105
    MCL_NIST_P224   = 106
    MCL_NIST_P256   = 107
    MCL_SECP160K1   = 108
    MCL_P160_1      = 109

class IoMode(Enum):
    DEC = 10
    HEX = 16
