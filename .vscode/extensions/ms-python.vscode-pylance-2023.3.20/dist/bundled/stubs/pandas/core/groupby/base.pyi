# from pandas.core.dtypes.common import is_list_like as is_list_like, is_scalar as is_scalar
from collections.abc import Hashable
import dataclasses

@dataclasses.dataclass(order=True, frozen=True)
class OutputKey:
    label: Hashable
    position: int
