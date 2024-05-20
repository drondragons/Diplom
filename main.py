# from src import Validator, NumberValidator, FractionValidator, IntValidator, DecimalValidator, ListValidator

# from fractions import Fraction
# from decimal import Decimal
# import math
# import sys
# from src import Real, OPERATORS

# from src.measurement import Meter

# from src.factory_method import RealFactoryMethod

# def main() -> None:    
#     # IntValidator()
#     ListValidator()
    
#     # Real(123).__index__()
#     # ~Real()
#     # str() == Real()
#     # Real() == str()
#     # Real(str())
#     print(10 - Real(1))
#     print(Real(1) - 10)
#     print(Real(10) - Real(1))
#     # print(Real(10) - str())
#     # print(str() - Real(10))
#     # print(Real(10) @ 1)
#     # print(10 @ Real(1))
#     # print(str() @ Real())
#     print(dir(Real))
#     print(Real().__add__(134894))
#     try:
#         # Real().__len__
#         print(Meter(Real(122930942)))
    
#     except Exception as e:
#         print(e)
    
    
#     Meter()
    
#     # e, m = ListValidator.validate([str(), 1], str, 1, 2)
#     # print(e, m)
    
#     # e, m = FractionValidator.validate(Fraction(1), 0, 1)
#     # print(e, m)
    
#     # print("Meter")
#     # for i in range(20):
#     #     print(Meter(Fraction(i)))
#     # meter = Meter(2)
#     # print(meter)
    
#     # t = [dir(int), dir(float), dir(Decimal), dir(Fraction)]
#     # for item in t:
#     #     print("__divmod__" in item)
        
#     # print(math.floor(Meter(Fraction(12323/234))))
#     # print(math.ceil(Meter(Fraction(12323/234))))
#     # print(math.trunc(Meter(Fraction(12323/234))))
#     # print(Meter(Fraction(12323/234)).__int__())
#     # print(Meter(Fraction(12323/234)).__float__())
#     # print(int(1).__float__())
#     # print(float(1.12434923).__float__())
#     # print(int(1).__sizeof__())
#     # print(float(1.23).__sizeof__())
#     # print(sys.getsizeof(1))
#     # print(sys.getsizeof(1.9245))
#     # print(sys.getsizeof(Meter(Fraction(123/243))))
#     # print(Meter(Fraction(123/243)).__sizeof__())
#     # print(sys.getsizeof(object()))
    
#     # # print(len(int(1)))
    
#     # print(1 == Real(1))
#     # print(Real(1) == 1)
#     # print(1 != Real(1))
#     # print(Real(1) != 1)
#     # print(1 < Real(1))
#     # print(Real(1) < 1)
#     # print(1 > Real(1))
#     # print(Real(1) > 1)
#     # print(1 <= Real(1))
#     # print(Real(1) <= 1)
#     # print(1 >= Real(1))
#     # print(Real(1) >= 1)
    
#     # # print(~Real(1))
#     # # print(Real(1).__inv__())
#     # # print(Real(1).__invert__())
#     # print(Real(1) + Real(1.23))
#     # print(Real(1) + 1.99345)
#     # print(1.2343 + Real(1234))
#     # # print(Real(1) + str())
#     # # print(str() + Real(12))
#     # # print(Real(1) + str())
    
#     # print(OPERATORS)
    
#     # # print(divmod(Fraction(10), 6))
#     # print(divmod(Real(10), Real(6)))
#     # print(divmod(Real(10), 6))
#     # print(divmod(10, Real(6)))
    
#     # print(1 - Real(4))
#     # print(Real(4) - 1)
    
#     # # print(Real(4) - str())
#     # print(Real(3) ** 2)
#     # print(2 ** Real(3))
    
#     # print(Real(3) @ 1)
#     # # '__class__',
#     # '__delattr__', '__dir__', '__doc__',
#     # '__getattribute__',
#     # '__getnewargs__', '__init_subclass__',
#     # '__new__', 
#     # '__reduce__', '__reduce_ex__', 
#     # '__setattr__', 
#     # '__sizeof__', '__subclasshook__',
#     # 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator',
#     # 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'

# from src import Validator, IntValidator
# from src import MeterConverter, Meter, KiloMeter, CentiMeter, LengthFactoryMethod, KiloMeterFactoryMethod
# from src import Real, RealFactoryMethod, MeterConverter, Length
# from src import Money, Dollar, Ruble, Square, SquareConverter, Volume, VolumeConverter
# from src import Title
# from src import Line, LineFactoryMethod
# from src import Rectangle
# import math
# from src import Length, Meter, KiloMeter, NanoMeter, DeciMeter, MilliMeter, LengthValidator, LengthConverter, MeterConverter
# from src.real import Real, RealValidator, RealFactoryMethod
# from src.factory_method import RealFactoryMethod
# from src.measurement import Meter, KiloMeter
# from src import LengthFactoryMethod, Money, Ruble, Dollar, Euro, MoneyFactoryMethod

from src import Validator, StringValidator, NumberValidator, ListValidator
from src import Title, TitleValidator
from src import Real, RealValidator, RealFactoryMethod
from src import Length, LengthValidator, LengthFactoryMethod, MeterConverter, KiloMeter, Meter

from src import MoneyValidator, Money, MoneyFactoryMethod, Ruble, Dollar, Euro
from src import Square, SquareConverter
from src import Volume, VolumeConverter
# from src import Line

def main() -> None:
    print(MoneyValidator.validate(Ruble(1), int(), int()))
    
    for _ in range(10):
        print(MoneyFactoryMethod.generate())
        print(LengthFactoryMethod.generate())
    print(Dollar(10))
    
    print(Dollar(10) + Euro(15) * Money(3))
    # print(Ruble(10) == Ruble(10))
    
    print(Square.print_short_form(Meter(10000000)))
    print(Meter(10) + KiloMeter(89))
    
    print(SquareConverter.auto_convert(Meter(1000000)))
    print(Volume.print_full_form(Meter(10000)))
    print(VolumeConverter.auto_convert(Meter(0.0001)))
    
    line = Line(Meter(789023))
    print(line)
    print(line.__repr__())
    for _ in range(10):
        print(LineFactoryMethod.generate())
        
    r = Rectangle(Line(Meter(10)), Line(Meter(135)))
    print(r.square)
    print(r)
    print("-=-=-=-=-=-=-=--=-=--=-=-")
    
    
    meter = CentiMeter(KiloMeter(12))
    print(meter, meter.__repr__(), meter.print_short_form())
    kilometer = KiloMeter(KiloMeter(15))
    print(kilometer, kilometer.print_short_form())
    kilometer = Length(Meter(99))
    print(kilometer, kilometer.print_short_form())
    for i in range(1000, 1010):
        print(Square.print_full_form(Length(i)))
        print(Square.print_short_form(Length(i)))
        print(Square.print_full_form(KiloMeter(i)))
        print(Square.print_short_form(KiloMeter(i)))
        print(Volume.print_full_form(Length(i)))
        print(Volume.print_short_form(Length(i)))
        print(Volume.print_full_form(KiloMeter(i)))
        print(Volume.print_short_form(KiloMeter(i)))
    
    print(MeterConverter.auto_convert(KiloMeter(0.0002)))
    
    print(SquareConverter.auto_convert(KiloMeter(0.1)))
    print(SquareConverter.auto_convert(KiloMeter(0.01)))
    print(SquareConverter.auto_convert(Meter(0.001)))    
    print(SquareConverter.auto_convert(CentiMeter(0.0001)))
    print(VolumeConverter.auto_convert(CentiMeter(0.001)))
    print(Money(133))
    print(Money(78324))
    print(Dollar(8394))
    print(Ruble(192))
    
    # print(MeterConverter.convert(KiloMeter(Real(15)), CentiMeter))
    # print(MeterConverter.auto_convert(CentiMeter(Real(30000))))
    print(RealFactoryMethod.generate(Real(), Real(3)))
    for _ in range(10):
        print(LengthFactoryMethod.generate(2))
        print(KiloMeterFactoryMethod.generate(90, 500))
        
    print(MeterConverter.auto_convert(KiloMeter(0.0002)))
    # print(RealValidator.validate(Real(1), 10))
    # print(RealFactoryMethod.generate(100, 90))
    # print(Meter(Real(1)))
    
    # meter = Meter(Real(1.2348743))
    # print(meter.__floor__())
    # print(meter)
     
    # kilometer = KiloMeter(Real(-38924))
    # print(kilometer)
    # print(kilometer.class_name)
    # print(kilometer != 38924)
    # kilometer.jknsdjv
    
    

if __name__ == "__main__":
    main()