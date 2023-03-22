// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// highly adapted for codemiror jshint
define(['codemirror/lib/codemirror'], function(CodeMirror) {
    "use strict";

    var forEach = function(arr, f) {
        for (var i = 0, e = arr.length; i < e; ++i) f(arr[i]);
    };

    var arrayContains = function(arr, item) {
        if (!Array.prototype.indexOf) {
            var i = arr.length;
            while (i--) {
                if (arr[i] === item) {
                    return true;
                }
            }
            return false;
        }
        return arr.indexOf(item) != -1;
    };

    CodeMirror.contextHint = function (editor) {
        // Find the token at the cursor
        var cur = editor.getCursor(),
            token = editor.getTokenAt(cur),
            tprop = token;
        // If it's not a 'word-style' token, ignore the token.
        // If it is a property, find out what it is a property of.
        var list = [];
        var clist = getCompletions(token, editor);
        for (var i = 0; i < clist.length; i++) {
            list.push({
                str: clist[i],
                type: "context",
                from: {
                    line: cur.line,
                    ch: token.start
                },
                to: {
                    line: cur.line,
                    ch: token.end
                }
            });
        }
        return list;
    };

    // find all 'words' of current cell
    var getAllTokens = function (editor) {
        var found = [];

        // add to found if not already in it


        function maybeAdd(str) {
            if (!arrayContains(found, str)) found.push(str);
        }

        // loop through all token on all lines
        var lineCount = editor.lineCount();
        // loop on line
        for (var l = 0; l < lineCount; l++) {
            var line = editor.getLine(l);
            //loop on char
            for (var c = 1; c < line.length; c++) {
                var tk = editor.getTokenAt({
                    line: l,
                    ch: c
                });
                // if token has a class, it has geat chances of beeing
                // of interest. Add it to the list of possible completions.
                // we could skip token of ClassName 'comment'
                // or 'number' and 'operator'
                if (tk.className !== null) {
                    maybeAdd(tk.string);
                }
                // jump to char after end of current token
                c = tk.end;
            }
        }
        return found;
    };

    var getCompletions = function(token, editor) {
        var candidates = getAllTokens(editor);
        // filter all token that have a common start (but nox exactly) the length of the current token
        var lambda = function (x) {
                return (x.indexOf(token.string) === 0 && x != token.string);
            };
        var filterd = candidates.filter(lambda);
        return filterd;
    };

    return {'contextHint': CodeMirror.contextHint};
});
