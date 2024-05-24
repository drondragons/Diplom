from .. import _print_full_form, _print_short_form
from ..length import Length, LengthValidator


__all__ = [
    "SquarePrinter",
]


class SquarePrinter:
    
    DEFAULT_SHORT_SQUARE_FORM = "кв."
    DEFAULT_SQUARE_FORMS = [
        ("квадратная", "квадратный"),
        ("квадратные", "квадратных"),
        ("квадратных", "квадратных"),
    ]
    
    @classmethod
    def print_full_form(cls, length: Length) -> str:
        s = f"\n\t{cls.__name__}.print_full_form: "
        LengthValidator._handle_exception(LengthValidator.validate, s, length)
        return _print_full_form(length, cls.DEFAULT_SQUARE_FORMS)
        
    @classmethod
    def print_short_form(cls, length: Length) -> str:
        s = f"\n\t{cls.__name__}.print_short_form: "
        LengthValidator._handle_exception(LengthValidator.validate, s, length)
        return _print_short_form(length, cls.DEFAULT_SHORT_SQUARE_FORM)
        
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")