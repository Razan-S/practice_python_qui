import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel
from components.landing import LandingApp
from assets.style import style, setupFont
from assets.enum import PageName

from components.selecting import Selecting
from components.Intersection import Intersection
from components.back_button import TriangleButton

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.landing_ui()

    def landing_ui(self):
        self.setWindowTitle("Traffic Control")
        self.setGeometry(50, 60, 400, 700)
        # self.setFixedSize(400, 700)

        self.current_page = LandingApp()
        self.setCentralWidget(self.current_page)

        self.current_page.switch_page_signal.connect(self.SwitchPage)

    def intersection_ui(self):
        self.setWindowTitle("Select Intersection")
        self.setGeometry(50, 60, 600, 700)
        # self.setFixedSize(600, 700)

        # self.current_page = Selecting(["Intersection 1", "Intersection 2", "Intersection 3"])
        self.current_page = Intersection()
        self.setCentralWidget(self.current_page)
        self.current_page.switch_page_signal.connect(self.SwitchPage)

    def traffic_light_ui(self):
        self.setWindowTitle("Control Traffic Light")
        self.setGeometry(50, 60, 600, 700)
        # self.setFixedSize(600, 700)

    def SwitchPage(self, page, details=""):
        match page:
            case PageName.LANDING:
                self.path = details
                self.landing_ui()
            case PageName.INTERSECTION:
                self.intersection_ui()
            case PageName.TRAFFIClIGHT:
                self.traffic_light_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    setupFont()
    style(app)

    window = MainApp()
    window.show()
    sys.exit(app.exec())