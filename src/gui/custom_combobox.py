from typing import List

from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox, QWidget

from .align_delegate import AlignDelegate


__all__ = [
    "CustomComboBox",
    "CustomMoneyComboBox",
    "CustomLengthComboBox",
]


class CustomComboBox(QComboBox):
    
    COMBOBOX_FONT = QFont("Times New Roman", 12)
    
    def __init__(self, items: List[object] = list(), parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.COMBOBOX_FONT.setBold(True)
        
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
        
        
class CustomMoneyComboBox(CustomComboBox):
    
    def __init__(self, items: List[object] = list(), parent: QWidget | None = None) -> None:
        super().__init__(items, parent)
        
        self._set_combobox_default_text(self, "рубль")
        

class CustomLengthComboBox(CustomComboBox):

    def __init__(self, items: List[object] = list(), parent: QWidget | None = None) -> None:
        super().__init__(items, parent)
        
        self._set_combobox_default_text(self, "метр")