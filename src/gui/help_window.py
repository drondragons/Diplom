from PyQt6.QtGui import QFont, QShowEvent, QGuiApplication
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QStyle, QLabel, QVBoxLayout, QFrame


__all__ = [
    "HelpWindow",
]


class HelpWindow(QWidget):
    
    TABULATION = "\t" * 7
    
    HELP_WINDOW_TITLE = """Справочная информация."""
    
    RESULT_DESCRIPTION = f"""{TABULATION}По окончании \
работы программы будет показана схема расположения \
объектов строительства на земельном участке."""
    
    MAXIMUM_WIDTH = 600
    
    def __init__(self) -> None:
        super().__init__()
        self.__setup_help_window()
        
    def __setup_help_window(self) -> None:
        self.__set_window_title()
        self.__set_window_icon()
        self.__set_window_geometry()
        self.__add_help_text()
        
    def __set_window_title(self) -> None:
        self.setWindowTitle(self.HELP_WINDOW_TITLE)
        
    def __set_window_icon(self) -> None:
        help_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarContextHelpButton
        )
        self.setWindowIcon(help_icon)
        
    def __set_window_geometry(self) -> None:
        self.setFixedWidth(self.MAXIMUM_WIDTH)
        
    def __add_help_text(self) -> None:
        heading_font = QFont("Times New Roman", 14)
        heading_font.setBold(True)
        
        main_font = QFont("Times New Roman", 12)
        
        main_layout = QVBoxLayout()
        
        main_heading = QLabel("Справочная информация")
        main_heading.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        main_heading.setFont(heading_font)
        
        horizontal_separator_line = QFrame()
        horizontal_separator_line.setFrameShape(QFrame.Shape.HLine)
        
        result_description = QLabel(self.RESULT_DESCRIPTION)
        result_description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        result_description.setFont(main_font)
        result_description.setWordWrap(True)
        
        main_layout.addWidget(main_heading)
        main_layout.addWidget(horizontal_separator_line)
        main_layout.addWidget(result_description)
        
        self.setLayout(main_layout)
        
    def showEvent(self, event: QShowEvent = None) -> None:
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        