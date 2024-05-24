import math
import operator
from typing import Tuple

from ... import _error, _type_error, _operate, _validate, _validation_operation
from ... import OPERATORS, REAL_TYPES
from ...measurement import Money, MoneyValidator, MoneyConverter, Ruble
from ...value_objects import Title


__all__ = [
    "Price",
]


class Price:
    
    __slots__ = [
        "_value",
        "_title",
    ]
    
    DEFAULT_TITLE = "Стоимость"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> Money:
        return self._value
    
    @value.setter
    def value(self, value: Money) -> None:
        s = f"\n\t{self.class_name}: "
        handler = MoneyValidator._handle_exception
        handler(MoneyValidator.validate, s, value, 0)
        self._value = MoneyConverter.convert(value, Ruble)
        
    @property
    def title(self) -> Title:
        return self._title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self._title = Title(title)
        
    def __init__(
        self,
        value: Money = Money(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.value = value
        self.title = title
        
    # ------------------- Output ---------------------------
        
    def __str__(self) -> str:
        return f"{self.title}:\t{self.value}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, value: {self.value})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.value, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        types = Price | Money | REAL_TYPES
        _validate(right, types, left, types, operator)
        
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def _operate(right: object, left: object, operator: operator) -> object:
        return _operate(right, Money | REAL_TYPES, left, Price, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Price":
        return self
    def __neg__(self) -> "Price":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __abs__(self) -> "Price":
        return self
    
    def __inv__(self) -> "Price":
        return ~self
    def __invert__(self) -> "Price":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Price":
        return Price(math.floor(self.value), self.title)
    def __ceil__(self) -> "Price":
        return Price(math.ceil(self.value), self.title)
    def __trunc__(self) -> "Price":
        return Price(math.trunc(self.value), self.title)
    
    def __int__(self) -> int:
        return math.floor(self.value)
    def __float__(self) -> float:
        return float(self.value)
    
    def __bool__(self) -> bool:
        return self.value != 0
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Price":
        return Price(round(self.value, n), self.title)
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def _compare(right: object, left: object, operator: operator) -> bool:
        return _validation_operation(right, left, operator, Price)
    
    def __eq__(self, other: object) -> bool:
        return Price._compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Price._compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Price._compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Price._compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Price._compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Price._compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def _math(right: object, left: object, operator: operator) -> Money:
        return _validation_operation(right, left, operator, Price)
    
    def __add__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.add), self.title)
    def __radd__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.add), self.title)
    def __iadd__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.iadd), self.title)
    
    def __sub__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.sub), self.title)
    def __rsub__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.sub), self.title)
    def __isub__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.isub), self.title)
    
    def __mul__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.mul), self.title)
    def __rmul__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.mul), self.title)
    def __imul__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.imul), self.title)
    
    def __pow__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.pow), self.title)
    def __rpow__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.pow), self.title)
    def __ipow__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.ipow), self.title)
    
    def __truediv__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.truediv), self.title)
    def __rtruediv__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.truediv), self.title)
    def __itruediv__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.itruediv), self.title)
    
    def __floordiv__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.floordiv), self.title)
    def __rfloordiv__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.floordiv), self.title)
    def __ifloordiv__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.ifloordiv), self.title)
    
    def __mod__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.mod), self.title)
    def __rmod__(self, other: object) -> "Price":
        return Price(Price._math(other, self, operator.mod), self.title)
    def __imod__(self, other: object) -> "Price":
        return Price(Price._math(self, other, operator.imod), self.title)
    
    def __divmod__(self, other: object) -> Tuple["Price", "Price"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Price", "Price"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Price":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Price":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))