from __future__ import annotations

from .lib import mcl
from .structures.g1 import G1
from .structures.g2 import G2
from .structures.gt import GT

import ctypes


def pairing(x: G1, y: G2) -> GT:
    res = GT()
    mcl.mclBn_pairing(ctypes.byref(res.value), ctypes.byref(x.value), ctypes.byref(y.value))
    return res


def millerLoop(x: G1, y: G2) -> GT:
    res = GT()
    mcl.mclBn_millerLoop(ctypes.byref(res.value), ctypes.byref(x.value), ctypes.byref(y.value))
    return res


def finalExp(x: GT) -> GT:
    res = GT()
    mcl.mclBn_finalExp(ctypes.byref(res.value), ctypes.byref(x.value))
    return res
