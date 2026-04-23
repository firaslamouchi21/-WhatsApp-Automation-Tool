# Contributing to WhatsApp Automation Tool

Thank you for your interest in contributing! This project is Docker-only and runs on a Linux VM.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment details (Docker version, etc.)
- Screenshots or logs if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:

- Use a clear and descriptive title
- Provide a detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- Provide examples or mockups if applicable

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/whatsapp-automation-tool.git
   cd whatsapp-automation-tool
   ```
3. **Make your changes** following the coding standards below
4. **Test with Docker**:
   ```bash
   docker build -t whatsapp-automation-tool .
   docker run --rm whatsapp-automation-tool pytest tests/
   ```
5. **Run linting** (if you have Python installed):
   ```bash
   black .
   isort .
   flake8 .
   mypy src/
   ```
6. **Commit your changes** with a clear commit message
7. **Push to your fork** and submit a pull request

## Development Setup

This project runs entirely in Docker. Here's how to set it up:

```bash
# Clone the repository
git clone https://github.com/firaslamouchi21/whatsapp-automation-tool.git
cd whatsapp-automation-tool

# Build the Docker image
docker build -t whatsapp-automation-tool .

# Run tests in Docker
docker run --rm whatsapp-automation-tool pytest tests/
```

If you want to work on the code locally (optional):

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Coding Standards

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and modular
- Add tests for new features

## Testing

```bash
# Run all tests in Docker
docker run --rm whatsapp-automation-tool pytest

# Run with coverage in Docker
docker run --rm whatsapp-automation-tool pytest --cov=src --cov-report=html

# Run specific test file
docker run --rm whatsapp-automation-tool pytest tests/test_whatsapp_automation.py
```

## Project Structure

```
whatsapp-automation-tool/
├── src/                    # Source code
│   ├── __init__.py
│   ├── whatsapp_automation.py
│   ├── phone_validator.py
│   ├── message_templates.py
│   └── logger_config.py
├── config/                 # Configuration files
├── templates/              # Message templates
├── tests/                  # Test files
├── main.py                 # CLI entry point
├── pyproject.toml          # Project configuration
├── setup.py                # Setup script (backward compat)
├── Dockerfile              # Docker image definition
└── README.md               # Project documentation
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
