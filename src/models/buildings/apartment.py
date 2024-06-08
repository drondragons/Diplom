import operator
from typing import List

from .building import Building

from ..flat import Flat, FlatFactoryMethod
from ..price import Price

from ... import _validate
from ...geometry.one_dimensional import Line
from ...measurement.length import Length, LengthValidator, MeterConverter, Meter
from ...measurement.money import Money, Ruble, MoneyValidator
from ...validators import ListValidator
from ...value_objects.title import Title
from ...value_objects.real import RealValidator


__all__ = [
    "Apartment",
]


class Apartment(Building):
    
    __slots__ = [
        "_floor_height",
        "_flats",
        "_income_cache",
        "_profit_cache",
    ]
    
    DEFAULT_TITLE = "Жилой дом"
    
    PERCENTAGE = 0.8
    MINIMUM_LENGTH = Meter(70)
    MINIMUM_WIDTH = Meter(40)
    MINIMUM_HEIGHT = Meter(20)
    MINIMUM_FLOOR_HEIGHT = Meter(2.5)
    MAXIMUM_FLOOR_HEIGHT = Meter(2.7)
    DEFAULT_MAXIMUM_FLAT_FOOTAGE = Meter(100)
    
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
    def living_area(self) -> Length:
        return self.floors * self.area * self.PERCENTAGE
        
    @property
    def minimum_flats_amount(self) -> int:
        return int(self.living_area / self.DEFAULT_MAXIMUM_FLAT_FOOTAGE)
    
    @property
    def maximum_flats_amount(self) -> int:
        return int(self.living_area / Flat.MINIMUM_FOOTAGE)
        
    @property
    def floors(self) -> int:
        return int((self.height.length - self.floor_height.length) / self.floor_height.length)
    
    def _invalidate_caches(self):
        self._income_cache = None
        self._profit_cache = None
    
    @property
    def flats(self) -> List[Flat]:
        return self._flats
    
    @flats.setter
    def flats(self, flats: List[Flat]) -> None:
        s = f"\n\t{self.class_name}: "
        
        minimum = self.minimum_flats_amount
        maximum = self.maximum_flats_amount
        handler = ListValidator._handle_exception
        handler(ListValidator.validate, s, flats, Flat, minimum, maximum)
        
        living_area = self.living_area
        for flat in flats:
            handler(RealValidator.validate, s, living_area.value - flat.footage.length.value, 0)
            living_area -= flat.footage.length

        self._flats = flats
        self._invalidate_caches()
        
    @property
    def flats_amount(self) -> int:
        return len(self.flats)
        
    @property
    def income(self) -> Price:
        if self._income != Building.DEFAULT_INCOME:
            return Price(self._income.value, "Доход с продаж квартир")
        
        if self._income_cache is None:
            income = sum(flat.price.value for flat in self.flats)
            self._income_cache =  Price(income, "Доход с продаж квартир")
            
        return self._income_cache
    
    @income.setter
    def income(self, income: Money) -> None:
        s = f"\n\t{self.class_name}: "
        
        handler = MoneyValidator._handle_exception
        handler(MoneyValidator.validate, s, income, 0)
        
        self._income = Price(income, "Доход с продаж квартир")
    
    @property
    def profit(self) -> Price:
        profit = self.income.value.value - self.price_to_build.value.value
        if profit <= 0:
            message = f"\n\t{self.class_name}: "
            message += f"Прибыль с постройки здания '{self.title}' {profit} <= 0!"
            raise ValueError(message)
        self._profit_cache = Price(Ruble(profit), "Прибыль с постройки")
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
        flats: List[Flat] = list(),
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(length, width, height, indent, price_to_build, income, title)
        self.floor_height = floor_height
        if income == Building.DEFAULT_INCOME:
            self.flats = flats if flats else FlatFactoryMethod.generate_flats(
                self.minimum_flats_amount,
                self.minimum_flats_amount
            )
        
    # ------------------- Output ---------------------------
    
    def print_flats_amount(self) -> str:
        return f"Количество квартир:\t{self.flats_amount}"
    
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
                     self.floor_height))
        
    # ------------------- Validation ---------------------------
    
    @staticmethod
    def _validate(right: object, left: object, operator: operator) -> None:
        _validate(right, Apartment, left, Apartment, operator)
        
    # ------------------- Comparison operators ---------------------------
    
    def __bool__(self) -> bool:
        return super().__bool__() and self.flats_amount != 0
        
    @staticmethod
    def _equality(right: object, left: object, operator: operator) -> bool:
        Apartment._validate(right, left, operator)
        
        return operator(right.length, left.length) and operator(right.width, left.width) and \
            operator(right.height, left.height) and operator(right.indent, left.indent) and \
            operator(right.price_to_build, left.price_to_build) and \
            operator(right.floor_height, left.floor_height) and \
            operator(right.income, left.income)
        
    def __eq__(self, other: object) -> bool:
        return Apartment._equality(self, other, operator.eq)
    def __ne__(self, other: object) -> bool:
        Apartment._validate(self, other, operator.ne)
        return not Apartment._equality(self, other, operator.eq)