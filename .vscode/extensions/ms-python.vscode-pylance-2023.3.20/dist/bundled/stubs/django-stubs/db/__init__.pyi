from typing import Any

from django.db.backends.utils import CursorWrapper

from . import migrations as migrations
from .utils import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from .utils import DJANGO_VERSION_PICKLE_KEY as DJANGO_VERSION_PICKLE_KEY
from .utils import ConnectionDoesNotExist as ConnectionDoesNotExist
from .utils import ConnectionHandler as ConnectionHandler
from .utils import DatabaseError as DatabaseError
from .utils import DataError as DataError
from .utils import Error as Error
from .utils import IntegrityError as IntegrityError
from .utils import InterfaceError as InterfaceError
from .utils import InternalError as InternalError
from .utils import NotSupportedError as NotSupportedError
from .utils import OperationalError as OperationalError
from .utils import ProgrammingError as ProgrammingError

connections: ConnectionHandler
router: Any
connection: DefaultConnectionProxy

class DefaultConnectionProxy:
    def cursor(self) -> CursorWrapper: ...
    def __getattr__(self, item: str) -> Any: ...
    def __setattr__(self, name: str, value: Any) -> None: ...
    def __delattr__(self, name: str) -> None: ...

def close_old_connections(**kwargs: Any) -> None: ...
def reset_queries(**kwargs: Any) -> None: ...
