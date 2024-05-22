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
        message = f"\n\t{cls.__name__}: "
        message += "Нереализованный абстрактный статический метод validate!"
        raise NotImplementedError(message)
    
    @classmethod
    def __get_types(
        cls, 
        types: Type | Union[Type] | List[Type] | Tuple[Type]
    ) -> Type | Tuple[Type]:
        if isinstance(types, type):
            return types
        elif isinstance(types, UnionType):
            return get_args(types)
        return tuple(types)
    
    @classmethod
    def __format_union_types(
        cls, 
        types: Type | Union[Type] | List[Type] | Tuple[Type]
    ) -> str:
        types = cls.__get_types(types)
        if isinstance(types, type):
            return f"'{types.__name__}'"
        s = cls.__get_string_from_union_types(types)
        return cls.__pretty_format_string_with_types(s)
    
    @classmethod
    def __get_string_from_union_types(cls, types: Tuple) -> str:
        return ", ".join(f"'{item.__name__}'" for item in types)
    
    @classmethod
    def __pretty_format_string_with_types(cls, types: str) -> str:
        return types[::-1].replace(",", "или ", 1)[::-1]
    
    @classmethod
    def validate_type(
        cls, 
        _type: Type | Union[Type] | List[Type] | Tuple[Type]
    ) -> Tuple[None | TypeError, str]:
        if not isinstance(_type, type | UnionType | list | tuple):
            message = "Ожидался тип, объединение, кортеж или список типов, "
            message += f"а не объект {type(_type).__name__}()!"
            return TypeError, message
        if isinstance(_type, list | tuple) and not _type:
            return TypeError, f"Список или кортеж типов пуст!"
        if isinstance(_type, list | tuple) and not all(isinstance(item, type) for item in _type):
            return TypeError, f"Список или кортеж типов содержит объекты!"
        return None, str()
    
    @classmethod
    def validate_type_of_type(
        cls, 
        _type: Type | Union[Type] | List[Type] | Tuple[Type],
        expected_types: Type | Union[Type] | List[Type] | Tuple[Type]
    ) -> Tuple[None | TypeError, str]:
        for item in (_type, expected_types):
            exception, message = cls.validate_type(item)
            if exception:
                return exception, message
            
        _type = cls.__get_types(_type)
        expected_types = cls.__get_types(expected_types)
        message = f"Недопустимый тип {cls.__format_union_types(_type)}! "
        message += f"Ожидался тип {cls.__format_union_types(expected_types)}!"
        if isinstance(_type, type) and isinstance(expected_types, type) and \
            _type != expected_types:
            return TypeError, message
        if isinstance(_type, type) and isinstance(expected_types, tuple) and \
            _type not in expected_types:
            return TypeError, message
        if isinstance(_type, tuple) and isinstance(expected_types, type) and \
            (len(_type) != 1 or len(_type) == 1 and _type[0] != expected_types):
            return TypeError, message
        if isinstance(_type, tuple) and isinstance(expected_types, tuple) and \
            not set(_type).issubset(expected_types):
                return TypeError, message
        return None, str()
    
    @classmethod
    def validate_object(cls, value: object) -> Tuple[None | TypeError, str]:
        exception, _ = cls.validate_type(value)
        if not exception:
            message = f"Ожидался объект, а не тип объекта {cls.__format_union_types(value)}!"
            return TypeError, message
        return None, str()
    
    @classmethod
    def validate_object_type(
        cls, 
        value: object, 
        expected_type: Type | Union[Type] | List[Type] | Tuple[Type]
    ) -> Tuple[None | TypeError, str]:
        exception, message = cls.validate_object(value)
        if not exception:
            exception, message = cls.validate_type(expected_type)
        
        if exception:
            return exception, message
        
        message = f"Недопустимый тип '{type(value).__name__}'! "
        message += f"Ожидался тип {cls.__format_union_types(expected_type)}!"
        expected_type = cls.__get_types(expected_type)
        if isinstance(expected_type, type) and not isinstance(value, expected_type):
            return TypeError, message
        if isinstance(expected_type, tuple) and type(value) not in expected_type:
            return TypeError, message
        return None, str()
            
    @classmethod
    def validate_value(
        cls, 
        value: object, 
        compareTo: object
    ) -> Tuple[None | ValueError, str]:
        exception, _ = cls.validate_type(value)
        if not exception:
            message = f"Ожидался сравниваемый объект, а не тип объекта '{value.__name__}'!"
            return TypeError, message
        
        exception, _ = cls.validate_type(compareTo)
        if not exception:
            message = f"Ожидался эталонный объект, а не тип объекта '{compareTo.__name__}'!"
            return TypeError, message
        
        return (None, str()) \
            if value == compareTo else \
                (ValueError, f"Несовпадение значения {value} с {compareTo}!")
    
    @classmethod
    def _handle_exception(cls, function, message, *args):
        exception, _message = function(*args)
        if exception:
            raise exception(message + _message)
    
    def __new__(self) -> None:
        s = f"\n\t{self.__name__}: "
        message = s + f"Экземпляры класса '{self.__name__}' не могут быть созданы!"
        raise TypeError(message)