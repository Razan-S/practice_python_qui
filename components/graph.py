from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QBoxLayout
from PyQt6.QtCore import QTimer, Qt
from assets.style import Style
import pyqtgraph as pg
import numpy as np
import sys

class LinearGraph(QWidget):
    def __init__(self, title="Real-time Dynamic Plot", x_name="X Axis", y_name="Y Axis", size=(50,50)):
        super().__init__()
        self.widsize = size
        self.x_data = []
        self.y_data = []
        self.title = title
        self.x_name = x_name
        self.y_name = y_name

        self.init_ui()

    def init_ui(self):
        self.setGeometry(0, 0, self.widsize[0], self.widsize[1])
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.graph_widget = pg.PlotWidget()
        self.layout.addWidget(self.graph_widget, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.graph_widget.setBackground(Style.Color.secondary.value)
        self.graph_widget.setTitle(self.title, color=Style.Color.primary.value, size="15pt")
        self.graph_widget.setLabel("left", self.y_name, color=Style.Color.primary.value)
        self.graph_widget.setLabel("bottom", self.x_name, color=Style.Color.primary.value)
        self.graph_widget.showGrid(x=True, y=True)

        self.curve = self.graph_widget.plot(self.x_data, self.y_data, pen=pg.mkPen({'color':Style.Color.orange.value, 'width':2}))

    def update_plot(self, x=None, y=None):
        self.x_data.append(x)
        self.y_data.append(y)

        self.curve.setData(self.x_data, self.y_data)