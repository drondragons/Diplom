from typing import Tuple

from .price import Price

from ... import REAL_TYPES
from ...validators import Validator
from ...validators import DEFAULT_NUMBER_MAXIMUM
from ...measurement import Money, MoneyValidator
from ...value_objects import TitleValidator


__all__ = [
    "PriceValidator",
]


class PriceValidator(Validator):
    
    @classmethod
    def validate(
        cls,
        value: Price,
        minimum: REAL_TYPES = Money.DEFAULT_MONEY_VALUE,
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = Validator.validate_object_type(value, Price)
        if not exception:
            exception, message = MoneyValidator.validate(value.value, minimum, maximum)
        if not exception:
            exception, message = TitleValidator.validate(value.title)
        return exception, message