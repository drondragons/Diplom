import random

from . import NUMBER_TYPES
from . import Validator, NumberValidator

from .real import Real

from ..factory_method import FactoryMethod


__all__ = [
    "RealFactoryMethod",
]


class RealFactoryMethod(FactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: NUMBER_TYPES = FactoryMethod.DEFAULT_MINIMUM_VALUE,
        maximum: NUMBER_TYPES = FactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True
    ) -> Real:
        methods = {
            (is_int, bool): Validator.validate_type,
            (minimum, NUMBER_TYPES): NumberValidator.validate,
            (maximum, NUMBER_TYPES): NumberValidator.validate,
        }
        for arg, method in methods.items():
            exception, message = method(*arg)
            if exception:
                raise exception(f"\n\t{cls.__name__}.generate: " + message)
        method = random.randint if is_int else random.uniform
        new_minimum, new_maximum = min(minimum, maximum), max(minimum, maximum)
        return Real(method(new_minimum, new_maximum))