from ...geometry.two_dimensional import Rectangle
from ...measurement.length import Length
from ...value_objects.title import Title


__all__ = [
    "Surface",
]


class Surface(Rectangle):
    
    DEFAULT_TITLE = "Прямоугольная плоскость под застройку"
    
    def __init__(
        self, 
        length: Length = Length(),
        width: Length = Length(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(length, width, title)
    
    # ------------------- Output ---------------------------
    
    def print_title(self) -> str:
        return "Квадратная плоскость под застройку" \
            if self.title == self.DEFAULT_TITLE and self.is_square() else \
                self.title