from PyQt6.QtGui import QFont, QKeyEvent
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDoubleSpinBox, QWidget, QHBoxLayout

from . import _find_money_form
from .font import NUMBER_FONT
from .custom_label import CustomLabel
from .custom_combobox import CustomMoneyComboBox


__all__ = [
    "CustomSpinBox",
    "CustomIntSpinBox",
    "CustomDoubleSpinBox",
    "Budget",
]


class CustomSpinBox(QDoubleSpinBox):
    
    SPINBOX_MINIMUM = 1
    SPINBOX_MAXIMUM = 2 ** 48
    
    SPINBOX_STEP = 10 ** 3
    DEFAULT_VALUE = 10 ** 9
    
    FIXED_WIDTH = 3 * 10 ** 2
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFont(NUMBER_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setRange(self.SPINBOX_MINIMUM, self.SPINBOX_MAXIMUM)
        self.setSingleStep(self.SPINBOX_STEP)
        self.setValue(self.DEFAULT_VALUE)
        self.setGroupSeparatorShown(True)
        self.setFixedWidth(self.FIXED_WIDTH)
        
        
class CustomIntSpinBox(CustomSpinBox):
    
    MAXIMUM_DECIMALS = 0
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setDecimals(self.MAXIMUM_DECIMALS)
        
    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        if event.key() == Qt.Key.Key_Comma:
            return
        return super().keyPressEvent(event)
        
    
class CustomDoubleSpinBox(CustomSpinBox):
    
    MAXIMUM_DECIMALS = 2
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setDecimals(self.MAXIMUM_DECIMALS)
        
        
class Budget(CustomDoubleSpinBox):
    
    def __init__(
        self, 
        combobox: CustomMoneyComboBox,
        parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.combobox = combobox
        self.__setup()
        
    def __set(self, value: object) -> None:
        CustomLabel._set_label_text(self.currency_label, _find_money_form, value, self.combobox.currentText())
        
    def __setup(self) -> None:
        self._layout = QHBoxLayout()
        
        label = CustomLabel("Бюджет застройщика:")
        
        self.currency_label = CustomLabel()
        self.setValue(10 ** 10)
        self.__set(self.value())
        
        self.valueChanged.connect(lambda value: self.__set(value))
        
        self._layout.addWidget(label)
        self._layout.addWidget(self)
        self._layout.addWidget(self.currency_label)
    
    def _set_label_text(self) -> None:
        CustomLabel._set_label_text(
            self.currency_label,
            _find_money_form,
            self.value(),
            self.combobox.currentText()
        )