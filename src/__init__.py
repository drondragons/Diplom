from decimal import Decimal
from fractions import Fraction

def format_number(value: object) -> str:
    if isinstance(value, float | Fraction):
        value = Decimal(float(value))
    return "{:,}".format(value).replace(",", " ")

def get_pretty_number(value: object) -> int | float:
    rounded_value = round(float(value), 6)
    number = Decimal(rounded_value)
    return float(number) if "." in str(number) else int(number)

def format_plural_form(value: object, forms: list[str]) -> str:
    value = get_pretty_number(value)
    if isinstance(value, float):
        return forms[1]
    last_digit = value % 10
    last_two_digits = value % 100
    if last_digit == 1 and last_two_digits != 11:
        return forms[0]
    elif 1 < last_digit < 5 and (last_two_digits < 10 or last_two_digits > 20):
        return forms[1]
    return forms[2]

from .number import *
from .validators import *
from .measurement import *