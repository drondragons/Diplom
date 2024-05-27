from .constants import *
from .factory_method import *


from decimal import Decimal
from fractions import Fraction
from typing import Type, Union

def _format_number(value: object) -> str:
    if isinstance(value, float | Fraction):
        value = Decimal(float(value))
    value = _get_pretty_number(value)
    return "{:,}".format(value).replace(",", " ")


from .validators import *


def _get_pretty_number(value: object) -> int | float:
    rounded_value = round(float(value), 6)
    number = Decimal(rounded_value)
    return float(number) if "." in str(number) else int(number)

def _get_year_form(value: object) -> str:
    return f"{value} {_format_plural_form(value, YEARS_FORMS)}"

def _format_plural_form(value: object, forms: list[str]) -> str:
    value = _get_pretty_number(value)
    if isinstance(value, float):
        return forms[1]
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11:
        return forms[0]
    elif 1 < last_digit < 5 and (last_two_digits < 10 or last_two_digits > 20):
        return forms[1]
    return forms[2]

def _error(obj: object, message: str = str()) -> str:
    return f"\n\t{type(obj).__name__}: {message}"

def _type_error(right: object, left: object, operator: operator) -> str:
    left_name = f"'{type(left).__name__}'"
    right_name = f"'{type(right).__name__}'"
    return f"Операция {right_name} {OPERATORS[operator]} {left_name} недоступна!"

def _validate(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator
) -> None:
    message = _type_error(right, left, operator)
    if not isinstance(right, right_type):
        raise TypeError(_error(left, message))
    if not isinstance(left, left_type):
        raise TypeError(_error(right, message))
    
def _operate(
    right: object, 
    right_type: Type | Union[Type],
    left: object, 
    left_type: Type | Union[Type],
    operator: operator
) -> object:
    if isinstance(right, right_type) and isinstance(left, left_type):
        return operator(right, left.value)
    if isinstance(right, left_type) and isinstance(left, right_type):
        return operator(right.value, left)
    return operator(right.value, left.value)

def _validation_operation(
    right: object,
    left: object,
    operator: operator,
    _type: Type
) -> bool:
    _type._validate(right, left, operator)
    return _type._operate(right, left, operator)


from .value_objects import *
from .measurement import *
from .geometry import *
from .models import *