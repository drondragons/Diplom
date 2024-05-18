import math
import operator
from typing import Tuple

from .. import REAL_TYPES

from ... import format_plural_form
from ... import DEFAULT_PLURAL_FORM, OPERATORS

from ...real import Real, RealValidator


__all__ = [
    "Meter",
    "NanoMeter",
    "DeciMeter",
    "KiloMeter",
    "PikoMeter",
    "MilliMeter",
    "CentiMeter",
    "FemtoMeter",
    "MicroMeter",
]


class MeterMeta(type):

    def __subclasscheck__(self, subclass: type) -> bool:
        return subclass in METER_CLASSES


class Meter(metaclass=MeterMeta):
    
    __slots__ = [
        "__value",
    ]
    
    SIZE_SI = 10 ** 0
    
    SHORT_FORM = "м"
    FULL_FORM = "метр"
    PREFIX_METER = str()
    
    DEFAULT_LENGTH_VALUE = 0
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> Real:
        return self.__value
    
    @value.setter
    def value(self, value: REAL_TYPES) -> None:
        value = Real(value)
        exception, message = RealValidator.validate_interval(value, 0)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__value = value
        
    def __init__(self, value: REAL_TYPES = DEFAULT_LENGTH_VALUE) -> None:
        self.value = value.value if isinstance(value, Meter) else value
        
    # ------------------- Output ---------------------------
        
    def __format_value(self) -> str:
        meter_forms = [self.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
        return f"{self.value} {format_plural_form(self.value, meter_forms)}"
        
    def print_short_form(self) -> str:
        return f"{self.value} {self.SHORT_FORM}\n"
        
    def __str__(self) -> str:
        return f"{self.__format_value()}\n"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (value: {self.__format_value()})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash(self.value)
    
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
        message = Meter.__type_error(right, left, operator)
        if not isinstance(right, Meter | REAL_TYPES):
            raise TypeError(Meter.__error(left, message))
        if not isinstance(left, Meter | REAL_TYPES):
            raise TypeError(Meter.__error(right, message))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def __operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, REAL_TYPES) and isinstance(left, Meter):
            return operator(right, left.value)
        if isinstance(right, Meter) and isinstance(left, REAL_TYPES):
            return operator(right.value, left)
        return operator(right.value, left.value)
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Meter":
        return self
    def __neg__(self) -> "Meter":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(Meter.__error(self, message))
    
    def __abs__(self) -> "Meter":
        return self
    
    def __inv__(self) -> "Meter":
        return ~self
    def __invert__(self) -> "Meter":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(Meter.__error(self, message))
    
    def __floor__(self) -> "Meter":
        return Meter(math.floor(self.value))
    def __ceil__(self) -> "Meter":
        return Meter(math.ceil(self.value))
    def __trunc__(self) -> "Meter":
        return Meter(math.trunc(self.value))
    
    def __int__(self) -> int:
        return math.floor(self.value)
    def __float__(self) -> float:
        return float(self.value)
    
    def __bool__(self) -> bool:
        return self.value != 0
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Meter":
        return Meter(round(self.value, n))
    
    # ------------------- Comparison operators ---------------------------
    
    @staticmethod
    def __compare(right: object, left: object, operator: operator) -> bool:
        Meter.__validate(right, left, operator)
        return Meter.__operate(right, left, operator)
    
    def __eq__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.ne)
    
    def __lt__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.lt)
    def __le__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.le)
    
    def __gt__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.gt)
    def __ge__(self, other: object) -> bool:
        return Meter.__compare(self, other, operator.ge)
    
    # ------------------- Mathematical operators ---------------------------
    
    @staticmethod
    def __math(right: object, left: object, operator: operator) -> "Meter":
        Meter.__validate(right, left, operator)
        return Meter(Meter.__operate(right, left, operator))
    
    def __add__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.add)
    def __radd__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.add)
    def __iadd__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.iadd)
    
    def __sub__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.sub)
    def __rsub__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.sub)
    def __isub__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.isub)
    
    def __mul__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.mul)
    def __rmul__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.mul)
    def __imul__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.imul)
    
    def __pow__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.pow)
    def __rpow__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.pow)
    def __ipow__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.ipow)
    
    def __truediv__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.truediv)
    def __rtruediv__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.truediv)
    def __itruediv__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.itruediv)
    
    def __floordiv__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.floordiv)
    def __rfloordiv__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.floordiv)
    def __ifloordiv__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.ifloordiv)
    
    def __mod__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.mod)
    def __rmod__(self, other: object) -> "Meter":
        return Meter.__math(other, self, operator.mod)
    def __imod__(self, other: object) -> "Meter":
        return Meter.__math(self, other, operator.imod)
    
    def __divmod__(self, other: object) -> Tuple["Meter", "Meter"]:
        return (self // other, self % other)
    def __rdivmod__(self, other: object) -> Tuple["Meter", "Meter"]:
        return (other // self, other % self)
    
    def __matmul__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Meter":
        raise TypeError(Meter.__error(self, Meter.__type_error(self, other, operator.ixor)))
    
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Meter":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(Meter.__error(self, message))
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(Meter.__error(self, message))
    

class NanoMeter(Meter):
    
    SIZE_SI = 10 ** (-9)
    
    PREFIX_FORM = "нано"
    SHORT_FORM = "н" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM   


class DeciMeter(Meter):
    
    SIZE_SI = 10 ** (-1)
    
    PREFIX_FORM = "деци"
    SHORT_FORM = "д" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    
class KiloMeter(Meter):
    
    SIZE_SI = 10 ** 3
    
    PREFIX_FORM = "кило"
    SHORT_FORM = "к" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    

class PikoMeter(Meter):
    
    SIZE_SI = 10 ** (-12)
    
    PREFIX_FORM = "пико"
    SHORT_FORM = "п" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    
class MilliMeter(Meter):
    
    SIZE_SI = 10 ** (-3)
    
    PREFIX_FORM = "милли"
    SHORT_FORM = "м" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    
class CentiMeter(Meter):
    
    SIZE_SI = 10 ** (-2)
    
    PREFIX_FORM = "санти"
    SHORT_FORM = "с" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    

class FemtoMeter(Meter):
    
    SIZE_SI = 10 ** (-15)
    
    PREFIX_FORM = "фемто"
    SHORT_FORM = "ф" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    

class MicroMeter(Meter):
    
    SIZE_SI = 10 ** (-6)
    
    PREFIX_FORM = "микро"
    SHORT_FORM = "мк" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    

METER_CLASSES = [
    KiloMeter,
    Meter,
    DeciMeter,
    CentiMeter,
    MilliMeter,
    MicroMeter,
    NanoMeter,
    PikoMeter,
    FemtoMeter,
]