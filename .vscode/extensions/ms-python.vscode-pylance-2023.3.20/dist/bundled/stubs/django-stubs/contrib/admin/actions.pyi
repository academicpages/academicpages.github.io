from typing import Any, Optional

from django.contrib.admin.options import ModelAdmin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.template.response import TemplateResponse

def delete_selected(
    modeladmin: ModelAdmin[Any], request: WSGIRequest, queryset: QuerySet[Any]
) -> Optional[TemplateResponse]: ...
