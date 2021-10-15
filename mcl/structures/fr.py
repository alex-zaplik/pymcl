from __future__ import annotations

from ..lib import mcl
from ..defines import FR_SIZE, IoMode

import ctypes


class Fr(ctypes.Structure):
    """
    A finite field of prime order `r`
    """

    _fields_ = [("value", ctypes.c_ulonglong * FR_SIZE)]

    def __init__(self, value = None):
        if isinstance(value, int):
            self.setInt(value)
        elif isinstance(value, str):
            self.setStr(value)
        elif isinstance(value, bytes):
            self.deserialize(value)
    
    def clear(self) -> None:
        """
        Sets the value to 0
        """
        mcl.mclBnFr_clear(ctypes.byref(self.value))
    
    def setInt(self, x: int) -> None:
        """
        Sets the value to x
        """
        mcl.mclBnFr_setInt(ctypes.byref(self.value), x)
    
    # TODO: Set/Get little endian buff

    def serialize(self) -> bytes:
        """
        Serializes the value to bytes
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        size = mcl.mclBnFr_serialize(buffer, len(buffer), ctypes.byref(self.value))
        return buffer[:size]
    
    def deserialize(self, buffer: bytes) -> None:
        """
        Deserializes bytes and sets the value
        """
        c_buffer = ctypes.create_string_buffer(buffer)
        mcl.mclBnFr_deserialize(ctypes.byref(self.value), c_buffer, len(buffer))

    def setStr(self, string: str, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Sets the value to the number in the string
        """
        mcl.mclBnFr_setStr(ctypes.byref(self.value), ctypes.c_char_p(string.encode()), len(string), io_mode.value)

    def getStr(self, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Returns a string with the value
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        mcl.mclBnFr_getStr(buffer, len(buffer), ctypes.byref(self.value), io_mode.value)
        return buffer.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    __repr__ = __str__

    def setByCSPRNG(self) -> None:
        """
        Sets a random value
        """
        mcl.mclBnFr_setByCSPRNG(ctypes.byref(self.value))
    
    def setHashOf(self, data) -> None:
        """
        Set the hash of the data as the value
        """
        buffer = ctypes.create_string_buffer(data.encode())
        mcl.mclBnFr_setHashOf(ctypes.byref(self.value), buffer, len(buffer))
    
    # Checks

    def isValid(self) -> bool:
        return mcl.mclBnFr_isValid(ctypes.byref(self.value)) != 0

    def isEqual(self, rhs: Fr) -> bool:
        return mcl.mclBnFr_isEqual(ctypes.byref(self.value), ctypes.byref(rhs.value)) != 0

    def __eq__(self, rhs: Fr) -> bool:
        return self.isEqual(rhs)
    
    def __ne__(self, rhs: Fr) -> bool:
        return not self.isEqual(rhs)

    def isZero(self) -> bool:
        return mcl.mclBnFr_isZero(ctypes.byref(self.value)) != 0

    def isOne(self) -> bool:
        return mcl.mclBnFr_isOne(ctypes.byref(self.value)) != 0

    def isOdd(self) -> bool:
        return mcl.mclBnFr_isOdd(ctypes.byref(self.value)) != 0

    def isNegative(self) -> bool:
        return mcl.mclBnFr_isNegative(ctypes.byref(self.value)) != 0

    # Unary arithmetic operators

    def neg(self) -> Fr:
        res = Fr()
        mcl.mclBnFr_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def __neg__(self) -> Fr:
        return self.neg()
    
    def inv(self) -> Fr:
        res = Fr()
        mcl.mclBnFr_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def sqr(self) -> Fr:
        res = Fr()
        mcl.mclBnFr_sqr(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def squareRoot(self) -> Fr:
        res = Fr()
        mcl.mclBnFr_squareRoot(ctypes.byref(res.value), ctypes.byref(self.value))
        return res

    # Binary arithmetic operators

    def add(self, rhs: Fr) -> Fr:
        res = Fr()
        mcl.mclBnFr_add(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __add__(self, rhs: Fr) -> Fr:
        return self.add(rhs)

    def sub(self, rhs: Fr) -> Fr:
        res = Fr()
        mcl.mclBnFr_sub(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __sub__(self, rhs: Fr) -> Fr:
        return self.sub(rhs)

    def mul(self, rhs: Fr) -> Fr:
        res = Fr()
        mcl.mclBnFr_mul(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __mul__(self, rhs: Fr) -> Fr:
        return self.mul(rhs)

    def div(self, rhs: Fr) -> Fr:
        res = Fr()
        mcl.mclBnFr_div(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __truediv__(self, rhs: Fr) -> Fr:
        return self.div(rhs)
    
    # TODO: Lagrange interpolation
