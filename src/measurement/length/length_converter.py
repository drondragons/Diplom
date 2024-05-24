from typing import Type, List

from .meter import Meter
from .length import Length

from .. import _convert
from ..converter import Converter

from ...validators import Validator


__all__ = [
    "LengthConverter",
    "MeterConverter",
]


class LengthConverter(Converter):
    
    @classmethod
    def _convert(cls, input: Length, output: Type = Length) -> Length:
        return output(input.value) \
            if type(input) == Length or type(output) == Length else \
                output(_convert(input.value, input.SIZE_SI, output.SIZE_SI))


class MeterConverter(LengthConverter):
    
    @classmethod
    def get_meter_types(cls) -> List[Type]:
        return [Meter] + [subclass for subclass in Meter.__subclasses__()]
    
    @classmethod
    def _increase_meter_type(cls, value: Meter) -> Meter:
        return cls._increase_type(value, cls.get_meter_types())
        
    @classmethod
    def _decrease_meter_type(cls, value: Meter) -> Meter:
        return cls._decrease_type(value, cls.get_meter_types())
    
    @classmethod
    def convert(cls, input: Length, output: Type = Length) -> Length:
        s = f"\n\t{cls.__name__}.convert: "
        meter_types = cls.get_meter_types() + [Length]
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, input, meter_types)
        handler(Validator.validate_type_of_type, s, output, meter_types)
        
        return cls._convert(input, output)
    
    @classmethod
    def _auto_convertation(cls, value: Length) -> Length:
        return cls._auto_convert(
            value,
            Length,
            cls._decrease_meter_type,
            cls._increase_meter_type
        )
    
    @classmethod
    def auto_convert(cls, value: Length) -> Length:
        s = f"\n\t{cls.__name__}.auto_convert: "
        meter_types = cls.get_meter_types() + [Length]
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, value, meter_types)
        
        return cls._auto_convertation(value)
                