from ..one_dimensional import Line, LineValidator

from ...title import Title, TitleValidator
from ...measurement import Length, Square, SquareConverter


__all__ = [
    "Rectangle",
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
        exception, message = LineValidator.validate(length)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__length = length
        
    @property
    def width(self) -> Line:
        return self.__width
    
    @width.setter
    def width(self, width: Line) -> None:
        exception, message = LineValidator.validate(width)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__width = width
        
    @property
    def title(self) -> Title:
        return self.__title
    
    @title.setter
    def title(self, title: Title) -> None:
        exception, message = TitleValidator.validate(title, False)
        if exception:
            raise exception(f"\n\t{self.class_name}: {message}")
        self.__title = title
        
    @property
    def square(self) -> str:
        width_type = type(self.width.length)
        length_type = type(self.length.length)
        # print(width_type, length_type)
        # print(type(self.width.length * self.length.length))
        if width_type == length_type:
            # print("+++++++++++++")
            square = width_type(self.width.length * self.length.length)
            # print(type(square))
            if width_type == Length:
                # print("&&&&&&&&&&&&")
                return Square.print_full_form(square)
            return SquareConverter.auto_convert(square)
                
        print(type(self.width.length), type(self.length.length))
        if type(self.width.length) == type(self.length.length):
            print(self.width * self.length)
    
    def __init__(
        self, 
        length: Line = Line(title = Title("Длина")),
        width: Line = Line(title = Title("Ширина")),
        title: Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.width = width
        self.length = length
        self.title = title
        
    # ------------------- Output ---------------------------
        
    def __str__(self) -> str:
        return f"{self.title}:\n\t{self.length}\n\t{self.width}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, length: {self.length}, width: {self.width})"