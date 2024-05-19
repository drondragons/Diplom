from typing import Tuple

from .length import Length

from .. import REAL_TYPES

from ...real import RealValidator
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
        return super().validate_interval(value, minimum, maximum)
    
    @classmethod
    def validate(
        cls,
        value: Length, 
        minimum: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE, 
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, Length)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message