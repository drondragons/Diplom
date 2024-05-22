from .length_meta import *
from .length import *
from .meter import *
from .length_validator import *
from .length_converter import *


import operator
from typing import Type, Union, Callable

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
    left = MeterConverter.convert(left).value
    right = MeterConverter.convert(right).value
    return operator(right, left)

def _meter_math(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator, 
    validation_function: Callable,
    operation_function: Callable
) -> object:
    left_type._validate(right, left, operator)
    real = left_type._operate(right, left, operator)
    if isinstance(right, right_type) or isinstance(left, right_type):
        return left_type(real)
    return MeterConverter.convert(Meter(real), left_type)


from .kilometer import *
from .nanometer import *
from .decimeter import *
from .pikometer import *
from .millimeter import *
from .centimeter import *
from .femtometer import *
from .micrometer import *
from .length_factory_method import *