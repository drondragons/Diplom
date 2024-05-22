import random
from types import NoneType
from typing import Type

from .money import *
from .ruble import *
from .dollar import *
from .euro import *
from .yuan import *
from .pound import *

from .. import REAL_TYPES

from ...real import Real, RealFactoryMethod, RealValidator
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
        money_type: Type = NoneType
    ) -> Money:
        s = f"\n\t{cls.__name__}.generate: "
        
        Validator._handle_exception(Validator.validate_object_type, s, minimum, REAL_TYPES)
        Validator._handle_exception(RealValidator.validate_interval, s, Real(minimum), 0)
        Validator._handle_exception(Validator.validate_object_type, s, maximum, REAL_TYPES)
        Validator._handle_exception(Validator.validate_object_type, s, is_int, bool)
        
        subclasses = [Money] + [subclass for subclass in Money.__subclasses__()]
        money_types = [NoneType] + subclasses
        Validator._handle_exception(Validator.validate_type_of_type, s, money_type, money_types)
        
        money_type = random.choice(subclasses) if money_type == NoneType else money_type
        return money_type(super().generate(minimum, maximum, is_int))
    
    
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