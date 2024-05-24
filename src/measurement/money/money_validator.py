from typing import Tuple

from .money import Money

from .. import REAL_TYPES

from ...validators import DEFAULT_NUMBER_MAXIMUM
from ...value_objects import Real, RealValidator


__all__ = [
    "MoneyValidator"
]


class MoneyValidator(RealValidator):
    
    @classmethod
    def validate(
        cls,
        value: Money, 
        minimum: REAL_TYPES = Money.DEFAULT_MONEY_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Money)
        if not exception:
            exception, message = super().validate(Real(minimum), 0)
        if not exception:
            exception, message = super().validate(Real(maximum), 0)
        if not exception:
            exception, message = super().validate(
                value.value,
                minimum, 
                maximum
            )
        return exception, message