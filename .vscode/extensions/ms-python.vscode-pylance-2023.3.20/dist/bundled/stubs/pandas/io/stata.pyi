from collections import abc
from collections.abc import Sequence
import datetime
from io import BytesIO
from types import TracebackType
from typing import (
    Literal,
    overload,
)

from pandas.core.frame import DataFrame
from typing_extensions import Self

from pandas._typing import (
    CompressionOptions,
    FilePath,
    HashableT,
    HashableT1,
    HashableT2,
    HashableT3,
    ReadBuffer,
    StataDateFormat,
    StorageOptions,
    WriteBuffer,
)

@overload
def read_stata(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    convert_dates: bool = ...,
    convert_categoricals: bool = ...,
    index_col: str | None = ...,
    convert_missing: bool = ...,
    preserve_dtypes: bool = ...,
    columns: list[HashableT] | None = ...,
    order_categoricals: bool = ...,
    chunksize: int | None = ...,
    iterator: Literal[True],
    compression: CompressionOptions = ...,
    storage_options: StorageOptions = ...,
) -> StataReader:
    """
Read Stata file into DataFrame.

Parameters
----------
filepath_or_buffer : str, path object or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid
    URL schemes include http, ftp, s3, and file. For file URLs, a host is
    expected. A local file could be: ``file://localhost/path/to/table.dta``.

    If you want to pass in a path object, pandas accepts any ``os.PathLike``.

    By file-like object, we refer to objects with a ``read()`` method,
    such as a file handle (e.g. via builtin ``open`` function)
    or ``StringIO``.
convert_dates : bool, default True
    Convert date variables to DataFrame time values.
convert_categoricals : bool, default True
    Read value labels and convert columns to Categorical/Factor variables.
index_col : str, optional
    Column to set as index.
convert_missing : bool, default False
    Flag indicating whether to convert missing values to their Stata
    representations.  If False, missing values are replaced with nan.
    If True, columns containing missing values are returned with
    object data types and missing values are represented by
    StataMissingValue objects.
preserve_dtypes : bool, default True
    Preserve Stata datatypes. If False, numeric data are upcast to pandas
    default types for foreign data (float64 or int64).
columns : list or None
    Columns to retain.  Columns will be returned in the given order.  None
    returns all columns.
order_categoricals : bool, default True
    Flag indicating whether converted categorical data are ordered.
chunksize : int, default None
    Return StataReader object for iterations, returns chunks with
    given number of lines.
iterator : bool, default False
    Return StataReader object.
compression : str or dict, default 'infer'
    For on-the-fly decompression of on-disk data. If 'infer' and 'filepath_or_buffer' is
    path-like, then detect compression from the following extensions: '.gz',
    '.bz2', '.zip', '.xz', '.zst', '.tar', '.tar.gz', '.tar.xz' or '.tar.bz2'
    (otherwise no compression).
    If using 'zip' or 'tar', the ZIP file must contain only one data file to be read in.
    Set to ``None`` for no decompression.
    Can also be a dict with key ``'method'`` set
    to one of {``'zip'``, ``'gzip'``, ``'bz2'``, ``'zstd'``, ``'tar'``} and other
    key-value pairs are forwarded to
    ``zipfile.ZipFile``, ``gzip.GzipFile``,
    ``bz2.BZ2File``, ``zstandard.ZstdDecompressor`` or
    ``tarfile.TarFile``, respectively.
    As an example, the following could be passed for Zstandard decompression using a
    custom compression dictionary:
    ``compression={'method': 'zstd', 'dict_data': my_compression_dict}``.

        .. versionadded:: 1.5.0
            Added support for `.tar` files.
storage_options : dict, optional
    Extra options that make sense for a particular storage connection, e.g.
    host, port, username, password, etc. For HTTP(S) URLs the key-value pairs
    are forwarded to ``urllib.request.Request`` as header options. For other
    URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are
    forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more
    details, and for more examples on storage options refer `here
    <https://pandas.pydata.org/docs/user_guide/io.html?
    highlight=storage_options#reading-writing-remote-files>`_.

Returns
-------
DataFrame or StataReader

See Also
--------
io.stata.StataReader : Low-level reader for Stata data files.
DataFrame.to_stata: Export Stata data files.

Notes
-----
Categorical variables read through an iterator may not have the same
categories and dtype. This occurs when  a variable stored in a DTA
file is associated to an incomplete set of value labels that only
label a strict subset of the values.

Examples
--------

Creating a dummy stata for this example
>>> df = pd.DataFrame({'animal': ['falcon', 'parrot', 'falcon',
...                              'parrot'],
...                   'speed': [350, 18, 361, 15]})  # doctest: +SKIP
>>> df.to_stata('animals.dta')  # doctest: +SKIP

Read a Stata dta file:

>>> df = pd.read_stata('animals.dta')  # doctest: +SKIP

Read a Stata dta file in 10,000 line chunks:
>>> values = np.random.randint(0, 10, size=(20_000, 1), dtype="uint8")  # doctest: +SKIP
>>> df = pd.DataFrame(values, columns=["i"])  # doctest: +SKIP
>>> df.to_stata('filename.dta')  # doctest: +SKIP

>>> itr = pd.read_stata('filename.dta', chunksize=10000)  # doctest: +SKIP
>>> for chunk in itr:
...    # Operate on a single chunk, e.g., chunk.mean()
...    pass  # doctest: +SKIP
    """
    pass
@overload
def read_stata(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    convert_dates: bool = ...,
    convert_categoricals: bool = ...,
    index_col: str | None = ...,
    convert_missing: bool = ...,
    preserve_dtypes: bool = ...,
    columns: list[HashableT] | None = ...,
    order_categoricals: bool = ...,
    chunksize: int,
    iterator: bool = ...,
    compression: CompressionOptions = ...,
    storage_options: StorageOptions = ...,
) -> StataReader: ...
@overload
def read_stata(
    filepath_or_buffer: FilePath | ReadBuffer[bytes],
    *,
    convert_dates: bool = ...,
    convert_categoricals: bool = ...,
    index_col: str | None = ...,
    convert_missing: bool = ...,
    preserve_dtypes: bool = ...,
    columns: list[HashableT] | None = ...,
    order_categoricals: bool = ...,
    chunksize: None = ...,
    iterator: Literal[False] = ...,
    compression: CompressionOptions = ...,
    storage_options: StorageOptions = ...,
) -> DataFrame: ...

class StataParser:
    def __init__(self) -> None: ...

class StataReader(StataParser, abc.Iterator):
    col_sizes: list[int] = ...
    path_or_buf: BytesIO = ...
    def __init__(
        self,
        path_or_buf: FilePath | ReadBuffer[bytes],
        convert_dates: bool = ...,
        convert_categoricals: bool = ...,
        index_col: str | None = ...,
        convert_missing: bool = ...,
        preserve_dtypes: bool = ...,
        columns: Sequence[str] | None = ...,
        order_categoricals: bool = ...,
        chunksize: int | None = ...,
        compression: CompressionOptions = ...,
        storage_options: StorageOptions = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> DataFrame: ...
    def get_chunk(self, size: int | None = ...) -> DataFrame: ...
    def read(
        self,
        nrows: int | None = ...,
        convert_dates: bool | None = ...,
        convert_categoricals: bool | None = ...,
        index_col: str | None = ...,
        convert_missing: bool | None = ...,
        preserve_dtypes: bool | None = ...,
        columns: list[str] | None = ...,
        order_categoricals: bool | None = ...,
    ): ...
    @property
    def data_label(self) -> str: ...
    def variable_labels(self) -> dict[str, str]: ...
    def value_labels(self) -> dict[str, dict[float, str]]: ...

class StataWriter(StataParser):
    def __init__(
        self,
        fname: FilePath | WriteBuffer[bytes],
        data: DataFrame,
        convert_dates: dict[HashableT1, StataDateFormat] | None = ...,
        write_index: bool = ...,
        byteorder: str | None = ...,
        time_stamp: datetime.datetime | None = ...,
        data_label: str | None = ...,
        variable_labels: dict[HashableT2, str] | None = ...,
        compression: CompressionOptions = ...,
        storage_options: StorageOptions = ...,
        *,
        value_labels: dict[HashableT3, dict[float, str]] | None = ...,
    ) -> None: ...
    def write_file(self) -> None: ...
