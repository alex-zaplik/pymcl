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


# Library defines
class CurveType(Enum):
    MCL_BN254 = 0
    MCL_BN381_1 = 1
    MCL_BN381_2 = 2
    MCL_BN462 = 3
    MCL_BN_SNARK1 = 4
    MCL_BLS12_381 = 5
    MCL_BN160 = 6

class IoMode(Enum):
    DEC = 10
    HEX = 16
