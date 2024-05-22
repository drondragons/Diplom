from typing import Type

from .square_printer import SquarePrinter

from ..length import Length, Meter
from ..length import LengthValidator, MeterConverter


__all__ = [
    "SquareConverter"
]


class SquareConverter(MeterConverter):
    
    @classmethod
    def _convert(cls, input: Length, output: Type = Length) -> Length:
        if type(input) == Length or type(output) == Length:
            return output(input.value) 
        first = input.SIZE_SI ** 2
        second = output.SIZE_SI ** 2
        return output(input.value * first / second)
    
    @classmethod
    def convert(cls, input: Length, output: Type = Length) -> str:
        s = f"\n\t{cls.__name__}.convert: "
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, input, meter_types)
        LengthValidator._handle_exception(LengthValidator.validate_type_of_type, s, output, meter_types)
        return SquarePrinter.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Meter) -> str:
        s = f"\n\t{cls.__name__}.auto_convert: "
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, value, meter_types)
        if type(value) != Length:
            value = cls._decrease_meter_type(value) \
                if value <= 1 else \
                    cls._increase_meter_type(value)
        return SquarePrinter.print_full_form(value)