from ..validators import NUMBER_TYPES
from ..measurement import Length
from ..value_objects import Real

REAL_TYPES = Real | NUMBER_TYPES
LENGTH_TYPES = Length | REAL_TYPES

DEFAULT_SIDE_TITLES = [
    "Длина",
    "Ширина",
    "Высота",
]


from .one_dimensional import *


LINE_TYPES = Line | LENGTH_TYPES


from .two_dimensional import *
from .three_dimensional import *