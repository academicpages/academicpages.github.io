const { Transform } = require('readable-stream')

class Block extends Transform {
  constructor (size, opts = {}) {
    super(opts)

    if (typeof size === 'object') {
      opts = size
      size = opts.size
    }

    this.size = size || 512

    const { nopad, zeroPadding = true } = opts

    if (nopad) this._zeroPadding = false
    else this._zeroPadding = !!zeroPadding

    this._buffered = []
    this._bufferedBytes = 0
  }

  _transform (buf, enc, next) {
    this._bufferedBytes += buf.length
    this._buffered.push(buf)

    while (this._bufferedBytes >= this.size) {
      const b = Buffer.concat(this._buffered)
      this._bufferedBytes -= this.size
      this.push(b.slice(0, this.size))
      this._buffered = [ b.slice(this.size, b.length) ]
    }
    next()
  }

  _flush () {
    if (this._bufferedBytes && this._zeroPadding) {
      const zeroes = Buffer.alloc(this.size - this._bufferedBytes)
      this._buffered.push(zeroes)
      this.push(Buffer.concat(this._buffered))
      this._buffered = null
    } else if (this._bufferedBytes) {
      this.push(Buffer.concat(this._buffered))
      this._buffered = null
    }
    this.push(null)
  }
}

module.exports = Block
