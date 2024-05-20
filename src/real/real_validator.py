from typing import Tuple

from .real import Real

from ..validators import Validator
from ..validators import NUMBER_TYPES, DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "RealValidator",
]


class RealValidator(Validator):
    
    @classmethod
    def _validate_interval(cls,
        value: Real, 
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        for item in (minimum, maximum):
            exception, message = cls.validate_object_type(item, Real | NUMBER_TYPES)
            if exception:
                return exception, message
        
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
        if value < new_minimum:
            return ValueError, f"Недопустимое значение ({value})! Значение должно быть не меньше {new_minimum}!"
        if value > new_maximum:
            return ValueError, f"Недопустимое значение ({value})! Значение должно быть не больше {new_maximum}!"
        return None, str()
    
    @classmethod
    def validate_interval(
        cls,
        value: Real, 
        minimum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: Real | NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(value, Real)
        if exception:
            return exception, message
        return cls._validate_interval(value, minimum, maximum)
    
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