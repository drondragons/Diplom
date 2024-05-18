from ..real import Real
from ..validators import NUMBER_TYPES

REAL_TYPES = Real | NUMBER_TYPES

DEFAULT_SHORT_FORM = "у.е."
DEFAULT_FULL_FORM = "условная единица"
DEFAULT_FORMS = [
    DEFAULT_FULL_FORM,
    "условные единицы",
    "условных единиц",
]

from .money import *
from .length import *