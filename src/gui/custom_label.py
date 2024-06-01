from typing import Callable

from PyQt6.QtWidgets import QLabel, QWidget

from .font import MAIN_FONT


__all__ = [
    "CustomLabel",
]


class CustomLabel(QLabel):
    
    LABEL_FONT = MAIN_FONT
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.setFont(self.LABEL_FONT)
        
    @staticmethod
    def _set_label_text(label: QLabel, function: Callable, value: object, text: str) -> None:
        print("Custom label _set_label_text", function(value, text))
        label.setText(function(value, text))