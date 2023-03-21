from typing import Any

from django.contrib import admin as admin

class SiteAdmin(admin.ModelAdmin[Any]):
    list_display: Any = ...
    search_fields: Any = ...
