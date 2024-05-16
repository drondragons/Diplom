from src import Validator, NumberValidator, FractionValidator
# from config import add_project_to_path

from fractions import Fraction

def main() -> None:
    # add_project_to_path()
    e, m = Validator.validate_type(1.0, int)
    print(e)
    print(m)
    
    print(Fraction())
    print(FractionValidator.validate(Fraction()))
    

if __name__ == "__main__":
    main()