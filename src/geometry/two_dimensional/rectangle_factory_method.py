from types import NoneType
from typing import Type

from .. import REAL_TYPES
from ..two_dimensional import Rectangle, Square

from ...validators import Validator
from ...measurement import Length, LengthFactoryMethod
from ...value_objects import Title
from ...factory_method import FactoryMethod


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
        
        generator = LengthFactoryMethod.generate
        width = generator(minimum, maximum, is_int, length_type)
        length = generator(minimum, maximum, is_int, length_type)
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        return Rectangle(length, width, title)
        

class SquareFactoryMethod(FactoryMethod):
    
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
        
        generator = LengthFactoryMethod.generate
        side = generator(minimum, maximum, is_int, length_type)
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        return Square(side, title)