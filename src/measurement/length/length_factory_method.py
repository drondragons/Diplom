from .length import *
from .length import METER_CLASSES

from .. import REAL_TYPES

from ...real import RealFactoryMethod

from ...validators import Validator


__all__ = [
    "LengthFactoryMethod",
    "MeterFactoryMethod",
    "NanoMeterFactoryMethod",
    "DeciMeterFactoryMethod",
    "KiloMeterFactoryMethod",
    "PikoMeterFactoryMethod",
    "MilliMeterFactoryMethod",
    "CentiMeterFactoryMethod",
    "FemtoMeterFactoryMethod",
    "MicroMeterFactoryMethod",
]


class LengthFactoryMethod(RealFactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = 0
    
    @classmethod
    def generate(
        cls,
        minimum: Length | REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: type = Length
    ) -> Length:
        minimum = Length(minimum)
        maximum = Length(maximum)
        
        if length_type not in METER_CLASSES and length_type != Length:
            message = f"Недопустимый тип '{length_type.__name__}'! Ожидался тип {Validator.format_union_types(length_type)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        return length_type(super().generate(minimum.value, maximum.value, is_int))
    

class MeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> Meter:
        return super().generate(minimum, maximum, is_int, Meter)
    
    
class NanoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> NanoMeter:
        return super().generate(minimum, maximum, is_int, NanoMeter)
    
    
class DeciMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> DeciMeter:
        return super().generate(minimum, maximum, is_int, DeciMeter)
    
    
class KiloMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> KiloMeter:
        return super().generate(minimum, maximum, is_int, KiloMeter)
    

class PikoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> PikoMeter:
        return super().generate(minimum, maximum, is_int, PikoMeter)
    
    
class MilliMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> MilliMeter:
        return super().generate(minimum, maximum, is_int, MilliMeter)
    
    
class CentiMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> CentiMeter:
        return super().generate(minimum, maximum, is_int, CentiMeter)
    

class FemtoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> FemtoMeter:
        return super().generate(minimum, maximum, is_int, FemtoMeter)
    

class MicroMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: Length | REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: Length | REAL_TYPES = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> MicroMeter:
        return super().generate(minimum, maximum, is_int, MicroMeter)