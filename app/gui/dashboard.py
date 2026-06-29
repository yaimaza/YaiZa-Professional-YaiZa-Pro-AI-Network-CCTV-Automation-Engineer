from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class Dashboard(QWidget):
    """Main dashboard view showing system status and metrics"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize dashboard UI"""
        layout = QVBoxLayout()
        
        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        self.setLayout(layout)
