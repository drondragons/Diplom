import operator

from ..price import Price

from ... import _validate
from ...measurement.money import Money, MoneyValidator
from ...measurement.length import Length, LengthValidator, Meter, MeterConverter
from ...measurement.square import SquareConverter
from ...value_objects.title import Title
from ...geometry.one_dimensional import Line
from ...geometry.three_dimensional import Parallelepiped


__all__ = [
    "Building",
]


class Building(Parallelepiped):
    
    __slots__ = [
        "_indent",
        "_price_to_build"
    ]
    
    DEFAULT_TITLE = "Здание"
    
    DEFAULT_INDENT = Meter(5)
    DEFAULT_INCOME = Money(0)
    DEFAULT_PRICE_TO_BUILD = Money(1_000_000_000)
    
    MINIMUM_LENGTH = Meter(40)
    MINIMUM_WIDTH = Meter(40)
    MINIMUM_HEIGHT = Meter(20)
    
    @property
    def length(self) -> Line:
        return self._length
    
    @length.setter
    def length(self, length: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, length, 0)
        
        length = MeterConverter.convert(length, Meter)
        handler(LengthValidator.validate, s, length, self.MINIMUM_LENGTH.value)
        
        self._length = Line(length, "Длина")
        
    @property
    def width(self) -> Line:
        return self._width
    
    @width.setter
    def width(self, width: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, width, 0)
        
        width = MeterConverter.convert(width, Meter)
        handler(LengthValidator.validate, s, width, self.MINIMUM_WIDTH.value)
        
        self._width = Line(width, "Ширина")
    
    @property
    def height(self) -> Line:
        return self._height
    
    @height.setter
    def height(self, height: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, height, 0)
        
        height = MeterConverter.convert(height, Meter)
        handler(LengthValidator.validate, s, height, self.MINIMUM_HEIGHT.value)
        
        self._height = Line(height, "Высота")
    
    @property
    def indent(self) -> Line:
        return self._indent
    
    @indent.setter
    def indent(self, indent: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, indent, 0)
        
        self._indent = Line(indent, "Отступ")
        
    @property
    def price_to_build(self) -> Price:
        return self._price_to_build
    
    @price_to_build.setter
    def price_to_build(self, price_to_build: Money) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = MoneyValidator._handle_exception
        handler(MoneyValidator.validate, s, price_to_build, 0)
        
        self._price_to_build = Price(price_to_build, "Стоимость постройки")
        
    @property
    def area_with_indent(self) -> Length:
        indent_area = 2 * self.indent.length + self.length.length
        return indent_area * (2 * self.indent.length + self.width.length)
    
    @property
    def length_with_indent(self) -> Length:
        return self.length.length + self.indent.length * 2
    
    @property
    def width_with_indent(self) -> Length:
        return self.width.length + self.indent.length * 2
    
    def __init__(
        self, 
        length: Length = MINIMUM_LENGTH,
        width: Length = MINIMUM_WIDTH,
        height: Length = MINIMUM_HEIGHT,
        indent: Length = DEFAULT_INDENT,
        price_to_build: Money = DEFAULT_PRICE_TO_BUILD,
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(length, width, height, title)
        self.indent = indent
        self.price_to_build = price_to_build
        
    # ------------------- Output ---------------------------
    
    def print_area_with_indent(self) -> str:
        return f"Площадь основания с отступами:\t{SquareConverter.auto_convert(self.area_with_indent)}"
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}\n\t{self.width}\n\t{self.height}"
        result += f"\n\t{self.print_volume()}\n\t{self.print_area()}"
        result += f"\n\t{self.print_area_with_indent()}"
        return result + f"\n\t{self.indent}\n\t{self.price_to_build}\n"
    
    def __repr__(self) -> str:
        result = f"{self.class_name} (title: {self.title}, "
        result += f"length: {self.length}, width: {self.width}, "
        result += f"height: {self.height}, indent: {self.indent}, "
        return result + f"price_to_build: {self.price_to_build})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.width, 
                     self.height, self.title, self.indent, self.price_to_build))
        
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Building, left, Building, operator)
        
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return super().__bool__() and self.indent != 0 and self.price_to_build != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Building._validate(right, left, operator)
        return operator(right.length, left.length) and operator(right.width, left.width) and \
            operator(right.height, left.height) and operator(right.indent, left.indent) and \
            operator(right.price_to_build, left.price_to_build)
        
    def __eq__(self, other: object) -> bool:
        return Building._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        Building._validate(self, other, operator.ne)
        return not Building._equality(self, other, operator.eq)