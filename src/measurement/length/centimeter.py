import math
import operator
from typing import Tuple

from .meter import Meter
from .length_converter import MeterConverter

from .. import REAL_TYPES


__all__ = [
    "CentiMeter",
]


class CentiMeter(Meter):
    
    __slots__ = [
        "__value",
    ]
    
    SIZE_SI = 10 ** (-2)
    
    PREFIX_FORM = "санти"
    SHORT_FORM = "с" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, REAL_TYPES) and type(left) == CentiMeter:
            return operator(right, left.value)
        if type(right) == CentiMeter and isinstance(left, REAL_TYPES):
            return operator(right.value, left)
        return operator(MeterConverter.convert(right).value, MeterConverter.convert(left).value)
    
    # ------------------- Unary operators ---------------------------
    
    def __floor__(self) -> "CentiMeter":
        return CentiMeter(math.floor(self.value))
    def __ceil__(self) -> "CentiMeter":
        return CentiMeter(math.ceil(self.value))
    def __trunc__(self) -> "CentiMeter":
        return CentiMeter(math.trunc(self.value))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "CentiMeter":
        return CentiMeter(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        CentiMeter._validate(right, left, operator)
        return CentiMeter._operate(right, left, operator)
    
    def __eq__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return CentiMeter._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> "CentiMeter":
        CentiMeter._validate(right, left, operator)
        real = CentiMeter._operate(right, left, operator)
        if isinstance(right, REAL_TYPES) or isinstance(left, REAL_TYPES):
            return CentiMeter(real)
        return MeterConverter.convert(Meter(real), CentiMeter)
    
    def __add__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.add)
    def __radd__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.add)
    def __iadd__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.sub)
    def __isub__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.mul)
    def __imul__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(other, self, operator.mod)
    def __imod__(self, other: object) -> "CentiMeter":
        return CentiMeter._math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["CentiMeter", "CentiMeter"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["CentiMeter", "CentiMeter"]:
        return (other // self, other % self)