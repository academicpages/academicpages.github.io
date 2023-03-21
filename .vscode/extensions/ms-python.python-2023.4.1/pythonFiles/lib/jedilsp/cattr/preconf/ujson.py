"""Preconfigured converters for ujson."""
from cattrs.preconf.ujson import configure_converter, make_converter, UjsonConverter

__all__ = ["configure_converter", "make_converter", UjsonConverter]
