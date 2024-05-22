from abc import abstractmethod


__all__ = [
    "FactoryMethod",
]


class FactoryMethod:
    
    DEFAULT_MAXIMUM_VALUE = 100
    DEFAULT_MINIMUM_VALUE = -DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    @abstractmethod
    def generate(cls) -> object:
        message = f"\n\t{cls.__name__}: "
        message += f"Нереализованный абстрактный статический метод generate!"
        raise NotImplementedError(message)
    
    def __new__(self) -> None:
        message = f"\n\t{self.__name__}: "
        message += f"Экземпляры класса '{self.__name__}' не могут быть созданы!"
        raise TypeError(message)