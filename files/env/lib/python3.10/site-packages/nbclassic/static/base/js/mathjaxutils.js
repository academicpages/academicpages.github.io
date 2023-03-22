// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
], function($, utils, i18n, dialog) {
    "use strict";

    var init = function () {
        if (window.MathJax) {
            // MathJax loaded
            MathJax.Hub.Config({
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                TeX: {
                    extensions: ['newcommand.js', 'begingroup.js']  // For \gdef
                },
                MathML: {
                    extensions: ['content-mathml.js']
                },
                // Center justify equations in code and markdown cells. Elsewhere
                // we use CSS to left justify single line equations in code cells.
                displayAlign: 'center',
                "HTML-CSS": {
                    availableFonts: [],
                    imageFont: null,
                    preferredFont: null,
                    webFont: "STIX-Web",
                    styles: {'.MathJax_Display': {"margin": 0}},
                    linebreaks: { automatic: true }
                },
            });
            MathJax.Hub.Configured();
        } else if (window.mathjax_url !== "") {
            // This statement is used simply so that message extraction
            // will pick up the strings.  The actual setting of the text
            // for the button is in dialog.js.
            var button_labels = [ i18n.msg._("OK") ];
            // Don't have MathJax, but should. Show dialog.
            dialog.modal({
                title : i18n.msg.sprintf(i18n.msg._("Failed to retrieve MathJax from '%s'",window.mathjax_url)),
                body : $("<p/>").addClass('dialog').text(
                        i18n.msg._("Math/LaTeX rendering will be disabled.")
                    ),
                buttons : {
                    OK : {class: "btn-danger"}
                }
            });
        }
    };

    // Some magic for deferring mathematical expressions to MathJax
    // by hiding them from the Markdown parser.
    // Some of the code here is adapted with permission from Davide Cervone
    // under the terms of the Apache2 license governing the MathJax project.
    // Other minor modifications are also due to StackExchange and are used with
    // permission.

    // MATHSPLIT contains the pattern for math delimiters and special symbols
    // needed for searching for math in the text input.
    var MATHSPLIT = /(\$\$?|\\(?:begin|end)\{[a-z]*\*?\}|\\[{}$]|[{}]|(?:\n\s*)+|@@\d+@@|\\\\(?:\(|\)|\[|\]))/i;

    //  The math is in blocks i through j, so
    //    collect it into one block and clear the others.
    //  Replace &, <, and > by named entities.
    //  For IE, put <br> at the ends of comments since IE removes \n.
    //  Clear the current math positions and store the index of the
    //    math, then push the math string onto the storage array.
    //  The preProcess function is called on all blocks if it has been passed in
    var process_math = function (i, j, pre_process, math, blocks) {
        var block = blocks.slice(i, j + 1).join("").replace(/&/g, "&amp;") // use HTML entity for &
        .replace(/</g, "&lt;") // use HTML entity for <
        .replace(/>/g, "&gt;") // use HTML entity for >
        ;
        if (utils.browser === 'msie') {
            block = block.replace(/(%[^\n]*)\n/g, "$1<br/>\n");
        }
        while (j > i) {
            blocks[j] = "";
            j--;
        }
        blocks[i] = "@@" + math.length + "@@"; // replace the current block text with a unique tag to find later
        if (pre_process){
            block = pre_process(block);
        }
        math.push(block);
        return blocks;
    };

    //  Break up the text into its component parts and search
    //    through them for math delimiters, braces, linebreaks, etc.
    //  Math delimiters must match and braces must balance.
    //  Don't allow math to pass through a double linebreak
    //    (which will be a paragraph).
    //
    var remove_math = function (text) {
        var math = []; // stores math strings for later
        var start;
        var end;
        var last;
        var braces;

        // Except for extreme edge cases, this should catch precisely those pieces of the markdown
        // source that will later be turned into code spans. While MathJax will not TeXify code spans,
        // we still have to consider them at this point; the following issue has happened several times:
        //
        //     `$foo` and `$bar` are varibales.  -->  <code>$foo ` and `$bar</code> are variables.

        var hasCodeSpans = /`/.test(text),
            de_tilde;
        if (hasCodeSpans) {
            var tilde = function (wholematch) {
                return wholematch.replace(/\$/g, "~D");
            }
            text = text.replace(/~/g, "~T")
                       .replace(/(^|[^\\])(`+)([^\n]*?[^`\n])\2(?!`)/gm, tilde)
                       .replace(/^\s{0,3}(`{3,})(.|\n)*?\1/gm, tilde);
            de_tilde = function (text) {
                return text.replace(/~([TD])/g, function (wholematch, character) {
                                                    return { T: "~", D: "$" }[character];
                                                });
            };
        } else {
            de_tilde = function (text) { return text; };
        }

        var blocks = utils.regex_split(text.replace(/\r\n?/g, "\n"),MATHSPLIT);

        for (var i = 1, m = blocks.length; i < m; i += 2) {
            var block = blocks[i];
            if (block.charAt(0) === "@") {
                //
                //  Things that look like our math markers will get
                //  stored and then retrieved along with the math.
                //
                blocks[i] = "@@" + math.length + "@@";
                math.push(block);
            }
            else if (start) {
                //
                //  If we are in math, look for the end delimiter,
                //    but don't go past double line breaks, and
                //    and balance braces within the math.
                //
                if (block === end) {
                    if (braces) {
                        last = i;
                    }
                    else {
                        blocks = process_math(start, i, de_tilde, math, blocks);
                        start  = null;
                        end    = null;
                        last   = null;
                    }
                }
                else if (block.match(/\n.*\n/)) {
                    if (last) {
                        i = last;
                        blocks = process_math(start, i, de_tilde, math, blocks);
                    }
                    start = null;
                    end = null;
                    last = null;
                    braces = 0;
                }
                else if (block === "{") {
                    braces++;
                }
                else if (block === "}" && braces) {
                    braces--;
                }
            }
            else {
                //
                //  Look for math start delimiters and when
                //    found, set up the end delimiter.
                //
                if (block === "$" || block === "$$") {
                    start = i;
                    end = block;
                    braces = 0;
                }
                else if (block === "\\\\\(" || block === "\\\\\[") {
                    start = i;
                    end = block.slice(-1) === "(" ? "\\\\\)" : "\\\\\]";
                    braces = 0;
                }
                else if (block.substr(1, 5) === "begin") {
                    start = i;
                    end = "\\end" + block.substr(6);
                    braces = 0;
                }
            }
        }
        if (last) {
            blocks = process_math(start, last, de_tilde, math, blocks);
            start  = null;
            end    = null;
            last   = null;
        }
        return [de_tilde(blocks.join("")), math];
    };

    //
    //  Put back the math strings that were saved,
    //    and clear the math array (no need to keep it around).
    //
    var replace_math = function (text, math) {
        //
        //  Replaces a math placeholder with its corresponding group.
        //  The math delimiters "\\(", "\\[", "\\)" and "\\]" are replaced
        //  removing one backslash in order to be interpreted correctly by MathJax.
        //
        var math_group_process = function (match, n) {
            var math_group = math[n];

            if (math_group.substr(0, 3) === "\\\\\("  && math_group.substr(math_group.length - 3) === "\\\\\)") {
                math_group = "\\\(" + math_group.substring(3, math_group.length - 3) + "\\\)";
            } else if (math_group.substr(0, 3) === "\\\\\[" && math_group.substr(math_group.length - 3) === "\\\\\]") {
                math_group = "\\\[" + math_group.substring(3, math_group.length - 3) + "\\\]";
            }
            
            return math_group;
        };

        // Replace all the math group placeholders in the text
        // with the saved strings.
        text = text.replace(/@@(\d+)@@/g, math_group_process);
        
        return text;
    };

    var mathjaxutils = {
        init : init,
        remove_math : remove_math,
        replace_math : replace_math
    };

    return mathjaxutils;
});
