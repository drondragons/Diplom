import operator

from ..one_dimensional import Line

from ... import _error, _validate
from ...measurement import SquareConverter, Length, LengthValidator
from ...value_objects import Title


__all__ = [
    "Rectangle",
    "Square",
]


class Rectangle:
    
    __slots__ = [
        "_width",
        "_length",
        "_title",
    ]
    
    DEFAULT_TITLE = "Прямоугольник"
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def length(self) -> Line:
        return self._length
    
    @length.setter
    def length(self, length: Length) -> None:
        s = f"\n\t{self.class_name}: "
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, length, 0)
        self._length = Line(length, "Длина")
        
    @property
    def width(self) -> Line:
        return self._width
    
    @width.setter
    def width(self, width: Length) -> None:
        s = f"\n\t{self.class_name}: "
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, width, 0)
        self._width = Line(width, "Ширина")
        
    @property
    def title(self) -> Title:
        return self._title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self._title = Title(title)
        
    @property
    def area(self) -> str:
        square = self.width.length * self.length.length
        return SquareConverter.auto_convert(square)
    
    @property
    def perimeter(self) -> Line:
        perimeter = 2 * (self.length.length + self.width.length)
        return Line(perimeter, "Периметр")
    
    def is_square(self) -> bool:
        return self.length == self.width
    
    def __init__(
        self, 
        length: Length = Length(),
        width: Length = Length(),
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
        result = f"{self.class_name} (title: {self.title}, "
        return result + f"length: {self.length}, width: {self.width})"
    
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
        return operator(right.length, left.length) and operator(right.width, left.width)
        
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
        return self._length
    
    @side.setter
    def side(self, side: Length) -> None:
        s = f"\n\t{self.class_name}: "
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, side, 0)
        self._width = Line(side, "Сторона")
        self._length = Line(side, "Сторона")
    
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
     
    def __init__(
        self, 
        side: Length = Length(),
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