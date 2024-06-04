import re
import copy
from typing import List, Callable

from PyQt6.QtGui import QAction, QKeyEvent
from PyQt6.QtCore import Qt, QPoint, QEvent
from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QHeaderView,
    QVBoxLayout,
    QMenu,
    QTableWidgetItem,
)

from . import _find_money_type, _find_length_type, _find_building_type
from .font import MAIN_FONT, MAIN_BOLD_FONT, NUMBER_FONT, NUMBER_BOLD_FONT
from .custom_combobox import CustomComboBox
from .validation_delegate import ValidationDelegate

from .. import _format_number
from ..models.buildings import Building, Apartment, Shop, School, Hospital, Kindergarten
from ..measurement.money import Money
from ..measurement.square import SquarePrinter
from ..measurement.length import Length
from ..value_objects.title import Title


__all__ = [
    "BuildingTable",
]


class CustomTableWidget(QTableWidget):
    
    COLUMN_HEADERS = list()
    
    def __init__(self, rows: int, columns: int, parent: QWidget | None = None) -> None:
        super().__init__(rows, columns, parent)
        self.__setup()
        
    def __setup(self) -> None:
        self._set_header(self.COLUMN_HEADERS)
        self._set_rows()
        self._set_columns()
        
    def _set_header(self, text: List[str]) -> None:
        self.setCornerButtonEnabled(False)
        
        self.horizontalHeader().setFont(MAIN_BOLD_FONT)
        self.setHorizontalHeaderLabels(text)
        
        self.verticalHeader().setFont(NUMBER_BOLD_FONT)
        self.setVerticalHeaderLabels([str(i + 1) for i in range(self.rowCount())])
    
    def _set_rows(self) -> None:
        self._set_row_width()
        
    def _set_row_width(self) -> None:
        self.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    
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
                
    def keyPressEvent(self, event: QKeyEvent) -> None:
        delete_keys = [Qt.Key.Key_Delete, Qt.Key.Key_Backspace]
        if event.key() not in delete_keys:
            return super().keyPressEvent(event)
        
        selected = self.selectedRanges()
        for range in selected:
            if range.leftColumn() == 0 and range.rightColumn() == self.columnCount() - 1:
                self.removeRow(range.topRow())
                        
            
class FullScreenTable(QWidget):
    
    WINDOW_TITLE = """Таблица на весь экран."""
    
    def __init__(self, table: CustomTableWidget, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle(self.WINDOW_TITLE)

        layout = QVBoxLayout()

        self.table = table
        
        self.escape_action = QAction(self)
        self.escape_action.setShortcut("Esc")
        self.escape_action.triggered.connect(self.closeEvent)
        self.addAction(self.escape_action)
        
        layout.addWidget(self.table)
        
        self.setLayout(layout)
    
    def closeEvent(self, event: QEvent) -> None:
        self.hide()
        self.destroyed.emit()
        
        
# class EditCommercialBuilding(QWidget):
    
#     WINDOW_TITLE = f"""Редактирование данных объекта '{text}'."""
    
#     def __init__(self, parent: QWidget | None = None) -> None:
#         super().__init__(parent)
#         self.setWindowTitle(self.WINDOW_TITLE)
        

    
class BuildingTable:
    
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
    COMMERCIAL_BUILDINGS = [Apartment, Shop]
    
    DEFAULT_BUILDINGS = [School, Kindergarten, Apartment, Shop, Hospital]
    
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
        self.table._set_header(headers)
    
    def __init__(
        self,
        length_combobox: CustomComboBox,
        money_combobox: CustomComboBox
    ) -> None:
        self.table = CustomTableWidget(0, len(self.COLUMN_HEADERS))
        self.money_combobox = money_combobox
        self.length_combobox = length_combobox
        self.is_full_screen = False
        self.__set_columns()
        self.__setup()
        self.__fill_table_by_default_buildings()
        
    def __fill_table_by_default_buildings(self) -> None:
        for building in self.DEFAULT_BUILDINGS:
            self._add_table_row(building)
        
    def __set_columns(self) -> None:
        self._set_column_headers_text()
        self._set_columns_unchanged()
        self.__set_validation_delegate()
        
    def __set_column(self, row: int) -> None:
        self.table._set_column_font(row)
        self.table._set_column_alignment(row)
        self._set_column_unchanged(row)
        
    def __set_validation_delegate(self) -> None:
        self.table.setItemDelegateForColumn(0, ValidationDelegate(Title, self.table))
        for i in range(1, 7):
            self.table.setItemDelegateForColumn(i, ValidationDelegate(Length, self.table))
        for i in range(7, self.table.columnCount()):
            self.table.setItemDelegateForColumn(i, ValidationDelegate(Money, self.table))
        
    def __setup(self) -> None:
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self._show_context_menu)
        
        self.table.itemChanged.connect(self.__item_changed)
        self.table.verticalHeader().sectionDoubleClicked.connect(self.__vertical_header_double_clicked)
    
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.table)
    
    def __is_row_filled(self, row: int) -> None:
        for column in range(self.table.columnCount()):
            if not self.table.item(row, column):
                return False
        return True
    
    def __get_item_value(self, row: int, column: int) -> str:
        return re.sub(r" ", "", self.table.item(row, column).text())
    
    def __get_width(self, row: int) -> int:
        return int(self.__get_item_value(row, 2))
    
    def __get_length(self, row: int) -> int:
        return int(self.__get_item_value(row, 1))
    
    def __get_indent(self, row: int) -> int:
        return int(self.__get_item_value(row, 4))
    
    def __get_income(self, row: int) -> int:
        return int(self.__get_item_value(row, 8))
    
    def __get_price_to_build(self, row: int) -> int:
        return int(self.__get_item_value(row, 7))
    
    def __count_area(self, row: int) -> int:
        return self.__get_width(row) * self.__get_length(row)
    
    def __count_area_with_indent(self, row: int) -> int:
        area = self.__count_area(row)
        area += 2 * self.__get_indent(row) * (self.__get_width(row) + self.__get_length(row))
        return area + 4 * self.__get_indent(row) ** 2
        
    def __count_profit(self, row: int) -> int:
        return self.__get_income(row) - self.__get_price_to_build(row)
    
    def __create_table_widget_item(self, value: int) -> QTableWidgetItem:
        return QTableWidgetItem(_format_number(value))
        
    def __item_changed(self, item: QTableWidgetItem) -> None:
        row = item.row()
        column = item.column()
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        if self.table.item(row, 0).text() in titles:
            return
        if column not in [1, 2, 4, 7, 8]:
            return
        if not self.__is_row_filled(row):
            return
        
        area_item = self.__create_table_widget_item(self.__count_area(row))
        area_with_indent_item = self.__create_table_widget_item(self.__count_area_with_indent(row))
        profit = self.__create_table_widget_item(self.__count_profit(row))
        match column:
            case 1 | 2:
                self.table.setItem(row, 5, area_item)
                self.table.setItem(row, 6, area_with_indent_item)
            case 4:
                self.table.setItem(row, 6, area_with_indent_item)
            case 7 | 8:
                self.table.setItem(row, 9, profit)
        self.__set_column(row)
    
    def __vertical_header_double_clicked(self, row: int) -> None:
        print("Double clicked vertical header")
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        if self.table.item(row, 0).text() not in titles:
            return
        
        
        print("Commercial")
    
    def _set_columns_unchanged(self) -> None:
        self.table._iterate_on_table(self._set_column_unchanged)
    
    def _set_column_unchanged(self, row: int) -> None:
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        
        is_commercial = False
        item = self.table.item(row, 0)
        if item:
            is_commercial = item.text() in titles
            
        unchangable_columns = [0, 3, 5, 6, 9] if not is_commercial else list(range(10))
        for column in unchangable_columns:
            item = self.table.item(row, column)
            if item:
                item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
    
    def _add_building_actions(self) -> QMenu:
        building_menu = QMenu("Добавить объект строительства", self.table)
        for building in self.BUILDINGS:
            building_menu.addAction(self._add_action(building))
        return building_menu
    
    def _add_action(self, building: Building) -> QAction:
        action = QAction(building.DEFAULT_TITLE, self.table)
        action.triggered.connect(lambda: self._add_table_row(building))
        return action
    
    def _add_table_row(self, _type: Building) -> None:
        self.table.setSortingEnabled(False)
        
        row_amount = self.table.rowCount()
        self.table.insertRow(row_amount)
        
        building = _type()
        is_commercial = _type in self.COMMERCIAL_BUILDINGS
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
    
        for j in range(self.table.columnCount()):
            self.table.setItem(row_amount, j, QTableWidgetItem(default_values[j]))
            
        self.__set_column(row_amount)
        
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        
    def _show_context_menu(self, pos: QPoint) -> None:
        context = QMenu(self.table)
        
        if not self.is_full_screen:
            expand_action = QAction("Развернуть таблицу на весь экран", self.table)
            expand_action.triggered.connect(self._show_full_screen_table)
            context.addAction(expand_action)
    
        context.addMenu(self._add_building_actions())
        
        context.exec(self.table.mapToGlobal(pos))
        
    def _show_full_screen_table(self) -> None:
        self.full_screen_table = FullScreenTable(self.table)
        self.full_screen_table.showMaximized()
        self.full_screen_table.destroyed.connect(self._on_full_screen_table_closed)
        self.is_full_screen = True
        
    def _on_full_screen_table_closed(self):
        self.table = self.full_screen_table.table
        self._layout.addWidget(self.table)
        self.is_full_screen = False