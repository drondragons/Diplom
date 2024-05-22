from .line import Line

from .. import LENGTH_TYPES

from ...title import Title
from ...measurement import Length


__all__ = [
    "LineBuilder",
]


class LineBuilder:
    
    def __init__(self) -> None:
        self.length = Length()
        self.title = Title()
        
    def add_length(self, value: LENGTH_TYPES) -> "LineBuilder":
        self.length = value if isinstance(value, Length) else Length(value)
        return self
    
    def add_title(self, value: str | Title) -> "LineBuilder":
        self.title = value
        return self
    
    def build(self) -> Line:
        return Line(self.length, self.title)