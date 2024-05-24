import operator
from typing import Tuple

from ..price import Price

from ... import _validate, _error, _type_error, OPERATORS
from ...geometry import Line
from ...measurement import Money, MoneyValidator, MoneyConverter, Ruble
from ...measurement import Length, LengthValidator, Meter, SquarePrinter
from ...value_objects import Title


__all__ = [
    "Flat",
]


class Flat:
    
    __slots__ = [
        "_footage",
        "_price_per_meter",
        "_title",
    ]
    
    DEFAULT_TITLE = "Квартира"
    DEFAULT_FOOTAGE = Meter(33)
    DEFAULT_PRICE_PER_METER = Money(100_000)
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def footage(self) -> Line:
        return self._footage
    
    @footage.setter
    def footage(self, footage: Length) -> None:
        s = f"\n\t{self.class_name}: "
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, footage, 0)
        handler(LengthValidator.validate_object_type, s, footage, Length | Meter)
        self._footage = Line(footage, "Метраж")
        
    @property
    def price_per_meter(self) -> Price:
        return self._price_per_meter
    
    @price_per_meter.setter
    def price_per_meter(self, price_per_meter: Money) -> None:
        s = f"\n\t{self.class_name}: "
        handler = MoneyValidator._handle_exception
        handler(MoneyValidator.validate, s, price_per_meter, 0)
        self._price_per_meter = Price(price_per_meter, "Цена за квадратный метр")
        
    @property
    def title(self) -> Title:
        return self._title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self._title = Title(title)
        
    @property
    def price(self) -> Price:
        price = self.footage.length.value * self.price_per_meter.value.value
        return Price(type(self.price_per_meter.value)(price))
    
    @property
    def maximum_person_amount(self) -> int:
        if self.footage <= 33:
            return 1
        elif self.footage <= 42:
            return 2
        return self.footage // 18
    
    def __init__(
        self, 
        footage: Length = DEFAULT_FOOTAGE,
        price_per_meter: Money = DEFAULT_PRICE_PER_METER,
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.footage = footage
        self.price_per_meter = price_per_meter
        self.title = title
        
    # ------------------- Output ---------------------------

    def print_footage(self) -> str:
        result = f"{self.footage.title}:\t"
        return result + f"{SquarePrinter.print_full_form(self.footage.length)}"

    def __str__(self) -> str:
        result = f"{self.title}:"
        result += f"\n\t{self.print_footage()}\n\t{self.price_per_meter}"
        return result + f"\n\t{self.price}\n"
    
    def __repr__(self) -> str:
        result = f"{self.class_name} "
        result += f"(title: {self.title}, footage: {self.footage}, "
        return result + f"price_per_meter: {self.price_per_meter})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.footage, self.price_per_meter, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Flat, left, Flat, operator)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Flat":
        message = f"Операция {OPERATORS[operator.add]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    def __neg__(self) -> "Flat":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __abs__(self) -> "Flat":
        message = f"Операция abs({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    def __inv__(self) -> "Flat":
        return ~self
    def __invert__(self) -> "Flat":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Flat":
        message = f"Операция math.floor({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __ceil__(self) -> "Flat":
        message = f"Операция math.ceil({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __trunc__(self) -> "Flat":
        message = f"Операция math.trunc({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    def __int__(self) -> int:
        message = f"Операция int({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __float__(self) -> float:
        message = f"Операция float({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Flat":
        message = f"Операция round({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return self.price_per_meter != 0 and self.footage != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Flat._validate(right, left, operator)
        return operator(right.footage, left.footage) and \
            operator(right.price_per_meter, left.price_per_meter)
        
    def __eq__(self, other: object) -> bool:
        return Flat._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Flat._equality(self, other, operator.ne)
        
    def __lt__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.lt)))
    def __le__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.le)))
    
    def __gt__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.gt)))
    def __ge__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.ge)))    
        
    # ------------------- Mathematical operators ---------------------------
    
    def __add__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.add)))
    def __radd__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.add)))
    def __iadd__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.iadd)))
    
    def __sub__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.sub)))
    def __rsub__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.sub)))
    def __isub__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.isub)))
    
    def __mul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.mul)))
    def __rmul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.mul)))
    def __imul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.imul)))
    
    def __pow__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.pow)))
    def __rpow__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.pow)))
    def __ipow__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.ipow)))
    
    def __truediv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.truediv)))
    def __rtruediv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.truediv)))
    def __itruediv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.itruediv)))
    
    def __floordiv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.floordiv)))
    def __rfloordiv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.floordiv)))
    def __ifloordiv__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.ifloordiv)))
    
    def __mod__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.mod)))
    def __rmod__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.mod)))
    def __imod__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.imod)))
    
    def __divmod__(self, other: object) -> Tuple["Flat", "Flat"]:
        message = f"Операция divmod недоступна!"
        raise TypeError(_error(self, message))
    def __rdivmod__(self, other: object) -> Tuple["Flat", "Flat"]:
        message = f"Операция divmod недоступна!"
        raise TypeError(_error(self, message))
    
    def __matmul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Flat":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
        
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Flat":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))