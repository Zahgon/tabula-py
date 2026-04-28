import json
from typing import Dict, Iterable, List, TextIO, Union, cast

from .file_util import _stringify_path, is_file_like
from .util import FileLikeObj, TabulaOption


def load_template(path_or_buffer: FileLikeObj) -> List[TabulaOption]:
    """Build tabula-py option from template file

    Args:
        path_or_buffer (str, path object or file-like object):
            File like object of Tabula app template.

    Returns:
        dict: tabula-py options
    """
    pass


def _convert_template_option(
    template: Dict[str, Union[bool, float, int, str]],
) -> TabulaOption:
    """Convert Tabula app template to tabula-py option

    Args:
        template (dict): Tabula app template

    Returns:
        `obj`:dict: tabula-py option
    """
    pass
