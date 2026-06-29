#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Development mode runner
Run without building EXE: python run_dev.py
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

if __name__ == "__main__":
    from main import main
    main()
