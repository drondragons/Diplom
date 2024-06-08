from typing import Tuple, Callable
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGroupBox, QWidget, QVBoxLayout, QHBoxLayout, QFrame

from . import _find_length_form
from .font import MAIN_FONT, MAIN_FONT_METRICS, NUMBER_BOLD_FONT
from .custom_label import CustomLabel, CustomBoldLabel
from .custom_spinbox import CustomDoubleSpinBox
from .custom_combobox import CustomLengthComboBox, CustomMoneyComboBox


__all__ = [
    "CustomGroupBox",
    "SurfaceGroupBox",
]


class CustomGroupBox(QGroupBox):
    
    GROUPBOX_FONT = MAIN_FONT
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.setFont(self.GROUPBOX_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
class SurfaceGroupBox(CustomGroupBox):
    
    STEP = 10
    MAXIMUM = 10 ** 6
    DEFAULT_VALUE = 10 ** 2
    
    def __init__(
        self, 
        combobox: CustomLengthComboBox,
        parent: QWidget | None = None
    ) -> None:
        super().__init__("Габариты земельного участка", parent)
        self.combobox = combobox
        self.MEASUREMENT_LABEL_FIXED_WIDTH = MAIN_FONT_METRICS.horizontalAdvance(
            max(CustomLengthComboBox.LENGTH_FULL_FORM, key = len)
        )
        self.__setup()
        
    def __set_part(
        self, 
        label_text: str, 
        width: int,
        function: Callable,
        combobox: CustomLengthComboBox, 
        main_layout: QVBoxLayout | QHBoxLayout
    ) -> Tuple[CustomDoubleSpinBox, CustomLabel]:
        layout = QHBoxLayout()
        
        label = CustomLabel(label_text)
        result = CustomLabel()
        result.setFixedWidth(width)
        
        spinbox = CustomDoubleSpinBox()
        spinbox.setSingleStep(self.STEP)
        spinbox.setValue(self.DEFAULT_VALUE)
        spinbox.setMaximum(self.MAXIMUM)
        spinbox.valueChanged.connect(
            lambda value: CustomLabel._set_label_text(result, function, value, combobox.currentText())
        )
        
        CustomLabel._set_label_text(result, function, spinbox.value(), combobox.currentText())
        
        layout.addWidget(label)
        layout.addWidget(spinbox)
        layout.addWidget(result)
        
        main_layout.addLayout(layout)
        
        return spinbox, result
        
    def __set_surface_part(
        self, 
        label_text: str,
        main_layout: QVBoxLayout | QHBoxLayout
    ) -> Tuple[CustomDoubleSpinBox, CustomLabel]:
        return self.__set_part(
            label_text,
            self.MEASUREMENT_LABEL_FIXED_WIDTH, 
            _find_length_form, 
            self.combobox,
            main_layout
        )
        
    def __setup(self) -> None:
        layout = QVBoxLayout()
        
        self.length_spinbox, self.length_label = self.__set_surface_part(
            "Длина земельного участка:", 
            layout
        )
        self.width_spinbox, self.width_label = self.__set_surface_part(
            "Ширина земельного участка:", 
            layout
        )
        
        self.setLayout(layout)
        
    def __set_label_text(self, label: CustomLabel, value: object) -> None:
        CustomLabel._set_label_text(label, _find_length_form, value, self.combobox.currentText())
        
    def _set_label_text(self) -> None:
        self.__set_label_text(self.length_label, self.length_spinbox.value())
        self.__set_label_text(self.width_label, self.width_spinbox.value())
        

class CountedGroupBox(CustomGroupBox):
    
    def __init__(
        self, 
        combobox: CustomMoneyComboBox,
        parent: QWidget | None = None
    ) -> None:
        super().__init__("Расчитанные значения", parent)
        self.combobox = combobox
        self.MEASUREMENT_LABEL_FIXED_WIDTH = MAIN_FONT_METRICS.horizontalAdvance(
            max(CustomMoneyComboBox.MONEY_FULL_FORM, key = len)
        )
        self.__setup()
        
    def _set_part(self, title: str) -> Tuple[CustomBoldLabel, CustomBoldLabel]:
        layout = QHBoxLayout()
        
        label = CustomLabel(title)
        
        value_label = CustomBoldLabel()
        value_label.setFont(NUMBER_BOLD_FONT)
        # value_label.setStyleSheet("color: blue;")
        value_label.setFixedWidth(100)
        
        measurement_label = CustomLabel()
        # measurement_label.setStyleSheet("color: blue;")
        measurement_label.setFixedWidth(self.MEASUREMENT_LABEL_FIXED_WIDTH)
        
        layout.addWidget(label)
        layout.addWidget(value_label)
        layout.addWidget(measurement_label)
        
        self._layout.addLayout(layout)
        
        return value_label, measurement_label
        
    def _set_separator(self) -> None:
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        self._layout.addWidget(separator)
        
    def __setup(self) -> None:
        self._layout = QVBoxLayout(self)
        
        self.necessary_income_value_label, self.necessary_income_measurement_label = \
            self._set_part("Доход с застройки земельного участка (обязательные объекты):")
        self.chosen_income_value_label, self.chosen_income_measurement_label = \
            self._set_part("Доход с застройки земельного участка (необязательные объекты):")
        self.result_income_value_label, self.result_income_measurement_label = \
            self._set_part("Итоговый доход с застройки земельного участка:")
        
        self._set_separator()
        
        self.necessary_cost_value_label, self.necessary_cost_measurement_label = \
            self._set_part("Затраты на застройку земельного участка (обязательные объекты):")
        self.chosen_cost_value_label, self.chosen_cost_measurement_label = \
            self._set_part("Затраты на застройку земельного участка (необязательные объекты):")
        self.result_cost_value_label, self.result_cost_measurement_label = \
            self._set_part("Итоговые затраты на застройку земельного участка:")
            
        self._set_separator()
            
        self.necessary_profit_value_label, self.necessary_profit_measurement_label = \
            self._set_part("Прибыль с застройки земельного участка (обязательные объекты):")
        self.chosen_profit_value_label, self.chosen_profit_measurement_label = \
            self._set_part("Прибыль с застройки земельного участка (необязательные объекты):")
        self.result_profit_value_label, self.result_profit_measurement_label = \
            self._set_part("Итоговая прибыль с застройки земельного участка:")