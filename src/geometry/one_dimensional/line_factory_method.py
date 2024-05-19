import random

from .line import Line

from .. import REAL_TYPES, DEFAULT_SIDE_TITLES

from ...title import Title
from ...factory_method import FactoryMethod
from ...measurement import METER_CLASSES
from ...measurement.length import Length, LengthFactoryMethod


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
        length_type: type = None,
        title: str = None
    ) -> Line:
        length_type = random.choice([Length] + METER_CLASSES) if not length_type else length_type
        length = LengthFactoryMethod.generate(minimum, maximum, is_int, length_type)
        title = random.choice([Line.DEFAULT_TITLE] + DEFAULT_SIDE_TITLES) if not title else title
        return Line(length, Title(title))