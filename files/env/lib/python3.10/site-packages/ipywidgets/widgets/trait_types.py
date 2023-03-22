# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

"""
Trait types for html widgets.
"""

import re
import traitlets
import datetime as dt

from .util import string_types


_color_names = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred ', 'indigo ', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'transparent', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

# Regex colors #fff and #ffffff
_color_hex_re = re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$')
# Regex colors #ffff and #ffffffff (includes alpha value)
_color_hexa_re = re.compile(r'^#[a-fA-F0-9]{4}(?:[a-fA-F0-9]{4})?$')

# Helpers (float percent, int percent with optional surrounding whitespace)
_color_frac_percent = r'\s*(\d+(\.\d*)?|\.\d+)?%?\s*'
_color_int_percent = r'\s*\d+%?\s*'

# rgb(), rgba(), hsl() and hsla() format strings
_color_rgb = r'rgb\({ip},{ip},{ip}\)'
_color_rgba = r'rgba\({ip},{ip},{ip},{fp}\)'
_color_hsl = r'hsl\({fp},{fp},{fp}\)'
_color_hsla = r'hsla\({fp},{fp},{fp},{fp}\)'

# Regex colors rgb/rgba/hsl/hsla
_color_rgbhsl_re = re.compile('({0})|({1})|({2})|({3})'.format(
    _color_rgb, _color_rgba, _color_hsl, _color_hsla
).format(ip=_color_int_percent, fp=_color_frac_percent))


class Color(traitlets.Unicode):
    """A string holding a valid HTML color such as 'blue', '#060482', '#A80'"""

    info_text = 'a valid HTML color'
    default_value = traitlets.Undefined

    def validate(self, obj, value):
        if value is None and self.allow_none:
            return value
        if isinstance(value, string_types):
            if (value.lower() in _color_names or _color_hex_re.match(value) or
                _color_hexa_re.match(value) or _color_rgbhsl_re.match(value)):
                return value

        self.error(obj, value)


class Datetime(traitlets.TraitType):
    """A trait type holding a Python datetime object"""

    klass = dt.datetime
    default_value = dt.datetime(1900, 1, 1)


class Date(traitlets.TraitType):
    """A trait type holding a Python date object"""

    klass = dt.date
    default_value = dt.date(1900, 1, 1)


def datetime_to_json(pydt, manager):
    """Serialize a Python datetime object to json.

    Instantiating a JavaScript Date object with a string assumes that the
    string is a UTC string, while instantiating it with constructor arguments
    assumes that it's in local time:

    >>> cdate = new Date('2015-05-12')
    Mon May 11 2015 20:00:00 GMT-0400 (Eastern Daylight Time)
    >>> cdate = new Date(2015, 4, 12) // Months are 0-based indices in JS
    Tue May 12 2015 00:00:00 GMT-0400 (Eastern Daylight Time)

    Attributes of this dictionary are to be passed to the JavaScript Date
    constructor.
    """
    if pydt is None:
        return None
    else:
        return dict(
            year=pydt.year,
            month=pydt.month - 1,  # Months are 0-based indices in JS
            date=pydt.day,
            hours=pydt.hour,       # Hours, Minutes, Seconds and Milliseconds
            minutes=pydt.minute,   # are plural in JS
            seconds=pydt.second,
            milliseconds=pydt.microsecond / 1000
        )


def datetime_from_json(js, manager):
    """Deserialize a Python datetime object from json."""
    if js is None:
        return None
    else:
        return dt.datetime(
            js['year'],
            js['month'] + 1,  # Months are 1-based in Python
            js['date'],
            js['hours'],
            js['minutes'],
            js['seconds'],
            js['milliseconds'] * 1000
        )

datetime_serialization = {
    'from_json': datetime_from_json,
    'to_json': datetime_to_json
}


def date_to_json(pydate, manager):
    """Serialize a Python date object.

    Attributes of this dictionary are to be passed to the JavaScript Date
    constructor.
    """
    if pydate is None:
        return None
    else:
        return dict(
            year=pydate.year,
            month=pydate.month - 1,  # Months are 0-based indices in JS
            date=pydate.day
        )


def date_from_json(js, manager):
    """Deserialize a Javascript date."""
    if js is None:
        return None
    else:
        return dt.date(
            js['year'],
            js['month'] + 1,  # Months are 1-based in Python
            js['date'],
        )

date_serialization = {
    'from_json': date_from_json,
    'to_json': date_to_json
}


class InstanceDict(traitlets.Instance):
    """An instance trait which coerces a dict to an instance.

    This lets the instance be specified as a dict, which is used
    to initialize the instance.

    Also, we default to a trivial instance, even if args and kwargs
    is not specified."""

    def validate(self, obj, value):
        if isinstance(value, dict):
            return super(InstanceDict, self).validate(obj, self.klass(**value))
        else:
            return super(InstanceDict, self).validate(obj, value)

    def make_dynamic_default(self):
        return self.klass(*(self.default_args or ()),
                          **(self.default_kwargs or {}))


# The regexp is taken
# from https://github.com/d3/d3-format/blob/master/src/formatSpecifier.js
_number_format_re = re.compile(r'^(?:(.)?([<>=^]))?([+\-\( ])?([$#])?(0)?(\d+)?(,)?(\.\d+)?([a-z%])?$', re.I)

# The valid types are taken from
# https://github.com/d3/d3-format/blob/master/src/formatTypes.js
_number_format_types = {
    'e', 'f', 'g', 'r', 's', '%', 'p', 'b', 'o', 'd', 'x',
    'X', 'c', ''
}


class NumberFormat(traitlets.Unicode):
    """A string holding a number format specifier, e.g. '.3f'

    This traitlet holds a string that can be passed to the
    `d3-format <https://github.com/d3/d3-format>`_ JavaScript library.
    The format allowed is similar to the Python format specifier (PEP 3101).
    """
    info_text = 'a valid number format'
    default_value = traitlets.Undefined

    def validate(self, obj, value):
        value = super(NumberFormat, self).validate(obj, value)
        re_match = _number_format_re.match(value)
        if re_match is None:
            self.error(obj, value)
        else:
            format_type = re_match.group(9)
            if format_type is None:
                return value
            elif format_type in _number_format_types:
                return value
            else:
                raise traitlets.TraitError(
                    'The type specifier of a NumberFormat trait must '
                    'be one of {}, but a value of \'{}\' was '
                    'specified.'.format(
                        list(_number_format_types), format_type)
                )

class TypedTuple(traitlets.Container):
    """A trait for a tuple of any length with type-checked elements."""
    klass = tuple
    _cast_types = (list,)


def bytes_from_json(js, obj):
    return None if js is None else js.tobytes()

bytes_serialization = {
    'from_json': bytes_from_json,
}
