import os
from PyQt6.QtGui import QIcon, QAction, QActionGroup, QGuiApplication, QShowEvent
from PyQt6.QtWidgets import QMainWindow, QStyle, QApplication

from .help_window import HelpWindow


__all__ = [
    "MainWindow",
]


class MainWindow(QMainWindow):
    
    MAIN_WINDOW_TITLE = """Дипломная работа. Метод размещения \
объектов строительства на земельном участке с использованием \
ограниченного рюкзака."""

    PROJECT_DIR = os.getcwd()
    CURRENT_DIR = os.path.join(PROJECT_DIR, "src", "gui", "img")
    
    MAIN_ICON_PATH = os.path.join(CURRENT_DIR, "bmstu-logo.pdf")
    
    def __init__(self, application: QApplication) -> None:
        super().__init__()
        self.application = application
        self.__setup_main_window()
        
    def __setup_main_window(self) -> None:
        self.__set_window_icon()
        self.__set_window_title()
        self.__set_menu_bar()
        self.showEvent()
        
    def __set_menu_bar(self) -> None:
        self.dark_theme_action = QAction("Тёмная тема", self)
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        
        self.light_theme_action = QAction("Светлая тема", self)
        self.light_theme_action.setCheckable(True)
        
        menubar = self.menuBar()
        settings_menu = menubar.addMenu("Настройки")
        
        desktop_icon = self.style().standardIcon(QStyle.StandardPixmap.SP_DesktopIcon)
        theme_menu = settings_menu.addMenu(desktop_icon, "Сменить тему")
        theme_menu.addAction(self.light_theme_action)
        theme_menu.addSeparator()
        theme_menu.addAction(self.dark_theme_action)
        
        help_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarContextHelpButton
        )
        help_action = QAction(help_icon, "Справка", self)
        help_action.triggered.connect(self.__show_help_window)
        settings_menu.addAction(help_action)

        action_group = QActionGroup(self)
        action_group.addAction(self.dark_theme_action)
        action_group.addAction(self.light_theme_action)
        action_group.triggered.connect(self.__change_theme)
    
    def __change_theme(self, action: QAction) -> None:
        if action == self.light_theme_action:
            self.application.setStyle("windowsvista")
            self.light_theme_action.setChecked(True)
        elif action == self.dark_theme_action:
            self.application.setStyle("fusion")
            self.dark_theme_action.setChecked(True)
        
    def __set_window_title(self) -> None:
        self.setWindowTitle(self.MAIN_WINDOW_TITLE)
        
    def __set_window_icon(self) -> None:
        self.setWindowIcon(QIcon(self.MAIN_ICON_PATH))
        
    def __show_help_window(self) -> None:
        self.help_window = HelpWindow()
        self.help_window.show()
        
    def showEvent(self, event: QShowEvent = None) -> None:
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self, event: QShowEvent) -> None:
        QApplication.closeAllWindows()