from . import Decimal, Fraction

NUMBER_TYPES = int | float | Decimal | Fraction

DEFAULT_NUMBER_MAXIMUM = (10 ** 10) ** 10
DEFAULT_NUMBER_MINIMUM = -DEFAULT_NUMBER_MAXIMUM