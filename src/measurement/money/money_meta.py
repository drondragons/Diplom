__all__ = [
    "MoneyMeta"
]


class MoneyMeta(type):
    
    def __subclasscheck__(cls, subclass: type) -> bool:
        return True if cls in subclass.__mro__ else False