from typing import Tuple

from .money import Money

from .. import REAL_TYPES

from ...real import RealValidator
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
        if exception:
            return exception, message
        return cls._validate_interval(value, minimum, maximum)
    
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