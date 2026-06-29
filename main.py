#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YaiZa-Pro Main Entry Point
Runs on Windows, Linux, and macOS
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Set up environment
os.environ.setdefault('QT_API', 'pyside6')

try:
    from PySide6.QtWidgets import QApplication
    from app.gui.main_window import MainWindow
except ImportError as e:
    print(f"Error: Failed to import required modules. {e}")
    print("Please install dependencies: pip install -r requirements.txt")
    sys.exit(1)


def main():
    """Main application entry point"""
    try:
        app = QApplication(sys.argv)
        
        # Set application name and icon
        app.setApplicationName("YaiZa Professional")
        app.setApplicationVersion("1.0.0")
        
        # Create and show main window
        window = MainWindow()
        window.show()
        
        # Run application
        sys.exit(app.exec())
    except Exception as e:
        print(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
