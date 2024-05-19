from typing import Tuple

from .title import Title

from ..validators import StringValidator


__all__ = [
    "TitleValidator",
]


class TitleValidator(StringValidator):
    
    @classmethod
    def validate_on_empty_string(cls, value: Title) -> Tuple[None | ValueError, str]:
        return (ValueError, "Строка не должна быть пустой!") \
            if not value or value.isspace() else \
                (None, str())
    
    @classmethod
    def validate(
        cls, 
        value: Title, 
        canBeEmpty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, Title)
        if not exception and not canBeEmpty:
            exception, message = cls.validate_on_empty_string(value)
        return exception, message