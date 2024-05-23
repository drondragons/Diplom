from typing import Tuple

from .length import Length

from .. import REAL_TYPES

from ...value_objects import Real, RealValidator
from ...validators import DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "LengthValidator"
]


class LengthValidator(RealValidator):
    
    @classmethod
    def validate_interval(
        cls,
        value: Length, 
        minimum: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(value, Length)
        if not exception:
            exception, message = cls._validate_minimum_maximum(minimum, maximum)
        if not exception:
            exception, message = RealValidator.validate_interval(Real(minimum), 0)
        if not exception:
            exception, message = cls._validate_interval(value, minimum, maximum)
        return exception, message
    
    @classmethod
    def validate(
        cls,
        value: Length, 
        minimum: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Length)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message