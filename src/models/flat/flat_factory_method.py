import random
from types import NoneType
from typing import Type, List, Tuple

from .flat import Flat, Pavilion

from ... import REAL_TYPES
from ...validators import Validator, IntValidator
from ...measurement.length import Length, Meter, LengthFactoryMethod
from ...measurement.money import MoneyFactoryMethod, Ruble, Money
from ...value_objects.title import Title
from ...value_objects.real import Real, RealValidator
from ...factory_method import FactoryMethod


__all__ = [
    "FlatFactoryMethod",
    "PavilionFactoryMethod",
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
    
    FLATS_PERCENTAGE = {
        1: 0.3,
        2: 0.5,
        3: 0.2
    }
    
    @classmethod
    def _generate(
        cls,
        minimum_footage: REAL_TYPES = DEFAULT_MINIMUM_FOOTAGE,
        maximum_footage: REAL_TYPES = DEFAULT_MAXIMUM_FOOTAGE,
        minimum_price_per_meter: REAL_TYPES = DEFAULT_MINIMUM_PRICE_PER_METER,
        maximum_price_per_meter: REAL_TYPES = DEFAULT_MAXIMUM_PRICE_PER_METER,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Flat.DEFAULT_TITLE
    ) -> Tuple[Length, Money, Title]:
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
        
        return footage, price_per_meter, title
    
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
        return Flat(*cls._generate(
                minimum_footage,
                maximum_footage,
                minimum_price_per_meter,
                maximum_price_per_meter,
                is_int,
                length_type,
                title
            )
        )
    
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
    
    @classmethod
    def generate_flats(cls, minimum_flats_amount: int, maximum_flats_amount: int) -> List[Flat]:
        s = f"\n\t{cls.__name__}.generate_flats: "
    
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, minimum_flats_amount, int)
        handler(Validator.validate_object_type, s, maximum_flats_amount, int)
        handler(IntValidator.validate, s, minimum_flats_amount, 0)
        handler(IntValidator.validate, s, maximum_flats_amount, 0)
        
        new_minimum = min(minimum_flats_amount, maximum_flats_amount)
        new_maximum = max(minimum_flats_amount, maximum_flats_amount)
        value = random.randint(new_minimum, new_maximum)
        
        flats = list()
        for i in range(1, 4):
            flats.append(int(cls.FLATS_PERCENTAGE[i] * value))
        flats[0] += new_minimum - sum(flats)
        return cls.__generate_flats(*flats)
    
    @classmethod
    def __generate_flats(
        cls, 
        one_room_amount: int = 30,
        two_room_amount: int = 50,
        three_room_amount: int = 10
    ) -> List[Flat]:
        flats = list()
        for _ in range(one_room_amount):
            flats.append(cls.generate_one_room_flat())
        for _ in range(two_room_amount):
            flats.append(cls.generate_two_room_flat())
        for _ in range(three_room_amount):
            flats.append(cls.generate_three_room_flat())
        return flats
    
    
class PavilionFactoryMethod(FlatFactoryMethod):
    
    DEFAULT_MINIMUM_FOOTAGE = Pavilion.MINIMUM_FOOTAGE.value
    DEFAULT_MAXIMUM_FOOTAGE = FactoryMethod.DEFAULT_MAXIMUM_VALUE
    
    DEFAULT_MINIMUM_PRICE_PER_METER = Pavilion.MINIMUM_PRICE_PER_METER.value
    DEFAULT_MAXIMUM_PRICE_PER_METER = Ruble(10_000).value
    
    @classmethod
    def generate(
        cls,
        minimum_footage: REAL_TYPES = DEFAULT_MINIMUM_FOOTAGE,
        maximum_footage: REAL_TYPES = DEFAULT_MAXIMUM_FOOTAGE,
        minimum_price_per_meter: REAL_TYPES = DEFAULT_MINIMUM_PRICE_PER_METER,
        maximum_price_per_meter: REAL_TYPES = DEFAULT_MAXIMUM_PRICE_PER_METER,
        is_int: bool = True,
        length_type: Type = NoneType,
        title: str | Title = Pavilion.DEFAULT_TITLE
    ) -> Pavilion:
        return Pavilion(*cls._generate(
                minimum_footage,
                maximum_footage,
                minimum_price_per_meter,
                maximum_price_per_meter,
                is_int,
                length_type,
                title
            )
        )
        
    @classmethod
    def generate_pavilions(
        cls,
        minimum_pavilions_amount: int,
        maximum_pavilions_amount: int
    ) -> List[Pavilion]:
        s = f"\n\t{cls.__name__}.generate_pavilions: "
    
        handler = Validator._handle_exception
        handler(Validator.validate_object_type, s, minimum_pavilions_amount, int)
        handler(Validator.validate_object_type, s, maximum_pavilions_amount, int)
        handler(IntValidator.validate, s, minimum_pavilions_amount, 0)
        handler(IntValidator.validate, s, maximum_pavilions_amount, 0)
        
        new_minimum = min(minimum_pavilions_amount, maximum_pavilions_amount)
        new_maximum = max(minimum_pavilions_amount, maximum_pavilions_amount)
        value = random.randint(new_minimum, new_maximum)
        
        pavilions = list()
        for _ in range(value):
            pavilions.append(cls.generate())
        return pavilions