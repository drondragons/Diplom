from .. import _format_plural_form
from ..constants import DEFAULT_PLURAL_FORM
from ..measurement import DEFAULT_FORMS
from ..measurement.money import Money
from ..measurement.length import Length, Meter

def _find_money_form(value: object, text: str) -> str:
    forms = next((subclass.PLURAL_MONEY_FORMS \
        for subclass in (Money.__subclasses__() + [Money]) \
            if subclass.FULL_FORM == text), None)
    return _format_plural_form(value, forms)

def _find_length_form(value: object, text: str) -> str:
    forms = list()
    for subclass in (Meter.__subclasses__() + [Length, Meter]):
        if subclass.FULL_FORM == text:
            forms = DEFAULT_FORMS \
                if subclass == Length else \
                    [subclass.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
    return _format_plural_form(value, forms)


from .main_window import *