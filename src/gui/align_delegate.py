from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStyledItemDelegate


__all__ = [
    "AlignDelegate",
]


class AlignDelegate(QStyledItemDelegate):
    
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter