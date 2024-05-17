from abc import abstractmethod
from typing import Type, Tuple, Union, get_args

__all__ = [
    "Validator"
]

class Validator:
    
    @classmethod
    @abstractmethod
    def validate(cls) -> str:    
        raise NotImplementedError(f"\n\t{cls.__name__}: Нереализованный абстрактный статический метод validate!")
    
    @classmethod
    def format_union_types(cls, types: Union[Type]) -> str:
        args = get_args(types)
        if not args:
            return f"'{types.__name__}'"
        return cls.__pretty_format_string_with_types(cls.__get_string_from_union_types(args))
    
    @classmethod
    def __get_string_from_union_types(cls, types: Tuple) -> str:
        return ", ".join(f"'{item.__name__}'" for item in types)
    
    @classmethod
    def __pretty_format_string_with_types(cls, types: str) -> str:
        return types[::-1].replace(",", "или ", 1)[::-1]
    
    @classmethod
    def validate_type(cls, value: object, expected_type: type) -> Tuple[None | TypeError, str]:
        return (None, str()) \
            if isinstance(value, expected_type) else \
                (TypeError, f"Недопустимый тип '{type(value).__name__}'! Ожидался тип {cls.format_union_types(expected_type)}!")
            
    @classmethod
    def validate_value(cls, value: object, compareTo: object) -> Tuple[None | ValueError, str]:
        return (None, str()) \
            if value == compareTo else \
                (ValueError, f"Несовпадение значения ({value}) с ({compareTo})!")
    
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")