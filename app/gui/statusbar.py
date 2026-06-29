from PySide6.QtWidgets import QStatusBar, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt


class StatusBar(QStatusBar):
    """Custom status bar showing system status"""

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize status bar UI"""
        # System status
        self.status_label = QLabel("Ready")
        self.addWidget(self.status_label)
        
        # Connection status
        self.connection_label = QLabel("Online")
        self.addPermanentWidget(self.connection_label)
        
        # Device count
        self.device_label = QLabel("Devices: 0")
        self.addPermanentWidget(self.device_label)

    def set_status(self, message: str):
        """Update status message"""
        self.status_label.setText(message)

    def set_connection_status(self, connected: bool):
        """Update connection status"""
        status = "Online" if connected else "Offline"
        self.connection_label.setText(status)

    def set_device_count(self, count: int):
        """Update device count"""
        self.device_label.setText(f"Devices: {count}")
