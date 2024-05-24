import math
import random

from .real import Real

from ...validators import Validator
from ...validators import NUMBER_TYPES
from ...factory_method import FactoryMethod


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
        s = f"\n\t{cls.__name__}.generate: "
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, is_int, bool)
        handler(Validator.validate_object_type, s, minimum, Real | NUMBER_TYPES)
        handler(Validator.validate_object_type, s, maximum, Real | NUMBER_TYPES)
        
        new_minimum = Real(min(minimum, maximum))
        new_maximum = Real(max(minimum, maximum))
        if math.ceil(new_minimum) > math.floor(new_maximum) and is_int:
            message = s + "Невозможно сгенерировать целое число "
            message += f"между {new_minimum} и {new_maximum}!"
            raise ValueError(message)
        
        new_minimum = new_minimum.value
        new_maximum = new_maximum.value
        if is_int:
            value = random.randint(math.ceil(new_minimum), math.floor(new_maximum))
        else:
            value = random.uniform(new_minimum, new_maximum)
        return Real(value)