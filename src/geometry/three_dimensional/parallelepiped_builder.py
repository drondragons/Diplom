from .parallelepiped import Parallelepiped, Cube

from .. import LENGTH_TYPES, REAL_TYPES

from ...measurement.length import Length
from ...value_objects.title import Title


__all__ = [
    "ParallelepipedBuilder",
    "CubeBuilder",
]


class ParallelepipedBuilder:
    
    def __init__(self) -> None:
        self.length = Length()
        self.width = Length()
        self.height = Length()
        self.title = Title(Parallelepiped.DEFAULT_TITLE)
        
    def add_length(self, value: LENGTH_TYPES) -> "ParallelepipedBuilder":
        self.length = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_width(self, value: LENGTH_TYPES) -> "ParallelepipedBuilder":
        self.width = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_height(self, value: LENGTH_TYPES) -> "ParallelepipedBuilder":
        self.height = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_title(self, value: str | Title) -> "ParallelepipedBuilder":
        self.title = value
        return self
    
    def build(self) -> Parallelepiped:
        return Parallelepiped(self.length, self.width, self.height, self.title)
    
    
class CubeBuilder:
    
    def __init__(self) -> None:
        self.side = Length()
        self.title = Title(Cube.DEFAULT_TITLE)
        
    def add_side(self, value: LENGTH_TYPES) -> "CubeBuilder":
        self.side = Length(value) if isinstance(value, REAL_TYPES) else value
        return self
    
    def add_title(self, value: str | Title) -> "CubeBuilder":
        self.title = value
        return self
    
    def build(self) -> Cube:
        return Cube(self.side, self.title)