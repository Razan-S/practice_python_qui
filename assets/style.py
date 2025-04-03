from PyQt6.QtGui import QFontDatabase
import os
import enum

class Style:
    class Color(enum.Enum):
        primary = "#3F7D58"
        secondary = "#EFEFEF"
        red = "#EC5228"
        orange = "#EF9651"
    class InterFont(enum.Enum):
        REGULAR = "Inter"
        THIN = "Inter Thin"
        EXTRALIGHT = "Inter ExtraLight"
        LIGHT = "Inter Light"
        MEDIUM = "Inter Medium"
        SEMIBOLD = "Inter SemiBold"
        EXTRABOLD = "Inter ExtraBold"
        BLACK = "Inter Black"

def setupFont():
    inter = QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "fonts", "Inter", "Inter-VariableFont_opsz,wght.ttf"))
    if inter < 0: print("Error")

    families = QFontDatabase.applicationFontFamilies(inter)
    print(families)

def style(app):
    app.setStyle("Windows")
    app.setStyleSheet(f"""
        QMainWindow {{
            background-color: {Style.Color.secondary.value};
        }}              
        QPushButton {{
            background-color: {Style.Color.primary.value};
            color: {Style.Color.secondary.value};
        }}
        QPushButton:hover {{
            background-color: {Style.Color.secondary.value};
            color: {Style.Color.primary.value};
            border: 2px solid {Style.Color.primary.value};
        }}
    """)