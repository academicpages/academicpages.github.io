vows = require 'vows'
assert = require 'assert'
Netmask = require('../lib/netmask').Netmask

shouldFailWithError = (msg) ->
    context =
        topic: ->
            try
                return new Netmask(@context.name)
            catch e
                return e
        'should fail': (e) ->
            assert.ok isError(e), "is an Error object #{e}"
        "with error `#{msg}'": (e) ->
            assert.ok e.message?.toLowerCase().indexOf(msg.toLowerCase()) > -1, "'#{e.message}' =~ #{msg}"

    return context

isError = (e) ->
    return typeof e == 'object' and Object.prototype.toString.call(e) == '[object Error]'

vows.describe('IPs with bytes greater than 255')
    .addBatch
        '209.256.68.22/255.255.224.0': shouldFailWithError 'Invalid net'
        '209.180.68.22/256.255.224.0': shouldFailWithError 'Invalid mask'
        '209.500.70.33/19': shouldFailWithError 'Invalid net'
        '140.999.82': shouldFailWithError 'Invalid net'
        '899.174': shouldFailWithError 'Invalid net'
        '900': shouldFailWithError 'Invalid net'
        '209.157.300/19': shouldFailWithError 'Invalid net'
        '209.300.64.0.10': shouldFailWithError 'Invalid net'
        'garbage': shouldFailWithError 'Invalid net'
    .export(module)

vows.describe('Ranges that are a power-of-two big, but are not legal blocks')
    .addBatch
        '218.0.0.0/221.255.255.255': shouldFailWithError 'Invalid mask'
        '218.0.0.4/218.0.0.11': shouldFailWithError 'Invalid mask'
    .export(module)
