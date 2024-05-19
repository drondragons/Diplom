from abc import abstractmethod

from .length import Meter
from .length import METER_CLASSES
from .length_validator import LengthValidator

from ..converter import Converter


__all__ = [
    "LengthConverter",
    "MeterConverter",
]


class LengthConverter(Converter):
    
    @classmethod
    def find_correct_meter_type(cls, values: list[Meter]) -> Meter:
        result = [value for value in values if 1 <= value]
        return min(result) if result else max(values)
    
    @classmethod
    def increase_meter_type(cls, value: Meter) -> Meter:
        meter_types = METER_CLASSES[:METER_CLASSES.index(type(value)) + 1]
        result = [
            cls._convert(value, meter)
                for meter in meter_types
                    if 0 < cls._convert(value, meter).value <= value.value
        ]
        return cls.find_correct_meter_type(result)
        
    @classmethod
    def decrease_meter_type(cls, value: Meter) -> Meter:
        meter_types = METER_CLASSES[METER_CLASSES.index(type(value)):]
        result = [
            cls._convert(value, meter)
                for meter in meter_types
                    if value.value <= cls._convert(value, meter).value < 1000
        ]
        return cls.find_correct_meter_type(result)
    
    @classmethod
    @abstractmethod
    def auto_convert(cls, value: Meter) -> Meter:
        raise NotImplementedError(f"\n\t{cls.__name__}: Нереализованный абстрактный статический метод auto_convert!")


class MeterConverter(LengthConverter):
    
    @classmethod
    def _convert(cls, input: Meter, output: type = Meter) -> Meter:
        exception, message = LengthValidator.validate_type(input, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        if output not in METER_CLASSES:
            message = f"Недопустимый тип '{output.__name__}'! Ожидался тип {LengthValidator.format_union_types(output)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        return output(input.value * input.SIZE_SI / output.SIZE_SI)
    
    @classmethod
    def convert(cls, input: Meter, output: type = Meter) -> Meter:
        return cls._convert(input, output)
    
    @classmethod
    def auto_convert(cls, value: Meter) -> Meter:
        exception, message = LengthValidator.validate_type(value, Meter)
        if exception:
            raise exception(f"\n\t{cls.__name__}.convert: " + message)
        return cls.decrease_meter_type(value) \
            if value <= 1 else \
                cls.increase_meter_type(value)