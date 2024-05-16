# from decimal import Decimal
# from fractions import Fraction

# def format_number(value: object) -> str:
#     if isinstance(value, float | Fraction):
#         value = Decimal(float(value))
#     return "{:,}".format(value).replace(",", " ")

from .constants import *
from .validator import *
from .list_validator import *
from .number_validator import *
from .string_validator import *