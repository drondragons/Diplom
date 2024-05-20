from abc import abstractmethod
from types import UnionType
from typing import Type, Union, Tuple, List, get_args


__all__ = [
    "Validator",
]


class Validator:
    
    @classmethod
    @abstractmethod
    def validate(cls) -> str:    
        raise NotImplementedError(f"\n\t{cls.__name__}: Нереализованный абстрактный статический метод validate!")
    
    @classmethod
    def format_union_types(cls, types: Type | Union[Type] | List[Type] | Tuple[Type]) -> str:
        if not isinstance(types, type | UnionType | list | tuple):
            raise TypeError(f"Ожидался тип, объединение, кортеж или список типов!")
        if isinstance(types, list | tuple) and not types:
            raise TypeError(f"Список или кортеж типов пуст!")
        if isinstance(types, list | tuple) and not all(isinstance(item, type) for item in types):
            raise TypeError(f"Список или кортеж типов содержит объекты!")
        
        args = None
        if isinstance(types, type):
            return f"'{types.__name__}'"
        elif isinstance(types, UnionType):
            args = get_args(types)
        elif isinstance(types, list | tuple):
            args = tuple(types)
        return cls.__pretty_format_string_with_types(cls.__get_string_from_union_types(args))
    
    @classmethod
    def __get_string_from_union_types(cls, types: Tuple) -> str:
        return ", ".join(f"'{item.__name__}'" for item in types)
    
    @classmethod
    def __pretty_format_string_with_types(cls, types: str) -> str:
        return types[::-1].replace(",", "или ", 1)[::-1]
    
    @classmethod
    def validate_type(cls, value: type | Union[Type]) -> Tuple[None | TypeError, str]:
        return (None, str()) \
            if isinstance(value, type) or isinstance(value, UnionType) else \
                (TypeError, f"Ожидался тип объекта, а не объект {type(value).__name__}()!")
    
    @classmethod
    def validate_object_type(cls, value: object, expected_type: type | Union[Type]) -> Tuple[None | TypeError, str]:
        if isinstance(value, type | UnionType):
            return (TypeError, f"Ожидался объект, а не тип объекта {cls.format_union_types(value)}!")
        exception, message = cls.validate_type(expected_type)
        if exception:
            return exception, message
        return (None, str()) \
            if isinstance(value, expected_type) else \
                (TypeError, f"Недопустимый тип '{type(value).__name__}'! Ожидался тип {cls.format_union_types(expected_type)}!")
            
    @classmethod
    def validate_value(cls, value: object, compareTo: object) -> Tuple[None | ValueError, str]:
        exception, message = cls.validate_type(value)
        if not exception:
            return (TypeError, f"Ожидался сравниваемый объект, а не тип объекта '{value.__name__}'!")
        
        exception, message = cls.validate_type(compareTo)
        if not exception:
            return (TypeError, f"Ожидался эталонный объект, а не тип объекта '{compareTo.__name__}'!")
        
        return (None, str()) \
            if value == compareTo else \
                (ValueError, f"Несовпадение значения {value} с {compareTo}!")
    
    @classmethod
    def _handle_exception(cls, function, message, *args):
        exception, _message = function(*args)
        if exception:
            raise exception(message + _message)
    
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")