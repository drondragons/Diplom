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
from src import Real, RealValidator, RealFactoryMethod, FemtoMeter
from src import Length, LengthValidator, LengthFactoryMethod, MeterConverter, KiloMeter, Meter, CentiMeter

from src import MoneyValidator, Money, MoneyFactoryMethod, Ruble, Dollar, Euro, DeciMeter
from src import SquarePrinter, SquareConverter
from src import VolumePrinter, VolumeConverter
from src import Line, LineFactoryMethod, Rectangle
from src import RectangleFactoryMethod, SquareFactoryMethod, NanoMeter

from types import NoneType
from src import Validator

def main() -> None:
    # print(Money(10) + Ruble(10) + Dollar(10))
    # print(CentiMeter(10) * KiloMeter(0.005))
    # print(Length(10) + Meter(10) + CentiMeter(10) * KiloMeter(0.005))
    # print(SquarePrinter.print_full_form(Length(10)))
    # print(VolumePrinter.print_full_form(Length(10)))
    # print(MeterConverter.convert(Length(10), KiloMeter))
    # print(MeterConverter.auto_convert(KiloMeter(0.001)))
    # # print(Length(10))
    # # print(Line(Length(10)))
    # print(Rectangle(Line(Length(10)), Line(Length(10))))
    # print(Meter(10) == Length(10))
    # print(CentiMeter(10) + Length(15))
    # print(Length(10) + CentiMeter(10))
    # print(MeterConverter.convert(Length(0.01), CentiMeter))
    # print(CentiMeter(0.01) + Meter(14) / Length(1) * 7 + Meter(12) +\
        # CentiMeter(23) * KiloMeter(0.4))
    # print(SquareConverter.auto_convert(Length(49) * Meter(53)))
    # print(Rectangle(Line(Length(49)), Line(Meter(53))))
    # print(Rectangle(Line(DeciMeter(9.9)), Line(Length(22))))
    # print(Rectangle(Line(CentiMeter(1.1)), Line(Length(78))))
    # print(Rectangle(Line(Length(94)), Line(DeciMeter(8.6))))
    # print(Rectangle(Line(Length(1)), Line(DeciMeter(9.8))))
    # print(Rectangle(Line(Length(14)), Line(NanoMeter(36))))
    # print(Rectangle(Line(Length(3)), Line(Meter(4.9))))
    # print(Rectangle(Line(Meter(4.9)), Line(Length(3))))
    # for _ in range(100):
    # print(RectangleFactoryMethod.generate())
    rect = RectangleFactoryMethod.generate()
    print(rect)
    print(rect.__repr__())
    # print(RectangleFactoryMethod.generate(length_type=Length))
    # print(SquareFactoryMethod.generate())
    # print(SquareConverter.auto_convert(FemtoMeter(0.01)))
    # print(CentiMeter(10) + CentiMeter(10))
    # print(CentiMeter(10) * CentiMeter(10))
    # print(2 * (CentiMeter(10) + CentiMeter(10)))
    # print(Rectangle(Line(CentiMeter(10)), Line(CentiMeter(15))))
    # print(Rectangle(Line(Length(10)), Line(CentiMeter(15))))
    # print(Rectangle(Line(CentiMeter(10)), Line(Length(15))))
    # print(Rectangle(Line(Length(10)), Line(Length(15))))
    
    
if __name__ == "__main__":
    main()