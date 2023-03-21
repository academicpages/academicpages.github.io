from typing import ClassVar

from pyasn1.codec.ber import encoder

class BooleanEncoder(encoder.IntegerEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class RealEncoder(encoder.RealEncoder): ...

class TimeEncoderMixIn:
    Z_CHAR: ClassVar[int]
    PLUS_CHAR: ClassVar[int]
    MINUS_CHAR: ClassVar[int]
    COMMA_CHAR: ClassVar[int]
    DOT_CHAR: ClassVar[int]
    ZERO_CHAR: ClassVar[int]
    MIN_LENGTH: ClassVar[int]
    MAX_LENGTH: ClassVar[int]
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class GeneralizedTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder): ...
class UTCTimeEncoder(TimeEncoderMixIn, encoder.OctetStringEncoder): ...

class SetOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceOfEncoder(encoder.SequenceOfEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SetEncoder(encoder.SequenceEncoder):
    def encodeValue(self, value, asn1Spec, encodeFun, **options): ...

class SequenceEncoder(encoder.SequenceEncoder):
    omitEmptyOptionals: bool

class Encoder(encoder.Encoder):
    fixedDefLengthMode: bool
    fixedChunkSize: int

encode: Encoder
