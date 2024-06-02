import copy
from typing import List, Callable

from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QHeaderView,
    QVBoxLayout,
    QMenu,
    QDialog,
    QTableWidgetItem,
)

from . import _find_money_type, _find_length_type
from .font import MAIN_FONT, MAIN_BOLD_FONT, NUMBER_FONT, NUMBER_BOLD_FONT
from .custom_combobox import CustomComboBox
from .validation_delegate import ValidationDelegate

from .. import _format_number
from ..models import Building, Apartment, Shop
from ..measurement.money import Money
from ..measurement.square import SquarePrinter
from ..measurement.length import Length
from ..value_objects.title import Title


__all__ = [
    "CustomTableWidget",
    "BuildingTable",
]


class CustomTableWidget(QTableWidget):
    
    COLUMN_HEADERS = list()
    
    def __init__(self, rows: int, columns: int, parent: QWidget | None = None) -> None:
        super().__init__(rows, columns, parent)
        self.__setup()
        
    def __setup(self) -> None:
        self._set_header(self.COLUMN_HEADERS)
        self._set_columns()
        
    def _set_header(self, text: List[str]) -> None:
        self.setCornerButtonEnabled(False)
        
        self.horizontalHeader().setFont(MAIN_BOLD_FONT)
        self.setHorizontalHeaderLabels(text)
        
        self.verticalHeader().setFont(NUMBER_BOLD_FONT)
        self.setVerticalHeaderLabels([str(i + 1) for i in range(self.rowCount())])
    
    def _set_columns(self) -> None:
        self._set_column_width()
        self._set_columns_font()
        self._set_columns_alignment()
        
    def _set_column_width(self) -> None:
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    
    def _iterate_on_table(self, function: Callable) -> None:
        for row in range(self.rowCount()):
            function(row)
    
    def _set_columns_alignment(self) -> None:
        self._iterate_on_table(self._set_column_alignment)
        
    def _set_column_alignment(self, row: int) -> None:
        for column in range(self.columnCount()):
            item = self.item(row, column)
            if item:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
    def _set_columns_font(self) -> None:
        self._iterate_on_table(self._set_column_font)
    
    def _set_column_font(self, row: int) -> None:
        for column in range(self.columnCount()):
            font = NUMBER_FONT if column else MAIN_FONT
            item = self.item(row, column)
            if item:
                item.setFont(font)
                        
            
class FullScreenTable(QDialog):
    
    TABLE_WINDOW_TITLE = """Таблица на весь экран."""
    
    def __init__(self, data: List[List[str]], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(self.TABLE_WINDOW_TITLE)
        
        layout = QVBoxLayout()
        
        self.table = QTableWidget(self)
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))
        
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(cell)
                self.table.setItem(i, j, item)
                
        layout.addWidget(self.table)
        
        self.setLayout(layout)
    

class BuildingTable(CustomTableWidget):
    
    COLUMN_HEADERS = [
        "Название объекта",
        "Длина",
        "Ширина",
        "Высота",
        "Отступ",
        "Площадь без отступов",
        "Площадь с отступами",
        "Стоимость постройки",
        "Потенциальный доход",
        "Прибыль",
    ]
    
    BUILDINGS = [building for building in Building.__subclasses__()]
    
    def _set_column_headers_text(self) -> None:
        headers = copy.deepcopy(self.COLUMN_HEADERS)
        for i in range(1, 5):
            short_form = _find_length_type(self.length_combobox.currentText()).SHORT_FORM
            headers[i] += (", " + short_form)
        for i in range(5, 7):
            short_form = ", " + SquarePrinter.DEFAULT_SHORT_SQUARE_FORM + " "
            short_form += _find_length_type(self.length_combobox.currentText()).SHORT_FORM
            headers[i] += short_form
        for i in range(7, len(self.COLUMN_HEADERS)):
            _type = _find_money_type(self.money_combobox.currentText())
            symbol = _type.SYMBOL
            if not symbol:
                symbol = _type.SHORT_FORM
            headers[i] += (", " + symbol)
        self._set_header(headers)
    
    def __init__(
        self,
        length_combobox: CustomComboBox,
        money_combobox: CustomComboBox,
        rows: int = 0, 
        parent: QWidget | None = None
    ) -> None:
        super().__init__(rows, len(self.COLUMN_HEADERS), parent)
        self.money_combobox = money_combobox
        self.length_combobox = length_combobox
        self.__set_columns()
        self.__setup()
        
    def __set_columns(self) -> None:
        self._set_column_headers_text()
        self._set_columns_unchanged()
        self.__set_validation_delegate()
        
    def __set_validation_delegate(self) -> None:
        self.setItemDelegateForColumn(0, ValidationDelegate(Title, self))
        for i in range(1, 7):
            self.setItemDelegateForColumn(i, ValidationDelegate(Length, self))
        for i in range(7, self.columnCount()):
            self.setItemDelegateForColumn(i, ValidationDelegate(Money, self))
        
    def __setup(self) -> None:
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)
        
        self._layout = QVBoxLayout()
        self._layout.addWidget(self)
    
    def _set_columns_unchanged(self) -> None:
        self._iterate_on_table(self._set_column_unchanged)
    
    def _set_column_unchanged(self, row: int) -> None:
        unchangable_columns = [5, 6, 9]
        for column in unchangable_columns:
            item = self.item(row, column)
            if item:
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
    
    def _add_building_actions(self) -> QMenu:
        building_menu = QMenu("Добавить объект строительства", self)
        for building in self.BUILDINGS:
            building_menu.addAction(self._add_action(building))
        return building_menu
    
    def _add_action(self, building: Building) -> QAction:
        action = QAction(building.DEFAULT_TITLE, self)
        action.triggered.connect(lambda: self._add_table_row(building))
        return action
    
    def _add_table_row(self, _type: Building) -> None:
        self.setSortingEnabled(False)
        
        row_amount = self.rowCount()
        self.insertRow(row_amount)
        
        building = _type()
        is_commercial = _type in [Apartment, Shop]
        income = int(building.income.value) if is_commercial else int(building.DEFAULT_INCOME)
        profit = int(building.profit.value) if is_commercial else int(building.price_to_build.value) - income

        default_values = [
            building.DEFAULT_TITLE,
            _format_number(int(building.length)),
            _format_number(int(building.width)),
            _format_number(int(building.height)),
            _format_number(int(building.indent)),
            _format_number(int(building.area)),
            _format_number(int(building.area_with_indent)),
            _format_number(int(building.price_to_build)),
            _format_number(int(income)),
            _format_number(int(profit)),
        ]
    
        for j in range(self.columnCount()):
            self.setItem(row_amount, j, QTableWidgetItem(default_values[j]))
        self._set_column_font(row_amount)
        self._set_column_alignment(row_amount)
        self._set_column_unchanged(row_amount)
        
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        
    def _show_context_menu(self, pos: QPoint) -> None:
        context = QMenu(self)
        
        expand_action = QAction("Развернуть таблицу на весь экран", self)
        # expand_action.triggered.connect(self._show_full_screen_table)
        context.addAction(expand_action)
    
        context.addMenu(self._add_building_actions())
        
        context.exec(self.mapToGlobal(pos))