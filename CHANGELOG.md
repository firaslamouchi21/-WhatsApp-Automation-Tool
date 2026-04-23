# Changelog

All notable changes to the WhatsApp Automation Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Modern `pyproject.toml` configuration
- MANIFEST.in for proper package file inclusion
- CONTRIBUTING.md guidelines
- Pre-commit configuration support

### Changed
- Project is now Docker-only (runs on Linux VM)
- Removed PyPI publishing (Docker deployment only)
- Updated setup.py to delegate to pyproject.toml
- Improved package metadata and classifiers
- Enhanced project structure for better maintainability
- Updated README to be more conversational and human-like

## [1.0.0] - 2024-04-23

### Added
- Initial release of WhatsApp Automation Tool
- WhatsApp Web automation via pywhatkit
- CSV lead list processing with pandas
- Phone number validation with phonenumbers
- Message template system with variable substitution
- CLI interface with argparse
- Docker support with noVNC GUI (Linux VM only)
- Rate limiting for message sending
- Dry-run mode for testing
- Progress tracking with tqdm
- Configuration management with YAML
- Logging system
- Test suite with pytest
- GitHub Actions CI/CD workflows
- GitHub Container Registry (GHCR) publishing
