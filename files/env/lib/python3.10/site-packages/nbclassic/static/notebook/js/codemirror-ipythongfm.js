// IPython GFM (GitHub Flavored Markdown) mode is just a slightly altered GFM
// Mode with support for latex.
//
// Latex support was supported by Codemirror GFM as of
//   https://github.com/codemirror/CodeMirror/pull/567
// But was later removed in
//   https://github.com/codemirror/CodeMirror/commit/d9c9f1b1ffe984aee41307f3e927f80d1f23590c


(function(mod) {
  if (typeof exports == "object" && typeof module == "object"){ // CommonJS
    mod(requirejs("codemirror/lib/codemirror")
        ,requirejs("codemirror/addon/mode/multiplex")
        ,requirejs("codemirror/mode/gfm/gfm")
        ,requirejs("codemirror/mode/stex/stex")
        );
  } else if (typeof define == "function" && define.amd){ // AMD
    define(["codemirror/lib/codemirror"
            ,"codemirror/addon/mode/multiplex"
            ,"codemirror/mode/python/python"
            ,"codemirror/mode/stex/stex"
            ], mod);
  } else {// Plain browser env
    mod(CodeMirror);
  }
})( function(CodeMirror){
    "use strict";

    CodeMirror.defineMode("ipythongfm", function(config, parserConfig) {

        var gfm_mode = CodeMirror.getMode(config, "gfm");
        var tex_mode = CodeMirror.getMode(config, "stex");

        return CodeMirror.multiplexingMode(
            gfm_mode,
            // By defining the $$ delimiter before the $ delimiter we don't run
            // into the problem that $$ is interpreted as two consecutive $.
            {
                open: "$$", close: "$$",
                mode: tex_mode,
                delimStyle: "delimit"
            },
            {
                open: "$", close: "$",
                mode: tex_mode,
                delimStyle: "delimit"
            },
            {
                open: "\\(", close: "\\)",
                mode: tex_mode,
                delimStyle: "delimit"
            },
            {
                open: "\\[", close: "\\]",
                mode: tex_mode,
                delimStyle: "delimit"
            }
            // .. more multiplexed styles can follow here
        );
    }, 'gfm');

    CodeMirror.defineMIME("text/x-ipythongfm", "ipythongfm");
})
