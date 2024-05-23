from abc import abstractmethod
from typing import List


__all__ = [
    "Converter",
]


class Converter:
    
    @classmethod
    @abstractmethod
    def convert(cls) -> object:
        message = f"\n\t{cls.__name__}: "
        message += "Нереализованный абстрактный статический метод convert!"
        raise NotImplementedError(message)
    
    @classmethod
    @abstractmethod
    def auto_convert(cls) -> object:
        message = f"\n\t{cls.__name__}: "
        message += "Нереализованный абстрактный статический метод auto_convert!"
        raise NotImplementedError(message)
    
    @classmethod
    def _find_correct_type(cls, values: List[object]) -> object:
        result = [value for value in values if 1 <= value]
        return min(result, key = lambda item: item.value) \
            if result else \
                max(values, key = lambda item: item.value)
                
    @classmethod
    def _increase_type(cls, value: object, types: List[object]) -> object:
        result = [
            cls._convert(value, _type)
                for _type in types
                    if 0 < cls._convert(value, _type).value <= value.value
        ]
        return cls._find_correct_type(result) if result else value
    
    @classmethod
    def _decrease_type(cls, value: object, types: List[object]) -> object:
        result = [
            cls._convert(value, _type)
                for _type in types
                    if value.value <= cls._convert(value, _type).value < 1000
        ]
        return cls._find_correct_type(result) if result else value
    
    def __new__(self) -> None:
        message = f"\n\t{self.__name__}: "
        message += f"Экземпляры класса '{self.__name__}' не могут быть созданы!"
        raise TypeError(message)