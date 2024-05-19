from .volume import Volume

from ..length import LengthValidator
from ..length import Meter, LengthConverter
from ..length.length import METER_CLASSES


__all__ = [
    "VolumeConverter"
]


class VolumeConverter(LengthConverter):
    
    @classmethod
    def _convert(cls, input: Meter, output: type = Meter) -> Meter:
        exception, message = LengthValidator.validate_type(input, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        if output not in METER_CLASSES:
            message = f"Недопустимый тип '{output.__name__}'! Ожидался тип {LengthValidator.format_union_types(output)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        first = input.SIZE_SI ** 3
        second = output.SIZE_SI ** 3
        
        return output(input.value * first / second)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> str:
        return Volume.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Meter) -> str:
        exception, message = LengthValidator.validate_type(value, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        value = cls.decrease_meter_type(value) \
            if value <= 1 else \
                cls.increase_meter_type(value)
        return Volume.print_full_form(value)