from .building import Building

from ...factory_method import FactoryMethod


__all__ = [
    "BuildingFactoryMethod",
]


class BuildingFactoryMethod(FactoryMethod):
    
    @classmethod
    def generate(cls) -> Building:
        return Building()