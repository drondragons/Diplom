from abc import abstractmethod

from .meter import Meter
from .length import Length
from .length_validator import LengthValidator

from ..converter import Converter


__all__ = [
    "LengthConverter",
    "MeterConverter",
]


class LengthConverter(Converter):
    
    @classmethod
    def _convert(cls, input: Length, output: type = Length) -> Meter:
        return output(input.value * input.SIZE_SI / output.SIZE_SI)
    
    @classmethod
    @abstractmethod
    def auto_convert(cls, value: Meter) -> Meter:
        message = f"\n\t{cls.__name__}: "
        message += "Нереализованный абстрактный статический метод auto_convert!"
        raise NotImplementedError(message)


class MeterConverter(LengthConverter):
    
    @classmethod
    def _find_correct_meter_type(cls, values: list[Meter]) -> Meter:
        result = [value for value in values if 1 <= value]
        return min(result, key = lambda meter: meter.value) \
            if result else \
                max(values, key = lambda meter: meter.value)
    
    @classmethod
    def _increase_meter_type(cls, value: Meter) -> Meter:
        meter_types = [Meter] + [subclass for subclass in Meter.__subclasses__()]
        result = [
            cls._convert(value, meter)
                for meter in meter_types
                    if 0 < cls._convert(value, meter).value <= value.value
        ]
        return cls._find_correct_meter_type(result)
        
    @classmethod
    def _decrease_meter_type(cls, value: Meter) -> Meter:
        meter_types = [Meter] + [subclass for subclass in Meter.__subclasses__()]
        result = [
            cls._convert(value, meter)
                for meter in meter_types
                    if value.value <= cls._convert(value, meter).value < 1000
        ]
        return cls._find_correct_meter_type(result)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> Meter:
        s = f"\n\t{cls.__name__}.convert: "
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, input, Meter)
        LengthValidator._handle_exception(LengthValidator.validate_type_of_type, s, output, meter_types)
        return cls._convert(input, output)
    
    @classmethod
    def auto_convert(cls, value: Meter) -> Meter:
        s = f"\n\t{cls.__name__}.auto_convert: "
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, value, Meter)
        return cls._decrease_meter_type(value) \
            if value <= 1 else \
                cls._increase_meter_type(value)