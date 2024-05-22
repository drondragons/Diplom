from typing import Tuple, Type

from .rectangle import Rectangle, Square

from .. import REAL_TYPES
from ..one_dimensional import LineValidator

from ...title import TitleValidator
from ...validators import Validator
from ...validators import DEFAULT_NUMBER_MAXIMUM
from ...measurement import Length


__all__ = [
    "RectangleValidator",
    "SquareValidator",
]


class RectangleValidator(Validator):
    
    @classmethod
    def validate(
        cls,
        value: Rectangle | Square,
        _type: Type,
        minimum_width: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_width: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_length: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_length: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        can_title_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type_of_type(_type, Rectangle | Square)
        if not exception:
            exception, message = cls.validate_object_type(value, _type)
        if not exception:
            exception, message = LineValidator.validate(
                value.length,
                minimum_length,
                maximum_length,
                can_title_be_empty
            )
        if not exception:
            exception, message = LineValidator.validate(
                value.width,
                minimum_width,
                maximum_width,
                can_title_be_empty
            )
        if not exception:
            exception, message = TitleValidator.validate(value.title, can_title_be_empty)
        return exception, message
    
    
class SquareValidator(RectangleValidator):
    
    @classmethod
    def validate(
        cls,
        value: Square,
        minimum_width: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_width: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        minimum_length: REAL_TYPES = Length.DEFAULT_LENGTH_VALUE,
        maximum_length: REAL_TYPES = DEFAULT_NUMBER_MAXIMUM,
        can_title_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        return super().validate(
            value,
            Square,
            minimum_width, 
            maximum_width, 
            minimum_length,
            maximum_length,
            can_title_be_empty
        )