from __future__ import annotations

from ..lib import mcl
from ..defines import G2_SIZE, IoMode
from .fr import Fr

import ctypes


class G2(ctypes.Structure):
    """
    The cyclic subgroup of the inverse image of E'(Fp^2)
    under a twisting isomorphism from E' to E
    """

    _fields_ = [("value", ctypes.c_ulonglong * G2_SIZE)]

    def __init__(self, value = None):
        if isinstance(value, G2):
            self.value = value.value
        elif isinstance(value, str):
            self.setStr(value)
        elif isinstance(value, bytes):
            self.deserialize(value)
    
    def clear(self) -> None:
        """
        Sets the value to 0
        """
        mcl.mclBnG2_clear(ctypes.byref(self.value))

    def serialize(self) -> bytes:
        """
        Serializes the value to bytes
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        size = mcl.mclBnG2_serialize(buffer, len(buffer), ctypes.byref(self.value))
        return buffer[:size]
    
    def deserialize(self, buffer: bytes) -> None:
        """
        Deserializes bytes and sets the value
        """
        c_buffer = ctypes.create_string_buffer(buffer)
        mcl.mclBnG2_deserialize(ctypes.byref(self.value), c_buffer, len(buffer))

    def setStr(self, string: str, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Sets the value to the number in the string
        """
        mcl.mclBnG2_setStr(ctypes.byref(self.value), ctypes.c_char_p(string.encode()), len(string), io_mode.value)

    def getStr(self, io_mode: IoMode = IoMode.DEC) -> None:
        """
        Returns a string with the value
        """
        buffer_len = 1024
        buffer = ctypes.create_string_buffer(buffer_len)
        mcl.mclBnG2_getStr(buffer, len(buffer), ctypes.byref(self.value), io_mode.value)
        return buffer.value.decode()

    def __str__(self) -> str:
        return self.getStr()

    __repr__ = __str__
    
    @staticmethod
    def hashAndMapTo(data) -> None:
        """
        Set the mapping of the hash of the data as the value
        """
        res = G2()
        buffer = ctypes.create_string_buffer(data.encode())
        mcl.mclBnG2_hashAndMapTo(ctypes.byref(res.value), buffer, len(buffer))
        return res
    
    # Checks

    def isValid(self) -> bool:
        return mcl.mclBnG2_isValid(ctypes.byref(self.value)) != 0

    def isValidOrder(self) -> bool:
        return mcl.mclBnG2_isValidOrder(ctypes.byref(self.value)) != 0

    def isEqual(self, rhs: G2) -> bool:
        return mcl.mclBnG2_isEqual(ctypes.byref(self.value), ctypes.byref(rhs.value)) != 0

    def __eq__(self, rhs: G2) -> bool:
        return self.isEqual(rhs)
    
    def __ne__(self, rhs: G2) -> bool:
        return not self.isEqual(rhs)

    def isZero(self) -> bool:
        return mcl.mclBnG2_isZero(ctypes.byref(self.value)) != 0

    # Unary arithmetic operators

    def neg(self) -> G2:
        res = G2()
        mcl.mclBnG2_neg(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def __neg__(self) -> G2:
        return self.neg()
    
    def dbl(self) -> G2:
        res = G2()
        mcl.mclBnG2_dbl(ctypes.byref(res.value), ctypes.byref(self.value))
        return res
    
    def normalize(self) -> G2:
        res = G2()
        mcl.mclBnG2_normalize(ctypes.byref(res.value), ctypes.byref(self.value))
        return res

    # Binary arithmetic operators

    def add(self, rhs: G2) -> G2:
        res = G2()
        mcl.mclBnG2_add(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __add__(self, rhs: G2) -> G2:
        return self.add(rhs)

    def sub(self, rhs: G2) -> G2:
        res = G2()
        mcl.mclBnG2_sub(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __sub__(self, rhs: G2) -> G2:
        return self.sub(rhs)

    def mul(self, rhs: Fr) -> G2:
        res = G2()
        mcl.mclBnG2_mul(ctypes.byref(res.value), ctypes.byref(self.value), ctypes.byref(rhs.value))
        return res
    
    def __mul__(self, rhs: Fr) -> G2:
        return self.mul(rhs)

    # Array arithmetic operators

    # TODO: mulVec