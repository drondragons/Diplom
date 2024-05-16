from src import Validator, NumberValidator, FractionValidator, IntValidator, DecimalValidator, ListValidator
# from config import add_project_to_path

from fractions import Fraction
from decimal import Decimal

from src.measurement import Meter

def main() -> None:    
    e, m = ListValidator.validate([str(), 1], str, 1, 2)
    print(e, m)
    
    e, m = FractionValidator.validate(Fraction(1), 0, 1)
    print(e, m)
    
    print("Meter")
    for i in range(20):
        print(Meter(i))
    meter = Meter(2)
    print(meter)
    

if __name__ == "__main__":
    main()