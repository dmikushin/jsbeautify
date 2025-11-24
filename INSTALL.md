# Installation Guide

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation Methods

### Method 1: Install from source (Recommended for development)

```bash
# Navigate to the project directory
cd jsbeautify

# Install in editable/development mode
pip install -e .

# Or install normally
pip install .
```

### Method 2: Build and install as wheel

```bash
# Install build tools
pip install build

# Build the package
python -m build

# Install the built wheel
pip install dist/jsbeautify_cli-0.1.0-py3-none-any.whl
```

### Method 3: Using virtual environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install the package
pip install .

# Now you can use jsbeautify command
jsbeautify --help
```

### Method 4: Using pipx (for CLI tools)

```bash
# Install pipx if not already installed
pip install --user pipx
pipx ensurepath

# Install jsbeautify-cli
pipx install .
```

## Verify Installation

After installation, verify that the package is installed correctly:

```bash
# Check if the command is available
which jsbeautify

# Check version
jsbeautify --version

# Show help
jsbeautify --help
```

## Testing the Package

Test the installation with a simple example:

```bash
# Create a test minified JavaScript
echo "function test(){console.log('hello');}" > test.min.js

# Start a simple HTTP server (optional, for testing with URL)
# python -m http.server 8000

# Use with a real URL
jsbeautify https://code.jquery.com/jquery-3.6.0.min.js jquery-beautified.js
```

## Troubleshooting

### Issue: Command not found after installation

**Solution:** Make sure the Python scripts directory is in your PATH:

```bash
# Find the scripts directory
python -m site --user-base

# Add to PATH (Linux/Mac - add to ~/.bashrc or ~/.zshrc)
export PATH="$PATH:$(python -m site --user-base)/bin"
```

### Issue: Permission denied during installation

**Solution:** Use a virtual environment or install with --user flag:

```bash
pip install --user .
```

### Issue: Dependencies not installing

**Solution:** Install dependencies manually:

```bash
pip install jsbeautifier requests
```

## Uninstallation

To uninstall the package:

```bash
pip uninstall jsbeautify-cli
```

## Development Installation

For development with additional tools:

```bash
# Install with development dependencies
pip install -e ".[dev]"

# This includes:
# - pytest (for testing)
# - black (for code formatting)
# - mypy (for type checking)
```
