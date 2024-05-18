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
        message = str()
        for index, element in enumerate(value, 1):
            exception, message = cls.validate_type(element, expected_type)
            if exception:
                message = f"Недопустимый тип '{type(element).__name__}' элемента №{index}! Ожидался тип {cls.format_union_types(expected_type)}!"
                break
        return (TypeError, message) if message else (None, message)
        
    @classmethod
    def validate(
        cls, 
        value: List[object],
        element_type: type,
        minimum: int = DEFAULT_NUMBER_MINIMUM,
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, list)
        if not exception:
            exception, message = cls.validate_interval(value, minimum, maximum)
        if not exception:
            exception, message = cls.validate_elements_type(value, element_type)
        return exception, message