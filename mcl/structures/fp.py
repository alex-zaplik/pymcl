from __future__ import annotations

from .. import mcl

from .. import defines
from ..defines import IoMode
from .g1 import G1

import ctypes


class Fp(ctypes.Structure):
    """
    A finite field of prime order `p`, that curves are defined over
    """

    def __init__(self, value = None):
        if mcl.mcl_lib is None:
            raise RuntimeError("MCL was not initialised, please run mcl_init first")

        self.value = (ctypes.c_ulonglong * defines.FP_SIZE)(*([0] * defines.FP_SIZE))

        if isinstance(value, Fp):
            self.value = (ctypes.c_ulonglong * defines.FP_SIZE)(*value.value)
        elif isinstance(value, int):
            self.setInt(value)
        elif isinstance(value, str):
            self.setStr(value)
        elif isinstance(value, bytes):
            self.deserialize(value)
    
    def clear(self) -> None:
        """
        Sets the value to 0
        """
        mcl.mcl_lib.mclBnFp_clear(ctypes.byref(self.value))
    
    def setInt(self, x: int) -> None:
        """
        Sets the value to x
        """
        mcl.mcl_lib.mclBnFp_setInt(ctypes.byref(self.value), x)
    
    # TODO: Set/Get little endian buff

    def serialize(self) -> bytes:
        """
        Serializes the value to bytes
        """
        buffer_len = 2048
        buffer = ctypes.create_string_buffer(buffer_len)
        size = mcl.mcl_lib.mclBnFp_serialize(buffer, len(buffer), ctypes.byref(self.value))
        return buffer[:size]
    
    def deserialize(self, buffer: bytes) -> None:
        """
        Deserializes bytes and sets the value
        """
        c_buffer = ctypes.create_string_buffer(buffer)
        mcl.mcl_lib.mclBnFp_deserialize(ctypes.byref(self.value), c_buffer, len(c_buffer))

    def setStr(self, string: str, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Sets the value to the number in the string
        """
        mcl.mcl_lib.mclBnFp_setStr(ctypes.byref(self.value), ctypes.c_char_p(string.encode()), len(string), io_mode.value)

    def getStr(self, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Returns a string with the value
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        mcl.mcl_lib.mclBnFp_getStr(buffer, len(buffer), ctypes.byref(self.value), io_mode.value)
        return buffer.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    __repr__ = __str__

    def setByCSPRNG(self) -> None:
        """
        Sets a random value
        """
        mcl.mcl_lib.mclBnFp_setByCSPRNG(ctypes.byref(self.value))
    
    def setHashOf(self, data) -> None:
        """
        Set the hash of the data as the value
        """
        mcl.mcl_lib.mclBnFp_setHashOf(ctypes.byref(self.value), ctypes.c_char_p(data), ctypes.c_size_t(len(data)))
    
    def mapToG1(self) -> G1:
        res = G1()
        mcl.mcl_lib.mclBnFp_mapToG1(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    # Checks

    def isValid(self) -> bool:
        return mcl.mcl_lib.mclBnFp_isValid(ctypes.byref(self.value)) != 0

    def isEqual(self, rhs: Fp) -> bool:
        return mcl.mcl_lib.mclBnFp_isEqual(ctypes.byref(self.value), ctypes.byref(rhs.value)) != 0

    def __eq__(self, rhs: Fp) -> bool:
        return self.isEqual(rhs)
    
    def __ne__(self, rhs: Fp) -> bool:
        return not self.isEqual(rhs)

    def isZero(self) -> bool:
        return mcl.mcl_lib.mclBnFp_isZero(ctypes.byref(self.value)) != 0

    def isOne(self) -> bool:
        return mcl.mcl_lib.mclBnFp_isOne(ctypes.byref(self.value)) != 0

    def isOdd(self) -> bool:
        return mcl.mcl_lib.mclBnFp_isOdd(ctypes.byref(self.value)) != 0

    def isNegative(self) -> bool:
        return mcl.mcl_lib.mclBnFp_isNegative(ctypes.byref(self.value)) != 0

    # Unary arithmetic operators

    def neg(self) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def __neg__(self) -> Fp:
        return self.neg()
    
    def inv(self) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def sqr(self) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_sqr(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def squareRoot(self) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_squareRoot(ctypes.byref(res.value), ctypes.byref(self.value))
        return res

    # Binary arithmetic operators

    def add(self, rhs: Fp) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_add(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __add__(self, rhs: Fp) -> Fp:
        return self.add(rhs)

    def sub(self, rhs: Fp) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_sub(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __sub__(self, rhs: Fp) -> Fp:
        return self.sub(rhs)

    def mul(self, rhs: Fp) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_mul(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __mul__(self, rhs: Fp) -> Fp:
        return self.mul(rhs)

    def div(self, rhs: Fp) -> Fp:
        res = Fp()
        mcl.mcl_lib.mclBnFp_div(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __truediv__(self, rhs: Fp) -> Fp:
        return self.div(rhs)
