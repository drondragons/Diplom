from abc import abstractmethod

__all__ = [
    "FactoryMethod"
]

class FactoryMethod:
    
    @classmethod
    
    def __new__(cls) -> None:
        raise TypeError(f"Экземпляры класса '{cls.__name__}' не могут быть созданы!")