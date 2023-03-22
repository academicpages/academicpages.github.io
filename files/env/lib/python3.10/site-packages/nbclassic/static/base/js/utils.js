// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'codemirror/lib/codemirror',
    'moment',
    'underscore',
    // silently upgrades CodeMirror
    'codemirror/mode/meta',
], function($, CodeMirror, moment, _){
    "use strict";
    
    // keep track of which extensions have been loaded already
    var extensions_loaded = [];

    /**
     * Whether or not an extension has been loaded
     * @param  {string} extension - name of the extension
     * @return {boolean}            true if loaded already
     */
    var is_loaded = function(extension) {
        var ext_path = "nbextensions/" + extension;
        return extensions_loaded.indexOf(ext_path) >= 0;
    };

    /**
     * Load a single extension.
     * @param  {string} extension - extension path.
     * @return {Promise} that resolves to an extension module handle
     */
    var load_extension = function (extension) {
        return new Promise(function(resolve, reject) {
            var ext_path = "nbextensions/" + extension;
            requirejs([ext_path], function(module) {
                if (!is_loaded(extension)) {
                    console.log("Loading extension: " + extension);
                    if (module && module.load_ipython_extension) {
                        Promise.resolve(module.load_ipython_extension()).then(function() {
                            resolve(module);
                        }).catch(reject);
                    }
                    extensions_loaded.push(ext_path);
                } else {
                    console.log("Loaded extension already: " + extension);
                    resolve(module);
                }
            }, function(err) {
                reject(err);
            });
        });
    };

    /**
     * Load multiple extensions.
     * Takes n-args, where each arg is a string path to the extension.
     * @return {Promise} that resolves to a list of loaded module handles.
     */
    var load_extensions = function () {
        console.log('load_extensions', arguments);
        return Promise.all(Array.prototype.map.call(arguments, load_extension)).catch(function(err) {
            console.error("Failed to load extension" + (err.requireModules.length>1?'s':'') + ":", err.requireModules, err);
        });
    };

    /**
     * Return a list of extensions that should be active
     * The config for nbextensions comes in as a dict where keys are
     * nbextensions paths and the values are a bool indicating if it
     * should be active. This returns a list of nbextension paths
     * where the value is true
     */
    function filter_extensions(nbext_config) {
        var active = [];
        Object.keys(nbext_config).forEach(function (nbext) {
            if (nbext_config[nbext]) {active.push(nbext);}
        });
        return active;
    }

    /**
     * Wait for a config section to load, and then load the extensions specified
     * in a 'load_extensions' key inside it.
     */
    function load_extensions_from_config(section) {
        return section.loaded.then(function() {
            if (section.data.load_extensions) {
                var active = filter_extensions(section.data.load_extensions);
                return load_extensions.apply(this, active);
            }
        }).catch(utils.reject('Could not load nbextensions from ' + section.section_name + ' config file'));
    }

    //============================================================================
    // Cross-browser RegEx Split
    //============================================================================

    // This code has been MODIFIED from the code licensed below to not replace the
    // default browser split.  The license is reproduced here.

    // see http://blog.stevenlevithan.com/archives/cross-browser-split for more info:
    /*!
     * Cross-Browser Split 1.1.1
     * Copyright 2007-2012 Steven Levithan <stevenlevithan.com>
     * Available under the MIT License
     * ECMAScript compliant, uniform cross-browser split method
     */

    /**
     * Splits a string into an array of strings using a regex or string
     * separator. Matches of the separator are not included in the result array.
     * However, if `separator` is a regex that contains capturing groups,
     * backreferences are spliced into the result each time `separator` is
     * matched. Fixes browser bugs compared to the native
     * `String.prototype.split` and can be used reliably cross-browser.
     * @param {String} str String to split.
     * @param {RegExp} separator Regex to use for separating
     *     the string.
     * @param {Number} [limit] Maximum number of items to include in the result
     *     array.
     * @returns {Array} Array of substrings.
     * @example
     *
     * // Basic use
     * regex_split('a b c d', ' ');
     * // -> ['a', 'b', 'c', 'd']
     *
     * // With limit
     * regex_split('a b c d', ' ', 2);
     * // -> ['a', 'b']
     *
     * // Backreferences in result array
     * regex_split('..word1 word2..', /([a-z]+)(\d+)/i);
     * // -> ['..', 'word', '1', ' ', 'word', '2', '..']
     */
    var regex_split = function (str, separator, limit) {
        var output = [],
            flags = (separator.ignoreCase ? "i" : "") +
                    (separator.multiline  ? "m" : "") +
                    (separator.extended   ? "x" : "") + // Proposed for ES6
                    (separator.sticky     ? "y" : ""), // Firefox 3+
            lastLastIndex = 0,
            separator2, match, lastIndex, lastLength;
        // Make `global` and avoid `lastIndex` issues by working with a copy
        separator = new RegExp(separator.source, flags + "g");

        var compliantExecNpcg = typeof(/()??/.exec("")[1]) === "undefined";
        if (!compliantExecNpcg) {
            // Doesn't need flags gy, but they don't hurt
            separator2 = new RegExp("^" + separator.source + "$(?!\\s)", flags);
        }
        /* Values for `limit`, per the spec:
         * If undefined: 4294967295 // Math.pow(2, 32) - 1
         * If 0, Infinity, or NaN: 0
         * If positive number: limit = Math.floor(limit); if (limit > 4294967295) limit -= 4294967296;
         * If negative number: 4294967296 - Math.floor(Math.abs(limit))
         * If other: Type-convert, then use the above rules
         */
        limit = typeof(limit) === "undefined" ?
            -1 >>> 0 : // Math.pow(2, 32) - 1
            limit >>> 0; // ToUint32(limit)
        for (match = separator.exec(str); match; match = separator.exec(str)) {
            // `separator.lastIndex` is not reliable cross-browser
            lastIndex = match.index + match[0].length;
            if (lastIndex > lastLastIndex) {
                output.push(str.slice(lastLastIndex, match.index));
                // Fix browsers whose `exec` methods don't consistently return `undefined` for
                // nonparticipating capturing groups
                if (!compliantExecNpcg && match.length > 1) {
                    match[0].replace(separator2, function () {
                        for (var i = 1; i < arguments.length - 2; i++) {
                            if (typeof(arguments[i]) === "undefined") {
                                match[i] = undefined;
                            }
                        }
                    });
                }
                if (match.length > 1 && match.index < str.length) {
                    Array.prototype.push.apply(output, match.slice(1));
                }
                lastLength = match[0].length;
                lastLastIndex = lastIndex;
                if (output.length >= limit) {
                    break;
                }
            }
            if (separator.lastIndex === match.index) {
                separator.lastIndex++; // Avoid an infinite loop
            }
        }
        if (lastLastIndex === str.length) {
            if (lastLength || !separator.test("")) {
                output.push("");
            }
        } else {
            output.push(str.slice(lastLastIndex));
        }
        return output.length > limit ? output.slice(0, limit) : output;
    };

    //============================================================================
    // End contributed Cross-browser RegEx Split
    //============================================================================


    var uuid = function () {
        /**
         * http://www.ietf.org/rfc/rfc4122.txt
         */
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 32; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[12] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
        s[16] = hexDigits.substr((s[16] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01

        var uuid = s.join("");
        return uuid;
    };

    var _ANSI_COLORS = [
        "ansi-black",
        "ansi-red",
        "ansi-green",
        "ansi-yellow",
        "ansi-blue",
        "ansi-magenta",
        "ansi-cyan",
        "ansi-white",
        "ansi-black-intense",
        "ansi-red-intense",
        "ansi-green-intense",
        "ansi-yellow-intense",
        "ansi-blue-intense",
        "ansi-magenta-intense",
        "ansi-cyan-intense",
        "ansi-white-intense",
    ];
    
    function _pushColoredChunk(chunk, fg, bg, bold, underline, inverse, out) {
        if (chunk) {
            var classes = [];
            var styles = [];

            if (bold && typeof fg === "number" && 0 <= fg && fg < 8) {
                fg += 8;  // Bold text uses "intense" colors
            }
            if (inverse) {
                [fg, bg] = [bg, fg];
            }

            if (typeof fg === "number") {
                classes.push(_ANSI_COLORS[fg] + "-fg");
            } else if (fg.length) {
                styles.push("color: rgb(" + fg + ")");
            } else if (inverse) {
                classes.push("ansi-default-inverse-fg");
            }

            if (typeof bg === "number") {
                classes.push(_ANSI_COLORS[bg] + "-bg");
            } else if (bg.length) {
                styles.push("background-color: rgb(" + bg + ")");
            } else if (inverse) {
                classes.push("ansi-default-inverse-bg");
            }

            if (bold) {
                classes.push("ansi-bold");
            }

            if (underline) {
                classes.push("ansi-underline");
            }

            if (classes.length || styles.length) {
                out.push("<span");
                if (classes.length) {
                    out.push(' class="' + classes.join(" ") + '"');
                }
                if (styles.length) {
                    out.push(' style="' + styles.join("; ") + '"');
                }
                out.push(">");
                out.push(chunk);
                out.push("</span>");
            } else {
                out.push(chunk);
            }
        }
    }

    function _getExtendedColors(numbers) {
        var r, g, b;
        var n = numbers.shift();
        if (n === 2 && numbers.length >= 3) {
            // 24-bit RGB
            r = numbers.shift();
            g = numbers.shift();
            b = numbers.shift();
            if ([r, g, b].some(function (c) { return c < 0 || 255 < c; })) {
                throw new RangeError("Invalid range for RGB colors");
            }
        } else if (n === 5 && numbers.length >= 1) {
            // 256 colors
            var idx = numbers.shift();
            if (idx < 0) {
                throw new RangeError("Color index must be >= 0");
            } else if (idx < 16) {
                // 16 default terminal colors
                return idx;
            } else if (idx < 232) {
                // 6x6x6 color cube, see https://stackoverflow.com/a/27165165/500098
                r = Math.floor((idx - 16) / 36);
                r = r > 0 ? 55 + r * 40 : 0;
                g = Math.floor(((idx - 16) % 36) / 6);
                g = g > 0 ? 55 + g * 40 : 0;
                b = (idx - 16) % 6;
                b = b > 0 ? 55 + b * 40 : 0;
            } else if (idx < 256) {
                // grayscale, see https://stackoverflow.com/a/27165165/500098
                r = g = b = (idx - 232) * 10 + 8;
            } else {
                throw new RangeError("Color index must be < 256");
            }
        } else {
            throw new RangeError("Invalid extended color specification");
        }
        return [r, g, b];
    }

    function _ansispan(str) {
        var ansi_re = /\x1b\[(.*?)([@-~])/g;
        var fg = [];
        var bg = [];
        var bold = false;
        var underline = false;
        var inverse = false;
        var match;
        var out = [];
        var numbers = [];
        var start = 0;

        str += "\x1b[m";  // Ensure markup for trailing text
        while ((match = ansi_re.exec(str))) {
            if (match[2] === "m") {
                var items = match[1].split(";");
                for (var i = 0; i < items.length; i++) {
                    var item = items[i];
                    if (item === "") {
                        numbers.push(0);
                    } else if (item.search(/^\d+$/) !== -1) {
                        numbers.push(parseInt(item));
                    } else {
                        // Ignored: Invalid color specification
                        numbers.length = 0;
                        break;
                    }
                }
            } else {
                // Ignored: Not a color code
            }
            var chunk = str.substring(start, match.index);
	    _pushColoredChunk(chunk, fg, bg, bold, underline, inverse, out);
            start = ansi_re.lastIndex;

            while (numbers.length) {
                var n = numbers.shift();
                switch (n) {
                    case 0:
                        fg = bg = [];
                        bold = false;
                        underline = false;
                        inverse = false;
                        break;
                    case 1:
                    case 5:
                        bold = true;
                        break;
                    case 4:
                        underline = true;
                        break;
                    case 7:
                        inverse = true;
                        break;
                    case 21:
                    case 22:
                        bold = false;
                        break;
                    case 24:
                        underline = false;
                        break;
                    case 27:
                        inverse = false;
                        break;
                    case 30:
                    case 31:
                    case 32:
                    case 33:
                    case 34:
                    case 35:
                    case 36:
                    case 37:
                        fg = n - 30;
                        break;
                    case 38:
                        try {
                            fg = _getExtendedColors(numbers);
                        } catch(e) {
                            numbers.length = 0;
                        }
                        break;
                    case 39:
                        fg = [];
                        break;
                    case 40:
                    case 41:
                    case 42:
                    case 43:
                    case 44:
                    case 45:
                    case 46:
                    case 47:
                        bg = n - 40;
                        break;
                    case 48:
                        try {
                            bg = _getExtendedColors(numbers);
                        } catch(e) {
                            numbers.length = 0;
                        }
                        break;
                    case 49:
                        bg = [];
                        break;
		    case 90:
		    case 91:
		    case 92:
		    case 93:
		    case 94:
		    case 95:
		    case 96:
		    case 97:
			fg = n - 90 + 8;
                        break;
		    case 100:
		    case 101:
		    case 102:
		    case 103:
		    case 104:
		    case 105:
		    case 106:
		    case 107:
			bg = n - 100 + 8;
                        break;
                    default:
                        // Unknown codes are ignored
                }
            }
        }
        return out.join("");
    }

    // Transform ANSI color escape codes into HTML <span> tags with CSS
    // classes such as "ansi-green-intense-fg".
    // The actual colors used are set in the CSS file.
    // This is supposed to have the same behavior as nbconvert.filters.ansi2html()
    function fixConsole(txt) {
        txt = _.escape(txt);

        // color ansi codes (and remove non-color escape sequences)
        txt = _ansispan(txt);
        return txt;
    }

    // Remove chunks that should be overridden by the effect of
    // carriage return characters
    function fixCarriageReturn(txt) {
        txt = txt.replace(/\r+\n/gm, '\n'); // \r followed by \n --> newline
        while (txt.search(/\r[^$]/g) > -1) {
            var base = txt.match(/^(.*)\r+/m)[1];
            var insert = txt.match(/\r+(.*)$/m)[1];
            insert = insert + base.slice(insert.length, base.length);
            txt = txt.replace(/\r+.*$/m, '\r').replace(/^.*\r/m, insert);
        }
        return txt;
    }

    // Remove characters that are overridden by backspace characters
    function fixBackspace(txt) {
        var tmp = txt;
        do {
            txt = tmp;
            // Cancel out anything-but-newline followed by backspace
            tmp = txt.replace(/[^\n]\x08/gm, '');
        } while (tmp.length < txt.length);
        return txt;
    }

    // Remove characters overridden by backspace and carriage return
    function fixOverwrittenChars(txt) {
        return fixCarriageReturn(fixBackspace(txt));
    }

    // Locate any URLs and convert them to an anchor tag
    function autoLinkUrls(txt) {
        return txt.replace(/(^|\s)(https?|ftp)(:[^'"<>\s]+)/gi,
            "$1<a target=\"_blank\" href=\"$2$3\">$2$3</a>");
    }

    var points_to_pixels = function (points) {
        /**
         * A reasonably good way of converting between points and pixels.
         */
        var test = $('<div style="display: none; width: 10000pt; padding:0; border:0;"></div>');
        $('body').append(test);
        var pixel_per_point = test.width()/10000;
        test.remove();
        return Math.floor(points*pixel_per_point);
    };
    
    var always_new = function (constructor) {
        /**
         * wrapper around contructor to avoid requiring `var a = new constructor()`
         * useful for passing constructors as callbacks,
         * not for programmer laziness.
         * from https://programmers.stackexchange.com/questions/118798
         */
        return function () {
            var obj = Object.create(constructor.prototype);
            constructor.apply(obj, arguments);
            return obj;
        };
    };

    var url_path_join = function () {
        /**
         * join a sequence of url components with '/'
         */
        var url = '';
        for (var i = 0; i < arguments.length; i++) {
            if (arguments[i] === '') {
                continue;
            }
            if (url.length > 0 && url[url.length-1] != '/') {
                url = url + '/' + arguments[i];
            } else {
                url = url + arguments[i];
            }
        }
        url = url.replace(/\/\/+/, '/');
        return url;
    };
    
    var url_path_split = function (path) {
        /**
         * Like os.path.split for URLs.
         * Always returns two strings, the directory path and the base filename
         */
        
        var idx = path.lastIndexOf('/');
        if (idx === -1) {
            return ['', path];
        } else {
            return [ path.slice(0, idx), path.slice(idx + 1) ];
        }
    };
    
    var parse_url = function (url) {
        /**
         * an `a` element with an href allows attr-access to the parsed segments of a URL
         * a = parse_url("http://localhost:8888/path/name#hash")
         * a.protocol = "http:"
         * a.host     = "localhost:8888"
         * a.hostname = "localhost"
         * a.port     = 8888
         * a.pathname = "/path/name"
         * a.hash     = "#hash"
         */
        var a = document.createElement("a");
        a.href = url;
        return a;
    };
    
    var encode_uri_components = function (uri) {
        /**
         * encode just the components of a multi-segment uri,
         * leaving '/' separators
         */
        return uri.split('/').map(encodeURIComponent).join('/');
    };
    
    var url_join_encode = function () {
        /**
         * join a sequence of url components with '/',
         * encoding each component with encodeURIComponent
         */
        return encode_uri_components(url_path_join.apply(null, arguments));
    };


    var splitext = function (filename) {
        /**
         * mimic Python os.path.splitext
         * Returns ['base', '.ext']
         */
        var idx = filename.lastIndexOf('.');
        if (idx > 0) {
            return [filename.slice(0, idx), filename.slice(idx)];
        } else {
            return [filename, ''];
        }
    };


    var escape_html = function (text) {
        /**
         * escape text to HTML
         */
        return $("<div/>").text(text).html();
    };


    var get_body_data = function(key) {
        /**
         * get a url-encoded item from body.data and decode it
         * we should never have any encoded URLs anywhere else in code
         * until we are building an actual request
         */
        var val = $('body').data(key);
        if (typeof val === 'undefined')
            return val;
        return decodeURIComponent(val);
    };
    
    var to_absolute_cursor_pos = function (cm, cursor) {
        console.warn('`utils.to_absolute_cursor_pos(cm, pos)` is deprecated. Use `cm.indexFromPos(cursor)`');
        return cm.indexFromPos(cursor);
    };
    
    var from_absolute_cursor_pos = function (cm, cursor_pos) {
        console.warn('`utils.from_absolute_cursor_pos(cm, pos)` is deprecated. Use `cm.posFromIndex(index)`');
        return cm.posFromIndex(cursor_pos);
    };
    
    // https://stackoverflow.com/questions/2400935/browser-detection-in-javascript
    var browser = (function() {
        if (typeof navigator === 'undefined') {
            // navigator undefined in node
            return 'None';
        }
        var N= navigator.appName, ua= navigator.userAgent, tem;
        var M= ua.match(/(opera|chrome|safari|firefox|msie)\/?\s*(\.?\d+(\.\d+)*)/i);
        if (M && (tem= ua.match(/version\/([\.\d]+)/i)) !== null) M[2]= tem[1];
        M= M? [M[1], M[2]]: [N, navigator.appVersion,'-?'];
        return M;
    })();

    // https://stackoverflow.com/questions/11219582/how-to-detect-my-browser-version-and-operating-system-using-javascript
    var platform = (function () {
        if (typeof navigator === 'undefined') {
            // navigator undefined in node
            return 'None';
        }
        var OSName="None";
        if (navigator.appVersion.indexOf("Win")!=-1) OSName="Windows";
        if (navigator.appVersion.indexOf("Mac")!=-1) OSName="MacOS";
        if (navigator.appVersion.indexOf("X11")!=-1) OSName="UNIX";
        if (navigator.appVersion.indexOf("Linux")!=-1) OSName="Linux";
        return OSName;
    })();
    
    var get_url_param = function (name) {
        // get a URL parameter. I cannot believe we actually need this.
        // Based on https://stackoverflow.com/a/25359264/938949
        var match = new RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
        if (match){
            return decodeURIComponent(match[1] || '');
        }
    };
    
    var is_or_has = function (a, b) {
        /**
         * Is b a child of a or a itself?
         */
        return a.has(b).length !==0 || a.is(b);
    };

    var is_focused = function (e) {
        /**
         * Is element e, or one of its children focused?
         */
        e = $(e);
        var target = $(document.activeElement);
        if (target.length > 0) {
            if (is_or_has(e, target)) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    };
    
    var mergeopt = function(_class, options, overwrite){
        options = options || {};
        overwrite = overwrite || {};
        return $.extend(true, {}, _class.options_default, options, overwrite);
    };
    
    var ajax_error_msg = function (jqXHR) {
        /**
         * Return a JSON error message if there is one,
         * otherwise the basic HTTP status text.
         */
        if (jqXHR.responseJSON && jqXHR.responseJSON.traceback) {
            return jqXHR.responseJSON.traceback;
        } else if (jqXHR.responseJSON && jqXHR.responseJSON.message) {
            return jqXHR.responseJSON.message;
        } else {
            return jqXHR.statusText;
        }
    };
    var log_ajax_error = function (jqXHR, status, error) {
        /**
         * log ajax failures with informative messages
         */
        var msg = "API request failed (" + jqXHR.status + "): ";
        console.log(jqXHR);
        msg += ajax_error_msg(jqXHR);
        console.log(msg);
    };

    var requireCodeMirrorMode = function (mode, callback, errback) {
        /** 
         * find a predefined mode or detect from CM metadata then
         * require and callback with the resolvable mode string: mime or
         * custom name
         */

        var modename = (typeof mode == "string") ? mode :
            mode.mode || mode.name;

        // simplest, cheapest check by mode name: mode may also have config
        if (CodeMirror.modes.hasOwnProperty(modename)) {
            // return the full mode object, if it has a name
            callback(mode.name ? mode : modename);
            return;
        }

        // *somehow* get back a CM.modeInfo-like object that has .mode and
        // .mime
        var info = (mode && mode.mode && mode.mime && mode) ||
            CodeMirror.findModeByName(modename) ||
            CodeMirror.findModeByExtension(modename.split(".").slice(-1)[0]) ||
            CodeMirror.findModeByMIME(modename) ||
            {mode: modename, mime: modename};

        requirejs([
                // might want to use CodeMirror.modeURL here
                ['codemirror/mode', info.mode, info.mode].join('/'),
            ], function() {
              // return the original mode, as from a kernelspec on first load
              // or the mimetype, as for most highlighting
              callback(mode.name ? mode : info.mime);
            }, errback
        );
    };
    
    /** Error type for wrapped XHR errors. */
    var XHR_ERROR = 'XhrError';
    
    /**
     * Wraps an AJAX error as an Error object.
     */
    var wrap_ajax_error = function (jqXHR, status, error) {
        var wrapped_error = new Error(ajax_error_msg(jqXHR));
        wrapped_error.name =  XHR_ERROR;
        // provide xhr response
        wrapped_error.xhr = jqXHR;
        wrapped_error.xhr_status = status;
        wrapped_error.xhr_error = error;
        return wrapped_error;
    };
    
    var ajax = function (url, settings) {
        // like $.ajax, but ensure XSRF or Authorization header is set
        if (typeof url === "object") {
            // called with single argument: $.ajax({url: '...'})
            settings = url;
            url = settings.url;
            delete settings.url;
        }
        settings = _add_auth_header(settings);
        return $.ajax(url, settings);
    };
    
    var _get_cookie = function (name) {
        // from tornado docs: http://www.tornadoweb.org/en/stable/guide/security.html
        var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return r ? r[1] : undefined;
    }

    var _add_auth_header = function (settings) {
        /**
         * Adds auth header to jquery ajax settings
         */
        settings = settings || {};
        if (!settings.headers) {
            settings.headers = {};
        }
        if (!settings.headers.Authorization) {
            var xsrf_token = _get_cookie('_xsrf');
            if (xsrf_token) {
                settings.headers['X-XSRFToken'] = xsrf_token;
            }
        }
        return settings;
    };

    var promising_ajax = function(url, settings) {
        /**
         * Like $.ajax, but returning an ES6 promise. success and error settings
         * will be ignored.
         */
        settings = settings || {};
        return new Promise(function(resolve, reject) {
            settings.success = function(data, status, jqXHR) {
                resolve(data);
            };
            settings.error = function(jqXHR, status, error) {
                log_ajax_error(jqXHR, status, error);
                reject(wrap_ajax_error(jqXHR, status, error));
            };
            ajax(url, settings);
        });
    };

    var WrappedError = function(message, error){
        /**
         * Wrappable Error class
         *
         * The Error class doesn't actually act on `this`.  Instead it always
         * returns a new instance of Error.  Here we capture that instance so we
         * can apply it's properties to `this`.
         */
        var tmp = Error.apply(this, [message]);

        // Copy the properties of the error over to this.
        var properties = Object.getOwnPropertyNames(tmp);
        for (var i = 0; i < properties.length; i++) {
            this[properties[i]] = tmp[properties[i]];
        }

        // Keep a stack of the original error messages.
        if (error instanceof WrappedError) {
            this.error_stack = error.error_stack;
        } else {
            this.error_stack = [error];
        }
        this.error_stack.push(tmp);

        return this;
    };

    WrappedError.prototype = Object.create(Error.prototype, {});


    var load_class = function(class_name, module_name, registry) {
        /**
         * Tries to load a class
         *
         * Tries to load a class from a module using require.js, if a module 
         * is specified, otherwise tries to load a class from the global 
         * registry, if the global registry is provided.
         */
        return new Promise(function(resolve, reject) {

            // Try loading the view module using require.js
            if (module_name) {
                requirejs([module_name], function(module) {
                    if (module[class_name] === undefined) {
                        reject(new Error('Class '+class_name+' not found in module '+module_name));
                    } else {
                        resolve(module[class_name]);
                    }
                }, reject);
            } else {
                if (registry && registry[class_name]) {
                    resolve(registry[class_name]);
                } else {
                    reject(new Error('Class '+class_name+' not found in registry '));
                }
            }
        });
    };

    var resolve_promises_dict = function(d) {
        /**
         * Resolve a promiseful dictionary.
         * Returns a single Promise.
         */
        var keys = Object.keys(d);
        var values = [];
        keys.forEach(function(key) {
            values.push(d[key]);
        });
        return Promise.all(values).then(function(v) {
            d = {};
            for(var i=0; i<keys.length; i++) {
                d[keys[i]] = v[i];
            }
            return d;
        });
    };

    var reject = function(message, log) {
        /**
         * Creates a wrappable Promise rejection function.
         * 
         * Creates a function that returns a Promise.reject with a new WrappedError
         * that has the provided message and wraps the original error that 
         * caused the promise to reject.
         */
        return function(error) { 
            var wrapped_error = new WrappedError(message, error);
            if (log) {
                console.error(message, " -- ", error);
            }
            return Promise.reject(wrapped_error); 
        };
    };

    var typeset = function(element, text) {
        /**
         * Apply MathJax rendering to an element, and optionally set its text
         *
         * If MathJax is not available, make no changes.
         *
         * Returns the output any number of typeset elements, or undefined if
         * MathJax was not available.
         *
         * Parameters
         * ----------
         * element: Node, NodeList, or jQuery selection
         * text: option string
         */
        var $el = element.jquery ? element : $(element);
        if(arguments.length > 1){
            $el.text(text);
        }
        if(!window.MathJax){
            return;
        }
        $el.map(function(){
            // MathJax takes a DOM node: $.map makes `this` the context
            MathJax.Hub.Queue(["Typeset", MathJax.Hub, this]);
            try {
                MathJax.Hub.Queue(
                    ["Require", MathJax.Ajax, "[MathJax]/extensions/TeX/AMSmath.js"],
                    function() { MathJax.InputJax.TeX.resetEquationNumbers(); }
                );
            } catch (e) {
                console.error("Error queueing resetEquationNumbers:", e);
            }
        });
    };

    var parse_b64_data_uri = function(uri) {
        /**
         * Parses a base64 encoded data-uri to extract mimetype and the
         * base64 string.
         *
         * For example, given 'data:image/png;base64,iVBORw', it will return
         * ["image/png", "iVBORw"]
         *
         * Parameters
         */
        // For performance reasons, the non-greedy ? qualifiers are crucial so
        // that the matcher stops early on big blobs. Without them, it will try
        // to match the whole blob which can take ages
        var regex = /^data:(.+?\/.+?);base64,/;
        var matches = uri.match(regex);
        var mime = matches[1];
        // matches[0] contains the whole data-uri prefix
        var b64_data = uri.slice(matches[0].length);
        return [mime, b64_data];
    };
    
    var time = {};
    time.milliseconds = {};
    time.milliseconds.s = 1000;
    time.milliseconds.m = 60 * time.milliseconds.s;
    time.milliseconds.h = 60 * time.milliseconds.m;
    time.milliseconds.d = 24 * time.milliseconds.h;
    
    time.thresholds = {
        // moment.js thresholds in milliseconds
        s: moment.relativeTimeThreshold('s') * time.milliseconds.s,
        m: moment.relativeTimeThreshold('m') * time.milliseconds.m,
        h: moment.relativeTimeThreshold('h') * time.milliseconds.h,
        d: moment.relativeTimeThreshold('d') * time.milliseconds.d,
    };
    
    time.timeout_from_dt = function (dt) {
        /** compute a timeout based on dt
        
        input and output both in milliseconds
        
        use moment's relative time thresholds:
        
        - 10 seconds if in 'seconds ago' territory
        - 1 minute if in 'minutes ago'
        - 1 hour otherwise
        */
        if (dt < time.thresholds.s) {
            return 10 * time.milliseconds.s;
        } else if (dt < time.thresholds.m) {
            return time.milliseconds.m;
        } else {
            return time.milliseconds.h;
        }
    };

    var format_datetime = function(date) {
        var text = moment(date).fromNow();
        return text === 'a few seconds ago' ? 'seconds ago' : text;
    };

    var datetime_sort_helper = function(a, b, order) {
        if (moment(a).isBefore(moment(b))) {
            return (order == 1) ? -1 : 1;
        } else if (moment(a).isSame(moment(b))) {
            return 0;
        } else {
            return (order == 1) ? 1 : -1;
        }
    };
    
    /**
    source: https://github.com/sindresorhus/pretty-bytes
    The MIT License (MIT)

    Copyright (c) Sindre Sorhus <sindresorhus@gmail.com> (sindresorhus.com)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
    **/
    var format_filesize = function(num) {
      if (num === undefined || num === null)
        return;

      var UNITS = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

      if (!Number.isFinite(num)) {
        console.error("Expected finite number, got ", typeof(num) + ": " + num);
      }

      var neg = num < 0;

      if (neg) {
        num = -num;
      }

      if (num < 1) {
        return (neg ? '-' : '') + num + ' B';
      }

      var exponent = Math.min(Math.floor(Math.log10(num) / 3), UNITS.length - 1);
      var numStr = Number((num / Math.pow(1000, exponent)).toPrecision(3));
      var unit = UNITS[exponent];

      return (neg ? '-' : '') + numStr + ' ' + unit;
    }

    // javascript stores text as utf16 and string indices use "code units",
    // which stores high-codepoint characters as "surrogate pairs",
    // which occupy two indices in the javascript string.
    // We need to translate cursor_pos in the protocol (in characters)
    // to js offset (with surrogate pairs taking two spots).
    function js_idx_to_char_idx (js_idx, text) {
        var char_idx = js_idx;
        for (var i = 0; i + 1 < text.length && i < js_idx; i++) {
            var char_code = text.charCodeAt(i);
            // check for surrogate pair
            if (char_code >= 0xD800 && char_code <= 0xDBFF) {
                var next_char_code = text.charCodeAt(i+1);
                if (next_char_code >= 0xDC00 && next_char_code <= 0xDFFF) {
                    char_idx--;
                    i++;
                }
            }
        }
        return char_idx;
    }

    function char_idx_to_js_idx (char_idx, text) {
        var js_idx = char_idx;
        for (var i = 0; i + 1 < text.length && i < js_idx; i++) {
            var char_code = text.charCodeAt(i);
            // check for surrogate pair
            if (char_code >= 0xD800 && char_code <= 0xDBFF) {
                var next_char_code = text.charCodeAt(i+1);
                if (next_char_code >= 0xDC00 && next_char_code <= 0xDFFF) {
                    js_idx++;
                    i++;
                }
            }
        }
        return js_idx;
    }

    if ('𝐚'.length === 1) {
        // If javascript fixes string indices of non-BMP characters,
        // don't keep shifting offsets to compensate for surrogate pairs
        char_idx_to_js_idx = js_idx_to_char_idx = function (idx, text) { return idx; };
    }

    // Test if a drag'n'drop event contains a file (as opposed to an HTML
    // element/text from the document)
    var dnd_contain_file = function(event) {
        // As per the HTML5 drag'n'drop spec, the dataTransfer.types should
        // contain one "Files" type if a file is being dragged
        // https://www.w3.org/TR/2011/WD-html5-20110113/dnd.html#dom-datatransfer-types
        if (event.dataTransfer.types) {
            for (var i = 0; i < event.dataTransfer.types.length; i++) {
                if (event.dataTransfer.types[i] == "Files") {
                    return true;
                }
            }
        }
        return false;
    };

    var throttle = function(fn, time) {
      var pending = null;

      return function () {
        if (pending) return;
        pending = setTimeout(run, time);

        return function () {
          clearTimeout(pending);
          pending = null;
        }
      }

      function run () {
        pending = null;
        fn();
      }
    }
    
    var change_favicon = function (src) {
        var link = document.createElement('link'),
            oldLink = document.getElementById('favicon');
        link.id = 'favicon';
        link.type = 'image/x-icon';
        link.rel = 'shortcut icon';
        link.href = utils.url_path_join(utils.get_body_data('baseUrl'), src);
        if (oldLink && (link.href === oldLink.href)) {
            // This favicon is already set, don't modify the DOM.
            return;
        }
        if (oldLink) document.head.removeChild(oldLink);
        document.head.appendChild(link);
    };

    var utils = {
        throttle: throttle,
        is_loaded: is_loaded,
        load_extension: load_extension,
        load_extensions: load_extensions,
        filter_extensions: filter_extensions,
        load_extensions_from_config: load_extensions_from_config,
        regex_split : regex_split,
        uuid : uuid,
        fixConsole : fixConsole,
        fixCarriageReturn : fixCarriageReturn,
        fixBackspace : fixBackspace,
        fixOverwrittenChars: fixOverwrittenChars,
        autoLinkUrls : autoLinkUrls,
        points_to_pixels : points_to_pixels,
        get_body_data : get_body_data,
        parse_url : parse_url,
        url_path_split : url_path_split,
        url_path_join : url_path_join,
        url_join_encode : url_join_encode,
        encode_uri_components : encode_uri_components,
        splitext : splitext,
        escape_html : escape_html,
        always_new : always_new,
        to_absolute_cursor_pos : to_absolute_cursor_pos,
        from_absolute_cursor_pos : from_absolute_cursor_pos,
        browser : browser,
        platform: platform,
        get_url_param: get_url_param,
        is_or_has : is_or_has,
        is_focused : is_focused,
        mergeopt: mergeopt,
        requireCodeMirrorMode : requireCodeMirrorMode,
        XHR_ERROR : XHR_ERROR,
        ajax : ajax,
        ajax_error_msg : ajax_error_msg,
        log_ajax_error : log_ajax_error,
        wrap_ajax_error : wrap_ajax_error,
        promising_ajax : promising_ajax,
        WrappedError: WrappedError,
        load_class: load_class,
        resolve_promises_dict: resolve_promises_dict,
        reject: reject,
        typeset: typeset,
        parse_b64_data_uri: parse_b64_data_uri,
        time: time,
        format_datetime: format_datetime,
        format_filesize: format_filesize,
        datetime_sort_helper: datetime_sort_helper,
        dnd_contain_file: dnd_contain_file,
        js_idx_to_char_idx: js_idx_to_char_idx,
        char_idx_to_js_idx: char_idx_to_js_idx,
        _ansispan:_ansispan,
        change_favicon: change_favicon
    };

    return utils;
}); 
