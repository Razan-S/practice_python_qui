from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from assets.style import Style
from assets.enum import PageName
from components.back_button import TriangleButton


class Intersection(QWidget):
    switch_page_signal = pyqtSignal(PageName, str)

    def __init__(self, intersection=None):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header = QHBoxLayout()
        self.layout.addLayout(self.header)

        self.title = QLabel("Information", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setWordWrap(True)

        self.back_button = TriangleButton()
        self.back_button.setFixedSize(50, 50)
        self.back_button.clicked.connect(lambda: self.switch_page_signal.emit(PageName.LANDING, ""))
        
        self.header.addWidget(self.back_button, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.header.addStretch(1)
        self.header.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.header.addStretch(1)

        self.setStyle()

    def setStyle(self):
        self.setStyleSheet(f"""
            QLabel {{
                color: {Style.Color.primary.value};
            }}
            QWidget {{
                background-color: {Style.Color.secondary.value};
            }}
        """)

        self.title.setFont(QFont(Style.InterFont.EXTRABOLD.value, 20))