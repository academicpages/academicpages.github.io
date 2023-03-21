# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: pandas, version: 1.2.4
# Module: pandas._libs.hashtable, version: unspecified
import typing
import builtins as _mod_builtins

class Factorizer(_mod_builtins.object):
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
    def count(self) -> typing.Any:
        ...
    
    def factorize(self) -> typing.Any:
        "\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        "
        ...
    
    def get_count(self) -> typing.Any:
        ...
    
    @property
    def table(self) -> typing.Any:
        ...
    
    def unique(self) -> typing.Any:
        ...
    
    @property
    def uniques(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float32HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[float32]\n            Array of values of which unique will be calculated\n        uniques : Float32Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[float32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[float32]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[float32]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[float32]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[float32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float32Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float64HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[float64]\n            Array of values of which unique will be calculated\n        uniques : Float64Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[float64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[float64]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[float64]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[float64]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[float64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Float64Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class HashTable(_mod_builtins.object):
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int16HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int16]\n            Array of values of which unique will be calculated\n        uniques : Int16Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int16]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[int16]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[int16]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int16]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int16]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int16Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int32HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int32]\n            Array of values of which unique will be calculated\n        uniques : Int32Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[int32]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[int32]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int32]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int32Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64Factorizer(_mod_builtins.object):
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
    def count(self) -> typing.Any:
        ...
    
    def factorize(self) -> typing.Any:
        "\n        Examples\n        --------\n        Factorize values with nans replaced by na_sentinel\n\n        >>> factorize(np.array([1,2,np.nan], dtype='O'), na_sentinel=20)\n        array([ 0,  1, 20])\n        "
        ...
    
    def get_count(self) -> typing.Any:
        ...
    
    @property
    def table(self) -> typing.Any:
        ...
    
    @property
    def uniques(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int64]\n            Array of values of which unique will be calculated\n        uniques : Int64Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[int64]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[int64]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int64]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int64Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int8HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int8]\n            Array of values of which unique will be calculated\n        uniques : Int8Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int8]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[int8]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[int8]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[int8]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[int8]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Int8Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ObjectVector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class PyObjectHashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        uniques : ObjectVector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then None _plus_\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then None _plus_\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            Not yet implemented for PyObjectHashTable.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

SIZE_HINT_LIMIT: int
class StringHashTable(HashTable):
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        uniques : ObjectVector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then any value\n            that is not a string is considered missing. If na_value is\n            not None, then _additionally_ any value "val" satisfying\n            val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then any value\n            that is not a string is considered missing. If na_value is\n            not None, then _additionally_ any value "val" satisfying\n            val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            Not yet implementd for StringHashTable.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_indexer(self) -> typing.Any:
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    na_string_sentinel: str
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[object]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[object]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class StringVector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt16HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint16]\n            Array of values of which unique will be calculated\n        uniques : UInt16Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint16]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[uint16]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[uint16]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint16]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint16]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt16Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt32HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint32]\n            Array of values of which unique will be calculated\n        uniques : UInt32Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[uint32]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[uint32]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint32]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint32]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt32Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt64HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint64]\n            Array of values of which unique will be calculated\n        uniques : UInt64Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[uint64]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[uint64]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint64]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint64]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt64Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt8HashTable(HashTable):
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def _unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint8]\n            Array of values of which unique will be calculated\n        uniques : UInt8Vector\n            Vector into which uniques will be written\n        count_prior : Py_ssize_t, default 0\n            Number of existing entries in uniques\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        ignore_na : boolean, default False\n            Whether NA-values should be ignored for calculating the uniques. If\n            True, the labels corresponding to missing values will be set to\n            na_sentinel.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint8]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse=True)\n            The labels from values to uniques\n        '
        ...
    
    def factorize(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Missing values are not included in the "uniques" for this method.\n        The labels for any missing values will be set to "na_sentinel"\n\n        Parameters\n        ----------\n        values : ndarray[uint8]\n            Array of values of which unique will be calculated\n        na_sentinel : Py_ssize_t, default -1\n            Sentinel value used for all NA-values in inverse\n        na_value : object, default None\n            Value to identify as missing. If na_value is None, then\n            any value "val" satisfying val != val is considered missing.\n            If na_value is not None, then _additionally_, any value "val"\n            satisfying val == na_value is considered missing.\n        mask : ndarray[bool], optional\n            If not None, the mask is used as indicator for missing values\n            (True = missing, False = valid) instead of `na_value` or\n            condition "val != val".\n\n        Returns\n        -------\n        uniques : ndarray[uint8]\n            Unique values of input, not sorted\n        labels : ndarray[int64]\n            The labels from values to uniques\n        '
        ...
    
    def get_item(self) -> typing.Any:
        ...
    
    def get_labels(self) -> typing.Any:
        ...
    
    def get_labels_groupby(self) -> typing.Any:
        ...
    
    def lookup(self) -> typing.Any:
        ...
    
    def map(self) -> typing.Any:
        ...
    
    def map_locations(self) -> typing.Any:
        ...
    
    def set_item(self) -> typing.Any:
        ...
    
    def sizeof(self) -> typing.Any:
        ' return the size of my table in bytes '
        ...
    
    def unique(self) -> typing.Any:
        '\n        Calculate unique values and labels (no sorting!)\n\n        Parameters\n        ----------\n        values : ndarray[uint8]\n            Array of values of which unique will be calculated\n        return_inverse : boolean, default False\n            Whether the mapping of the original array values to their location\n            in the vector of uniques should be returned.\n\n        Returns\n        -------\n        uniques : ndarray[uint8]\n            Unique values of input, not sorted\n        labels : ndarray[int64] (if return_inverse)\n            The labels from values to uniques\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class UInt8Vector(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
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
    
    def to_array(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: typing.Any
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_Enum() -> typing.Any:
    ...

def __pyx_unpickle_Factorizer() -> typing.Any:
    ...

def __pyx_unpickle_HashTable() -> typing.Any:
    ...

def __pyx_unpickle_Int64Factorizer() -> typing.Any:
    ...

__test__: dict
def duplicated_float32() -> typing.Any:
    ...

def duplicated_float64() -> typing.Any:
    ...

def duplicated_int16() -> typing.Any:
    ...

def duplicated_int32() -> typing.Any:
    ...

def duplicated_int64() -> typing.Any:
    ...

def duplicated_int8() -> typing.Any:
    ...

def duplicated_object() -> typing.Any:
    ...

def duplicated_uint16() -> typing.Any:
    ...

def duplicated_uint32() -> typing.Any:
    ...

def duplicated_uint64() -> typing.Any:
    ...

def duplicated_uint8() -> typing.Any:
    ...

def get_hashtable_trace_domain() -> typing.Any:
    ...

def ismember_float32() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : float32 ndarray\n    values : float32 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_float64() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : float64 ndarray\n    values : float64 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_int16() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : int16 ndarray\n    values : int16 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_int32() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : int32 ndarray\n    values : int32 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_int64() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : int64 ndarray\n    values : int64 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_int8() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : int8 ndarray\n    values : int8 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_object() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : object ndarray\n    values : object ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_uint16() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : uint16 ndarray\n    values : uint16 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_uint32() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : uint32 ndarray\n    values : uint32 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_uint64() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : uint64 ndarray\n    values : uint64 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def ismember_uint8() -> typing.Any:
    '\n    Return boolean of values in arr on an\n    element by-element basis\n\n    Parameters\n    ----------\n    arr : uint8 ndarray\n    values : uint8 ndarray\n\n    Returns\n    -------\n    boolean ndarry len of (arr)\n    '
    ...

def mode_float32() -> typing.Any:
    ...

def mode_float64() -> typing.Any:
    ...

def mode_int16() -> typing.Any:
    ...

def mode_int32() -> typing.Any:
    ...

def mode_int64() -> typing.Any:
    ...

def mode_int8() -> typing.Any:
    ...

def mode_object() -> typing.Any:
    ...

def mode_uint16() -> typing.Any:
    ...

def mode_uint32() -> typing.Any:
    ...

def mode_uint64() -> typing.Any:
    ...

def mode_uint8() -> typing.Any:
    ...

def unique_label_indices() -> typing.Any:
    '\n    Indices of the first occurrences of the unique labels\n    *excluding* -1. equivalent to:\n        np.unique(labels, return_index=True)[1]\n    '
    ...

def value_count_float32() -> typing.Any:
    ...

def value_count_float64() -> typing.Any:
    ...

def value_count_int16() -> typing.Any:
    ...

def value_count_int32() -> typing.Any:
    ...

def value_count_int64() -> typing.Any:
    ...

def value_count_int8() -> typing.Any:
    ...

def value_count_object() -> typing.Any:
    ...

def value_count_uint16() -> typing.Any:
    ...

def value_count_uint32() -> typing.Any:
    ...

def value_count_uint64() -> typing.Any:
    ...

def value_count_uint8() -> typing.Any:
    ...

def __getattr__(name) -> typing.Any:
    ...

