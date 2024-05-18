from .meter import Meter
from .meter import METER_CLASSES
from .meter_validator import MeterValidator

from .constants import REAL_TYPES
from ...real import Real, RealFactoryMethod

from ...validators import Validator
from ...validators import NUMBER_TYPES


__all__ = [
    "MeterFactoryMethod",
]


class MeterFactoryMethod(RealFactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = 0
    
    @classmethod
    def generate(
        cls,
        minimum: Meter | REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: Meter | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        meter_type: type = Meter
    ) -> Meter:
        minimum = Meter(minimum)
        maximum = Meter(maximum)
        
        if meter_type not in METER_CLASSES:
            message = f"Недопустимый тип '{meter_type.__name__}'! Ожидался тип {Validator.format_union_types(meter_type)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        return meter_type(super().generate(minimum.value, maximum.value, is_int))