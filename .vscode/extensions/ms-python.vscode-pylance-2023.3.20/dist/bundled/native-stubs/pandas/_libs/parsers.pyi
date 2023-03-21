# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.parsers, version: unspecified
import typing
import builtins as _mod_builtins
import numpy as _mod_numpy
import pandas.errors as _mod_pandas_errors

DtypeWarning = _mod_pandas_errors.DtypeWarning
ENOENT: int
EmptyDataError = _mod_pandas_errors.EmptyDataError
ParserError = _mod_pandas_errors.ParserError
ParserWarning = _mod_pandas_errors.ParserWarning
QUOTE_MINIMAL: int
QUOTE_NONE: int
QUOTE_NONNUMERIC: int
STR_NA_VALUES: set
class TextReader(_mod_builtins.object):
    "\n\n    # source: StringIO or file object\n\n    ..versionchange:: 1.2.0\n        removed 'compression', 'memory_map', and 'encoding' argument.\n        These arguments are outsourced to CParserWrapper.\n        'source' has to be a file handle.\n    "
    def __init__(self, *args, **kwargs) -> None:
        "\n\n    # source: StringIO or file object\n\n    ..versionchange:: 1.2.0\n        removed 'compression', 'memory_map', and 'encoding' argument.\n        These arguments are outsourced to CParserWrapper.\n        'source' has to be a file handle.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _convert_column_data(self) -> typing.Any:
        ...
    
    def _get_converter(self) -> typing.Any:
        ...
    
    def _set_quoting(self) -> typing.Any:
        ...
    
    @property
    def allow_leading_cols(self) -> typing.Any:
        ...
    
    @property
    def buffer_lines(self) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    @property
    def converters(self) -> typing.Any:
        ...
    
    @property
    def delim_whitespace(self) -> typing.Any:
        ...
    
    @property
    def delimiter(self) -> typing.Any:
        ...
    
    @property
    def dtype(self) -> typing.Any:
        ...
    
    @property
    def dtype_cast_order(self) -> typing.Any:
        ...
    
    @property
    def header(self) -> typing.Any:
        ...
    
    @property
    def header_end(self) -> typing.Any:
        ...
    
    @property
    def header_start(self) -> typing.Any:
        ...
    
    @property
    def index_col(self) -> typing.Any:
        ...
    
    @property
    def leading_cols(self) -> typing.Any:
        ...
    
    @property
    def low_memory(self) -> typing.Any:
        ...
    
    @property
    def mangle_dupe_cols(self) -> typing.Any:
        ...
    
    @property
    def na_values(self) -> typing.Any:
        ...
    
    @property
    def names(self) -> typing.Any:
        ...
    
    @property
    def noconvert(self) -> typing.Any:
        ...
    
    @property
    def orig_header(self) -> typing.Any:
        ...
    
    def read(self) -> typing.Any:
        '\n        rows=None --> read all rows\n        '
        ...
    
    def remove_noconvert(self) -> typing.Any:
        ...
    
    def set_error_bad_lines(self) -> typing.Any:
        ...
    
    def set_noconvert(self) -> typing.Any:
        ...
    
    @property
    def skipfooter(self) -> typing.Any:
        ...
    
    @property
    def skiprows(self) -> typing.Any:
        ...
    
    @property
    def table_width(self) -> typing.Any:
        ...
    
    @property
    def unnamed_cols(self) -> typing.Any:
        ...
    
    @property
    def usecols(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

_NA_VALUES: list
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

__test__: dict
def _compute_na_values() -> typing.Any:
    ...

def _concatenate_chunks() -> typing.Any:
    ...

def _ensure_encoded() -> typing.Any:
    ...

def _maybe_encode() -> typing.Any:
    ...

def _maybe_upcast() -> typing.Any:
    '\n\n    '
    ...

def is_bool_dtype(arr_or_dtype) -> bool:
    "\n    Check whether the provided array or dtype is of a boolean dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array or dtype is of a boolean dtype.\n\n    Notes\n    -----\n    An ExtensionArray is considered boolean when the ``_is_boolean``\n    attribute is set to True.\n\n    Examples\n    --------\n    >>> is_bool_dtype(str)\n    False\n    >>> is_bool_dtype(int)\n    False\n    >>> is_bool_dtype(bool)\n    True\n    >>> is_bool_dtype(np.bool_)\n    True\n    >>> is_bool_dtype(np.array(['a', 'b']))\n    False\n    >>> is_bool_dtype(pd.Series([1, 2]))\n    False\n    >>> is_bool_dtype(np.array([True, False]))\n    True\n    >>> is_bool_dtype(pd.Categorical([True, False]))\n    True\n    >>> is_bool_dtype(pd.arrays.SparseArray([True, False]))\n    True\n    "
    ...

def is_categorical_dtype(arr_or_dtype) -> bool:
    '\n    Check whether an array-like or dtype is of the Categorical dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array-like or dtype is of the Categorical dtype.\n\n    Examples\n    --------\n    >>> is_categorical_dtype(object)\n    False\n    >>> is_categorical_dtype(CategoricalDtype())\n    True\n    >>> is_categorical_dtype([1, 2, 3])\n    False\n    >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))\n    True\n    >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))\n    True\n    '
    ...

def is_datetime64_dtype(arr_or_dtype) -> bool:
    '\n    Check whether an array-like or dtype is of the datetime64 dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array-like or dtype is of the datetime64 dtype.\n\n    Examples\n    --------\n    >>> is_datetime64_dtype(object)\n    False\n    >>> is_datetime64_dtype(np.datetime64)\n    True\n    >>> is_datetime64_dtype(np.array([], dtype=int))\n    False\n    >>> is_datetime64_dtype(np.array([], dtype=np.datetime64))\n    True\n    >>> is_datetime64_dtype([1, 2, 3])\n    False\n    '
    ...

def is_extension_array_dtype(arr_or_dtype) -> bool:
    "\n    Check if an object is a pandas extension array type.\n\n    See the :ref:`Use Guide <extending.extension-types>` for more.\n\n    Parameters\n    ----------\n    arr_or_dtype : object\n        For array-like input, the ``.dtype`` attribute will\n        be extracted.\n\n    Returns\n    -------\n    bool\n        Whether the `arr_or_dtype` is an extension array type.\n\n    Notes\n    -----\n    This checks whether an object implements the pandas extension\n    array interface. In pandas, this includes:\n\n    * Categorical\n    * Sparse\n    * Interval\n    * Period\n    * DatetimeArray\n    * TimedeltaArray\n\n    Third-party libraries may implement arrays or types satisfying\n    this interface as well.\n\n    Examples\n    --------\n    >>> from pandas.api.types import is_extension_array_dtype\n    >>> arr = pd.Categorical(['a', 'b'])\n    >>> is_extension_array_dtype(arr)\n    True\n    >>> is_extension_array_dtype(arr.dtype)\n    True\n\n    >>> arr = np.array(['a', 'b'])\n    >>> is_extension_array_dtype(arr.dtype)\n    False\n    "
    ...

def is_float_dtype(arr_or_dtype) -> bool:
    "\n    Check whether the provided array or dtype is of a float dtype.\n\n    This function is internal and should not be exposed in the public API.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array or dtype is of a float dtype.\n\n    Examples\n    --------\n    >>> is_float_dtype(str)\n    False\n    >>> is_float_dtype(int)\n    False\n    >>> is_float_dtype(float)\n    True\n    >>> is_float_dtype(np.array(['a', 'b']))\n    False\n    >>> is_float_dtype(pd.Series([1, 2]))\n    False\n    >>> is_float_dtype(pd.Index([1, 2.]))\n    True\n    "
    ...

def is_integer_dtype(arr_or_dtype) -> bool:
    "\n    Check whether the provided array or dtype is of an integer dtype.\n\n    Unlike in `in_any_int_dtype`, timedelta64 instances will return False.\n\n    .. versionchanged:: 0.24.0\n\n       The nullable Integer dtypes (e.g. pandas.Int64Dtype) are also considered\n       as integer by this function.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array or dtype is of an integer dtype and\n        not an instance of timedelta64.\n\n    Examples\n    --------\n    >>> is_integer_dtype(str)\n    False\n    >>> is_integer_dtype(int)\n    True\n    >>> is_integer_dtype(float)\n    False\n    >>> is_integer_dtype(np.uint64)\n    True\n    >>> is_integer_dtype('int8')\n    True\n    >>> is_integer_dtype('Int8')\n    True\n    >>> is_integer_dtype(pd.Int8Dtype)\n    True\n    >>> is_integer_dtype(np.datetime64)\n    False\n    >>> is_integer_dtype(np.timedelta64)\n    False\n    >>> is_integer_dtype(np.array(['a', 'b']))\n    False\n    >>> is_integer_dtype(pd.Series([1, 2]))\n    True\n    >>> is_integer_dtype(np.array([], dtype=np.timedelta64))\n    False\n    >>> is_integer_dtype(pd.Index([1, 2.]))  # float\n    False\n    "
    ...

def is_object_dtype(arr_or_dtype) -> bool:
    '\n    Check whether an array-like or dtype is of the object dtype.\n\n    Parameters\n    ----------\n    arr_or_dtype : array-like\n        The array-like or dtype to check.\n\n    Returns\n    -------\n    boolean\n        Whether or not the array-like or dtype is of the object dtype.\n\n    Examples\n    --------\n    >>> is_object_dtype(object)\n    True\n    >>> is_object_dtype(int)\n    False\n    >>> is_object_dtype(np.array([], dtype=object))\n    True\n    >>> is_object_dtype(np.array([], dtype=int))\n    False\n    >>> is_object_dtype([1, 2, 3])\n    False\n    '
    ...

k = _mod_numpy.object_
na_values: dict
def pandas_dtype(dtype) -> Union[numpy.dtype, ForwardRef('ExtensionDtype')]:
    '\n    Convert input into a pandas only dtype object or a numpy dtype object.\n\n    Parameters\n    ----------\n    dtype : object to be converted\n\n    Returns\n    -------\n    np.dtype or a pandas dtype\n\n    Raises\n    ------\n    TypeError if not a dtype\n    '
    ...

def sanitize_objects() -> typing.Any:
    '\n    Convert specified values, including the given set na_values and empty\n    strings if convert_empty is True, to np.nan.\n\n    Parameters\n    ----------\n    values : ndarray[object]\n    na_values : set\n    convert_empty : bool, default True\n    '
    ...

def union_categoricals(to_union, sort_categories, ignore_order) -> typing.Any:
    '\n    Combine list-like of Categorical-like, unioning categories.\n\n    All categories must have the same dtype.\n\n    Parameters\n    ----------\n    to_union : list-like\n        Categorical, CategoricalIndex, or Series with dtype=\'category\'.\n    sort_categories : bool, default False\n        If true, resulting categories will be lexsorted, otherwise\n        they will be ordered as they appear in the data.\n    ignore_order : bool, default False\n        If true, the ordered attribute of the Categoricals will be ignored.\n        Results in an unordered categorical.\n\n    Returns\n    -------\n    Categorical\n\n    Raises\n    ------\n    TypeError\n        - all inputs do not have the same dtype\n        - all inputs do not have the same ordered property\n        - all inputs are ordered and their categories are not identical\n        - sort_categories=True and Categoricals are ordered\n    ValueError\n        Empty list of categoricals passed\n\n    Notes\n    -----\n    To learn more about categories, see `link\n    <https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#unioning>`__\n\n    Examples\n    --------\n    >>> from pandas.api.types import union_categoricals\n\n    If you want to combine categoricals that do not necessarily have\n    the same categories, `union_categoricals` will combine a list-like\n    of categoricals. The new categories will be the union of the\n    categories being combined.\n\n    >>> a = pd.Categorical(["b", "c"])\n    >>> b = pd.Categorical(["a", "b"])\n    >>> union_categoricals([a, b])\n    [\'b\', \'c\', \'a\', \'b\']\n    Categories (3, object): [\'b\', \'c\', \'a\']\n\n    By default, the resulting categories will be ordered as they appear\n    in the `categories` of the data. If you want the categories to be\n    lexsorted, use `sort_categories=True` argument.\n\n    >>> union_categoricals([a, b], sort_categories=True)\n    [\'b\', \'c\', \'a\', \'b\']\n    Categories (3, object): [\'a\', \'b\', \'c\']\n\n    `union_categoricals` also works with the case of combining two\n    categoricals of the same categories and order information (e.g. what\n    you could also `append` for).\n\n    >>> a = pd.Categorical(["a", "b"], ordered=True)\n    >>> b = pd.Categorical(["a", "b", "a"], ordered=True)\n    >>> union_categoricals([a, b])\n    [\'a\', \'b\', \'a\', \'b\', \'a\']\n    Categories (2, object): [\'a\' < \'b\']\n\n    Raises `TypeError` because the categories are ordered and not identical.\n\n    >>> a = pd.Categorical(["a", "b"], ordered=True)\n    >>> b = pd.Categorical(["a", "b", "c"], ordered=True)\n    >>> union_categoricals([a, b])\n    Traceback (most recent call last):\n        ...\n    TypeError: to union ordered Categoricals, all categories must be the same\n\n    New in version 0.20.0\n\n    Ordered categoricals with different categories or orderings can be\n    combined by using the `ignore_ordered=True` argument.\n\n    >>> a = pd.Categorical(["a", "b", "c"], ordered=True)\n    >>> b = pd.Categorical(["c", "b", "a"], ordered=True)\n    >>> union_categoricals([a, b], ignore_order=True)\n    [\'a\', \'b\', \'c\', \'c\', \'b\', \'a\']\n    Categories (3, object): [\'a\', \'b\', \'c\']\n\n    `union_categoricals` also works with a `CategoricalIndex`, or `Series`\n    containing categorical data, but note that the resulting array will\n    always be a plain `Categorical`\n\n    >>> a = pd.Series(["b", "c"], dtype=\'category\')\n    >>> b = pd.Series(["a", "b"], dtype=\'category\')\n    >>> union_categoricals([a, b])\n    [\'b\', \'c\', \'a\', \'b\']\n    Categories (3, object): [\'b\', \'c\', \'a\']\n    '
    ...

def __getattr__(name) -> typing.Any:
    ...

