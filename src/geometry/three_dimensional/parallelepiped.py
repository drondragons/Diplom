import operator

from ..one_dimensional import Line
from ..two_dimensional import Rectangle

from ... import _validate
from ...measurement.square import SquareConverter
from ...measurement.volume import VolumeConverter
from ...measurement.length import Length, LengthValidator
from ...value_objects.title import Title


__all__ = [
    "Parallelepiped",
    "Cube",
]


class Parallelepiped(Rectangle):
    
    __slots__ = [
        "_height",
    ]
    
    DEFAULT_TITLE = "Параллелепипед"
    
    @property
    def height(self) -> Line:
        return self._height
    
    @height.setter
    def height(self, height: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, height, 0)
        
        self._height = Line(height, "Высота")
        
    @property
    def volume(self) -> Length:
        return self.length.length * self.width.length * self.height.length
    
    @property
    def area_surface(self) -> Length:
        area = self.length.length * self.width.length
        area += (self.length.length * self.height.length)
        area += (self.width.length * self.height.length)
        return 2 * area
    
    @property
    def perimeter(self) -> Line:
        perimeter = 4 * (self.length.length + self.width.length + self.height.length)
        return Line(perimeter, "Периметр")
    
    def is_cube(self) -> bool:
        return self.length == self.width == self.height
    
    def __init__(
        self, 
        length: Length = Length(),
        width: Length = Length(),
        height: Length = Length(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.width = width
        self.length = length
        self.height = height
        self.title = title
        
    # ------------------- Output ---------------------------
    
    def print_title(self) -> str:
        return "Куб" \
            if self.title == self.DEFAULT_TITLE and self.is_cube() else \
                self.title
    
    def print_area_surface(self) -> str:
        return f"Площадь поверхности:\t{SquareConverter.auto_convert(self.area_surface)}"
    
    def print_area(self) -> str:
        return f"Площадь основания:\t{SquareConverter.auto_convert(self.area)}"
    
    def print_volume(self) -> str:
        return f"Объём:\t{VolumeConverter.auto_convert(self.volume)}"
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}\n\t{self.width}\n\t{self.height}"
        result += f"\n\t{self.print_volume()}\n\t{self.print_area()}"
        return result + f"\n\t{self.print_area_surface()}\n\t{self.perimeter}\n"
    
    def __repr__(self) -> str:
        result = f"{self.class_name} (title: {self.title}, "
        result += f"length: {self.length}, width: {self.width}, "
        return result + f"height: {self.height})"
        
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.width, self.height, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Parallelepiped, left, Parallelepiped, operator)
    
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return super().__bool__() and self.height != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Parallelepiped._validate(right, left, operator)
        return operator(right.length, left.length) and operator(right.width, left.width) and \
            operator(right.height, left.height)
        
    def __eq__(self, other: object) -> bool:
        return Parallelepiped._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Parallelepiped._equality(self, other, operator.ne)
    
    
class Cube(Parallelepiped):
    
    DEFAULT_TITLE = "Куб"
    
    @property
    def side(self) -> Line:
        return self.length
    
    @side.setter
    def side(self, side: Length) -> None:
        s = f"\n\t{self.class_name}: "
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, side, 0)
        self._width = Line(side, "Сторона")
        self._length = Line(side, "Сторона")
        self._height = Line(side, "Сторона")
        
    @property
    def length(self) -> Line:
        return self._length
    
    @length.setter
    def length(self, length: Length) -> None:
        self.side = length
        
    @property
    def width(self) -> Line:
        return self._width
    
    @width.setter
    def width(self, width: Length) -> None:
        self.side = width
        
    @property
    def height(self) -> Line:
        return self._height
        
    @height.setter
    def height(self, height: Length) -> None:
        self.side = height
        
    def __init__(
        self, 
        side: Length = Length(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(side, side, side, title)
        
    # ------------------- Output ---------------------------
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}"
        result += f"\n\t{self.print_volume()}"
        return result + f"\n\t{self.print_area()}\n\t{self.perimeter}\n"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, side: {self.side})"