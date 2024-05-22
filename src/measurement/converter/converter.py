from abc import abstractmethod


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
    
    def __new__(self) -> None:
        message = f"\n\t{self.__name__}: "
        message += f"Экземпляры класса '{self.__name__}' не могут быть созданы!"
        raise TypeError(message)