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
    
    DEFAULT_MINIMUM_VALUE = Money.DEFAULT_MONEY_VALUE
    DEFAULT_MAXIMUM_VALUE = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        money_type: type = Money
    ) -> Money:
        minimum = Money(minimum)
        maximum = Money(maximum)
        
        exception, message = Validator.validate_type(is_int, bool)
        if exception:
            message = f"Недопустимый тип '{type(is_int).__name__}'! Ожидался тип bool!"
            raise TypeError(f"\n\t{cls.__name__}.generate: " + message)
        
        if money_type not in MONEY_CLASSES:
            message = f"Недопустимый тип '{type(money_type).__name__}'! Ожидался тип {Validator.format_union_types(money_type)}!"
            raise TypeError(f"\n\t{cls.__name__}.generate: " + message)
        
        return money_type(super().generate(minimum.value, maximum.value, is_int))
    
    
class RubleFactoryMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Ruble:
        return super().generate(minimum, maximum, is_int, Ruble)
    
    
class DollarFactoryMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Dollar:
        return super().generate(minimum, maximum, is_int, Dollar)
    
    
class EuroFactoryMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Euro:
        return super().generate(minimum, maximum, is_int, Euro)
    
    
class YuanFactoryMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Yuan:
        return super().generate(minimum, maximum, is_int, Yuan)