long2ip = (long) ->
    a = (long & (0xff << 24)) >>> 24;
    b = (long & (0xff << 16)) >>> 16;
    c = (long & (0xff << 8)) >>> 8;
    d = long & 0xff;
    return [a, b, c, d].join('.')

ip2long = (ip) ->
    b = (ip + '').split('.');
    if b.length is 0 or b.length > 4 then throw new Error('Invalid IP')
    for byte, i in b
        if isNaN parseInt(byte, 10) then throw new Error("Invalid byte: #{byte}")
        if byte < 0 or byte > 255 then throw new Error("Invalid byte: #{byte}")
    return ((b[0] or 0) << 24 | (b[1] or 0) << 16 | (b[2] or 0) << 8 | (b[3] or 0)) >>> 0


class Netmask
    constructor: (net, mask) ->
        throw new Error("Missing `net' parameter") unless typeof net is 'string'
        unless mask
            # try to find the mask in the net (i.e.: 1.2.3.4/24 or 1.2.3.4/255.255.255.0)
            [net, mask] = net.split('/', 2)
        unless mask
            switch net.split('.').length
                when 1 then mask = 8
                when 2 then mask = 16
                when 3 then mask = 24
                when 4 then mask = 32
                else throw new Error("Invalid net address: #{net}")

        if typeof mask is 'string' and mask.indexOf('.') > -1
            # Compute bitmask, the netmask as a number of bits in the network portion of the address for this block (eg.: 24)
            try
                @maskLong = ip2long(mask)
            catch error
                throw new Error("Invalid mask: #{mask}")
            for i in [32..0]
                if @maskLong == (0xffffffff << (32 - i)) >>> 0
                    @bitmask = i
                    break
        else if mask
            # The mask was passed as bitmask, compute the mask as long from it
            @bitmask = parseInt(mask, 10)
            @maskLong = 0
            if @bitmask > 0
                @maskLong = (0xffffffff << (32 - @bitmask)) >>> 0
        else
            throw new Error("Invalid mask: empty")

        try
            @netLong = (ip2long(net) & @maskLong) >>> 0
        catch error
            throw new Error("Invalid net address: #{net}")

        throw new Error("Invalid mask for ip4: #{mask}") unless @bitmask <= 32

        # The number of IP address in the block (eg.: 254)
        @size = Math.pow(2, 32 - @bitmask)
        # The address of the network block as a string (eg.: 216.240.32.0)
        @base = long2ip(@netLong)
        # The netmask as a string (eg.: 255.255.255.0)
        @mask = long2ip(@maskLong)
        # The host mask, the opposite of the netmask (eg.: 0.0.0.255)
        @hostmask = long2ip(~@maskLong)
        # The first usable address of the block
        @first = if @bitmask <= 30 then long2ip(@netLong + 1) else @base
        # The last  usable address of the block
        @last = if @bitmask <= 30 then long2ip(@netLong + @size - 2) else long2ip(@netLong + @size - 1)
        # The block's broadcast address: the last address of the block (eg.: 192.168.1.255)
        @broadcast = if @bitmask <= 30 then long2ip(@netLong + @size - 1)

    # Returns true if the given ip or netmask is contained in the block
    contains: (ip) ->
        if typeof ip is 'string' and (ip.indexOf('/') > 0 or ip.split('.').length isnt 4)
            ip = new Netmask(ip)

        if ip instanceof Netmask
            return @contains(ip.base) and @contains((ip.broadcast || ip.last))
        else
            return (ip2long(ip) & @maskLong) >>> 0 == ((@netLong & @maskLong)) >>> 0

    # Returns the Netmask object for the block which follow this one
    next: (count=1) ->
        return new Netmask(long2ip(@netLong + (@size * count)), @mask)

    forEach: (fn) ->
        range = [ip2long(@first)..ip2long(@last)]
        fn long2ip(long), long, index for long, index in range

    # Returns the complete netmask formatted as `base/bitmask`
    toString: ->
        return @base + "/" + @bitmask


exports.ip2long = ip2long
exports.long2ip = long2ip
exports.Netmask = Netmask
