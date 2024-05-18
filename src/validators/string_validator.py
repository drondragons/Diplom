from typing import Tuple
from .validator import Validator


__all__ = [
    "StringValidator",
]


class StringValidator(Validator):
    
    @classmethod
    def validate_on_empty_string(cls, value: str) -> Tuple[None | ValueError, str]:
        return (ValueError, "Строка не должна быть пустой!") \
            if not value or value.isspace() else \
                (None, str())
    
    @classmethod
    def validate(
        cls, 
        value: str, 
        canBeEmpty: bool = False
    ) -> Tuple[None | TypeError | ValueError, str]:
        exception, message = cls.validate_type(value, str)
        if not exception and not canBeEmpty:
            exception, message = cls.validate_on_empty_string(value)
        return exception, message