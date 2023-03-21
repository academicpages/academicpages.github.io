# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: numpy, version: 1.20.2
# Module: numpy.random._mt19937, version: unspecified
import typing
import builtins as _mod_builtins
import numpy.random.bit_generator as _mod_numpy_random_bit_generator

class MT19937(_mod_numpy_random_bit_generator.BitGenerator):
    '\n    MT19937(seed=None)\n\n    Container for the Mersenne Twister pseudo-random number generator.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Attributes\n    ----------\n    lock: threading.Lock\n        Lock instance that is shared so that the same bit git generator can\n        be used in multiple Generators without corrupting the state. Code that\n        generates values from a bit generator should hold the bit generator\'s\n        lock.\n\n    Notes\n    -----\n    ``MT19937`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers [1]_. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    The Python stdlib module "random" also contains a Mersenne Twister\n    pseudo-random number generator.\n\n    **State and Seeding**\n\n    The ``MT19937`` state vector consists of a 624-element array of\n    32-bit unsigned integers plus a single integer value between 0 and 624\n    that indexes the current position within the main array.\n\n    The input seed is processed by `SeedSequence` to fill the whole state. The\n    first element is reset such that only its most significant bit is set.\n\n    **Parallel Features**\n\n    The preferred way to use a BitGenerator in parallel applications is to use\n    the `SeedSequence.spawn` method to obtain entropy values, and to use these\n    to generate new BitGenerators:\n\n    >>> from numpy.random import Generator, MT19937, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> rg = [Generator(MT19937(s)) for s in sg.spawn(10)]\n\n    Another method is to use `MT19937.jumped` which advances the state as-if\n    :math:`2^{128}` random numbers have been generated ([1]_, [2]_). This\n    allows the original sequence to be split so that distinct segments can be\n    used in each worker process. All generators should be chained to ensure\n    that the segments come from the same sequence.\n\n    >>> from numpy.random import Generator, MT19937, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> bit_generator = MT19937(sg)\n    >>> rg = []\n    >>> for _ in range(10):\n    ...    rg.append(Generator(bit_generator))\n    ...    # Chain the BitGenerators\n    ...    bit_generator = bit_generator.jumped()\n\n    **Compatibility Guarantee**\n\n    ``MT19937`` makes a guarantee that a fixed seed and will always produce\n    the same random integer stream.\n\n    References\n    ----------\n    .. [1] Hiroshi Haramoto, Makoto Matsumoto, and Pierre L\'Ecuyer, "A Fast\n        Jump Ahead Algorithm for Linear Recurrences in a Polynomial Space",\n        Sequences and Their Applications - SETA, 290--298, 2008.\n    .. [2] Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François\n        Panneton, Pierre L\'Ecuyer, "Efficient Jump Ahead for F2-Linear\n        Random Number Generators", INFORMS JOURNAL ON COMPUTING, Vol. 20,\n        No. 3, Summer 2008, pp. 385-390.\n\n    '
    def __init__(self, seed=...) -> None:
        '\n    MT19937(seed=None)\n\n    Container for the Mersenne Twister pseudo-random number generator.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Attributes\n    ----------\n    lock: threading.Lock\n        Lock instance that is shared so that the same bit git generator can\n        be used in multiple Generators without corrupting the state. Code that\n        generates values from a bit generator should hold the bit generator\'s\n        lock.\n\n    Notes\n    -----\n    ``MT19937`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers [1]_. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    The Python stdlib module "random" also contains a Mersenne Twister\n    pseudo-random number generator.\n\n    **State and Seeding**\n\n    The ``MT19937`` state vector consists of a 624-element array of\n    32-bit unsigned integers plus a single integer value between 0 and 624\n    that indexes the current position within the main array.\n\n    The input seed is processed by `SeedSequence` to fill the whole state. The\n    first element is reset such that only its most significant bit is set.\n\n    **Parallel Features**\n\n    The preferred way to use a BitGenerator in parallel applications is to use\n    the `SeedSequence.spawn` method to obtain entropy values, and to use these\n    to generate new BitGenerators:\n\n    >>> from numpy.random import Generator, MT19937, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> rg = [Generator(MT19937(s)) for s in sg.spawn(10)]\n\n    Another method is to use `MT19937.jumped` which advances the state as-if\n    :math:`2^{128}` random numbers have been generated ([1]_, [2]_). This\n    allows the original sequence to be split so that distinct segments can be\n    used in each worker process. All generators should be chained to ensure\n    that the segments come from the same sequence.\n\n    >>> from numpy.random import Generator, MT19937, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> bit_generator = MT19937(sg)\n    >>> rg = []\n    >>> for _ in range(10):\n    ...    rg.append(Generator(bit_generator))\n    ...    # Chain the BitGenerators\n    ...    bit_generator = bit_generator.jumped()\n\n    **Compatibility Guarantee**\n\n    ``MT19937`` makes a guarantee that a fixed seed and will always produce\n    the same random integer stream.\n\n    References\n    ----------\n    .. [1] Hiroshi Haramoto, Makoto Matsumoto, and Pierre L\'Ecuyer, "A Fast\n        Jump Ahead Algorithm for Linear Recurrences in a Polynomial Space",\n        Sequences and Their Applications - SETA, 290--298, 2008.\n    .. [2] Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François\n        Panneton, Pierre L\'Ecuyer, "Efficient Jump Ahead for F2-Linear\n        Random Number Generators", INFORMS JOURNAL ON COMPUTING, Vol. 20,\n        No. 3, Summer 2008, pp. 385-390.\n\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __reduce_cython__(self) -> typing.Any:
        ...
    
    def __setstate_cython__(self) -> typing.Any:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _legacy_seeding(self, seed) -> typing.Any:
        '\n        _legacy_seeding(seed)\n\n        Seed the generator in a backward compatible way. For modern\n        applications, creating a new instance is preferable. Calling this\n        overrides self._seed_seq\n\n        Parameters\n        ----------\n        seed : {None, int, array_like}\n            Random seed initializing the pseudo-random number generator.\n            Can be an integer in [0, 2**32-1], array of integers in\n            [0, 2**32-1], a `SeedSequence, or ``None``. If `seed`\n            is ``None``, then fresh, unpredictable entropy will be pulled from\n            the OS.\n\n        Raises\n        ------\n        ValueError\n            If seed values are out of range for the PRNG.\n        '
        ...
    
    def jumped(self, jumps=...) -> typing.Any:
        '\n        jumped(jumps=1)\n\n        Returns a new bit generator with the state jumped\n\n        The state of the returned big generator is jumped as-if\n        2**(128 * jumps) random numbers have been generated.\n\n        Parameters\n        ----------\n        jumps : integer, positive\n            Number of times to jump the state of the bit generator returned\n\n        Returns\n        -------\n        bit_generator : MT19937\n            New instance of generator jumped iter times\n\n        Notes\n        -----\n        The jump step is computed using a modified version of Matsumoto\'s\n        implementation of Horner\'s method. The step polynomial is precomputed\n        to perform 2**128 steps. The jumped state has been verified to match\n        the state produced using Matsumoto\'s original code.\n\n        References\n        ----------\n        .. [1] Matsumoto, M, Generating multiple disjoint streams of\n           pseudorandom number sequences.  Accessed on: May 6, 2020.\n           http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/JUMP/\n        .. [2] Hiroshi Haramoto, Makoto Matsumoto, Takuji Nishimura, François\n           Panneton, Pierre L\'Ecuyer, "Efficient Jump Ahead for F2-Linear\n           Random Number Generators", INFORMS JOURNAL ON COMPUTING, Vol. 20,\n           No. 3, Summer 2008, pp. 385-390.\n        '
        ...
    
    @property
    def state(self) -> typing.Any:
        '\n        Get or set the PRNG state\n\n        Returns\n        -------\n        state : dict\n            Dictionary containing the information required to describe the\n            state of the PRNG\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__all__: list
__doc__: typing.Any
__file__: str
__name__: str
__package__: str
__test__: dict
def __getattr__(name) -> typing.Any:
    ...

