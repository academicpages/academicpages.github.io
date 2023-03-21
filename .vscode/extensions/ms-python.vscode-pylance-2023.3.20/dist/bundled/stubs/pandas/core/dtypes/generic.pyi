from pandas import Series
from pandas.core.arrays import ExtensionArray
from typing_extensions import TypeAlias

ABCSeries: TypeAlias = type[Series]
ABCExtensionArray: TypeAlias = type[ExtensionArray]
