from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from assets.style import Style
from assets.enum import PopupType

class Popup(QMainWindow):
    def __init__(self, message, title="Message", message_type:PopupType=PopupType.INFO):
        super().__init__()
        self.title = title
        self.message = message
        self.message_type = message_type
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 300, 200)

        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Dialog)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)

        self.label = QLabel(self.message)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setFont(QFont(Style.InterFont.BLACK.value))
     
        self.close_button = QPushButton("OK")
        self.close_button.setFont(QFont(Style.InterFont.BLACK.value))
        self.close_button.setFixedWidth(100)
        self.close_button.clicked.connect(self.close)

        self.setStyle()

        layout.addStretch()
        layout.addWidget(self.label)
        layout.addStretch()
        layout.addWidget(self.close_button, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(0)

    def setStyle(self):
        match self.message_type:
            case PopupType.INFO:
                label_style = "color: black;"
                button_bg = "black"
                button_fg = Style.Color.secondary.value
            case PopupType.WARNING:
                label_style = f"color: {Style.Color.orange.value};"
                button_bg = Style.Color.orange.value
                button_fg = Style.Color.secondary.value
            case PopupType.ERROR:
                label_style = f"color: {Style.Color.red.value};"
                button_bg = Style.Color.red.value
                button_fg = Style.Color.secondary.value
            case PopupType.SUCCESS:
                label_style = f"color: {Style.Color.primary.value};"
                button_bg = Style.Color.primary.value
                button_fg = Style.Color.secondary.value
            case _:
                label_style = "color: black;"
                button_bg = "black"
                button_fg = Style.Color.secondary.value

        button_style = f"""
            QPushButton {{
                background-color: {button_bg}; 
                color: {button_fg};
                border-radius: 5px;
                padding: 5px;
            }}
            QPushButton:hover {{
                background-color: {button_fg}; 
                color: {button_bg};
                border: 2px solid {button_bg};
            }}
        """

        self.label.setStyleSheet(label_style)
        self.close_button.setStyleSheet(button_style)
