import random
from types import NoneType
from typing import Type

from .flat import Flat

from ... import REAL_TYPES
from ...validators import Validator
from ...measurement import Length, Meter, Ruble
from ...measurement import MoneyFactoryMethod, LengthFactoryMethod
from ...value_objects import Title
from ...factory_method import FactoryMethod


__all__ = [
    "FlatFactoryMethod",
]


class FlatFactoryMethod(FactoryMethod):
    
    DEFAULT_MINIMUM_VALUE = MoneyFactoryMethod.DEFAULT_MINIMUM_VALUE
    DEFAULT_MAXIMUM_VALUE = FactoryMethod.DEFAULT_MAXIMUM_VALUE
    
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
        minimum: REAL_TYPES = DEFAULT_MINIMUM_VALUE,
        maximum: REAL_TYPES = DEFAULT_MAXIMUM_VALUE,
        is_int: bool = True,
        length_type: Type = NoneType,
        money_type: Type = NoneType,
        title: str | Title = Flat.DEFAULT_TITLE
    ) -> Flat:
        s = f"\n\t{cls.__name__}.generate: "
        
        footage_types = [Length, Meter]
        handler = Validator._handle_exception
        handler(Validator.validate_type_of_type, s, length_type, footage_types + [NoneType])
        
        length_type = random.choice(footage_types) if length_type == NoneType else length_type
        generator = LengthFactoryMethod.generate
        footage = generator(minimum, maximum, is_int, length_type)
        
        generator = MoneyFactoryMethod.generate
        price_per_meter = generator(minimum, maximum, is_int, money_type)
        
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, title, str | Title)
        
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
        generator(100_000, 200_000, True, Ruble)
        
        return Flat(footage, Ruble(Flat.DEFAULT_PRICE_PER_METER), title)