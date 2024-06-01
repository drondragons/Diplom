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
from src import PavilionFactoryMethod, Shop
from src import Surface, Building, Apartment, School, Hospital, Pavilion

from src import BoundedKnapsack, Binpacker, Kindergarten
from src import _get_pretty_number

import sys
from src.gui import MainWindow
from PyQt6.QtWidgets import QApplication


def main() -> None:
    application = QApplication(sys.argv)
    application.setStyle("fusion")
    
    main_window = MainWindow(application)
    main_window.show()
    
    sys.exit(application.exec())
    
    # surface = Surface()
    # # surface.length = Length(500)
    # # surface.width = Meter(500)
    # # surface.length = Length(300)
    # # surface.width = Meter(200)
    # # surface.length = Length(500)
    # # surface.width = Meter(200)
    # surface.length = Length(150)
    # surface.width = Meter(120)
    # print(surface)
    
    # apartment = Apartment(title="7-этажный жилой дом")
    # print(apartment)
    # shop = Shop(length=Meter(70), width=Meter(60))
    # print(shop)
    # ten_apartment = Apartment(
    #     height=Length(27.5), 
    #     title="10-этажный жилой дом"
    # )
    # print(ten_apartment)
    # fifteen_apartment = Apartment(
    #     height=Length(40), 
    #     title="15-этажный жилой дом", 
    #     price_to_build=Ruble(1_200_000_000)
    # )
    # print(fifteen_apartment)
    
    # budget = Price(Ruble(10_000_000_000), "Бюджет")
    # buildings = [
    #     School(length=Meter(40), width=Meter(70)), 
    #     Hospital(length=Meter(50), width=Meter(60)), 
    #     Kindergarten(length=Meter(50), width=Meter(40)),
    #     apartment,
    #     shop, 
    #     ten_apartment,
    #     fifteen_apartment
    # ]
        
    # surface.validate_placement_buildings(buildings)
    
    # print("=" * 100)
    
    # solution = BoundedKnapsack.solve_dynamic(surface.area, buildings, budget)
    # for item in solution:
    #     print(item)
    
    # print("=" * 100)
    
    # pacher = Binpacker(int(surface.width), int(surface.length))
    # while True:
    #     if pacher.fit_blocks(solution):
    #         print(pacher.plot_packing())
    #         break
        
    #     if not isinstance(solution[-1], Apartment | Shop):
    #         print("\n\tНевозможно расположить даже требуемые объекты!\n")
    #         break
    #     else:
    #         minimum = solution[-1].profit
            
    #     index = 0
    #     for i, building in enumerate(solution):
    #         if isinstance(building, Apartment | Shop) and building.profit <= minimum:
    #             index = i
    #             minimum = building.profit
    #     solution = solution[:index] + solution[index + 1:]
    
    # profit = 0
    # price_to_build = 0
    # price_to_build_choose = 0
    # for item in solution:
    #     if isinstance(item, Apartment | Shop):
    #         profit += item.profit
    #         price_to_build_choose += item.price_to_build
    #     price_to_build += item.price_to_build
    # print(Price(profit.value, "Прибыль с застройки участка"))
    # print(Price(price_to_build.value, "Затраты на строительство всех объектов"))
    # print(Price((price_to_build - price_to_build_choose).value, "Затраты на строительство обязательных объектов"))
    # print("Конец")
        
    
if __name__ == "__main__":
    main()