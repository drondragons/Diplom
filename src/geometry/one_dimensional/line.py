import math
import operator
from typing import Tuple

from . import _line_operate

from .. import LENGTH_TYPES

from ... import _error, _type_error, _validate, _validation_operation
from ...constants import OPERATORS
from ...measurement import Length, LengthValidator, MeterConverter
from ...value_objects import Title


__all__ = [
    "Line"
]


class Line:
    
    __slots__ = [
        "_length",
        "_title",
    ]
    
    DEFAULT_TITLE = "Отрезок"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def length(self) -> Length:
        return self._length
    
    @length.setter
    def length(self, length: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, length, 0)
        
        self._length = MeterConverter.auto_convert(length)
        
    @property
    def title(self) -> Title:
        return self._title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self._title = Title(title)
        
    def __init__(
        self, 
        length: Length = Length(), 
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.length = length
        self.title = title
        
    # ------------------- Output ---------------------------
        
    def __str__(self) -> str:
        return f"{self.title}:\t{self.length}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, length: {self.length})"

    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Line | LENGTH_TYPES, left, Line | LENGTH_TYPES, operator)
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _line_operate(right, LENGTH_TYPES, left, Line, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Line":
        return self
    def __neg__(self) -> "Line":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __abs__(self) -> "Line":
        return self
    
    def __inv__(self) -> "Line":
        return ~self
    def __invert__(self) -> "Line":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Line":
        return Line(math.floor(self.length), self.title)
    def __ceil__(self) -> "Line":
        return Line(math.ceil(self.length), self.title)
    def __trunc__(self) -> "Line":
        return Line(math.trunc(self.length), self.title)
    
    def __int__(self) -> int:
        return math.floor(self.length)
    def __float__(self) -> float:
        return float(self.length)
    
    def __bool__(self) -> bool:
        return self.length != 0
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Line":
        return Line(round(self.length, n), self.title)
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Line)
    
    def __eq__(self, other: object) -> bool:
        return Line._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Line._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Line._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Line._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Line._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Line._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> Length:
        return _validation_operation(right, left, operator, Line)
    
    def __add__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.add), self.title)
    def __radd__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.add), self.title)
    def __iadd__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.iadd), self.title)
    
    def __sub__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.sub), self.title)
    def __rsub__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.sub), self.title)
    def __isub__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.isub), self.title)
    
    def __mul__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.mul), self.title)
    def __rmul__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.mul), self.title)
    def __imul__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.imul), self.title)
    
    def __pow__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.pow), self.title)
    def __rpow__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.pow), self.title)
    def __ipow__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.ipow), self.title)
    
    def __truediv__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.truediv), self.title)
    def __rtruediv__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.truediv), self.title)
    def __itruediv__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.itruediv), self.title)
    
    def __floordiv__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.floordiv), self.title)
    def __rfloordiv__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.floordiv), self.title)
    def __ifloordiv__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.ifloordiv), self.title)
    
    def __mod__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.mod), self.title)
    def __rmod__(self, other: object) -> "Line":
        return Line(Line._math(other, self, operator.mod), self.title)
    def __imod__(self, other: object) -> "Line":
        return Line(Line._math(self, other, operator.imod), self.title)
    
    def __divmod__(self, other: object) -> Tuple["Line", "Line"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Line", "Line"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Line":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Line":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))