from typing import Tuple

from .building import Building

from ..price import PriceValidator

from ... import REAL_TYPES
from ...validators import Validator, DEFAULT_NUMBER_MAXIMUM
from ...measurement.length import Length
from ...measurement.money import Money
from ...geometry.one_dimensional import LineValidator
from ...value_objects.title import TitleValidator


__all__ = [
    "BuildingValidator",
]


class BuildingValidator(Validator):
    
    @classmethod
    def validate(
        cls,
        value: Building,
        minimum_width: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_width: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_length: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_length: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_height: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_height: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_indent: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_indent: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_price_to_build: REAL_TYPES = Money.DEFAULT_MONEY_VALUE,
        maximum_price_to_build: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Building)
        if not exception:
            exception, message = LineValidator.validate(
                value.length,
                minimum_length,
                maximum_length
            )
        if not exception:
            exception, message = LineValidator.validate(
                value.width,
                minimum_width,
                maximum_width
            )
        if not exception:
            exception, message = LineValidator.validate(
                value.height,
                minimum_height,
                maximum_height
            )
        if not exception:
            exception, message = LineValidator.validate(
                value.indent,
                minimum_indent,
                maximum_indent
            )
        if not exception:
            exception, message = PriceValidator.validate(
                value.price_to_build,
                minimum_price_to_build,
                maximum_price_to_build
            )
        if not exception:
            exception, message = TitleValidator.validate(value.title)
        return exception, message