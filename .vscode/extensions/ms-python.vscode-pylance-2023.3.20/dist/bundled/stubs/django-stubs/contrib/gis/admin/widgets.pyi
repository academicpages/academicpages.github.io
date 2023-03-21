from typing import Any

from django.forms.widgets import Textarea as Textarea

geo_context: Any
logger: Any

class OpenLayersWidget(Textarea):
    def get_context(self, name: Any, value: Any, attrs: Any) -> Any: ...
    def map_options(self) -> Any: ...
