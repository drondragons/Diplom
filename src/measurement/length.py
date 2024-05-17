import sys
import math
from ..validators.constants import NUMBER_TYPES
from .. import format_number, format_plural_form
from ..validators.number_validator import NumberValidator
from .constants import DEFAULT_LENGTH_VALUE, DEFAULT_PLURAL_FORM

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
    def value(self) -> NUMBER_TYPES:
        return self.__value
    
    @value.setter
    def value(self, value: object) -> None:
        exception, message = NumberValidator.validate(value, NUMBER_TYPES, 0)
        if exception:
            raise exception(f"'{self.__class__.__name__}': " + message)
        self.__value = value
        
    def __init__(self, value: object = DEFAULT_LENGTH_VALUE) -> None:
        self.value = value
        
    def __format_value(self) -> str:
        meter_forms = [self.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
        return f"{format_number(self.value)} {format_plural_form(self.value, meter_forms)}\n"
        
    def __str__(self) -> str:
        return self.__format_value()
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (value: {self.value})"
    
    def __hash__(self) -> int:
        return hash(self.value)
    
    def __format__(self, format_spec: str = str(), /) -> "Meter":
        raise TypeError(f"'{self.__class__.__name__}': Операция форматирования (format(self)) недоступна!")
    
    def __index__(self) -> "Meter":
        raise TypeError(f"'{self.__class__.__name__}': Операция индексирования (self[index]) недоступна!")
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Meter":
        return self
    def __neg__(self) -> "Meter":
        raise TypeError(f"'{self.__class__.__name__}': Бинарная операция отрицания (-self) недоступна!")
    
    def __abs__(self) -> "Meter":
        return self
    
    def __invert__(self) -> "Meter":
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
    
    # def __sizeof__(self) -> int:
    #     return 
        # return sys.getsizeof(object()) + sys.getsizeof(self.value)
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Meter":
        return Meter(round(self.value, n))
    
    
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