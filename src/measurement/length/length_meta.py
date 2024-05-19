__all__ = [
    "LengthMeta"
]


class LengthMeta(type):
    
    def __subclasscheck__(cls, subclass: type) -> bool:
        return True if cls in subclass.__mro__ else False