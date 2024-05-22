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
from src import Length, LengthValidator, LengthFactoryMethod, MeterConverter, KiloMeter, Meter, CentiMeter

from src import MoneyValidator, Money, MoneyFactoryMethod, Ruble, Dollar, Euro
from src import Square, SquareConverter
from src import Volume, VolumeConverter
from src import Line, LineFactoryMethod, Rectangle

from types import NoneType
from src import Validator

def main() -> None:
    print(Real(10) * 10 + Real(8) / 7 / Real(0.1) ** Real(2))
    print(10 * 10 + 8 / 7 / 0.1 ** 2)
    
    print(Dollar(10) + Euro(10) + Ruble(10) + Dollar(10) + Euro(10))
    
    
    # print(Line(Meter(10000)))
    # print(Line(Meter(10000)))
    # print(Meter(10000))
    # print(Meter(0.1))
    # print(Line(Meter(1000)))
    # print(Line(CentiMeter(1000)))
    # print(Line(Meter(0.001)))
    print("_+_+_+_+_+_+_+_+_+__+_+_+_+_+_+__")
    # print(Line(Meter(1000)))
    print(Line(Meter(100_000)))
    print(Line(Meter(0.2)))
    print(Line(Meter(0.0000000000000001)))
    print(Rectangle(Line(Meter(100)), Line(Meter(0.000_1))))
    # print(Line(Meter(0.1)))
    # print(Line(CentiMeter(1000)))
    # print(Line(Length(10000)))
    # print(Line(KiloMeter(10000)))
    # print(Line(CentiMeter(10000)))

if __name__ == "__main__":
    main()