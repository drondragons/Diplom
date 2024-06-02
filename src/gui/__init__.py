from .. import _format_plural_form
from ..constants import DEFAULT_PLURAL_FORM
from ..measurement import DEFAULT_FORMS
from ..measurement.money import Money
from ..measurement.length import Length, Meter

def _find_money_type(text: str) -> Money:
    return next((subclass \
        for subclass in (Money.__subclasses__() + [Money]) \
            if subclass.FULL_FORM == text), None)

def _find_money_form(value: object, text: str) -> str:
    return _format_plural_form(value, _find_money_type(text).PLURAL_MONEY_FORMS)

def _find_length_type(text: str) -> Length:
    return next((subclass \
        for subclass in (Meter.__subclasses__() + [Length, Meter]) \
            if subclass.FULL_FORM == text), None)

def _find_length_form(value: object, text: str) -> str:
    forms = DEFAULT_FORMS
    _type = _find_length_type(text)
    if _type != Length:
        forms = [_type.FULL_FORM + form for form in DEFAULT_PLURAL_FORM]
    return _format_plural_form(value, forms)


from .main_window import *