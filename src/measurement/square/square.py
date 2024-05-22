from ..length import Length, LengthValidator

from ... import _format_plural_form


__all__ = [
    "Square",
]


class Square:
    
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
        square_forms = [form[0] for form in cls.DEFAULT_SQUARE_FORMS] \
            if type(length) == Length else \
                [form[1] for form in cls.DEFAULT_SQUARE_FORMS]
        form = _format_plural_form(length.value.value, square_forms)
        words = str(length)[len(str(length.value)) + 1:]
        return f"{length.value} {form} {words}"
    
    @classmethod
    def print_short_form(cls, length: Length) -> str:
        s = f"\n\t{cls.__name__}.print_short_form: "
        LengthValidator._handle_exception(LengthValidator.validate, s, length)
        words = str(length.print_short_form())[len(str(length.value)) + 1:]
        return f"{length.value} {cls.DEFAULT_SHORT_SQUARE_FORM} {words}"
    
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")