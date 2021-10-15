from __future__ import annotations
from .lib import mcl
from .defines import MCLBN_COMPILED_TIME_VAR, CurveType


def mcl_init(curve_type: CurveType):
    ret = mcl.mclBn_init(curve_type.value, MCLBN_COMPILED_TIME_VAR)
    if ret:
        raise RuntimeError(f'Init error: {ret}')

# TODO: mclBn_setMapToMode
# TODO: mclBn_verifyOrderG1
# TODO: mclBn_verifyOrderG2
