import operator
from typing import Tuple

from ..one_dimensional import Line

from ... import _error, _validate, _type_error
from ...constants import OPERATORS
from ...measurement.length import Length, LengthValidator
from ...measurement.square import SquareConverter
from ...value_objects.title import Title


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
    def area(self) -> Length:
        return self.width.length * self.length.length
    
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
        return f"Площадь:\t{SquareConverter.auto_convert(self.area)}"
    
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
    
    # ------------------- Unary operators ---------------------------
    
    def __pos__(self) -> "Rectangle":
        message = f"Операция {OPERATORS[operator.add]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    def __neg__(self) -> "Rectangle":
        message = f"Операция {OPERATORS[operator.sub]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __abs__(self) -> "Rectangle":
        message = f"Операция abs({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    def __inv__(self) -> "Rectangle":
        return ~self
    def __invert__(self) -> "Rectangle":
        message = f"Операция {OPERATORS[operator.inv]}{self.class_name} недоступна!"
        raise TypeError(_error(self, message))
    
    def __floor__(self) -> "Rectangle":
        message = f"Операция math.floor({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __ceil__(self) -> "Rectangle":
        message = f"Операция math.ceil({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __trunc__(self) -> "Rectangle":
        message = f"Операция math.trunc({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    def __int__(self) -> int:
        message = f"Операция int({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    def __float__(self) -> float:
        message = f"Операция float({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
    # ------------------- Binary operators ---------------------------
    
    def __round__(self, n: int = 0) -> "Rectangle":
        message = f"Операция round({self.class_name}) недоступна!"
        raise TypeError(_error(self, message))
    
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
    
    def __lt__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.lt)))
    def __le__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.le)))
    
    def __gt__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.gt)))
    def __ge__(self, other: object) -> bool:
        raise TypeError(_error(self, _type_error(self, other, operator.ge)))
    
    # ------------------- Mathematical operators ---------------------------
    
    def __add__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.add)))
    def __radd__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.add)))
    def __iadd__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.iadd)))
    
    def __sub__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.sub)))
    def __rsub__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.sub)))
    def __isub__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.isub)))
    
    def __mul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.mul)))
    def __rmul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.mul)))
    def __imul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.imul)))
    
    def __pow__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.pow)))
    def __rpow__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.pow)))
    def __ipow__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.ipow)))
    
    def __truediv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.truediv)))
    def __rtruediv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.truediv)))
    def __itruediv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.itruediv)))
    
    def __floordiv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.floordiv)))
    def __rfloordiv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.floordiv)))
    def __ifloordiv__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.ifloordiv)))
    
    def __mod__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.mod)))
    def __rmod__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.mod)))
    def __imod__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.imod)))
    
    def __divmod__(self, other: object) -> Tuple["Rectangle", "Rectangle"]:
        message = f"Операция divmod недоступна!"
        raise TypeError(_error(self, message))
    def __rdivmod__(self, other: object) -> Tuple["Rectangle", "Rectangle"]:
        message = f"Операция divmod недоступна!"
        raise TypeError(_error(self, message))
    
    def __matmul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.matmul)))
    def __rmatmul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.matmul)))
    def __imatmul__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.imatmul)))
        
    def __rshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.rshift)))
    def __rrshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.rshift)))
    def __irshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.irshift)))
    
    def __lshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.lshift)))
    def __rlshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.lshift)))
    def __ilshift__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.ilshift)))
        
    def __or__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.or_)))
    def __ror__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.or_)))
    def __ior__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.ior)))
        
    def __and__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.and_)))
    def __rand__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.and_)))
    def __iand__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.iand)))
        
    def __xor__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.xor)))
    def __rxor__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(other, self, operator.xor)))
    def __ixor__(self, other: object) -> "Rectangle":
        raise TypeError(_error(self, _type_error(self, other, operator.ixor)))
        
    # ------------------- Other magic methods ---------------------------
    
    def __format__(self, format_spec: str = str(), /) -> str:
        return self.__str__()
    
    def __index__(self) -> "Rectangle":
        message = f"Операция индексирования (Iterable[{self.class_name}]) недоступна!"
        raise TypeError(_error(self, message))
    
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