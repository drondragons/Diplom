from .validator import Validator
from . import Tuple, Decimal, Fraction
from .constants import NUMBER_TYPES, DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM

from .. import format_number


__all__ = [
    "NumberValidator", 
    "IntValidator",
    "FloatValidator",
    "DecimalValidator",
    "FractionValidator",
]


class NumberValidator(Validator):
    
    @classmethod
    def validate_interval(
        cls,
        value: NUMBER_TYPES, 
        minimum: NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
        if value < new_minimum:
            return ValueError, f"Недопустимое значение ({format_number(value)})! Значение должно быть не меньше {format_number(new_minimum)}!"
        if value > new_maximum:
            return ValueError, f"Недопустимое значение ({format_number(value)})! Значение должно быть не больше {format_number(new_maximum)}!"
        return None, str()
    
    @classmethod
    def validate(
        cls,
        value: NUMBER_TYPES, 
        _type: type,
        minimum: NUMBER_TYPES = DEFAULT_NUMBER_MINIMUM, 
        maximum: NUMBER_TYPES = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, _type)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        return exception, message
    

class IntValidator(NumberValidator):
    
    @classmethod
    def validate(
        cls,
        value: int, 
        minimum: int = DEFAULT_NUMBER_MINIMUM, 
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        return super().validate(value, int, minimum, maximum)
        

class FloatValidator(NumberValidator):
    
    @classmethod
    def validate(
        cls,
        value: float, 
        minimum: float = DEFAULT_NUMBER_MINIMUM, 
        maximum: float = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        return super().validate(value, float, minimum, maximum)
    
        
class DecimalValidator(NumberValidator):
    
    @classmethod
    def validate(
        cls,
        value: Decimal, 
        minimum: Decimal = DEFAULT_NUMBER_MINIMUM, 
        maximum: Decimal = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        return super().validate(value, Decimal, minimum, maximum)
        
        
class FractionValidator(NumberValidator):
    
    @classmethod
    def validate(
        cls,
        value: Fraction, 
        minimum: Fraction = DEFAULT_NUMBER_MINIMUM, 
        maximum: Fraction = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        return super().validate(value, Fraction, minimum, maximum)