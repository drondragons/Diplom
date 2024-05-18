from typing import Tuple

from .meter import Meter
from .constants import REAL_TYPES

from ...real import RealValidator
from ...validators import DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "MeterValidator"
]


class MeterValidator(RealValidator):
    
    @classmethod
    def validate_interval(
        cls,
        value: Meter, 
        minimum: REAL_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        return super().validate_interval(value, minimum, maximum)
    
    @classmethod
    def validate(
        cls,
        value: Meter, 
        minimum: REAL_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, Meter)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message