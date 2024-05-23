import math
import operator
from typing import Tuple

from .length import Length

from .. import REAL_TYPES

from ... import _format_plural_form
from ... import _validate, _operate, _validation_operation
from ... import DEFAULT_PLURAL_FORM


__all__ = [
    "Meter",
]


class Meter(Length):
    
    SIZE_SI = 10 ** 0
    
    SHORT_FORM = "м"
    FULL_FORM = "метр"
    PREFIX_METER = str()
    
    # ------------------- Output ---------------------------
    
    def __format_value(self) -> str:
        meter_forms = [self.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
        return f"{self.value} {_format_plural_form(self.value, meter_forms)}"
    
    def __str__(self) -> str:
        return f"{self.__format_value()}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (value: {self.__format_value()})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        types = Length | Meter | REAL_TYPES
        _validate(right, types, left, types, operator)
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _operate(right, REAL_TYPES, left, Meter, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __floor__(self) -> "Meter":
        return Meter(math.floor(self.value))
    def __ceil__(self) -> "Meter":
        return Meter(math.ceil(self.value))
    def __trunc__(self) -> "Meter":
        return Meter(math.trunc(self.value))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Meter":
        return Meter(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Meter)
    
    def __eq__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Meter._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> "Meter":
        return Meter(_validation_operation(right, left, operator, Meter))
    
    def __add__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.add)
    def __radd__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Meter":
        return Meter._math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Meter":
        return Meter._math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Meter", "Meter"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Meter", "Meter"]:
        return (other // self, other % self)