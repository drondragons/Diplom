import os
from PyQt6.QtGui import (
    QIcon,
    QAction,
    QActionGroup,
    QGuiApplication,
    QShowEvent,
    QFont,
)
from PyQt6.QtWidgets import (
    QMainWindow, 
    QStyle,
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from .help_window import HelpWindow
from .custom_label import CustomLabel
from .custom_spinbox import Budget
from .custom_groupbox import SurfaceGroupBox
from .custom_combobox import CustomMoneyComboBox, CustomLengthComboBox


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
        self.__set_layouts()
        self.__set_input()
        self.__show_placement()
        self.__show_profit()
        self.showEvent()
        
    def __set_layouts(self) -> None:
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.main_layout = QVBoxLayout(self.main_widget)
        
        self.input_and_figure_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_and_figure_layout)
        
        self.output_layout = QVBoxLayout()
        self.main_layout.addLayout(self.input_and_figure_layout)
        
        self.input_layout = QVBoxLayout()
        self.input_and_figure_layout.addLayout(self.input_layout)
        
    def __set_input(self) -> None:
        self.__set_money_layout(True)
        self.__set_length_layout(True)
        self.__set_budget_layout()
        self.__set_surface()
        
    def __set_surface(self) -> None:
        self.surface_groupbox = SurfaceGroupBox(self.length_combobox)
        self.input_layout.addWidget(self.surface_groupbox)
        
    def __set_money_layout(self, is_visible: bool = False) -> None:
        self.money_combobox = CustomMoneyComboBox(self.__money_combobox_changed)
        self.money_combobox.is_visible(is_visible)
        self.input_layout.addLayout(self.money_combobox._layout)
    
    def __money_combobox_changed(self) -> None:
        self.budget_spinbox._set_label_text()
        
    def __set_length_layout(self, is_visible: bool = False) -> None:
        self.length_combobox = CustomLengthComboBox(self.__length_combobox_changed)
        self.length_combobox.is_visible(is_visible)
        self.input_layout.addLayout(self.length_combobox._layout)
        
    def __length_combobox_changed(self) -> None:
        self.surface_groupbox._set_label_text()
        
    def __set_budget_layout(self) -> None:
        self.budget_spinbox = Budget(self.money_combobox)
        self.input_layout.addLayout(self.budget_spinbox._layout)
        
    def __set_menu_bar(self) -> None:
        self.dark_theme_action = QAction("Тёмная тема", self)
        self.dark_theme_action.setCheckable(True)
        self.dark_theme_action.setChecked(True)
        
        self.light_theme_action = QAction("Светлая тема", self)
        self.light_theme_action.setCheckable(True)
        
        menubar = self.menuBar()
        menubar.setFont(QFont("Candara", 10))
        settings_menu = menubar.addMenu("Настройки")
        settings_menu.setFont(QFont("Candara", 10))
        
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
    
    def __show_placement(self) -> None:
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.input_and_figure_layout.addWidget(self.canvas)
        
        self.ax = self.figure.add_subplot(111)

        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        
        self.ax.set_title("Размещение объектов строительства на земельном участке", pad=20)
        self.ax.set_xlabel("Ширина земельного участка, в метрах", labelpad=7)
        self.ax.set_ylabel("Длина земельного участка, в метрах", labelpad=7)
        
        self.canvas.draw()
    
    def __show_profit(self) -> None:
        profit_layout = QHBoxLayout()
        self.output_layout.addChildLayout(profit_layout)
        
        profit_label = CustomLabel("Прибыль с застройки земельного участка")
        self.profit_label = CustomLabel()
        
        profit_layout.addWidget(profit_label)
        profit_layout.addWidget(self.profit_label)
    
    def showEvent(self, event: QShowEvent = None) -> None:
        qr = self.frameGeometry()           
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def closeEvent(self, event: QShowEvent) -> None:
        QApplication.closeAllWindows()