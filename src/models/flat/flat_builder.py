from .flat import Flat

from ... import LENGTH_TYPES, REAL_TYPES
from ...measurement import Length, Money
from ...value_objects import Title


__all__ = [
    "FlatBuilder",
]


class FlatBuilder:
    
    def __init__(self) -> None:
        self.footage = Flat.MINIMUM_FOOTAGE
        self.price_per_meter = Flat.MINIMUM_PRICE_PER_METER
        self.title = Title(Flat.DEFAULT_TITLE)
        
    def add_footage(self, value: LENGTH_TYPES) -> "FlatBuilder":
        self.footage = value if isinstance(value, Length) else Length(value)
        return self
    
    def add_price_per_meter(self, value: Money | REAL_TYPES) -> "FlatBuilder":
        self.price_per_meter = value if isinstance(value, Money) else Money(value)
        return self
    
    def add_title(self, value: str | Title) -> "FlatBuilder":
        self.title = value
        return self
    
    def build(self) -> Flat:
        return Flat(self.footage, self.price_per_meter, self.title)