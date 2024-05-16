from .constants import *
from . import format_number
from typing import List, Tuple
from .validator import Validator

__all__ = [
    "ListValidator"
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

    # @classmethod
    # def validateListElements(
    #     cls, 
    #     value: list,
    #     _type: type,
    #     compareTo: object,
    #     message: str = str()
    # ) -> None:
    #     cls.validateElementsType(value, _type, message)
    #     cls.validateElementsValue(value, compareTo, message)

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

    # @classmethod
    # def validateElementsType(
    #     cls,
    #     value: list,
    #     _type: type, 
    #     message: str = str()
    # ) -> None:
    #     for index, element in enumerate(value):
    #         cls.validateType(
    #             element, 
    #             _type, 
    #             f"элемента №{index} списка {message}"
    #         )
            
    # @classmethod
    # def validateElementsValue(
    #     cls, 
    #     value: list,
    #     compareTo: object,
    #     message: str = str()
    # ) -> None:
    #     for index, element in enumerate(value):
    #         cls.validateValue(
    #             element, 
    #             compareTo, 
    #             f"элемента №{index} списка {message}"
    #         ) 
    
    # @classmethod
    # def validateListElementTypes(
    #     cls,
    #     value: list,
    #     elementType: type,
    #     minimum: float = DEFAULT_MINIMUM_NUMBER, 
    #     maximum: float = DEFAULT_MAXIMUM_NUMBER, 
    #     message: str = str()
    # ) -> None:
    #     cls.validateType(value, list, message)
    #     cls.validateInterval(value, minimum, maximum, message)
    #     cls.validateElementsType(value, elementType, message)
        
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
        
    def __new__(cls) -> None:
        super().__new__(cls)