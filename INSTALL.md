# YaiZa-Pro Installation Guide

## Windows Installation

### Method 1: Automated Installation (Recommended)

1. **Download Python**
   - Download Python 3.8+ from https://www.python.org/
   - During installation, make sure to check "Add Python to PATH"

2. **Run Installer**
   ```batch
   installer.bat
   ```
   This will:
   - Check Python installation
   - Create virtual environment
   - Install all dependencies
   - Create necessary folders

3. **Run YaiZa-Pro**
   ```batch
   venv\Scripts\activate.bat
   python main.py
   ```

### Method 2: Manual Installation

1. **Install Python**
   - Python 3.8 or higher
   - Ensure Python is in PATH

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python main.py
   ```

### Method 3: Professional Installer (.EXE)

1. **Install Inno Setup**
   - Download from https://jrsoftware.org/isinfo.php
   - Install Inno Setup on your system

2. **Build Installer**
   ```bash
   "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
   ```

3. **Run Generated Setup**
   - Execute `YaiZa-Pro-1.0.0-Setup.exe`
   - Follow the installation wizard

## Linux/macOS Installation

1. **Install Python**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3.10 python3-pip python3-venv
   
   # macOS
   brew install python3
   ```

2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Application**
   ```bash
   python main.py
   ```

## Troubleshooting

### Python not found
- Reinstall Python and ensure "Add to PATH" is checked
- Verify: `python --version`

### pip not available
```bash
python -m ensurepip --default-pip
```

### Permission denied (Linux/macOS)
```bash
chmod +x main.py
sudo python main.py
```

### Virtual environment not activating
```bash
# Windows
venv\Scripts\activate.bat

# Linux/macOS
source venv/bin/activate
```

## Uninstallation

### Windows
```batch
uninstaller.bat
```

### Linux/macOS
```bash
rm -rf venv
rm -rf ~/.yaiza-pro
```

## System Requirements

- **OS**: Windows 7+, Linux (Ubuntu 18.04+), macOS 10.12+
- **Python**: 3.8+
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: 500MB minimum
- **Network**: Internet connection (for first setup)

## First Run

1. Application will create necessary directories
2. Configure settings in `config/` folder
3. Set up device connections in GUI
4. Run network diagnostics

## Support

For issues or questions:
- Check logs in `logs/` folder
- Review README.md
- Visit GitHub: https://github.com/yaimaza/
