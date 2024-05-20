import random

from .money import *
from .ruble import *
from .dollar import *
from .euro import *
from .yuan import *
from .pound import *

from .. import REAL_TYPES

from ...real import RealFactoryMethod
from ...validators import Validator


__all__ = [
    "MoneyFactoryMethod",
    "RubleFactoryMethod",
    "DollarFactoryMethod",
    "EuroFactoryMethod",
    "YuanFactoryMethod",
    "PoundFactoryMethod",
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
        money_type: type = None
    ) -> Money:
        minimum = Money(minimum)
        maximum = Money(maximum)
        
        exception, message = Validator.validate_object_type(is_int, bool)
        if exception:
            message = f"Недопустимый тип '{type(is_int).__name__}'! Ожидался тип bool!"
            raise TypeError(f"\n\t{cls.__name__}.generate: " + message)
        
        if not isinstance(money_type, type) and money_type != None:
            message = f"Ожидался тип, а не объект {money_type.__class__.__name__}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        money_types = [Money] + [subclass for subclass in Money.__subclasses__()]
        if money_type not in (money_types + [None]):
            message = f"Недопустимый тип '{money_type.__name__}'! Ожидался тип {Validator.format_union_types(money_types)}!"
            raise TypeError(f"\n\t{cls.__name__}.generate: " + message)
        
        money_type = random.choice(money_types) if not money_type else money_type
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
    

class PoundFactoryMethod(MoneyFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Pound:
        return super().generate(minimum, maximum, is_int, Pound)