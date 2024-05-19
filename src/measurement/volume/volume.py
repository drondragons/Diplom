from ..length import Length, LengthValidator

from ... import format_plural_form


__all__ = [
    "Volume",
]


class Volume:
    
    DEFAULT_SHORT_SQUARE_FORM = "куб."
    DEFAULT_SQUARE_FORMS = [
        ("кубическая", "кубический"),
        ("кубические", "кубических"),
        ("кубических", "кубических"),
    ]
    
    @classmethod
    def print_full_form(cls, length: Length) -> str:
        exception, message = LengthValidator.validate(length)
        if exception:
            raise exception(f"\n\t{cls.__name__}.print_form: " + message)
        square_forms = [form[0] for form in cls.DEFAULT_SQUARE_FORMS] \
            if type(length) == Length else \
                [form[1] for form in cls.DEFAULT_SQUARE_FORMS]
        form = format_plural_form(length.value.value, square_forms)
        words = str(length)[len(str(length.value)) + 1:]
        return f"{length.value} {form} {words}"
    
    @classmethod
    def print_short_form(cls, length: Length) -> str:
        exception, message = LengthValidator.validate(length)
        if exception:
            raise exception(f"\n\t{cls.__name__}.print_form: " + message)
        words = str(length.print_short_form())[len(str(length.value)) + 1:]
        return f"{length.value} {cls.DEFAULT_SHORT_SQUARE_FORM} {words}"
    
    def __new__(self) -> None:
        raise TypeError(f"\n\t{self.__name__}: Экземпляры класса '{self.__name__}' не могут быть созданы!")