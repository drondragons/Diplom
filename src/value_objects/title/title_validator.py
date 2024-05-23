from typing import Tuple

from .title import Title

from ...validators import StringValidator


__all__ = [
    "TitleValidator",
]


class TitleValidator(StringValidator):
    
    @classmethod
    def __validate_on_empty_title(cls, value: Title) -> Tuple[None | ValueError, str]:
        return (ValueError, "Название не должно быть пустым!") \
            if not value or value.isspace() else \
                (None, str())
    
    @classmethod
    def validate(
        cls, 
        value: Title, 
        can_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(can_be_empty, bool)
        if not exception:
            exception, message = cls.validate_object_type(value, Title)
        if not exception and not can_be_empty:
            exception, message = cls.__validate_on_empty_title(value)
        return exception, message