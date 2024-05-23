from .length_meta import *
from .length import *
from .meter import *
from .length_validator import *
from .length_converter import *


import operator
from typing import Type, Union

def _meter_operate(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator
) -> object:
    if isinstance(right, right_type) and type(left) == left_type:
        return operator(right, left.value)
    if type(right) == left_type and isinstance(left, right_type):
        return operator(right.value, left)
    if type(left) == Length and type(right) != Length:
        left = MeterConverter.convert(left, type(right))
    if type(left) != Length and type(right) == Length:
        right = MeterConverter.convert(right, type(left))
    if type(left) != Length and type(right) != Length:
        left = MeterConverter.convert(left, Meter)
        right = MeterConverter.convert(right, Meter)
    return operator(right, left)

def _meter_math(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator, 
) -> object:
    left_type._validate(right, left, operator)
    real = left_type._operate(right, left, operator)
    if isinstance(right, right_type) or isinstance(left, right_type):
        return left_type(real)
    return real


from .kilometer import *
from .nanometer import *
from .decimeter import *
from .pikometer import *
from .millimeter import *
from .centimeter import *
from .femtometer import *
from .micrometer import *
from .length_factory_method import *