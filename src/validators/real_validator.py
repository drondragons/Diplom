# from ..real import Real
# from typing import Tuple
# from .constants import *
# from .. import format_number
# from .validator import Validator

# __all__ = [
#     "RealValidator",
# ]

# class RealValidator(Validator):
    
#     @classmethod
#     def validate_interval(
#         cls,
#         value: Real, 
#         minimum: Real = DEFAULT_NUMBER_MINIMUM, 
#         maximum: Real = DEFAULT_NUMBER_MAXIMUM
#     ) -> Tuple[None | ValueError, str]:
#         new_minimum = min(minimum, maximum)
#         new_maximum = max(minimum, maximum)
#         if value < new_minimum:
#             return ValueError, f"Недопустимое значение ({value})! Значение должно быть не меньше {format_number(new_minimum)}!"
#         if value > new_maximum:
#             return ValueError, f"Недопустимое значение ({value})! Значение должно быть не больше {format_number(new_maximum)}!"
#         return None, str()
    
#     @classmethod
#     def validate(
#         cls,
#         value: Real, 
#         minimum: Real = DEFAULT_NUMBER_MINIMUM, 
#         maximum: Real = DEFAULT_NUMBER_MAXIMUM
#     ) -> Tuple[None | TypeError | ValueError, str]:
#         exception, message = cls.validate_type(value, Real)
#         if not exception:
#             exception, message = cls.validate_interval(value, minimum, maximum)
#         return exception, message
    
#     def __new__(cls) -> None:
#         return super().__new__(cls)