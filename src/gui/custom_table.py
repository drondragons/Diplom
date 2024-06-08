import re
import copy
from typing import List, Callable, Tuple, Type

from PyQt6.QtGui import QAction, QKeyEvent, QShowEvent, QGuiApplication
from PyQt6.QtCore import Qt, QPoint, QEvent
from PyQt6.QtWidgets import (
    QWidget,
    QTableWidget,
    QHeaderView,
    QVBoxLayout,
    QHBoxLayout,
    QMenu,
    QTableWidgetItem,
    QStyle,
    QMessageBox
)

from . import _find_money_type, _find_length_type, _find_money_form
from . import _find_length_form
from .font import MAIN_FONT, MAIN_BOLD_FONT, NUMBER_FONT, NUMBER_BOLD_FONT, MAIN_FONT_METRICS
from .custom_label import CustomLabel
from .custom_spinbox import CustomDoubleSpinBox
from .custom_combobox import CustomComboBox, CustomLengthComboBox, CustomMoneyComboBox
from .custom_pushbutton import CustomPushButton
from .validation_delegate import ValidationDelegate

from .. import _format_number
from ..models.price import Price
from ..models.buildings import Building, Apartment, Shop, School, Hospital, Kindergarten
from ..measurement.money import Money
from ..measurement.square import SquarePrinter
from ..measurement.length import Length
from ..value_objects.real import Real
from ..value_objects.title import Title
from ..geometry.one_dimensional import Line


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
        icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_DesktopIcon
        )
        self.setWindowIcon(icon)

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
        
        
class EditCommercialBuilding(QWidget):
    
    COLUMN_HEADERS = [
        "Длина",
        "Ширина",
        "Высота",
        "Отступ",
        "Стоимость постройки",
        "Доход",
        "Высота этажа",
    ]
    
    def __init__(
        self,
        row: int,
        building: Building,
        length_combobox: CustomComboBox,
        money_combobox: CustomComboBox,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        
        self.money_combobox = money_combobox
        self.length_combobox = length_combobox
        
        self.length_label_width = MAIN_FONT_METRICS.horizontalAdvance(
            max(CustomLengthComboBox.LENGTH_FULL_FORM, key = len)
        )
        self.money_label_width = MAIN_FONT_METRICS.horizontalAdvance(
            max(CustomMoneyComboBox.MONEY_FULL_FORM, key = len)
        )
        
        self.row = row
        self.building = building
        
        self.setWindowTitle(f"""Редактирование данных объекта «{building.title}».""")
        icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_DesktopIcon
        )
        self.setWindowIcon(icon)
        
        self._layout = QVBoxLayout(self)
        
        self.length_spinbox, self.length_label = self._set_part_1(
            self.building.length,
            minimum = self.building.MINIMUM_LENGTH
        )
        self.width_spinbox, self.width_label = self._set_part_1(
            self.building.width,
            minimum = self.building.MINIMUM_WIDTH
        )
        self.height_spinbox, self.height_label = self._set_part_1(
            self.building.height,
            minimum = self.building.MINIMUM_HEIGHT
        )
        self.indent_spinbox, self.indent_label = self._set_part_1(
            self.building.indent,
            1,
            100,
            0
        )
        self.price_to_build_spinbox, self.price_to_build_label = self._set_part_2(
            self.building.price_to_build
        )
        self.income_spinbox, self.income_label = self._set_part_2(
            self.building.income,
        )
        self.floor_height_spinbox, self.floor_height_label = self._set_part_1(
            self.building.floor_height,
            0.01,
            Apartment.MAXIMUM_FLOOR_HEIGHT,
            Apartment.MINIMUM_FLOOR_HEIGHT
        )
        
        self.button = CustomPushButton("Сохранить изменения")
        self.button.clicked.connect(self._on_button_clicked)
        self._layout.addWidget(self.button)
        
        self.result = None
    
    def _on_button_clicked(self) -> None:    
        try:
            building = type(self.building)(
                Length(Real(self.length_spinbox.value())),
                Length(Real(self.width_spinbox.value())),
                Length(Real(self.height_spinbox.value())),
                Length(Real(self.indent_spinbox.value())),
                Money(Real(self.price_to_build_spinbox.value())),
                Money(Real(self.income_spinbox.value())),
                Length(Real(self.floor_height_spinbox.value()))
            )
            
            if self.building == building:
                self.hide()
                return
            
            self.building = building
            
            self.hide()
            self.destroyed.emit()
            
        except Exception as exception:
            message = type(exception).__name__ + ":" + str(exception)
            QMessageBox.warning(None, "Ошибка ввода данных.", message)
        
    def _set_part_1(
        self,
        value: Line,
        step: float = 10,
        maximum: float = 10 ** 6,
        minimum: float = 1
    ) -> Tuple[CustomDoubleSpinBox, CustomLabel]:
        layout = QHBoxLayout()
        
        label = CustomLabel(str(value.title))
        
        spinbox = CustomDoubleSpinBox()
        spinbox.setSingleStep(step)
        spinbox.setValue(float(value.length))
        spinbox.setMaximum(maximum)
        spinbox.setMinimum(minimum)
        
        result = CustomLabel()
        result.setFixedWidth(self.length_label_width)
        
        spinbox.valueChanged.connect(
            lambda v: CustomLabel._set_label_text(
                result,
                _find_length_form,
                v,
                self.length_combobox.currentText()
            )
        )
        CustomLabel._set_label_text(
            result,
            _find_length_form,
            spinbox.value(),
            self.length_combobox.currentText()
        )
        
        layout.addWidget(label)
        layout.addWidget(spinbox)
        layout.addWidget(result)
        
        self._layout.addLayout(layout)
        
        return spinbox, result
    
    def _set_part_2(self, value: Price) -> Tuple[CustomDoubleSpinBox, CustomLabel]:
        layout = QHBoxLayout()
        
        label = CustomLabel(str(value.title))
        
        spinbox = CustomDoubleSpinBox()
        spinbox.setValue(int(value.value))
        
        result = CustomLabel()
        result.setFixedWidth(self.money_label_width)
        
        spinbox.valueChanged.connect(
            lambda v: CustomLabel._set_label_text(
                result,
                _find_money_form,
                v,
                self.money_combobox.currentText()
            )
        )
        CustomLabel._set_label_text(
            result,
            _find_money_form,
            spinbox.value(),
            self.money_combobox.currentText()
        )
        
        layout.addWidget(label)
        layout.addWidget(spinbox)
        layout.addWidget(result)
        
        self._layout.addLayout(layout)
        
        return spinbox, result
        
    def showEvent(self, event: QShowEvent = None) -> None:
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def __set_length_label_text(self, label: CustomLabel, value: int | float) -> None:
        CustomLabel._set_label_text(
            label,
            _find_length_form, 
            value, 
            self.length_combobox.currentText()
        )
        
    def __set_money_label_text(self, label: CustomLabel, value: int | float) -> None:
        CustomLabel._set_label_text(
            label,
            _find_money_form, 
            value, 
            self.money_combobox.currentText()
        )
        
    def __set_length_labels_text(self) -> None:
        self.__set_length_label_text(self.length_label, self.length_spinbox.value())
        self.__set_length_label_text(self.width_label, self.width_spinbox.value())
        self.__set_length_label_text(self.height_label, self.height_spinbox.value())
        self.__set_length_label_text(self.indent_label, self.indent_spinbox.value())
        self.__set_length_label_text(self.floor_height_label, self.floor_height_spinbox.value())
        
        self.__set_money_label_text(self.price_to_build_label, self.price_to_build_spinbox.value())
        self.__set_money_label_text(self.income_label, self.income_spinbox.value())
        
    def _set_label_text(self) -> None:
        self.__set_length_labels_text()
        
    def closeEvent(self, event: QEvent) -> None:
        self.hide()

    
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
    
    COLUMN_MAPPING = {
        1: 'length',
        2: 'width',
        3: 'height',
        4: 'indent',
        5: 'area',
        6: 'area_with_indent',
        7: 'price_to_build',
        8: 'income',
        9: 'profit'
    }
    
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
        self.is_changed = False
        
        self.buildings = list()
        
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
        self.table.verticalHeader().sectionDoubleClicked.connect(
            self.__vertical_header_double_clicked
        )
    
        self._layout = QVBoxLayout()
        self._layout.addWidget(self.table)
    
    def __is_row_filled(self, row: int) -> None:
        for column in range(self.table.columnCount()):
            if not self.table.item(row, column):
                return False
        return True
    
    def __create_table_widget_item(self, value: int) -> QTableWidgetItem:
        return QTableWidgetItem(_format_number(value))
      
    def __make_building_attribute(self, item: QTableWidgetItem, _type = Type) -> Money | Length:
        return _type(Real(int(re.sub(r" ", "", item.text()))))
        
    def __building_change(self, row: int) -> None:
        for col in [1, 2, 3, 4, 7, 8]:
            if col in [1, 2, 3, 4]:
                attribute_type = Length
            else:
                attribute_type = Money    
            setattr(
                self.buildings[row],
                self.COLUMN_MAPPING[col], 
                self.__make_building_attribute(self.table.item(row, col), attribute_type)
            )
            
        self.is_changed = True
        
    def __item_changed(self, item: QTableWidgetItem) -> None:
        row = item.row()
        column = item.column()
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        if not self.buildings or len(self.buildings) - 1 < row:
            return
        if self.is_changed:
            return
        if self.table.item(row, 0).text() in titles:
            return
        if column not in [1, 2, 3, 4, 7, 8]:
            return
        if not self.__is_row_filled(row):
            return
        
        try:
            self.__building_change(row)
        
            for col, attr in self.COLUMN_MAPPING.items():
                value = getattr(self.buildings[row], attr) 
                value = value.length if col < 5 else value.value if col != 9 else value
                value = int(value)
                self.table.setItem(row, col, self.__create_table_widget_item(value))
            
        except Exception as exception:
            message = type(exception).__name__ + ":" + str(exception)
            QMessageBox.warning(None, "Ошибка ввода данных.", message)
                
            value = getattr(self.buildings[row], self.COLUMN_MAPPING[column])
            value = value.length if column < 5 else value.value if column != 9 else value
            item = self.__create_table_widget_item(int(value))
            
            self.is_changed = True
            self.table.setItem(row, column, item)
        
        self.__set_column(row)
        self.is_changed = False
        
    def __vertical_header_double_clicked(self, row: int) -> None:
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        if self.table.item(row, 0).text() not in titles:
            return
        
        self.edit_window = EditCommercialBuilding(
            row,
            self.buildings[row],
            self.length_combobox,
            self.money_combobox
        )
        self.edit_window.show()
        self.edit_window.destroyed.connect(self._on_edit_window_closed)
    
    def _set_columns_unchanged(self) -> None:
        self.table._iterate_on_table(self._set_column_unchanged)
    
    def _set_column_unchanged(self, row: int) -> None:
        titles = [building.DEFAULT_TITLE for building in self.COMMERCIAL_BUILDINGS]
        
        is_commercial = False
        item = self.table.item(row, 0)
        if item:
            is_commercial = item.text() in titles
            
        unchangable_columns = [0, 5, 6, 9] if not is_commercial else list(range(10))
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
    
    def _add_table_row(self, _type: Building) -> Building:
        self.table.setSortingEnabled(False)
        
        row_amount = self.table.rowCount()
        self.table.insertRow(row_amount)
        
        building = _type()
        is_commercial = _type in self.COMMERCIAL_BUILDINGS
        income = int(building.income.value) if is_commercial else int(building.DEFAULT_INCOME)
        profit = int(building.profit.value) if is_commercial else income - int(building.price_to_build.value)

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
        
        self.buildings.append(building)
        self.buildings = sorted(self.buildings, key = lambda b: b.title)
        
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
        
    def _on_edit_window_closed(self):
        row = self.edit_window.row
        for col, attr in self.COLUMN_MAPPING.items():
            value = getattr(self.edit_window.building, attr) 
            value = value.length if col < 5 else value.value if col != 9 else value
            value = int(value)
            self.table.setItem(row, col, self.__create_table_widget_item(value))
        self.buildings[row] = self.edit_window.building
        self.__set_column(row)