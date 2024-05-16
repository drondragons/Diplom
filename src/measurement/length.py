from ..validators.constants import NUMBER_TYPES
from .. import format_number, format_plural_form
from ..validators.number_validator import NumberValidator
from .constants import DEFAULT_LENGTH_VALUE, DEFAULT_PLURAL_FORM

__all__ = [
    "Meter",
]

class Meter:
    
    SHORT_FORM = "м"
    FULL_FORM = "метр"
    PREFIX_METER = str()
    
    @property
    def value(self) -> NUMBER_TYPES:
        return self._value
    
    @value.setter
    def value(self, value: object) -> None:
        exception, message = NumberValidator.validate(value, NUMBER_TYPES, 0)
        if exception:
            raise exception(f"'{self.__class__.__name__}': " + message)
        self._value = value
        
    def __init__(self, value: object = DEFAULT_LENGTH_VALUE) -> None:
        self.value = value
        
    def __format_value(self) -> str:
        meter_forms = [self.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
        return f"{format_number(self.value)} {format_plural_form(self.value, meter_forms)}"
        
    def __str__(self) -> str:
        return f"{self.__format_value()}\n"
    
    
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