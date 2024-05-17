from abc import abstractmethod

__all__ = [
    "FactoryMethod"
]

class FactoryMethod:
    
    @classmethod
    @abstractmethod
    def generate(cls) -> object:
        raise NotImplementedError(f"\n\t{cls.__name__}: Нереализованный абстрактный статический метод generate!")
    
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")