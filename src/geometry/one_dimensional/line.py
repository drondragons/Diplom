import math
import operator
from typing import Tuple

from .. import LENGTH_TYPES

from ... import OPERATORS
from ...title import Title, TitleValidator
from ...measurement import Length, LengthValidator, MeterConverter


__all__ = [
    "Line"
]


class Line:
    
    __slots__ = [
        "__length",
        "__title",
    ]
    
    DEFAULT_TITLE = "Отрезок"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def length(self) -> Length:
        return self.__length
    
    @length.setter
    def length(self, length: Length) -> None:
        exception, message = LengthValidator.validate(length)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__length = length
        
    @property
    def title(self) -> Title:
        return self.__title
    
    @title.setter
    def title(self, title: Title) -> None:
        exception, message = TitleValidator.validate(title, False)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__title = title
        
    def __init__(
        self, 
        length: Length = Length(), 
        title: Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.length = length
        self.title = title
        
    # ------------------- Output ---------------------------
        
    def __format_length(self) -> str:
        return self.length \
            if type(self.length) == Length else \
                MeterConverter.auto_convert(self.length)
        
    def __str__(self) -> str:
        return f"{self.title}: {self.__format_length()}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, value: {self.__format_length()})"

    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.length, self.title))
    
    # ------------------- Error validation ---------------------------
    
    @staticmethod
    def __error(obj: object, message: str = str()) -> str:
        return f"\n\t{type(obj).__name__}: {message}"
    
    @staticmethod
    def __type_error(right: object, left: object, operator: operator) -> str:
        left_name = f"'{type(left).__name__}'"
        right_name = f"'{type(right).__name__}'"
        return f"Операция {right_name} {OPERATORS[operator]} {left_name} недоступна!"
    
    @staticmethod
    def __validate(right: object, left: object, operator: operator) -> None:
        message = Line.__type_error(right, left, operator)
        if not isinstance(right, Line | LENGTH_TYPES):
            raise TypeError(Line.__error(left, message))
        if not isinstance(left, Line | LENGTH_TYPES):
            raise TypeError(Line.__error(right, message))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def __operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, LENGTH_TYPES) and isinstance(left, Line):
            return operator(right, left.length)
        if isinstance(right, Line) and isinstance(left, LENGTH_TYPES):
            return operator(right.length, left)
        return operator(right.length, left.length)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Line":
        return self
    def __neg__(self) -> "Line":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(Line.__error(self, message))
    
    def __abs__(self) -> "Line":
        return self
    
    def __inv__(self) -> "Line":
        return ~self
    def __invert__(self) -> "Line":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(Line.__error(self, message))
    
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
    def __compare(right: object, left: object, operator: operator) -> bool:
        Line.__validate(right, left, operator)
        return Line.__operate(right, left, operator)
    
    def __eq__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Line.__compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def __math(right: object, left: object, operator: operator) -> "Line":
        Line.__validate(right, left, operator)
        return Line.__operate(right, left, operator)
    
    def __add__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.add), self.title)
    def __radd__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.add), self.title)
    def __iadd__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.iadd), self.title)
    
    def __sub__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.sub), self.title)
    def __rsub__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.sub), self.title)
    def __isub__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.isub), self.title)
    
    def __mul__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.mul), self.title)
    def __rmul__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.mul), self.title)
    def __imul__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.imul), self.title)
    
    def __pow__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.pow), self.title)
    def __rpow__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.pow), self.title)
    def __ipow__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.ipow), self.title)
    
    def __truediv__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.truediv), self.title)
    def __rtruediv__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.truediv), self.title)
    def __itruediv__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.itruediv), self.title)
    
    def __floordiv__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.floordiv), self.title)
    def __rfloordiv__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.floordiv), self.title)
    def __ifloordiv__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.ifloordiv), self.title)
    
    def __mod__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.mod), self.title)
    def __rmod__(self, other: object) -> "Line":
        return Line(Line.__math(other, self, operator.mod), self.title)
    def __imod__(self, other: object) -> "Line":
        return Line(Line.__math(self, other, operator.imod), self.title)
    
    def __divmod__(self, other: object) -> Tuple["Line", "Line"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Line", "Line"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Line":
        raise TypeError(Line.__error(self, Line.__type_error(self, other, operator.ixor)))
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Line":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(Line.__error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(Line.__error(self, message))