import random

from .real import Real

from ..validators import Validator
from ..validators import NUMBER_TYPES

from ..factory_method import FactoryMethod


__all__ = [
    "RealFactoryMethod",
]


class RealFactoryMethod(FactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Real | NUMBER_TYPES = FactoryMethod.DEFAULT_MINIMUM_VALUE,
        maximum: Real | NUMBER_TYPES = FactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Real:
        minimum = Real(minimum)
        maximum = Real(maximum)
        
        exception, message = Validator.validate_type(is_int, bool)
        if exception:
            raise exception(f"\n\t{cls.__name__}.generate: " + message)
        
        method = random.randint if is_int else random.uniform
        new_minimum, new_maximum = min(minimum, maximum), max(minimum, maximum)
        return Real(method(new_minimum.value, new_maximum.value))