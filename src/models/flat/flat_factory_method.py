import random
from types import NoneType
from typing import Type

from .flat import Flat

from ... import REAL_TYPES
from ...validators import Validator
from ...measurement.length import Length, Meter, LengthFactoryMethod
from ...measurement.money import MoneyFactoryMethod, Ruble
from ...value_objects.title import Title
from ...value_objects.real import Real, RealValidator
from ...factory_method import FactoryMethod


__all__ = [
    "FlatFactoryMethod",
]


class FlatFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_FOOTAGE = Flat.MINIMUM_FOOTAGE.value
    DEFAULT_MAXIMUM_FOOTAGE = FactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    DEFAULT_MINIMUM_PRICE_PER_METER = Flat.MINIMUM_PRICE_PER_METER.value
    DEFAULT_MAXIMUM_PRICE_PER_METER = Ruble(200_000).value
    
    ROOM_FLAT_FOOTAGE = {
        1: (28, 33),
        2: (44, 53),
        3: (56, 65),
        4: (70, 77),
        5: (84, 96),
        6: (103, 109),
    }
    
    ROOM_FLAT_TITLE = {
        1: "Однокомнатная квартира",
        2: "Двухкомнатная квартира",
        3: "Трёхкомнатная квартира",
        4: "Четырёхкомнатная квартира",
        5: "Пятикомнатная квартира",
        6: "Шестикомнатная квартира",
    }
    
    @classmethod
    def generate(
        cls,
        minimum_footage: REAL_TYPES = DEFAULT_MINIMUM_FOOTAGE,
        maximum_footage: REAL_TYPES = DEFAULT_MAXIMUM_FOOTAGE,
        minimum_price_per_meter: REAL_TYPES = DEFAULT_MINIMUM_PRICE_PER_METER,
        maximum_price_per_meter: REAL_TYPES = DEFAULT_MAXIMUM_PRICE_PER_METER,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Flat.DEFAULT_TITLE
    ) -> Flat:
        s = f"\n\t{cls.__name__}.generate: "
        
        footage_types = [Length, Meter]
        handler = Validator._handle_exception
        handler(Validator.validate_type_of_type, s, length_type, footage_types + [NoneType])
        handler(Validator.validate_object_type, s, title, str | Title)
        
        minimum = cls.DEFAULT_MINIMUM_FOOTAGE
        handler(RealValidator.validate, s, Real(minimum_footage), minimum)
        handler(RealValidator.validate, s, Real(maximum_footage), minimum)
        
        minimum = cls.DEFAULT_MINIMUM_PRICE_PER_METER
        handler(RealValidator.validate, s, Real(minimum_price_per_meter), minimum)
        handler(RealValidator.validate, s, Real(maximum_price_per_meter), minimum)
        
        length_type = random.choice(footage_types) if length_type == NoneType else length_type
        generator = LengthFactoryMethod.generate
        footage = generator(minimum_footage, maximum_footage, is_int, length_type)
        
        generator = MoneyFactoryMethod.generate
        price_per_meter = generator(minimum_price_per_meter, maximum_price_per_meter, is_int, Ruble)
        
        return Flat(footage, price_per_meter, title)
    
    @classmethod
    def generate_one_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(1)
    
    @classmethod
    def generate_two_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(2)
    
    @classmethod
    def generate_three_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(3)
    
    @classmethod
    def generate_four_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(4)
    
    @classmethod
    def generate_five_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(5)
    
    @classmethod
    def generate_six_room_flat(cls) -> Flat:
        return cls.__generate_room_flat(6)
    
    @classmethod
    def __generate_room_flat(cls, room_amount: int) -> Flat:
        generator = LengthFactoryMethod.generate
        footage = generator(*cls.ROOM_FLAT_FOOTAGE[room_amount], True, Meter)
        
        title = cls.ROOM_FLAT_TITLE[room_amount]
        
        generator = MoneyFactoryMethod.generate
        price_per_meter = generator(100_000, 200_000, True, Ruble)
        
        return Flat(footage, price_per_meter, title)