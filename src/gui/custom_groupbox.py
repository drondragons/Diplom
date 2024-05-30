from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGroupBox, QWidget#, QVBoxLayout, QHBoxLayout

# from . import _find_length_form
# from .custom_label import CustomLabel
# from .custom_spinbox import CustomDoubleSpinBox


__all__ = [
    "CustomGroupBox",
]


class CustomGroupBox(QGroupBox):
    
    GROUPBOX_FONT = QFont("Times New Roman", 12)
    
    def __init__(self, text: str = str(), parent: QWidget | None = None) -> None:
        super().__init__(text, parent)
        
        self.GROUPBOX_FONT.setBold(True)
        
        self.setFont(self.GROUPBOX_FONT)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
# class SurfaceGroupBox(CustomGroupBox):
    
#     TITLE = "Габариты земельного участка"
    
#     def __init__(self, parent: QWidget | None = None) -> None:
#         super().__init__(self.TITLE, parent)
        
#         surface_layout = QVBoxLayout()
        
#         surface_width_layout = QHBoxLayout()
#         surface_width_label = CustomLabel("Ширина земельного участка")
#         self.surface_width_spinbox = CustomDoubleSpinBox()
#         self.surface_width_spinbox.valueChanged.connect(self.__update_surface_width)
#         self.surface_width_measurement_label = CustomLabel()
#         surface_width_layout.addWidget(surface_width_label)
#         surface_width_layout.addWidget(self.surface_width_spinbox)
#         surface_width_layout.addWidget(self.surface_width_measurement_label)

#         surface_length_layout = QHBoxLayout()
#         surface_length_label = CustomLabel("Длина земельного участка")
#         self.surface_length_spinbox = CustomDoubleSpinBox()
#         surface_length_layout.addWidget(surface_length_label)
#         surface_length_layout.addWidget(self.surface_length_spinbox)

#         surface_layout.addLayout(surface_length_layout)
#         surface_layout.addLayout(surface_width_layout)
        
#         self.setLayout(surface_layout)
        
#     def __update_surface_width(self, value: float) -> None:
        
#     def __set_value(self, value: float) -> None:
#         self.surface_width_measurement_label.setText(
#             _find_length_form(
#                 value,
#                 self.
#             )
#         )