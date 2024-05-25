from types import NoneType
from typing import Type

from .parallelepiped import Parallelepiped, Cube

from .. import REAL_TYPES

from ...validators import Validator
from ...measurement.length import Length, LengthFactoryMethod
from ...value_objects.title import Title
from ...factory_method import FactoryMethod


__all__ = [
    "ParallelepipedFactoryMethod",
    "CubeFactoryMethod",
]


class ParallelepipedFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = Length.DEFAULT_LENGTH_VALUE
    DEFAULT_MAXIMUM_VALUE = FactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Parallelepiped.DEFAULT_TITLE
    ) -> Parallelepiped:
        s = f"\n\t{cls.__name__}.generate: "
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        generator = LengthFactoryMethod.generate
        width = generator(minimum, maximum, is_int, length_type)
        length = generator(minimum, maximum, is_int, length_type)
        height = generator(minimum, maximum, is_int, length_type)
        
        return Parallelepiped(length, width, height, title)
    

class CubeFactoryMethod(FactoryMethod):
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = ParallelepipedFactoryMethod.DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = ParallelepipedFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Cube.DEFAULT_TITLE
    ) -> Cube:
        s = f"\n\t{cls.__name__}.generate: "
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
        generator = LengthFactoryMethod.generate
        side = generator(minimum, maximum, is_int, length_type)
        
        return Cube(side, title)