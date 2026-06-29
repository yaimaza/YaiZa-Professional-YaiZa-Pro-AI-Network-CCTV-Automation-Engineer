from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("YaiZa Professional Dashboard")

        layout.addWidget(title)
