from ..real import Real
from ..validators import NUMBER_TYPES
from ..measurement.length import Length

REAL_TYPES = Real | NUMBER_TYPES
LENGTH_TYPES = Length | REAL_TYPES

DEFAULT_SIDE_TITLES = [
    "Длина",
    "Ширина",
    "Высота",
]

from .one_dimensional import *