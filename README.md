# jsbeautify-cli

A simple command-line tool to beautify JavaScript files from URLs.

## Features

- Download JavaScript files from URLs
- Automatically beautify/format JavaScript code
- Save beautified output to a file
- Simple and easy-to-use CLI interface

## Installation

### From source

```bash
# Clone the repository
git clone https://github.com/m4ll0k/jsbeautify.git
cd jsbeautify

# Install the package
pip install .

# Or install in development mode
pip install -e .
```

### From PyPI (when published)

```bash
pip install jsbeautify-cli
```

## Usage

### Command Line

After installation, you can use the `jsbeautify` command:

```bash
jsbeautify <url> <output>
```

**Arguments:**
- `url`: URL of the JavaScript file to beautify (must contain `.js`)
- `output`: Path to save the beautified JavaScript file

**Options:**
- `-h, --help`: Show help message
- `-v, --version`: Show version information

### Examples

```bash
# Beautify a JavaScript file from a CDN
jsbeautify https://cdn.example.com/script.min.js beautified.js

# Beautify a JavaScript bundle
jsbeautify https://example.com/bundle.js output.js
```

### As a Python Module

You can also use jsbeautify as a Python module:

```python
from jsbeautify import beauty, getjs

# Fetch and beautify JavaScript from URL
response = getjs("https://example.com/script.js")
if response.status_code == 200:
    beautified = beauty(response.content)
    print(beautified)

# Or beautify JavaScript content directly
js_code = "function test(){console.log('hello');}"
beautified = beauty(js_code)
print(beautified)
```

## Requirements

- Python 3.7+
- jsbeautifier>=1.14.0
- requests>=2.25.0

## Development

### Setup Development Environment

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run tests (if available)
pytest

# Format code
black jsbeautify/
```

## Project Structure

```
jsbeautify/
├── jsbeautify/
│   ├── __init__.py      # Package initialization and exports
│   ├── core.py          # Core functionality (beauty, getjs)
│   └── main.py          # CLI entry point
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
└── jsbeautify.py        # (Legacy script - can be removed)
```

## License

MIT License

## Author

- **m4ll0k**
- GitHub: [github.com/m4ll0k](https://github.com/m4ll0k)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### 0.1.0 (2024)
- Initial release
- Refactored as a proper Python package
- Added pyproject.toml configuration
- Improved error handling
- Added type hints
- Better CLI with argparse
