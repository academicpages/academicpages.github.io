from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.sql import sql_flush as sql_flush
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import connections as connections

class Command(BaseCommand):
    output_transaction: bool = ...
