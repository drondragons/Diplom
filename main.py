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

from src import Surface, Building, Apartment

def main() -> None:
    surface = Surface()
    surface.length = Length(100)
    surface.width = Meter(100)
    print(surface)
    
    apartment = Apartment()
    print(apartment)
    
    print(surface.validate_placement_buildings([apartment, apartment, apartment, apartment]))
    
    
if __name__ == "__main__":
    main()