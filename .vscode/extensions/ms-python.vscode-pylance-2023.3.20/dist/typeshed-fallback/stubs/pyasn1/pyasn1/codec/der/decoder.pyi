from pyasn1.codec.cer import decoder

class BitStringDecoder(decoder.BitStringDecoder):
    supportConstructedForm: bool

class OctetStringDecoder(decoder.OctetStringDecoder):
    supportConstructedForm: bool

class Decoder(decoder.Decoder):
    supportIndefLength: bool

decode: Decoder
