from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel
from PyQt6.QtCore import Qt, pyqtSignal
from assets.style import Style

class Selecting(QWidget):
    def __init__(self, choices):
        super().__init__()
        self.choices = choices
        self.selected_button = None
        self.selected_value = None
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Select Intersection")
        self.setGeometry(50, 60, 600, 350)
        # self.setFixedSize(600, 350)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        for i, choice in enumerate(self.choices):
            button = QPushButton(choice)
            button.clicked.connect(lambda checked, b=button: self.clicked_event(b))
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            if i % 2 == 0:
                self.layout.addWidget(button, i // 2, 0)
            else:
                self.layout.addWidget(button, i // 2, 1)

    def clicked_event(self, button):
        if self.selected_button == button:
            button.setStyleSheet(f"background-color: {Style.Color.primary.value};")
            return

        if self.selected_button:
            self.selected_button.setStyleSheet(f"background-color: {Style.Color.primary.value};")

        self.selected_button = button
        self.selected_value = button.text()

        button.setStyleSheet(f"background-color: {Style.Color.red.value};")

    def get_selected_value(self):
        return self.selected_value