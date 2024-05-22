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


from typing import List
from .. import _format_plural_form

def _print_full_form(
    length: Length,
    forms: List[str]    
) -> str:
    square_forms = [form[0] for form in forms] \
        if type(length) == Length else \
            [form[1] for form in forms]
    form = _format_plural_form(length.value.value, square_forms)
    words = str(length)[len(str(length.value)) + 1:]
    return f"{length.value} {form} {words}"

def _print_short_form(
    length: Length,
    forms: List[str]
) -> str:
    words = str(length.print_short_form())[len(str(length.value)) + 1:]
    return f"{length.value} {forms} {words}"


from .square import *
from .volume import *