from typing import Tuple

from .flat import Flat

from ..price import PriceValidator

from ... import REAL_TYPES
from ...geometry.one_dimensional import LineValidator
from ...validators import Validator, DEFAULT_NUMBER_MAXIMUM
from ...value_objects.title import TitleValidator


__all__ = [
    "FlatValidator",
]


class FlatValidator(Validator):
    
    @classmethod
    def validate(
        cls,
        value: Flat,
        minimum_footage: REAL_TYPES = Flat.MINIMUM_FOOTAGE,
        maximum_footage: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_price_per_meter: REAL_TYPES = Flat.MINIMUM_PRICE_PER_METER,
        maximum_price_per_meter: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Flat)
        if not exception:
            exception, message = LineValidator.validate(
                value.footage,
                minimum_footage,
                maximum_footage
            )
        if not exception:
            exception, message = PriceValidator.validate(
                value.price_per_meter,
                minimum_price_per_meter,
                maximum_price_per_meter
            )
        if not exception:
            exception, message = TitleValidator.validate(value.title)
        return exception, message