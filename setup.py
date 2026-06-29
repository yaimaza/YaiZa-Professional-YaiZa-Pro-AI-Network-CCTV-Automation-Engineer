#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YaiZa-Pro Setup Script
Setup configuration for package installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="YaiZa-Pro",
    version="1.0.0",
    author="YaiZa",
    author_email="yaiza@professional.com",
    description="AI Network CCTV Automation Engineer - Professional Suite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaimaza/YaiZa-Professional-YaiZa-Pro-AI-Network-CCTV-Automation-Engineer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "PyQt5>=5.15.0",
        "PyQt5-sip>=12.9.0",
        "SQLAlchemy>=1.4.0",
        "pymysql>=1.0.0",
        "requests>=2.26.0",
        "paramiko>=2.8.0",
        "tensorflow>=2.6.0",
        "scikit-learn>=0.24.0",
        "opencv-python>=4.5.0",
        "APScheduler>=3.8.0",
        "python-dotenv>=0.19.0",
        "pyyaml>=5.4.0",
        "loguru>=0.6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.6b0",
            "flake8>=3.9.0",
            "pylint>=2.9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "yaiza-pro=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
