from types import NoneType
from typing import Type

from .parallelepiped import Parallelepiped, Cube

from .. import REAL_TYPES
from ..one_dimensional import LineFactoryMethod

from ...title import Title
from ...validators import Validator
from ...measurement import Length
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
        width = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Ширина")
        length = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Длина")
        height = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Высота")
        Validator._handle_exception(Validator.validate_object_type, s, title, str | Title)
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
        side = LineFactoryMethod.generate(minimum, maximum, is_int, length_type, "Сторона")
        Validator._handle_exception(Validator.validate_object_type, s, title, str | Title)
        return Cube(side, title)