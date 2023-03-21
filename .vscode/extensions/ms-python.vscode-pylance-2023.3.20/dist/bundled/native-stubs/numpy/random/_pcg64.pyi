# Python: 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]
# Library: numpy, version: 1.20.2
# Module: numpy.random._pcg64, version: unspecified
import typing
import builtins as _mod_builtins
import numpy.random.bit_generator as _mod_numpy_random_bit_generator

class PCG64(_mod_numpy_random_bit_generator.BitGenerator):
    '\n    PCG64(seed=None)\n\n    BitGenerator for the PCG-64 pseudo-random number generator.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Notes\n    -----\n    PCG-64 is a 128-bit implementation of O\'Neill\'s permutation congruential\n    generator ([1]_, [2]_). PCG-64 has a period of :math:`2^{128}` and supports\n    advancing an arbitrary number of steps as well as :math:`2^{127}` streams.\n    The specific member of the PCG family that we use is PCG XSL RR 128/64\n    as described in the paper ([2]_).\n\n    ``PCG64`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    Supports the method :meth:`advance` to advance the RNG an arbitrary number of\n    steps. The state of the PCG-64 RNG is represented by 2 128-bit unsigned\n    integers.\n\n    **State and Seeding**\n\n    The ``PCG64`` state vector consists of 2 unsigned 128-bit values,\n    which are represented externally as Python ints. One is the state of the\n    PRNG, which is advanced by a linear congruential generator (LCG). The\n    second is a fixed odd increment used in the LCG.\n\n    The input seed is processed by `SeedSequence` to generate both values. The\n    increment is not independently settable.\n\n    **Parallel Features**\n\n    The preferred way to use a BitGenerator in parallel applications is to use\n    the `SeedSequence.spawn` method to obtain entropy values, and to use these\n    to generate new BitGenerators:\n\n    >>> from numpy.random import Generator, PCG64, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> rg = [Generator(PCG64(s)) for s in sg.spawn(10)]\n\n    **Compatibility Guarantee**\n\n    ``PCG64`` makes a guarantee that a fixed seed and will always produce\n    the same random integer stream.\n\n    References\n    ----------\n    .. [1] `"PCG, A Family of Better Random Number Generators"\n           <http://www.pcg-random.org/>`_\n    .. [2] O\'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient\n           Statistically Good Algorithms for Random Number Generation"\n           <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_\n    '
    def __init__(self, seed=...) -> None:
        '\n    PCG64(seed=None)\n\n    BitGenerator for the PCG-64 pseudo-random number generator.\n\n    Parameters\n    ----------\n    seed : {None, int, array_like[ints], SeedSequence}, optional\n        A seed to initialize the `BitGenerator`. If None, then fresh,\n        unpredictable entropy will be pulled from the OS. If an ``int`` or\n        ``array_like[ints]`` is passed, then it will be passed to\n        `SeedSequence` to derive the initial `BitGenerator` state. One may also\n        pass in a `SeedSequence` instance.\n\n    Notes\n    -----\n    PCG-64 is a 128-bit implementation of O\'Neill\'s permutation congruential\n    generator ([1]_, [2]_). PCG-64 has a period of :math:`2^{128}` and supports\n    advancing an arbitrary number of steps as well as :math:`2^{127}` streams.\n    The specific member of the PCG family that we use is PCG XSL RR 128/64\n    as described in the paper ([2]_).\n\n    ``PCG64`` provides a capsule containing function pointers that produce\n    doubles, and unsigned 32 and 64- bit integers. These are not\n    directly consumable in Python and must be consumed by a ``Generator``\n    or similar object that supports low-level access.\n\n    Supports the method :meth:`advance` to advance the RNG an arbitrary number of\n    steps. The state of the PCG-64 RNG is represented by 2 128-bit unsigned\n    integers.\n\n    **State and Seeding**\n\n    The ``PCG64`` state vector consists of 2 unsigned 128-bit values,\n    which are represented externally as Python ints. One is the state of the\n    PRNG, which is advanced by a linear congruential generator (LCG). The\n    second is a fixed odd increment used in the LCG.\n\n    The input seed is processed by `SeedSequence` to generate both values. The\n    increment is not independently settable.\n\n    **Parallel Features**\n\n    The preferred way to use a BitGenerator in parallel applications is to use\n    the `SeedSequence.spawn` method to obtain entropy values, and to use these\n    to generate new BitGenerators:\n\n    >>> from numpy.random import Generator, PCG64, SeedSequence\n    >>> sg = SeedSequence(1234)\n    >>> rg = [Generator(PCG64(s)) for s in sg.spawn(10)]\n\n    **Compatibility Guarantee**\n\n    ``PCG64`` makes a guarantee that a fixed seed and will always produce\n    the same random integer stream.\n\n    References\n    ----------\n    .. [1] `"PCG, A Family of Better Random Number Generators"\n           <http://www.pcg-random.org/>`_\n    .. [2] O\'Neill, Melissa E. `"PCG: A Family of Simple Fast Space-Efficient\n           Statistically Good Algorithms for Random Number Generation"\n           <https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>`_\n    '
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
    
    def advance(self, delta) -> typing.Any:
        '\n        advance(delta)\n\n        Advance the underlying RNG as-if delta draws have occurred.\n\n        Parameters\n        ----------\n        delta : integer, positive\n            Number of draws to advance the RNG. Must be less than the\n            size state variable in the underlying RNG.\n\n        Returns\n        -------\n        self : PCG64\n            RNG advanced delta steps\n\n        Notes\n        -----\n        Advancing a RNG updates the underlying RNG state as-if a given\n        number of calls to the underlying RNG have been made. In general\n        there is not a one-to-one relationship between the number output\n        random values from a particular distribution and the number of\n        draws from the core RNG.  This occurs for two reasons:\n\n        * The random values are simulated using a rejection-based method\n          and so, on average, more than one value from the underlying\n          RNG is required to generate an single draw.\n        * The number of bits required to generate a simulated value\n          differs from the number of bits generated by the underlying\n          RNG.  For example, two 16-bit integer values can be simulated\n          from a single draw of a 32-bit RNG.\n\n        Advancing the RNG state resets any pre-computed random numbers.\n        This is required to ensure exact reproducibility.\n        '
        ...
    
    def jumped(self, jumps=...) -> typing.Any:
        '\n        jumped(jumps=1)\n\n        Returns a new bit generator with the state jumped.\n\n        Jumps the state as-if jumps * 210306068529402873165736369884012333109\n        random numbers have been generated.\n\n        Parameters\n        ----------\n        jumps : integer, positive\n            Number of times to jump the state of the bit generator returned\n\n        Returns\n        -------\n        bit_generator : PCG64\n            New instance of generator jumped iter times\n\n        Notes\n        -----\n        The step size is phi-1 when multiplied by 2**128 where phi is the\n        golden ratio.\n        '
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

