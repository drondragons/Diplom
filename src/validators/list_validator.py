from typing import List, Tuple

from .validator import Validator
from .constants import DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM

from .. import format_number


__all__ = [
    "ListValidator",
]


class ListValidator(Validator):
    
    @classmethod
    def validate_interval(
        cls, 
        value: List[object], 
        minimum: int = DEFAULT_NUMBER_MINIMUM, 
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(value, list)
        if exception:
            return exception, message
        
        for item in (minimum, maximum):
            exception, message = cls.validate_object_type(item, int)
            if exception:
                return exception, message
        
        value = len(value)
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
        if value < new_minimum:
            return ValueError, f"Недостаточное количество элементов ({format_number(value)})! Количество элементов должно быть не меньше {format_number(new_minimum)}!"
        if value > new_maximum:
            return ValueError, f"Слишком большое количество элементов ({format_number(value)})! Количество элементов должно быть не больше {format_number(maximum)}!"
        return None, str()

    @classmethod
    def validate_elements_type(
        cls,
        value: List[object],
        expected_type: type
    ) -> Tuple[None | TypeError, str]:
        exception, message = cls.validate_object_type(value, list)
        if exception:
            return exception, message
        
        excpetion, message = cls.validate_type(expected_type)
        if excpetion:
            return exception, message
        
        message = str()
        exception = None
        for element in value:
            exception, message = cls.validate_object_type(element, expected_type)
            if exception:
                break
        return exception, message
        
    @classmethod
    def validate(
        cls, 
        value: List[object],
        element_type: type,
        minimum: int = DEFAULT_NUMBER_MINIMUM,
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(element_type)
        if not exception:
            exception, message = cls.validate_object_type(value, list)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        if not exception:
            exception, message = cls.validate_elements_type(value, element_type)
        return exception, message