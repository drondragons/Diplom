from .price import Price

from ... import REAL_TYPES
from ...measurement.money import Money
from ...value_objects.title import Title


__all__ = [
    "PriceBuilder",
]


class PriceBuilder:
    
    def __init__(self) -> None:
        self.money = Money()
        self.title = Title()
        
    def add_money(self, value: Money | REAL_TYPES) -> "PriceBuilder":
        self.money = value if isinstance(value, Money) else Money(value)
        return self
    
    def add_title(self, value: str | Title) -> "PriceBuilder":
        self.title = value
        return self
    
    def build(self) -> Price:
        return Price(self.money, self.title)