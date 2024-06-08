from .building import Building

from ...measurement.length import Length
from ...measurement.money import Money
from ...value_objects.title import Title


__all__ = [
    "School",
]


class School(Building):
    
    DEFAULT_TITLE = "Школа"
    DEFAULT_PRICE_TO_BUILD = Money(1_500_000_000)
    
    def __init__(
        self, 
        length: Length = Building.MINIMUM_LENGTH,
        width: Length = Building.MINIMUM_WIDTH,
        height: Length = Building.MINIMUM_HEIGHT,
        indent: Length = Building.DEFAULT_INDENT,
        price_to_build: Money = DEFAULT_PRICE_TO_BUILD,
        income: Money = Building.DEFAULT_INCOME,
        title: str | Title = Title(DEFAULT_TITLE)
    ) -> None:
        super().__init__(length, width, height, indent, price_to_build, income, title)