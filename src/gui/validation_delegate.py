from typing import Type

from PyQt6.QtCore import QAbstractItemModel, QModelIndex, QObject
from PyQt6.QtWidgets import QStyledItemDelegate, QMessageBox, QTableWidgetItem

from ..validators import Validator
from ..value_objects.real import Real
from ..value_objects.title import Title


__all__ = [
    "ValidationDelegate",
]


class ValidationDelegate(QStyledItemDelegate):
    
    def __init__(self, class_type: Type, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.class_type = class_type
    
    def setModelData(
        self,
        editor: QTableWidgetItem,
        model: QAbstractItemModel,
        index: QModelIndex
    ) -> None:
        value = editor.text()
        try:
            if self.class_type == Title:
                self.class_type(value)
            else:
                if not value or value.isspace():
                    message = "\n\tСтрока не должна быть пустой! "
                    message += f"{Validator.validate_type_of_type(str, self.class_type)[1]}"
                    raise ValueError(message)
                self.class_type(Real(int(value)))
            model.setData(index, value)
            
        except Exception as exception:
            message = type(exception).__name__ + ":" + str(exception)
            QMessageBox.warning(None, "Ошибка ввода данных.", message)