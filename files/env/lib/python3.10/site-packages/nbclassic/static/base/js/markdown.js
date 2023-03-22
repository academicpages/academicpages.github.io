// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/mathjaxutils',
    'base/js/security',
    'components/marked/lib/marked',
    'codemirror/lib/codemirror',
], function($, utils, mathjaxutils, security, marked, CodeMirror){
    "use strict";

    marked.setOptions({
        gfm : true,
        tables: true,
        langPrefix: "cm-s-ipython language-",
        highlight: function(code, lang, callback) {
            if (!lang) {
                // no language, no highlight
                if (callback) {
                    callback(null, code);
                    return;
                } else {
                    return code;
                }
            }
            utils.requireCodeMirrorMode(lang, function (spec) {
                var el = document.createElement("div");
                var mode = CodeMirror.getMode({}, spec);
                if (!mode) {
                    console.log("No CodeMirror mode: " + lang);
                    callback(null, code);
                    return;
                }
                try {
                    CodeMirror.runMode(code, spec, el);
                    callback(null, el.innerHTML);
                } catch (err) {
                    console.log("Failed to highlight " + lang + " code", err);
                    callback(err, code);
                }
            }, function (err) {
                console.log("No CodeMirror mode: " + lang);
                console.log("Require CodeMirror mode error: " + err);
                callback(null, code);
            });
        }
    });

    var mathjax_init_done = false;
    function ensure_mathjax_init() {
        if(!mathjax_init_done) {
            mathjax_init_done = true;
            mathjaxutils.init();
        }
    }

    function render(markdown, options, callback) {
        /**
         * Find a readme in the current directory. Look for files with
         * a name like 'readme.md' (case insensitive) or similar and
         * mimetype 'text/markdown'.
         * 
         * @param markdown: the markdown text to parse
         * @param options
         *  Object with parameters:
         *      with_math: the markdown can contain mathematics
         *      clean_tables: prevent default inline styles for table cells
         *      sanitize: remove dangerous html (like <script>)
         * @param callback
         *  A function with two arguments (err, html)
         *      err: null or the error if there was one
         *      html: the rendered html string, or if {sanitize: true} was used
        *             a sanitized jQuery object
         */
        options = $.extend({
            // Apply mathjax transformation
            with_math: false,
            // Prevent marked from returning inline styles for table cells
            clean_tables: false,
            // Apply sanitation, this will return a jQuery object.
            sanitize: false,
        }, options);
        var renderer = new marked.Renderer();
        if(options.clean_tables) {
            renderer.tablecell = function (content, flags) {
            var type = flags.header ? 'th' : 'td';
            var style = flags.align == null ? '': ' style="text-align: ' + flags.align + '"';
            var start_tag = '<' + type + style + '>';
            var end_tag = '</' + type + '>\n';
            return start_tag + content + end_tag;
            };
        }
        var text = markdown;
        var math = null;
        if(options.with_math) {
            ensure_mathjax_init();
            var text_and_math = mathjaxutils.remove_math(markdown);
            text = text_and_math[0];
            math = text_and_math[1];
        }
        marked(text, { renderer: renderer }, function (err, html) {
            if(!err) {
                if(options.with_math) {
                    html = mathjaxutils.replace_math(html, math);
                }
                if(options.sanitize) {
                    html = $(security.sanitize_html_and_parse(html, true));
                }
            }
            callback(err, html);
        });
    }

    return {'render': render};
});
