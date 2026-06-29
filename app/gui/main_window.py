from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout
)

from app.gui.sidebar import Sidebar
from app.gui.dashboard import Dashboard


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("YaiZa Professional")
        self.resize(1600, 900)

        container = QWidget()
        self.setCentralWidget(container)

        layout = QHBoxLayout(container)

        self.sidebar = Sidebar()
        self.dashboard = Dashboard()

        layout.addWidget(self.sidebar)
        layout.addWidget(self.dashboard)
