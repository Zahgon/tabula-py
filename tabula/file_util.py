import os
import shutil
import uuid
from tempfile import gettempdir
from typing import BinaryIO, Optional, Tuple, cast
from urllib.parse import (
    quote,
    unquote,
    urlparse,
    uses_netloc,
    uses_params,
    uses_relative,
)
from urllib.request import Request, urlopen

from .util import FileLikeObj

_VALID_URLS = set(uses_relative + uses_netloc + uses_params)
_VALID_URLS.discard("")
MAX_FILE_SIZE = 200


def localize_file(
    path_or_buffer: FileLikeObj,
    user_agent: Optional[str] = None,
    suffix: str = ".pdf",
    use_raw_url=False,
) -> Tuple[str, bool]:
    """Ensure localize target file.

    If the target file is remote, this function fetches into local storage.

    Args:
        path_or_buffer (str):
            File path or file like object or URL of target file.
        user_agent (str, optional):
            Set a custom user-agent when download a pdf from a url. Otherwise
            it uses the default ``urllib.request`` user-agent.
        suffix (str, optional):
            File extension to check.
        use_raw_url (bool):
            Use `path_or_buffer` without quoting/dequoting.

    Returns:
        (str, bool):
            tuple of str and bool, which represents file name in local storage
            and temporary file flag.
    """
    pass


def _is_url(url: str) -> bool:
    pass


def _create_request(path_or_buffer: str, user_agent: str) -> Request:
    pass


def is_file_like(obj: FileLikeObj) -> bool:
    """Check file like object

    Args:
        obj:
            file like object.

    Returns:
        bool: file like object or not
    """
    pass


def _stringify_path(path_or_buffer: FileLikeObj) -> str:
    """Convert path like object to string

    Args:
        path_or_buffer: object to be converted

    Returns:
        string_path_or_buffer: maybe string version of path_or_buffer
    """
    pass
