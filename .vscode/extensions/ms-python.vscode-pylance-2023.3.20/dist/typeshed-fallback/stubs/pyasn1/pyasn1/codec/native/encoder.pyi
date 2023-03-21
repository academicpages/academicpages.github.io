from abc import abstractmethod
from collections import OrderedDict

class AbstractItemEncoder:
    @abstractmethod
    def encode(self, value, encodeFun, **options) -> None: ...

class BooleanEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class IntegerEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class BitStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class OctetStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class TextStringEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class NullEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options) -> None: ...

class ObjectIdentifierEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class RealEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class SetEncoder(AbstractItemEncoder):
    protoDict = dict
    def encode(self, value, encodeFun, **options): ...

class SequenceEncoder(SetEncoder):
    protoDict = OrderedDict

class SequenceOfEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class ChoiceEncoder(SequenceEncoder): ...

class AnyEncoder(AbstractItemEncoder):
    def encode(self, value, encodeFun, **options): ...

class Encoder:
    def __init__(self, tagMap, typeMap=...) -> None: ...
    def __call__(self, value, **options): ...

encode: Encoder
