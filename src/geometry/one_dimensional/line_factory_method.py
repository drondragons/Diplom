import random
from types import NoneType
from typing import Type

from .line import Line

from .. import REAL_TYPES, DEFAULT_SIDE_TITLES

from ...validators import Validator
from ...measurement.length import Length, LengthFactoryMethod
from ...value_objects.title import Title
from ...factory_method import FactoryMethod


__all__ = [
    "LineFactoryMethod",
]


class LineFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = Length.DEFAULT_LENGTH_VALUE
    DEFAULT_MAXIMUM_VALUE = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = str()
    ) -> Line:
        s = f"\n\t{cls.__name__}.generate: "
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        generator = LengthFactoryMethod.generate
        length = generator(minimum, maximum, is_int, length_type)
        
        titles = [Line.DEFAULT_TITLE] + DEFAULT_SIDE_TITLES
        title = random.choice(titles) if not title else title
        
        return Line(length, Title(title))