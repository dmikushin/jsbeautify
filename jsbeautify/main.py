"""
Command-line interface for jsbeautify.
"""

import sys
import argparse
from pathlib import Path

from .core import beauty, getjs
from . import __version__


def main() -> None:
    """
    Main entry point for the jsbeautify CLI.
    """
    parser = argparse.ArgumentParser(
        description="Beautify JavaScript files from URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  jsbeautify https://example.com/script.js output.js
  jsbeautify https://cdn.example.com/bundle.js beautified.js
        """
    )

    parser.add_argument(
        "url",
        help="URL of the JavaScript file to beautify"
    )

    parser.add_argument(
        "output",
        help="Output file path to save the beautified JavaScript"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"jsbeautify {__version__}"
    )

    args = parser.parse_args()

    # Validate URL contains .js
    if '.js' not in args.url:
        sys.exit(f'Error: ".js" not found in URL ({args.url}). Please check your URL.')

    # Fetch JavaScript file
    print(f"Fetching JavaScript from: {args.url}")
    response = getjs(args.url)

    # Check if request was successful
    if isinstance(response, dict):
        sys.exit(f"Error: Failed to fetch JavaScript file. Status: {response.get('status_code', 'unknown')}")

    if response.status_code != 200:
        sys.exit(f"Error: HTTP {response.status_code} - Failed to fetch JavaScript file.")

    # Beautify JavaScript content
    print("Beautifying JavaScript...")
    try:
        beautified_js = beauty(response.content)
    except Exception as e:
        sys.exit(f"Error: Failed to beautify JavaScript: {e}")

    # Write to output file
    try:
        output_path = Path(args.output)
        output_path.write_text(beautified_js, encoding='utf-8')
        print(f"Done! File saved to: {output_path.absolute()}")
    except Exception as e:
        sys.exit(f"Error: Failed to write output file: {e}")


if __name__ == "__main__":
    main()
