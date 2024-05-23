from typing import Type

from .square_printer import SquarePrinter

from ..length import Length, Meter
from ..length import MeterConverter

from ...validators import Validator


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
        handler = Validator._handle_exception
        meter_types = [Length] + cls.get_meter_types()
        handler(Validator.validate_object_type, s, input, meter_types)
        handler(Validator.validate_type_of_type, s, output, meter_types)
        return SquarePrinter.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Meter) -> str:
        s = f"\n\t{cls.__name__}.auto_convert: "
        handler = Validator._handle_exception
        meter_types = [Length] + cls.get_meter_types()
        handler(Validator.validate_object_type, s, value, meter_types)
        return SquarePrinter.print_full_form(cls._auto_convert(value))