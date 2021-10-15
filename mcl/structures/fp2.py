from __future__ import annotations

from ..lib import mcl
from ..defines import FP_SIZE, IoMode
from .g2 import G2

import ctypes


class Fp2(ctypes.Structure):
    """
    A finite field of prime order `p`, that curves are defined over
    """

    _fields_ = [("value", ctypes.c_ulonglong * FP_SIZE * 2)]

    def __init__(self, value = None):
        if isinstance(value, bytes):
            self.deserialize(value)
    
    def clear(self) -> None:
        """
        Sets the value to 0
        """
        mcl.mclBnFp2_clear(ctypes.byref(self.value))

    def serialize(self) -> bytes:
        """
        Serializes the value to bytes
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        size = mcl.mclBnFp2_serialize(buffer, len(buffer), ctypes.byref(self.value))
        return buffer[:size]
    
    def deserialize(self, buffer: bytes) -> None:
        """
        Deserializes bytes and sets the value
        """
        c_buffer = ctypes.create_string_buffer(buffer)
        mcl.mclBnFp2_deserialize(ctypes.byref(self.value), c_buffer, len(buffer))
    
    def mapToG2(self) -> G2:
        res = G2()
        mcl.mclBnFp2_mapToG2(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    # Checks

    def isEqual(self, rhs: Fp2) -> bool:
        return mcl.mclBnFp2_isEqual(ctypes.byref(self.value), ctypes.byref(rhs.value)) != 0

    def __eq__(self, rhs: Fp2) -> bool:
        return self.isEqual(rhs)
    
    def __ne__(self, rhs: Fp2) -> bool:
        return not self.isEqual(rhs)

    def isZero(self) -> bool:
        return mcl.mclBnFp2_isZero(ctypes.byref(self.value)) != 0

    def isOne(self) -> bool:
        return mcl.mclBnFp2_isOne(ctypes.byref(self.value)) != 0

    # Unary arithmetic operators

    def neg(self) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def __neg__(self) -> Fp2:
        return self.neg()
    
    def inv(self) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def sqr(self) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_sqr(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def squareRoot(self) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_squareRoot(ctypes.byref(res.value), ctypes.byref(self.value))
        return res

    # Binary arithmetic operators

    def add(self, rhs: Fp2) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_add(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __add__(self, rhs: Fp2) -> Fp2:
        return self.add(rhs)

    def sub(self, rhs: Fp2) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_sub(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __sub__(self, rhs: Fp2) -> Fp2:
        return self.sub(rhs)

    def mul(self, rhs: Fp2) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_mul(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __mul__(self, rhs: Fp2) -> Fp2:
        return self.mul(rhs)

    def div(self, rhs: Fp2) -> Fp2:
        res = Fp2()
        mcl.mclBnFp2_div(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __truediv__(self, rhs: Fp2) -> Fp2:
        return self.div(rhs)
