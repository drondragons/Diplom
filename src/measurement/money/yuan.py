import math
import operator
from typing import Tuple

from .money import Money
from .money_converter import MoneyConverter

from .. import REAL_TYPES


__all__ = [
    "Yuan",
]


class Yuan(Money):
    
    SHORT_FORM = str()
    FULL_FORM = "юань"
    INTERNATIONAL_FORM = "CNY"
    SYMBOL = "¥"
    PLURAL_MONEY_FORMS = [
        FULL_FORM,
        "юаня",
        "юаней",
    ]
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, REAL_TYPES) and type(left) == Yuan:
            return operator(right, left.value)
        if type(right) == Yuan and isinstance(left, REAL_TYPES):
            return operator(right.value, left)
        if type(right) == Money or type(left) == Money:
            return operator(Yuan(left).value, Yuan(right).value)
        left = MoneyConverter.convert(left, Yuan).value
        right = MoneyConverter.convert(right, Yuan).value
        return operator(right, left)
    
    # ------------------- Unary operators ---------------------------
    
    def __floor__(self) -> "Yuan":
        return Yuan(math.floor(self.value))
    def __ceil__(self) -> "Yuan":
        return Yuan(math.ceil(self.value))
    def __trunc__(self) -> "Yuan":
        return Yuan(math.trunc(self.value))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Yuan":
        return Yuan(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        Yuan._validate(right, left, operator)
        return Yuan._operate(right, left, operator)
    
    def __eq__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Yuan._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> "Yuan":
        Yuan._validate(right, left, operator)
        return Yuan(Yuan._operate(right, left, operator))
    
    def __add__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.add)
    def __radd__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Yuan":
        return Yuan._math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Yuan":
        return Yuan._math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Yuan", "Yuan"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Yuan", "Yuan"]:
        return (other // self, other % self)