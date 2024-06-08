import operator
from typing import List

from .building import Building

from ..flat import Pavilion, PavilionFactoryMethod
from ..price import Price

from ... import _get_year_form, _validate
from ...geometry.one_dimensional import Line
from ...measurement.length import Meter, Length, LengthValidator, MeterConverter
from ...measurement.money import Money, Ruble, MoneyValidator
from ...validators import ListValidator
from ...value_objects.title import Title
from ...value_objects.real import RealValidator


__all__ = [
    "Shop",
]


class Shop(Building):
    
    __slots__ = [
        "_floor_height",
        "_pavilions",
        "_income_cache",
        "_profit_cache",
    ]
    
    DEFAULT_TITLE = "Торговый центр"
    
    YEARS = 10
    PERCENTAGE = 0.8
    MINIMUM_LENGTH = Meter(50)
    MINIMUM_WIDTH = Meter(50)
    MINIMUM_HEIGHT = Meter(10)
    MINIMUM_FLOOR_HEIGHT = Meter(2.5)
    MAXIMUM_FLOOR_HEIGHT = Meter(2.7)
    DEFAULT_MAXIMUM_FLAT_FOOTAGE = Meter(200)
    
    @property
    def floor_height(self) -> Line:
        return self._floor_height
    
    @floor_height.setter
    def floor_height(self, floor_height: Length) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = LengthValidator._handle_exception
        handler(LengthValidator.validate, s, floor_height, 0)
        
        minimum = self.MINIMUM_FLOOR_HEIGHT.value
        maximum = self.MAXIMUM_FLOOR_HEIGHT.value
        floor_height = MeterConverter.convert(floor_height, Meter)
        handler(LengthValidator.validate, s, floor_height, minimum, maximum)
        
        self._floor_height = Line(floor_height, "Высота этажа")
    
    @property
    def shop_area(self) -> Length:
        return self.floors * self.area * self.PERCENTAGE
        
    @property
    def minimum_pavilions_amount(self) -> int:
        return int(self.shop_area / self.DEFAULT_MAXIMUM_FLAT_FOOTAGE)
    
    @property
    def maximum_pavilions_amount(self) -> int:
        return int(self.shop_area / Pavilion.MINIMUM_FOOTAGE)
        
    @property
    def floors(self) -> int:
        return int((self.height.length - self.floor_height.length) / self.floor_height.length)
    
    def _invalidate_caches(self):
        self._income_cache = None
        self._profit_cache = None
    
    @property
    def pavilions(self) -> List[Pavilion]:
        return self._pavilions
    
    @pavilions.setter
    def pavilions(self, pavilions: List[Pavilion]) -> None:
        s = f"\n\t{self.class_name}: "
        
        minimum = self.minimum_pavilions_amount
        maximum = self.maximum_pavilions_amount
        handler = ListValidator._handle_exception
        handler(ListValidator.validate, s, pavilions, Pavilion, minimum, maximum)
        
        shop_area = self.shop_area
        for pavilion in pavilions:
            handler(RealValidator.validate, s, shop_area.value - pavilion.footage.length.value, 0)
            shop_area -= pavilion.footage.length

        self._pavilions = pavilions
        self._invalidate_caches()
        
    @property
    def pavilions_amount(self) -> int:
        return len(self.pavilions)
        
    @property
    def income(self) -> Price:
        if self._income != Building.DEFAULT_INCOME:
            return Price(self._income.value, f"Доход с аренды (за {_get_year_form(self.YEARS)})")
        
        if self._income_cache is None:
            income = sum(pavilion.price.value for pavilion in self.pavilions) * 12 * self.YEARS
            self._income_cache = Price(income, f"Доход с аренды (за {_get_year_form(self.YEARS)})")
            
        return self._income_cache
    
    @income.setter
    def income(self, income: Money) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = MoneyValidator._handle_exception
        handler(MoneyValidator.validate, s, income, 0)
        
        self._income = Price(income, f"Доход с аренды (за {_get_year_form(self.YEARS)})")
    
    @property
    def profit(self) -> Price:
        profit = self.income.value.value - self.price_to_build.value.value
        if profit <= 0:
            message = f"\n\t{self.class_name}: "
            message += f"Прибыль ({_get_year_form(self.YEARS)} окупаемости) "
            message += f"'{self.title}' {profit} <= 0!"
            raise ValueError(message)
        self._profit_cache = Price(Ruble(profit), f"Прибыль ({_get_year_form(self.YEARS)} окупаемости)")
        return self._profit_cache
    
    def __init__(
        self, 
        length: Length = MINIMUM_LENGTH,
        width: Length = MINIMUM_WIDTH,
        height: Length = MINIMUM_HEIGHT,
        indent: Length = Building.DEFAULT_INDENT,
        price_to_build: Money = Building.DEFAULT_PRICE_TO_BUILD,
        income: Money = Building.DEFAULT_INCOME,
        floor_height: Length = MINIMUM_FLOOR_HEIGHT,
        pavilions: List[Pavilion] = list(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(length, width, height, indent, price_to_build, income, title)
        self.floor_height = floor_height
        if income == Building.DEFAULT_INCOME:
            self.pavilions = pavilions if pavilions else PavilionFactoryMethod.generate_pavilions(
                self.minimum_pavilions_amount,
                self.minimum_pavilions_amount
            )
        
    # ------------------- Output ---------------------------
    
    def print_pavilions_amount(self) -> str:
        return f"Количество павильонов:\t{self.pavilions_amount}"
    
    def __str__(self) -> str:
        result = f"{self.print_title()}:"
        result += f"\n\t{self.length}\n\t{self.width}\n\t{self.height}"
        result += f"\n\t{self.print_volume()}\n\t{self.print_area()}"
        result += f"\n\t{self.print_area_with_indent()}"
        result += f"\n\t{self.indent}\n\t{self.price_to_build}"
        result += f"\n\t{self.income}"
        return result + f"\n\t{self.profit}\n"
    
    def __repr__(self) -> str:
        result = f"{self.class_name} (title: {self.title}, "
        result += f"length: {self.length}, width: {self.width}, "
        result += f"height: {self.height}, indent: {self.indent}, "
        return result + f"price_to_build: {self.price_to_build})"
    
    # ------------------- Hash ---------------------------
    
    def __hash__(self) -> int:
        return hash((self.class_name, self.length, self.width, 
                     self.height, self.title, self.indent, self.price_to_build,
                     self.floor_height, self.pavilions))
        
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Shop, left, Shop, operator)
        
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return super().__bool__() and self.pavilions_amount != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Shop._validate(right, left, operator)
        
        return operator(right.length, left.length) and operator(right.width, left.width) and \
            operator(right.height, left.height) and operator(right.indent, left.indent) and \
            operator(right.price_to_build, left.price_to_build) and \
            operator(right.floor_height, left.floor_height) and \
            operator(right.income, left.income)
        
    def __eq__(self, other: object) -> bool:
        return Shop._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        Shop._validate(self, other, operator.ne)
        return not Shop._equality(self, other, operator.eq)