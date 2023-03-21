from django.db.backends.base.client import BaseDatabaseClient as BaseDatabaseClient

class DatabaseClient(BaseDatabaseClient):
    executable_name: str = ...
