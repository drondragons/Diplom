import os
from PyQt6.QtGui import (
    QIcon,
    QAction,
    QActionGroup,
    QGuiApplication,
    QShowEvent,
    QFont,
)
from PyQt6.QtWidgets import (
    QMainWindow, 
    QStyle,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QMessageBox
)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from . import _find_money_form
from .help_window import HelpWindow
from .custom_table import BuildingTable
from .custom_spinbox import Budget
from .custom_groupbox import SurfaceGroupBox, CountedGroupBox
from .custom_combobox import CustomMoneyComboBox, CustomLengthComboBox
from .custom_pushbutton import CustomPushButton

from .. import _format_number, _format_plural_form
from ..models.price import Price
from ..models.surface import Surface
from ..models.knapsack import BoundedKnapsack
from ..models.buildings import Apartment, Shop
from ..models.placement import Binpacker
from ..value_objects.real import Real
from ..measurement.money import Money
from ..measurement.length import Length


__all__ = [
    "MainWindow",
]


class MainWindow(QMainWindow):
    
    MAIN_WINDOW_TITLE = """Дипломная работа. Метод размещения \
объектов строительства на земельном участке с использованием \
ограниченного рюкзака."""

    PROJECT_DIR = os.getcwd()
    CURRENT_DIR = os.path.join(PROJECT_DIR, "src", "gui", "img")
    
    MAIN_ICON_PATH = os.path.join(CURRENT_DIR, "bmstu-logo.pdf")
    
    def __init__(self, application: QApplication) -> None:
        super().__init__()
        self.application = application
        self.__setup_main_window()
        
    def __setup_main_window(self) -> None:
        self.__set_window_icon()
        self.__set_window_title()
        self.__set_menu_bar()
        self.__set_layouts()
        self.__set_input()
        self.__show_placement()
        self.__show_result()
        self.showEvent()
        
    def __set_layouts(self) -> None:
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QVBoxLayout(self.main_widget)
        
        self.input_and_figure_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_and_figure_layout)
        
        self.output_layout = QVBoxLayout()
        self.main_layout.addLayout(self.output_layout)
        
        self.input_layout = QVBoxLayout()
        self.input_and_figure_layout.addLayout(self.input_layout)
        
    def __set_input(self) -> None:
        self.__set_money_layout()
        self.__set_length_layout()
        self.__set_budget_layout()
        self.__set_surface()
        self.__set_building_table()
        self.__set_button()
        
    def __set_button(self) -> None:
        self.placement_button = CustomPushButton("Разместить объекты строительства на земельном участке")
        self.placement_button.clicked.connect(self._on_button_placement)
        self.input_layout.addWidget(self.placement_button)
        
    def _on_button_placement(self) -> None:
        width = Length(Real(self.surface_groupbox.width_spinbox.value()))
        length = Length(Real(self.surface_groupbox.length_spinbox.value()))
        budget = Price(Money(Real(self.budget_spinbox.value())))
        buildings = self.building_table.buildings
        
        try:
            surface = Surface(length, width)
            surface.validate_placement_buildings(buildings)
    
            solution = BoundedKnapsack.solve_dynamic(surface.area, buildings, budget)
            # for item in solution:
            #     print(item)
            # input()
            print("Максимум найден!")
            pacher = Binpacker(int(surface.width), int(surface.length))
            while True:
                if pacher.fit_blocks(solution):
                    self._update_figure(pacher)
                    break
                
                if not isinstance(solution[-1], Apartment | Shop):
                    raise ValueError("\n\tНевозможно расположить даже требуемые объекты!\n")
                else:
                    minimum = solution[-1].profit
                    
                index = 0
                for i, building in enumerate(solution):
                    if isinstance(building, Apartment | Shop) and building.profit <= minimum:
                        index = i
                        minimum = building.profit
                solution = solution[:index] + solution[index + 1:]
                
        except Exception as exception:
            message = type(exception).__name__ + ":" + str(exception)
            QMessageBox.warning(None, "Ошибка размещения.", message)
            return 
            
        try:
            income = Price()
            income_chosen = Price()
            cost = Price()
            cost_chosen = Price()
            for item in solution:
                cost += item.price_to_build
                income += item.income
                if isinstance(item, Apartment | Shop):
                    cost_chosen += item.price_to_build
                    income_chosen += item.income
            
            # ------------------- Income ----------------------
            
            income_necessary = float(income.value.value - income_chosen.value.value)
            self.counted_groupbox.necessary_income_value_label.setText(
                f"{_format_number(income_necessary)}"
            )
            self.counted_groupbox.necessary_income_measurement_label.setText(
                f"{_find_money_form(income_necessary, self.money_combobox.currentText())}"
            )
            
            income_chosen = float(income_chosen.value.value)
            self.counted_groupbox.chosen_income_value_label.setText(
                f"{_format_number(income_chosen)}"
            )
            self.counted_groupbox.chosen_income_measurement_label.setText(
                f"{_find_money_form(income_chosen, self.money_combobox.currentText())}"
            )
            
            income = float(income.value.value)
            self.counted_groupbox.result_income_value_label.setText(
                f"{_format_number(income)}"
            )
            self.counted_groupbox.result_income_measurement_label.setText(
                f"{_find_money_form(income, self.money_combobox.currentText())}"
            )
            
            # ------------------- Cost ----------------------
            
            cost_necessary = float(cost.value.value - cost_chosen.value.value)
            self.counted_groupbox.necessary_cost_value_label.setText(
                f"{_format_number(cost_necessary)}"
            )
            self.counted_groupbox.necessary_cost_measurement_label.setText(
                f"{_find_money_form(cost_necessary, self.money_combobox.currentText())}"
            )
            
            cost_chosen = float(cost_chosen.value.value)
            self.counted_groupbox.chosen_cost_value_label.setText(
                f"{_format_number(cost_chosen)}"
            )
            self.counted_groupbox.chosen_cost_measurement_label.setText(
                f"{_find_money_form(cost_chosen, self.money_combobox.currentText())}"
            )
            
            cost = float(cost.value.value)
            self.counted_groupbox.result_cost_value_label.setText(
                f"{_format_number(cost)}"
            )
            self.counted_groupbox.result_cost_measurement_label.setText(
                f"{_find_money_form(cost, self.money_combobox.currentText())}"
            )
            
            # ------------------- Profit ----------------------
            
            profit_necessary = income_necessary - cost_necessary
            self.counted_groupbox.necessary_profit_value_label.setText(
                f"{_format_number(profit_necessary)}"
            )
            self.counted_groupbox.necessary_profit_measurement_label.setText(
                f"{_find_money_form(profit_necessary, self.money_combobox.currentText())}"
            )
            
            profit_chosen = income_chosen - cost_chosen
            self.counted_groupbox.chosen_profit_value_label.setText(
                f"{_format_number(profit_chosen)}"
            )
            self.counted_groupbox.chosen_profit_measurement_label.setText(
                f"{_find_money_form(profit_chosen, self.money_combobox.currentText())}"
            )
            
            profit = income - cost
            self.counted_groupbox.result_profit_value_label.setText(
                f"{_format_number(profit)}"
            )
            self.counted_groupbox.result_profit_measurement_label.setText(
                f"{_find_money_form(profit, self.money_combobox.currentText())}"
            )
            
        except Exception as exception:
            message = type(exception).__name__ + ":" + str(exception)
            QMessageBox.warning(None, "Ошибка вычислений.", message)
            return 
          
    def _update_figure(self, packer) -> None:
        self.ax.clear()
        packer.plot_packing(self.ax)
        self._draw_canvas()
        
    def __set_building_table(self) -> None:
        self.building_table = BuildingTable(self.length_combobox, self.money_combobox)
        self.input_layout.addLayout(self.building_table._layout)
        
    def __set_surface(self) -> None:
        self.surface_groupbox = SurfaceGroupBox(self.length_combobox)
        self.input_layout.addWidget(self.surface_groupbox)
        
    def __set_money_layout(self, is_visible: bool = False) -> None:
        self.money_combobox = CustomMoneyComboBox(self.__money_combobox_changed)
        self.money_combobox.is_visible(is_visible)
        self.input_layout.addLayout(self.money_combobox._layout)
    
    def __money_combobox_changed(self) -> None:
        self.budget_spinbox._set_label_text()
        self.building_table._set_column_headers_text()
        self.building_table.edit_window._set_label_text()
        
    def __set_length_layout(self, is_visible: bool = False) -> None:
        self.length_combobox = CustomLengthComboBox(self.__length_combobox_changed)
        self.length_combobox.is_visible(is_visible)
        self.input_layout.addLayout(self.length_combobox._layout)
        
    def __length_combobox_changed(self) -> None:
        self.surface_groupbox._set_label_text()
        self.building_table._set_column_headers_text()
        
    def __set_budget_layout(self) -> None:
        self.budget_spinbox = Budget(self.money_combobox)
        self.input_layout.addLayout(self.budget_spinbox._layout)
        
    def __set_menu_bar(self) -> None:
        self.dark_theme_action = QAction("Тёмная тема", self)
        self.dark_theme_action.setCheckable(True)
        
        self.light_theme_action = QAction("Светлая тема", self)
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setChecked(True)
        
        menubar = self.menuBar()
        menubar.setFont(QFont("Candara", 10))
        settings_menu = menubar.addMenu("Настройки")
        settings_menu.setFont(QFont("Candara", 10))
        
        desktop_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)
        theme_menu = settings_menu.addMenu(desktop_icon, "Сменить тему")
        theme_menu.addAction(self.light_theme_action)
        theme_menu.addSeparator()
        theme_menu.addAction(self.dark_theme_action)
        
        help_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarContextHelpButton
        )
        help_action = QAction(help_icon, "Справка", self)
        help_action.triggered.connect(self.__show_help_window)
        settings_menu.addAction(help_action)

        action_group = QActionGroup(self)
        action_group.addAction(self.dark_theme_action)
        action_group.addAction(self.light_theme_action)
        action_group.triggered.connect(self.__change_theme)
    
    def __change_theme(self, action: QAction) -> None:
        if action == self.light_theme_action:
            self.application.setStyle("windowsvista")
            self.light_theme_action.setChecked(True)
        elif action == self.dark_theme_action:
            self.application.setStyle("fusion")
            self.dark_theme_action.setChecked(True)
        
    def __set_window_title(self) -> None:
        self.setWindowTitle(self.MAIN_WINDOW_TITLE)
        
    def __set_window_icon(self) -> None:
        self.setWindowIcon(QIcon(self.MAIN_ICON_PATH))
        
    def __show_help_window(self) -> None:
        self.help_window = HelpWindow()
        self.help_window.show()
    
    def _draw_canvas(self) -> None:
        self.ax.set_title("Размещение объектов строительства на земельном участке", pad=20)
        self.ax.set_xlabel("Ширина земельного участка, в метрах", labelpad=7)
        self.ax.set_ylabel("Длина земельного участка, в метрах", labelpad=7)
        
        self.canvas.draw()
    
    def __show_placement(self) -> None:
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.input_and_figure_layout.addWidget(self.canvas)
        
        self.ax = self.figure.add_subplot(111)
        
        self._draw_canvas()
    
    def __show_result(self) -> None:
        self.counted_groupbox = CountedGroupBox(self.money_combobox)
        self.input_layout.addWidget(self.counted_groupbox)
    
    def showEvent(self, event: QShowEvent = None) -> None:
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self, event: QShowEvent) -> None:
        QApplication.closeAllWindows()