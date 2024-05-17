import math
import operator
from ..real import Real
from ..constants import OPERATORS
from .. import format_plural_form
from ..validators.number_validator import NumberValidator
from .constants import NUMBER_TYPES, DEFAULT_LENGTH_VALUE, DEFAULT_PLURAL_FORM

__all__ = [
    "Meter",
]

class Meter:
    
    __slots__ = [
        "__value",
    ]
    
    SHORT_FORM = "м"
    FULL_FORM = "метр"
    PREFIX_METER = str()
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def value(self) -> Real:
        return self.__value
    
    @value.setter
    def value(self, value: Real) -> None:
        print(type(value))
        exception, message = NumberValidator.validate(value, Real, 0)
        print(exception, message)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__value = value
        
    def __init__(self, value: object = DEFAULT_LENGTH_VALUE) -> None:
        self.value = value
        
    # ------------------- Output ---------------------------
        
    def __format_value(self) -> str:
        meter_forms = [self.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
        return f"{self.value} {format_plural_form(self.value, meter_forms)}\n"
        
    def __str__(self) -> str:
        return self.__format_value()
    
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
        if not isinstance(right, Meter | Real | NUMBER_TYPES):
            raise TypeError(Meter.__error(left, message))
        if not isinstance(left, Meter | Real | NUMBER_TYPES):
            raise TypeError(Real.__error(right, message))
    
    # ------------------- Operate ---------------------------
    
    @staticmethod
    def __operate(right: object, left: object, operator: operator) -> object:
        if isinstance(right, NUMBER_TYPES) and isinstance(left, Real):
            return operator(right, left.value)
        if isinstance(right, Real) and isinstance(left, NUMBER_TYPES):
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
        raise TypeError()
        raise TypeError(f"'{self.__class__.__name__}': Бинарная операция инверсии (~self) недоступна!")
    
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
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Meter":
        return Meter(round(self.value, n))
    
    
    def __format__(self, format_spec: str = str(), /) -> "Meter":
        raise TypeError(f"'{self.__class__.__name__}': Операция форматирования (format(self)) недоступна!")
    
    def __index__(self) -> "Meter":
        raise TypeError(f"'{self.__class__.__name__}': Операция индексирования (self[index]) недоступна!")
    
    
    
class KiloMeter(Meter):
    
    PREFIX_FORM = "кило"
    SHORT_FORM = "к" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    
class NanoMeter(Meter):
    
    PREFIX_FORM = "нано"
    SHORT_FORM = "н" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    
    
class DeciMeter(Meter):
    
    PREFIX_FORM = "деци"
    SHORT_FORM = "д" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM
    

class PikoMeter(Meter):
    
    PREFIX_FORM = "пико"
    SHORT_FORM = "п" + Meter.SHORT_FORM
    FULL_FORM = PREFIX_FORM + Meter.FULL_FORM