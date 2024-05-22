import operator

from ..one_dimensional import Line, LineValidator
from ..two_dimensional import Rectangle

from ... import _validate
from ...title import Title
from ...measurement import SquareConverter, VolumeConverter


__all__ = [
    "Parallelepiped",
    "Cube",
]


class Parallelepiped(Rectangle):
    
    __slots__ = [
        "__height",
    ]
    
    DEFAULT_TITLE = "Параллелепипед"
    
    @property
    def height(self) -> Line:
        return self.__height
    
    @height.setter
    def height(self, height: Line) -> None:
        s = f"\n\t{self.class_name}: "
        LineValidator._handle_exception(LineValidator.validate, s, height, 0)
        if height.title == Line.DEFAULT_TITLE:
            height.title = "Высота"
        self.__height = height
        
    @property
    def volume(self) -> str:
        volume = self.length.length * self.width.length * self.height.length
        return VolumeConverter.auto_convert(volume)
    
    @property
    def area(self) -> str:
        area = self.length.length * self.width.length
        area += (self.length.length * self.height.length)
        area += (self.width.length * self.height.length)
        return SquareConverter.auto_convert(2 * area)
    
    @property
    def perimeter(self) -> Line:
        perimeter = 4 * (self.length + self.width + self.height)
        perimeter.title = "Периметр"
        return perimeter
    
    def is_cube(self) -> bool:
        return self.length == self.width == self.height
    
    def __init__(
        self, 
        length: Line = Line(title = Title("Длина")),
        width: Line = Line(title = Title("Ширина")),
        height: Line = Line(title = Title("Высота")),
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
    
    def print_area(self) -> str:
        return f"Площадь поверхности:\t{self.area}"
    
    def print_volume(self) -> str:
        return f"Объём:\t{self.volume}"
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}\n\t{self.width}\n\t{self.height}"
        result += f"\n\t{self.print_volume()}"
        return result + f"\n\t{self.print_area()}\n\t{self.perimeter}\n"
    
    def __repr__(self) -> str:
        result = f"{self.class_name} (title: {self.title}, "
        return result + f"length: {self.length}, width: {self.width})"
        
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.width, self.height, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Parallelepiped, left, Parallelepiped, operator)
    
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return self.length != 0 and self.width != 0 and self.height != 0
        
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
    def side(self, side: Line) -> None:
        s = f"\n\t{self.class_name}: "
        LineValidator._handle_exception(LineValidator.validate, s, side, 0)
        if side.title == Line.DEFAULT_TITLE:
            side.title = "Сторона"
        self.__width = side
        self.__length = side
        self.__height = side
        
    @property
    def length(self) -> Line:
        return self.__length
    
    @length.setter
    def length(self, length: Line) -> None:
        self.side = length
        
    @property
    def width(self) -> Line:
        return self.__width
    
    @width.setter
    def width(self, width: Line) -> None:
        self.side = width
        
    @property
    def height(self) -> Line:
        return self.__height
        
    @height.setter
    def height(self, height: Line) -> None:
        self.side = height
        
    def __init__(
        self, 
        side: Line = Line(title = Title("Сторона")),
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