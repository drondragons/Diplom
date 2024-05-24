from src import Validator, StringValidator, NumberValidator, ListValidator
from src import Title, TitleValidator
from src import Real, RealValidator, RealFactoryMethod
from src import Length, LengthValidator, LengthFactoryMethod, MeterConverter, KiloMeter, Meter, CentiMeter

from src import MoneyValidator, Money, MoneyFactoryMethod, Ruble, Dollar, Euro, DeciMeter
from src import SquarePrinter, SquareConverter, MoneyConverter, Yuan
from src import VolumePrinter, VolumeConverter, ParallelepipedFactoryMethod
from src import Line, LineFactoryMethod, Rectangle, CubeFactoryMethod, Square
from src import RectangleFactoryMethod, SquareFactoryMethod, NanoMeter, ParallelepipedBuilder

from types import NoneType
from src import Validator
from src import Money, MoneyConverter, MoneyFactoryMethod, MoneyValidator, Ruble, Dollar
from src import LineValidator, LineBuilder, RectangleBuilder, SquareBuilder, Parallelepiped

from src import Flat, Price, PriceFactoryMethod, FlatFactoryMethod, FlatBuilder

def main() -> None:
    print(Dollar(Real(13)))
    print(MoneyConverter.convert(Ruble(100), Ruble))
    print(MoneyFactoryMethod.generate())
    print(MoneyValidator.validate(Money(1), int(), int(1)))
    
    
    
    print(RectangleFactoryMethod.generate())
    
    print(MeterConverter.auto_convert(Length(10)))
    print(MeterConverter.auto_convert(Meter(1)))
    print(Line(Meter(1000)))
    print(MoneyConverter.auto_convert(Ruble(100)))
    
    
    builder = LineBuilder()
    line = builder.add_length(CentiMeter(100)).build()
    print(line)
    line_2 = builder.add_length(Meter(1)).build()
    print(line)
    print(line_2)
    print(line == line_2)
    
    rect_builder = RectangleBuilder()
    rect_1 = rect_builder.add_length(10).add_width(10).add_title("Прикол").build()
    print(rect_1)
    rect_2 = rect_builder.add_length(CentiMeter(1000)).add_width(CentiMeter(1000)).add_title("Прикол_2").build()
    print(rect_1)
    print(rect_2)
    print(rect_1 == rect_2)
    
    print(Square())
    
    suqare_builder = SquareBuilder()
    sq_1 = suqare_builder.add_side(100).add_title("Тест").build()
    print(sq_1)
    sq_2 = suqare_builder.add_side(Meter(10)).build()
    print(sq_1)
    print(sq_2)
    print(sq_1 == sq_2)
    
    print(rect_2 == sq_2)
    
    
    q = Parallelepiped()
    print(q == Parallelepiped())
    
    print(CubeFactoryMethod.generate())
    
    builder = ParallelepipedBuilder()
    p_1 = builder.add_width(CentiMeter(10)).add_length(CentiMeter(19)).add_height(CentiMeter(1)).build()
    print(p_1)
    print(CentiMeter(10) * Length(19) * KiloMeter(1))
    print(MeterConverter.auto_convert(Meter(1000)))
    
    print(MoneyConverter.convert(Ruble(100), Dollar))
    print(MoneyConverter.convert(Money(100), Dollar))
    print(MoneyConverter.convert(Yuan(100), Dollar))
    print(MoneyConverter.auto_convert(Ruble(100)))
    
    flat = Flat(Meter(50), Ruble(100_000))
    print(flat)
    print(flat.__repr__())
    
    print(Price(Euro(10), "Цена за метр"))
    print(PriceFactoryMethod.generate())
    print(FlatFactoryMethod.generate(18, 19))
    
    builder = FlatBuilder()
    flat = builder.build()
    print(flat)
    
    print(FlatFactoryMethod.generate_one_room_flat())
    print(FlatFactoryMethod.generate_two_room_flat())
    print(FlatFactoryMethod.generate_three_room_flat())
    print(FlatFactoryMethod.generate_four_room_flat())
    print(FlatFactoryMethod.generate_five_room_flat())
    print(FlatFactoryMethod.generate_six_room_flat())
    
    
if __name__ == "__main__":
    main()