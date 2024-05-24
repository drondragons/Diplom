from decimal import Decimal
from fractions import Fraction

NUMBER_TYPES = int | float | Decimal | Fraction

DEFAULT_NUMBER_MAXIMUM = (10 ** 10) ** 10
DEFAULT_NUMBER_MINIMUM = -DEFAULT_NUMBER_MAXIMUM


from .validator import *
from .list_validator import *
from .number_validator import *
from .string_validator import *