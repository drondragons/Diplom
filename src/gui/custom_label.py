from typing import Callable

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget


__all__ = [
    "CustomLabel",
]


class CustomLabel(QLabel):
    
    LABEL_FONT = QFont("Times New Roman", 12)
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        
        self.LABEL_FONT.setBold(True)
        
        self.setFont(self.LABEL_FONT)
        
    @staticmethod
    def _set_label_text(label: QLabel, function: Callable, value: object, text: str) -> None:
        label.setText(function(value, text))