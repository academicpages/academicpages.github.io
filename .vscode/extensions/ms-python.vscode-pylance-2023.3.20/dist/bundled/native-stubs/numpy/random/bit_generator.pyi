# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: numpy, version: 1.20.2
# Module: numpy.random.bit_generator, version: unspecified
import typing
import abc as _mod_abc
import builtins as _mod_builtins
import itertools as _mod_itertools
import re as _mod_re

class BitGenerator(_mod_builtins.object):
    "\n    BitGenerator(seed=None)\n\n    Base Class for generic BitGenerators, which provide a stream\n    of random bits based on different algorithms. Must be overridden.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        ~`numpy.random.SeedSequence` to derive the initial `BitGenerator` state.\n        One may also pass in a `SeedSequence` instance.\n\n    Attributes\n    ----------\n    lock : threading.Lock\n        Lock instance that is shared so that the same BitGenerator can\n        be used in multiple Generators without corrupting the state. Code that\n        generates values from a bit generator should hold the bit generator's\n        lock.\n\n    See Also\n    --------\n    SeedSequence\n    "
    def __getstate__(self) -> typing.Any:
        ...
    
    def __init__(self, seed=...) -> None:
        "\n    BitGenerator(seed=None)\n\n    Base Class for generic BitGenerators, which provide a stream\n    of random bits based on different algorithms. Must be overridden.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        ~`numpy.random.SeedSequence` to derive the initial `BitGenerator` state.\n        One may also pass in a `SeedSequence` instance.\n\n    Attributes\n    ----------\n    lock : threading.Lock\n        Lock instance that is shared so that the same BitGenerator can\n        be used in multiple Generators without corrupting the state. Code that\n        generates values from a bit generator should hold the bit generator's\n        lock.\n\n    See Also\n    --------\n    SeedSequence\n    "
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
    
    def _benchmark(self) -> typing.Any:
        'Used in tests'
        ...
    
    @property
    def _cffi(self) -> typing.Any:
        ...
    
    @property
    def _ctypes(self) -> typing.Any:
        ...
    
    @property
    def _seed_seq(self) -> typing.Any:
        ...
    
    @property
    def capsule(self) -> typing.Any:
        ...
    
    @property
    def cffi(self) -> typing.Any:
        '\n        CFFI interface\n\n        Returns\n        -------\n        interface : namedtuple\n            Named tuple containing CFFI wrapper\n\n            * state_address - Memory address of the state struct\n            * state - pointer to the state struct\n            * next_uint64 - function pointer to produce 64 bit integers\n            * next_uint32 - function pointer to produce 32 bit integers\n            * next_double - function pointer to produce doubles\n            * bitgen - pointer to the bit generator struct\n        '
        ...
    
    @property
    def ctypes(self) -> typing.Any:
        '\n        ctypes interface\n\n        Returns\n        -------\n        interface : namedtuple\n            Named tuple containing ctypes wrapper\n\n            * state_address - Memory address of the state struct\n            * state - pointer to the state struct\n            * next_uint64 - function pointer to produce 64 bit integers\n            * next_uint32 - function pointer to produce 32 bit integers\n            * next_double - function pointer to produce doubles\n            * bitgen - pointer to the bit generator struct\n        '
        ...
    
    @property
    def lock(self) -> typing.Any:
        ...
    
    def random_raw(self, size=...) -> typing.Any:
        '\n        random_raw(self, size=None)\n\n        Return randoms as generated by the underlying BitGenerator\n\n        Parameters\n        ----------\n        size : int or tuple of ints, optional\n            Output shape.  If the given shape is, e.g., ``(m, n, k)``, then\n            ``m * n * k`` samples are drawn.  Default is None, in which case a\n            single value is returned.\n        output : bool, optional\n            Output values.  Used for performance testing since the generated\n            values are not returned.\n\n        Returns\n        -------\n        out : uint or ndarray\n            Drawn samples.\n\n        Notes\n        -----\n        This method directly exposes the the raw underlying pseudo-random\n        number generator. All values are returned as unsigned 64-bit\n        values irrespective of the number of bits produced by the PRNG.\n\n        See the class docstring for the number of bits returned.\n        '
        ...
    
    @property
    def state(self) -> typing.Any:
        '\n        Get or set the PRNG state\n\n        The base BitGenerator.state must be overridden by a subclass\n\n        Returns\n        -------\n        state : dict\n            Dictionary containing the information required to describe the\n            state of the PRNG\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

DECIMAL_RE: _mod_re.Pattern
class ISeedSequence(_mod_abc.ABC):
    '\n    Abstract base class for seed sequences.\n\n    ``BitGenerator`` implementations should treat any object that adheres to\n    this interface as a seed sequence.\n\n    See Also\n    --------\n    SeedSequence, SeedlessSeedSequence\n    '
    __abstractmethods__: frozenset
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        '\n    Abstract base class for seed sequences.\n\n    ``BitGenerator`` implementations should treat any object that adheres to\n    this interface as a seed sequence.\n\n    See Also\n    --------\n    SeedSequence, SeedlessSeedSequence\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    _abc_impl: _mod__abc._abc_data
    def generate_state(self, n_words, dtype) -> typing.Any:
        "\n        generate_state(n_words, dtype=np.uint32)\n\n        Return the requested number of words for PRNG seeding.\n\n        A BitGenerator should call this method in its constructor with\n        an appropriate `n_words` parameter to properly seed itself.\n\n        Parameters\n        ----------\n        n_words : int\n        dtype : np.uint32 or np.uint64, optional\n            The size of each word. This should only be either `uint32` or\n            `uint64`. Strings (`'uint32'`, `'uint64'`) are fine. Note that\n            requesting `uint64` will draw twice as many bits as `uint32` for\n            the same `n_words`. This is a convenience for `BitGenerator`s that\n            express their states as `uint64` arrays.\n\n        Returns\n        -------\n        state : uint32 or uint64 array, shape=(n_words,)\n        "
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ISpawnableSeedSequence(ISeedSequence):
    '\n    Abstract base class for seed sequences that can spawn.\n    '
    __abstractmethods__: frozenset
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        '\n    Abstract base class for seed sequences that can spawn.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    _abc_impl: _mod__abc._abc_data
    def spawn(self, n_children) -> typing.Any:
        '\n        spawn(n_children)\n\n        Spawn a number of child `SeedSequence` s by extending the\n        `spawn_key`.\n\n        Parameters\n        ----------\n        n_children : int\n\n        Returns\n        -------\n        seqs : list of `SeedSequence` s\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def Lock() -> typing.Any:
    'allocate_lock() -> lock object\n(allocate() is an obsolete synonym)\n\nCreate a new lock object. See help(type(threading.Lock())) for\ninformation about locks.'
    ...

class SeedSequence(_mod_builtins.object):
    '\n    SeedSequence(entropy=None, *, spawn_key=(), pool_size=4)\n\n    SeedSequence mixes sources of entropy in a reproducible way to set the\n    initial state for independent and very probably non-overlapping\n    BitGenerators.\n\n    Once the SeedSequence is instantiated, you can call the `generate_state`\n    method to get an appropriately sized seed. Calling `spawn(n) <spawn>` will\n    create ``n`` SeedSequences that can be used to seed independent\n    BitGenerators, i.e. for different threads.\n\n    Parameters\n    ----------\n    entropy : {None, int, sequence[int]}, optional\n        The entropy for creating a `SeedSequence`.\n    spawn_key : {(), sequence[int]}, optional\n        A third source of entropy, used internally when calling\n        `SeedSequence.spawn`\n    pool_size : {int}, optional\n        Size of the pooled entropy to store. Default is 4 to give a 128-bit\n        entropy pool. 8 (for 256 bits) is another reasonable choice if working\n        with larger PRNGs, but there is very little to be gained by selecting\n        another value.\n    n_children_spawned : {int}, optional\n        The number of children already spawned. Only pass this if\n        reconstructing a `SeedSequence` from a serialized form.\n\n    Notes\n    -----\n\n    Best practice for achieving reproducible bit streams is to use\n    the default ``None`` for the initial entropy, and then use\n    `SeedSequence.entropy` to log/pickle the `entropy` for reproducibility:\n\n    >>> sq1 = np.random.SeedSequence()\n    >>> sq1.entropy\n    243799254704924441050048792905230269161  # random\n    >>> sq2 = np.random.SeedSequence(sq1.entropy)\n    >>> np.all(sq1.generate_state(10) == sq2.generate_state(10))\n    True\n    '
    def __init__(self, entropy=..., *, spawn_key=..., pool_size=...) -> None:
        '\n    SeedSequence(entropy=None, *, spawn_key=(), pool_size=4)\n\n    SeedSequence mixes sources of entropy in a reproducible way to set the\n    initial state for independent and very probably non-overlapping\n    BitGenerators.\n\n    Once the SeedSequence is instantiated, you can call the `generate_state`\n    method to get an appropriately sized seed. Calling `spawn(n) <spawn>` will\n    create ``n`` SeedSequences that can be used to seed independent\n    BitGenerators, i.e. for different threads.\n\n    Parameters\n    ----------\n    entropy : {None, int, sequence[int]}, optional\n        The entropy for creating a `SeedSequence`.\n    spawn_key : {(), sequence[int]}, optional\n        A third source of entropy, used internally when calling\n        `SeedSequence.spawn`\n    pool_size : {int}, optional\n        Size of the pooled entropy to store. Default is 4 to give a 128-bit\n        entropy pool. 8 (for 256 bits) is another reasonable choice if working\n        with larger PRNGs, but there is very little to be gained by selecting\n        another value.\n    n_children_spawned : {int}, optional\n        The number of children already spawned. Only pass this if\n        reconstructing a `SeedSequence` from a serialized form.\n\n    Notes\n    -----\n\n    Best practice for achieving reproducible bit streams is to use\n    the default ``None`` for the initial entropy, and then use\n    `SeedSequence.entropy` to log/pickle the `entropy` for reproducibility:\n\n    >>> sq1 = np.random.SeedSequence()\n    >>> sq1.entropy\n    243799254704924441050048792905230269161  # random\n    >>> sq2 = np.random.SeedSequence(sq1.entropy)\n    >>> np.all(sq1.generate_state(10) == sq2.generate_state(10))\n    True\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce__(self) -> typing.Union[str, typing.Tuple[typing.Any, ...]]:
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __setstate__(self, state: typing.Any) -> None:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def entropy(self) -> typing.Any:
        ...
    
    def generate_state(self, *args, **kwds) -> typing.Any:
        "\n        generate_state(n_words, dtype=np.uint32)\n\n        Return the requested number of words for PRNG seeding.\n\n        A BitGenerator should call this method in its constructor with\n        an appropriate `n_words` parameter to properly seed itself.\n\n        Parameters\n        ----------\n        n_words : int\n        dtype : np.uint32 or np.uint64, optional\n            The size of each word. This should only be either `uint32` or\n            `uint64`. Strings (`'uint32'`, `'uint64'`) are fine. Note that\n            requesting `uint64` will draw twice as many bits as `uint32` for\n            the same `n_words`. This is a convenience for `BitGenerator`s that\n            express their states as `uint64` arrays.\n\n        Returns\n        -------\n        state : uint32 or uint64 array, shape=(n_words,)\n        "
        ...
    
    @property
    def n_children_spawned(self) -> typing.Any:
        ...
    
    @property
    def pool(self) -> typing.Any:
        ...
    
    @property
    def pool_size(self) -> typing.Any:
        ...
    
    def spawn(self, n_children) -> typing.Any:
        '\n        spawn(n_children)\n\n        Spawn a number of child `SeedSequence` s by extending the\n        `spawn_key`.\n\n        Parameters\n        ----------\n        n_children : int\n\n        Returns\n        -------\n        seqs : list of `SeedSequence` s\n        '
        ...
    
    @property
    def spawn_key(self) -> typing.Any:
        ...
    
    @property
    def state(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SeedlessSeedSequence(_mod_builtins.object):
    '\n    A seed sequence for BitGenerators with no need for seed state.\n\n    See Also\n    --------\n    SeedSequence, ISeedSequence\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    A seed sequence for BitGenerators with no need for seed state.\n\n    See Also\n    --------\n    SeedSequence, ISeedSequence\n    '
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
    
    def generate_state(self) -> typing.Any:
        ...
    
    def spawn(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SeedlessSequence(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__all__: list
__doc__: str
__file__: str
__name__: str
__package__: str
def __pyx_unpickle_SeedSequence() -> typing.Any:
    ...

def __pyx_unpickle_SeedlessSeedSequence() -> typing.Any:
    ...

__test__: dict
def _coerce_to_uint32_array() -> typing.Any:
    ' Coerce an input to a uint32 array.\n\n    If a `uint32` array, pass it through directly.\n    If a non-negative integer, then break it up into `uint32` words, lowest\n    bits first.\n    If a string starting with "0x", then interpret as a hex integer, as above.\n    If a string of decimal digits, interpret as a decimal integer, as above.\n    If a sequence of ints or strings, interpret each element as above and\n    concatenate.\n\n    Note that the handling of `int64` or `uint64` arrays are not just\n    straightforward views as `uint32` arrays. If an element is small enough to\n    fit into a `uint32`, then it will only take up one `uint32` element in the\n    output. This is to make sure that the interpretation of a sequence of\n    integers is the same regardless of numpy\'s default integer type, which\n    differs on different platforms.\n\n    Parameters\n    ----------\n    x : int, str, sequence of int or str\n\n    Returns\n    -------\n    seed_array : uint32 array\n\n    Examples\n    --------\n    >>> import numpy as np\n    >>> from numpy.random.bit_generator import _coerce_to_uint32_array\n    >>> _coerce_to_uint32_array(12345)\n    array([12345], dtype=uint32)\n    >>> _coerce_to_uint32_array(\'12345\')\n    array([12345], dtype=uint32)\n    >>> _coerce_to_uint32_array(\'0x12345\')\n    array([74565], dtype=uint32)\n    >>> _coerce_to_uint32_array([12345, \'67890\'])\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.uint32))\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array(np.array([12345, 67890], dtype=np.int64))\n    array([12345, 67890], dtype=uint32)\n    >>> _coerce_to_uint32_array([12345, 0x10deadbeef, 67890, 0xdeadbeef])\n    array([     12345, 3735928559,         16,      67890, 3735928559],\n          dtype=uint32)\n    >>> _coerce_to_uint32_array(1234567890123456789012345678901234567890)\n    array([3460238034, 2898026390, 3235640248, 2697535605,          3],\n          dtype=uint32)\n    '
    ...

def _int_to_uint32_array() -> typing.Any:
    ...

cycle = _mod_itertools.cycle
def randbits(self, k) -> typing.Any:
    'getrandbits(k) -> x.  Generates an int with k random bits.'
    ...

def __getattr__(name) -> typing.Any:
    ...

