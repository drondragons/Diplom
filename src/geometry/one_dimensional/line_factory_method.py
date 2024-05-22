import random
from types import NoneType
from typing import Type

from .line import Line

from .. import REAL_TYPES, DEFAULT_SIDE_TITLES

from ...title import Title
from ...validators import Validator
from ...measurement import Length, LengthFactoryMethod
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
        length = LengthFactoryMethod.generate(minimum, maximum, is_int, length_type)
        Validator._handle_exception(Validator.validate_object_type, s, title, str | Title)
        title = random.choice([Line.DEFAULT_TITLE] + DEFAULT_SIDE_TITLES) if not title else title
        return Line(length, Title(title))