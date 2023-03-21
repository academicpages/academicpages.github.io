from collections import OrderedDict
from typing import Any, Callable, Dict, Optional, Type, Union

from django.contrib.sitemaps import GenericSitemap, Sitemap
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

def x_robots_tag(func: Callable[..., Any]) -> Callable[..., Any]: ...
def index(
    request: HttpRequest,
    sitemaps: Dict[str, Union[Type[Sitemap], Sitemap]],
    template_name: str = ...,
    content_type: str = ...,
    sitemap_url_name: str = ...,
) -> TemplateResponse: ...
def sitemap(
    request: HttpRequest,
    sitemaps: Union[
        Dict[str, Type[Sitemap]], Dict[str, GenericSitemap], OrderedDict[Any, Any]
    ],
    section: Optional[str] = ...,
    template_name: str = ...,
    content_type: str = ...,
) -> TemplateResponse: ...
