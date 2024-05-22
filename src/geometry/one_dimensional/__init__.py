import operator
from typing import Type, Union

def _line_operate(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator
) -> None:
    if isinstance(right, right_type) and isinstance(left, left_type):
        return operator(right, left.length)
    if isinstance(right, left_type) and isinstance(left, right_type):
        return operator(right.length, left)
    return operator(right.length, left.length)


from .line import *
from .line_validator import *
from .line_factory_method import *