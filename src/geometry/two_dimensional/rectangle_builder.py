from .rectangle import Rectangle, Square

from .. import LENGTH_TYPES, REAL_TYPES

from ...measurement import Length
from ...value_objects import Title


__all__ = [
    "RectangleBuilder",
    "SquareBuilder",
]


class RectangleBuilder:
    
    def __init__(self) -> None:
        self.width = Length()
        self.length = Length()
        self.title = Title(Rectangle.DEFAULT_TITLE)
        
    def add_length(self, value: LENGTH_TYPES) -> "RectangleBuilder":
        self.length = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_width(self, value: LENGTH_TYPES) -> "RectangleBuilder":
        self.width = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_title(self, value: str | Title) -> "RectangleBuilder":
        self.title = value
        return self
    
    def build(self) -> Rectangle:
        return Rectangle(self.length, self.width, self.title)
    
    
class SquareBuilder:
    
    def __init__(self) -> None:
        self.side = Length()
        self.title = Title(Square.DEFAULT_TITLE)
        
    def add_side(self, value: Length) -> "SquareBuilder":
        self.side = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_title(self, value: str | Title) -> "SquareBuilder":
        self.title = value
        return self
    
    def build(self) -> Square:
        return Square(self.side, self.title)