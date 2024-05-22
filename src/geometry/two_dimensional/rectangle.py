import operator

from ..one_dimensional import Line, LineValidator

from ... import _error, _validate
from ...title import Title
from ...measurement import SquareConverter, MeterConverter


__all__ = [
    "Rectangle",
    "Square",
]


class Rectangle:
    
    __slots__ = [
        "__width",
        "__length",
        "__title",
    ]
    
    DEFAULT_TITLE = "Прямоугольник"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def length(self) -> Line:
        return self.__length
    
    @length.setter
    def length(self, length: Line) -> None:
        s = f"\n\t{self.class_name}: "
        LineValidator._handle_exception(LineValidator.validate, s, length)
        if length.title == Line.DEFAULT_TITLE:
            length.title = "Длина"
        self.__length = length
        
    @property
    def width(self) -> Line:
        return self.__width
    
    @width.setter
    def width(self, width: Line) -> None:
        s = f"\n\t{self.class_name}: "
        LineValidator._handle_exception(LineValidator.validate, s, width)
        if width.title == Line.DEFAULT_TITLE:
            width.title = "Ширина"
        self.__width = width
        
    @property
    def title(self) -> Title:
        return self.__title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self.__title = Title(title)
        
    @property
    def area(self) -> str:
        square = self.width.length * self.length.length
        return SquareConverter.auto_convert(square)
    
    @property
    def perimeter(self) -> Line:
        perimeter = 2 * (self.length + self.width)
        perimeter.title = "Периметр"
        return perimeter
    
    def is_square(self) -> bool:
        return self.length == self.width
    
    def __init__(
        self, 
        length: Line = Line(title = Title("Длина")),
        width: Line = Line(title = Title("Ширина")),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.width = width
        self.length = length
        self.title = title
        
    # ------------------- Output ---------------------------
    
    def print_title(self) -> str:
        return "Квадрат" \
            if self.title == self.DEFAULT_TITLE and self.is_square() else \
                self.title
    
    def print_area(self) -> str:
        return f"Площадь:\t{self.area}"
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}\n\t{self.width}"
        return result + f"\n\t{self.print_area()}\n\t{self.perimeter}\n"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, length: {self.length}, width: {self.width})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.width, self.title))
    
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Rectangle, left, Rectangle, operator)
    
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return self.length != 0 and self.width != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Rectangle._validate(right, left, operator)
        return operator(right.length == left.length) and operator(right.width == left.width)
        
    def __eq__(self, other: object) -> bool:
        return Rectangle._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        return Rectangle._equality(self, other, operator.ne)
        
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __getattribute__(self, name: str) -> None:
        try:
            return super().__getattribute__(name)
        except AttributeError:
            pass
        message = f"Класс '{self.class_name}' не содержит атрибут {name}!"
        raise AttributeError(_error(self, message))
    
    
class Square(Rectangle):
    
    DEFAULT_TITLE = "Квадрат"
    
    @property
    def side(self) -> Line:
        return self.length
    
    @side.setter
    def side(self, side: Line) -> None:
        s = f"\n\t{self.class_name}: "
        LineValidator._handle_exception(LineValidator.validate, s, side)
        if side.title == Line.DEFAULT_TITLE:
            side.title = "Сторона"
        self.__width = side
        self.__length = side
        
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
        
    def __init__(
        self, 
        side: Line = Line(title = Title("Сторона")),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(side, side, title)
        
    # ------------------- Output ---------------------------
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.side}"
        return result + f"\n\t{self.print_area()}\n\t{self.perimeter}\n"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, side: {self.side})"