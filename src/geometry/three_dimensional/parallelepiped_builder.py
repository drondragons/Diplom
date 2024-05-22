from .parallelepiped import Parallelepiped, Cube

from .. import LINE_TYPES, REAL_TYPES
from ..one_dimensional import Line

from ...title import Title
from ...measurement import Length


__all__ = [
    "ParallelepipedBuilder",
    "CubeBuilder",
]


class ParallelepipedBuilder:
    
    def __init__(self) -> None:
        self.length = Line(title = "Длина")
        self.width = Line(title = "Ширина")
        self.height = Line(title = "Высота")
        self.title = Title(Parallelepiped.DEFAULT_TITLE)
        
    def add_length(self, value: LINE_TYPES) -> "ParallelepipedBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.length = Line(value, "Длина")
        return self
    
    def add_width(self, value: LINE_TYPES) -> "ParallelepipedBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.width = Line(value, "Ширина")
        return self
    
    def add_height(self, value: LINE_TYPES) -> "ParallelepipedBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.height = Line(value, "Высота")
        return self
    
    def add_title(self, value: str | Title) -> "ParallelepipedBuilder":
        self.title = value
        return self
    
    def build(self) -> Parallelepiped:
        return Parallelepiped(self.length, self.width, self.height, self.title)
    
    
class CubeBuilder:
    
    def __init__(self) -> None:
        self.side = Line(title = "Сторона")
        self.title = Title(Cube.DEFAULT_TITLE)
        
    def add_side(self, value: LINE_TYPES) -> "CubeBuilder":
        if isinstance(value, Line):
            value = value.length
        elif isinstance(value, Length):
            value = value
        elif isinstance(value, REAL_TYPES):
            value = Length(value)
        self.side = Line(value, "Сторона")
        return self
    
    def add_title(self, value: str | Title) -> "CubeBuilder":
        self.title = value
        return self
    
    def build(self) -> Cube:
        return Cube(self.side, self.title)