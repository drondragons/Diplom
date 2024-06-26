from typing import Tuple

from .line import Line

from .. import REAL_TYPES

from ...validators import Validator, DEFAULT_NUMBER_MAXIMUM
from ...measurement.length import Length, LengthValidator
from ...value_objects.title import TitleValidator


__all__ = [
    "LineValidator",
]


class LineValidator(Validator):
    
    @classmethod
    def validate(
        cls, 
        value: Line,
        minimum: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = Validator.validate_object_type(value, Line)
        if not exception:
            exception, message = LengthValidator.validate(value.length, minimum, maximum)
        if not exception:
            exception, message = TitleValidator.validate(value.title)
        return exception, message