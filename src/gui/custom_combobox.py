from typing import List, Callable

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QWidget, QHBoxLayout

from .font import MAIN_FONT
from .custom_label import CustomLabel
from .align_delegate import AlignDelegate

from ..measurement.money import Money
from ..measurement.length import Length, Meter


__all__ = [
    "CustomComboBox",
    "CustomMoneyComboBox",
    "CustomLengthComboBox",
]


class CustomComboBox(QComboBox):
    
    COMBOBOX_FONT = MAIN_FONT
    
    def __init__(self, items: List[object] = list(), parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFont(self.COMBOBOX_FONT)
        delegate = AlignDelegate(self)
        self.setItemDelegate(delegate)
        self.setEditable(True)
        self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit().setReadOnly(True)
        self.addItems(items)
        
    @staticmethod
    def _set_combobox_default_text(combobox: QComboBox, text: str) -> None:
        index = combobox.findText(text)
        if index < 0:
            index = 0
        combobox.setCurrentIndex(index)
        combobox.setCurrentText(combobox.itemText(index))
    
    def _setup(
        self,
        _type: str,
        title: str,
        function: Callable,
    ) -> None:
        self._set_combobox_default_text(self, _type)
        
        self._layout = QHBoxLayout()
        
        self.label = CustomLabel(title)
        
        self.currentIndexChanged.connect(function)
        
        self._layout.addWidget(self.label)
        self._layout.addWidget(self)
        
    def is_visible(self, is_visible: bool = False) -> None:
        self.label.setVisible(is_visible)
        self.setVisible(is_visible)
    
        
class CustomMoneyComboBox(CustomComboBox):
    
    MONEY_FULL_FORM = \
        [Money.FULL_FORM] + [subclass.FULL_FORM for subclass in Money.__subclasses__()]
    
    def __init__(self, function: Callable, parent: QWidget | None = None) -> None:
        super().__init__(self.MONEY_FULL_FORM, parent)
        self.__setup(function)
        
    def __setup(self, function: Callable) -> None:
        self._setup("рубль", "Валюта:", function)
        

class CustomLengthComboBox(CustomComboBox):

    LENGTH_FULL_FORM = \
        [Length.FULL_FORM, Meter.FULL_FORM] + \
        [subclass.FULL_FORM for subclass in Meter.__subclasses__()]

    def __init__(self, function: Callable, parent: QWidget | None = None) -> None:
        super().__init__(self.LENGTH_FULL_FORM, parent)
        self.__setup(function)
        
    def __setup(self, function: Callable) -> None:
        self._setup("метр", "Единица измерения:", function)