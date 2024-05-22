from typing import Tuple

from .money import Money

from .. import REAL_TYPES

from ...real import Real, RealValidator
from ...validators import DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "MoneyValidator"
]


class MoneyValidator(RealValidator):
    
    @classmethod
    def validate_interval(
        cls,
        value: Money, 
        minimum: REAL_TYPES = Money.DEFAULT_MONEY_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(value, Money)
        if not exception:
            exception, message = cls._validate_minimum_maximum(minimum, maximum)
        if not exception:
            exception, message = RealValidator.validate_interval(Real(minimum), 0, maximum)
        if not exception:
            exception, message = cls._validate_interval(value, minimum, maximum)
        return exception, message
    
    @classmethod
    def validate(
        cls,
        value: Money, 
        minimum: REAL_TYPES = Money.DEFAULT_MONEY_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Money)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message