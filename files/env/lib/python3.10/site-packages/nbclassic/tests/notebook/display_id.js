//
// Various output tests
//

casper.notebook_test(function () {
    
    function get_outputs(cell_idx) {
        var outputs_json = casper.evaluate(function (cell_idx) {
            var cell = Jupyter.notebook.get_cell(cell_idx);
            return JSON.stringify(cell.output_area.outputs);
        }, {cell_idx: cell_idx});
        return JSON.parse(outputs_json);
    }
    
    this.thenEvaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 0);
        var cell = Jupyter.notebook.get_cell(0);
        cell.set_text([
            "ip = get_ipython()",
            "from IPython.display import display",
            "def display_with_id(obj, display_id, update=False, execute_result=False):",
            "  iopub = ip.kernel.iopub_socket",
            "  session = get_ipython().kernel.session",
            "  data, md = ip.display_formatter.format(obj)",
            "  transient = {'display_id': display_id}",
            "  content = {'data': data, 'metadata': md, 'transient': transient}",
            "  if execute_result:",
            "    msg_type = 'execute_result'",
            "    content['execution_count'] = ip.execution_count",
            "  else:",
            "    msg_type = 'update_display_data' if update else 'display_data'",
            "  session.send(iopub, msg_type, content, parent=ip.parent_header)",
            "",
        ].join('\n'));
        cell.execute();
    });

    this.thenEvaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 1);
        var cell = Jupyter.notebook.get_cell(1);
        cell.set_text([
            "display('above')",
            "display_with_id(1, 'here')",
            "display('below')",
        ].join('\n'));
        cell.execute();
    });

    this.wait_for_output(1);
    this.wait_for_idle()

    this.then(function () {
        var outputs = get_outputs(1);
        this.test.assertEquals(outputs.length, 3, 'cell 1 has the right number of outputs');
        this.test.assertEquals(outputs[1].transient.display_id, 'here', 'has transient display_id');
        this.test.assertEquals(outputs[1].data['text/plain'], '1', 'display_with_id produces output');
    });


    this.thenEvaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 2);
        var cell = Jupyter.notebook.get_cell(2);
        cell.set_text([
            "display_with_id(2, 'here')",
            "display_with_id(3, 'there')",
            "display_with_id(4, 'here')",
        ].join('\n'));
        cell.execute();
    });

    this.wait_for_output(2);
    this.wait_for_idle();

    this.then(function () {
        var outputs1 = get_outputs(1);
        this.test.assertEquals(outputs1[1].data['text/plain'], '4', '');
        this.test.assertEquals(outputs1.length, 3, 'cell 1 still has the right number of outputs');
        var outputs2 = get_outputs(2);
        this.test.assertEquals(outputs2.length, 3, 'cell 2 has the right number of outputs');
        this.test.assertEquals(outputs2[0].transient.display_id, 'here', 'check display id 0');
        this.test.assertEquals(outputs2[0].data['text/plain'], '4', 'output[2][0]');
        this.test.assertEquals(outputs2[1].transient.display_id, 'there', 'display id 1');
        this.test.assertEquals(outputs2[1].data['text/plain'], '3', 'output[2][1]');
        this.test.assertEquals(outputs2[2].transient.display_id, 'here', 'display id 2');
        this.test.assertEquals(outputs2[2].data['text/plain'], '4', 'output[2][2]');
    });

    this.then(function () {
        this.echo("Test output callback overrides work with display ids");
    });

    this.thenEvaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 3);
        var cell = Jupyter.notebook.get_cell(3);
        cell.set_text([
            "display_with_id(5, 'here')",
            "display_with_id(6, 'here', update=True)",
        ].join('\n'));
        cell.execute();
        var kernel = IPython.notebook.kernel;
        var msg_id = cell.last_msg_id;
        var callback_id = 'mycallbackid'
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

    this.waitFor(function () {
        return this.evaluate(function () {
            var cell = IPython.notebook.get_cell(3);
            return cell.iopub_messages.length >= 2;
        });
    });
    this.wait_for_idle();

    this.then(function () {
        var returned = this.evaluate(function () {
            var cell = IPython.notebook.get_cell(3);
            return [cell.output_area.outputs, cell.iopub_messages];
        });
        var cell_results = returned[0];
        var callback_results = returned[1];
        this.test.assertEquals(cell_results.length, 0, "correct number of cell outputs");
        this.test.assertEquals(callback_results.length, 2, "correct number of callback outputs");
        this.test.assertEquals(callback_results[0].output_type, 'display_data', 'check output_type 0');
        this.test.assertEquals(callback_results[0].transient.display_id, 'here', 'check display id 0');
        this.test.assertEquals(callback_results[0].data['text/plain'], '5', 'value');
        this.test.assertEquals(callback_results[1].output_type, 'update_display_data', 'check output_type 1');
        this.test.assertEquals(callback_results[1].transient.display_id, 'here', 'display id 1');
        this.test.assertEquals(callback_results[1].data['text/plain'], '6', 'value');
    });

    this.thenEvaluate(function () {
        Jupyter.notebook.insert_cell_at_index("code", 4);
        var cell = Jupyter.notebook.get_cell(4);
        cell.set_text([
            "display_with_id(7, 'here')",
            "display_with_id(8, 'here', update=True)",
            "display_with_id(9, 'result', execute_result=True)"
        ].join('\n'));
        cell.execute();

        Jupyter.notebook.insert_cell_at_index("code", 5);
        var cell = Jupyter.notebook.get_cell(5);
        cell.set_text([
            "display_with_id(10, 'result', update=True)",
            "1",
        ].join('\n'));
        cell.execute();
    });

    this.wait_for_output(4);
    this.wait_for_output(5);
    this.wait_for_idle();

    this.then(function () {
        var returned = JSON.parse(this.evaluate(function () {
            var cell3 = Jupyter.notebook.get_cell(3);
            var cell4 = Jupyter.notebook.get_cell(4);
            return JSON.stringify([cell4.output_area.outputs, cell3.iopub_messages]);
        }));
        var cell_results = returned[0];
        var callback_results = returned[1];
        this.test.assertEquals(cell_results.length, 2, "correct number of cell outputs");
        this.test.assertEquals(callback_results.length, 4, "correct number of callback outputs");
        this.test.assertEquals(callback_results[0].output_type, 'display_data', 'check output_type 0');
        this.test.assertEquals(callback_results[0].transient.display_id, 'here', 'check display id 0');
        this.test.assertEquals(callback_results[0].data['text/plain'], '5', 'value');
        this.test.assertEquals(callback_results[1].output_type, 'update_display_data', 'check output_type 1');
        this.test.assertEquals(callback_results[1].transient.display_id, 'here', 'display id 1');
        this.test.assertEquals(callback_results[1].data['text/plain'], '6', 'value');
        this.test.assertEquals(callback_results[2].output_type, 'display_data', 'check output_type 2');
        this.test.assertEquals(callback_results[2].transient.display_id, 'here', 'check display id 2');
        this.test.assertEquals(callback_results[2].data['text/plain'], '7', 'value');
        this.test.assertEquals(callback_results[3].output_type, 'update_display_data', 'check output_type 3');
        this.test.assertEquals(callback_results[3].transient.display_id, 'here', 'display id 3');
        this.test.assertEquals(callback_results[3].data['text/plain'], '8', 'value');

        this.test.assertEquals(cell_results[1].data['text/plain'], '10', 'update execute_result')
    });


});
