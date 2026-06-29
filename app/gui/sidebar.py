from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    """Sidebar navigation menu"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize sidebar UI"""
        layout = QVBoxLayout()
        
        # Add navigation buttons
        dashboard_btn = QPushButton("Dashboard")
        devices_btn = QPushButton("Devices")
        monitor_btn = QPushButton("Monitor")
        settings_btn = QPushButton("Settings")
        
        layout.addWidget(dashboard_btn)
        layout.addWidget(devices_btn)
        layout.addWidget(monitor_btn)
        layout.addStretch()
        layout.addWidget(settings_btn)
        
        self.setLayout(layout)
        self.setMaximumWidth(200)
