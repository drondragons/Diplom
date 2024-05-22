from types import NoneType
from typing import Type

from .. import REAL_TYPES
from ..one_dimensional import LineFactoryMethod
from ..two_dimensional import Rectangle, Square

from ...title import Title
from ...validators import Validator
from ...measurement import Length
from ...factory_method import FactoryMethod

from ...measurement import Meter


__all__ = [
    "RectangleFactoryMethod",
    "SquareFactoryMethod",
]


class RectangleFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = Length.DEFAULT_LENGTH_VALUE
    DEFAULT_MAXIMUM_VALUE = FactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Rectangle.DEFAULT_TITLE
    ) -> Rectangle:
        s = f"\n\t{cls.__name__}.generate: "
        width = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Ширина")
        length = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Длина")
        Validator._handle_exception(Validator.validate_object_type, s, title, str | Title)
        return Rectangle(length, width, title)
        

class SquareFactoryMethod(RectangleFactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = RectangleFactoryMethod.DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = RectangleFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Square.DEFAULT_TITLE
    ) -> Square:
        s = f"\n\t{cls.__name__}.generate: "
        side = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Сторона")
        Validator._handle_exception(Validator.validate_object_type, s, title, str | Title)
        return Square(side, title)