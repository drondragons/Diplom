from typing import Tuple

from .validator import Validator


__all__ = [
    "StringValidator",
]


class StringValidator(Validator):
    
    @classmethod
    def _validate_on_empty(cls, value: str) -> Tuple[None | ValueError, str]:
        return (ValueError, "Строка не должна быть пустой!") \
            if not value or value.isspace() else \
                (None, str())
    
    @classmethod
    def validate(
        cls, 
        value: str, 
        can_be_empty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_object_type(can_be_empty, bool)
        if not exception:
            exception, message = cls.validate_object_type(value, str)
        if not exception and not can_be_empty:
            exception, message = cls._validate_on_empty(value)
        return exception, message