//
// Various output tests
//

casper.notebook_test(function () {
    
    this.compare_outputs = function(results, expected) {
        for (var i = 0; i < results.length; i++) {
            var r = results[i];
            var ex = expected[i];
            this.test.assertEquals(r.output_type, ex.output_type, "output  " + i + " = " + r.output_type);
            if (r.output_type === 'stream') {
                this.test.assertEquals(r.name, ex.name, "stream  " + i + " = " + r.name);
                this.test.assertEquals(r.text, ex.text, "content " + i);
            }
        }
    }
    this.test_coalesced_output = function (msg, code, expected) {
        this.then(function () {
            this.echo("Test coalesced output: " + msg);
        });
        
        this.thenEvaluate(function (code) {
            IPython.notebook.insert_cell_at_index("code", 0);
            var cell = IPython.notebook.get_cell(0);
            cell.set_text(code);
            cell.execute();
        }, {code: code});
        
        this.wait_for_output(0);
        
        this.then(function () {
            var results = this.evaluate(function () {
                var cell = IPython.notebook.get_cell(0);
                return cell.output_area.outputs;
            });
            this.test.assertEquals(results.length, expected.length, "correct number of outputs");
            this.compare_outputs(results, expected);
        });
        
    };

    this.thenEvaluate(function () {
        IPython.notebook.insert_cell_at_index("code", 0);
        var cell = IPython.notebook.get_cell(0);
        cell.set_text([
            "import sys",
            "from IPython.display import display, clear_output"
            ].join("\n")
        );
        cell.execute();
    });

    this.test_coalesced_output("stdout", [
        "print(1)",
        "sys.stdout.flush()",
        "print(2)",
        "sys.stdout.flush()",
        "print(3)"
        ].join("\n"), [{
            output_type: "stream",
            name: "stdout",
            text: "1\n2\n3\n"
        }]
    );
    
    this.test_coalesced_output("stdout+sdterr", [
        "print(1)",
        "sys.stdout.flush()",
        "print(2)",
        "print(3, file=sys.stderr)"
        ].join("\n"), [{
            output_type: "stream",
            name: "stdout",
            text: "1\n2\n"
        },{
            output_type: "stream",
            name: "stderr",
            text: "3\n"
        }]
    );

    this.test_coalesced_output("display splits streams", [
        "print(1)",
        "sys.stdout.flush()",
        "display(2)",
        "print(3)"
        ].join("\n"), [{
            output_type: "stream",
            name: "stdout",
            text: "1\n"
        },{
            output_type: "display_data",
        },{
            output_type: "stream",
            name: "stdout",
            text: "3\n"
        }]
    );
    this.test_coalesced_output("test nested svg", [
        'from IPython.display import SVG',
        'nested_svg="""',
        '<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100" >',
        '  <svg x="0">',
        '    <rect x="10" y="10" height="80" width="80" style="fill: #0000ff"/>',
        '  </svg>',
        '  <svg x="100">',
        '    <rect x="10" y="10" height="80" width="80" style="fill: #00cc00"/>',
        '  </svg>',
        '</svg>"""',
        'SVG(nested_svg)'
        ].join("\n"), [{
            output_type: "execute_result",
            data: { 
            "text/plain" : "<IPython.core.display.SVG object>",
            "image/svg+xml": [
              '<svg height="200" width="100" xmlns="http://www.w3.org/2000/svg">',
              '  <svg x="0">',
              '    <rect height="80" style="fill: #0000ff" width="80" x="10" y="10"/>',
              '  </svg>',
              '  <svg x="100">',
              '    <rect height="80" style="fill: #00cc00" width="80" x="10" y="10"/>',
              '  </svg>',
              '</svg>'].join("\n")
            },
        }]
    );

    this.then(function () {
        this.echo("Test output callback overrides");
    });

    this.thenEvaluate(function () {
        IPython.notebook.insert_cell_at_index("code", 0);
        var cell = IPython.notebook.get_cell(0);
        cell.set_text(["print(1)",
        "sys.stdout.flush()",
        "print(2)",
        "sys.stdout.flush()",
        "print(3, file=sys.stderr)",
        "sys.stdout.flush()",
        "display(2)",
        "clear_output()",
        "sys.stdout.flush()",
        "print('remove handler')",
        "sys.stdout.flush()",
        "print('back to cell')",
        "sys.stdout.flush()",
        ].join('\n'));
        cell.execute();
        var kernel = IPython.notebook.kernel;
        var msg_id = cell.last_msg_id;
        var callback_id = 'mycallbackid'
        cell.iopub_messages = [];
        var add_msg = function(msg) {
            if (msg.content.text==="remove handler\n") {
                kernel.output_callback_overrides_pop(msg_id);
            }
            msg.content.output_type = msg.msg_type;
            cell.iopub_messages.push(msg.content);
        };
        kernel.set_callbacks_for_msg(callback_id, {
            iopub: {
                output: add_msg,
                clear_output: add_msg,
            }
        }, false);
        kernel.output_callback_overrides_push(msg_id, callback_id);
    });
    
    this.wait_for_idle();
    
    this.then(function () {
        var expected_callback = [{
            output_type: "stream",
            name: "stdout",
            text: "1\n"
        }, {
            output_type: "stream",
            name: "stdout",
            text: "2\n"
        }, {
            output_type: "stream",
            name: "stderr",
            text: "3\n"
        },{
            output_type: "display_data",
        },{
            output_type: "clear_output",
        },{
            output_type: "stream",
            name: "stdout",
            text: "remove handler\n"
        },]
        var expected_cell = [{
            output_type: "stream",
            name: "stdout",
            text: "back to cell\n"
        }]
        var returned = this.evaluate(function () {
            var cell = IPython.notebook.get_cell(0);
            return [cell.output_area.outputs, cell.iopub_messages];
        });
        var cell_results = returned[0];
        var callback_results = returned[1];
        this.test.assertEquals(cell_results.length, expected_cell.length, "correct number of cell outputs");
        this.test.assertEquals(callback_results.length, expected_callback.length, "correct number of callback outputs");
        this.compare_outputs(cell_results, expected_cell);
        this.compare_outputs(callback_results, expected_callback);
    });

    this.then(function () {
        this.echo("Test output callback overrides get execute_results messages too");
    });

    this.thenEvaluate(function () {
        IPython.notebook.insert_cell_at_index("code", 0);
        var cell = IPython.notebook.get_cell(0);
        cell.set_text("'end'");
        cell.execute();
        var kernel = IPython.notebook.kernel;
        var msg_id = cell.last_msg_id;
        var callback_id = 'mycallbackid2'
        cell.iopub_messages = [];
        var add_msg = function(msg) {
            msg.content.output_type = msg.msg_type;
            cell.iopub_messages.push(msg.content);
        };
        kernel.set_callbacks_for_msg(callback_id, {
            iopub: {
                output: add_msg,
                clear_output: add_msg,
            }
        }, false);
        kernel.output_callback_overrides_push(msg_id, callback_id);
    });
    
    this.wait_for_idle();
    
    this.then(function () {
        var expected_callback = [{
            output_type: "execute_result",
            data: {
            "text/plain" : "'end'"
            }
        }];
        var expected_cell = [];
        var returned = this.evaluate(function () {
            var cell = IPython.notebook.get_cell(0);
            return [cell.output_area.outputs, cell.iopub_messages];
        });
        var cell_results = returned[0];
        var callback_results = returned[1];
        this.test.assertEquals(cell_results.length, expected_cell.length, "correct number of cell outputs");
        this.test.assertEquals(callback_results.length, expected_callback.length, "correct number of callback outputs");
        this.compare_outputs(callback_results, expected_callback);
    });
});
