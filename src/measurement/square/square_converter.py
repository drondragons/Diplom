from .square import Square

from ..length import Length, Meter, LengthValidator, LengthConverter


__all__ = [
    "SquareConverter"
]


class SquareConverter(LengthConverter):
    
    @classmethod
    def _convert(cls, input: Meter, output: type = Meter) -> Meter:    
        first = input.SIZE_SI ** 2
        second = output.SIZE_SI ** 2
        
        return output(input.value * first / second)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> str:
        s = f"\n\t{cls.__name__}.convert: "
        LengthValidator._handle_exception(LengthValidator.validate, s, input)
        LengthValidator._handle_exception(LengthValidator.validate_type, s, output)
        
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        if output not in meter_types:
            message = f"Недопустимый тип {LengthValidator.format_union_types(output)}! Ожидался тип {LengthValidator.format_union_types(meter_types)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        return Square.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Meter) -> str:
        s = f"\n\t{cls.__name__}.auto_convert: "
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, value, Meter)
        value = cls._decrease_meter_type(value) \
            if value <= 1 else \
                cls._increase_meter_type(value)
        return Square.print_full_form(value)