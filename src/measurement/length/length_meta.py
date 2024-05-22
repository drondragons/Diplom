from typing import Type


__all__ = [
    "LengthMeta"
]


class LengthMeta(type):
    
    def __subclasscheck__(cls, subclass: Type) -> bool:
        return True if cls in subclass.__mro__ else False