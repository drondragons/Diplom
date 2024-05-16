def format_number(value: object) -> str:
    return "{:,}".format(value).replace(",", " ")

from .constants import *
from .validator import *
from .list_validator import *
from .number_validator import *
from .string_validator import *