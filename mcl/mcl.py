from __future__ import annotations
from . import defines
from .defines import CurveType

import ctypes
import platform
import os


MCL_PATH = os.environ.get("MCL_PATH", "/usr/local/")
mcl_lib = None


def load_lib(path, *args):
    try:
        return ctypes.CDLL(path, *args)
    except OSError:
        print(
f"""Failed to import mcl library from {MCL_PATH}.
Please set mcl installation directory to MCL_PATH and run again.

export MCL_PATH=<path>
""")


def is_curve_6_6(ct: CurveType):
    if ct == CurveType.MCL_BN381_1 or ct == CurveType.MCL_BN381_2:
        return True
    
    if ct == CurveType.MCL_SECP384R1:
        return True

    return False


def mcl_init(curve_type: CurveType):
    global mcl_lib

    lib_file = ""

    if is_curve_6_6(curve_type):
        defines.MCLBN_FR_UNIT_SIZE = 6
        defines.MCLBN_FP_UNIT_SIZE = 6
        lib_file = "lib/libmclbn384.so"
    # elif curve_type == CurveType.MCL_BN462 or curve_type == CurveType.MCL_SECP521R1:
    #     defines.MCLBN_FR_UNIT_SIZE = 8
    #     defines.MCLBN_FP_UNIT_SIZE = 8
    #     lib_file = "lib/libmclbn512.so"
    else:    
        defines.MCLBN_FR_UNIT_SIZE = 4
        defines.MCLBN_FP_UNIT_SIZE = 6
        lib_file = "lib/libmclbn384_256.so"

    defines.G2_AVAILABLE = curve_type.value < 100

    defines.FR_SIZE = defines.MCLBN_FR_UNIT_SIZE
    defines.FP_SIZE = defines.MCLBN_FP_UNIT_SIZE
    defines.G1_SIZE = defines.MCLBN_FP_UNIT_SIZE * 3
    defines.G2_SIZE = defines.MCLBN_FP_UNIT_SIZE * 6
    defines.GT_SIZE = defines.MCLBN_FP_UNIT_SIZE * 12

    defines.MCLBN_COMPILED_TIME_VAR = (defines.MCLBN_FR_UNIT_SIZE * 10) + defines.MCLBN_FP_UNIT_SIZE

    name = platform.system()
    if name == 'Linux':
        load_lib(MCL_PATH + "lib/libmcl.so", ctypes.RTLD_GLOBAL)
        mcl_lib = load_lib(MCL_PATH + lib_file)
    else:
        raise RuntimeError(f'Not supported yet: {name}')

    ret = mcl_lib.mclBn_init(curve_type.value, defines.MCLBN_COMPILED_TIME_VAR)

    if ret:
        ret = -ret
        raise RuntimeError(f'Init error: {ret} -> {defines.MCLBN_COMPILED_TIME_VAR} {ret // 100} {ret % 100}')

# TODO: mclBn_setMapToMode
# TODO: mclBn_verifyOrderG1
# TODO: mclBn_verifyOrderG2
