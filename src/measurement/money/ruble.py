import math
import operator
from typing import Tuple

from . import _money_operate
from .money import Money

from .. import REAL_TYPES

from ... import _validation_operation


__all__ = [
    "Ruble",
]


class Ruble(Money):
    
    SHORT_FORM = "руб"
    FULL_FORM = "рубль"
    INTERNATIONAL_FORM = "RUB"
    SYMBOL = "₽"
    PLURAL_MONEY_FORMS = [
        FULL_FORM,
        "рубля",
        "рублей",
    ]
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _money_operate(right, REAL_TYPES, left, Ruble, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __floor__(self) -> "Ruble":
        return Ruble(math.floor(self.value))
    def __ceil__(self) -> "Ruble":
        return Ruble(math.ceil(self.value))
    def __trunc__(self) -> "Ruble":
        return Ruble(math.trunc(self.value))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Ruble":
        return Ruble(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Ruble)
    
    def __eq__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Ruble._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> "Ruble":
        return Ruble(_validation_operation(right, left, operator, Ruble))
    
    def __add__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.add)
    def __radd__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Ruble":
        return Ruble._math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Ruble":
        return Ruble._math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Ruble", "Ruble"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Ruble", "Ruble"]:
        return (other // self, other % self)