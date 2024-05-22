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
        
        s = f"\n\t{cls.__name__}.generate: "
        Validator._handle_exception(Validator.validate_object_type, s, is_int, bool)
        
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
        if new_maximum - new_minimum < 1 and is_int:
            message = s
            message += "Невозможно сгенерировать целое число, "
            message += f"так как разница между минимумом "
            message += f"и максимумом меньше единицы!"
            raise ValueError(message)
        method = random.randint if is_int else random.uniform
        return Real(method(new_minimum.value, new_maximum.value))