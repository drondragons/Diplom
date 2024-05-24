from typing import Tuple

from .real import Real

from ...validators import NumberValidator
from ...validators import NUMBER_TYPES, DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "RealValidator",
]


class RealValidator(NumberValidator):
    
    @classmethod
    def validate(
        cls,
        value: Real, 
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Real)
        if not exception:
            minimum = minimum.value if isinstance(minimum, Real) else minimum
            maximum = maximum.value if isinstance(maximum, Real) else maximum
            exception, message = super().validate(
                value.value, 
                NUMBER_TYPES, 
                minimum, 
                maximum
            )
        return exception, message