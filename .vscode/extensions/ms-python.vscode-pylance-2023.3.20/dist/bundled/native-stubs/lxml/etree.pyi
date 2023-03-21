# Python: 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Library: lxml, version: 4.6.1
# Module: lxml.etree, version: 4.6.1
import typing
import builtins as _mod_builtins

class _MemDebug(_mod_builtins.object):
    'Debugging support for the memory allocation in libxml2.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Debugging support for the memory allocation in libxml2.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def blocks_used(self) -> typing.Any:
        'blocks_used(self)\n\n        Returns the total number of memory blocks currently allocated by libxml2.\n        Note that libxml2 constrains this value to a C int, which limits\n        the accuracy on 64 bit systems.\n        '
        ...
    
    def bytes_used(self) -> typing.Any:
        'bytes_used(self)\n\n        Returns the total amount of memory (in bytes) currently used by libxml2.\n        Note that libxml2 constrains this value to a C int, which limits\n        the accuracy on 64 bit systems.\n        '
        ...
    
    def dict_size(self) -> typing.Any:
        'dict_size(self)\n\n        Returns the current size of the global name dictionary used by libxml2\n        for the current thread.  Each thread has its own dictionary.\n        '
        ...
    
    def dump(self, output_file, byte_count) -> typing.Any:
        'dump(self, output_file=None, byte_count=None)\n\n        Dumps the current memory blocks allocated by libxml2 to a file.\n\n        The optional parameter \'output_file\' specifies the file path.  It defaults\n        to the file ".memorylist" in the current directory.\n\n        The optional parameter \'byte_count\' limits the number of bytes in the dump.\n        Note that this parameter is ignored when lxml is compiled against a libxml2\n        version before 2.7.0.\n        '
        ...
    
    def show(self, output_file, block_count) -> typing.Any:
        'show(self, output_file=None, block_count=None)\n\n        Dumps the current memory blocks allocated by libxml2 to a file.\n        The output file format is suitable for line diffing.\n\n        The optional parameter \'output_file\' specifies the file path.  It defaults\n        to the file ".memorydump" in the current directory.\n\n        The optional parameter \'block_count\' limits the number of blocks\n        in the dump.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class AncestorsIterator(_ElementMatchIterator):
    'AncestorsIterator(self, node, tag=None)\n    Iterates over the ancestors of an element (from parent to parent).\n    '
    def __init__(self, node, tag=...) -> None:
        'AncestorsIterator(self, node, tag=None)\n    Iterates over the ancestors of an element (from parent to parent).\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class AttributeBasedElementClassLookup(FallbackElementClassLookup):
    "AttributeBasedElementClassLookup(self, attribute_name, class_mapping, fallback=None)\n    Checks an attribute of an Element and looks up the value in a\n    class dictionary.\n\n    Arguments:\n      - attribute name - '{ns}name' style string\n      - class mapping  - Python dict mapping attribute values to Element classes\n      - fallback       - optional fallback lookup mechanism\n\n    A None key in the class mapping will be checked if the attribute is\n    missing.\n    "
    def __init__(self, attribute_name, class_mapping, fallback=...) -> None:
        "AttributeBasedElementClassLookup(self, attribute_name, class_mapping, fallback=None)\n    Checks an attribute of an Element and looks up the value in a\n    class dictionary.\n\n    Arguments:\n      - attribute name - '{ns}name' style string\n      - class mapping  - Python dict mapping attribute values to Element classes\n      - fallback       - optional fallback lookup mechanism\n\n    A None key in the class mapping will be checked if the attribute is\n    missing.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class C14NError(LxmlError):
    'Error during C14N serialisation.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error during C14N serialisation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class C14NWriterTarget(_mod_builtins.object):
    '\n    Canonicalization writer target for the XMLParser.\n\n    Serialises parse events to XML C14N 2.0.\n\n    Configuration options:\n\n    - *with_comments*: set to true to include comments\n    - *strip_text*: set to true to strip whitespace before and after text content\n    - *rewrite_prefixes*: set to true to replace namespace prefixes by "n{number}"\n    - *qname_aware_tags*: a set of qname aware tag names in which prefixes\n                          should be replaced in text content\n    - *qname_aware_attrs*: a set of qname aware attribute names in which prefixes\n                           should be replaced in text content\n    - *exclude_attrs*: a set of attribute names that should not be serialised\n    - *exclude_tags*: a set of tag names that should not be serialised\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Canonicalization writer target for the XMLParser.\n\n    Serialises parse events to XML C14N 2.0.\n\n    Configuration options:\n\n    - *with_comments*: set to true to include comments\n    - *strip_text*: set to true to strip whitespace before and after text content\n    - *rewrite_prefixes*: set to true to replace namespace prefixes by "n{number}"\n    - *qname_aware_tags*: a set of qname aware tag names in which prefixes\n                          should be replaced in text content\n    - *qname_aware_attrs*: a set of qname aware attribute names in which prefixes\n                           should be replaced in text content\n    - *exclude_attrs*: a set of attribute names that should not be serialised\n    - *exclude_tags*: a set of tag names that should not be serialised\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _iter_namespaces(self, ns_stack) -> typing.Any:
        ...
    
    def close(self) -> typing.Any:
        ...
    
    def comment(self, text) -> typing.Any:
        ...
    
    def data(self, data) -> typing.Any:
        ...
    
    def end(self, tag) -> typing.Any:
        ...
    
    def pi(self, target, data) -> typing.Any:
        ...
    
    def start(self, tag, attrs) -> typing.Any:
        ...
    
    def start_ns(self, prefix, uri) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CDATA(_mod_builtins.object):
    'CDATA(data)\n\n    CDATA factory.  This factory creates an opaque data object that\n    can be used to set Element text.  The usual way to use it is::\n\n        >>> el = Element(\'content\')\n        >>> el.text = CDATA(\'a string\')\n\n        >>> print(el.text)\n        a string\n        >>> print(tostring(el, encoding="unicode"))\n        <content><![CDATA[a string]]></content>\n    '
    def __init__(self, data) -> None:
        'CDATA(data)\n\n    CDATA factory.  This factory creates an opaque data object that\n    can be used to set Element text.  The usual way to use it is::\n\n        >>> el = Element(\'content\')\n        >>> el.text = CDATA(\'a string\')\n\n        >>> print(el.text)\n        a string\n        >>> print(tostring(el, encoding="unicode"))\n        <content><![CDATA[a string]]></content>\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def Comment(text) -> typing.Any:
    'Comment(text=None)\n\n    Comment element factory. This factory function creates a special element that will\n    be serialized as an XML comment.\n    '
    ...

class CommentBase(_Comment):
    'All custom Comment classes must inherit from this one.\n\n    To create an XML Comment instance, use the ``Comment()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Comments must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'All custom Comment classes must inherit from this one.\n\n    To create an XML Comment instance, use the ``Comment()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Comments must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class CustomElementClassLookup(FallbackElementClassLookup):
    "CustomElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    You can inherit from this class and override the method::\n\n        lookup(self, type, doc, namespace, name)\n\n    to lookup the element class for a node. Arguments of the method:\n    * type:      one of 'element', 'comment', 'PI', 'entity'\n    * doc:       document that the node is in\n    * namespace: namespace URI of the node (or None for comments/PIs/entities)\n    * name:      name of the element/entity, None for comments, target for PIs\n\n    If you return None from this method, the fallback will be called.\n    "
    def __init__(self, fallback=...) -> None:
        "CustomElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    You can inherit from this class and override the method::\n\n        lookup(self, type, doc, namespace, name)\n\n    to lookup the element class for a node. Arguments of the method:\n    * type:      one of 'element', 'comment', 'PI', 'entity'\n    * doc:       document that the node is in\n    * namespace: namespace URI of the node (or None for comments/PIs/entities)\n    * name:      name of the element/entity, None for comments, target for PIs\n\n    If you return None from this method, the fallback will be called.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def lookup(self, type, doc, namespace, name) -> typing.Any:
        'lookup(self, type, doc, namespace, name)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

DEBUG: int
class DTD(_Validator):
    'DTD(self, file=None, external_id=None)\n    A DTD validator.\n\n    Can load from filesystem directly given a filename or file-like object.\n    Alternatively, pass the keyword parameter ``external_id`` to load from a\n    catalog.\n    '
    def __call__(self, etree) -> typing.Any:
        '__call__(self, etree)\n\n        Validate doc using the DTD.\n\n        Returns true if the document is valid, false if not.\n        '
        ...
    
    def __init__(self, file=..., external_id=...) -> None:
        'DTD(self, file=None, external_id=None)\n    A DTD validator.\n\n    Can load from filesystem directly given a filename or file-like object.\n    Alternatively, pass the keyword parameter ``external_id`` to load from a\n    catalog.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def elements(self) -> typing.Any:
        ...
    
    def entities(self) -> typing.Any:
        ...
    
    @property
    def external_id(self) -> typing.Any:
        ...
    
    def iterelements(self) -> typing.Any:
        ...
    
    def iterentities(self) -> typing.Any:
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def system_url(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DTDError(LxmlError):
    'Base class for DTD errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class for DTD errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DTDParseError(DTDError):
    'Error while parsing a DTD.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while parsing a DTD.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DTDValidateError(DTDError):
    'Error while validating an XML document with a DTD.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while validating an XML document with a DTD.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DocInfo(_mod_builtins.object):
    'Document information provided by parser and DTD.'
    @property
    def URL(self) -> typing.Any:
        'The source URL of the document (or None if unknown).'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        'Document information provided by parser and DTD.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def clear(self) -> typing.Any:
        'Removes DOCTYPE and internal subset from the document.'
        ...
    
    @property
    def doctype(self) -> typing.Any:
        'Returns a DOCTYPE declaration string for the document.'
        ...
    
    @property
    def encoding(self) -> typing.Any:
        'Returns the encoding name as declared by the document.'
        ...
    
    @property
    def externalDTD(self) -> typing.Any:
        'Returns a DTD validator based on the external subset of the document.'
        ...
    
    @property
    def internalDTD(self) -> typing.Any:
        'Returns a DTD validator based on the internal subset of the document.'
        ...
    
    @property
    def public_id(self) -> typing.Any:
        'Public ID of the DOCTYPE.\n\n        Mutable.  May be set to a valid string or None.  If a DTD does not\n        exist, setting this variable (even to None) will create one.\n        '
        ...
    
    @property
    def root_name(self) -> typing.Any:
        'Returns the name of the root node as defined by the DOCTYPE.'
        ...
    
    @property
    def standalone(self) -> typing.Any:
        "Returns the standalone flag as declared by the document.  The possible\n        values are True (``standalone='yes'``), False\n        (``standalone='no'`` or flag not provided in the declaration),\n        and None (unknown or no declaration found).  Note that a\n        normal truth test on this value will always tell if the\n        ``standalone`` flag was set to ``'yes'`` or not.\n        "
        ...
    
    @property
    def system_url(self) -> typing.Any:
        'System ID of the DOCTYPE.\n\n        Mutable.  May be set to a valid string or None.  If a DTD does not\n        exist, setting this variable (even to None) will create one.\n        '
        ...
    
    @property
    def xml_version(self) -> typing.Any:
        'Returns the XML version as declared by the document.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class DocumentInvalid(LxmlError):
    'Validation error.\n\n    Raised by all document validators when their ``assertValid(tree)``\n    method fails.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Validation error.\n\n    Raised by all document validators when their ``assertValid(tree)``\n    method fails.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ETCompatXMLParser(XMLParser):
    'ETCompatXMLParser(self, encoding=None, attribute_defaults=False,                  dtd_validation=False, load_dtd=False, no_network=True,                  ns_clean=False, recover=False, schema=None,                  huge_tree=False, remove_blank_text=False, resolve_entities=True,                  remove_comments=True, remove_pis=True, strip_cdata=True,                  target=None, compact=True)\n\n    An XML parser with an ElementTree compatible default setup.\n\n    See the XMLParser class for details.\n\n    This parser has ``remove_comments`` and ``remove_pis`` enabled by default\n    and thus ignores comments and processing instructions.\n    '
    def __init__(self, encoding=..., attribute_defaults=..., dtd_validation=..., load_dtd=..., no_network=..., ns_clean=..., recover=..., schema=..., huge_tree=..., remove_blank_text=..., resolve_entities=..., remove_comments=..., remove_pis=..., strip_cdata=..., target=..., compact=...) -> None:
        'ETCompatXMLParser(self, encoding=None, attribute_defaults=False,                  dtd_validation=False, load_dtd=False, no_network=True,                  ns_clean=False, recover=False, schema=None,                  huge_tree=False, remove_blank_text=False, resolve_entities=True,                  remove_comments=True, remove_pis=True, strip_cdata=True,                  target=None, compact=True)\n\n    An XML parser with an ElementTree compatible default setup.\n\n    See the XMLParser class for details.\n\n    This parser has ``remove_comments`` and ``remove_pis`` enabled by default\n    and thus ignores comments and processing instructions.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ETXPath(XPath):
    'ETXPath(self, path, extensions=None, regexp=True, smart_strings=True)\n    Special XPath class that supports the ElementTree {uri} notation for namespaces.\n\n    Note that this class does not accept the ``namespace`` keyword\n    argument. All namespaces must be passed as part of the path\n    string.  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    '
    def __init__(self, path, extensions=..., regexp=..., smart_strings=...) -> None:
        'ETXPath(self, path, extensions=None, regexp=True, smart_strings=True)\n    Special XPath class that supports the ElementTree {uri} notation for namespaces.\n\n    Note that this class does not accept the ``namespace`` keyword\n    argument. All namespaces must be passed as part of the path\n    string.  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def Element(_tag, attrib, nsmap, **_extra) -> typing.Any:
    'Element(_tag, attrib=None, nsmap=None, **_extra)\n\n    Element factory.  This function returns an object implementing the\n    Element interface.\n\n    Also look at the `_Element.makeelement()` and\n    `_BaseParser.makeelement()` methods, which provide a faster way to\n    create an Element within a specific document or parser context.\n    '
    ...

class ElementBase(_Element):
    'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n\n    The public Element class.  All custom Element classes must inherit\n    from this one.  To create an Element, use the `Element()` factory.\n\n    BIG FAT WARNING: Subclasses *must not* override __init__ or\n    __new__ as it is absolutely undefined when these objects will be\n    created or destroyed.  All persistent state of Elements must be\n    stored in the underlying XML.  If you really need to initialize\n    the object after creation, you can implement an ``_init(self)``\n    method that will be called directly after object creation.\n\n    Subclasses of this class can be instantiated to create a new\n    Element.  By default, the tag name will be the class name and the\n    namespace will be empty.  You can modify this with the following\n    class attributes:\n\n    * TAG - the tag name, possibly containing a namespace in Clark\n      notation\n\n    * NAMESPACE - the default namespace URI, unless provided as part\n      of the TAG attribute.\n\n    * HTML - flag if the class is an HTML tag, as opposed to an XML\n      tag.  This only applies to un-namespaced tags and defaults to\n      false (i.e. XML).\n\n    * PARSER - the parser that provides the configuration for the\n      newly created document.  Providing an HTML parser here will\n      default to creating an HTML element.\n\n    In user code, the latter three are commonly inherited in class\n    hierarchies that implement a common namespace.\n    '
    def __init__(self, *children, attrib=..., nsmap=..., **_extra) -> None:
        'ElementBase(*children, attrib=None, nsmap=None, **_extra)\n        '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementChildIterator(_ElementMatchIterator):
    'ElementChildIterator(self, node, tag=None, reversed=False)\n    Iterates over the children of an element.\n    '
    def __init__(self, node, tag=..., reversed=...) -> None:
        'ElementChildIterator(self, node, tag=None, reversed=False)\n    Iterates over the children of an element.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementClassLookup(_mod_builtins.object):
    'ElementClassLookup(self)\n    Superclass of Element class lookups.\n    '
    def __init__(self) -> None:
        'ElementClassLookup(self)\n    Superclass of Element class lookups.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementDefaultClassLookup(ElementClassLookup):
    'ElementDefaultClassLookup(self, element=None, comment=None, pi=None, entity=None)\n    Element class lookup scheme that always returns the default Element\n    class.\n\n    The keyword arguments ``element``, ``comment``, ``pi`` and ``entity``\n    accept the respective Element classes.\n    '
    def __init__(self, element=..., comment=..., pi=..., entity=...) -> None:
        'ElementDefaultClassLookup(self, element=None, comment=None, pi=None, entity=None)\n    Element class lookup scheme that always returns the default Element\n    class.\n\n    The keyword arguments ``element``, ``comment``, ``pi`` and ``entity``\n    accept the respective Element classes.\n    '
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
    def comment_class(self) -> typing.Any:
        ...
    
    @property
    def element_class(self) -> typing.Any:
        ...
    
    @property
    def entity_class(self) -> typing.Any:
        ...
    
    @property
    def pi_class(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementDepthFirstIterator(_mod_builtins.object):
    "ElementDepthFirstIterator(self, node, tag=None, inclusive=True)\n    Iterates over an element and its sub-elements in document order (depth\n    first pre-order).\n\n    Note that this also includes comments, entities and processing\n    instructions.  To filter them out, check if the ``tag`` property\n    of the returned element is a string (i.e. not None and not a\n    factory function), or pass the ``Element`` factory for the ``tag``\n    argument to receive only Elements.\n\n    If the optional ``tag`` argument is not None, the iterator returns only\n    the elements that match the respective name and namespace.\n\n    The optional boolean argument 'inclusive' defaults to True and can be set\n    to False to exclude the start element itself.\n\n    Note that the behaviour of this iterator is completely undefined if the\n    tree it traverses is modified during iteration.\n    "
    def __init__(self, node, tag=..., inclusive=...) -> None:
        "ElementDepthFirstIterator(self, node, tag=None, inclusive=True)\n    Iterates over an element and its sub-elements in document order (depth\n    first pre-order).\n\n    Note that this also includes comments, entities and processing\n    instructions.  To filter them out, check if the ``tag`` property\n    of the returned element is a string (i.e. not None and not a\n    factory function), or pass the ``Element`` factory for the ``tag``\n    argument to receive only Elements.\n\n    If the optional ``tag`` argument is not None, the iterator returns only\n    the elements that match the respective name and namespace.\n\n    The optional boolean argument 'inclusive' defaults to True and can be set\n    to False to exclude the start element itself.\n\n    Note that the behaviour of this iterator is completely undefined if the\n    tree it traverses is modified during iteration.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> ElementDepthFirstIterator:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementNamespaceClassLookup(FallbackElementClassLookup):
    'ElementNamespaceClassLookup(self, fallback=None)\n\n    Element class lookup scheme that searches the Element class in the\n    Namespace registry.\n\n    Usage:\n\n    >>> lookup = ElementNamespaceClassLookup()\n    >>> ns_elements = lookup.get_namespace("http://schema.org/Movie")\n\n    >>> @ns_elements\n    ... class movie(ElementBase):\n    ...     "Element implementation for \'movie\' tag (using class name) in schema namespace."\n\n    >>> @ns_elements("movie")\n    ... class MovieElement(ElementBase):\n    ...     "Element implementation for \'movie\' tag (explicit tag name) in schema namespace."\n    '
    def __init__(self, fallback=...) -> None:
        'ElementNamespaceClassLookup(self, fallback=None)\n\n    Element class lookup scheme that searches the Element class in the\n    Namespace registry.\n\n    Usage:\n\n    >>> lookup = ElementNamespaceClassLookup()\n    >>> ns_elements = lookup.get_namespace("http://schema.org/Movie")\n\n    >>> @ns_elements\n    ... class movie(ElementBase):\n    ...     "Element implementation for \'movie\' tag (using class name) in schema namespace."\n\n    >>> @ns_elements("movie")\n    ... class MovieElement(ElementBase):\n    ...     "Element implementation for \'movie\' tag (explicit tag name) in schema namespace."\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def get_namespace(self, ns_uri) -> typing.Any:
        'get_namespace(self, ns_uri)\n\n        Retrieve the namespace object associated with the given URI.\n        Pass None for the empty namespace.\n\n        Creates a new namespace object if it does not yet exist.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ElementTextIterator(_mod_builtins.object):
    "ElementTextIterator(self, element, tag=None, with_tail=True)\n    Iterates over the text content of a subtree.\n\n    You can pass the ``tag`` keyword argument to restrict text content to a\n    specific tag name.\n\n    You can set the ``with_tail`` keyword argument to ``False`` to skip over\n    tail text (e.g. if you know that it's only whitespace from pretty-printing).\n    "
    def __init__(self, element, tag=..., with_tail=...) -> None:
        "ElementTextIterator(self, element, tag=None, with_tail=True)\n    Iterates over the text content of a subtree.\n\n    You can pass the ``tag`` keyword argument to restrict text content to a\n    specific tag name.\n\n    You can set the ``with_tail`` keyword argument to ``False`` to skip over\n    tail text (e.g. if you know that it's only whitespace from pretty-printing).\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> ElementTextIterator:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def ElementTree(element) -> typing.Any:
    'ElementTree(element=None, file=None, parser=None)\n\n    ElementTree wrapper class.\n    '
    ...

def Entity(name) -> typing.Any:
    'Entity(name)\n\n    Entity factory.  This factory function creates a special element\n    that will be serialized as an XML entity reference or character\n    reference.  Note, however, that entities will not be automatically\n    declared in the document.  A document that uses entity references\n    requires a DTD to define the entities.\n    '
    ...

class EntityBase(_Entity):
    'All custom Entity classes must inherit from this one.\n\n    To create an XML Entity instance, use the ``Entity()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Entities must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'All custom Entity classes must inherit from this one.\n\n    To create an XML Entity instance, use the ``Entity()`` factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of Entities must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Error(_mod_builtins.Exception):
    __dict__: typing.Dict[str, typing.Any]
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ErrorDomains(_mod_builtins.object):
    'Libxml2 error domains'
    BUFFER: int
    C14N: int
    CATALOG: int
    CHECK: int
    DATATYPE: int
    DTD: int
    FTP: int
    HTML: int
    HTTP: int
    I18N: int
    IO: int
    MEMORY: int
    MODULE: int
    NAMESPACE: int
    NONE: int
    OUTPUT: int
    PARSER: int
    REGEXP: int
    RELAXNGP: int
    RELAXNGV: int
    SCHEMASP: int
    SCHEMASV: int
    SCHEMATRONV: int
    TREE: int
    URI: int
    VALID: int
    WRITER: int
    XINCLUDE: int
    XPATH: int
    XPOINTER: int
    XSLT: int
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Libxml2 error domains'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    @classmethod
    def _getName(cls, self, key, default) -> typing.Any:
        'Return the value for key if key is in the dictionary, else default.'
        ...
    
    _names: dict
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ErrorLevels(_mod_builtins.object):
    'Libxml2 error levels'
    ERROR: int
    FATAL: int
    NONE: int
    WARNING: int
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Libxml2 error levels'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    @classmethod
    def _getName(cls, self, key, default) -> typing.Any:
        'Return the value for key if key is in the dictionary, else default.'
        ...
    
    _names: dict
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ErrorTypes(_mod_builtins.object):
    'Libxml2 error types'
    BUF_OVERFLOW: int
    C14N_CREATE_CTXT: int
    C14N_CREATE_STACK: int
    C14N_INVALID_NODE: int
    C14N_RELATIVE_NAMESPACE: int
    C14N_REQUIRES_UTF8: int
    C14N_UNKNOW_NODE: int
    CATALOG_ENTRY_BROKEN: int
    CATALOG_MISSING_ATTR: int
    CATALOG_NOT_CATALOG: int
    CATALOG_PREFER_VALUE: int
    CATALOG_RECURSION: int
    CHECK_ENTITY_TYPE: int
    CHECK_FOUND_ATTRIBUTE: int
    CHECK_FOUND_CDATA: int
    CHECK_FOUND_COMMENT: int
    CHECK_FOUND_DOCTYPE: int
    CHECK_FOUND_ELEMENT: int
    CHECK_FOUND_ENTITY: int
    CHECK_FOUND_ENTITYREF: int
    CHECK_FOUND_FRAGMENT: int
    CHECK_FOUND_NOTATION: int
    CHECK_FOUND_PI: int
    CHECK_FOUND_TEXT: int
    CHECK_NAME_NOT_NULL: int
    CHECK_NOT_ATTR: int
    CHECK_NOT_ATTR_DECL: int
    CHECK_NOT_DTD: int
    CHECK_NOT_ELEM_DECL: int
    CHECK_NOT_ENTITY_DECL: int
    CHECK_NOT_NCNAME: int
    CHECK_NOT_NS_DECL: int
    CHECK_NOT_UTF8: int
    CHECK_NO_DICT: int
    CHECK_NO_DOC: int
    CHECK_NO_ELEM: int
    CHECK_NO_HREF: int
    CHECK_NO_NAME: int
    CHECK_NO_NEXT: int
    CHECK_NO_PARENT: int
    CHECK_NO_PREV: int
    CHECK_NS_ANCESTOR: int
    CHECK_NS_SCOPE: int
    CHECK_OUTSIDE_DICT: int
    CHECK_UNKNOWN_NODE: int
    CHECK_WRONG_DOC: int
    CHECK_WRONG_NAME: int
    CHECK_WRONG_NEXT: int
    CHECK_WRONG_PARENT: int
    CHECK_WRONG_PREV: int
    DTD_ATTRIBUTE_DEFAULT: int
    DTD_ATTRIBUTE_REDEFINED: int
    DTD_ATTRIBUTE_VALUE: int
    DTD_CONTENT_ERROR: int
    DTD_CONTENT_MODEL: int
    DTD_CONTENT_NOT_DETERMINIST: int
    DTD_DIFFERENT_PREFIX: int
    DTD_DUP_TOKEN: int
    DTD_ELEM_DEFAULT_NAMESPACE: int
    DTD_ELEM_NAMESPACE: int
    DTD_ELEM_REDEFINED: int
    DTD_EMPTY_NOTATION: int
    DTD_ENTITY_TYPE: int
    DTD_ID_FIXED: int
    DTD_ID_REDEFINED: int
    DTD_ID_SUBSET: int
    DTD_INVALID_CHILD: int
    DTD_INVALID_DEFAULT: int
    DTD_LOAD_ERROR: int
    DTD_MISSING_ATTRIBUTE: int
    DTD_MIXED_CORRUPT: int
    DTD_MULTIPLE_ID: int
    DTD_NOTATION_REDEFINED: int
    DTD_NOTATION_VALUE: int
    DTD_NOT_EMPTY: int
    DTD_NOT_PCDATA: int
    DTD_NOT_STANDALONE: int
    DTD_NO_DOC: int
    DTD_NO_DTD: int
    DTD_NO_ELEM_NAME: int
    DTD_NO_PREFIX: int
    DTD_NO_ROOT: int
    DTD_ROOT_NAME: int
    DTD_STANDALONE_DEFAULTED: int
    DTD_STANDALONE_WHITE_SPACE: int
    DTD_UNKNOWN_ATTRIBUTE: int
    DTD_UNKNOWN_ELEM: int
    DTD_UNKNOWN_ENTITY: int
    DTD_UNKNOWN_ID: int
    DTD_UNKNOWN_NOTATION: int
    DTD_XMLID_TYPE: int
    DTD_XMLID_VALUE: int
    ERR_ATTLIST_NOT_FINISHED: int
    ERR_ATTLIST_NOT_STARTED: int
    ERR_ATTRIBUTE_NOT_FINISHED: int
    ERR_ATTRIBUTE_NOT_STARTED: int
    ERR_ATTRIBUTE_REDEFINED: int
    ERR_ATTRIBUTE_WITHOUT_VALUE: int
    ERR_CDATA_NOT_FINISHED: int
    ERR_CHARREF_AT_EOF: int
    ERR_CHARREF_IN_DTD: int
    ERR_CHARREF_IN_EPILOG: int
    ERR_CHARREF_IN_PROLOG: int
    ERR_COMMENT_NOT_FINISHED: int
    ERR_CONDSEC_INVALID: int
    ERR_CONDSEC_INVALID_KEYWORD: int
    ERR_CONDSEC_NOT_FINISHED: int
    ERR_CONDSEC_NOT_STARTED: int
    ERR_DOCTYPE_NOT_FINISHED: int
    ERR_DOCUMENT_EMPTY: int
    ERR_DOCUMENT_END: int
    ERR_DOCUMENT_START: int
    ERR_ELEMCONTENT_NOT_FINISHED: int
    ERR_ELEMCONTENT_NOT_STARTED: int
    ERR_ENCODING_NAME: int
    ERR_ENTITYREF_AT_EOF: int
    ERR_ENTITYREF_IN_DTD: int
    ERR_ENTITYREF_IN_EPILOG: int
    ERR_ENTITYREF_IN_PROLOG: int
    ERR_ENTITYREF_NO_NAME: int
    ERR_ENTITYREF_SEMICOL_MISSING: int
    ERR_ENTITY_BOUNDARY: int
    ERR_ENTITY_CHAR_ERROR: int
    ERR_ENTITY_IS_EXTERNAL: int
    ERR_ENTITY_IS_PARAMETER: int
    ERR_ENTITY_LOOP: int
    ERR_ENTITY_NOT_FINISHED: int
    ERR_ENTITY_NOT_STARTED: int
    ERR_ENTITY_PE_INTERNAL: int
    ERR_ENTITY_PROCESSING: int
    ERR_EQUAL_REQUIRED: int
    ERR_EXTRA_CONTENT: int
    ERR_EXT_ENTITY_STANDALONE: int
    ERR_EXT_SUBSET_NOT_FINISHED: int
    ERR_GT_REQUIRED: int
    ERR_HYPHEN_IN_COMMENT: int
    ERR_INTERNAL_ERROR: int
    ERR_INVALID_CHAR: int
    ERR_INVALID_CHARREF: int
    ERR_INVALID_DEC_CHARREF: int
    ERR_INVALID_ENCODING: int
    ERR_INVALID_HEX_CHARREF: int
    ERR_INVALID_URI: int
    ERR_LITERAL_NOT_FINISHED: int
    ERR_LITERAL_NOT_STARTED: int
    ERR_LTSLASH_REQUIRED: int
    ERR_LT_IN_ATTRIBUTE: int
    ERR_LT_REQUIRED: int
    ERR_MISPLACED_CDATA_END: int
    ERR_MISSING_ENCODING: int
    ERR_MIXED_NOT_FINISHED: int
    ERR_MIXED_NOT_STARTED: int
    ERR_NAME_REQUIRED: int
    ERR_NAME_TOO_LONG: int
    ERR_NMTOKEN_REQUIRED: int
    ERR_NOTATION_NOT_FINISHED: int
    ERR_NOTATION_NOT_STARTED: int
    ERR_NOTATION_PROCESSING: int
    ERR_NOT_STANDALONE: int
    ERR_NOT_WELL_BALANCED: int
    ERR_NO_DTD: int
    ERR_NO_MEMORY: int
    ERR_NS_DECL_ERROR: int
    ERR_OK: int
    ERR_PCDATA_REQUIRED: int
    ERR_PEREF_AT_EOF: int
    ERR_PEREF_IN_EPILOG: int
    ERR_PEREF_IN_INT_SUBSET: int
    ERR_PEREF_IN_PROLOG: int
    ERR_PEREF_NO_NAME: int
    ERR_PEREF_SEMICOL_MISSING: int
    ERR_PI_NOT_FINISHED: int
    ERR_PI_NOT_STARTED: int
    ERR_PUBID_REQUIRED: int
    ERR_RESERVED_XML_NAME: int
    ERR_SEPARATOR_REQUIRED: int
    ERR_SPACE_REQUIRED: int
    ERR_STANDALONE_VALUE: int
    ERR_STRING_NOT_CLOSED: int
    ERR_STRING_NOT_STARTED: int
    ERR_TAG_NAME_MISMATCH: int
    ERR_TAG_NOT_FINISHED: int
    ERR_UNDECLARED_ENTITY: int
    ERR_UNKNOWN_ENCODING: int
    ERR_UNKNOWN_VERSION: int
    ERR_UNPARSED_ENTITY: int
    ERR_UNSUPPORTED_ENCODING: int
    ERR_URI_FRAGMENT: int
    ERR_URI_REQUIRED: int
    ERR_USER_STOP: int
    ERR_VALUE_REQUIRED: int
    ERR_VERSION_MISMATCH: int
    ERR_VERSION_MISSING: int
    ERR_XMLDECL_NOT_FINISHED: int
    ERR_XMLDECL_NOT_STARTED: int
    FTP_ACCNT: int
    FTP_EPSV_ANSWER: int
    FTP_PASV_ANSWER: int
    FTP_URL_SYNTAX: int
    HTML_STRUCURE_ERROR: int
    HTML_UNKNOWN_TAG: int
    HTTP_UNKNOWN_HOST: int
    HTTP_URL_SYNTAX: int
    HTTP_USE_IP: int
    I18N_CONV_FAILED: int
    I18N_EXCESS_HANDLER: int
    I18N_NO_HANDLER: int
    I18N_NO_NAME: int
    I18N_NO_OUTPUT: int
    IO_BUFFER_FULL: int
    IO_EACCES: int
    IO_EADDRINUSE: int
    IO_EAFNOSUPPORT: int
    IO_EAGAIN: int
    IO_EALREADY: int
    IO_EBADF: int
    IO_EBADMSG: int
    IO_EBUSY: int
    IO_ECANCELED: int
    IO_ECHILD: int
    IO_ECONNREFUSED: int
    IO_EDEADLK: int
    IO_EDOM: int
    IO_EEXIST: int
    IO_EFAULT: int
    IO_EFBIG: int
    IO_EINPROGRESS: int
    IO_EINTR: int
    IO_EINVAL: int
    IO_EIO: int
    IO_EISCONN: int
    IO_EISDIR: int
    IO_EMFILE: int
    IO_EMLINK: int
    IO_EMSGSIZE: int
    IO_ENAMETOOLONG: int
    IO_ENCODER: int
    IO_ENETUNREACH: int
    IO_ENFILE: int
    IO_ENODEV: int
    IO_ENOENT: int
    IO_ENOEXEC: int
    IO_ENOLCK: int
    IO_ENOMEM: int
    IO_ENOSPC: int
    IO_ENOSYS: int
    IO_ENOTDIR: int
    IO_ENOTEMPTY: int
    IO_ENOTSOCK: int
    IO_ENOTSUP: int
    IO_ENOTTY: int
    IO_ENXIO: int
    IO_EPERM: int
    IO_EPIPE: int
    IO_ERANGE: int
    IO_EROFS: int
    IO_ESPIPE: int
    IO_ESRCH: int
    IO_ETIMEDOUT: int
    IO_EXDEV: int
    IO_FLUSH: int
    IO_LOAD_ERROR: int
    IO_NETWORK_ATTEMPT: int
    IO_NO_INPUT: int
    IO_UNKNOWN: int
    IO_WRITE: int
    MODULE_CLOSE: int
    MODULE_OPEN: int
    NS_ERR_ATTRIBUTE_REDEFINED: int
    NS_ERR_COLON: int
    NS_ERR_EMPTY: int
    NS_ERR_QNAME: int
    NS_ERR_UNDEFINED_NAMESPACE: int
    NS_ERR_XML_NAMESPACE: int
    REGEXP_COMPILE_ERROR: int
    RNGP_ANYNAME_ATTR_ANCESTOR: int
    RNGP_ATTRIBUTE_CHILDREN: int
    RNGP_ATTRIBUTE_CONTENT: int
    RNGP_ATTRIBUTE_EMPTY: int
    RNGP_ATTRIBUTE_NOOP: int
    RNGP_ATTR_CONFLICT: int
    RNGP_CHOICE_CONTENT: int
    RNGP_CHOICE_EMPTY: int
    RNGP_CREATE_FAILURE: int
    RNGP_DATA_CONTENT: int
    RNGP_DEFINE_CREATE_FAILED: int
    RNGP_DEFINE_EMPTY: int
    RNGP_DEFINE_MISSING: int
    RNGP_DEFINE_NAME_MISSING: int
    RNGP_DEF_CHOICE_AND_INTERLEAVE: int
    RNGP_ELEMENT_CONTENT: int
    RNGP_ELEMENT_EMPTY: int
    RNGP_ELEMENT_NAME: int
    RNGP_ELEMENT_NO_CONTENT: int
    RNGP_ELEM_CONTENT_EMPTY: int
    RNGP_ELEM_CONTENT_ERROR: int
    RNGP_ELEM_TEXT_CONFLICT: int
    RNGP_EMPTY: int
    RNGP_EMPTY_CONSTRUCT: int
    RNGP_EMPTY_CONTENT: int
    RNGP_EMPTY_NOT_EMPTY: int
    RNGP_ERROR_TYPE_LIB: int
    RNGP_EXCEPT_EMPTY: int
    RNGP_EXCEPT_MISSING: int
    RNGP_EXCEPT_MULTIPLE: int
    RNGP_EXCEPT_NO_CONTENT: int
    RNGP_EXTERNALREF_EMTPY: int
    RNGP_EXTERNALREF_RECURSE: int
    RNGP_EXTERNAL_REF_FAILURE: int
    RNGP_FORBIDDEN_ATTRIBUTE: int
    RNGP_FOREIGN_ELEMENT: int
    RNGP_GRAMMAR_CONTENT: int
    RNGP_GRAMMAR_EMPTY: int
    RNGP_GRAMMAR_MISSING: int
    RNGP_GRAMMAR_NO_START: int
    RNGP_GROUP_ATTR_CONFLICT: int
    RNGP_HREF_ERROR: int
    RNGP_INCLUDE_EMPTY: int
    RNGP_INCLUDE_FAILURE: int
    RNGP_INCLUDE_RECURSE: int
    RNGP_INTERLEAVE_ADD: int
    RNGP_INTERLEAVE_CREATE_FAILED: int
    RNGP_INTERLEAVE_EMPTY: int
    RNGP_INTERLEAVE_NO_CONTENT: int
    RNGP_INVALID_DEFINE_NAME: int
    RNGP_INVALID_URI: int
    RNGP_INVALID_VALUE: int
    RNGP_MISSING_HREF: int
    RNGP_NAME_MISSING: int
    RNGP_NEED_COMBINE: int
    RNGP_NOTALLOWED_NOT_EMPTY: int
    RNGP_NSNAME_ATTR_ANCESTOR: int
    RNGP_NSNAME_NO_NS: int
    RNGP_PARAM_FORBIDDEN: int
    RNGP_PARAM_NAME_MISSING: int
    RNGP_PARENTREF_CREATE_FAILED: int
    RNGP_PARENTREF_NAME_INVALID: int
    RNGP_PARENTREF_NOT_EMPTY: int
    RNGP_PARENTREF_NO_NAME: int
    RNGP_PARENTREF_NO_PARENT: int
    RNGP_PARSE_ERROR: int
    RNGP_PAT_ANYNAME_EXCEPT_ANYNAME: int
    RNGP_PAT_ATTR_ATTR: int
    RNGP_PAT_ATTR_ELEM: int
    RNGP_PAT_DATA_EXCEPT_ATTR: int
    RNGP_PAT_DATA_EXCEPT_ELEM: int
    RNGP_PAT_DATA_EXCEPT_EMPTY: int
    RNGP_PAT_DATA_EXCEPT_GROUP: int
    RNGP_PAT_DATA_EXCEPT_INTERLEAVE: int
    RNGP_PAT_DATA_EXCEPT_LIST: int
    RNGP_PAT_DATA_EXCEPT_ONEMORE: int
    RNGP_PAT_DATA_EXCEPT_REF: int
    RNGP_PAT_DATA_EXCEPT_TEXT: int
    RNGP_PAT_LIST_ATTR: int
    RNGP_PAT_LIST_ELEM: int
    RNGP_PAT_LIST_INTERLEAVE: int
    RNGP_PAT_LIST_LIST: int
    RNGP_PAT_LIST_REF: int
    RNGP_PAT_LIST_TEXT: int
    RNGP_PAT_NSNAME_EXCEPT_ANYNAME: int
    RNGP_PAT_NSNAME_EXCEPT_NSNAME: int
    RNGP_PAT_ONEMORE_GROUP_ATTR: int
    RNGP_PAT_ONEMORE_INTERLEAVE_ATTR: int
    RNGP_PAT_START_ATTR: int
    RNGP_PAT_START_DATA: int
    RNGP_PAT_START_EMPTY: int
    RNGP_PAT_START_GROUP: int
    RNGP_PAT_START_INTERLEAVE: int
    RNGP_PAT_START_LIST: int
    RNGP_PAT_START_ONEMORE: int
    RNGP_PAT_START_TEXT: int
    RNGP_PAT_START_VALUE: int
    RNGP_PREFIX_UNDEFINED: int
    RNGP_REF_CREATE_FAILED: int
    RNGP_REF_CYCLE: int
    RNGP_REF_NAME_INVALID: int
    RNGP_REF_NOT_EMPTY: int
    RNGP_REF_NO_DEF: int
    RNGP_REF_NO_NAME: int
    RNGP_START_CHOICE_AND_INTERLEAVE: int
    RNGP_START_CONTENT: int
    RNGP_START_EMPTY: int
    RNGP_START_MISSING: int
    RNGP_TEXT_EXPECTED: int
    RNGP_TEXT_HAS_CHILD: int
    RNGP_TYPE_MISSING: int
    RNGP_TYPE_NOT_FOUND: int
    RNGP_TYPE_VALUE: int
    RNGP_UNKNOWN_ATTRIBUTE: int
    RNGP_UNKNOWN_COMBINE: int
    RNGP_UNKNOWN_CONSTRUCT: int
    RNGP_UNKNOWN_TYPE_LIB: int
    RNGP_URI_FRAGMENT: int
    RNGP_URI_NOT_ABSOLUTE: int
    RNGP_VALUE_EMPTY: int
    RNGP_VALUE_NO_CONTENT: int
    RNGP_XMLNS_NAME: int
    RNGP_XML_NS: int
    SAVE_CHAR_INVALID: int
    SAVE_NOT_UTF8: int
    SAVE_NO_DOCTYPE: int
    SAVE_UNKNOWN_ENCODING: int
    SCHEMAP_AG_PROPS_CORRECT: int
    SCHEMAP_ATTRFORMDEFAULT_VALUE: int
    SCHEMAP_ATTRGRP_NONAME_NOREF: int
    SCHEMAP_ATTR_NONAME_NOREF: int
    SCHEMAP_AU_PROPS_CORRECT: int
    SCHEMAP_AU_PROPS_CORRECT_2: int
    SCHEMAP_A_PROPS_CORRECT_2: int
    SCHEMAP_A_PROPS_CORRECT_3: int
    SCHEMAP_COMPLEXTYPE_NONAME_NOREF: int
    SCHEMAP_COS_ALL_LIMITED: int
    SCHEMAP_COS_CT_EXTENDS_1_1: int
    SCHEMAP_COS_CT_EXTENDS_1_2: int
    SCHEMAP_COS_CT_EXTENDS_1_3: int
    SCHEMAP_COS_ST_DERIVED_OK_2_1: int
    SCHEMAP_COS_ST_DERIVED_OK_2_2: int
    SCHEMAP_COS_ST_RESTRICTS_1_1: int
    SCHEMAP_COS_ST_RESTRICTS_1_2: int
    SCHEMAP_COS_ST_RESTRICTS_1_3_1: int
    SCHEMAP_COS_ST_RESTRICTS_1_3_2: int
    SCHEMAP_COS_ST_RESTRICTS_2_1: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_1_1: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_1_2: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_1: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_2: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_3: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_4: int
    SCHEMAP_COS_ST_RESTRICTS_2_3_2_5: int
    SCHEMAP_COS_ST_RESTRICTS_3_1: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_1: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_1_2: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_1: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_2: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_3: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_4: int
    SCHEMAP_COS_ST_RESTRICTS_3_3_2_5: int
    SCHEMAP_COS_VALID_DEFAULT_1: int
    SCHEMAP_COS_VALID_DEFAULT_2_1: int
    SCHEMAP_COS_VALID_DEFAULT_2_2_1: int
    SCHEMAP_COS_VALID_DEFAULT_2_2_2: int
    SCHEMAP_CT_PROPS_CORRECT_1: int
    SCHEMAP_CT_PROPS_CORRECT_2: int
    SCHEMAP_CT_PROPS_CORRECT_3: int
    SCHEMAP_CT_PROPS_CORRECT_4: int
    SCHEMAP_CT_PROPS_CORRECT_5: int
    SCHEMAP_CVC_SIMPLE_TYPE: int
    SCHEMAP_C_PROPS_CORRECT: int
    SCHEMAP_DEF_AND_PREFIX: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_1: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_1: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_2: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_1_3: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_2_2: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_3: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_1: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_2: int
    SCHEMAP_DERIVATION_OK_RESTRICTION_4_3: int
    SCHEMAP_ELEMFORMDEFAULT_VALUE: int
    SCHEMAP_ELEM_DEFAULT_FIXED: int
    SCHEMAP_ELEM_NONAME_NOREF: int
    SCHEMAP_EXTENSION_NO_BASE: int
    SCHEMAP_E_PROPS_CORRECT_2: int
    SCHEMAP_E_PROPS_CORRECT_3: int
    SCHEMAP_E_PROPS_CORRECT_4: int
    SCHEMAP_E_PROPS_CORRECT_5: int
    SCHEMAP_E_PROPS_CORRECT_6: int
    SCHEMAP_FACET_NO_VALUE: int
    SCHEMAP_FAILED_BUILD_IMPORT: int
    SCHEMAP_FAILED_LOAD: int
    SCHEMAP_FAILED_PARSE: int
    SCHEMAP_GROUP_NONAME_NOREF: int
    SCHEMAP_IMPORT_NAMESPACE_NOT_URI: int
    SCHEMAP_IMPORT_REDEFINE_NSNAME: int
    SCHEMAP_IMPORT_SCHEMA_NOT_URI: int
    SCHEMAP_INCLUDE_SCHEMA_NOT_URI: int
    SCHEMAP_INCLUDE_SCHEMA_NO_URI: int
    SCHEMAP_INTERNAL: int
    SCHEMAP_INTERSECTION_NOT_EXPRESSIBLE: int
    SCHEMAP_INVALID_ATTR_COMBINATION: int
    SCHEMAP_INVALID_ATTR_INLINE_COMBINATION: int
    SCHEMAP_INVALID_ATTR_NAME: int
    SCHEMAP_INVALID_ATTR_USE: int
    SCHEMAP_INVALID_BOOLEAN: int
    SCHEMAP_INVALID_ENUM: int
    SCHEMAP_INVALID_FACET: int
    SCHEMAP_INVALID_FACET_VALUE: int
    SCHEMAP_INVALID_MAXOCCURS: int
    SCHEMAP_INVALID_MINOCCURS: int
    SCHEMAP_INVALID_REF_AND_SUBTYPE: int
    SCHEMAP_INVALID_WHITE_SPACE: int
    SCHEMAP_MG_PROPS_CORRECT_1: int
    SCHEMAP_MG_PROPS_CORRECT_2: int
    SCHEMAP_MISSING_SIMPLETYPE_CHILD: int
    SCHEMAP_NOATTR_NOREF: int
    SCHEMAP_NOROOT: int
    SCHEMAP_NOTATION_NO_NAME: int
    SCHEMAP_NOTHING_TO_PARSE: int
    SCHEMAP_NOTYPE_NOREF: int
    SCHEMAP_NOT_DETERMINISTIC: int
    SCHEMAP_NOT_SCHEMA: int
    SCHEMAP_NO_XMLNS: int
    SCHEMAP_NO_XSI: int
    SCHEMAP_PREFIX_UNDEFINED: int
    SCHEMAP_P_PROPS_CORRECT_1: int
    SCHEMAP_P_PROPS_CORRECT_2_1: int
    SCHEMAP_P_PROPS_CORRECT_2_2: int
    SCHEMAP_RECURSIVE: int
    SCHEMAP_REDEFINED_ATTR: int
    SCHEMAP_REDEFINED_ATTRGROUP: int
    SCHEMAP_REDEFINED_ELEMENT: int
    SCHEMAP_REDEFINED_GROUP: int
    SCHEMAP_REDEFINED_NOTATION: int
    SCHEMAP_REDEFINED_TYPE: int
    SCHEMAP_REF_AND_CONTENT: int
    SCHEMAP_REF_AND_SUBTYPE: int
    SCHEMAP_REGEXP_INVALID: int
    SCHEMAP_RESTRICTION_NONAME_NOREF: int
    SCHEMAP_S4S_ATTR_INVALID_VALUE: int
    SCHEMAP_S4S_ATTR_MISSING: int
    SCHEMAP_S4S_ATTR_NOT_ALLOWED: int
    SCHEMAP_S4S_ELEM_MISSING: int
    SCHEMAP_S4S_ELEM_NOT_ALLOWED: int
    SCHEMAP_SIMPLETYPE_NONAME: int
    SCHEMAP_SRC_ATTRIBUTE_1: int
    SCHEMAP_SRC_ATTRIBUTE_2: int
    SCHEMAP_SRC_ATTRIBUTE_3_1: int
    SCHEMAP_SRC_ATTRIBUTE_3_2: int
    SCHEMAP_SRC_ATTRIBUTE_4: int
    SCHEMAP_SRC_ATTRIBUTE_GROUP_1: int
    SCHEMAP_SRC_ATTRIBUTE_GROUP_2: int
    SCHEMAP_SRC_ATTRIBUTE_GROUP_3: int
    SCHEMAP_SRC_CT_1: int
    SCHEMAP_SRC_ELEMENT_1: int
    SCHEMAP_SRC_ELEMENT_2_1: int
    SCHEMAP_SRC_ELEMENT_2_2: int
    SCHEMAP_SRC_ELEMENT_3: int
    SCHEMAP_SRC_IMPORT: int
    SCHEMAP_SRC_IMPORT_1_1: int
    SCHEMAP_SRC_IMPORT_1_2: int
    SCHEMAP_SRC_IMPORT_2: int
    SCHEMAP_SRC_IMPORT_2_1: int
    SCHEMAP_SRC_IMPORT_2_2: int
    SCHEMAP_SRC_IMPORT_3_1: int
    SCHEMAP_SRC_IMPORT_3_2: int
    SCHEMAP_SRC_INCLUDE: int
    SCHEMAP_SRC_LIST_ITEMTYPE_OR_SIMPLETYPE: int
    SCHEMAP_SRC_REDEFINE: int
    SCHEMAP_SRC_RESOLVE: int
    SCHEMAP_SRC_RESTRICTION_BASE_OR_SIMPLETYPE: int
    SCHEMAP_SRC_SIMPLE_TYPE_1: int
    SCHEMAP_SRC_SIMPLE_TYPE_2: int
    SCHEMAP_SRC_SIMPLE_TYPE_3: int
    SCHEMAP_SRC_SIMPLE_TYPE_4: int
    SCHEMAP_SRC_UNION_MEMBERTYPES_OR_SIMPLETYPES: int
    SCHEMAP_ST_PROPS_CORRECT_1: int
    SCHEMAP_ST_PROPS_CORRECT_2: int
    SCHEMAP_ST_PROPS_CORRECT_3: int
    SCHEMAP_SUPERNUMEROUS_LIST_ITEM_TYPE: int
    SCHEMAP_TYPE_AND_SUBTYPE: int
    SCHEMAP_UNION_NOT_EXPRESSIBLE: int
    SCHEMAP_UNKNOWN_ALL_CHILD: int
    SCHEMAP_UNKNOWN_ANYATTRIBUTE_CHILD: int
    SCHEMAP_UNKNOWN_ATTRGRP_CHILD: int
    SCHEMAP_UNKNOWN_ATTRIBUTE_GROUP: int
    SCHEMAP_UNKNOWN_ATTR_CHILD: int
    SCHEMAP_UNKNOWN_BASE_TYPE: int
    SCHEMAP_UNKNOWN_CHOICE_CHILD: int
    SCHEMAP_UNKNOWN_COMPLEXCONTENT_CHILD: int
    SCHEMAP_UNKNOWN_COMPLEXTYPE_CHILD: int
    SCHEMAP_UNKNOWN_ELEM_CHILD: int
    SCHEMAP_UNKNOWN_EXTENSION_CHILD: int
    SCHEMAP_UNKNOWN_FACET_CHILD: int
    SCHEMAP_UNKNOWN_FACET_TYPE: int
    SCHEMAP_UNKNOWN_GROUP_CHILD: int
    SCHEMAP_UNKNOWN_IMPORT_CHILD: int
    SCHEMAP_UNKNOWN_INCLUDE_CHILD: int
    SCHEMAP_UNKNOWN_LIST_CHILD: int
    SCHEMAP_UNKNOWN_MEMBER_TYPE: int
    SCHEMAP_UNKNOWN_NOTATION_CHILD: int
    SCHEMAP_UNKNOWN_PREFIX: int
    SCHEMAP_UNKNOWN_PROCESSCONTENT_CHILD: int
    SCHEMAP_UNKNOWN_REF: int
    SCHEMAP_UNKNOWN_RESTRICTION_CHILD: int
    SCHEMAP_UNKNOWN_SCHEMAS_CHILD: int
    SCHEMAP_UNKNOWN_SEQUENCE_CHILD: int
    SCHEMAP_UNKNOWN_SIMPLECONTENT_CHILD: int
    SCHEMAP_UNKNOWN_SIMPLETYPE_CHILD: int
    SCHEMAP_UNKNOWN_TYPE: int
    SCHEMAP_UNKNOWN_UNION_CHILD: int
    SCHEMAP_WARN_ATTR_POINTLESS_PROH: int
    SCHEMAP_WARN_ATTR_REDECL_PROH: int
    SCHEMAP_WARN_SKIP_SCHEMA: int
    SCHEMAP_WARN_UNLOCATED_SCHEMA: int
    SCHEMAP_WILDCARD_INVALID_NS_MEMBER: int
    SCHEMATRONV_ASSERT: int
    SCHEMATRONV_REPORT: int
    SCHEMAV_ATTRINVALID: int
    SCHEMAV_ATTRUNKNOWN: int
    SCHEMAV_CONSTRUCT: int
    SCHEMAV_CVC_ATTRIBUTE_1: int
    SCHEMAV_CVC_ATTRIBUTE_2: int
    SCHEMAV_CVC_ATTRIBUTE_3: int
    SCHEMAV_CVC_ATTRIBUTE_4: int
    SCHEMAV_CVC_AU: int
    SCHEMAV_CVC_COMPLEX_TYPE_1: int
    SCHEMAV_CVC_COMPLEX_TYPE_2_1: int
    SCHEMAV_CVC_COMPLEX_TYPE_2_2: int
    SCHEMAV_CVC_COMPLEX_TYPE_2_3: int
    SCHEMAV_CVC_COMPLEX_TYPE_2_4: int
    SCHEMAV_CVC_COMPLEX_TYPE_3_1: int
    SCHEMAV_CVC_COMPLEX_TYPE_3_2_1: int
    SCHEMAV_CVC_COMPLEX_TYPE_3_2_2: int
    SCHEMAV_CVC_COMPLEX_TYPE_4: int
    SCHEMAV_CVC_COMPLEX_TYPE_5_1: int
    SCHEMAV_CVC_COMPLEX_TYPE_5_2: int
    SCHEMAV_CVC_DATATYPE_VALID_1_2_1: int
    SCHEMAV_CVC_DATATYPE_VALID_1_2_2: int
    SCHEMAV_CVC_DATATYPE_VALID_1_2_3: int
    SCHEMAV_CVC_ELT_1: int
    SCHEMAV_CVC_ELT_2: int
    SCHEMAV_CVC_ELT_3_1: int
    SCHEMAV_CVC_ELT_3_2_1: int
    SCHEMAV_CVC_ELT_3_2_2: int
    SCHEMAV_CVC_ELT_4_1: int
    SCHEMAV_CVC_ELT_4_2: int
    SCHEMAV_CVC_ELT_4_3: int
    SCHEMAV_CVC_ELT_5_1_1: int
    SCHEMAV_CVC_ELT_5_1_2: int
    SCHEMAV_CVC_ELT_5_2_1: int
    SCHEMAV_CVC_ELT_5_2_2_1: int
    SCHEMAV_CVC_ELT_5_2_2_2_1: int
    SCHEMAV_CVC_ELT_5_2_2_2_2: int
    SCHEMAV_CVC_ELT_6: int
    SCHEMAV_CVC_ELT_7: int
    SCHEMAV_CVC_ENUMERATION_VALID: int
    SCHEMAV_CVC_FACET_VALID: int
    SCHEMAV_CVC_FRACTIONDIGITS_VALID: int
    SCHEMAV_CVC_IDC: int
    SCHEMAV_CVC_LENGTH_VALID: int
    SCHEMAV_CVC_MAXEXCLUSIVE_VALID: int
    SCHEMAV_CVC_MAXINCLUSIVE_VALID: int
    SCHEMAV_CVC_MAXLENGTH_VALID: int
    SCHEMAV_CVC_MINEXCLUSIVE_VALID: int
    SCHEMAV_CVC_MININCLUSIVE_VALID: int
    SCHEMAV_CVC_MINLENGTH_VALID: int
    SCHEMAV_CVC_PATTERN_VALID: int
    SCHEMAV_CVC_TOTALDIGITS_VALID: int
    SCHEMAV_CVC_TYPE_1: int
    SCHEMAV_CVC_TYPE_2: int
    SCHEMAV_CVC_TYPE_3_1_1: int
    SCHEMAV_CVC_TYPE_3_1_2: int
    SCHEMAV_CVC_WILDCARD: int
    SCHEMAV_DOCUMENT_ELEMENT_MISSING: int
    SCHEMAV_ELEMCONT: int
    SCHEMAV_ELEMENT_CONTENT: int
    SCHEMAV_EXTRACONTENT: int
    SCHEMAV_FACET: int
    SCHEMAV_HAVEDEFAULT: int
    SCHEMAV_INTERNAL: int
    SCHEMAV_INVALIDATTR: int
    SCHEMAV_INVALIDELEM: int
    SCHEMAV_ISABSTRACT: int
    SCHEMAV_MISC: int
    SCHEMAV_MISSING: int
    SCHEMAV_NOROLLBACK: int
    SCHEMAV_NOROOT: int
    SCHEMAV_NOTDETERMINIST: int
    SCHEMAV_NOTEMPTY: int
    SCHEMAV_NOTNILLABLE: int
    SCHEMAV_NOTSIMPLE: int
    SCHEMAV_NOTTOPLEVEL: int
    SCHEMAV_NOTYPE: int
    SCHEMAV_UNDECLAREDELEM: int
    SCHEMAV_VALUE: int
    SCHEMAV_WRONGELEM: int
    TREE_INVALID_DEC: int
    TREE_INVALID_HEX: int
    TREE_NOT_UTF8: int
    TREE_UNTERMINATED_ENTITY: int
    WAR_CATALOG_PI: int
    WAR_ENTITY_REDEFINED: int
    WAR_LANG_VALUE: int
    WAR_NS_COLUMN: int
    WAR_NS_URI: int
    WAR_NS_URI_RELATIVE: int
    WAR_SPACE_VALUE: int
    WAR_UNDECLARED_ENTITY: int
    WAR_UNKNOWN_VERSION: int
    XINCLUDE_BUILD_FAILED: int
    XINCLUDE_DEPRECATED_NS: int
    XINCLUDE_ENTITY_DEF_MISMATCH: int
    XINCLUDE_FALLBACKS_IN_INCLUDE: int
    XINCLUDE_FALLBACK_NOT_IN_INCLUDE: int
    XINCLUDE_FRAGMENT_ID: int
    XINCLUDE_HREF_URI: int
    XINCLUDE_INCLUDE_IN_INCLUDE: int
    XINCLUDE_INVALID_CHAR: int
    XINCLUDE_MULTIPLE_ROOT: int
    XINCLUDE_NO_FALLBACK: int
    XINCLUDE_NO_HREF: int
    XINCLUDE_PARSE_VALUE: int
    XINCLUDE_RECURSION: int
    XINCLUDE_TEXT_DOCUMENT: int
    XINCLUDE_TEXT_FRAGMENT: int
    XINCLUDE_UNKNOWN_ENCODING: int
    XINCLUDE_XPTR_FAILED: int
    XINCLUDE_XPTR_RESULT: int
    XPATH_ENCODING_ERROR: int
    XPATH_EXPRESSION_OK: int
    XPATH_EXPR_ERROR: int
    XPATH_INVALID_ARITY: int
    XPATH_INVALID_CHAR_ERROR: int
    XPATH_INVALID_CTXT_POSITION: int
    XPATH_INVALID_CTXT_SIZE: int
    XPATH_INVALID_OPERAND: int
    XPATH_INVALID_PREDICATE_ERROR: int
    XPATH_INVALID_TYPE: int
    XPATH_MEMORY_ERROR: int
    XPATH_NUMBER_ERROR: int
    XPATH_START_LITERAL_ERROR: int
    XPATH_UNCLOSED_ERROR: int
    XPATH_UNDEF_PREFIX_ERROR: int
    XPATH_UNDEF_VARIABLE_ERROR: int
    XPATH_UNFINISHED_LITERAL_ERROR: int
    XPATH_UNKNOWN_FUNC_ERROR: int
    XPATH_VARIABLE_REF_ERROR: int
    XPTR_CHILDSEQ_START: int
    XPTR_EVAL_FAILED: int
    XPTR_EXTRA_OBJECTS: int
    XPTR_RESOURCE_ERROR: int
    XPTR_SUB_RESOURCE_ERROR: int
    XPTR_SYNTAX_ERROR: int
    XPTR_UNKNOWN_SCHEME: int
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Libxml2 error types'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    @classmethod
    def _getName(cls, self, key, default) -> typing.Any:
        'Return the value for key if key is in the dictionary, else default.'
        ...
    
    _names: dict
    def __getattr__(self, name) -> typing.Any:
        ...
    

def Extension(module, function_mapping) -> typing.Any:
    'Extension(module, function_mapping=None, ns=None)\n\n    Build a dictionary of extension functions from the functions\n    defined in a module or the methods of an object.\n\n    As second argument, you can pass an additional mapping of\n    attribute names to XPath function names, or a list of function\n    names that should be taken.\n\n    The ``ns`` keyword argument accepts a namespace URI for the XPath\n    functions.\n    '
    ...

class FallbackElementClassLookup(ElementClassLookup):
    'FallbackElementClassLookup(self, fallback=None)\n\n    Superclass of Element class lookups with additional fallback.\n    '
    def __init__(self, fallback=...) -> None:
        'FallbackElementClassLookup(self, fallback=None)\n\n    Superclass of Element class lookups with additional fallback.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def fallback(self) -> typing.Any:
        ...
    
    def set_fallback(self, lookup) -> typing.Any:
        'set_fallback(self, lookup)\n\n        Sets the fallback scheme for this lookup method.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def FunctionNamespace(ns_uri) -> typing.Any:
    'FunctionNamespace(ns_uri)\n\n    Retrieve the function namespace object associated with the given\n    URI.\n\n    Creates a new one if it does not yet exist. A function namespace\n    can only be used to register extension functions.\n\n    Usage:\n\n    >>> ns_functions = FunctionNamespace("http://schema.org/Movie")\n\n    >>> @ns_functions  # uses function name\n    ... def add2(x):\n    ...     return x + 2\n\n    >>> @ns_functions("add3")  # uses explicit name\n    ... def add_three(x):\n    ...     return x + 3\n    '
    ...

def HTML(text, parser) -> typing.Any:
    'HTML(text, parser=None, base_url=None)\n\n    Parses an HTML document from a string constant.  Returns the root\n    node (or the result returned by a parser target).  This function\n    can be used to embed "HTML literals" in Python code.\n\n    To override the parser with a different ``HTMLParser`` you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    ...

class HTMLParser(_FeedParser):
    "HTMLParser(self, encoding=None, remove_blank_text=False,                    remove_comments=False, remove_pis=False, strip_cdata=True,                    no_network=True, target=None, schema: XMLSchema =None,                    recover=True, compact=True, collect_ids=True, huge_tree=False)\n\n    The HTML parser.\n\n    This parser allows reading HTML into a normal XML tree.  By\n    default, it can read broken (non well-formed) HTML, depending on\n    the capabilities of libxml2.  Use the 'recover' option to switch\n    this off.\n\n    Available boolean keyword arguments:\n\n    - recover            - try hard to parse through broken HTML (default: True)\n    - no_network         - prevent network access for related files (default: True)\n    - remove_blank_text  - discard empty text nodes that are ignorable (i.e. not actual text content)\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - default_doctype    - add a default doctype even if it is not found in the HTML (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads for performance\n    reasons.\n    "
    def __init__(self, encoding=..., remove_blank_text=..., remove_comments=..., remove_pis=..., strip_cdata=..., no_network=..., target=..., schema=..., recover=..., compact=..., collect_ids=..., huge_tree=...) -> None:
        "HTMLParser(self, encoding=None, remove_blank_text=False,                    remove_comments=False, remove_pis=False, strip_cdata=True,                    no_network=True, target=None, schema: XMLSchema =None,                    recover=True, compact=True, collect_ids=True, huge_tree=False)\n\n    The HTML parser.\n\n    This parser allows reading HTML into a normal XML tree.  By\n    default, it can read broken (non well-formed) HTML, depending on\n    the capabilities of libxml2.  Use the 'recover' option to switch\n    this off.\n\n    Available boolean keyword arguments:\n\n    - recover            - try hard to parse through broken HTML (default: True)\n    - no_network         - prevent network access for related files (default: True)\n    - remove_blank_text  - discard empty text nodes that are ignorable (i.e. not actual text content)\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - default_doctype    - add a default doctype even if it is not found in the HTML (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads for performance\n    reasons.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class HTMLPullParser(HTMLParser):
    "HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)\n\n    HTML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
    def __init__(self, events=..., *, tag=..., base_url=..., **kwargs) -> None:
        "HTMLPullParser(self, events=None, *, tag=None, base_url=None, **kwargs)\n\n    HTML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def read_events(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

LIBXML_COMPILED_VERSION: tuple
LIBXML_VERSION: tuple
LIBXSLT_COMPILED_VERSION: tuple
LIBXSLT_VERSION: tuple
LXML_VERSION: tuple
class LxmlError(Error):
    'Main exception base class for lxml.  All other exceptions inherit from\n    this one.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Main exception base class for lxml.  All other exceptions inherit from\n    this one.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class LxmlRegistryError(LxmlError):
    'Base class of lxml registry errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class of lxml registry errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class LxmlSyntaxError(LxmlError,_mod_builtins.SyntaxError):
    'Base class for all syntax errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class for all syntax errors.\n    '
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
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class NamespaceRegistryError(LxmlRegistryError):
    'Error registering a namespace extension.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error registering a namespace extension.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def PI(target, text) -> typing.Any:
    'ProcessingInstruction(target, text=None)\n\n    ProcessingInstruction element factory. This factory function creates a\n    special element that will be serialized as an XML processing instruction.\n    '
    ...

class PIBase(_ProcessingInstruction):
    'All custom Processing Instruction classes must inherit from this one.\n\n    To create an XML ProcessingInstruction instance, use the ``PI()``\n    factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of PIs must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'All custom Processing Instruction classes must inherit from this one.\n\n    To create an XML ProcessingInstruction instance, use the ``PI()``\n    factory.\n\n    Subclasses *must not* override __init__ or __new__ as it is\n    absolutely undefined when these objects will be created or\n    destroyed.  All persistent state of PIs must be stored in the\n    underlying XML.  If you really need to initialize the object after\n    creation, you can implement an ``_init(self)`` method that will be\n    called after object creation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ParseError(LxmlSyntaxError):
    'Syntax error while parsing an XML document.\n\n    For compatibility with ElementTree 1.3 and later.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, message, code, line, column, filename) -> None:
        'Syntax error while parsing an XML document.\n\n    For compatibility with ElementTree 1.3 and later.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    position: property
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ParserBasedElementClassLookup(FallbackElementClassLookup):
    'ParserBasedElementClassLookup(self, fallback=None)\n    Element class lookup based on the XML parser.\n    '
    def __init__(self, fallback=...) -> None:
        'ParserBasedElementClassLookup(self, fallback=None)\n    Element class lookup based on the XML parser.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class ParserError(LxmlError):
    'Internal lxml parser error.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Internal lxml parser error.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def ProcessingInstruction(target, text) -> typing.Any:
    'ProcessingInstruction(target, text=None)\n\n    ProcessingInstruction element factory. This factory function creates a\n    special element that will be serialized as an XML processing instruction.\n    '
    ...

class PyErrorLog(_BaseErrorLog):
    "PyErrorLog(self, logger_name=None, logger=None)\n    A global error log that connects to the Python stdlib logging package.\n\n    The constructor accepts an optional logger name or a readily\n    instantiated logger instance.\n\n    If you want to change the mapping between libxml2's ErrorLevels and Python\n    logging levels, you can modify the level_map dictionary from a subclass.\n\n    The default mapping is::\n\n            ErrorLevels.WARNING = logging.WARNING\n            ErrorLevels.ERROR   = logging.ERROR\n            ErrorLevels.FATAL   = logging.CRITICAL\n\n    You can also override the method ``receive()`` that takes a LogEntry\n    object and calls ``self.log(log_entry, format_string, arg1, arg2, ...)``\n    with appropriate data.\n    "
    def __init__(self, logger_name=..., logger=...) -> None:
        "PyErrorLog(self, logger_name=None, logger=None)\n    A global error log that connects to the Python stdlib logging package.\n\n    The constructor accepts an optional logger name or a readily\n    instantiated logger instance.\n\n    If you want to change the mapping between libxml2's ErrorLevels and Python\n    logging levels, you can modify the level_map dictionary from a subclass.\n\n    The default mapping is::\n\n            ErrorLevels.WARNING = logging.WARNING\n            ErrorLevels.ERROR   = logging.ERROR\n            ErrorLevels.FATAL   = logging.CRITICAL\n\n    You can also override the method ``receive()`` that takes a LogEntry\n    object and calls ``self.log(log_entry, format_string, arg1, arg2, ...)``\n    with appropriate data.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def copy(self) -> typing.Any:
        'Dummy method that returns an empty error log.\n        '
        ...
    
    @property
    def level_map(self) -> typing.Any:
        ...
    
    def log(self, log_entry, message, *args) -> typing.Any:
        'log(self, log_entry, message, *args)\n\n        Called by the .receive() method to log a _LogEntry instance to\n        the Python logging system.  This handles the error level\n        mapping.\n\n        In the default implementation, the ``message`` argument\n        receives a complete log line, and there are no further\n        ``args``.  To change the message format, it is best to\n        override the .receive() method instead of this one.\n        '
        ...
    
    def receive(self, log_entry) -> typing.Any:
        'receive(self, log_entry)\n\n        Receive a _LogEntry instance from the logging system.  Calls\n        the .log() method with appropriate parameters::\n\n            self.log(log_entry, repr(log_entry))\n\n        You can override this method to provide your own log output\n        format.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class PythonElementClassLookup(FallbackElementClassLookup):
    'PythonElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    This class lookup scheme allows access to the entire XML tree in\n    read-only mode.  To use it, re-implement the ``lookup(self, doc,\n    root)`` method in a subclass::\n\n        from lxml import etree, pyclasslookup\n\n        class MyElementClass(etree.ElementBase):\n            honkey = True\n\n        class MyLookup(pyclasslookup.PythonElementClassLookup):\n            def lookup(self, doc, root):\n                if root.tag == "sometag":\n                    return MyElementClass\n                else:\n                    for child in root:\n                        if child.tag == "someothertag":\n                            return MyElementClass\n                # delegate to default\n                return None\n\n    If you return None from this method, the fallback will be called.\n\n    The first argument is the opaque document instance that contains\n    the Element.  The second argument is a lightweight Element proxy\n    implementation that is only valid during the lookup.  Do not try\n    to keep a reference to it.  Once the lookup is done, the proxy\n    will be invalid.\n\n    Also, you cannot wrap such a read-only Element in an ElementTree,\n    and you must take care not to keep a reference to them outside of\n    the `lookup()` method.\n\n    Note that the API of the Element objects is not complete.  It is\n    purely read-only and does not support all features of the normal\n    `lxml.etree` API (such as XPath, extended slicing or some\n    iteration methods).\n\n    See https://lxml.de/element_classes.html\n    '
    def __init__(self, fallback=...) -> None:
        'PythonElementClassLookup(self, fallback=None)\n    Element class lookup based on a subclass method.\n\n    This class lookup scheme allows access to the entire XML tree in\n    read-only mode.  To use it, re-implement the ``lookup(self, doc,\n    root)`` method in a subclass::\n\n        from lxml import etree, pyclasslookup\n\n        class MyElementClass(etree.ElementBase):\n            honkey = True\n\n        class MyLookup(pyclasslookup.PythonElementClassLookup):\n            def lookup(self, doc, root):\n                if root.tag == "sometag":\n                    return MyElementClass\n                else:\n                    for child in root:\n                        if child.tag == "someothertag":\n                            return MyElementClass\n                # delegate to default\n                return None\n\n    If you return None from this method, the fallback will be called.\n\n    The first argument is the opaque document instance that contains\n    the Element.  The second argument is a lightweight Element proxy\n    implementation that is only valid during the lookup.  Do not try\n    to keep a reference to it.  Once the lookup is done, the proxy\n    will be invalid.\n\n    Also, you cannot wrap such a read-only Element in an ElementTree,\n    and you must take care not to keep a reference to them outside of\n    the `lookup()` method.\n\n    Note that the API of the Element objects is not complete.  It is\n    purely read-only and does not support all features of the normal\n    `lxml.etree` API (such as XPath, extended slicing or some\n    iteration methods).\n\n    See https://lxml.de/element_classes.html\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def lookup(self, doc, element) -> typing.Any:
        'lookup(self, doc, element)\n\n        Override this method to implement your own lookup scheme.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class QName(_mod_builtins.object):
    'QName(text_or_uri_or_element, tag=None)\n\n    QName wrapper for qualified XML names.\n\n    Pass a tag name by itself or a namespace URI and a tag name to\n    create a qualified name.  Alternatively, pass an Element to\n    extract its tag name.  ``None`` as first argument is ignored in\n    order to allow for generic 2-argument usage.\n\n    The ``text`` property holds the qualified name in\n    ``{namespace}tagname`` notation.  The ``namespace`` and\n    ``localname`` properties hold the respective parts of the tag\n    name.\n\n    You can pass QName objects wherever a tag name is expected.  Also,\n    setting Element text from a QName will resolve the namespace prefix\n    on assignment and set a qualified text value.  This is helpful in XML\n    languages like SOAP or XML-Schema that use prefixed tag names in\n    their text content.\n    '
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    def __hash__(self) -> int:
        'Return hash(self).'
        ...
    
    def __init__(self, text_or_uri_or_element, tag=...) -> None:
        'QName(text_or_uri_or_element, tag=None)\n\n    QName wrapper for qualified XML names.\n\n    Pass a tag name by itself or a namespace URI and a tag name to\n    create a qualified name.  Alternatively, pass an Element to\n    extract its tag name.  ``None`` as first argument is ignored in\n    order to allow for generic 2-argument usage.\n\n    The ``text`` property holds the qualified name in\n    ``{namespace}tagname`` notation.  The ``namespace`` and\n    ``localname`` properties hold the respective parts of the tag\n    name.\n\n    You can pass QName objects wherever a tag name is expected.  Also,\n    setting Element text from a QName will resolve the namespace prefix\n    on assignment and set a qualified text value.  This is helpful in XML\n    languages like SOAP or XML-Schema that use prefixed tag names in\n    their text content.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def localname(self) -> typing.Any:
        ...
    
    @property
    def namespace(self) -> typing.Any:
        ...
    
    @property
    def text(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelaxNG(_Validator):
    'RelaxNG(self, etree=None, file=None)\n    Turn a document into a Relax NG validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n    '
    def __call__(self, etree) -> typing.Any:
        '__call__(self, etree)\n\n        Validate doc using Relax NG.\n\n        Returns true if document is valid, false if not.'
        ...
    
    def __init__(self, etree=..., file=...) -> None:
        'RelaxNG(self, etree=None, file=None)\n    Turn a document into a Relax NG validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def from_rnc_string(self, cls, src, base_url) -> typing.Any:
        "Parse a RelaxNG schema in compact syntax from a text string\n\n        Requires the rnc2rng package to be installed.\n\n        Passing the source URL or file path of the source as 'base_url'\n        will enable resolving resource references relative to the source.\n        "
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelaxNGError(LxmlError):
    'Base class for RelaxNG errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class for RelaxNG errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelaxNGErrorTypes(_mod_builtins.object):
    'Libxml2 RelaxNG error types'
    RELAXNG_ERR_ATTREXTRANS: int
    RELAXNG_ERR_ATTRNAME: int
    RELAXNG_ERR_ATTRNONS: int
    RELAXNG_ERR_ATTRVALID: int
    RELAXNG_ERR_ATTRWRONGNS: int
    RELAXNG_ERR_CONTENTVALID: int
    RELAXNG_ERR_DATAELEM: int
    RELAXNG_ERR_DATATYPE: int
    RELAXNG_ERR_DUPID: int
    RELAXNG_ERR_ELEMEXTRANS: int
    RELAXNG_ERR_ELEMNAME: int
    RELAXNG_ERR_ELEMNONS: int
    RELAXNG_ERR_ELEMNOTEMPTY: int
    RELAXNG_ERR_ELEMWRONG: int
    RELAXNG_ERR_ELEMWRONGNS: int
    RELAXNG_ERR_EXTRACONTENT: int
    RELAXNG_ERR_EXTRADATA: int
    RELAXNG_ERR_INTEREXTRA: int
    RELAXNG_ERR_INTERNAL: int
    RELAXNG_ERR_INTERNODATA: int
    RELAXNG_ERR_INTERSEQ: int
    RELAXNG_ERR_INVALIDATTR: int
    RELAXNG_ERR_LACKDATA: int
    RELAXNG_ERR_LIST: int
    RELAXNG_ERR_LISTELEM: int
    RELAXNG_ERR_LISTEMPTY: int
    RELAXNG_ERR_LISTEXTRA: int
    RELAXNG_ERR_MEMORY: int
    RELAXNG_ERR_NODEFINE: int
    RELAXNG_ERR_NOELEM: int
    RELAXNG_ERR_NOGRAMMAR: int
    RELAXNG_ERR_NOSTATE: int
    RELAXNG_ERR_NOTELEM: int
    RELAXNG_ERR_TEXTWRONG: int
    RELAXNG_ERR_TYPE: int
    RELAXNG_ERR_TYPECMP: int
    RELAXNG_ERR_TYPEVAL: int
    RELAXNG_ERR_VALELEM: int
    RELAXNG_ERR_VALUE: int
    RELAXNG_OK: int
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Libxml2 RelaxNG error types'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    @classmethod
    def _getName(cls, self, key, default) -> typing.Any:
        'Return the value for key if key is in the dictionary, else default.'
        ...
    
    _names: dict
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelaxNGParseError(RelaxNGError):
    'Error while parsing an XML document as RelaxNG.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while parsing an XML document as RelaxNG.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class RelaxNGValidateError(RelaxNGError):
    'Error while validating an XML document with a RelaxNG schema.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while validating an XML document with a RelaxNG schema.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Resolver(_mod_builtins.object):
    'This is the base class of all resolvers.'
    def __init__(self, *args, **kwargs) -> None:
        'This is the base class of all resolvers.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def resolve(self, system_url, public_id, context) -> typing.Any:
        'resolve(self, system_url, public_id, context)\n\n        Override this method to resolve an external source by\n        ``system_url`` and ``public_id``.  The third argument is an\n        opaque context object.\n\n        Return the result of one of the ``resolve_*()`` methods.\n        '
        ...
    
    def resolve_empty(self, context) -> typing.Any:
        'resolve_empty(self, context)\n\n        Return an empty input document.\n\n        Pass context as parameter.\n        '
        ...
    
    def resolve_file(self, f, context) -> typing.Any:
        'resolve_file(self, f, context, base_url=None, close=True)\n\n        Return an open file-like object as input document.\n\n        Pass open file and context as parameters.  You can pass the\n        base URL or filename of the file through the ``base_url``\n        keyword argument.  If the ``close`` flag is True (the\n        default), the file will be closed after reading.\n\n        Note that using ``.resolve_filename()`` is more efficient,\n        especially in threaded environments.\n        '
        ...
    
    def resolve_filename(self, filename, context) -> typing.Any:
        'resolve_filename(self, filename, context)\n\n        Return the name of a parsable file as input document.\n\n        Pass filename and context as parameters.  You can also pass a\n        URL with an HTTP, FTP or file target.\n        '
        ...
    
    def resolve_string(self, string, context) -> typing.Any:
        'resolve_string(self, string, context, base_url=None)\n\n        Return a parsable string as input document.\n\n        Pass data string and context as parameters.  You can pass the\n        source URL or filename through the ``base_url`` keyword\n        argument.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class Schematron(_Validator):
    'Schematron(self, etree=None, file=None)\n    A Schematron validator.\n\n    Pass a root Element or an ElementTree to turn it into a validator.\n    Alternatively, pass a filename as keyword argument \'file\' to parse from\n    the file system.\n\n    Schematron is a less well known, but very powerful schema language.  The main\n    idea is to use the capabilities of XPath to put restrictions on the structure\n    and the content of XML documents.  Here is a simple example::\n\n      >>> schematron = Schematron(XML(\'\'\'\n      ... <schema xmlns="http://www.ascc.net/xml/schematron" >\n      ...   <pattern name="id is the only permitted attribute name">\n      ...     <rule context="*">\n      ...       <report test="@*[not(name()=\'id\')]">Attribute\n      ...         <name path="@*[not(name()=\'id\')]"/> is forbidden<name/>\n      ...       </report>\n      ...     </rule>\n      ...   </pattern>\n      ... </schema>\n      ... \'\'\'))\n\n      >>> xml = XML(\'\'\'\n      ... <AAA name="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC color="ccc"/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      0\n\n      >>> xml = XML(\'\'\'\n      ... <AAA id="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      1\n\n    Schematron was added to libxml2 in version 2.6.21.  Before version 2.6.32,\n    however, Schematron lacked support for error reporting other than to stderr.\n    This version is therefore required to retrieve validation warnings and\n    errors in lxml.\n    '
    def __call__(self, etree) -> typing.Any:
        '__call__(self, etree)\n\n        Validate doc using Schematron.\n\n        Returns true if document is valid, false if not.'
        ...
    
    def __init__(self, etree=..., file=...) -> None:
        'Schematron(self, etree=None, file=None)\n    A Schematron validator.\n\n    Pass a root Element or an ElementTree to turn it into a validator.\n    Alternatively, pass a filename as keyword argument \'file\' to parse from\n    the file system.\n\n    Schematron is a less well known, but very powerful schema language.  The main\n    idea is to use the capabilities of XPath to put restrictions on the structure\n    and the content of XML documents.  Here is a simple example::\n\n      >>> schematron = Schematron(XML(\'\'\'\n      ... <schema xmlns="http://www.ascc.net/xml/schematron" >\n      ...   <pattern name="id is the only permitted attribute name">\n      ...     <rule context="*">\n      ...       <report test="@*[not(name()=\'id\')]">Attribute\n      ...         <name path="@*[not(name()=\'id\')]"/> is forbidden<name/>\n      ...       </report>\n      ...     </rule>\n      ...   </pattern>\n      ... </schema>\n      ... \'\'\'))\n\n      >>> xml = XML(\'\'\'\n      ... <AAA name="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC color="ccc"/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      0\n\n      >>> xml = XML(\'\'\'\n      ... <AAA id="aaa">\n      ...   <BBB id="bbb"/>\n      ...   <CCC/>\n      ... </AAA>\n      ... \'\'\')\n\n      >>> schematron.validate(xml)\n      1\n\n    Schematron was added to libxml2 in version 2.6.21.  Before version 2.6.32,\n    however, Schematron lacked support for error reporting other than to stderr.\n    This version is therefore required to retrieve validation warnings and\n    errors in lxml.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SchematronError(LxmlError):
    'Base class of all Schematron errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class of all Schematron errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SchematronParseError(SchematronError):
    'Error while parsing an XML document as Schematron schema.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while parsing an XML document as Schematron schema.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SchematronValidateError(SchematronError):
    'Error while validating an XML document with a Schematron schema.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while validating an XML document with a Schematron schema.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SerialisationError(LxmlError):
    'A libxml2 error that occurred during serialisation.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'A libxml2 error that occurred during serialisation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class SiblingsIterator(_ElementMatchIterator):
    'SiblingsIterator(self, node, tag=None, preceding=False)\n    Iterates over the siblings of an element.\n\n    You can pass the boolean keyword ``preceding`` to specify the direction.\n    '
    def __init__(self, node, tag=..., preceding=...) -> None:
        'SiblingsIterator(self, node, tag=None, preceding=False)\n    Iterates over the siblings of an element.\n\n    You can pass the boolean keyword ``preceding`` to specify the direction.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def SubElement(_parent, _tag, attrib, nsmap, **_extra) -> typing.Any:
    'SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra)\n\n    Subelement factory.  This function creates an element instance, and\n    appends it to an existing element.\n    '
    ...

class TreeBuilder(_SaxParserTarget):
    'TreeBuilder(self, element_factory=None, parser=None,\n                    comment_factory=None, pi_factory=None,\n                    insert_comments=True, insert_pis=True)\n\n    Parser target that builds a tree from parse event callbacks.\n\n    The factory arguments can be used to influence the creation of\n    elements, comments and processing instructions.\n\n    By default, comments and processing instructions are inserted into\n    the tree, but they can be ignored by passing the respective flags.\n\n    The final tree is returned by the ``close()`` method.\n    '
    def __init__(self, element_factory=..., parser=..., comment_factory=..., pi_factory=..., insert_comments=..., insert_pis=...) -> None:
        'TreeBuilder(self, element_factory=None, parser=None,\n                    comment_factory=None, pi_factory=None,\n                    insert_comments=True, insert_pis=True)\n\n    Parser target that builds a tree from parse event callbacks.\n\n    The factory arguments can be used to influence the creation of\n    elements, comments and processing instructions.\n\n    By default, comments and processing instructions are inserted into\n    the tree, but they can be ignored by passing the respective flags.\n\n    The final tree is returned by the ``close()`` method.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def close(self) -> typing.Any:
        'close(self)\n\n        Flushes the builder buffers, and returns the toplevel document\n        element.  Raises XMLSyntaxError on inconsistencies.\n        '
        ...
    
    def comment(self, comment) -> typing.Any:
        'comment(self, comment)\n\n        Creates a comment using the factory, appends it (unless disabled)\n        and returns it.\n        '
        ...
    
    def data(self, data) -> typing.Any:
        'data(self, data)\n\n        Adds text to the current element.  The value should be either an\n        8-bit string containing ASCII text, or a Unicode string.\n        '
        ...
    
    def end(self, tag) -> typing.Any:
        'end(self, tag)\n\n        Closes the current element.\n        '
        ...
    
    def pi(self, target, data) -> typing.Any:
        'pi(self, target, data=None)\n\n        Creates a processing instruction using the factory, appends it\n        (unless disabled) and returns it.\n        '
        ...
    
    def start(self, tag, attrs, nsmap) -> typing.Any:
        'start(self, tag, attrs, nsmap=None)\n\n        Opens a new element.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XInclude(_mod_builtins.object):
    'XInclude(self)\n    XInclude processor.\n\n    Create an instance and call it on an Element to run XInclude\n    processing.\n    '
    def __call__(self, node) -> typing.Any:
        '__call__(self, node)'
        ...
    
    def __init__(self) -> None:
        'XInclude(self)\n    XInclude processor.\n\n    Create an instance and call it on an Element to run XInclude\n    processing.\n    '
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
    def error_log(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XIncludeError(LxmlError):
    'Error during XInclude processing.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error during XInclude processing.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def XML(text, parser) -> typing.Any:
    'XML(text, parser=None, base_url=None)\n\n    Parses an XML document or fragment from a string constant.\n    Returns the root node (or the result returned by a parser target).\n    This function can be used to embed "XML literals" in Python code,\n    like in\n\n       >>> root = XML("<root><test/></root>")\n       >>> print(root.tag)\n       root\n\n    To override the parser with a different ``XMLParser`` you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    ...

def XMLDTDID(text, parser) -> typing.Any:
    'XMLDTDID(text, parser=None, base_url=None)\n\n    Parse the text and return a tuple (root node, ID dictionary).  The root\n    node is the same as returned by the XML() function.  The dictionary\n    contains string-element pairs.  The dictionary keys are the values of ID\n    attributes as defined by the DTD.  The elements referenced by the ID are\n    stored as dictionary values.\n\n    Note that you must not modify the XML tree if you use the ID dictionary.\n    The results are undefined.\n    '
    ...

def XMLID(text, parser) -> typing.Any:
    "XMLID(text, parser=None, base_url=None)\n\n    Parse the text and return a tuple (root node, ID dictionary).  The root\n    node is the same as returned by the XML() function.  The dictionary\n    contains string-element pairs.  The dictionary keys are the values of 'id'\n    attributes.  The elements referenced by the ID are stored as dictionary\n    values.\n    "
    ...

class XMLParser(_FeedParser):
    "XMLParser(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema =None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True)\n\n    The XML parser.\n\n    Parsers can be supplied as additional argument to various parse\n    functions of the lxml API.  A default parser is always available\n    and can be replaced by a call to the global function\n    'set_default_parser'.  New parsers can be created at any time\n    without a major run-time overhead.\n\n    The keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if DTD\n    validation or attribute default values are requested (unless you\n    additionally provide an XMLSchema from which the default\n    attributes can be read).\n\n    Available boolean keyword arguments:\n\n    - attribute_defaults - inject default attributes from DTD or XMLSchema\n    - dtd_validation     - validate against a DTD referenced by the document\n    - load_dtd           - use DTD for parsing\n    - no_network         - prevent network access for related files (default: True)\n    - ns_clean           - clean up redundant namespace declarations\n    - recover            - try hard to parse through broken XML\n    - remove_blank_text  - discard blank text nodes that appear ignorable\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True, always True with DTD validation)\n    - resolve_entities   - replace entities by their text value (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads.  While this is\n    not harmful, it is more efficient to use separate parsers.  This does not\n    apply to the default parser.\n    "
    def __init__(self, encoding=..., attribute_defaults=..., dtd_validation=..., load_dtd=..., no_network=..., ns_clean=..., recover=..., schema=..., huge_tree=..., remove_blank_text=..., resolve_entities=..., remove_comments=..., remove_pis=..., strip_cdata=..., collect_ids=..., target=..., compact=...) -> None:
        "XMLParser(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema =None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True)\n\n    The XML parser.\n\n    Parsers can be supplied as additional argument to various parse\n    functions of the lxml API.  A default parser is always available\n    and can be replaced by a call to the global function\n    'set_default_parser'.  New parsers can be created at any time\n    without a major run-time overhead.\n\n    The keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if DTD\n    validation or attribute default values are requested (unless you\n    additionally provide an XMLSchema from which the default\n    attributes can be read).\n\n    Available boolean keyword arguments:\n\n    - attribute_defaults - inject default attributes from DTD or XMLSchema\n    - dtd_validation     - validate against a DTD referenced by the document\n    - load_dtd           - use DTD for parsing\n    - no_network         - prevent network access for related files (default: True)\n    - ns_clean           - clean up redundant namespace declarations\n    - recover            - try hard to parse through broken XML\n    - remove_blank_text  - discard blank text nodes that appear ignorable\n    - remove_comments    - discard comments\n    - remove_pis         - discard processing instructions\n    - strip_cdata        - replace CDATA sections by normal text content (default: True)\n    - compact            - save memory for short text content (default: True)\n    - collect_ids        - use a hash table of XML IDs for fast access (default: True, always True with DTD validation)\n    - resolve_entities   - replace entities by their text value (default: True)\n    - huge_tree          - disable security restrictions and support very deep trees\n                           and very long text content (only affects libxml2 2.7+)\n\n    Other keyword arguments:\n\n    - encoding - override the document encoding\n    - target   - a parser target object that will receive the parse events\n    - schema   - an XMLSchema to validate against\n\n    Note that you should avoid sharing parsers between threads.  While this is\n    not harmful, it is more efficient to use separate parsers.  This does not\n    apply to the default parser.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLPullParser(XMLParser):
    "XMLPullParser(self, events=None, *, tag=None, **kwargs)\n\n    XML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
    def __init__(self, events=..., *, tag=..., **kwargs) -> None:
        "XMLPullParser(self, events=None, *, tag=None, **kwargs)\n\n    XML parser that collects parse events in an iterator.\n\n    The collected events are the same as for iterparse(), but the\n    parser itself is non-blocking in the sense that it receives\n    data chunks incrementally through its .feed() method, instead\n    of reading them directly from a file(-like) object all by itself.\n\n    By default, it collects Element end events.  To change that,\n    pass any subset of the available events into the ``events``\n    argument: ``'start'``, ``'end'``, ``'start-ns'``,\n    ``'end-ns'``, ``'comment'``, ``'pi'``.\n\n    To support loading external dependencies relative to the input\n    source, you can pass the ``base_url``.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def read_events(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSchema(_Validator):
    'XMLSchema(self, etree=None, file=None)\n    Turn a document into an XML Schema validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n\n    Passing the ``attribute_defaults`` boolean option will make the\n    schema insert default/fixed attributes into validated documents.\n    '
    def __call__(self, etree) -> typing.Any:
        '__call__(self, etree)\n\n        Validate doc using XML Schema.\n\n        Returns true if document is valid, false if not.\n        '
        ...
    
    def __init__(self, etree=..., file=...) -> None:
        'XMLSchema(self, etree=None, file=None)\n    Turn a document into an XML Schema validator.\n\n    Either pass a schema as Element or ElementTree, or pass a file or\n    filename through the ``file`` keyword argument.\n\n    Passing the ``attribute_defaults`` boolean option will make the\n    schema insert default/fixed attributes into validated documents.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSchemaError(LxmlError):
    'Base class of all XML Schema errors\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class of all XML Schema errors\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSchemaParseError(XMLSchemaError):
    'Error while parsing an XML document as XML Schema.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while parsing an XML document as XML Schema.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSchemaValidateError(XMLSchemaError):
    'Error while validating an XML document with an XML Schema.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error while validating an XML document with an XML Schema.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSyntaxAssertionError(XMLSyntaxError,_mod_builtins.AssertionError):
    '\n    An XMLSyntaxError that additionally inherits from AssertionError for\n    ElementTree / backwards compatibility reasons.\n\n    This class may get replaced by a plain XMLSyntaxError in a future version.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, message, code, line, column, filename) -> None:
        '\n    An XMLSyntaxError that additionally inherits from AssertionError for\n    ElementTree / backwards compatibility reasons.\n\n    This class may get replaced by a plain XMLSyntaxError in a future version.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XMLSyntaxError(ParseError):
    'Syntax error while parsing an XML document.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, message, code, line, column, filename) -> None:
        'Syntax error while parsing an XML document.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

XMLTreeBuilder: ETCompatXMLParser
class XPath(_XPathEvaluatorBase):
    "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
    def __call__(self, _etree_or_element, **_variables) -> typing.Any:
        '__call__(self, _etree_or_element, **_variables)'
        ...
    
    def __init__(self, path, namespaces=..., extensions=..., regexp=..., smart_strings=...) -> None:
        "XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    A compiled XPath expression that can be called on Elements and ElementTrees.\n\n    Besides the XPath expression, you can pass prefix-namespace\n    mappings and extension functions to the constructor through the\n    keyword arguments ``namespaces`` and ``extensions``.  EXSLT\n    regular expression support can be disabled with the 'regexp'\n    boolean keyword (defaults to True).  Smart strings will be\n    returned for string results unless you pass\n    ``smart_strings=False``.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def path(self) -> typing.Any:
        'The literal XPath expression.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathDocumentEvaluator(XPathElementEvaluator):
    "XPathDocumentEvaluator(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an ElementTree.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    def __call__(self, _path, **_variables) -> typing.Any:
        '__call__(self, _path, **_variables)\n\n        Evaluate an XPath expression on the document.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n        '
        ...
    
    def __init__(self, etree, namespaces=..., extensions=..., regexp=..., smart_strings=...) -> None:
        "XPathDocumentEvaluator(self, etree, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an ElementTree.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathElementEvaluator(_XPathEvaluatorBase):
    "XPathElementEvaluator(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an element.\n\n    Absolute XPath expressions (starting with '/') will be evaluated against\n    the ElementTree as returned by getroottree().\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    def __call__(self, _path, **_variables) -> typing.Any:
        "__call__(self, _path, **_variables)\n\n        Evaluate an XPath expression on the document.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n\n        Absolute XPath expressions (starting with '/') will be evaluated\n        against the ElementTree as returned by getroottree().\n        "
        ...
    
    def __init__(self, element, namespaces=..., extensions=..., regexp=..., smart_strings=...) -> None:
        "XPathElementEvaluator(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n    Create an XPath evaluator for an element.\n\n    Absolute XPath expressions (starting with '/') will be evaluated against\n    the ElementTree as returned by getroottree().\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def register_namespace(self, prefix, uri) -> typing.Any:
        'Register a namespace with the XPath context.\n        '
        ...
    
    def register_namespaces(self, namespaces) -> typing.Any:
        'Register a prefix -> uri dict.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathError(LxmlError):
    'Base class of all XPath errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class of all XPath errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathEvalError(XPathError):
    'Error during XPath evaluation.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error during XPath evaluation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def XPathEvaluator(etree_or_element) -> typing.Any:
    "XPathEvaluator(etree_or_element, namespaces=None, extensions=None, regexp=True, smart_strings=True)\n\n    Creates an XPath evaluator for an ElementTree or an Element.\n\n    The resulting object can be called with an XPath expression as argument\n    and XPath variables provided as keyword arguments.\n\n    Additional namespace declarations can be passed with the\n    'namespace' keyword argument.  EXSLT regular expression support\n    can be disabled with the 'regexp' boolean keyword (defaults to\n    True).  Smart strings will be returned for string results unless\n    you pass ``smart_strings=False``.\n    "
    ...

class XPathFunctionError(XPathEvalError):
    'Internal error looking up an XPath extension function.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Internal error looking up an XPath extension function.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathResultError(XPathEvalError):
    'Error handling an XPath result.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error handling an XPath result.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XPathSyntaxError(LxmlSyntaxError,XPathError):
    __dict__: typing.Dict[str, typing.Any]
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
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLT(_mod_builtins.object):
    'XSLT(self, xslt_input, extensions=None, regexp=True, access_control=None)\n\n    Turn an XSL document into an XSLT object.\n\n    Calling this object on a tree or Element will execute the XSLT::\n\n        transform = etree.XSLT(xsl_tree)\n        result = transform(xml_tree)\n\n    Keyword arguments of the constructor:\n\n    - extensions: a dict mapping ``(namespace, name)`` pairs to\n      extension functions or extension elements\n    - regexp: enable exslt regular expression support in XPath\n      (default: True)\n    - access_control: access restrictions for network or file\n      system (see `XSLTAccessControl`)\n\n    Keyword arguments of the XSLT call:\n\n    - profile_run: enable XSLT profiling (default: False)\n\n    Other keyword arguments of the call are passed to the stylesheet\n    as parameters.\n    '
    def __call__(self, _input, profile_run=..., **kw) -> typing.Any:
        '__call__(self, _input, profile_run=False, **kw)\n\n        Execute the XSL transformation on a tree or Element.\n\n        Pass the ``profile_run`` option to get profile information\n        about the XSLT.  The result of the XSLT will have a property\n        xslt_profile that holds an XML tree with profiling data.\n        '
        ...
    
    def __copy__(self) -> typing.Any:
        ...
    
    def __deepcopy__(self, memo) -> typing.Any:
        ...
    
    def __init__(self, xslt_input, extensions=..., regexp=..., access_control=...) -> None:
        'XSLT(self, xslt_input, extensions=None, regexp=True, access_control=None)\n\n    Turn an XSL document into an XSLT object.\n\n    Calling this object on a tree or Element will execute the XSLT::\n\n        transform = etree.XSLT(xsl_tree)\n        result = transform(xml_tree)\n\n    Keyword arguments of the constructor:\n\n    - extensions: a dict mapping ``(namespace, name)`` pairs to\n      extension functions or extension elements\n    - regexp: enable exslt regular expression support in XPath\n      (default: True)\n    - access_control: access restrictions for network or file\n      system (see `XSLTAccessControl`)\n\n    Keyword arguments of the XSLT call:\n\n    - profile_run: enable XSLT profiling (default: False)\n\n    Other keyword arguments of the call are passed to the stylesheet\n    as parameters.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def apply(self, _input, **kw) -> typing.Any:
        'apply(self, _input,  profile_run=False, **kw)\n        \n        :deprecated: call the object, not this method.'
        ...
    
    @property
    def error_log(self) -> typing.Any:
        'The log of errors and warnings of an XSLT execution.'
        ...
    
    def set_global_max_depth(self, max_depth) -> typing.Any:
        'set_global_max_depth(max_depth)\n\n        The maximum traversal depth that the stylesheet engine will allow.\n        This does not only count the template recursion depth but also takes\n        the number of variables/parameters into account.  The required setting\n        for a run depends on both the stylesheet and the input data.\n\n        Example::\n\n            XSLT.set_global_max_depth(5000)\n\n        Note that this is currently a global, module-wide setting because\n        libxslt does not support it at a per-stylesheet level.\n        '
        ...
    
    def strparam(self, strval) -> typing.Any:
        'strparam(strval)\n\n        Mark an XSLT string parameter that requires quote escaping\n        before passing it into the transformation.  Use it like this::\n\n            result = transform(doc, some_strval = XSLT.strparam(\n                \'\'\'it\'s "Monty Python\'s" ...\'\'\'))\n\n        Escaped string parameters can be reused without restriction.\n        '
        ...
    
    def tostring(self, result_tree) -> typing.Any:
        'tostring(self, result_tree)\n\n        Save result doc to string based on stylesheet output method.\n\n        :deprecated: use str(result_tree) instead.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTAccessControl(_mod_builtins.object):
    'XSLTAccessControl(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True)\n\n    Access control for XSLT: reading/writing files, directories and\n    network I/O.  Access to a type of resource is granted or denied by\n    passing any of the following boolean keyword arguments.  All of\n    them default to True to allow access.\n\n    - read_file\n    - write_file\n    - create_dir\n    - read_network\n    - write_network\n\n    For convenience, there is also a class member `DENY_ALL` that\n    provides an XSLTAccessControl instance that is readily configured\n    to deny everything, and a `DENY_WRITE` member that denies all\n    write access but allows read access.\n\n    See `XSLT`.\n    '
    DENY_ALL: XSLTAccessControl
    DENY_WRITE: XSLTAccessControl
    def __init__(self, read_file=..., write_file=..., create_dir=..., read_network=..., write_network=...) -> None:
        'XSLTAccessControl(self, read_file=True, write_file=True, create_dir=True, read_network=True, write_network=True)\n\n    Access control for XSLT: reading/writing files, directories and\n    network I/O.  Access to a type of resource is granted or denied by\n    passing any of the following boolean keyword arguments.  All of\n    them default to True to allow access.\n\n    - read_file\n    - write_file\n    - create_dir\n    - read_network\n    - write_network\n\n    For convenience, there is also a class member `DENY_ALL` that\n    provides an XSLTAccessControl instance that is readily configured\n    to deny everything, and a `DENY_WRITE` member that denies all\n    write access but allows read access.\n\n    See `XSLT`.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def options(self) -> typing.Any:
        'The access control configuration as a map of options.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTApplyError(XSLTError):
    'Error running an XSL transformation.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error running an XSL transformation.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTError(LxmlError):
    'Base class of all XSLT errors.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Base class of all XSLT errors.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTExtension(_mod_builtins.object):
    'Base class of an XSLT extension element.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Base class of an XSLT extension element.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def apply_templates(self, context, node, output_parent) -> typing.Any:
        'apply_templates(self, context, node, output_parent=None, elements_only=False, remove_blank_text=False)\n\n        Call this method to retrieve the result of applying templates\n        to an element.\n\n        The return value is a list of elements or text strings that\n        were generated by the XSLT processor.  If you pass\n        ``elements_only=True``, strings will be discarded from the result\n        list.  The option ``remove_blank_text=True`` will only discard\n        strings that consist entirely of whitespace (e.g. formatting).\n        These options do not apply to Elements, only to bare string results.\n\n        If you pass an Element as `output_parent` parameter, the result\n        will instead be appended to the element (including attributes\n        etc.) and the return value will be `None`.  This is a safe way\n        to generate content into the output document directly, without\n        having to take care of special values like text or attributes.\n        Note that the string discarding options will be ignored in this\n        case.\n        '
        ...
    
    def execute(self, context, self_node, input_node, output_parent) -> typing.Any:
        'execute(self, context, self_node, input_node, output_parent)\n        Execute this extension element.\n\n        Subclasses must override this method.  They may append\n        elements to the `output_parent` element here, or set its text\n        content.  To this end, the `input_node` provides read-only\n        access to the current node in the input document, and the\n        `self_node` points to the extension element in the stylesheet.\n\n        Note that the `output_parent` parameter may be `None` if there\n        is no parent element in the current context (e.g. no content\n        was added to the output tree yet).\n        '
        ...
    
    def process_children(self, context, output_parent) -> typing.Any:
        'process_children(self, context, output_parent=None, elements_only=False, remove_blank_text=False)\n\n        Call this method to process the XSLT content of the extension\n        element itself.\n\n        The return value is a list of elements or text strings that\n        were generated by the XSLT processor.  If you pass\n        ``elements_only=True``, strings will be discarded from the result\n        list.  The option ``remove_blank_text=True`` will only discard\n        strings that consist entirely of whitespace (e.g. formatting).\n        These options do not apply to Elements, only to bare string results.\n\n        If you pass an Element as `output_parent` parameter, the result\n        will instead be appended to the element (including attributes\n        etc.) and the return value will be `None`.  This is a safe way\n        to generate content into the output document directly, without\n        having to take care of special values like text or attributes.\n        Note that the string discarding options will be ignored in this\n        case.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTExtensionError(XSLTError):
    'Error registering an XSLT extension.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error registering an XSLT extension.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTParseError(XSLTError):
    'Error parsing a stylesheet document.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error parsing a stylesheet document.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class XSLTSaveError(XSLTError,SerialisationError):
    'Error serialising an XSLT result.\n    '
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        'Error serialising an XSLT result.\n    '
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
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Attrib(_mod_builtins.object):
    'A dict-like proxy for the ``Element.attrib`` property.\n    '
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __copy__(self) -> typing.Any:
        ...
    
    def __deepcopy__(self, memo) -> typing.Any:
        ...
    
    def __delitem__(self, key) -> None:
        'Delete self[key].'
        ...
    
    def __eq__(self, value) -> bool:
        'Return self==value.'
        ...
    
    def __ge__(self, value) -> bool:
        'Return self>=value.'
        ...
    
    def __getitem__(self, key) -> typing.Any:
        'Return self[key].'
        ...
    
    def __gt__(self, value) -> bool:
        'Return self>value.'
        ...
    
    __hash__: typing.Any
    def __init__(self, *args, **kwargs) -> None:
        'A dict-like proxy for the ``Element.attrib`` property.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _Attrib:
        'Implement iter(self).'
        ...
    
    def __le__(self, value) -> bool:
        'Return self<=value.'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
        ...
    
    def __lt__(self, value) -> bool:
        'Return self<value.'
        ...
    
    def __ne__(self, value) -> bool:
        'Return self!=value.'
        ...
    
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    def __setitem__(self, key, value) -> None:
        'Set self[key] to value.'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def clear(self) -> typing.Any:
        ...
    
    def get(self, key, default) -> typing.Any:
        ...
    
    def has_key(self, key) -> typing.Any:
        ...
    
    def items(self) -> typing.Any:
        ...
    
    def iteritems(self) -> typing.Any:
        ...
    
    def iterkeys(self) -> typing.Any:
        ...
    
    def itervalues(self) -> typing.Any:
        ...
    
    def keys(self) -> typing.Any:
        ...
    
    def pop(self, key, *default) -> typing.Any:
        ...
    
    def update(self, sequence_or_dict) -> typing.Any:
        ...
    
    def values(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _BaseErrorLog(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def copy(self) -> typing.Any:
        ...
    
    @property
    def last_error(self) -> typing.Any:
        ...
    
    def receive(self, entry) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Comment(__ContentOnlyElement):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def tag(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Document(_mod_builtins.object):
    'Internal base class to reference a libxml document.\n\n    When instances of this class are garbage collected, the libxml\n    document is cleaned up.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'Internal base class to reference a libxml document.\n\n    When instances of this class are garbage collected, the libxml\n    document is cleaned up.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _DomainErrorLog(_ErrorLog):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def receive(self, entry) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Element(_mod_builtins.object):
    'Element class.\n\n    References a document object and a libxml node.\n\n    By pointing to a Document instance, a reference is kept to\n    _Document as long as there is some pointer to a node in it.\n    '
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    def __contains__(self, value: typing.Any) -> bool:
        '__contains__(self, element)'
        ...
    
    def __copy__(self) -> typing.Any:
        '__copy__(self)'
        ...
    
    def __deepcopy__(self, memo) -> typing.Any:
        '__deepcopy__(self, memo)'
        ...
    
    def __delitem__(self, x) -> None:
        '__delitem__(self, x)\n\n        Deletes the given subelement or a slice.\n        '
        ...
    
    def __getitem__(self, index: int) -> typing.Any:
        'Returns the subelement at the given position or the requested\n        slice.\n        '
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        'Element class.\n\n    References a document object and a libxml node.\n\n    By pointing to a Document instance, a reference is kept to\n    _Document as long as there is some pointer to a node in it.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _Element:
        '__iter__(self)'
        ...
    
    def __len__(self) -> int:
        '__len__(self)\n\n        Returns the number of subelements.\n        '
        ...
    
    def __repr__(self) -> str:
        '__repr__(self)'
        ...
    
    def __reversed__(self) -> typing.Any:
        '__reversed__(self)'
        ...
    
    def __setitem__(self, index: typing.Any, value: typing.Any) -> None:
        '__setitem__(self, x, value)\n\n        Replaces the given subelement index or slice.\n        '
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _init(self) -> typing.Any:
        '_init(self)\n\n        Called after object initialisation.  Custom subclasses may override\n        this if they recursively call _init() in the superclasses.\n        '
        ...
    
    def addnext(self, element) -> typing.Any:
        'addnext(self, element)\n\n        Adds the element as a following sibling directly after this\n        element.\n\n        This is normally used to set a processing instruction or comment after\n        the root node of a document.  Note that tail text is automatically\n        discarded when adding at the root level.\n        '
        ...
    
    def addprevious(self, element) -> typing.Any:
        'addprevious(self, element)\n\n        Adds the element as a preceding sibling directly before this\n        element.\n\n        This is normally used to set a processing instruction or comment\n        before the root node of a document.  Note that tail text is\n        automatically discarded when adding at the root level.\n        '
        ...
    
    def append(self, element) -> typing.Any:
        'append(self, element)\n\n        Adds a subelement to the end of this element.\n        '
        ...
    
    @property
    def attrib(self) -> typing.Any:
        'Element attribute dictionary. Where possible, use get(), set(),\n        keys(), values() and items() to access element attributes.\n        '
        ...
    
    @property
    def base(self) -> typing.Any:
        'The base URI of the Element (xml:base or HTML base URL).\n        None if the base URI is unknown.\n\n        Note that the value depends on the URL of the document that\n        holds the Element if there is no xml:base attribute on the\n        Element or its ancestors.\n\n        Setting this property will set an xml:base attribute on the\n        Element, regardless of the document type (XML or HTML).\n        '
        ...
    
    def clear(self, keep_tail) -> typing.Any:
        'clear(self, keep_tail=False)\n\n        Resets an element.  This function removes all subelements, clears\n        all attributes and sets the text and tail properties to None.\n\n        Pass ``keep_tail=True`` to leave the tail text untouched.\n        '
        ...
    
    def cssselect(self, expr) -> typing.Any:
        '\n        Run the CSS expression on this element and its children,\n        returning a list of the results.\n\n        Equivalent to lxml.cssselect.CSSSelect(expr)(self) -- note\n        that pre-compiling the expression can provide a substantial\n        speedup.\n        '
        ...
    
    def extend(self, elements) -> typing.Any:
        'extend(self, elements)\n\n        Extends the current children by the elements in the iterable.\n        '
        ...
    
    def find(self, path, namespaces) -> typing.Any:
        'find(self, path, namespaces=None)\n\n        Finds the first matching subelement, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def findall(self, path, namespaces) -> typing.Any:
        'findall(self, path, namespaces=None)\n\n        Finds all matching subelements, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def findtext(self, path, default, namespaces) -> typing.Any:
        'findtext(self, path, default=None, namespaces=None)\n\n        Finds text for the first matching subelement, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def get(self, key, default) -> typing.Any:
        'get(self, key, default=None)\n\n        Gets an element attribute.\n        '
        ...
    
    def getchildren(self) -> typing.Any:
        'getchildren(self)\n\n        Returns all direct children.  The elements are returned in document\n        order.\n\n        :deprecated: Note that this method has been deprecated as of\n          ElementTree 1.3 and lxml 2.0.  New code should use\n          ``list(element)`` or simply iterate over elements.\n        '
        ...
    
    def getiterator(self, tag, *tags) -> typing.Any:
        'getiterator(self, tag=None, *tags)\n\n        Returns a sequence or iterator of all elements in the subtree in\n        document order (depth first pre-order), starting with this\n        element.\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n\n        :deprecated: Note that this method is deprecated as of\n          ElementTree 1.3 and lxml 2.0.  It returns an iterator in\n          lxml, which diverges from the original ElementTree\n          behaviour.  If you want an efficient iterator, use the\n          ``element.iter()`` method instead.  You should only use this\n          method in new code if you require backwards compatibility\n          with older versions of lxml or ElementTree.\n        '
        ...
    
    def getnext(self) -> typing.Any:
        'getnext(self)\n\n        Returns the following sibling of this element or None.\n        '
        ...
    
    def getparent(self) -> typing.Any:
        'getparent(self)\n\n        Returns the parent of this element or None for the root element.\n        '
        ...
    
    def getprevious(self) -> typing.Any:
        'getprevious(self)\n\n        Returns the preceding sibling of this element or None.\n        '
        ...
    
    def getroottree(self) -> typing.Any:
        'getroottree(self)\n\n        Return an ElementTree for the root node of the document that\n        contains this element.\n\n        This is the same as following element.getparent() up the tree until it\n        returns None (for the root element) and then build an ElementTree for\n        the last parent that was returned.'
        ...
    
    def index(self, child, start, stop) -> typing.Any:
        'index(self, child, start=None, stop=None)\n\n        Find the position of the child within the parent.\n\n        This method is not part of the original ElementTree API.\n        '
        ...
    
    def insert(self, index, element) -> typing.Any:
        'insert(self, index, element)\n\n        Inserts a subelement at the given position in this element\n        '
        ...
    
    def items(self) -> typing.Any:
        'items(self)\n\n        Gets element attributes, as a sequence. The attributes are returned in\n        an arbitrary order.\n        '
        ...
    
    def iter(self, tag, *tags) -> typing.Any:
        'iter(self, tag=None, *tags)\n\n        Iterate over all elements in the subtree in document order (depth\n        first pre-order), starting with this element.\n\n        Can be restricted to find only elements with specific tags:\n        pass ``"{ns}localname"`` as tag. Either or both of ``ns`` and\n        ``localname`` can be ``*`` for a wildcard; ``ns`` can be empty\n        for no namespace. ``"localname"`` is equivalent to ``"{}localname"``\n        (i.e. no namespace) but ``"*"`` is ``"{*}*"`` (any or no namespace),\n        not ``"{}*"``.\n\n        You can also pass the Element, Comment, ProcessingInstruction and\n        Entity factory functions to look only for the specific element type.\n\n        Passing multiple tags (or a sequence of tags) instead of a single tag\n        will let the iterator return all elements matching any of these tags,\n        in document order.\n        '
        ...
    
    def iterancestors(self, tag, *tags) -> typing.Any:
        'iterancestors(self, tag=None, *tags)\n\n        Iterate over the ancestors of this element (from parent to parent).\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n        '
        ...
    
    def iterchildren(self, tag, *tags) -> typing.Any:
        "iterchildren(self, tag=None, *tags, reversed=False)\n\n        Iterate over the children of this element.\n\n        As opposed to using normal iteration on this element, the returned\n        elements can be reversed with the 'reversed' keyword and restricted\n        to find only elements with specific tags, see `iter`.\n        "
        ...
    
    def iterdescendants(self, tag, *tags) -> typing.Any:
        'iterdescendants(self, tag=None, *tags)\n\n        Iterate over the descendants of this element in document order.\n\n        As opposed to ``el.iter()``, this iterator does not yield the element\n        itself.  The returned elements can be restricted to find only elements\n        with specific tags, see `iter`.\n        '
        ...
    
    def iterfind(self, path, namespaces) -> typing.Any:
        'iterfind(self, path, namespaces=None)\n\n        Iterates over all matching subelements, by tag name or path.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def itersiblings(self, tag, *tags) -> typing.Any:
        "itersiblings(self, tag=None, *tags, preceding=False)\n\n        Iterate over the following or preceding siblings of this element.\n\n        The direction is determined by the 'preceding' keyword which\n        defaults to False, i.e. forward iteration over the following\n        siblings.  When True, the iterator yields the preceding\n        siblings in reverse document order, i.e. starting right before\n        the current element and going backwards.\n\n        Can be restricted to find only elements with specific tags,\n        see `iter`.\n        "
        ...
    
    def itertext(self, tag, *tags) -> typing.Any:
        'itertext(self, tag=None, *tags, with_tail=True)\n\n        Iterates over the text content of a subtree.\n\n        You can pass tag names to restrict text content to specific elements,\n        see `iter`.\n\n        You can set the ``with_tail`` keyword argument to ``False`` to skip\n        over tail text.\n        '
        ...
    
    def keys(self) -> typing.Any:
        'keys(self)\n\n        Gets a list of attribute names.  The names are returned in an\n        arbitrary order (just like for an ordinary Python dictionary).\n        '
        ...
    
    def makeelement(self, _tag, attrib, nsmap, **_extra) -> typing.Any:
        'makeelement(self, _tag, attrib=None, nsmap=None, **_extra)\n\n        Creates a new element associated with the same document.\n        '
        ...
    
    @property
    def nsmap(self) -> typing.Any:
        'Namespace prefix->URI mapping known in the context of this\n        Element.  This includes all namespace declarations of the\n        parents.\n\n        Note that changing the returned dict has no effect on the Element.\n        '
        ...
    
    @property
    def prefix(self) -> typing.Any:
        'Namespace prefix or None.\n        '
        ...
    
    def remove(self, element) -> typing.Any:
        'remove(self, element)\n\n        Removes a matching subelement. Unlike the find methods, this\n        method compares elements based on identity, not on tag value\n        or contents.\n        '
        ...
    
    def replace(self, old_element, new_element) -> typing.Any:
        'replace(self, old_element, new_element)\n\n        Replaces a subelement with the element passed as second argument.\n        '
        ...
    
    def set(self, key, value) -> typing.Any:
        'set(self, key, value)\n\n        Sets an element attribute.\n        '
        ...
    
    @property
    def sourceline(self) -> typing.Any:
        'Original line number as found by the parser or None if unknown.\n        '
        ...
    
    @property
    def tag(self) -> typing.Any:
        'Element tag\n        '
        ...
    
    @property
    def tail(self) -> typing.Any:
        "Text after this element's end tag, but before the next sibling\n        element's start tag. This is either a string or the value None, if\n        there was no text.\n        "
        ...
    
    @property
    def text(self) -> typing.Any:
        'Text before the first subelement. This is either a string or\n        the value None, if there was no text.\n        '
        ...
    
    def values(self) -> typing.Any:
        'values(self)\n\n        Gets element attribute values as a sequence of strings.  The\n        attributes are returned in an arbitrary order.\n        '
        ...
    
    def xpath(self, _path, **_variables) -> typing.Any:
        'xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)\n\n        Evaluate an xpath expression using the element as context node.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementIterator(_ElementTagMatcher):
    '\n    Dead but public. :)\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Dead but public. :)\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _ElementIterator:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementMatchIterator(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _ElementMatchIterator:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementStringResult(_mod_builtins.bytes):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @classmethod
    def fromhex(cls, type, string) -> typing.Any:
        "Create a bytes object from a string of hexadecimal numbers.\n\nSpaces between two numbers are accepted.\nExample: bytes.fromhex('B9 01EF') -> b'\\\\xb9\\\\x01\\\\xef'."
        ...
    
    def getparent(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementTagMatcher(_mod_builtins.object):
    '\n    Dead but public. :)\n    '
    def __init__(self, *args, **kwargs) -> None:
        '\n    Dead but public. :)\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementTree(_mod_builtins.object):
    def __copy__(self) -> typing.Any:
        ...
    
    def __deepcopy__(self, memo) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _setroot(self, root) -> typing.Any:
        '_setroot(self, root)\n\n        Relocate the ElementTree to a new root node.\n        '
        ...
    
    @property
    def docinfo(self) -> typing.Any:
        'Information about the document provided by parser and DTD.'
        ...
    
    def find(self, path, namespaces) -> typing.Any:
        'find(self, path, namespaces=None)\n\n        Finds the first toplevel element with given tag.  Same as\n        ``tree.getroot().find(path)``.\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def findall(self, path, namespaces) -> typing.Any:
        'findall(self, path, namespaces=None)\n\n        Finds all elements matching the ElementPath expression.  Same as\n        getroot().findall(path).\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def findtext(self, path, default, namespaces) -> typing.Any:
        'findtext(self, path, default=None, namespaces=None)\n\n        Finds the text for the first element matching the ElementPath\n        expression.  Same as getroot().findtext(path)\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def getelementpath(self, element) -> typing.Any:
        'getelementpath(self, element)\n\n        Returns a structural, absolute ElementPath expression to find the\n        element.  This path can be used in the .find() method to look up\n        the element, provided that the elements along the path and their\n        list of immediate children were not modified in between.\n\n        ElementPath has the advantage over an XPath expression (as returned\n        by the .getpath() method) that it does not require additional prefix\n        declarations.  It is always self-contained.\n        '
        ...
    
    def getiterator(self, tag, *tags) -> typing.Any:
        'getiterator(self, *tags, tag=None)\n\n        Returns a sequence or iterator of all elements in document order\n        (depth first pre-order), starting with the root element.\n\n        Can be restricted to find only elements with specific tags,\n        see `_Element.iter`.\n\n        :deprecated: Note that this method is deprecated as of\n          ElementTree 1.3 and lxml 2.0.  It returns an iterator in\n          lxml, which diverges from the original ElementTree\n          behaviour.  If you want an efficient iterator, use the\n          ``tree.iter()`` method instead.  You should only use this\n          method in new code if you require backwards compatibility\n          with older versions of lxml or ElementTree.\n        '
        ...
    
    def getpath(self, element) -> typing.Any:
        'getpath(self, element)\n\n        Returns a structural, absolute XPath expression to find the element.\n\n        For namespaced elements, the expression uses prefixes from the\n        document, which therefore need to be provided in order to make any\n        use of the expression in XPath.\n\n        Also see the method getelementpath(self, element), which returns a\n        self-contained ElementPath expression.\n        '
        ...
    
    def getroot(self) -> typing.Any:
        'getroot(self)\n\n        Gets the root element for this tree.\n        '
        ...
    
    def iter(self, tag, *tags) -> typing.Any:
        'iter(self, tag=None, *tags)\n\n        Creates an iterator for the root element.  The iterator loops over\n        all elements in this tree, in document order.  Note that siblings\n        of the root element (comments or processing instructions) are not\n        returned by the iterator.\n\n        Can be restricted to find only elements with specific tags,\n        see `_Element.iter`.\n        '
        ...
    
    def iterfind(self, path, namespaces) -> typing.Any:
        'iterfind(self, path, namespaces=None)\n\n        Iterates over all elements matching the ElementPath expression.\n        Same as getroot().iterfind(path).\n\n        The optional ``namespaces`` argument accepts a\n        prefix-to-namespace mapping that allows the usage of XPath\n        prefixes in the path expression.\n        '
        ...
    
    def parse(self, source, parser) -> typing.Any:
        'parse(self, source, parser=None, base_url=None)\n\n        Updates self with the content of source and returns its root.\n        '
        ...
    
    @property
    def parser(self) -> typing.Any:
        'The parser that was used to parse the document in this ElementTree.\n        '
        ...
    
    def relaxng(self, relaxng) -> typing.Any:
        'relaxng(self, relaxng)\n\n        Validate this document using other document.\n\n        The relaxng argument is a tree that should contain a Relax NG schema.\n\n        Returns True or False, depending on whether validation\n        succeeded.\n\n        Note: if you are going to apply the same Relax NG schema against\n        multiple documents, it is more efficient to use the RelaxNG\n        class directly.\n        '
        ...
    
    def write(self, file) -> typing.Any:
        'write(self, file, encoding=None, method="xml",\n                  pretty_print=False, xml_declaration=None, with_tail=True,\n                  standalone=None, doctype=None, compression=0,\n                  exclusive=False, inclusive_ns_prefixes=None,\n                  with_comments=True, strip_text=False)\n\n        Write the tree to a filename, file or file-like object.\n\n        Defaults to ASCII encoding and writing a declaration as needed.\n\n        The keyword argument \'method\' selects the output method:\n        \'xml\', \'html\', \'text\' or \'c14n\'.  Default is \'xml\'.\n\n        With ``method="c14n"`` (C14N version 1), the options ``exclusive``,\n        ``with_comments`` and ``inclusive_ns_prefixes`` request exclusive\n        C14N, include comments, and list the inclusive prefixes respectively.\n\n        With ``method="c14n2"`` (C14N version 2), the ``with_comments`` and\n        ``strip_text`` options control the output of comments and text space\n        according to C14N 2.0.\n\n        Passing a boolean value to the ``standalone`` option will\n        output an XML declaration with the corresponding\n        ``standalone`` flag.\n\n        The ``doctype`` option allows passing in a plain string that will\n        be serialised before the XML tree.  Note that passing in non\n        well-formed content here will make the XML output non well-formed.\n        Also, an existing doctype in the document tree will not be removed\n        when serialising an ElementTree instance.\n\n        The ``compression`` option enables GZip compression level 1-9.\n\n        The ``inclusive_ns_prefixes`` should be a list of namespace strings\n        (i.e. [\'xs\', \'xsi\']) that will be promoted to the top-level element\n        during exclusive C14N serialisation.  This parameter is ignored if\n        exclusive mode=False.\n\n        If exclusive=True and no list is provided, a namespace will only be\n        rendered if it is used by the immediate parent or one of its attributes\n        and its prefix and values have not already been rendered by an ancestor\n        of the namespace node\'s parent element.\n        '
        ...
    
    def write_c14n(self, file) -> typing.Any:
        'write_c14n(self, file, exclusive=False, with_comments=True,\n                       compression=0, inclusive_ns_prefixes=None)\n\n        C14N write of document. Always writes UTF-8.\n\n        The ``compression`` option enables GZip compression level 1-9.\n\n        The ``inclusive_ns_prefixes`` should be a list of namespace strings\n        (i.e. [\'xs\', \'xsi\']) that will be promoted to the top-level element\n        during exclusive C14N serialisation.  This parameter is ignored if\n        exclusive mode=False.\n\n        If exclusive=True and no list is provided, a namespace will only be\n        rendered if it is used by the immediate parent or one of its attributes\n        and its prefix and values have not already been rendered by an ancestor\n        of the namespace node\'s parent element.\n\n        NOTE: This method is deprecated as of lxml 4.4 and will be removed in a\n        future release.  Use ``.write(f, method="c14n")`` instead.\n        '
        ...
    
    def xinclude(self) -> typing.Any:
        'xinclude(self)\n\n        Process the XInclude nodes in this document and include the\n        referenced XML fragments.\n\n        There is support for loading files through the file system, HTTP and\n        FTP.\n\n        Note that XInclude does not support custom resolvers in Python space\n        due to restrictions of libxml2 <= 2.6.29.\n        '
        ...
    
    def xmlschema(self, xmlschema) -> typing.Any:
        'xmlschema(self, xmlschema)\n\n        Validate this document using other document.\n\n        The xmlschema argument is a tree that should contain an XML Schema.\n\n        Returns True or False, depending on whether validation\n        succeeded.\n\n        Note: If you are going to apply the same XML Schema against\n        multiple documents, it is more efficient to use the XMLSchema\n        class directly.\n        '
        ...
    
    def xpath(self, _path, **_variables) -> typing.Any:
        'xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)\n\n        XPath evaluate in context of document.\n\n        ``namespaces`` is an optional dictionary with prefix to namespace URI\n        mappings, used by XPath.  ``extensions`` defines additional extension\n        functions.\n\n        Returns a list (nodeset), or bool, float or string.\n\n        In case of a list result, return Element for element nodes,\n        string for text and attribute values.\n\n        Note: if you are going to apply multiple XPath expressions\n        against the same document, it is more efficient to use\n        XPathEvaluator directly.\n        '
        ...
    
    def xslt(self, _xslt, extensions, access_control, **_kw) -> typing.Any:
        'xslt(self, _xslt, extensions=None, access_control=None, **_kw)\n\n        Transform this document using other document.\n\n        xslt is a tree that should be XSLT\n        keyword parameters are XSLT transformation parameters.\n\n        Returns the transformed tree.\n\n        Note: if you are going to apply the same XSLT stylesheet against\n        multiple documents, it is more efficient to use the XSLT\n        class directly.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ElementUnicodeResult(_mod_builtins.str):
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
    
    @property
    def attrname(self) -> typing.Any:
        ...
    
    def getparent(self) -> typing.Any:
        ...
    
    @property
    def is_attribute(self) -> typing.Any:
        ...
    
    @property
    def is_tail(self) -> typing.Any:
        ...
    
    @property
    def is_text(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Entity(__ContentOnlyElement):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def name(self) -> typing.Any:
        ...
    
    @property
    def tag(self) -> typing.Any:
        ...
    
    @property
    def text(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ErrorLog(_ListErrorLog):
    def __exit__(self, *args) -> typing.Any:
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _ErrorLog:
        'Implement iter(self).'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def clear(self) -> typing.Any:
        ...
    
    def copy(self) -> typing.Any:
        'Creates a shallow copy of this error log and the list of entries.\n        '
        ...
    
    def receive(self, entry) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _FeedParser(_BaseParser):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def close(self) -> typing.Any:
        'close(self)\n\n        Terminates feeding data to this parser.  This tells the parser to\n        process any remaining data in the feed buffer, and then returns the\n        root Element of the tree that was parsed.\n\n        This method must be called after passing the last chunk of data into\n        the ``feed()`` method.  It should only be called when using the feed\n        parser interface, all other usage is undefined.\n        '
        ...
    
    def feed(self, data) -> typing.Any:
        'feed(self, data)\n\n        Feeds data to the parser.  The argument should be an 8-bit string\n        buffer containing encoded data, although Unicode is supported as long\n        as both string types are not mixed.\n\n        This is the main entry point to the consumer interface of a\n        parser.  The parser will parse as much of the XML stream as it\n        can on each call.  To finish parsing or to reset the parser,\n        call the ``close()`` method.  Both methods may raise\n        ParseError if errors occur in the input data.  If an error is\n        raised, there is no longer a need to call ``close()``.\n\n        The feed parser interface is independent of the normal parser\n        usage.  You can use the same parser as a feed parser and in\n        the ``parse()`` function concurrently.\n        '
        ...
    
    @property
    def feed_error_log(self) -> typing.Any:
        'The error log of the last (or current) run of the feed parser.\n\n        Note that this is local to the feed parser and thus is\n        different from what the ``error_log`` property returns.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _IDDict(_mod_builtins.object):
    "IDDict(self, etree)\n    A dictionary-like proxy class that mapps ID attributes to elements.\n\n    The dictionary must be instantiated with the root element of a parsed XML\n    document, otherwise the behaviour is undefined.  Elements and XML trees\n    that were created or modified 'by hand' are not supported.\n    "
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __getitem__(self, key) -> typing.Any:
        'Return self[key].'
        ...
    
    def __init__(self, etree) -> None:
        "IDDict(self, etree)\n    A dictionary-like proxy class that mapps ID attributes to elements.\n\n    The dictionary must be instantiated with the root element of a parsed XML\n    document, otherwise the behaviour is undefined.  Elements and XML trees\n    that were created or modified 'by hand' are not supported.\n    "
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _IDDict:
        'Implement iter(self).'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def copy(self) -> typing.Any:
        ...
    
    def get(self, id_name) -> typing.Any:
        ...
    
    def has_key(self, id_name) -> typing.Any:
        ...
    
    def items(self) -> typing.Any:
        ...
    
    def iteritems(self) -> typing.Any:
        ...
    
    def iterkeys(self) -> typing.Any:
        ...
    
    def itervalues(self) -> typing.Any:
        ...
    
    def keys(self) -> typing.Any:
        ...
    
    def values(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ListErrorLog(_BaseErrorLog):
    'Immutable base version of a list based error log.'
    def __bool__(self) -> bool:
        'self != 0'
        ...
    
    def __contains__(self, key) -> bool:
        'Return key in self.'
        ...
    
    def __getitem__(self, key) -> typing.Any:
        'Return self[key].'
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        'Immutable base version of a list based error log.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> _ListErrorLog:
        'Implement iter(self).'
        ...
    
    def __len__(self) -> int:
        'Return len(self).'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def copy(self) -> typing.Any:
        'Creates a shallow copy of this error log.  Reuses the list of\n        entries.\n        '
        ...
    
    def filter_domains(self, domains) -> typing.Any:
        'Filter the errors by the given domains and return a new error log\n        containing the matches.\n        '
        ...
    
    def filter_from_errors(self) -> typing.Any:
        'filter_from_errors(self)\n\n        Convenience method to get all error messages or worse.\n        '
        ...
    
    def filter_from_fatals(self) -> typing.Any:
        'filter_from_fatals(self)\n\n        Convenience method to get all fatal error messages.\n        '
        ...
    
    def filter_from_level(self, level) -> typing.Any:
        'filter_from_level(self, level)\n\n        Return a log with all messages of the requested level of worse.\n        '
        ...
    
    def filter_from_warnings(self) -> typing.Any:
        'filter_from_warnings(self)\n\n        Convenience method to get all warnings or worse.\n        '
        ...
    
    def filter_levels(self, levels) -> typing.Any:
        'filter_levels(self, levels)\n\n        Filter the errors by the given error levels and return a new\n        error log containing the matches.\n        '
        ...
    
    def filter_types(self, types) -> typing.Any:
        'filter_types(self, types)\n\n        Filter the errors by the given types and return a new error\n        log containing the matches.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _LogEntry(_mod_builtins.object):
    'A log message entry from an error log.\n\n    Attributes:\n\n    - message: the message text\n    - domain: the domain ID (see lxml.etree.ErrorDomains)\n    - type: the message type ID (see lxml.etree.ErrorTypes)\n    - level: the log level ID (see lxml.etree.ErrorLevels)\n    - line: the line at which the message originated (if applicable)\n    - column: the character column at which the message originated (if applicable)\n    - filename: the name of the file in which the message originated (if applicable)\n    - path: the location in which the error was found (if available)\n    '
    def __init__(self, *args, **kwargs) -> None:
        'A log message entry from an error log.\n\n    Attributes:\n\n    - message: the message text\n    - domain: the domain ID (see lxml.etree.ErrorDomains)\n    - type: the message type ID (see lxml.etree.ErrorTypes)\n    - level: the log level ID (see lxml.etree.ErrorLevels)\n    - line: the line at which the message originated (if applicable)\n    - column: the character column at which the message originated (if applicable)\n    - filename: the name of the file in which the message originated (if applicable)\n    - path: the location in which the error was found (if available)\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def column(self) -> typing.Any:
        ...
    
    @property
    def domain(self) -> typing.Any:
        ...
    
    @property
    def domain_name(self) -> typing.Any:
        'The name of the error domain.  See lxml.etree.ErrorDomains\n        '
        ...
    
    @property
    def filename(self) -> typing.Any:
        'The file path where the report originated, if any.\n        '
        ...
    
    @property
    def level(self) -> typing.Any:
        ...
    
    @property
    def level_name(self) -> typing.Any:
        'The name of the error level.  See lxml.etree.ErrorLevels\n        '
        ...
    
    @property
    def line(self) -> typing.Any:
        ...
    
    @property
    def message(self) -> typing.Any:
        'The log message string.\n        '
        ...
    
    @property
    def path(self) -> typing.Any:
        'The XPath for the node where the error was detected.\n        '
        ...
    
    @property
    def type(self) -> typing.Any:
        ...
    
    @property
    def type_name(self) -> typing.Any:
        'The name of the error type.  See lxml.etree.ErrorTypes\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _ProcessingInstruction(__ContentOnlyElement):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __repr__(self) -> str:
        'Return repr(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def attrib(self) -> typing.Any:
        'Returns a dict containing all pseudo-attributes that can be\n        parsed from the text content of this processing instruction.\n        Note that modifying the dict currently has no effect on the\n        XML node, although this is not guaranteed to stay this way.\n        '
        ...
    
    def get(self, key, default) -> typing.Any:
        'get(self, key, default=None)\n\n        Try to parse pseudo-attributes from the text content of the\n        processing instruction, search for one with the given key as\n        name and return its associated value.\n\n        Note that this is only a convenience method for the most\n        common case that all text content is structured in\n        attribute-like name-value pairs with properly quoted values.\n        It is not guaranteed to work for all possible text content.\n        '
        ...
    
    @property
    def tag(self) -> typing.Any:
        ...
    
    @property
    def target(self) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _RotatingErrorLog(_ErrorLog):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def receive(self, entry) -> typing.Any:
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _SaxParserTarget(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _TargetParserResult(_mod_builtins.Exception):
    __dict__: typing.Dict[str, typing.Any]
    def __init__(self, result) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def __weakref__(self) -> typing.Any:
        'list of weak references to the object (if defined)'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _Validator(_mod_builtins.object):
    'Base class for XML validators.'
    def __init__(self, *args, **kwargs) -> None:
        'Base class for XML validators.'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def _append_log_message(self, domain, type, level, line, message, filename) -> typing.Any:
        ...
    
    def _clear_error_log(self) -> typing.Any:
        ...
    
    def assertValid(self, etree) -> typing.Any:
        'assertValid(self, etree)\n\n        Raises `DocumentInvalid` if the document does not comply with the schema.\n        '
        ...
    
    def assert_(self, etree) -> typing.Any:
        'assert_(self, etree)\n\n        Raises `AssertionError` if the document does not comply with the schema.\n        '
        ...
    
    @property
    def error_log(self) -> typing.Any:
        'The log of validation errors and warnings.'
        ...
    
    def validate(self, etree) -> typing.Any:
        'validate(self, etree)\n\n        Validate the document using this schema.\n\n        Returns true if document is valid, false if not.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _XPathEvaluatorBase(_mod_builtins.object):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def error_log(self) -> typing.Any:
        ...
    
    def evaluate(self, _eval_arg, **_variables) -> typing.Any:
        'evaluate(self, _eval_arg, **_variables)\n\n        Evaluate an XPath expression.\n\n        Instead of calling this method, you can also call the evaluator object\n        itself.\n\n        Variables may be provided as keyword arguments.  Note that namespaces\n        are currently not supported for variables.\n\n        :deprecated: call the object, not its method.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _XSLTProcessingInstruction(PIBase):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def parseXSL(self, parser) -> typing.Any:
        'parseXSL(self, parser=None)\n\n        Try to parse the stylesheet referenced by this PI and return\n        an ElementTree for it.  If the stylesheet is embedded in the\n        same document (referenced via xml:id), find and return an\n        ElementTree for the stylesheet Element.\n\n        The optional ``parser`` keyword argument can be passed to specify the\n        parser used to read from external stylesheet URLs.\n        '
        ...
    
    def set(self, key, value) -> typing.Any:
        "set(self, key, value)\n\n        Supports setting the 'href' pseudo-attribute in the text of\n        the processing instruction.\n        "
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class _XSLTResultTree(_ElementTree):
    'The result of an XSLT evaluation.\n\n    Use ``str()`` or ``bytes()`` (or ``unicode()`` in Python 2.x) to serialise to a string,\n    and the ``.write_output()`` method to write serialise to a file.\n    '
    def __init__(self, *args, **kwargs) -> None:
        'The result of an XSLT evaluation.\n\n    Use ``str()`` or ``bytes()`` (or ``unicode()`` in Python 2.x) to serialise to a string,\n    and the ``.write_output()`` method to write serialise to a file.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __pyx_vtable__: PyCapsule
    def __str__(self) -> str:
        'Return str(self).'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __unicode__(self) -> typing.Any:
        ...
    
    def write_output(self, file) -> typing.Any:
        'write_output(self, file, *, compression=0)\n\n        Serialise the XSLT output to a file or file-like object.\n\n        As opposed to the generic ``.write()`` method, ``.write_output()`` serialises\n        the result as defined by the ``<xsl:output>`` tag.\n        '
        ...
    
    @property
    def xslt_profile(self) -> typing.Any:
        'Return an ElementTree with profiling data for the stylesheet run.\n        '
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__all__: list
__doc__: str
__docformat__: str
__file__: str
__name__: str
__package__: str
__pyx_capi__: dict
__test__: dict
__version__: str
def adopt_external_document(capsule, parser) -> typing.Any:
    'adopt_external_document(capsule, parser=None)\n\n    Unpack a libxml2 document pointer from a PyCapsule and wrap it in an\n    lxml ElementTree object.\n\n    This allows external libraries to build XML/HTML trees using libxml2\n    and then pass them efficiently into lxml for further processing.\n\n    If a ``parser`` is provided, it will be used for configuring the\n    lxml document.  No parsing will be done.\n\n    The capsule must have the name ``"libxml2:xmlDoc"`` and its pointer\n    value must reference a correct libxml2 document of type ``xmlDoc*``.\n    The creator of the capsule must take care to correctly clean up the\n    document using an appropriate capsule destructor.  By default, the\n    libxml2 document will be copied to let lxml safely own the memory\n    of the internal tree that it uses.\n\n    If the capsule context is non-NULL, it must point to a C string that\n    can be compared using ``strcmp()``.  If the context string equals\n    ``"destructor:xmlFreeDoc"``, the libxml2 document will not be copied\n    but the capsule invalidated instead by clearing its destructor and\n    name.  That way, lxml takes ownership of the libxml2 document in memory\n    without creating a copy first, and the capsule destructor will not be\n    called.  The document will then eventually be cleaned up by lxml using\n    the libxml2 API function ``xmlFreeDoc()`` once it is no longer used.\n\n    If no copy is made, later modifications of the tree outside of lxml\n    should not be attempted after transferring the ownership.\n    '
    ...

def canonicalize(xml_data, **options) -> typing.Any:
    'Convert XML to its C14N 2.0 serialised form.\n\n    If *out* is provided, it must be a file or file-like object that receives\n    the serialised canonical XML output (text, not bytes) through its ``.write()``\n    method.  To write to a file, open it in text mode with encoding "utf-8".\n    If *out* is not provided, this function returns the output as text string.\n\n    Either *xml_data* (an XML string, tree or Element) or *file*\n    (a file path or file-like object) must be provided as input.\n\n    The configuration options are the same as for the ``C14NWriterTarget``.\n    '
    ...

def cleanup_namespaces(tree_or_element, top_nsmap, keep_ns_prefixes) -> typing.Any:
    "cleanup_namespaces(tree_or_element, top_nsmap=None, keep_ns_prefixes=None)\n\n    Remove all namespace declarations from a subtree that are not used\n    by any of the elements or attributes in that tree.\n\n    If a 'top_nsmap' is provided, it must be a mapping from prefixes\n    to namespace URIs.  These namespaces will be declared on the top\n    element of the subtree before running the cleanup, which allows\n    moving namespace declarations to the top of the tree.\n\n    If a 'keep_ns_prefixes' is provided, it must be a list of prefixes.\n    These prefixes will not be removed as part of the cleanup.\n    "
    ...

def clear_error_log() -> typing.Any:
    'clear_error_log()\n\n    Clear the global error log.  Note that this log is already bound to a\n    fixed size.\n\n    Note: since lxml 2.2, the global error log is local to a thread\n    and this function will only clear the global error log of the\n    current thread.\n    '
    ...

def dump(elem) -> typing.Any:
    'dump(elem, pretty_print=True, with_tail=True)\n\n    Writes an element tree or element structure to sys.stdout. This function\n    should be used for debugging only.\n    '
    ...

def fromstring(text, parser) -> typing.Any:
    'fromstring(text, parser=None, base_url=None)\n\n    Parses an XML document or fragment from a string.  Returns the\n    root node (or the result returned by a parser target).\n\n    To override the default parser with a different parser you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    '
    ...

def fromstringlist(strings, parser) -> typing.Any:
    'fromstringlist(strings, parser=None)\n\n    Parses an XML document from a sequence of strings.  Returns the\n    root node (or the result returned by a parser target).\n\n    To override the default parser with a different parser you can pass it to\n    the ``parser`` keyword argument.\n    '
    ...

def get_default_parser() -> typing.Any:
    'get_default_parser()'
    ...

class htmlfile(xmlfile):
    'htmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental HTML serialisation.  Works the same as\n    xmlfile.\n    '
    def __init__(self, output_file, encoding=..., compression=..., close=..., buffered=...) -> None:
        'htmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental HTML serialisation.  Works the same as\n    xmlfile.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def indent(tree, space) -> typing.Any:
    'indent(tree, space="  ", level=0)\n\n    Indent an XML document by inserting newlines and indentation space\n    after elements.\n\n    *tree* is the ElementTree or Element to modify.  The (root) element\n    itself will not be changed, but the tail text of all elements in its\n    subtree will be adapted.\n\n    *space* is the whitespace to insert for each indentation level, two\n    space characters by default.\n\n    *level* is the initial indentation level. Setting this to a higher\n    value than 0 can be used for indenting subtrees that are more deeply\n    nested inside of a document.\n    '
    ...

def iselement(element) -> typing.Any:
    'iselement(element)\n\n    Checks if an object appears to be a valid element object.\n    '
    ...

class iterparse(_mod_builtins.object):
    'iterparse(self, source, events=("end",), tag=None,                   attribute_defaults=False, dtd_validation=False,                   load_dtd=False, no_network=True, remove_blank_text=False,                   remove_comments=False, remove_pis=False, encoding=None,                   html=False, recover=None, huge_tree=False, schema=None)\n\n    Incremental parser.\n\n    Parses XML into a tree and generates tuples (event, element) in a\n    SAX-like fashion. ``event`` is any of \'start\', \'end\', \'start-ns\',\n    \'end-ns\'.\n\n    For \'start\' and \'end\', ``element`` is the Element that the parser just\n    found opening or closing.  For \'start-ns\', it is a tuple (prefix, URI) of\n    a new namespace declaration.  For \'end-ns\', it is simply None.  Note that\n    all start and end events are guaranteed to be properly nested.\n\n    The keyword argument ``events`` specifies a sequence of event type names\n    that should be generated.  By default, only \'end\' events will be\n    generated.\n\n    The additional ``tag`` argument restricts the \'start\' and \'end\' events to\n    those elements that match the given tag.  The ``tag`` argument can also be\n    a sequence of tags to allow matching more than one tag.  By default,\n    events are generated for all elements.  Note that the \'start-ns\' and\n    \'end-ns\' events are not impacted by this restriction.\n\n    The other keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if validation or\n    attribute default values are requested.\n\n    Available boolean keyword arguments:\n     - attribute_defaults: read default attributes from DTD\n     - dtd_validation: validate (if DTD is available)\n     - load_dtd: use DTD for parsing\n     - no_network: prevent network access for related files\n     - remove_blank_text: discard blank text nodes\n     - remove_comments: discard comments\n     - remove_pis: discard processing instructions\n     - strip_cdata: replace CDATA sections by normal text content (default: True)\n     - compact: safe memory for short text content (default: True)\n     - resolve_entities: replace entities by their text value (default: True)\n     - huge_tree: disable security restrictions and support very deep trees\n                  and very long text content (only affects libxml2 2.7+)\n     - html: parse input as HTML (default: XML)\n     - recover: try hard to parse through broken input (default: True for HTML,\n                False otherwise)\n\n    Other keyword arguments:\n     - encoding: override the document encoding\n     - schema: an XMLSchema to validate against\n    '
    def __init__(self, source, events=..., tag=..., attribute_defaults=..., dtd_validation=..., load_dtd=..., no_network=..., remove_blank_text=..., remove_comments=..., remove_pis=..., encoding=..., html=..., recover=..., huge_tree=..., schema=...) -> None:
        'iterparse(self, source, events=("end",), tag=None,                   attribute_defaults=False, dtd_validation=False,                   load_dtd=False, no_network=True, remove_blank_text=False,                   remove_comments=False, remove_pis=False, encoding=None,                   html=False, recover=None, huge_tree=False, schema=None)\n\n    Incremental parser.\n\n    Parses XML into a tree and generates tuples (event, element) in a\n    SAX-like fashion. ``event`` is any of \'start\', \'end\', \'start-ns\',\n    \'end-ns\'.\n\n    For \'start\' and \'end\', ``element`` is the Element that the parser just\n    found opening or closing.  For \'start-ns\', it is a tuple (prefix, URI) of\n    a new namespace declaration.  For \'end-ns\', it is simply None.  Note that\n    all start and end events are guaranteed to be properly nested.\n\n    The keyword argument ``events`` specifies a sequence of event type names\n    that should be generated.  By default, only \'end\' events will be\n    generated.\n\n    The additional ``tag`` argument restricts the \'start\' and \'end\' events to\n    those elements that match the given tag.  The ``tag`` argument can also be\n    a sequence of tags to allow matching more than one tag.  By default,\n    events are generated for all elements.  Note that the \'start-ns\' and\n    \'end-ns\' events are not impacted by this restriction.\n\n    The other keyword arguments in the constructor are mainly based on the\n    libxml2 parser configuration.  A DTD will also be loaded if validation or\n    attribute default values are requested.\n\n    Available boolean keyword arguments:\n     - attribute_defaults: read default attributes from DTD\n     - dtd_validation: validate (if DTD is available)\n     - load_dtd: use DTD for parsing\n     - no_network: prevent network access for related files\n     - remove_blank_text: discard blank text nodes\n     - remove_comments: discard comments\n     - remove_pis: discard processing instructions\n     - strip_cdata: replace CDATA sections by normal text content (default: True)\n     - compact: safe memory for short text content (default: True)\n     - resolve_entities: replace entities by their text value (default: True)\n     - huge_tree: disable security restrictions and support very deep trees\n                  and very long text content (only affects libxml2 2.7+)\n     - html: parse input as HTML (default: XML)\n     - recover: try hard to parse through broken input (default: True for HTML,\n                False otherwise)\n\n    Other keyword arguments:\n     - encoding: override the document encoding\n     - schema: an XMLSchema to validate against\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> iterparse:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def error_log(self) -> typing.Any:
        'The error log of the last (or current) parser run.\n        '
        ...
    
    def makeelement(self, _tag, attrib, nsmap, **_extra) -> typing.Any:
        'makeelement(self, _tag, attrib=None, nsmap=None, **_extra)\n\n        Creates a new element associated with this parser.\n        '
        ...
    
    @property
    def resolvers(self) -> typing.Any:
        'The custom resolver registry of the last (or current) parser run.\n        '
        ...
    
    @property
    def root(self) -> typing.Any:
        ...
    
    def set_element_class_lookup(self, lookup) -> typing.Any:
        'set_element_class_lookup(self, lookup = None)\n\n        Set a lookup scheme for element classes generated from this parser.\n\n        Reset it by passing None or nothing.\n        '
        ...
    
    @property
    def version(self) -> typing.Any:
        'The version of the underlying XML parser.'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

class iterwalk(_mod_builtins.object):
    'iterwalk(self, element_or_tree, events=("end",), tag=None)\n\n    A tree walker that generates events from an existing tree as if it\n    was parsing XML data with ``iterparse()``.\n\n    Just as for ``iterparse()``, the ``tag`` argument can be a single tag or a\n    sequence of tags.\n\n    After receiving a \'start\' or \'start-ns\' event, the children and\n    descendants of the current element can be excluded from iteration\n    by calling the ``skip_subtree()`` method.\n    '
    def __init__(self, element_or_tree, events=..., tag=...) -> None:
        'iterwalk(self, element_or_tree, events=("end",), tag=None)\n\n    A tree walker that generates events from an existing tree as if it\n    was parsing XML data with ``iterparse()``.\n\n    Just as for ``iterparse()``, the ``tag`` argument can be a single tag or a\n    sequence of tags.\n\n    After receiving a \'start\' or \'start-ns\' event, the children and\n    descendants of the current element can be excluded from iteration\n    by calling the ``skip_subtree()`` method.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    def __iter__(self) -> iterwalk:
        'Implement iter(self).'
        ...
    
    def __next__(self) -> typing.Any:
        ...
    
    __pyx_vtable__: PyCapsule
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def skip_subtree(self) -> typing.Any:
        "Prevent descending into the current subtree.\n        Instead, the next returned event will be the 'end' event of the current element\n        (if included), ignoring any children or descendants.\n\n        This has no effect right after an 'end' or 'end-ns' event.\n        "
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

memory_debugger: _MemDebug
def open(file, mode, buffering, encoding, errors, newline, closefd, opener) -> typing.Any:
    'Open file and return a stream.  Raise OSError upon failure.\n\nfile is either a text or byte string giving the name (and the path\nif the file isn\'t in the current working directory) of the file to\nbe opened or an integer file descriptor of the file to be\nwrapped. (If a file descriptor is given, it is closed when the\nreturned I/O object is closed, unless closefd is set to False.)\n\nmode is an optional string that specifies the mode in which the file\nis opened. It defaults to \'r\' which means open for reading in text\nmode.  Other common values are \'w\' for writing (truncating the file if\nit already exists), \'x\' for creating and writing to a new file, and\n\'a\' for appending (which on some Unix systems, means that all writes\nappend to the end of the file regardless of the current seek position).\nIn text mode, if encoding is not specified the encoding used is platform\ndependent: locale.getpreferredencoding(False) is called to get the\ncurrent locale encoding. (For reading and writing raw bytes use binary\nmode and leave encoding unspecified.) The available modes are:\n\n========= ===============================================================\nCharacter Meaning\n--------- ---------------------------------------------------------------\n\'r\'       open for reading (default)\n\'w\'       open for writing, truncating the file first\n\'x\'       create a new file and open it for writing\n\'a\'       open for writing, appending to the end of the file if it exists\n\'b\'       binary mode\n\'t\'       text mode (default)\n\'+\'       open a disk file for updating (reading and writing)\n\'U\'       universal newline mode (deprecated)\n========= ===============================================================\n\nThe default mode is \'rt\' (open for reading text). For binary random\naccess, the mode \'w+b\' opens and truncates the file to 0 bytes, while\n\'r+b\' opens the file without truncation. The \'x\' mode implies \'w\' and\nraises an `FileExistsError` if the file already exists.\n\nPython distinguishes between files opened in binary and text modes,\neven when the underlying operating system doesn\'t. Files opened in\nbinary mode (appending \'b\' to the mode argument) return contents as\nbytes objects without any decoding. In text mode (the default, or when\n\'t\' is appended to the mode argument), the contents of the file are\nreturned as strings, the bytes having been first decoded using a\nplatform-dependent encoding or using the specified encoding if given.\n\n\'U\' mode is deprecated and will raise an exception in future versions\nof Python.  It has no effect in Python 3.  Use newline to control\nuniversal newlines mode.\n\nbuffering is an optional integer used to set the buffering policy.\nPass 0 to switch buffering off (only allowed in binary mode), 1 to select\nline buffering (only usable in text mode), and an integer > 1 to indicate\nthe size of a fixed-size chunk buffer.  When no buffering argument is\ngiven, the default buffering policy works as follows:\n\n* Binary files are buffered in fixed-size chunks; the size of the buffer\n  is chosen using a heuristic trying to determine the underlying device\'s\n  "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.\n  On many systems, the buffer will typically be 4096 or 8192 bytes long.\n\n* "Interactive" text files (files for which isatty() returns True)\n  use line buffering.  Other text files use the policy described above\n  for binary files.\n\nencoding is the name of the encoding used to decode or encode the\nfile. This should only be used in text mode. The default encoding is\nplatform dependent, but any encoding supported by Python can be\npassed.  See the codecs module for the list of supported encodings.\n\nerrors is an optional string that specifies how encoding errors are to\nbe handled---this argument should not be used in binary mode. Pass\n\'strict\' to raise a ValueError exception if there is an encoding error\n(the default of None has the same effect), or pass \'ignore\' to ignore\nerrors. (Note that ignoring encoding errors can lead to data loss.)\nSee the documentation for codecs.register or run \'help(codecs.Codec)\'\nfor a list of the permitted encoding error strings.\n\nnewline controls how universal newlines works (it only applies to text\nmode). It can be None, \'\', \'\\n\', \'\\r\', and \'\\r\\n\'.  It works as\nfollows:\n\n* On input, if newline is None, universal newlines mode is\n  enabled. Lines in the input can end in \'\\n\', \'\\r\', or \'\\r\\n\', and\n  these are translated into \'\\n\' before being returned to the\n  caller. If it is \'\', universal newline mode is enabled, but line\n  endings are returned to the caller untranslated. If it has any of\n  the other legal values, input lines are only terminated by the given\n  string, and the line ending is returned to the caller untranslated.\n\n* On output, if newline is None, any \'\\n\' characters written are\n  translated to the system default line separator, os.linesep. If\n  newline is \'\' or \'\\n\', no translation takes place. If newline is any\n  of the other legal values, any \'\\n\' characters written are translated\n  to the given string.\n\nIf closefd is False, the underlying file descriptor will be kept open\nwhen the file is closed. This does not work when a file name is given\nand must be True in that case.\n\nA custom opener can be used by passing a callable as *opener*. The\nunderlying file descriptor for the file object is then obtained by\ncalling *opener* with (*file*, *flags*). *opener* must return an open\nfile descriptor (passing os.open as *opener* results in functionality\nsimilar to passing None).\n\nopen() returns a file object whose type depends on the mode, and\nthrough which the standard file operations such as reading and writing\nare performed. When open() is used to open a file in a text mode (\'w\',\n\'r\', \'wt\', \'rt\', etc.), it returns a TextIOWrapper. When used to open\na file in a binary mode, the returned class varies: in read binary\nmode, it returns a BufferedReader; in write binary and append binary\nmodes, it returns a BufferedWriter, and in read/write mode, it returns\na BufferedRandom.\n\nIt is also possible to use a string or bytearray as a file for both\nreading and writing. For strings StringIO can be used like a file\nopened in a text mode, and for bytes a BytesIO can be used like a file\nopened in a binary mode.'
    ...

def parse(source, parser) -> typing.Any:
    'parse(source, parser=None, base_url=None)\n\n    Return an ElementTree object loaded with source elements.  If no parser\n    is provided as second argument, the default parser is used.\n\n    The ``source`` can be any of the following:\n\n    - a file name/path\n    - a file object\n    - a file-like object\n    - a URL using the HTTP or FTP protocol\n\n    To parse from a string, use the ``fromstring()`` function instead.\n\n    Note that it is generally faster to parse from a file path or URL\n    than from an open file object or file-like object.  Transparent\n    decompression from gzip compressed sources is supported (unless\n    explicitly disabled in libxml2).\n\n    The ``base_url`` keyword allows setting a URL for the document\n    when parsing from a file-like object.  This is needed when looking\n    up external entities (DTD, XInclude, ...) with relative paths.\n    '
    ...

def parseid(source, parser) -> typing.Any:
    'parseid(source, parser=None)\n\n    Parses the source into a tuple containing an ElementTree object and an\n    ID dictionary.  If no parser is provided as second argument, the default\n    parser is used.\n\n    Note that you must not modify the XML tree if you use the ID dictionary.\n    The results are undefined.\n    '
    ...

def register_namespace(prefix, uri) -> typing.Any:
    'Registers a namespace prefix that newly created Elements in that\n    namespace will use.  The registry is global, and any existing\n    mapping for either the given prefix or the namespace URI will be\n    removed.\n    '
    ...

def set_default_parser(parser) -> typing.Any:
    'set_default_parser(parser=None)\n\n    Set a default parser for the current thread.  This parser is used\n    globally whenever no parser is supplied to the various parse functions of\n    the lxml API.  If this function is called without a parser (or if it is\n    None), the default parser is reset to the original configuration.\n\n    Note that the pre-installed default parser is not thread-safe.  Avoid the\n    default parser in multi-threaded environments.  You can create a separate\n    parser for each thread explicitly or use a parser pool.\n    '
    ...

def set_element_class_lookup(lookup) -> typing.Any:
    'set_element_class_lookup(lookup = None)\n\n    Set the global default element class lookup method.\n    '
    ...

def strip_attributes(tree_or_element, *attribute_names) -> typing.Any:
    "strip_attributes(tree_or_element, *attribute_names)\n\n    Delete all attributes with the provided attribute names from an\n    Element (or ElementTree) and its descendants.\n\n    Attribute names can contain wildcards as in `_Element.iter`.\n\n    Example usage::\n\n        strip_attributes(root_element,\n                         'simpleattr',\n                         '{http://some/ns}attrname',\n                         '{http://other/ns}*')\n    "
    ...

def strip_elements(tree_or_element, *tag_names) -> typing.Any:
    "strip_elements(tree_or_element, *tag_names, with_tail=True)\n\n    Delete all elements with the provided tag names from a tree or\n    subtree.  This will remove the elements and their entire subtree,\n    including all their attributes, text content and descendants.  It\n    will also remove the tail text of the element unless you\n    explicitly set the ``with_tail`` keyword argument option to False.\n\n    Tag names can contain wildcards as in `_Element.iter`.\n\n    Note that this will not delete the element (or ElementTree root\n    element) that you passed even if it matches.  It will only treat\n    its descendants.  If you want to include the root element, check\n    its tag name directly before even calling this function.\n\n    Example usage::\n\n        strip_elements(some_element,\n            'simpletagname',             # non-namespaced tag\n            '{http://some/ns}tagname',   # namespaced tag\n            '{http://some/other/ns}*'    # any tag from a namespace\n            lxml.etree.Comment           # comments\n            )\n    "
    ...

def strip_tags(tree_or_element, *tag_names) -> typing.Any:
    "strip_tags(tree_or_element, *tag_names)\n\n    Delete all elements with the provided tag names from a tree or\n    subtree.  This will remove the elements and their attributes, but\n    *not* their text/tail content or descendants.  Instead, it will\n    merge the text content and children of the element into its\n    parent.\n\n    Tag names can contain wildcards as in `_Element.iter`.\n\n    Note that this will not delete the element (or ElementTree root\n    element) that you passed even if it matches.  It will only treat\n    its descendants.\n\n    Example usage::\n\n        strip_tags(some_element,\n            'simpletagname',             # non-namespaced tag\n            '{http://some/ns}tagname',   # namespaced tag\n            '{http://some/other/ns}*'    # any tag from a namespace\n            Comment                      # comments (including their text!)\n            )\n    "
    ...

def tostring(element_or_tree) -> typing.Any:
    'tostring(element_or_tree, encoding=None, method="xml",\n                 xml_declaration=None, pretty_print=False, with_tail=True,\n                 standalone=None, doctype=None,\n                 exclusive=False, inclusive_ns_prefixes=None,\n                 with_comments=True, strip_text=False,\n                 )\n\n    Serialize an element to an encoded string representation of its XML\n    tree.\n\n    Defaults to ASCII encoding without XML declaration.  This\n    behaviour can be configured with the keyword arguments \'encoding\'\n    (string) and \'xml_declaration\' (bool).  Note that changing the\n    encoding to a non UTF-8 compatible encoding will enable a\n    declaration by default.\n\n    You can also serialise to a Unicode string without declaration by\n    passing the name ``\'unicode\'`` as encoding (or the ``str`` function\n    in Py3 or ``unicode`` in Py2).  This changes the return value from\n    a byte string to an unencoded unicode string.\n\n    The keyword argument \'pretty_print\' (bool) enables formatted XML.\n\n    The keyword argument \'method\' selects the output method: \'xml\',\n    \'html\', plain \'text\' (text content without tags), \'c14n\' or \'c14n2\'.\n    Default is \'xml\'.\n\n    With ``method="c14n"`` (C14N version 1), the options ``exclusive``,\n    ``with_comments`` and ``inclusive_ns_prefixes`` request exclusive\n    C14N, include comments, and list the inclusive prefixes respectively.\n\n    With ``method="c14n2"`` (C14N version 2), the ``with_comments`` and\n    ``strip_text`` options control the output of comments and text space\n    according to C14N 2.0.\n\n    Passing a boolean value to the ``standalone`` option will output\n    an XML declaration with the corresponding ``standalone`` flag.\n\n    The ``doctype`` option allows passing in a plain string that will\n    be serialised before the XML tree.  Note that passing in non\n    well-formed content here will make the XML output non well-formed.\n    Also, an existing doctype in the document tree will not be removed\n    when serialising an ElementTree instance.\n\n    You can prevent the tail text of the element from being serialised\n    by passing the boolean ``with_tail`` option.  This has no impact\n    on the tail text of children, which will always be serialised.\n    '
    ...

def tostringlist(element_or_tree, *args, **kwargs) -> typing.Any:
    'tostringlist(element_or_tree, *args, **kwargs)\n\n    Serialize an element to an encoded string representation of its XML\n    tree, stored in a list of partial strings.\n\n    This is purely for ElementTree 1.3 compatibility.  The result is a\n    single string wrapped in a list.\n    '
    ...

def tounicode(element_or_tree) -> typing.Any:
    'tounicode(element_or_tree, method="xml", pretty_print=False,\n                  with_tail=True, doctype=None)\n\n    Serialize an element to the Python unicode representation of its XML\n    tree.\n\n    :deprecated: use ``tostring(el, encoding=\'unicode\')`` instead.\n\n    Note that the result does not carry an XML encoding declaration and is\n    therefore not necessarily suited for serialization to byte streams without\n    further treatment.\n\n    The boolean keyword argument \'pretty_print\' enables formatted XML.\n\n    The keyword argument \'method\' selects the output method: \'xml\',\n    \'html\' or plain \'text\'.\n\n    You can prevent the tail text of the element from being serialised\n    by passing the boolean ``with_tail`` option.  This has no impact\n    on the tail text of children, which will always be serialised.\n    '
    ...

def use_global_python_log(log) -> typing.Any:
    'use_global_python_log(log)\n\n    Replace the global error log by an etree.PyErrorLog that uses the\n    standard Python logging package.\n\n    Note that this disables access to the global error log from exceptions.\n    Parsers, XSLT etc. will continue to provide their normal local error log.\n\n    Note: prior to lxml 2.2, this changed the error log globally.\n    Since lxml 2.2, the global error log is local to a thread and this\n    function will only set the global error log of the current thread.\n    '
    ...

class xmlfile(_mod_builtins.object):
    'xmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental XML serialisation.\n\n    Usage example::\n\n         with xmlfile("somefile.xml", encoding=\'utf-8\') as xf:\n             xf.write_declaration(standalone=True)\n             xf.write_doctype(\'<!DOCTYPE root SYSTEM "some.dtd">\')\n\n             # generate an element (the root element)\n             with xf.element(\'root\'):\n                  # write a complete Element into the open root element\n                  xf.write(etree.Element(\'test\'))\n\n                  # generate and write more Elements, e.g. through iterparse\n                  for element in generate_some_elements():\n                      # serialise generated elements into the XML file\n                      xf.write(element)\n\n                  # or write multiple Elements or strings at once\n                  xf.write(etree.Element(\'start\'), "text", etree.Element(\'end\'))\n\n    If \'output_file\' is a file(-like) object, passing ``close=True`` will\n    close it when exiting the context manager.  By default, it is left\n    to the owner to do that.  When a file path is used, lxml will take care\n    of opening and closing the file itself.  Also, when a compression level\n    is set, lxml will deliberately close the file to make sure all data gets\n    compressed and written.\n\n    Setting ``buffered=False`` will flush the output after each operation,\n    such as opening or closing an ``xf.element()`` block or calling\n    ``xf.write()``.  Alternatively, calling ``xf.flush()`` can be used to\n    explicitly flush any pending output when buffering is enabled.\n    '
    def __aenter__(self) -> typing.Any:
        ...
    
    def __aexit__(self, exc_type, exc_val, exc_tb) -> typing.Any:
        ...
    
    def __enter__(self) -> typing.Any:
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> typing.Any:
        ...
    
    def __init__(self, output_file, encoding=..., compression=..., close=..., buffered=...) -> None:
        'xmlfile(self, output_file, encoding=None, compression=None, close=False, buffered=True)\n\n    A simple mechanism for incremental XML serialisation.\n\n    Usage example::\n\n         with xmlfile("somefile.xml", encoding=\'utf-8\') as xf:\n             xf.write_declaration(standalone=True)\n             xf.write_doctype(\'<!DOCTYPE root SYSTEM "some.dtd">\')\n\n             # generate an element (the root element)\n             with xf.element(\'root\'):\n                  # write a complete Element into the open root element\n                  xf.write(etree.Element(\'test\'))\n\n                  # generate and write more Elements, e.g. through iterparse\n                  for element in generate_some_elements():\n                      # serialise generated elements into the XML file\n                      xf.write(element)\n\n                  # or write multiple Elements or strings at once\n                  xf.write(etree.Element(\'start\'), "text", etree.Element(\'end\'))\n\n    If \'output_file\' is a file(-like) object, passing ``close=True`` will\n    close it when exiting the context manager.  By default, it is left\n    to the owner to do that.  When a file path is used, lxml will take care\n    of opening and closing the file itself.  Also, when a compression level\n    is set, lxml will deliberately close the file to make sure all data gets\n    compressed and written.\n\n    Setting ``buffered=False`` will flush the output after each operation,\n    such as opening or closing an ``xf.element()`` block or calling\n    ``xf.write()``.  Alternatively, calling ``xf.flush()`` can be used to\n    explicitly flush any pending output when buffering is enabled.\n    '
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

def __getattr__(name) -> typing.Any:
    ...

