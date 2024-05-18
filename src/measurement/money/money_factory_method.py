from .money import *
from .money import MONEY_CLASSES

from .. import REAL_TYPES

from ...real import RealFactoryMethod

from ...validators import Validator


__all__ = [
    "MoneyFactoryMethod",
    "RubleFactoryMethod",
    "DollarFactoryMethod",
    "EuroFactoryMethod",
    "YuanFactoryMethod",
]


class MoneyFactoryMethod(RealFactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = 0
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        money_type: type = Money
    ) -> Money:
        minimum = Money(minimum)
        maximum = Money(maximum)
        
        if money_type not in MONEY_CLASSES:
            message = f"Недопустимый тип '{money_type.__name__}'! Ожидался тип {Validator.format_union_types(money_type)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        return money_type(super().generate(minimum.value, maximum.value, is_int))
    
    
class RubleFactorMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Ruble:
        return super().generate(minimum, maximum, is_int, Ruble)
    
    
class DollarFactorMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Dollar:
        return super().generate(minimum, maximum, is_int, Dollar)
    
    
class EuroFactorMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Euro:
        return super().generate(minimum, maximum, is_int, Euro)
    
    
class YuanFactorMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: Money | REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Money | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Yuan:
        return super().generate(minimum, maximum, is_int, Yuan)