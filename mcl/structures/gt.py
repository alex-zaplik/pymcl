from __future__ import annotations

from ..lib import mcl
from ..defines import GT_SIZE, IoMode
from .fr import Fr

import ctypes


class GT(ctypes.Structure):
    """
    A finite field of prime order `r`
    """
    
    _fields_ = [("value", ctypes.c_ulonglong * GT_SIZE)]

    def __init__(self, value = None):
        if isinstance(value, GT):
            self.value = value.value
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
        mcl.mclBnGT_clear(ctypes.byref(self.value))
    
    def setInt(self, x: int) -> None:
        """
        Sets the value to x
        """
        mcl.mclBnGT_setInt(ctypes.byref(self.value), x)

    def serialize(self) -> bytes:
        """
        Serializes the value to bytes
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        size = mcl.mclBnGT_serialize(buffer, len(buffer), ctypes.byref(self.value))
        return buffer[:size]
    
    def deserialize(self, buffer: bytes) -> None:
        """
        Deserializes bytes and sets the value
        """
        c_buffer = ctypes.create_string_buffer(buffer)
        mcl.mclBnGT_deserialize(ctypes.byref(self.value), c_buffer, len(buffer))

    def setStr(self, string: str, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Sets the value to the number in the string
        """
        mcl.mclBnGT_setStr(ctypes.byref(self.value), ctypes.c_char_p(string.encode()), len(string), io_mode.value)

    def getStr(self, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Returns a string with the value
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        mcl.mclBnGT_getStr(buffer, len(buffer), ctypes.byref(self.value), io_mode.value)
        return buffer.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    __repr__ = __str__
    
    # Checks

    def isEqual(self, rhs: GT) -> bool:
        return mcl.mclBnGT_isEqual(ctypes.byref(self.value), ctypes.byref(rhs.value)) != 0

    def __eq__(self, rhs: GT) -> bool:
        return self.isEqual(rhs)
    
    def __ne__(self, rhs: GT) -> bool:
        return not self.isEqual(rhs)

    def isZero(self) -> bool:
        return mcl.mclBnGT_isZero(ctypes.byref(self.value)) != 0

    def isOne(self) -> bool:
        return mcl.mclBnGT_isOne(ctypes.byref(self.value)) != 0

    def isOdd(self) -> bool:
        return mcl.mclBnGT_isOdd(ctypes.byref(self.value)) != 0

    # Unary arithmetic operators

    def neg(self) -> GT:
        res = GT()
        mcl.mclBnGT_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def __neg__(self) -> GT:
        return self.neg()
    
    def inv(self) -> GT:
        res = GT()
        mcl.mclBnGT_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def sqr(self) -> GT:
        res = GT()
        mcl.mclBnGT_sqr(ctypes.byref(res.value), ctypes.byref(self.value))
        return res

    # Binary arithmetic operators

    def add(self, rhs: GT) -> GT:
        res = GT()
        mcl.mclBnGT_add(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __add__(self, rhs: GT) -> GT:
        return self.add(rhs)

    def sub(self, rhs: GT) -> GT:
        res = GT()
        mcl.mclBnGT_sub(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __sub__(self, rhs: GT) -> GT:
        return self.sub(rhs)

    def mul(self, rhs: GT) -> GT:
        res = GT()
        mcl.mclBnGT_mul(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __mul__(self, rhs: GT) -> GT:
        return self.mul(rhs)

    def div(self, rhs: GT) -> GT:
        res = GT()
        mcl.mclBnGT_div(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __truediv__(self, rhs: GT) -> GT:
        return self.div(rhs)
    
    def pow(self, exp: Fr) -> GT:
        res = GT()
        mcl.mclBnGT_pow(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(exp.value))
        return res
    
    def __pow__(self, exp: Fr) -> GT:
        return self.pow(exp)
