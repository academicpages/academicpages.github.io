//
// Test that the correct cells are executed when there are marked cells.
//
casper.notebook_test(function () {
    var that = this;
    var assert_outputs = function (expected, msg_prefix) {
        var msg, i;
        msg_prefix = "(assert_outputs) "+(msg_prefix || 'no prefix')+": ";
        for (i = 0; i < that.get_cells_length(); i++) {
            if (expected[i] === undefined) {
                msg = msg_prefix + 'cell ' + i + ' not executed';
                that.test.assertFalse(that.cell_has_outputs(i), msg);

            } else {
                msg = msg_prefix + 'cell ' + i + ' executed';
                var out = (that.get_output_cell(i, undefined, msg_prefix)||{test:'<no cells>'}).text
                that.test.assertEquals(out, expected[i], msg + ', out is: '+out);
            }
        }
    };

    this.then(function () {
        this.set_cell_text(0, 'print("a")');
        this.append_cell('print("b")');
        this.append_cell('print("c")');
        this.append_cell('print("d")');
        this.test.assertEquals(this.get_cells_length(), 4, "correct number of cells");
    });

    this.then(function () {
        this.select_cell(1);
        this.select_cell(2, false);
    });

    this.then(function () {
        this.evaluate(function () {
            IPython.notebook.clear_all_output();
        });
    })

    this.then(function(){
        this.select_cell(1);
        this.validate_notebook_state('before execute 1', 'command', 1);
        this.select_cell(1);
        this.select_cell(2, false);
        this.trigger_keydown('ctrl-enter');
    });

    this.wait_for_output(1);
    this.wait_for_output(2);

    this.then(function () {
        assert_outputs([undefined, 'b\n', 'c\n', undefined], 'run selected 1');
        this.validate_notebook_state('run selected cells 1', 'command', 2);
    });


    // execute and insert below when there are selected cells
    this.then(function () {
        this.evaluate(function () {
            IPython.notebook.clear_all_output();
        });

        this.select_cell(1);
        this.validate_notebook_state('before execute 2', 'command', 1);
        this.evaluate(function () {
            $("#run_cell_insert_below").click();
        });
    });

    this.wait_for_output(1);

    this.then(function () {
        assert_outputs([undefined, 'b\n', undefined, undefined , undefined],'run selected cells 2');
        this.validate_notebook_state('run selected cells 2', 'edit', 2);
    });

    // check that it doesn't affect run all above
    this.then(function () {
        this.evaluate(function () {
            IPython.notebook.clear_all_output();
        });

        this.select_cell(1);
        this.validate_notebook_state('before execute 3', 'command', 1);
        this.evaluate(function () {
            $("#run_all_cells_above").click();
        });
    });

    this.wait_for_output(0);

    this.then(function () {
        assert_outputs(['a\n', undefined, undefined, undefined],'run cells above');
        this.validate_notebook_state('run cells above', 'command', 0);
    });

    // check that it doesn't affect run all below
    this.then(function () {
        this.evaluate(function () {
            IPython.notebook.clear_all_output();
        });

        this.select_cell(1);
        this.validate_notebook_state('before execute 4', 'command', 1);
        this.evaluate(function () {
            $("#run_all_cells_below").click();
        });
    });

    this.wait_for_output(1);
    this.wait_for_output(2);
    this.wait_for_output(3);

    this.then(function () {
        assert_outputs([undefined, 'b\n', undefined, 'c\n', 'd\n'],'run cells below');
        this.validate_notebook_state('run cells below', 'command', 4);
    });

    // check that it doesn't affect run all
    this.then(function () {
        this.evaluate(function () {
            IPython.notebook.clear_all_output();
        });

        this.select_cell(1);
        this.validate_notebook_state('before execute 5', 'command', 1);
        this.evaluate(function () {
            $("#run_all_cells").click();
        });
    });

    this.wait_for_output(0);
    this.wait_for_output(1);
    this.wait_for_output(2);
    this.wait_for_output(3);

    this.then(function () {
        assert_outputs(['a\n', 'b\n', undefined, 'c\n', 'd\n'],'run all cells');
        this.validate_notebook_state('run all cells', 'command', 4);
    });

    this.then(function(){
        this.set_cell_text(0, 'print("x")');
        this.set_cell_text(1, 'print("y")');

        this.select_cell(0);
        this.select_cell(1, false);
        this.trigger_keydown('alt-enter');

    });
    
    this.wait_for_output(0);
    this.wait_for_output(1);
    this.then(function () {
        assert_outputs(['x\n', 'y\n', undefined, undefined,  'c\n', 'd\n'],'run selection and insert below');
        this.validate_notebook_state('run selection insert below', 'edit', 2);
    });

    this.then(function(){
        this.set_cell_text(1, 'print("z")');
        this.set_cell_text(2, 'print("a")');

        this.select_cell(1);
        this.select_cell(2, false);
        this.evaluate(function () {
            $("#run_cell_select_below").click();
        });

    });
    
    this.wait_for_output(1);
    this.wait_for_output(2);
    this.then(function () {
        assert_outputs(['x\n', 'z\n', 'a\n', undefined, 'c\n', 'd\n'],'run selection and select below');
        this.validate_notebook_state('run selection select below', 'command', 3);
    });
});
