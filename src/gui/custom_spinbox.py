from PyQt6.QtGui import QFont, QKeyEvent
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDoubleSpinBox, QWidget

from .. import _get_pretty_number
from .. import DEFAULT_NUMBER_MAXIMUM


__all__ = [
    "CustomSpinBox",
    "CustomIntSpinBox",
    "CustomDoubleSpinBox",
]


class CustomSpinBox(QDoubleSpinBox):
    
    SPINBOX_FONT = QFont("Times New Roman", 12)
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.SPINBOX_FONT.setBold(True)
        
        self.setFont(self.SPINBOX_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setRange(1, DEFAULT_NUMBER_MAXIMUM)
        self.setSingleStep(1_000)
        self.setValue(1_000_000_000)
        self.setGroupSeparatorShown(True)
        self.setFixedWidth(300)
        
        
class CustomIntSpinBox(CustomSpinBox):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.setDecimals(0)
        
    
class CustomDoubleSpinBox(CustomSpinBox):
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.setDecimals(6)
        self.valueChanged.connect(self.update_decimals)
        
    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        super().keyPressEvent(event)
        if isinstance(_get_pretty_number(self.value()), int) and \
            event.key() == Qt.Key.Key_Comma or event.key() == Qt.Key.Key_Period:
            self.setDecimals(6)
        
    def update_decimals(self) -> None:
        self.textChanged.emit
        if isinstance(_get_pretty_number(self.value()), int):
            self.setDecimals(0)