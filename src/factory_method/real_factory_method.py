import random
from ..real import Real
from ..validators import NUMBER_TYPES
from ..validators import Validator, NumberValidator

__all__ = [
    "RealFactoryMethod",
]

class RealFactoryMethod:
    
    DEFAULT_MAXIMUM = 100
    DEFAULT_MINIMUM = -DEFAULT_MAXIMUM
    
    @classmethod
    def generate(
        cls, 
        minimum: NUMBER_TYPES = DEFAULT_MINIMUM,
        maximum: NUMBER_TYPES = DEFAULT_MAXIMUM,
        is_int: bool = True
    ) -> Real:
        exception, message = Validator.validate_type(is_int, bool)
        if exception:
            raise exception(message)
        
        exception, message = NumberValidator.validate(minimum, NUMBER_TYPES)
        if exception:
            raise exception(message)
        
        exception, message = NumberValidator.validate(maximum, NUMBER_TYPES)
        if exception:
            raise exception(message)
        
        new_minimum = min(minimum, maximum)
        new_maximum = max(minimum, maximum)
    
        method = random.randint if is_int else random.uniform
        return Real(method(new_minimum, new_maximum))
    
    def __new__(cls) -> None:
        raise TypeError(f"Экземпляры класса '{cls.__name__}' не могут быть созданы!")