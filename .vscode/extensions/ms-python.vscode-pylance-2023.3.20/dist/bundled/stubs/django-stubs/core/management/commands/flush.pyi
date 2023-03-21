from typing import Tuple

from django.apps import apps as apps
from django.core.management.base import BaseCommand as BaseCommand
from django.core.management.base import CommandError as CommandError
from django.core.management.color import Style
from django.core.management.color import no_style as no_style
from django.core.management.sql import (
    emit_post_migrate_signal as emit_post_migrate_signal,
)
from django.core.management.sql import sql_flush as sql_flush
from django.db import DEFAULT_DB_ALIAS as DEFAULT_DB_ALIAS
from django.db import connections as connections

class Command(BaseCommand):
    stealth_options: Tuple[str] = ...
    style: Style = ...
