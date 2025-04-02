from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from assets.style import Style

class Popup(QMainWindow):
    def __init__(self, message, title="Message", message_type="info"):
        """
        Initialize a popup window
        
        :param message: Text message to display
        :param title: Window title (default: "Message")
        :param message_type: Type of message: "info", "success", "warning", or "error"
        """
        super().__init__()
        self.message_type = message_type
        self.init_ui(message, title)

    def init_ui(self, message, title):
        # Set window properties
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 300, 200)
        self.setFixedSize(150, 100)
        
        # Set window flags to make it a proper popup
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.Dialog)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout(central_widget)
        
        
        # Create and style message label
        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        font = QFont()
        font.setPointSize(11)
        label.setFont(font)
        label.setStyleSheet(f"color: {Style.Color.primary.value};")
        
        # Create close button
        close_button = QPushButton("OK")
        close_button.setFixedWidth(100)
        close_button.clicked.connect(self.close)
        
        # Add widgets to layout
        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(close_button, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(0)
        
    def get_style_color(self):
        """Return the color based on message type"""
        if self.message_type == "info":
            return "#3498db"  # Blue
        elif self.message_type == "success":
            return "#2ecc71"  # Green
        elif self.message_type == "warning":
            return "#f39c12"  # Orange
        elif self.message_type == "error":
            return "#e74c3c"  # Red
        else:
            return "#3498db"  # Default blue

# Usage examples:
# info_popup = Popup("This is an information message", title="Information", message_type="info")
# error_popup = Popup("Something went wrong!", title="Error", message_type="error")
# warning_popup = Popup("This action cannot be undone", title="Warning", message_type="warning")
# success_popup = Popup("Operation completed successfully", title="Success", message_type="success")
