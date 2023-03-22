// Test opening a rich notebook, saving it, and reopening it again.
//
//toJSON fromJSON toJSON and do a string comparison


// this is just a copy of OutputArea.mime_mape_r in IPython/html/static/notebook/js/outputarea.js
mime =  {
        "text" : "text/plain",
        "html" : "text/html",
        "svg" : "image/svg+xml",
        "png" : "image/png",
        "jpeg" : "image/jpeg",
        "latex" : "text/latex",
        "json" : "application/json",
        "javascript" : "application/javascript",
    };

var black_dot_jpeg="u\"\"\"/9j/4AAQSkZJRgABAQEASABIAAD/2wBDACodICUgGiolIiUvLSoyP2lEPzo6P4FcYUxpmYagnpaG\nk5GovfLNqLPltZGT0v/V5fr/////o8v///////L/////2wBDAS0vLz83P3xERHz/rpOu////////\n////////////////////////////////////////////////////////////wgARCAABAAEDAREA\nAhEBAxEB/8QAFAABAAAAAAAAAAAAAAAAAAAABP/EABQBAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEA\nAhADEAAAARn/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAEFAn//xAAUEQEAAAAAAAAAAAAA\nAAAAAAAA/9oACAEDAQE/AX//xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAECAQE/AX//xAAUEAEA\nAAAAAAAAAAAAAAAAAAAA/9oACAEBAAY/An//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/\nIX//2gAMAwEAAgADAAAAEB//xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAEDAQE/EH//xAAUEQEA\nAAAAAAAAAAAAAAAAAAAA/9oACAECAQE/EH//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/\nEH//2Q==\"\"\"";
var black_dot_png = 'u\"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEUAAACnej3aAAAAAWJLR0QA\\niAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB94BCRQnOqNu0b4AAAAKSURBVAjXY2AA\\nAAACAAHiIbwzAAAAAElFTkSuQmCC\"';
var svg = "\"<svg width='1cm' height='1cm' viewBox='0 0 1000 500'><defs><style>rect {fill:red;}; </style></defs><rect id='r1' x='200' y='100' width='600' height='300' /></svg>\"";

// helper function to ensure that the short_name is found in the toJSON
// representation, while the original in-memory cell retains its long mimetype
// name, and that fromJSON also gets its long mimetype name
function assert_has(short_name, json, result, result2) {
    var long_name = mime[short_name];
    this.test.assertFalse(json[0].data.hasOwnProperty(short_name),
            "toJSON()   representation doesn't use " + short_name);
    this.test.assertTrue(json[0].data.hasOwnProperty(long_name),
            'toJSON()   representation uses ' + long_name);
    this.test.assertTrue(result.data.hasOwnProperty(long_name),
            'toJSON()   original embedded JSON keeps ' + long_name);
    this.test.assertTrue(result2.data.hasOwnProperty(long_name),
            'fromJSON() embedded ' + short_name + ' gets mime key ' + long_name);
}
          
// helper function for checkout that the first two cells have a particular
// output_type (either 'execute_result' or 'display_data'), and checks the to/fromJSON
// for a set of mimetype keys, ensuring the old short names ('javascript', 'text',
// 'png', etc) are not used.
function check_output_area(output_type, keys) {
    this.wait_for_output(0);
    var json = this.evaluate(function() {
        var json = IPython.notebook.get_cell(0).output_area.toJSON();
        // appended cell will initially be empty, let's add some output
        IPython.notebook.get_cell(1).output_area.fromJSON(json);
        return json;
    });
    // The evaluate call above happens asynchronously: wait for cell[1] to have output
    this.wait_for_output(1);
    var result = this.get_output_cell(0);
    var result2 = this.get_output_cell(1);
    this.test.assertEquals(result.output_type, output_type,
        'testing ' + output_type + ' for ' + keys.join(' and '));

    for (var idx in keys) {
        assert_has.apply(this, [keys[idx], json, result, result2]);
    }
}


// helper function to clear the first two cells, set the text of and execute
// the first one
function clear_and_execute(that, code) {
    that.evaluate(function() {
        IPython.notebook.get_cell(0).clear_output();
        IPython.notebook.get_cell(1).clear_output();
    });
    that.then(function () {
        that.set_cell_text(0, code);
        that.execute_cell(0);
        that.wait_for_idle();
    });
}

casper.notebook_test(function () {
    this.evaluate(function () {
        var cell = IPython.notebook.get_cell(0);
        // "we have to make messes to find out who we are"
        cell.set_text([
            "%%javascript",
            "IPython.notebook.insert_cell_below('code')"
            ].join('\n')
            );
    });

    this.execute_cell_then(0, function () {
        var result = this.get_output_cell(0);
        var num_cells = this.get_cells_length();
        this.test.assertEquals(num_cells, 2, '%%javascript magic works');
        this.test.assertTrue(result.data.hasOwnProperty('application/javascript'),
            'testing JS embedded with mime key');
    });

    //this.thenEvaluate(function() { IPython.notebook.save_notebook(); });
    this.then(function () {
        clear_and_execute(this, [
            "%%javascript",
            "var a=5;"
            ].join('\n'));
    });
   

    this.then(function () {
        check_output_area.apply(this, ['display_data', ['javascript']]);

    });

    this.then(function() {
        clear_and_execute(this, '%lsmagic');
    });
   
    this.then(function () {
        check_output_area.apply(this, ['execute_result', ['text', 'json']]);
    });

    this.then(function() {
        clear_and_execute(this,
            "x = %lsmagic\nfrom IPython.display import display; display(x)");
    });

    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'json']]);
    });
    
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Latex; Latex('$X^2$')");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['execute_result', ['text', 'latex']]);
    });

    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Latex, display; display(Latex('$X^2$'))");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'latex']]);
    });
    
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import HTML; HTML('<b>it works!</b>')");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['execute_result', ['text', 'html']]);
    });

    this.then(function() {
        clear_and_execute(this,
            "from base64 import b64decode;" + 
            "black_dot_png = b64decode(" + black_dot_png + ");" + 
            "black_dot_jpeg = b64decode(" + black_dot_jpeg + ")"
        );
    });
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import HTML, display; display(HTML('<b>it works!</b>'))");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'html']]);
    });


    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Image; Image(black_dot_png)");
    });
    this.thenEvaluate(function() { IPython.notebook.save_notebook(); });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['execute_result', ['text', 'png']]);
    });
    
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Image, display; display(Image(black_dot_png))");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'png']]);
    });


    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Image; Image(black_dot_jpeg, format='jpeg')");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['execute_result', ['text', 'jpeg']]);
    });
    
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import Image, display; display(Image(black_dot_jpeg, format='jpeg'))");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'jpeg']]);
    });
    
    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import SVG; SVG(" + svg + ")");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['execute_result', ['text', 'svg']]);
    });

    this.then(function() {
        clear_and_execute(this,
            "from IPython.display import SVG, display; display(SVG(" + svg + "))");
    });
    
    this.then(function ( ) {
        check_output_area.apply(this, ['display_data', ['text', 'svg']]);
    });
    
    this.thenEvaluate(function() { IPython.notebook.save_notebook(); });

    this.then(function() {
        clear_and_execute(this, [
            "from IPython.core.formatters import HTMLFormatter",
            "x = HTMLFormatter()",
            "x.format_type = 'text/superfancymimetype'",
            "get_ipython().display_formatter.formatters['text/superfancymimetype'] = x",
            "from IPython.display import HTML, display",
            'display(HTML("yo"))',
            "HTML('hello')"].join('\n')
            );
             
    });
    
    this.wait_for_output(0, 1);
    
    this.then(function () {
        var long_name = 'text/superfancymimetype';
        var result = this.get_output_cell(0);
        this.test.assertTrue(result.data.hasOwnProperty(long_name),
            'display_data custom mimetype ' + long_name);
        result = this.get_output_cell(0, 1);
        this.test.assertTrue(result.data.hasOwnProperty(long_name),
            'execute_result custom mimetype ' + long_name);
    
    });
    
});
