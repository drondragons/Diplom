from typing import Callable

from PyQt6.QtWidgets import QLabel, QWidget

from .font import MAIN_FONT, MAIN_BOLD_FONT


__all__ = [
    "CustomLabel",
    "CustomBoldLabel",
]


class CustomLabel(QLabel):
    
    LABEL_FONT = MAIN_FONT
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.setFont(self.LABEL_FONT)
        
    @staticmethod
    def _set_label_text(label: QLabel, function: Callable, value: object, text: str) -> None:
        label.setText(function(value, text))
        
        
class CustomBoldLabel(CustomLabel):
    
    LABEL_FONT = MAIN_BOLD_FONT
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)