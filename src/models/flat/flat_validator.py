from typing import Tuple

from .flat import Flat

from ..price import PriceValidator

from ... import REAL_TYPES
from ...geometry import LineValidator
from ...validators import Validator, DEFAULT_NUMBER_MAXIMUM
from ...measurement import Money, Length
from ...value_objects import TitleValidator


__all__ = [
    "FlatValidator",
]


class FlatValidator(Validator):
    
    @classmethod
    def validate(
        cls,
        value: Flat,
        minimum_footage: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_footage: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_price_per_meter: REAL_TYPES = Money.DEFAULT_MONEY_VALUE,
        maximum_price_per_meter: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        can_title_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Flat)
        if not exception:
            exception, message = LineValidator.validate(
                value.footage,
                minimum_footage,
                maximum_footage,
                can_title_be_empty
            )
        if not exception:
            exception, message = PriceValidator.validate(
                value.price_per_meter,
                minimum_price_per_meter,
                maximum_price_per_meter,
                can_title_be_empty
            )
        if not exception:
            exception, message = TitleValidator.validate(value.title, can_title_be_empty)
        return exception, message