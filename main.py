from src import Validator, NumberValidator, FractionValidator, IntValidator, DecimalValidator, ListValidator

from fractions import Fraction
from decimal import Decimal
import math
import sys
from src import Real, OPERATORS

from src.measurement import Meter

def main() -> None:    
    e, m = ListValidator.validate([str(), 1], str, 1, 2)
    print(e, m)
    
    e, m = FractionValidator.validate(Fraction(1), 0, 1)
    print(e, m)
    
    print("Meter")
    for i in range(20):
        print(Meter(Fraction(i)))
    meter = Meter(2)
    print(meter)
    
    t = [dir(int), dir(float), dir(Decimal), dir(Fraction)]
    for item in t:
        print("__or__" in item)
        
    print(math.floor(Meter(Fraction(12323/234))))
    print(math.ceil(Meter(Fraction(12323/234))))
    print(math.trunc(Meter(Fraction(12323/234))))
    print(Meter(Fraction(12323/234)).__int__())
    print(Meter(Fraction(12323/234)).__float__())
    print(int(1).__float__())
    print(float(1.12434923).__float__())
    print(int(1).__sizeof__())
    print(float(1.23).__sizeof__())
    print(sys.getsizeof(1))
    print(sys.getsizeof(1.9245))
    print(sys.getsizeof(Meter(Fraction(123/243))))
    print(Meter(Fraction(123/243)).__sizeof__())
    print(sys.getsizeof(object()))
    
    # print(len(int(1)))
    
    print(1 == Real(1))
    print(Real(1) == 1)
    print(1 != Real(1))
    print(Real(1) != 1)
    print(1 < Real(1))
    print(Real(1) < 1)
    print(1 > Real(1))
    print(Real(1) > 1)
    print(1 <= Real(1))
    print(Real(1) <= 1)
    print(1 >= Real(1))
    print(Real(1) >= 1)
    
    # print(~Real(1))
    print(Real(1).__inv__())
    print(Real(1).__invert__())
    
    print(OPERATORS)
    
    # '__add__', '__and__', '__bool__', '__class__',
    # '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
    # '__floordiv__', '__ge__', '__getattribute__',
    # '__getnewargs__', '__gt__', '__init_subclass__',
    # '__le__', '__lshift__', '__lt__', '__mod__', '__mul__',
    # '__ne__', '__new__', '__or__', '__pow__', '__radd__', '__rand__',
    # '__rdivmod__', '__reduce__', '__reduce_ex__', '__rfloordiv__',
    # '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', 
    # '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', 
    # '__sizeof__', '__sub__', '__subclasshook__', '__truediv__', 
    # '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator',
    # 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes'
    

if __name__ == "__main__":
    main()