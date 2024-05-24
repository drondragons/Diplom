from typing import List, Tuple, Type, Union

from . import DEFAULT_NUMBER_MINIMUM, DEFAULT_NUMBER_MAXIMUM
from .validator import Validator

from .. import _format_number


__all__ = [
    "ListValidator",
]


class ListValidator(Validator):
    
    @classmethod
    def _validate_interval(
        cls, 
        value_list: List[object], 
        minimum: int = DEFAULT_NUMBER_MINIMUM, 
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_object_type(minimum, int)
        if not exception:
            exception, message = cls.validate_object_type(maximum, int)
        if exception:
            return exception, message
        
        value_list = len(value_list)
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
        if value_list < new_minimum:
            message = f"Недостаточное количество элементов ({_format_number(value_list)})! "
            message += f"Количество элементов должно быть не меньше {_format_number(new_minimum)}!"
            return ValueError, message
        if value_list > new_maximum:
            message = f"Слишком большое количество элементов ({_format_number(value_list)})! "
            message += f"Количество элементов должно быть не больше {_format_number(new_maximum)}!"
            return ValueError, message
        return None, str()

    @classmethod
    def _validate_elements_type(
        cls,
        value_list: List[object],
        expected_type: Type
    ) -> Tuple[None | TypeError, str]:
        exception, message = cls.validate_type(expected_type)
        if exception:
            return exception, message
        for element in value_list:
            exception, message = cls.validate_object_type(element, expected_type)
            if exception:
                break
        return exception, message
        
    @classmethod
    def validate(
        cls, 
        value_list: List[object],
        element_type: Type | Union[Type] | List[Type] | Tuple[Type],
        minimum: int = DEFAULT_NUMBER_MINIMUM,
        maximum: int = DEFAULT_NUMBER_MAXIMUM
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(element_type)
        if not exception:
            exception, message = cls.validate_object_type(value_list, list)
        if not exception:
            exception, message = cls._validate_interval(value_list, minimum, maximum)
        if not exception:
            exception, message = cls._validate_elements_type(value_list, element_type)
        return exception, message