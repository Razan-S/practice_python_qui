from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, pyqtSignal
from assets.style import Style
import os

from components.popup import Popup
from assets.enum import PageName, PopupType

class LandingApp(QWidget):
    switch_page_signal = pyqtSignal(PageName, str)

    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Practice Python GUI")
        self.setGeometry(50, 60, 400, 700)
        self.setFixedSize(400, 700)
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.label = QLabel("TRAFFIC\nCONTROL\nINTERFACE", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.label.setWordWrap(True)
        
        self.drag_drop_widget = DragDropFileWidget()
        
        self.button = QPushButton("GO CONTROL!", self)
        self.button.clicked.connect(self.load_simulation)

        self.setLandingStyle()
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.drag_drop_widget)
        self.layout.addWidget(self.button)
        
    def show_file_contents(self):
        path = self.drag_drop_widget.get_file_path()
        if path and path is not None:
            print(f"File Path: {path}") if os.path.exists(path) else print("File not found")
        else:
            print("No file selected")

    def load_simulation(self):
        path = self.drag_drop_widget.get_file_path()
        if path and path is not None:
            self.switch_page_signal.emit(PageName.INTERSECTION, path)
        else:
            popup = Popup("Please select a SUMO config file before proceed", title="Error", message_type=PopupType.ERROR)
            popup.show()
            self.popup = popup

    def setLandingStyle(self):
        self.label.setStyleSheet(f"""
            QLabel {{
                color: {Style.Color.primary.value};
            }}
        """)

        self.button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {Style.Color.primary.value};
                    color: {Style.Color.secondary.value};
                    padding: 10px 20px;
                }}
                QPushButton:hover {{
                    background-color: {Style.Color.secondary.value};
                    color: {Style.Color.primary.value};
                    border: 2px solid {Style.Color.primary.value};
                }}
                QPushButton:pressed {{
                    background-color: #2B6944;
                    color: {Style.Color.secondary.value};
                }}
            """)
        
        self.label.setFont(QFont(Style.InterFont.BLACK.value, 32))
        self.button.setFont(QFont(Style.InterFont.EXTRABOLD.value, 24))

class DragDropFileWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.path = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Drag & Drop File or Select from Dialog")
        self.setGeometry(100, 100, 400, 200)
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("Drag & Drop a file here or use the button to select one", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.button = QPushButton("Select File", self)
        self.button.clicked.connect(self.open_file_dialog)
        
        self.clearB = QPushButton("Clear", self)
        self.clearB.clicked.connect(self.clearing)
        
        self.toolbar = QHBoxLayout()
        self.toolbar.addWidget(self.button)
        self.toolbar.addWidget(self.clearB)
        
        self.setUploadStyle(True)
        
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.toolbar)
        self.setLayout(self.layout)
        
        self.setAcceptDrops(True)
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            self.set_file_path(file_path) if self.check_valid_file_type(file_path) else None
    
    def open_file_dialog(self):
        self.fileDialog = QFileDialog()
        self.fileDialog.setNameFilter("SUMO config (*.sumocfg)")
        
        file_path, _ = self.fileDialog.getOpenFileName(self, "Select a File", )
        if file_path:
            self.set_file_path(file_path) if self.check_valid_file_type(file_path) else None
    
    def check_valid_file_type(self, file_path):
        if file_path.endswith(".sumocfg"):
            self.setUploadStyle(True)
            return True
        else:
            self.label.setText("Invalid file type. Please select a SUMO config file")
            self.setUploadStyle(False)
            return False
    
    def setUploadStyle(self, isValid):
        if isValid:
            styleLabel = f"border: 2px dashed {Style.Color.primary.value}; padding: 20px; color: {Style.Color.primary.value}; background-color: white;"
            styleButton = f"""
                QPushButton {{
                    background-color: {Style.Color.primary.value}; 
                    color: {Style.Color.secondary.value}; 
                    padding: 10px 20px;
                }}
                QPushButton:hover {{
                    background-color: {Style.Color.secondary.value};
                    color: {Style.Color.primary.value};
                    border: 2px solid {Style.Color.primary.value};
                }}
            """
        else:
            styleLabel = f"border: 2px dashed {Style.Color.red.value}; padding: 20px; color: {Style.Color.red.value}; background-color: white;"
            styleButton = f"""
                QPushButton {{
                    background-color: {Style.Color.red.value}; 
                    color: {Style.Color.secondary.value}; 
                    padding: 10px 20px;
                }}
                QPushButton:hover {{
                    background-color: #B33715;
                    color: {Style.Color.secondary.value};
                }}
            """

        self.label.setStyleSheet(styleLabel)
        self.label.setFont(QFont(Style.InterFont.REGULAR.value, 9))
        self.button.setStyleSheet(styleButton)
        self.button.setFont(QFont(Style.InterFont.MEDIUM.value, 12))
        self.clearB.setStyleSheet(styleButton)
        self.clearB.setFont(QFont(Style.InterFont.MEDIUM.value, 12))
      
    def set_file_path(self, file_path):
        file_path_label = None
        (file_path_label := file_path) if len(file_path) < 30 else (file_path_label := f"{file_path[:30]}...")
        self.path = os.path.abspath(file_path)
        
        self.label.setText(f"Selected File: {file_path_label}")
        self.label.setToolTip(file_path)
               
    def get_file_path(self):
        if self.path and self.path is not None:
            return self.path if os.path.exists(self.path) else None
        return None
    
    def clearing(self):
        self.path = None
        self.label.setText("Drag & Drop a file here or use the button to select one")

        self.setUploadStyle(True)
        self.label.setToolTip(None)