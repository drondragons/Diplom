from ...geometry import Line
from ...measurement import Money, MoneyValidator, Ruble
from ...measurement import Length, LengthValidator
from ...value_objects import Title


__all__ = [
    "Flat",
]


class Flat:
    
    __slots__ = [
        "_footage",
        "_price_per_meter",
        "_title",
    ]
    
    DEFAULT_TITLE = "Квартира"
    DEFAULT_FOOTAGE = Length(33)
    DEFAULT_PRICE_PER_METER = Ruble(100_000)
    
    @property
    def class_name(self) -> str:
        return self.__class__.__name__
    
    @property
    def footage(self) -> Line:
        return self._footage
    
    @footage.setter
    def footage(self, footage: Length) -> None:
        s = f"\n\t{self.class_name}: "
        LengthValidator._handle_exception(LengthValidator.validate, s, footage, 0)
        self._footage = Line(footage, "Метраж")
        
    @property
    def price_per_meter(self) -> Money:
        return self._price_per_meter
    
    @price_per_meter.setter
    def price_per_meter(self, price_per_meter: Money) -> None:
        s = f"\n\t{self.class_name}: "
        MoneyValidator._handle_exception(MoneyValidator.validate, s, price_per_meter, 0)
        self._price_per_meter = price_per_meter
        
    @property
    def title(self) -> Title:
        return self._title
    
    @title.setter
    def title(self, title: str | Title) -> None:
        self._title = Title(title)
        
    @property
    def price(self) -> Money:
        return Money(self.footage.length.value * self.price_per_meter.value)
    
    @property
    def maximum_person_amount(self) -> int:
        if self.footage <= 33:
            return 1
        elif self.footage <= 42:
            return 2
        return self.footage // 18
    
    def __init__(
        self, 
        footage: Length = DEFAULT_FOOTAGE,
        price_per_meter: Money = DEFAULT_PRICE_PER_METER,
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        self.footage = footage
        self.price_per_meter = price_per_meter
        self.title = title
        
    # ------------------- Output ---------------------------
        
    def __str__(self) -> str:
        return f"{self.title}:\t{self.length}"
    
    def __repr__(self) -> str:
        return f"{self.class_name} (title: {self.title}, length: {self.length})"