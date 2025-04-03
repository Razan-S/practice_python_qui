import enum

class PopupType(enum.Enum):
    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"
    SUCCESS = "Success"

class PageName(enum.Enum):
    LANDING = "Landing"
    INTERSECTION = "Intersection"
    TRAFFIClIGHT = "TrafficLight"

class GraphProperties(enum.Enum):
    LINEAR = "Linear"
    CIRCULAR = "Circular"
    GRID = "Grid"
    RANDOM = "Random"