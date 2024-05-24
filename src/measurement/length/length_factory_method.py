import random
from types import NoneType
from typing import Type

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

from ...value_objects import Real, RealFactoryMethod, RealValidator
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
        length_type: Type = NoneType
    ) -> Length:
        s = f"\n\t{cls.__name__}.generate: "
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, is_int, bool)
        handler(Validator.validate_object_type, s, minimum, REAL_TYPES)
        handler(Validator.validate_object_type, s, maximum, REAL_TYPES)
        
        minimum = Real(minimum)
        maximum = Real(maximum)
        handler(RealValidator._validate_interval, s, minimum, 0)
        handler(RealValidator._validate_interval, s, maximum, 0)
        
        subclasses = [Meter, Length] + [subclass for subclass in Meter.__subclasses__()]
        meter_types = [NoneType] + subclasses
        handler(Validator.validate_type_of_type, s, length_type, meter_types)
    
        length_type = random.choice(subclasses) if length_type == NoneType else length_type
        return length_type(super().generate(minimum, maximum, is_int))
    

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