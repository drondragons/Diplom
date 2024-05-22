from .money_meta import *
from .money import *
from .money_validator import *
from .money_converter import *


import operator
from typing import Type, Union

def _money_operate(
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
    if type(right) == Money or type(left) == Money:
        return operator(left_type(left).value, left_type(right).value)
    left = MoneyConverter.convert(left, left_type).value
    right = MoneyConverter.convert(right, left_type).value
    return operator(right, left)


from .ruble import *
from .dollar import *
from .euro import *
from .yuan import *
from .pound import *
from .money_factory_method import *