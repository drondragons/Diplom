from PyQt6.QtWidgets import QPushButton, QWidget

from .font import MAIN_BOLD_FONT


__all__ = [
    "CustomPushButton",
]


class CustomPushButton(QPushButton):
    
    PUSHBUTTON_FONT = MAIN_BOLD_FONT
    
    def __init__(self, text: str, parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        self.setFont(self.PUSHBUTTON_FONT)