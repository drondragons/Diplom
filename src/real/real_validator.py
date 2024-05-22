from typing import Tuple

from .real import Real

from ..validators import NumberValidator
from ..validators import NUMBER_TYPES, DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "RealValidator",
]


class RealValidator(NumberValidator):
    
    @classmethod
    def _validate_minimum_maximum(
        cls,
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(minimum, Real | NUMBER_TYPES)
        if not exception:
            exception, message = cls.validate_object_type(maximum, Real | NUMBER_TYPES)
        return exception, message
    
    @classmethod
    def validate_interval(
        cls,
        value: Real, 
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(value, Real)
        if not exception:
            exception, message = cls._validate_minimum_maximum(minimum, maximum)
        if not exception:
            exception, message = cls._validate_interval(value, minimum, maximum)
        return exception, message
    
    @classmethod
    def validate(
        cls,
        value: Real, 
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Real)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message