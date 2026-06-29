# YaiZa-Pro Project Structure

Complete directory and file structure of YaiZa-Pro application.

```
YaiZa-Pro/
│
├── app/                              # Main application package
│   ├── __init__.py
│   │
│   ├── core/                         # Core system modules
│   │   ├── __init__.py
│   │   ├── system.py                 # Main system controller
│   │   ├── config_loader.py          # Configuration loading
│   │   ├── database.py               # Database manager
│   │   ├── plugin_loader.py          # Plugin system
│   │   ├── ai_engine.py              # AI/ML engine
│   │   └── dashboard.py              # Dashboard display
│   │
│   ├── ai/                           # AI and ML modules
│   │   ├── __init__.py
│   │   ├── analyzer.py               # Problem analysis
│   │   ├── thinker.py                # AI thinking engine
│   │   ├── planner.py                # Planning module
│   │   ├── executor.py               # Execution engine
│   │   ├── verifier.py               # Verification module
│   │   └── reporter.py               # Report generation
│   │
│   ├── network/                      # Network management
│   │   ├── __init__.py
│   │   ├── devices/                  # Device drivers
│   │   │   ├── __init__.py
│   │   │   ├── hikvision.py          # Hikvision CCTV
│   │   │   ├── dahua.py              # Dahua CCTV
│   │   │   ├── mikrotik.py           # Mikrotik Router
│   │   │   ├── tp_link.py            # TP-Link Switch
│   │   │   ├── ubiquiti.py           # Ubiquiti Wireless
│   │   │   └── zkteco.py             # ZKTeco Access Control
│   │   ├── manager.py                # Network manager
│   │   └── monitor.py                # Network monitor
│   │
│   ├── cctv/                         # CCTV operations
│   │   ├── __init__.py
│   │   ├── camera.py                 # Camera control
│   │   ├── recording.py              # Recording management
│   │   └── streaming.py              # Stream handling
│   │
│   ├── repair/                       # Network repair & recovery
│   │   ├── __init__.py
│   │   ├── ping.py                   # Health check (Ping)
│   │   ├── analyzer.py               # Issue analysis
│   │   ├── backup.py                 # Configuration backup
│   │   ├── repair.py                 # Repair engine
│   │   ├── verifier.py               # Verification system
│   │   └── rollback.py               # Rollback manager
│   │
│   ├── gui/                          # Graphical user interface
│   │   ├── __init__.py
│   │   ├── main_window.py            # Main window
│   │   ├── dialogs.py                # Dialog windows
│   │   └── widgets.py                # Custom widgets
│   │
│   ├── database/                     # Database operations
│   │   ├── __init__.py
│   │   ├── models.py                 # Database models
│   │   ├── queries.py                # Query builders
│   │   └── migrations.py             # Database migrations
│   │
│   ├── plugins/                      # Plugin system
│   │   ├── __init__.py
│   │   ├── base.py                   # Base plugin class
│   │   └── examples/                 # Example plugins
│   │
│   ├── automation/                   # Automation scripts
│   │   ├── __init__.py
│   │   ├── scheduler.py              # Task scheduler
│   │   └── workflows.py              # Workflow engine
│   │
│   ├── reports/                      # Report generation
│   │   ├── __init__.py
│   │   ├── generator.py              # Report generator
│   │   └── templates/                # Report templates
│   │       ├── daily_report.html
│   │       ├── weekly_report.html
│   │       └── monthly_report.html
│   │
│   ├── settings/                     # Configuration settings
│   │   ├── __init__.py
│   │   └── config.py                 # Settings manager
│   │
│   └── utils/                        # Utility functions
│       ├── __init__.py
│       ├── logger.py                 # Logging utilities
│       ├── helpers.py                # Helper functions
│       └── validators.py             # Data validators
│
├── assets/                           # Images and resources
│   ├── icons/
│   │   ├── app_icon.ico
│   │   ├── camera.png
│   │   ├── network.png
│   │   ├── ai.png
│   │   └── settings.png
│   ├── images/
│   │   ├── logo.png
│   │   ├── screenshot_1.png
│   │   └── screenshot_2.png
│   └── styles/
│       ├── dark_theme.qss
│       └── light_theme.qss
│
├── config/                           # Configuration files
│   ├── devices.yaml                  # Device configurations
│   ├── network.yaml                  # Network settings
│   ├── ai.yaml                       # AI settings
│   ├── database.yaml                 # Database configuration
│   └── example_config.yaml           # Example configuration
│
├── data/                             # Data storage
│   ├── database.db                   # SQLite database
│   ├── cache/                        # Cache files
│   ├── exports/                      # Exported data
│   └── logs/                         # Application logs
│
├── logs/                             # Log files
│   ├── app.log                       # Main application log
│   ├── network.log                   # Network operations log
│   ├── repair.log                    # Repair operations log
│   ├── ai.log                        # AI operations log
│   └── error.log                     # Error log
│
├── installer/                        # Installation files
│   ├── windows/
│   │   ├── installer.bat
│   │   ├── uninstaller.bat
│   │   └── installer.iss
│   ├── linux/
│   │   ├── installer.sh
│   │   └── uninstaller.sh
│   └── macos/
│       ├── installer.sh
│       └── uninstaller.sh
│
├── tests/                            # Unit tests
│   ├── __init__.py
│   ├── test_core.py
│   ├── test_network.py
│   ├── test_ai.py
│   ├── test_repair.py
│   └── test_utils.py
│
├── docs/                             # Documentation
│   ├── README.md
│   ├── INSTALL.md
│   ├── USAGE.md
│   ├── API.md
│   ├── CONFIGURATION.md
│   ├── TROUBLESHOOTING.md
│   └── DEVELOPMENT.md
│
├── main.py                           # Application entry point
├── setup.py                          # Python package setup
├── requirements.txt                  # Python dependencies
├── install_helper.py                 # Installation helper
├── uninstaller.bat                   # Windows uninstaller
├── LICENSE.txt                       # License file
├── README.md                         # Project README
├── PROJECT_STRUCTURE.md              # This file
├── INSTALL.md                        # Installation guide
├── .gitignore                        # Git ignore rules
├── .env.example                      # Environment variables example
└── .github/                          # GitHub specific files
    └── workflows/
        ├── tests.yml                 # Test workflow
        └── build.yml                 # Build workflow
```

---

## 📊 File Organization Summary

| Folder | Purpose | Files |
|--------|---------|-------|
| `app/core/` | Core system functionality | 6 files |
| `app/ai/` | AI and ML operations | 6 files |
| `app/network/` | Network management | 8+ files |
| `app/repair/` | Network repair system | 6 files |
| `app/gui/` | User interface | 3+ files |
| `app/database/` | Database operations | 3+ files |
| `app/plugins/` | Plugin system | 2+ files |
| `app/automation/` | Automation scripts | 2+ files |
| `app/reports/` | Report generation | 1+ file |
| `app/settings/` | Configuration | 1+ file |
| `app/utils/` | Utility functions | 3+ files |
| `assets/` | Images and resources | 10+ files |
| `config/` | Configuration files | 5+ files |
| `data/` | Data storage | Multiple |
| `logs/` | Log files | Multiple |
| `tests/` | Unit tests | 5+ files |
| `docs/` | Documentation | 7+ files |

---

## 🔑 Key Files

- **main.py** - Application entry point
- **setup.py** - Package installation configuration
- **requirements.txt** - Python dependencies
- **README.md** - Project documentation
- **INSTALL.md** - Installation guide
- **LICENSE.txt** - License information
- **app/core/system.py** - Main system controller
- **app/core/dashboard.py** - Dashboard display
- **app/repair/ping.py** - Network health check

---

## 📦 Directory Sizes (Approximate)

- **app/** - ~500KB (main application code)
- **assets/** - ~5MB (images and resources)
- **config/** - ~50KB (configuration files)
- **data/** - Variable (user data)
- **logs/** - Variable (log files)
- **tests/** - ~100KB (test files)
- **docs/** - ~200KB (documentation)

**Total Source Code:** ~1-2MB

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/yaimaza/YaiZa-Professional-YaiZa-Pro-AI-Network-CCTV-Automation-Engineer.git

# Navigate to directory
cd YaiZa-Professional-YaiZa-Pro-AI-Network-CCTV-Automation-Engineer

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

---

## 📝 File Naming Conventions

- **Python files** - `lowercase_with_underscores.py`
- **Classes** - `PascalCase`
- **Functions** - `lowercase_with_underscores()`
- **Constants** - `UPPERCASE_WITH_UNDERSCORES`
- **Config files** - `lowercase.yaml`

---

Generated: 2026-06-29
Version: 1.0.0
