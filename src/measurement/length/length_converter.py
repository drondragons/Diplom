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
    def _find_correct_meter_type(cls, values: list[Meter]) -> Meter:
        result = [value for value in values if 1 <= value]
        return min(result) if result else max(values)
    
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
    @abstractmethod
    def auto_convert(cls, value: Meter) -> Meter:
        raise NotImplementedError(f"\n\t{cls.__name__}: Нереализованный абстрактный статический метод auto_convert!")


class MeterConverter(LengthConverter):
    
    @classmethod
    def _convert(cls, input: Meter, output: type = Meter) -> Meter:
        return output(input.value * input.SIZE_SI / output.SIZE_SI)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> Meter:
        s = f"\n\t{cls.__name__}.convert: "
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, input, Meter)
        LengthValidator._handle_exception(LengthValidator.validate_type, s, output)
        
        meter_types = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        if output not in meter_types:
            message = f"Недопустимый тип {LengthValidator.format_union_types(output)}! Ожидался тип {LengthValidator.format_union_types(meter_types)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        return cls._convert(input, output)
    
    @classmethod
    def auto_convert(cls, value: Meter) -> Meter:
        s = f"\n\t{cls.__name__}.auto_convert: "
        LengthValidator._handle_exception(LengthValidator.validate_object_type, s, value, Meter)
        return cls._decrease_meter_type(value) \
            if value <= 1 else \
                cls._increase_meter_type(value)