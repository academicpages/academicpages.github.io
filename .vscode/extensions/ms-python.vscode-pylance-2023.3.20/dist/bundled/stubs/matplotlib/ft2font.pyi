# Python: 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)]
# Library: matplotlib, version: 3.4.0
# Module: matplotlib.ft2font, version: unspecified
import typing
import builtins as _mod_builtins

BOLD: int
EXTERNAL_STREAM: int
FAST_GLYPHS: int
FIXED_SIZES: int
FIXED_WIDTH: int
class FT2Font(_mod_builtins.object):
    'Create a new FT2Font object.\n\nAttributes\n----------\nnum_faces\n    Number of faces in file.\nface_flags, style_flags : int\n    Face and style flags; see the ft2font constants.\nnum_glyphs\n    Number of glyphs in the face.\nfamily_name, style_name\n    Face family and style name.\nnum_fixed_sizes\n    Number of bitmap in the face.\nscalable\n    Whether face is scalable; attributes after this one are only\n    defined for scalable faces.\nbbox\n    Face global bounding box (xmin, ymin, xmax, ymax).\nunits_per_EM\n    Number of font units covered by the EM.\nascender, descender\n    Ascender and descender in 26.6 units.\nheight\n    Height in 26.6 units; used to compute a default line spacing\n    (baseline-to-baseline distance).\nmax_advance_width, max_advance_height\n    Maximum horizontal and vertical cursor advance for all glyphs.\nunderline_position, underline_thickness\n    Vertical position and thickness of the underline bar.\npostscript_name\n    PostScript name of the font.\n'
    def __init__(self, *args, **kwargs) -> None:
        'Create a new FT2Font object.\n\nAttributes\n----------\nnum_faces\n    Number of faces in file.\nface_flags, style_flags : int\n    Face and style flags; see the ft2font constants.\nnum_glyphs\n    Number of glyphs in the face.\nfamily_name, style_name\n    Face family and style name.\nnum_fixed_sizes\n    Number of bitmap in the face.\nscalable\n    Whether face is scalable; attributes after this one are only\n    defined for scalable faces.\nbbox\n    Face global bounding box (xmin, ymin, xmax, ymax).\nunits_per_EM\n    Number of font units covered by the EM.\nascender, descender\n    Ascender and descender in 26.6 units.\nheight\n    Height in 26.6 units; used to compute a default line spacing\n    (baseline-to-baseline distance).\nmax_advance_width, max_advance_height\n    Maximum horizontal and vertical cursor advance for all glyphs.\nunderline_position, underline_thickness\n    Vertical position and thickness of the underline bar.\npostscript_name\n    PostScript name of the font.\n'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def ascender(self) -> typing.Any:
        ...
    
    @property
    def bbox(self) -> typing.Any:
        ...
    
    def clear(self) -> typing.Any:
        'Clear all the glyphs, reset for a new call to `.set_text`.\n'
        ...
    
    @property
    def descender(self) -> typing.Any:
        ...
    
    def draw_glyph_to_bitmap(self, bitmap, x, y, glyph) -> typing.Any:
        'Draw a single glyph to the bitmap at pixel locations x, y\nNote it is your responsibility to set up the bitmap manually\nwith ``set_bitmap_size(w, h)`` before this call is made.\n\nIf you want automatic layout, use `.set_text` in combinations with\n`.draw_glyphs_to_bitmap`.  This function is instead intended for people\nwho want to render individual glyphs (e.g., returned by `.load_char`)\nat precise locations.\n'
        ...
    
    def draw_glyphs_to_bitmap(self) -> typing.Any:
        'Draw the glyphs that were loaded by `.set_text` to the bitmap.\nThe bitmap size will be automatically set to include the glyphs.\n'
        ...
    
    @property
    def face_flags(self) -> typing.Any:
        ...
    
    @property
    def family_name(self) -> typing.Any:
        ...
    
    @property
    def fname(self) -> typing.Any:
        ...
    
    def get_bitmap_offset(self) -> typing.Any:
        'Get the (x, y) offset in 26.6 subpixels for the bitmap if ink hangs left or below (0, 0).\nSince Matplotlib only supports left-to-right text, y is always 0.\n'
        ...
    
    def get_char_index(self, codepoint) -> typing.Any:
        'Return the glyph index corresponding to a character *codepoint*.\n'
        ...
    
    def get_charmap(self) -> typing.Any:
        'Return a dict that maps the character codes of the selected charmap\n(Unicode by default) to their corresponding glyph indices.\n'
        ...
    
    def get_descent(self) -> typing.Any:
        'Get the descent in 26.6 subpixels of the current string set by `.set_text`.\nThe rotation of the string is accounted for.  To get the descent\nin pixels, divide this value by 64.\n'
        ...
    
    def get_glyph_name(self, index) -> typing.Any:
        "Retrieve the ASCII name of a given glyph *index* in a face.\n\nDue to Matplotlib's internal design, for fonts that do not contain glyph\nnames (per FT_FACE_FLAG_GLYPH_NAMES), this returns a made-up name which\ndoes *not* roundtrip through `.get_name_index`.\n"
        ...
    
    def get_image(self) -> typing.Any:
        'Return the underlying image buffer for this font object.\n'
        ...
    
    def get_kerning(self, left, right, mode) -> typing.Any:
        'Get the kerning between *left* and *right* glyph indices.\n*mode* is a kerning mode constant:\n  KERNING_DEFAULT  - Return scaled and grid-fitted kerning distances\n  KERNING_UNFITTED - Return scaled but un-grid-fitted kerning distances\n  KERNING_UNSCALED - Return the kerning vector in original font units\n'
        ...
    
    def get_name_index(self, name) -> typing.Any:
        "Return the glyph index of a given glyph *name*.\nThe glyph index 0 means 'undefined character code'.\n"
        ...
    
    def get_num_glyphs(self) -> typing.Any:
        'Return the number of loaded glyphs.\n'
        ...
    
    def get_path(self) -> typing.Any:
        'Get the path data from the currently loaded glyph as a tuple of vertices, codes.\n'
        ...
    
    def get_ps_font_info(self) -> typing.Any:
        'Return the information in the PS Font Info structure.\n'
        ...
    
    def get_sfnt(self) -> typing.Any:
        'Load the entire SFNT names table, as a dict whose keys are\n(platform-ID, ISO-encoding-scheme, language-code, and description)\ntuples.\n'
        ...
    
    def get_sfnt_table(self, name) -> typing.Any:
        'Return one of the following SFNT tables: head, maxp, OS/2, hhea, vhea, post, or pclt.\n'
        ...
    
    def get_width_height(self) -> typing.Any:
        'Get the width and height in 26.6 subpixels of the current string set by `.set_text`.\nThe rotation of the string is accounted for.  To get width and height\nin pixels, divide these values by 64.\n'
        ...
    
    def get_xys(self) -> typing.Any:
        'Get the xy locations of the current glyphs.\n'
        ...
    
    @property
    def height(self) -> typing.Any:
        ...
    
    def load_char(self, charcode, flags) -> typing.Any:
        'Load character with *charcode* in current fontfile and set glyph.\n*flags* can be a bitwise-or of the LOAD_XXX constants;\nthe default value is LOAD_FORCE_AUTOHINT.\nReturn value is a Glyph object, with attributes\n  width          # glyph width\n  height         # glyph height\n  bbox           # the glyph bbox (xmin, ymin, xmax, ymax)\n  horiBearingX   # left side bearing in horizontal layouts\n  horiBearingY   # top side bearing in horizontal layouts\n  horiAdvance    # advance width for horizontal layout\n  vertBearingX   # left side bearing in vertical layouts\n  vertBearingY   # top side bearing in vertical layouts\n  vertAdvance    # advance height for vertical layout\n'
        ...
    
    def load_glyph(self, glyphindex, flags) -> typing.Any:
        'Load character with *glyphindex* in current fontfile and set glyph.\n*flags* can be a bitwise-or of the LOAD_XXX constants;\nthe default value is LOAD_FORCE_AUTOHINT.\nReturn value is a Glyph object, with attributes\n  width          # glyph width\n  height         # glyph height\n  bbox           # the glyph bbox (xmin, ymin, xmax, ymax)\n  horiBearingX   # left side bearing in horizontal layouts\n  horiBearingY   # top side bearing in horizontal layouts\n  horiAdvance    # advance width for horizontal layout\n  vertBearingX   # left side bearing in vertical layouts\n  vertBearingY   # top side bearing in vertical layouts\n  vertAdvance    # advance height for vertical layout\n'
        ...
    
    @property
    def max_advance_height(self) -> typing.Any:
        ...
    
    @property
    def max_advance_width(self) -> typing.Any:
        ...
    
    @property
    def num_charmaps(self) -> typing.Any:
        ...
    
    @property
    def num_faces(self) -> typing.Any:
        ...
    
    @property
    def num_fixed_sizes(self) -> typing.Any:
        ...
    
    @property
    def num_glyphs(self) -> typing.Any:
        ...
    
    @property
    def postscript_name(self) -> typing.Any:
        ...
    
    @property
    def scalable(self) -> typing.Any:
        ...
    
    def select_charmap(self, i) -> typing.Any:
        'Select a charmap by its FT_Encoding number.\n'
        ...
    
    def set_charmap(self, i) -> typing.Any:
        'Make the i-th charmap current.\n'
        ...
    
    def set_size(self, ptsize, dpi) -> typing.Any:
        'Set the point size and dpi of the text.\n'
        ...
    
    def set_text(self, string, angle, flags) -> typing.Any:
        'Set the text *string* and *angle*.\n*flags* can be a bitwise-or of the LOAD_XXX constants;\nthe default value is LOAD_FORCE_AUTOHINT.\nYou must call this before `.draw_glyphs_to_bitmap`.\nA sequence of x,y positions is returned.\n'
        ...
    
    @property
    def style_flags(self) -> typing.Any:
        ...
    
    @property
    def style_name(self) -> typing.Any:
        ...
    
    @property
    def underline_position(self) -> typing.Any:
        ...
    
    @property
    def underline_thickness(self) -> typing.Any:
        ...
    
    @property
    def units_per_EM(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class FT2Image(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def draw_rect(self, x0, y0, x1, y1) -> typing.Any:
        'Draw an empty rectangle to the image.\n'
        ...
    
    def draw_rect_filled(self, x0, y0, x1, y1) -> typing.Any:
        'Draw a filled rectangle to the image.\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

GLYPH_NAMES: int
HORIZONTAL: int
ITALIC: int
KERNING: int
KERNING_DEFAULT: int
KERNING_UNFITTED: int
KERNING_UNSCALED: int
LOAD_CROP_BITMAP: int
LOAD_DEFAULT: int
LOAD_FORCE_AUTOHINT: int
LOAD_IGNORE_GLOBAL_ADVANCE_WIDTH: int
LOAD_IGNORE_TRANSFORM: int
LOAD_LINEAR_DESIGN: int
LOAD_MONOCHROME: int
LOAD_NO_AUTOHINT: int
LOAD_NO_BITMAP: int
LOAD_NO_HINTING: int
LOAD_NO_RECURSE: int
LOAD_NO_SCALE: int
LOAD_PEDANTIC: int
LOAD_RENDER: int
LOAD_TARGET_LCD: int
LOAD_TARGET_LCD_V: int
LOAD_TARGET_LIGHT: int
LOAD_TARGET_MONO: int
LOAD_TARGET_NORMAL: int
LOAD_VERTICAL_LAYOUT: int
MULTIPLE_MASTERS: int
SCALABLE: int
SFNT: int
VERTICAL: int
__doc__: typing.Any
__file__: str
__freetype_build_type__: str
__freetype_version__: str
__name__: str
__package__: str
def __getattr__(name) -> typing.Any:
    ...

