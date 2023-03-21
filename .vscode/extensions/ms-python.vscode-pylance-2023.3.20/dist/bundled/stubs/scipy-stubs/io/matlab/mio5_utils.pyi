# Python: 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Library: scipy, version: 1.6.2
# Module: scipy.io.matlab.mio5_utils, version: unspecified
import typing
import builtins as _mod_builtins
import scipy.sparse.csc as _mod_scipy_sparse_csc

class VarHeader5(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def dims(self) -> typing.Any:
        ...
    
    @property
    def is_global(self) -> typing.Any:
        ...
    
    @property
    def is_logical(self) -> typing.Any:
        ...
    
    @property
    def mclass(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def nzmax(self) -> typing.Any:
        ...
    
    def set_dims(self) -> typing.Any:
        ' Allow setting of dimensions from python\n\n        This is for constructing headers for tests\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class VarReader5(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
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
    
    def array_from_header(self) -> typing.Any:
        ' Read array of any class, given matrix `header`\n\n        Parameters\n        ----------\n        header : VarHeader5\n           array header object\n        process : int, optional\n           If not zero, apply post-processing on returned array\n           \n        Returns\n        -------\n        arr : array or sparse array\n           read array\n        '
        ...
    
    @property
    def is_swapped(self) -> typing.Any:
        ...
    
    @property
    def little_endian(self) -> typing.Any:
        ...
    
    def read_cells(self) -> typing.Any:
        ' Read cell array from stream '
        ...
    
    def read_char(self) -> typing.Any:
        ' Read char matrices from stream as arrays\n\n        Matrices of char are likely to be converted to matrices of\n        string by later processing in ``array_from_header``\n        '
        ...
    
    def read_fieldnames(self) -> typing.Any:
        'Read fieldnames for struct-like matrix.'
        ...
    
    def read_full_tag(self) -> typing.Any:
        ' Python method for reading full u4, u4 tag from stream\n\n        Returns\n        -------\n        mdtype : int32\n           matlab data type code\n        byte_count : int32\n           number of data bytes following\n\n        Notes\n        -----\n        Assumes tag is in fact full, that is, is not a small data\n        element.  This means it can skip some checks and makes it\n        slightly faster than ``read_tag``\n        '
        ...
    
    def read_header(self) -> typing.Any:
        ' Return matrix header for current stream position\n\n        Returns matrix headers at top level and sub levels\n\n        Parameters\n        ----------\n        check_stream_limit : if True, then if the returned header\n        is passed to array_from_header, it will be verified that\n        the length of the uncompressed data is not overlong (which\n        can indicate .mat file corruption)\n        '
        ...
    
    def read_numeric(self) -> typing.Any:
        ' Read numeric data element into ndarray\n\n        Reads element, then casts to ndarray.\n\n        The type of the array is usually given by the ``mdtype`` returned via\n        ``read_element``.  Sparse logical arrays are an exception, where the\n        type of the array may be ``np.bool_`` even if the ``mdtype`` claims the\n        data is of float64 type.\n\n        Parameters\n        ----------\n        copy : bool, optional\n            Whether to copy the array before returning.  If False, return array\n            backed by bytes read from file.\n        nnz : int, optional\n            Number of non-zero values when reading numeric data from sparse\n            matrices.  -1 if not reading sparse matrices, or to disable check\n            for bytes data instead of declared data type (see Notes).\n\n        Returns\n        -------\n        arr : array\n            Numeric array\n\n        Notes\n        -----\n        MATLAB apparently likes to store sparse logical matrix data as bytes\n        instead of miDOUBLE (float64) data type, even though the data element\n        still declares its type as miDOUBLE.  We can guess this has happened by\n        looking for the length of the data compared to the expected number of\n        elements, using the `nnz` input parameter.\n        '
        ...
    
    def read_opaque(self) -> typing.Any:
        " Read opaque (function workspace) type\n\n        Looking at some mat files, the structure of this type seems to\n        be:\n\n        * array flags as usual (already read into `hdr`)\n        * 3 int8 strings\n        * a matrix\n\n        Then there's a matrix at the end of the mat file that seems have\n        the anonymous founction workspaces - we load it as\n        ``__function_workspace__``\n\n        See the comments at the beginning of ``mio5.py``\n        "
        ...
    
    def read_real_complex(self) -> typing.Any:
        ' Read real / complex matrices from stream '
        ...
    
    def read_struct(self) -> typing.Any:
        ' Read struct or object array from stream\n\n        Objects are just structs with an extra field *classname*,\n        defined before (this here) struct format structure\n        '
        ...
    
    def read_tag(self) -> typing.Any:
        ' Read tag mdtype and byte_count\n\n        Does necessary swapping and takes account of SDE formats.\n\n        See also ``read_full_tag`` method.\n        \n        Returns\n        -------\n        mdtype : int\n           matlab data type code\n        byte_count : int\n           number of bytes following that comprise the data\n        tag_data : None or str\n           Any data from the tag itself.  This is None for a full tag,\n           and string length `byte_count` if this is a small data\n           element.\n        '
        ...
    
    def set_stream(self) -> typing.Any:
        ' Set stream of best type from file-like `fobj`\n\n        Called from Python when initiating a variable read\n        '
        ...
    
    def shape_from_header(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_VarHeader5() -> typing.Any:
    ...

__test__: dict
def asbytes(s) -> typing.Any:
    ...

def asstr(s) -> typing.Any:
    ...

def byteswap_u4() -> typing.Any:
    ...

def chars_to_strings() -> typing.Any:
    " Convert final axis of char array to strings\n\n    Parameters\n    ----------\n    in_arr : array\n       dtype of 'U1'\n\n    Returns\n    -------\n    str_arr : array\n       dtype of 'UN' where N is the length of the last dimension of\n       ``arr``\n    "
    ...

csc_matrix = _mod_scipy_sparse_csc.csc_matrix
def pycopy(x) -> typing.Any:
    "Shallow copy operation on arbitrary Python objects.\n\n    See the module's __doc__ string for more info.\n    "
    ...

def squeeze_element() -> typing.Any:
    ' Return squeezed element\n\n    The returned object may not be an ndarray - for example if we do\n    ``arr.item`` to return a ``mat_struct`` object from a struct array '
    ...

swapped_code: str
def __getattr__(name) -> typing.Any:
    ...

