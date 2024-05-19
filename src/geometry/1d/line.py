import math
import operator
from typing import Tuple

from ...measurement import REAL_TYPES
from ...measurement import Length

from ...validators import StringValidator


__all__ = [
    "Line"
]


class Line:
    
    __slots__ = [
        "__value",
        "__title",
    ]
    
    DEFAULT_VALUE = 0
    DEFAULT_TITLE = "Отрезок"
    
    @property
    def value(self) -> Length:
        return self.__value
    
    @value.setter
    def value(self, value: Length) -> None:
        self.__value = value
        
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, title: str) -> None:
        exception, message = StringValidator.validate(title, False)