import math
import operator
from .. import format_number
from ..validators.constants import NUMBER_TYPES
from .constants import DEFAULT_REAL_VALUE, OPERATORS
from ..validators.number_validator import NumberValidator

__all__ = [
    "Real"
]

class Real:
    
    __slots__ = [
        "__value"
    ]
    
    @property
    def value(self) -> NUMBER_TYPES:
        return self.__value
    
    @value.setter
    def value(self, value: object) -> None:
        exception, message = NumberValidator.validate(value, NUMBER_TYPES)
        if exception:
            raise exception(f"'{self.__class__.__name__}': " + message)
        self.__value = value
        
    def __init__(self, value: object = DEFAULT_REAL_VALUE) -> None:
        self.value = value
        
    def __format_value(self) -> str:
        return f"{format_number(self.value)}"
        
    def __str__(self) -> str:
        return self.__format_value()
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (value: {self.__format_value()})"
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __format__(self, format_spec: str = str(), /) -> "Real":
        raise TypeError(f"'{self.__class__.__name__}': Операция форматирования (format({self.__class__.__name__})) недоступна!")
    
    def __index__(self) -> "Real":
        raise TypeError(f"'{self.__class__.__name__}': Операция индексирования ({self.__class__.__name__}[index]) недоступна!")
    
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
        raise TypeError(f"\n\t'{self.__class__.__name__}': Операция {OPERATORS[operator.inv]}{self.__class__.__name__} недоступна!")
    
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
    
    def __compare(self, other: object, operator: operator) -> bool:
        if not isinstance(other, Real | NUMBER_TYPES):
            raise TypeError(f"'{self.__class__.__name__}': Операция {self.__class__.__name__} {OPERATORS[operator]} {type(other).__name__} недоступна!")
        if isinstance(other, Real):
            return operator(self.value, other.value)
        return operator(self.value, other)
    
    def __eq__(self, other: object) -> bool:
        return self.__compare(other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return self.__compare(other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return self.__compare(other, operator.lt)
    def __le__(self, other: object) -> bool:
        return self.__compare(other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return self.__compare(other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return (self.__compare(other, operator.ge))
    
    # @classmethod
    # def min(cls, right: "Side", left: "Side") -> "Side":
    #     if not isinstance(left, Side) and not isinstance(right, Side):
    #         return TypeError(f"Недопустимый тип для операции min!")
    #     return min(right.value, left.value)
    
    # @classmethod
    # def max(cls, right: "Side", left: "Side") -> "Side":
    #     if not isinstance(left, Side) and not isinstance(right, Side):
    #         return TypeError(f"Недопустимый тип для операции max!")
    #     return max(right.value, left.value)