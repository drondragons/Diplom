from typing import Tuple

from .title import Title

from ...validators import StringValidator


__all__ = [
    "TitleValidator",
]


class TitleValidator(StringValidator):
    
    @classmethod
    def validate(
        cls, 
        value: Title, 
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(value, Title)
        if not exception:
            exception, message = super().validate(value.value, False)
        return exception, message