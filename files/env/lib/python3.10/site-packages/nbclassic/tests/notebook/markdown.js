//
// Test that a Markdown cell is rendered to HTML.
//
casper.notebook_test(function () {
    "use strict";

    var text = 'multi\nline';
    this.evaluate(function (text) {
        var cell = IPython.notebook.insert_cell_at_index('markdown', 0);
        cell.set_text(text);
    }, {text: text});

    // Test markdown code blocks
    function mathjax_render_test(input_string, result, message){
      casper.thenEvaluate(function (text){
        window._test_result = null;
        require(['base/js/mathjaxutils'],function(mathjaxutils){
          window._test_result = mathjaxutils.remove_math(text);
        });
      }, {text: input_string});
      casper.waitFor(function() {
        return casper.evaluate(function(){
          return window._test_result!==null;
        });
      });
      casper.then(function(){
        var return_val = casper.evaluate(function(){
          var blah = window._test_result;
          delete window._test_result;
          return blah;
        });
        this.test.assertEquals(return_val[0], result[0], message+" markdown");
        this.test.assertEquals(return_val[1].length, result[1].length, message+" math instance count");
        for(var i=0; i<return_val[1].length; i++){
          this.test.assertEquals(return_val[1][i], result[1][i], message+" math instance "+i);
        };
      });
    };
    var input_string_1 = 'x \\\\(a_{0}+ b_{T}\\\\) y \\\\(a_{0}+  b_{T}\\\\) z';
    var expected_result_1 = ['x @@0@@ y @@1@@ z', ['\\\\(a_{0}+ b_{T}\\\\)','\\\\(a_{0}+  b_{T}\\\\)']];
    var message_1 = "multiple inline(LaTeX style) with underscores";
    
    var input_string_2 = 'x \\\\[a_{0}+ b_{T}\\\\] y \\\\[a_{0}+  b_{T}\\\\] z';
    var expected_result_2 = ['x @@0@@ y @@1@@ z', ['\\\\[a_{0}+ b_{T}\\\\]','\\\\[a_{0}+  b_{T}\\\\]']];
    var message_2 = "multiple equation (LaTeX style) with underscores";

    var input_string_3 = 'x $a_{0}+ b_{T}$ y $a_{0}+  b_{T}$ z';
    var expected_result_3 = ['x @@0@@ y @@1@@ z',['$a_{0}+ b_{T}$','$a_{0}+  b_{T}$']];
    var message_3 = "multiple inline(TeX style) with underscores";
    
    var input_string_4 = 'x $$a_{0}+ b_{T}$$ y $$a_{0}+  b_{T}$$ z';
    var expected_result_4 = ['x @@0@@ y @@1@@ z', ['$$a_{0}+ b_{T}$$','$$a_{0}+  b_{T}$$']];
    var message_4 = "multiple equation(TeX style) with underscores";

    var input_string_5 = 'x \\begin{equation}a_{0}+ b_{T}\\end{equation} y \\begin{equation}a_{0}+  b_{T}\\end{equation} z';
    var expected_result_5 = ['x @@0@@ y @@1@@ z',['\\begin{equation}a_{0}+ b_{T}\\end{equation}','\\begin{equation}a_{0}+  b_{T}\\end{equation}']];
    var message_5 = "multiple equations with underscores";

    mathjax_render_test(input_string_1, expected_result_1, message_1);
    mathjax_render_test(input_string_2, expected_result_2, message_2);
    mathjax_render_test(input_string_3, expected_result_3, message_3);
    mathjax_render_test(input_string_4, expected_result_4, message_4);
    mathjax_render_test(input_string_5, expected_result_5, message_5);
});
