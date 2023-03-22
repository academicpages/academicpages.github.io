// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'components/sanitizer/index',
], function($, sanitizer) {
    "use strict";

    var noop = function (x) { return x; };
    var defaultSanitizer = sanitizer.defaultSanitizer;

    var sanitize_html = function (html, allow_css) {
        /**
         * sanitize HTML
         * if allow_css is true (default: false), CSS is sanitized as well.
         * otherwise, CSS elements and attributes are simply removed.
         */
         const options = {};
         if (!allow_css) {
             options.allowedStyles = {};
         }
        return defaultSanitizer.sanitize(html, options);
    };

    var sanitize_html_and_parse = function (html, allow_css) {
        /**
         * Sanitize HTML and parse it safely using jQuery.
         *
         * This disable's jQuery's html 'prefilter', which can make invalid
         * HTML valid after the sanitizer has checked it.
         *
         * Returns an array of DOM nodes.
         */
        var sanitized_html = sanitize_html(html, allow_css);
        var prev_htmlPrefilter = $.htmlPrefilter;
        $.htmlPrefilter = function(html) {return html;};  // Don't modify HTML
        try {
            return $.parseHTML(sanitized_html);
        } finally {
            $.htmlPrefilter = prev_htmlPrefilter;  // Set it back again
        }
    };

    var security = {
        sanitize_html_and_parse: sanitize_html_and_parse,
        sanitize_html: sanitize_html
    };

    return security;
});
