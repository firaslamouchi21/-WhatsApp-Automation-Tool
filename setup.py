"""Setup configuration for WhatsApp Automation Tool."""

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="whatsapp-automation-tool",
    version="1.0.0",
    author="Firas",
    author_email="contact@example.com",
    description="Professional WhatsApp automation tool for business outreach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firas/whatsapp-automation-tool",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications :: Chat",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=[
        "pandas>=2.0.0",
        "pywhatkit>=5.4",
        "phonenumbers>=8.13.0",
        "pyyaml>=6.0",
        "tqdm>=4.65.0",
        "openpyxl>=3.1.0",
        "requests>=2.31.0",
        "click>=8.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "pytest-mock>=3.11.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pre-commit>=3.3.0",
        ],
        "docs": [
            "sphinx>=7.1.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "whatsapp-automation=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt"],
    },
    keywords="whatsapp automation marketing business outreach messaging",
    project_urls={
        "Bug Reports": "https://github.com/firas/whatsapp-automation-tool/issues",
        "Source": "https://github.com/firas/whatsapp-automation-tool",
        "Documentation": "https://github.com/firas/whatsapp-automation-tool/docs",
    },
)
