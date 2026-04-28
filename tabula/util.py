"""
Utility module providing some convenient functions.
"""

from __future__ import annotations

import os
import platform
import shlex
from dataclasses import dataclass
from logging import getLogger
from typing import IO, Iterable, List, Optional, Sequence, Union, cast

logger = getLogger(__name__)

FileLikeObj = Union[IO, str, os.PathLike]


def java_version() -> str:
    """Show Java version

    Returns:
        str: Result of ``java -version``
    """
    pass


def environment_info() -> None:
    """Show environment information for reporting.

    Returns:
        str:
            Detailed information like Python version, Java version,
            or OS environment, etc.
    """
    pass


@dataclass
class TabulaOption:
    """Build options for tabula-java

    Args:
        pages (str, int, `iterable` of `int`, optional):
            An optional values specifying pages to extract from. It allows
            `str`,`int`, `iterable` of :`int`. Default: `1`

            Examples:
                ``'1-2,3'``, ``'all'``, ``[1,2]``
        guess (bool, optional):
            Guess the portion of the page to analyze per page. Default `True`
            If you use "area" option, this option becomes `False`.

            Note:
                As of tabula-java 1.0.3, guess option becomes independent from
                lattice and stream option, you can use guess and lattice/stream option
                at the same time.

        area (iterable of float, iterable of iterable of float, optional):
            Portion of the page to analyze(top,left,bottom,right).
            Default is entire page.

            Note:
                If you want to use multiple area options and extract in one table, it
                should be better to set ``multiple_tables=False`` for :func:`read_pdf()`

            Examples:
                ``[269.875,12.75,790.5,561]``,
                ``[[12.1,20.5,30.1,50.2], [1.0,3.2,10.5,40.2]]``

        relative_area (bool, optional):
            If all area values are between 0-100 (inclusive) and preceded by ``'%'``,
            input will be taken as % of actual height or width of the page.
            Default ``False``.
        lattice (bool, optional):
            Force PDF to be extracted using lattice-mode extraction
            (if there are ruling lines separating each cell, as in a PDF of an
            Excel spreadsheet)
        stream (bool, optional):
            Force PDF to be extracted using stream-mode extraction
            (if there are no ruling lines separating each cell, as in a PDF of an
            Excel spreadsheet)
        password (str, optional):
            Password to decrypt document. Default: empty
        silent (bool, optional):
            Suppress all stderr output.
        columns (Sequence, optional):
            X coordinates of column boundaries. Must be sorted and of a datatype that
            preserves order, e.g. tuple or list

            Example:
                ``[10.1, 20.2, 30.3]``
        relative_columns (bool, optional):
            If all values are between 0-100 (inclusive) and preceded by '%',
            input will be taken as % of actual width of the page.
            Default ``False``.
        format (str, optional):
            Format for output file or extracted object.
            (``"CSV"``, ``"TSV"``, ``"JSON"``)
        batch (str, optional):
            Convert all PDF files in the provided directory. This argument should be
            directory path.
        output_path (str, optional):
            Output file path. File format of it is depends on ``format``.
            Same as ``--outfile`` option of tabula-java.
        options (str, optional):
            Raw option string for tabula-java.
        multiple_tables (bool, optional):
            Extract multiple tables into a dataframe. Default: True
    """

    pages: Optional[Union[str, int, Iterable[int]]] = None
    guess: bool = True
    area: Optional[Union[Iterable[float], Iterable[Iterable[float]]]] = None
    relative_area: bool = False
    lattice: bool = False
    stream: bool = False
    password: Optional[str] = None
    silent: Optional[bool] = None
    columns: Optional[Sequence[float]] = None
    relative_columns: bool = False
    format: Optional[str] = None
    batch: Optional[str] = None
    output_path: Optional[str] = None
    options: Optional[str] = ""
    multiple_tables: bool = True

    def merge(self, other: TabulaOption) -> TabulaOption:
        """Merge two TabulaOption.
        self will overwrite other fields' values.
        """
        pass

    def build_option_list(self) -> List[str]:
        """Convert to tabula-java option list"""
        pass


def _format_with_relative(values: Iterable[float], is_relative: bool) -> str:
    pass


def _validate_area(values: Iterable[float]) -> None:
    pass
