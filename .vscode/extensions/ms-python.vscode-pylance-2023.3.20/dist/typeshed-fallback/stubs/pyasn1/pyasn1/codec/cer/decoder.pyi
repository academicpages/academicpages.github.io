from _typeshed import Unused

from pyasn1.codec.ber import decoder
from pyasn1.type import univ
from pyasn1.type.tag import TagSet

class BooleanDecoder(decoder.AbstractSimpleDecoder):
    protoComponent: univ.Boolean
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

BitStringDecoder = decoder.BitStringDecoder
OctetStringDecoder = decoder.OctetStringDecoder
RealDecoder = decoder.RealDecoder

class Decoder(decoder.Decoder): ...

decode: Decoder
