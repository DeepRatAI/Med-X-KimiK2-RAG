"""
Setup script for medex package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")

setup(
    name="medex",
    version="0.1.0",
    author="DeepRatAI",
    author_email="info@deeprat.tech",
    description="AI-powered Clinical Reasoning Assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepRatAI/Med-X-KimiK2-RAG",
    packages=find_packages(include=["medex", "medex.*"]),
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-asyncio>=0.19.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "medex=medex.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
)
