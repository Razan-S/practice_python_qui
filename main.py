import sys, os
import enum
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtCore import Qt

class Style:
    class Color(enum.Enum):
        primary = "#3F7D58"
        secondary = "#EFEFEF"
        red = "#EC5228"
        orange = "#EF9651"


class LandingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Practice Python GUI")
        self.setGeometry(50, 100, 400, 900)
        
        central_widget = QWidget(self)
        central_widget.setStyleSheet(f"background-color: {Style.Color.secondary.value};")
        self.setCentralWidget(central_widget)
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel("TRAFFIC", self)
        self.label.setStyleSheet(f"font-size: 20px; font-weight: bold; padding: 20px; color: {Style.Color.primary.value};")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.drag_drop_widget = DragDropFileWidget()
        
        self.button = QPushButton("Let's Control", self)
        self.button.setStyleSheet(f"background-color: {Style.Color.orange.value}; color: {Style.Color.secondary.value}; padding 10px 20px;")
        self.button.clicked.connect(self.show_file_contents)
        
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.drag_drop_widget)
        self.layout.addWidget(self.button)
        central_widget.setLayout(self.layout)
        
    def show_file_contents(self):
        path = self.drag_drop_widget.get_file_path()
        if path and path is not None:
            # print(path)
            print(f"File Path: {path}") if os.path.exists(path) else print("File not found")
        else:
            print("No file selected")

    
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
            styleLabel = f"border: 2px dashed {Style.Color.primary.value}; padding: 20px; color: {Style.Color.primary.value};"
            styleButton = f"background-color: {Style.Color.primary.value}; color: {Style.Color.secondary.value}; padding 10px 20px;" 
        else:
            styleLabel = f"border: 2px dashed {Style.Color.red.value}; padding: 20px; color: {Style.Color.red.value};"
            styleButton = f"background-color: {Style.Color.red.value}; color: {Style.Color.secondary.value}; padding 10px 20px;"

        self.label.setStyleSheet(styleLabel)
        self.button.setStyleSheet(styleButton)
        self.clearB.setStyleSheet(styleButton)
      
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
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LandingApp()
    window.show()
    sys.exit(app.exec())