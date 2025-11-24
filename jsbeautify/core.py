"""
Core functionality for jsbeautify package.
"""

import sys
from typing import Union

try:
    import jsbeautifier
    import requests
except ImportError as e:
    sys.exit(f"{e}.. please install required dependencies: pip install jsbeautifier requests")


def beauty(content: Union[str, bytes]) -> str:
    """
    Beautify JavaScript content.

    Args:
        content: JavaScript content as string or bytes

    Returns:
        Beautified JavaScript as string
    """
    if isinstance(content, bytes):
        content = content.decode('utf-8')
    return jsbeautifier.beautify(content)


def getjs(url: str) -> Union[requests.Response, dict]:
    """
    Fetch JavaScript file from URL.

    Args:
        url: URL of the JavaScript file

    Returns:
        Response object if successful, dict with error info otherwise
    """
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            return response
        return {"content": b"", "status_code": response.status_code}
    except Exception as e:
        return {"content": b"", "status_code": 500, "error": str(e)}
