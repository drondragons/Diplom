from .money import Money
from .money import MONEY_CLASSES

from .. import REAL_TYPES

from ...real import RealFactoryMethod

from ...validators import Validator


__all__ = [
    "MoneyFactoryMethod",
]


class MoneyFactoryMethod(RealFactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = 0
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        meter_type: type = Money
    ) -> Money:
        minimum = Money(minimum)
        maximum = Money(maximum)
        
        if meter_type not in MONEY_CLASSES:
            message = f"Недопустимый тип '{meter_type.__name__}'! Ожидался тип {Validator.format_union_types(meter_type)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        return meter_type(super().generate(minimum.value, maximum.value, is_int))