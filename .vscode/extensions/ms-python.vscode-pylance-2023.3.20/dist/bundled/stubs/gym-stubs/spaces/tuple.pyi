from typing import Sequence

import numpy as np

from .space import Space

class Tuple(Space):
    def __init__(self, spaces: Sequence[Space]): ...
