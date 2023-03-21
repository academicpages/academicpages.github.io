from _typeshed import Incomplete, Unused
from abc import ABCMeta, abstractmethod
from collections.abc import Callable

from pyasn1.type import base, char, univ, useful
from pyasn1.type.base import Asn1Type
from pyasn1.type.tag import TagSet

class AbstractDecoder:
    protoComponent: Asn1Type | None
    @abstractmethod
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ) -> None: ...
    # Abstract, but implementation is optional
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ) -> None: ...

class AbstractSimpleDecoder(AbstractDecoder, metaclass=ABCMeta):
    @staticmethod
    def substrateCollector(asn1Object, substrate, length): ...

class ExplicitTagDecoder(AbstractSimpleDecoder):
    protoComponent: univ.Any
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class IntegerDecoder(AbstractSimpleDecoder):
    protoComponent: univ.Integer
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Unused = ...,
        substrateFun: Unused = ...,
        **options,
    ): ...

class BooleanDecoder(IntegerDecoder):
    protoComponent: univ.Boolean

class BitStringDecoder(AbstractSimpleDecoder):
    protoComponent: univ.BitString
    supportConstructedForm: bool
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class OctetStringDecoder(AbstractSimpleDecoder):
    protoComponent: univ.OctetString
    supportConstructedForm: bool
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class NullDecoder(AbstractSimpleDecoder):
    protoComponent: univ.Null
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Unused = ...,
        substrateFun: Unused = ...,
        **options,
    ): ...

class ObjectIdentifierDecoder(AbstractSimpleDecoder):
    protoComponent: univ.ObjectIdentifier
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Unused = ...,
        substrateFun: Unused = ...,
        **options,
    ): ...

class RealDecoder(AbstractSimpleDecoder):
    protoComponent: univ.Real
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Unused = ...,
        substrateFun: Unused = ...,
        **options,
    ): ...

class AbstractConstructedDecoder(AbstractDecoder, metaclass=ABCMeta):
    protoComponent: base.ConstructedAsn1Type | None

class UniversalConstructedTypeDecoder(AbstractConstructedDecoder):
    protoRecordComponent: univ.SequenceAndSetBase | None
    protoSequenceComponent: univ.SequenceOfAndSetOfBase | None
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class SequenceOrSequenceOfDecoder(UniversalConstructedTypeDecoder):
    protoRecordComponent: univ.Sequence
    protoSequenceComponent: univ.SequenceOf

class SequenceDecoder(SequenceOrSequenceOfDecoder):
    protoComponent: univ.Sequence

class SequenceOfDecoder(SequenceOrSequenceOfDecoder):
    protoComponent: univ.SequenceOf

class SetOrSetOfDecoder(UniversalConstructedTypeDecoder):
    protoRecordComponent: univ.Set
    protoSequenceComponent: univ.SetOf

class SetDecoder(SetOrSetOfDecoder):
    protoComponent: univ.Set

class SetOfDecoder(SetOrSetOfDecoder):
    protoComponent: univ.SetOf

class ChoiceDecoder(AbstractConstructedDecoder):
    protoComponent: univ.Choice
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Incomplete | None = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class AnyDecoder(AbstractSimpleDecoder):
    protoComponent: univ.Any
    def valueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Unused = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...
    def indefLenValueDecoder(
        self,
        substrate,
        asn1Spec,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state: Unused = ...,
        decodeFun: Callable[..., Incomplete] | None = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

class UTF8StringDecoder(OctetStringDecoder):
    protoComponent: char.UTF8String

class NumericStringDecoder(OctetStringDecoder):
    protoComponent: char.NumericString

class PrintableStringDecoder(OctetStringDecoder):
    protoComponent: char.PrintableString

class TeletexStringDecoder(OctetStringDecoder):
    protoComponent: char.TeletexString

class VideotexStringDecoder(OctetStringDecoder):
    protoComponent: char.VideotexString

class IA5StringDecoder(OctetStringDecoder):
    protoComponent: char.IA5String

class GraphicStringDecoder(OctetStringDecoder):
    protoComponent: char.GraphicString

class VisibleStringDecoder(OctetStringDecoder):
    protoComponent: char.VisibleString

class GeneralStringDecoder(OctetStringDecoder):
    protoComponent: char.GeneralString

class UniversalStringDecoder(OctetStringDecoder):
    protoComponent: char.UniversalString

class BMPStringDecoder(OctetStringDecoder):
    protoComponent: char.BMPString

class ObjectDescriptorDecoder(OctetStringDecoder):
    protoComponent: useful.ObjectDescriptor

class GeneralizedTimeDecoder(OctetStringDecoder):
    protoComponent: useful.GeneralizedTime

class UTCTimeDecoder(OctetStringDecoder):
    protoComponent: useful.UTCTime

class Decoder:
    defaultErrorState: int
    defaultRawDecoder: AnyDecoder
    supportIndefLength: bool
    def __init__(self, tagMap, typeMap=...) -> None: ...
    def __call__(
        self,
        substrate,
        asn1Spec: Asn1Type | None = ...,
        tagSet: TagSet | None = ...,
        length: int | None = ...,
        state=...,
        decodeFun: Unused = ...,
        substrateFun: Callable[..., Incomplete] | None = ...,
        **options,
    ): ...

decode: Decoder
