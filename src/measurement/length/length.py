import math
import operator
from typing import Tuple

from .length_meta import LengthMeta

from .. import REAL_TYPES, DEFAULT_FULL_FORM, DEFAULT_SHORT_FORM, DEFAULT_FORMS

from ... import _format_plural_form
from ... import _error, _validate, _operate, _type_error, _validation_operation
from ... import OPERATORS
from ...value_objects import Real, RealValidator


__all__ = [
    "Length"
]


class Length(metaclass=LengthMeta):
    
    __slots__ = [
        "_value",
    ]
    
    SIZE_SI = 1
    
    SHORT_FORM = DEFAULT_SHORT_FORM
    FULL_FORM = DEFAULT_FULL_FORM
    PREFIX_FORM = str()
    
    DEFAULT_LENGTH_VALUE = 0
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> Real:
        return self._value
    
    @value.setter
    def value(self, value: REAL_TYPES) -> None:
        s = f"\n\t{self.class_name}: "
        
        value = Real(value)
        handler = RealValidator._handle_exception
        handler(RealValidator.validate, s, value, 0)
        
        self._value = value
        
    def __init__(self, value: REAL_TYPES = DEFAULT_LENGTH_VALUE) -> None:
        self.value = value.value if isinstance(value, Length) else value
        
    # ------------------- Output ---------------------------
        
    def __format_value(self) -> str:
        return f"{self.value} {_format_plural_form(self.value, DEFAULT_FORMS)}"
        
    def print_short_form(self) -> str:
        return f"{self.value} {self.SHORT_FORM}"
        
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
        _validate(right, Length | REAL_TYPES, left, Length | REAL_TYPES, operator)
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _operate(right, REAL_TYPES, left, Length, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Length":
        return self
    def __neg__(self) -> "Length":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __abs__(self) -> "Length":
        return self
    
    def __inv__(self) -> "Length":
        return ~self
    def __invert__(self) -> "Length":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Length":
        return Length(math.floor(self.value))
    def __ceil__(self) -> "Length":
        return Length(math.ceil(self.value))
    def __trunc__(self) -> "Length":
        return Length(math.trunc(self.value))
    
    def __int__(self) -> int:
        return int(self.value)
    def __float__(self) -> float:
        return float(self.value)
    
    def __bool__(self) -> bool:
        return self.value != 0
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Length":
        return Length(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Length)
    
    def __eq__(self, other: object) -> bool:
        return Length._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Length._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Length._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Length._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Length._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Length._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> "Length":
        return Length(_validation_operation(right, left, operator, Length))
    
    def __add__(self, other: object) -> "Length":
        return Length._math(self, other, operator.add)
    def __radd__(self, other: object) -> "Length":
        return Length._math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Length":
        return Length._math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Length":
        return Length._math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Length":
        return Length._math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Length":
        return Length._math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Length":
        return Length._math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Length":
        return Length._math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Length":
        return Length._math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Length":
        return Length._math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Length":
        return Length._math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Length":
        return Length._math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Length":
        return Length._math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Length":
        return Length._math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Length":
        return Length._math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Length":
        return Length._math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Length":
        return Length._math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Length":
        return Length._math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Length":
        return Length._math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Length":
        return Length._math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Length":
        return Length._math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Length", "Length"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Length", "Length"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Length":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Length":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))