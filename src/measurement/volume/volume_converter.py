from .volume import Volume

from ..length import Length, Meter
from ..length import LengthValidator, MeterConverter


__all__ = [
    "VolumeConverter"
]


class VolumeConverter(MeterConverter):
    
    @classmethod
    def _convert(cls, input: Meter, output: type = Meter) -> Meter:    
        first = input.SIZE_SI ** 3
        second = output.SIZE_SI ** 3
        return output(input.value * first / second)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> str:
        s = f"\n\t{cls.__name__}.convert: "
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        LengthValidator._handle_exception(LengthValidator.validate, s, input)
        LengthValidator._handle_exception(LengthValidator.validate_type_of_type, s, output, meter_types)
        return Volume.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Meter) -> str:
        s = f"\n\t{cls.__name__}.auto_convert: "
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, value, Meter)
        value = cls._decrease_meter_type(value) \
            if value <= 1 else \
                cls._increase_meter_type(value)
        return Volume.print_full_form(value)