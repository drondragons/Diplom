import math
import operator
from typing import Tuple

from .. import OPERATORS
from .. import _format_number
from .. import _error, _validate, _operate, _type_error, _validation_operation
from ..validators import NUMBER_TYPES
from ..validators import NumberValidator


__all__ = [
    "Real",
]


class Real:
    
    __slots__ = [
        "__value"
    ]
    
    DEFAULT_REAL_VALUE = 0
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> NUMBER_TYPES:
        return self.__value
    
    @value.setter
    def value(self, value: NUMBER_TYPES) -> None:
        s = f"\n\t{self.class_name}: "
        NumberValidator._handle_exception(NumberValidator.validate, s, value, NUMBER_TYPES)
        self.__value = value
        
    def __init__(self, value: NUMBER_TYPES = DEFAULT_REAL_VALUE) -> None:
        self.value = value.value if isinstance(value, Real) else value
        
    # ------------------- Output ---------------------------
        
    def __format_value(self) -> str:
        return f"{_format_number(self.value)}"
        
    def __str__(self) -> str:
        return self.__format_value()
    
    def __repr__(self) -> str:
        return f"{self.class_name} (value: {self.__format_value()})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Real | NUMBER_TYPES, left, Real | NUMBER_TYPES, operator)
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _operate(right, NUMBER_TYPES, left, Real, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Real":
        return self
    def __neg__(self) -> "Real":
        return Real(-self.value)
    
    def __abs__(self) -> "Real":
        return Real(abs(self.value))
    
    def __inv__(self) -> "Real":
        return ~self
    def __invert__(self) -> "Real":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Real":
        return Real(math.floor(self.value))
    def __ceil__(self) -> "Real":
        return Real(math.ceil(self.value))
    def __trunc__(self) -> "Real":
        return Real(math.trunc(self.value))
    
    def __int__(self) -> int:
        return math.floor(self.value)
    def __float__(self) -> float:
        return float(self.value)
    
    def __bool__(self) -> bool:
        return self.value != 0
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Real":
        return Real(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def __compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Real)
    
    def __eq__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Real.__compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def __math(right: object, left: object, operator: operator) -> "Real":
        return Real(_validation_operation(right, left, operator, Real))
    
    def __add__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.add)
    def __radd__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Real":
        return Real.__math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Real":
        return Real.__math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Real", "Real"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Real", "Real"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Real":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
        
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Real":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))