from typing import List

from ..buildings import Building

from ...geometry.two_dimensional import Rectangle
from ...measurement.length import Length, Meter
from ...validators import ListValidator
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
    
    def validate_placement_buildings(self, buildings: List[Building]) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = ListValidator._handle_exception
        handler(ListValidator.validate, s, buildings, Building)
        
        for building in buildings:
            side = min(self.width, self.length)
            message = "\n\tSurface.validate_placement_buildings:\tОбъект "
            if side < building.width_with_indent:
                message += f"«{building.title}» невозможно расположить из-за ширины "
                message += f"({side.length} < {building.width_with_indent}), "
                message += f"большей чем может вместить {self.title.lower()}!"
                raise ValueError(message)
            if side < building.length_with_indent:
                message += f"«{building.title}» невозможно расположить из-за длины "
                message += f"({side.length} < {building.length_with_indent}), "
                message += f"большей чем может вместить {self.title.lower()}!"
                raise ValueError(message)
    
    # ------------------- Output ---------------------------
    
    def print_title(self) -> str:
        return "Квадратная плоскость под застройку" \
            if self.title == self.DEFAULT_TITLE and self.is_square() else \
                self.title