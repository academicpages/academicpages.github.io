from pyasn1.codec.cer import encoder

class SetEncoder(encoder.SetEncoder): ...

class Encoder(encoder.Encoder):
    fixedDefLengthMode: bool
    fixedChunkSize: int

encode: Encoder
