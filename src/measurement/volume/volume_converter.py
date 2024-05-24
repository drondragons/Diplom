from typing import Type

from .volume_printer import VolumePrinter

from .. import _convert
from ..length import Length
from ..length import MeterConverter

from ...validators import Validator


__all__ = [
    "VolumeConverter"
]


class VolumeConverter(MeterConverter):
    
    @classmethod
    def _convert(cls, input: Length, output: Type = Length) -> Length: 
        if type(input) == Length or type(output) == Length:
            return output(input.value)
        return output(_convert(input.value, input.SIZE_SI ** 3, output.SIZE_SI ** 3))
    
    @classmethod
    def convert(cls, input: Length, output: Type = Length) -> str:
        s = f"\n\t{cls.__name__}.convert: "
        meter_types = [Length] + cls.get_meter_types()
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, input, meter_types)
        handler(Validator.validate_type_of_type, s, output, meter_types)
        
        return VolumePrinter.print_full_form(cls._convert(input, output))

    @classmethod
    def auto_convert(cls, value: Length) -> str:
        s = f"\n\t{cls.__name__}.auto_convert: "
        meter_types = [Length] + cls.get_meter_types()
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, value, meter_types)
        
        return VolumePrinter.print_full_form(cls._auto_convertation(value))