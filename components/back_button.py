from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QPolygon, QColor
from PyQt6.QtCore import QPoint
from assets.style import Style

class TriangleButton(QPushButton):
    def __init__(self, parent="Back"):
        super().__init__(parent)
        self.setFixedSize(50, 50)  # Set button size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        triangle = QPolygon([
            QPoint(35, 10),
            QPoint(35, 40),
            QPoint(10, 25)
        ])
        
        painter.setBrush(QColor(239, 150, 81))
        painter.drawPolygon(triangle)