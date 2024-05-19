import random

from .length import Length
from .meter import Meter
from .kilometer import KiloMeter
from .nanometer import NanoMeter
from .decimeter import DeciMeter
from .pikometer import PikoMeter
from .millimeter import MilliMeter
from .centimeter import CentiMeter
from .femtometer import FemtoMeter
from .micrometer import MicroMeter

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
    
    DEFAULT_MINIMUM_VALUE = Length.DEFAULT_LENGTH_VALUE
    DEFAULT_MAXIMUM_VALUE = RealFactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    @classmethod
    def generate(
        cls,
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: type = None
    ) -> Length:
        minimum = Length(minimum)
        maximum = Length(maximum)
        
        exception, message = Validator.validate_type(is_int, bool)
        if exception:
            message = f"Недопустимый тип '{type(is_int).__name__}'! Ожидался тип bool!"
            raise TypeError(f"\n\t{cls.__name__}.generate: " + message)
        
        if not isinstance(length_type, type) and length_type != None:
            message = f"Ожидался тип, а не объект {length_type.__class__.__name__}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        meter_types = [Length, Meter] + [subclass for subclass in Meter.__subclasses__()]
        if length_type not in (meter_types + [None]):
            message = f"Недопустимый тип '{length_type.__name__}'! Ожидался тип {Validator.format_union_types(meter_types)}!"
            raise TypeError(f"\n\t{cls.__name__}.convert: " + message)
        
        length_type = random.choice(meter_types) if not length_type else length_type
        return length_type(super().generate(minimum.value, maximum.value, is_int))
    

class MeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> Meter:
        return super().generate(minimum, maximum, is_int, Meter)
    
    
class NanoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> NanoMeter:
        return super().generate(minimum, maximum, is_int, NanoMeter)
    
    
class DeciMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> DeciMeter:
        return super().generate(minimum, maximum, is_int, DeciMeter)
    
    
class KiloMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> KiloMeter:
        return super().generate(minimum, maximum, is_int, KiloMeter)
    

class PikoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> PikoMeter:
        return super().generate(minimum, maximum, is_int, PikoMeter)
    
    
class MilliMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> MilliMeter:
        return super().generate(minimum, maximum, is_int, MilliMeter)
    
    
class CentiMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> CentiMeter:
        return super().generate(minimum, maximum, is_int, CentiMeter)
    

class FemtoMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> FemtoMeter:
        return super().generate(minimum, maximum, is_int, FemtoMeter)
    

class MicroMeterFactoryMethod(LengthFactoryMethod):
    
    @classmethod
    def generate(
        cls, 
        minimum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MINIMUM_VALUE, 
        maximum: REAL_TYPES = LengthFactoryMethod.DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
    ) -> MicroMeter:
        return super().generate(minimum, maximum, is_int, MicroMeter)