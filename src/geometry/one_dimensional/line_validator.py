from .line import Line

from .. import REAL_TYPES

from ...title import TitleValidator
from ...validators import Validator
from ...measurement.length import LengthValidator


__all__ = [
    "LineValidator",
]


class LineValidator(Validator):
    
    @classmethod
    def validate(
        cls, 
        value: Line,
        minimum: RE
    )