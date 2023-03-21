from django.db.backends.sqlite3.client import DatabaseClient as DatabaseClient

class SpatiaLiteClient(DatabaseClient):
    executable_name: str = ...
