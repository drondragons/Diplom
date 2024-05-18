from .meter import *
from ..converter import Converter
from .meter_validator import MeterValidator


__all__ = [
    "MeterConverter",
]


class MeterConverter(Converter):
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> Meter:
        exception, message = MeterValidator.validate_type(input, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        if output is Meter:
            message = f"Недопустимый тип '{output.__name__}'! Ожидался тип {MeterValidator.format_union_types(output)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        return output(input.value * input.SIZE_SI / output.SIZE_SI)
    
    @classmethod
    def auto_convert(cls, value: Meter) -> Meter:
        exception, message = MeterValidator.validate_type(input, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)