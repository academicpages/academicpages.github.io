import numpy as np
from matplotlib._typing import *
from .triangulation import Triangulation

class TriFinder:
    def __init__(self, triangulation: Triangulation) -> None: ...

class TrapezoidMapTriFinder(TriFinder):
    def __init__(self, triangulation: Triangulation) -> None: ...
    def __call__(self, x: ArrayLike, y: ArrayLike) -> np.ndarray: ...
