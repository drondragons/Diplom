from typing import Tuple

from .line import Line

from .. import REAL_TYPES

from ...title import TitleValidator
from ...validators import Validator
from ...validators import DEFAULT_NUMBER_MAXIMUM
from ...measurement.length import Length, LengthValidator


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
        can_title_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = LengthValidator.validate(value.length, minimum, maximum)
        if not exception:
            exception, message = TitleValidator.validate(value.title, can_title_be_empty)
        return exception, message