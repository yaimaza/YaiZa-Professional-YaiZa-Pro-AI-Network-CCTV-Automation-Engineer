#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YaiZa-Pro Installation Helper
Assists with installation and configuration
"""

import os
import sys
import platform
import subprocess
from pathlib import Path


class InstallationHelper:
    """Installation helper for YaiZa-Pro"""
    
    def __init__(self):
        self.os_type = platform.system()
        self.project_root = Path(__file__).parent
        
    def check_python_version(self):
        """Check Python version"""
        version = sys.version_info
        print(f"Python version: {version.major}.{version.minor}.{version.micro}")
        
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print("ERROR: Python 3.8+ is required")
            return False
        
        print("✓ Python version OK")
        return True
        
    def check_dependencies(self):
        """Check if dependencies are installed"""
        try:
            import pip
            print("✓ pip is available")
            return True
        except ImportError:
            print("ERROR: pip is not available")
            return False
            
    def install_dependencies(self):
        """Install required dependencies"""
        print("\n[*] Installing dependencies...")
        
        requirements_file = self.project_root / "requirements.txt"
        
        if not requirements_file.exists():
            print("ERROR: requirements.txt not found")
            return False
            
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)])
            print("✓ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("ERROR: Failed to install dependencies")
            return False
            
    def create_directories(self):
        """Create required directories"""
        print("\n[*] Creating required directories...")
        
        dirs = ["logs", "data", "config"]
        
        for dir_name in dirs:
            dir_path = self.project_root / dir_name
            dir_path.mkdir(exist_ok=True)
            print(f"✓ Created {dir_name}/")
            
    def setup_environment(self):
        """Setup environment variables"""
        print("\n[*] Setting up environment...")
        
        env_file = self.project_root / ".env"
        
        if not env_file.exists():
            with open(env_file, 'w') as f:
                f.write("# YaiZa-Pro Environment Variables\n")
                f.write("DEBUG=False\n")
                f.write("LOG_LEVEL=INFO\n")
                f.write("DATABASE_URL=sqlite:///data/yaiza.db\n")
                
            print("✓ Environment file created")
        else:
            print("✓ Environment file already exists")
            
    def run_installation(self):
        """Run full installation"""
        print("\n" + "="*50)
        print("YaiZa-Pro Installation Helper")
        print("="*50 + "\n")
        
        if not self.check_python_version():
            return False
            
        if not self.check_dependencies():
            return False
            
        if not self.install_dependencies():
            return False
            
        self.create_directories()
        self.setup_environment()
        
        print("\n" + "="*50)
        print("Installation Complete!")
        print("="*50)
        print("\nTo run YaiZa-Pro:")
        print(f"  python {self.project_root / 'main.py'}")
        
        return True


if __name__ == "__main__":
    helper = InstallationHelper()
    success = helper.run_installation()
    sys.exit(0 if success else 1)
