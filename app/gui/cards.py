from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Card(QWidget):
    """Reusable card component for displaying information"""

    def __init__(self, title: str, content: str = ""):
        super().__init__()
        self.title_text = title
        self.content_text = content
        self.init_ui()

    def init_ui(self):
        """Initialize card UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Title
        title = QLabel(self.title_text)
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        
        layout.addWidget(title)
        
        # Content
        if self.content_text:
            content = QLabel(self.content_text)
            content.setWordWrap(True)
            layout.addWidget(content)
        
        layout.addStretch()
        
        self.setStyleSheet(
            "background-color: white; "
            "border: 1px solid #ddd; "
            "border-radius: 5px; "
            "padding: 10px;"
        )


class StatCard(QWidget):
    """Card for displaying statistics"""

    def __init__(self, label: str, value: str, unit: str = ""):
        super().__init__()
        self.label = label
        self.value = value
        self.unit = unit
        self.init_ui()

    def init_ui(self):
        """Initialize stat card UI"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Label
        label_widget = QLabel(self.label)
        label_font = QFont()
        label_font.setPointSize(10)
        label_widget.setFont(label_font)
        label_widget.setStyleSheet("color: #666;")
        
        # Value
        value_layout = QHBoxLayout()
        value_widget = QLabel(self.value)
        value_font = QFont()
        value_font.setPointSize(18)
        value_font.setBold(True)
        value_widget.setFont(value_font)
        value_widget.setStyleSheet("color: #333;")
        
        value_layout.addWidget(value_widget)
        
        if self.unit:
            unit_widget = QLabel(self.unit)
            unit_widget.setStyleSheet("color: #999;")
            value_layout.addWidget(unit_widget)
        
        value_layout.addStretch()
        
        layout.addWidget(label_widget)
        layout.addLayout(value_layout)
        layout.addStretch()
        
        self.setStyleSheet(
            "background-color: white; "
            "border: 1px solid #ddd; "
            "border-radius: 5px; "
            "padding: 10px;"
        )


class AlertCard(QWidget):
    """Card for displaying alerts"""

    def __init__(self, message: str, alert_type: str = "info"):
        super().__init__()
        self.message = message
        self.alert_type = alert_type  # info, warning, error, success
        self.init_ui()

    def init_ui(self):
        """Initialize alert card UI"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 15, 10)
        
        message_label = QLabel(self.message)
        message_label.setWordWrap(True)
        layout.addWidget(message_label)
        
        # Set color based on alert type
        colors = {
            "info": "#d1ecf1",
            "warning": "#fff3cd",
            "error": "#f8d7da",
            "success": "#d4edda"
        }
        bg_color = colors.get(self.alert_type, "#d1ecf1")
        
        self.setStyleSheet(
            f"background-color: {bg_color}; "
            "border: 1px solid #bee5eb; "
            "border-radius: 5px; "
            "padding: 10px;"
        )
