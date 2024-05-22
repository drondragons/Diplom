from .rectangle import Rectangle, Square

from .. import LINE_TYPES, REAL_TYPES
from ..one_dimensional import Line

from ...title import Title
from ...measurement import Length


__all__ = [
    "RectangleBuilder",
    "SquareBuilder",
]


class RectangleBuilder:
    
    def __init__(self) -> None:
        self.length = Line(title = "Длина")
        self.width = Line(title = "Ширина")
        self.title = Title(Rectangle.DEFAULT_TITLE)
        
    def add_length(self, value: LINE_TYPES) -> "RectangleBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.length = Line(value, "Длина")
        return self
    
    def add_width(self, value: LINE_TYPES) -> "RectangleBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.width = Line(value, "Ширина")
        return self
    
    def add_title(self, value: str | Title) -> "RectangleBuilder":
        self.title = value
        return self
    
    def build(self) -> Rectangle:
        return Rectangle(self.length, self.width, self.title)
    
    
class SquareBuilder:
    
    def __init__(self) -> None:
        self.side = Line(title = "Сторона")
        self.title = Title(Square.DEFAULT_TITLE)
        
    def add_side(self, value: LINE_TYPES) -> "SquareBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.side = Line(value, "Сторона")
        return self
    
    def add_title(self, value: str | Title) -> "SquareBuilder":
        self.title = value
        return self
    
    def build(self) -> Square:
        return Square(self.side, self.title)