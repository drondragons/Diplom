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

from . import _find_money_form, _find_length_form
from .help_window import HelpWindow
from .custom_label import CustomLabel
from .custom_spinbox import CustomIntSpinBox, CustomDoubleSpinBox
from .custom_groupbox import CustomGroupBox
from .custom_combobox import CustomMoneyComboBox, CustomLengthComboBox

from ..measurement.money import Money
from ..measurement.length import Length, Meter


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
    
    MONEY_FULL_FORM = \
        [Money.FULL_FORM] + [subclass.FULL_FORM for subclass in Money.__subclasses__()]
        
    LENGTH_FULL_FORM = \
        [Length.FULL_FORM, Meter.FULL_FORM] + \
        [subclass.FULL_FORM for subclass in Meter.__subclasses__()]
    
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
        self.__set_money_layout()
        self.__set_length_layout(True)
        self.__set_budget_layout()
        self.__set_surface()
        
    def __set_surface(self) -> None:
        surface_groupbox = CustomGroupBox("Габариты земельного участка")
        
        surface_layout = QVBoxLayout()
        
        surface_width_layout = QHBoxLayout()
        surface_width_label = CustomLabel("Ширина земельного участка:")
        self.surface_width_spinbox = CustomDoubleSpinBox()
        self.surface_width_spinbox.valueChanged.connect(self.__update_surface_width)
        self.surface_width_measurement_label = CustomLabel()
        self.surface_width_measurement_label.setFixedWidth(140)
        self.surface_width_measurement_label.setText(
            _find_length_form(
                self.surface_width_spinbox.value(),
                self.length_combobox.currentText()
            )
        )
        surface_width_layout.addWidget(surface_width_label)
        surface_width_layout.addWidget(self.surface_width_spinbox)
        surface_width_layout.addWidget(self.surface_width_measurement_label)

        # surface_length_layout = QHBoxLayout()
        # surface_length_label = CustomLabel("Длина земельного участка")
        # self.surface_length_spinbox = CustomIntSpinBox()
        # surface_length_layout.addWidget(surface_length_label)
        # surface_length_layout.addWidget(self.surface_length_spinbox)

        # surface_layout.addLayout(surface_length_layout)
        surface_layout.addLayout(surface_width_layout)
        
        surface_groupbox.setLayout(surface_layout)
        
        self.input_layout.addWidget(surface_groupbox)
        
        # surface_layout = QVBoxLayout()
        
        # surface_size_layout = QVBoxLayout()
        # self.surface_width_spinbox = CustomIntSpinBox()
        # self.surface_length_spinbox = CustomIntSpinBox()
        # surface_size_layout.addWidget(self.surface_length_spinbox)
        # surface_size_layout.addWidget(self.surface_width_spinbox)
        
        # surface_title_layout = QVBoxLayout()
        # surface_width_label = CustomLabel("Ширина земельного участка:")
        # surface_length_label = CustomLabel("Длина земельного участка:")
        # surface_title_layout.addWidget(surface_length_label)
        # surface_title_layout.addWidget(surface_width_label)
        
        # surface_measurements_layout = QVBoxLayout()
        # self.surface_width_measurement_label = CustomLabel()
        # self.surface_width_measurement_label.setText(
        #     _find_length_form(
        #         self.surface_width_spinbox.value(),
        #         self.length_combobox.currentText()
        #     )
        # )
        # self.surface_length_measurement_label = CustomLabel()
        # self.surface_length_measurement_label.setText(
        #     _find_length_form(
        #         self.surface_length_spinbox.value(),
        #         self.length_combobox.currentText()
        #     )
        # )
        # surface_measurements_layout.addWidget(self.surface_length_measurement_label)
        # surface_measurements_layout.addWidget(self.surface_width_measurement_label)
        
        # surface_layout.addLayout(surface_title_layout)
        # surface_layout.addLayout(surface_size_layout)
        # surface_layout.addLayout(surface_measurements_layout)
        
        # surface_groupbox.setLayout(surface_layout)
        
        # self.input_layout.addWidget(surface_groupbox)
        
    def __update_surface_width(self, value: object) -> None:
        self.surface_width_measurement_label.setText(
            _find_length_form(
                value,
                self.length_combobox.currentText()
            )
        )
        
    def __set_money_layout(self, is_visible: bool = False) -> None:
        money_layout = QHBoxLayout()
        
        money_label = CustomLabel("Валюта:")
        money_label.setVisible(is_visible)
        
        self.money_combobox = CustomMoneyComboBox(self.MONEY_FULL_FORM)
        self.money_combobox.setVisible(is_visible)
        self.money_combobox.currentIndexChanged.connect(self.__money_combobox_changed)
        
        money_layout.addWidget(money_label)
        money_layout.addWidget(self.money_combobox)
        
        self.input_layout.addLayout(money_layout)
    
    def __money_combobox_changed(self) -> None:
        CustomLabel._set_label_text(
            self.budget_currency_label, 
            _find_money_form, 
            self.budget_spinbox.value(),
            self.money_combobox.currentText()
        )
        # self.budget_currency_label.setText(
        #     _find_money_form(
        #         self.budget_spinbox.value(), 
        #         self.money_combobox.currentText()
        #     )
        # )
        
    def __set_length_layout(self, is_visible: bool = False) -> None:
        length_layout = QHBoxLayout()
        
        length_label = CustomLabel("Единица измерения:")
        length_label.setVisible(is_visible)
        
        self.length_combobox = CustomLengthComboBox(self.LENGTH_FULL_FORM)
        self.length_combobox.setVisible(is_visible)
        self.length_combobox.currentIndexChanged.connect(self.__length_combobox_changed)
        
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_combobox)
        
        self.input_layout.addLayout(length_layout)
        
    def __length_combobox_changed(self) -> None:
        # self.surface_length_measurement_label.setText(
        #     _find_length_form(
        #         self.surface_length_spinbox.value(),
        #         self.length_combobox.currentText()
        #     )
        # )
        self.surface_width_measurement_label.setText(
            _find_length_form(
                self.surface_width_spinbox.value(),
                self.length_combobox.currentText()
            )
        )
        
    def __set_budget_layout(self) -> None:
        budget_layout = QHBoxLayout()
        
        budget_label = CustomLabel("Бюджет застройщика:")
        
        self.budget_spinbox = CustomIntSpinBox()
        
        self.budget_currency_label = CustomLabel()
        CustomLabel._set_label_text(
            self.budget_currency_label, 
            _find_money_form, 
            self.budget_spinbox.value(),
            self.money_combobox.currentText()
        )
        
        budget_layout.addWidget(budget_label)
        budget_layout.addWidget(self.budget_spinbox)
        budget_layout.addWidget(self.budget_currency_label)
        
        self.input_layout.addLayout(budget_layout)
        
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