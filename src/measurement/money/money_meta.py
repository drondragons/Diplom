from typing import Type


__all__ = [
    "MoneyMeta"
]


class MoneyMeta(type):
    
    def __subclasscheck__(cls, subclass: Type) -> bool:
        return True if cls in subclass.__mro__ else False