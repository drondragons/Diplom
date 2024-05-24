import random
from types import NoneType
from typing import Type

from .price import Price

from ... import REAL_TYPES

from ...validators import Validator
from ...measurement import Money, MoneyFactoryMethod
from ...value_objects import Title
from ...factory_method import FactoryMethod


__all__ = [
    "PriceFactoryMethod",
]


class PriceFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = Money.DEFAULT_MONEY_VALUE
    DEFAULT_MAXIMUM_VALUE = MoneyFactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        money_type: Type = NoneType,
        title: str | Title = str()
    ) -> Price:
        s = f"\n\t{cls.__name__}.generate: "
        
        generator = MoneyFactoryMethod.generate
        money = generator(minimum, maximum, is_int, money_type)
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        return Price(money, Title(title))