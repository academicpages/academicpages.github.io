function createError(message) {
    var err = new Error(message);
    err.source = "ulid";
    return err;
}
// These values should NEVER change. If
// they do, we're no longer making ulids!
var ENCODING = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"; // Crockford's Base32
var ENCODING_LEN = ENCODING.length;
var TIME_MAX = Math.pow(2, 48) - 1;
var TIME_LEN = 10;
var RANDOM_LEN = 16;
function replaceCharAt(str, index, char) {
    if (index > str.length - 1) {
        return str;
    }
    return str.substr(0, index) + char + str.substr(index + 1);
}
function incrementBase32(str) {
    var done = undefined;
    var index = str.length;
    var char = void 0;
    var charIndex = void 0;
    var maxCharIndex = ENCODING_LEN - 1;
    while (!done && index-- >= 0) {
        char = str[index];
        charIndex = ENCODING.indexOf(char);
        if (charIndex === -1) {
            throw createError("incorrectly encoded string");
        }
        if (charIndex === maxCharIndex) {
            str = replaceCharAt(str, index, ENCODING[0]);
            continue;
        }
        done = replaceCharAt(str, index, ENCODING[charIndex + 1]);
    }
    if (typeof done === "string") {
        return done;
    }
    throw createError("cannot increment this string");
}
function randomChar(prng) {
    var rand = Math.floor(prng() * ENCODING_LEN);
    if (rand === ENCODING_LEN) {
        rand = ENCODING_LEN - 1;
    }
    return ENCODING.charAt(rand);
}
function encodeTime(now, len) {
    if (isNaN(now)) {
        throw new Error(now + " must be a number");
    }
    if (now > TIME_MAX) {
        throw createError("cannot encode time greater than " + TIME_MAX);
    }
    if (now < 0) {
        throw createError("time must be positive");
    }
    if (Number.isInteger(now) === false) {
        throw createError("time must be an integer");
    }
    var mod = void 0;
    var str = "";
    for (; len > 0; len--) {
        mod = now % ENCODING_LEN;
        str = ENCODING.charAt(mod) + str;
        now = (now - mod) / ENCODING_LEN;
    }
    return str;
}
function encodeRandom(len, prng) {
    var str = "";
    for (; len > 0; len--) {
        str = randomChar(prng) + str;
    }
    return str;
}
function decodeTime(id) {
    if (id.length !== TIME_LEN + RANDOM_LEN) {
        throw createError("malformed ulid");
    }
    var time = id.substr(0, TIME_LEN).split("").reverse().reduce(function (carry, char, index) {
        var encodingIndex = ENCODING.indexOf(char);
        if (encodingIndex === -1) {
            throw createError("invalid character found: " + char);
        }
        return carry += encodingIndex * Math.pow(ENCODING_LEN, index);
    }, 0);
    if (time > TIME_MAX) {
        throw createError("malformed ulid, timestamp too large");
    }
    return time;
}
function detectPrng() {
    var allowInsecure = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : false;
    var root = arguments[1];

    if (!root) {
        root = typeof window !== "undefined" ? window : null;
    }
    var browserCrypto = root && (root.crypto || root.msCrypto);
    if (browserCrypto) {
        return function () {
            var buffer = new Uint8Array(1);
            browserCrypto.getRandomValues(buffer);
            return buffer[0] / 0xff;
        };
    } else {
        try {
            var nodeCrypto = require("crypto");
            return function () {
                return nodeCrypto.randomBytes(1).readUInt8() / 0xff;
            };
        } catch (e) {}
    }
    if (allowInsecure) {
        try {
            console.error("secure crypto unusable, falling back to insecure Math.random()!");
        } catch (e) {}
        return function () {
            return Math.random();
        };
    }
    throw createError("secure crypto unusable, insecure Math.random not allowed");
}
function factory(currPrng) {
    if (!currPrng) {
        currPrng = detectPrng();
    }
    return function ulid(seedTime) {
        if (isNaN(seedTime)) {
            seedTime = Date.now();
        }
        return encodeTime(seedTime, TIME_LEN) + encodeRandom(RANDOM_LEN, currPrng);
    };
}
function monotonicFactory(currPrng) {
    if (!currPrng) {
        currPrng = detectPrng();
    }
    var lastTime = 0;
    var lastRandom = void 0;
    return function ulid(seedTime) {
        if (isNaN(seedTime)) {
            seedTime = Date.now();
        }
        if (seedTime <= lastTime) {
            var incrementedRandom = lastRandom = incrementBase32(lastRandom);
            return encodeTime(lastTime, TIME_LEN) + incrementedRandom;
        }
        lastTime = seedTime;
        var newRandom = lastRandom = encodeRandom(RANDOM_LEN, currPrng);
        return encodeTime(seedTime, TIME_LEN) + newRandom;
    };
}
var ulid = factory();

export { replaceCharAt, incrementBase32, randomChar, encodeTime, encodeRandom, decodeTime, detectPrng, factory, monotonicFactory, ulid };
