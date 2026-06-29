#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build YaiZa-Pro as Windows EXE
Run: python build_exe.py
"""

import os
import sys
import shutil
from pathlib import Path

try:
    import PyInstaller.__main__ as pyi
except ImportError:
    print("Error: PyInstaller not installed.")
    print("Install it: pip install PyInstaller")
    sys.exit(1)


def build_exe():
    """Build executable using PyInstaller"""
    project_root = Path(__file__).parent
    dist_dir = project_root / "dist"
    build_dir = project_root / "build"
    
    print("\n" + "="*60)
    print("YaiZa-Pro EXE Builder")
    print("="*60 + "\n")
    
    # Clean previous builds
    print("[*] Cleaning previous builds...")
    for dir_path in [dist_dir, build_dir, project_root / "*.spec"]:
        if isinstance(dir_path, Path) and dir_path.exists():
            try:
                if dir_path.is_dir():
                    shutil.rmtree(dir_path)
                    print(f"    ✓ Removed {dir_path.name}")
            except Exception as e:
                print(f"    ✗ Failed to remove {dir_path}: {e}")
    
    print("\n[*] Building executable...\n")
    
    # PyInstaller arguments
    args = [
        str(project_root / "main.py"),
        "--name=YaiZa-Pro",
        "--onefile",  # Single EXE file
        "--windowed",  # No console window
        f"--distpath={dist_dir}",
        f"--buildpath={build_dir}",
        f"--specpath={project_root}",
        "--icon=assets/icon.ico" if (project_root / "assets" / "icon.ico").exists() else "",
        "--add-data=config:config",
        "--add-data=assets:assets",
        "--collect-all=PySide6",
        "--hidden-import=numpy",
        "--hidden-import=pandas",
        "--hidden-import=sklearn",
    ]
    
    # Remove empty arguments
    args = [arg for arg in args if arg]
    
    try:
        pyi.run(args)
        print("\n" + "="*60)
        print("✓ Build Successful!")
        print("="*60)
        print(f"\nExecutable created at: {dist_dir / 'YaiZa-Pro.exe'}")
        print(f"\nTo run: {dist_dir / 'YaiZa-Pro.exe'}")
        return True
    except Exception as e:
        print("\n" + "="*60)
        print("✗ Build Failed!")
        print("="*60)
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
