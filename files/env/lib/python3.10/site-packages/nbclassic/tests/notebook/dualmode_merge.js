
// Test
casper.notebook_test(function () {
    var a = 'ab\n\ncd';
    var b = 'print("b")';
    var c = 'print("c")';
    var d = '"d"';
    var e = '"e"';
    var f = '"f"';
    var g = '"g"';
    var N = 7;

    var that = this;
    var cell_is_mergeable = function (index) {
        // Get the mergeable status of a cell.
        return that.evaluate(function (index) {
            var cell = IPython.notebook.get_cell(index);
            return cell.is_mergeable();
        }, index);
    };

    var cell_is_splittable = function (index) {
        // Get the splittable status of a cell.
        return that.evaluate(function (index) {
            var cell = IPython.notebook.get_cell(index);
            return cell.is_splittable();
        }, index);
    };

    var close_dialog = function () {
        this.evaluate(function(){
            $('div.modal-footer button.btn-default').click();
        }, {});
    };

    this.then(function () {
        // Split and merge cells
        this.select_cell(0);
        this.trigger_keydown('a', 'enter'); // Create cell above and enter edit mode.
        this.validate_notebook_state('a, enter', 'edit', 0);
        this.set_cell_text(0, 'abcd');
        this.set_cell_editor_cursor(0, 0, 2);
        this.test.assertEquals(this.get_cell_text(0), 'abcd', 'Verify that cell 0 has the new contents.');
        this.trigger_keydown('ctrl-shift--'); // Split
        this.test.assertEquals(this.get_cell_text(0), 'ab', 'split; Verify that cell 0 has the first half.');
        this.test.assertEquals(this.get_cell_text(1), 'cd', 'split; Verify that cell 1 has the second half.');
        this.validate_notebook_state('split', 'edit', 1);
        this.select_cell(0); // Move up to cell 0
        this.evaluate(function() { IPython.notebook.extend_selection_by(1);});
        this.trigger_keydown('shift-m'); // Merge
        this.validate_notebook_state('merge', 'command', 0);
        this.test.assertEquals(this.get_cell_text(0), a, 'merge; Verify that cell 0 has the merged contents.');
    });

    // add some more cells and test splitting/merging when a cell is not deletable
    this.then(function () {
        this.append_cell(b);
        this.append_cell(c);
        this.append_cell(d);
        this.append_cell(e);
        this.append_cell(f);
        this.append_cell(g);
    });

    this.thenEvaluate(function() {
        IPython.notebook.get_cell(1).metadata.deletable = false;
    });

    // Check that merge/split status are correct
    this.then(function () {
        this.test.assert(cell_is_splittable(0), 'Cell 0 is splittable');
        this.test.assert(cell_is_mergeable(0), 'Cell 0 is mergeable');
        this.test.assert(!cell_is_splittable(1), 'Cell 1 is not splittable');
        this.test.assert(!cell_is_mergeable(1), 'Cell 1 is not mergeable');
        this.test.assert(cell_is_splittable(2), 'Cell 2 is splittable');
        this.test.assert(cell_is_mergeable(2), 'Cell 2 is mergeable');
    });

    // Try to merge cell 0 above, nothing should happen
    this.then(function () {
        this.select_cell(0);
    });
    this.thenEvaluate(function() {
        IPython.notebook.merge_cell_above();
    });
    this.then(function() {
        this.test.assertEquals(this.get_cells_length(), N, 'Merge cell 0 above: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 0 above: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 0 above: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 0 above: Cell 2 is unchanged');
        this.validate_notebook_state('merge up', 'command', 0);
    });

    // Try to merge cell 0 below with cell 1, should not work, as 1 is locked
    this.then(function () {
        this.trigger_keydown('esc');
        this.select_cell(0);
        this.select_cell(1,false);
        this.trigger_keydown('shift-m');
        this.trigger_keydown('esc');
        this.test.assertEquals(this.get_cells_length(), N, 'Merge cell 0 down: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 0 down: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 0 down: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 0 down: Cell 2 is unchanged');
        this.validate_notebook_state('merge 0 with 1', 'command', 1);
    });

    // Try to merge cell 1 above with cell 0
    this.then(function () {
        this.select_cell(1);
    });
    this.thenEvaluate(function () {
        IPython.notebook.merge_cell_above();
    });
    this.then(function () {
        this.test.assertEquals(this.get_cells_length(), N, 'Merge cell 1 up: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 1 up: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 1 up: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 1 up: Cell 2 is unchanged');
        this.validate_notebook_state('merge up', 'command', 1);
    });

    // Try to split cell 1
    this.then(function () {
        this.select_cell(1);
        this.trigger_keydown('enter');
        this.set_cell_editor_cursor(1, 0, 2);
        this.trigger_keydown('ctrl-shift--'); // Split
        this.test.assertEquals(this.get_cells_length(), N, 'Split cell 1: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Split cell 1: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Split cell 1: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Split cell 1: Cell 2 is unchanged');
        this.validate_notebook_state('ctrl-shift--', 'edit', 1); 
    });

    // Try to merge cell 1 down, should fail, as 1 is locked
    this.then(function () {
        this.trigger_keydown('esc');
        this.select_cell(1);
        this.select_cell(2, false); // extend selection
        this.trigger_keydown('shift-m');
        this.trigger_keydown('esc');
        this.test.assertEquals(this.get_cells_length(), N, 'Merge cell 1 down: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 1 down: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 1 down: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 1 down: Cell 2 is unchanged');
        this.validate_notebook_state('Merge 1 with 2', 'command', 2);
    });

    // Try to merge cell 2 above with cell 1, should fail, 1 is locked
    this.then(function () {
        this.select_cell(2);
    });
    this.thenEvaluate(function () {
        IPython.notebook.merge_cell_above();
    });
    this.then(function () {
        this.test.assertEquals(this.get_cells_length(), N, 'Merge cell 2 up: There are still '+N+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 2 up: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 2 up: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 2 up: Cell 2 is unchanged');
        this.validate_notebook_state('merge up', 'command', 2);
    });

    this.then(function () {
        this.trigger_keydown('esc');
        this.select_cell(3);
        this.select_cell(4, false); // extend selection
        this.trigger_keydown('shift-m');
        this.trigger_keydown('esc');
        this.test.assertEquals(this.get_cells_length(), N-1 , 'Merge cell 3 with 4: There are now '+(N-1)+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 3 with 4: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 3 with 4: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 3 with 4: Cell 2 is unchanged');
        this.test.assertEquals(this.get_cell_text(3), d+'\n\n'+e, 'Merge cell 3 with 4: Cell 3 is merged');
        this.test.assertEquals(this.get_cell_text(4), f, 'Merge cell 3 with 4: Cell 5 is now cell 4');
        this.test.assertEquals(this.get_cell_text(5), g, 'Merge cell 3 with 4: Cell 6 is now cell 5');
        this.validate_notebook_state('actual merge', 'command', 3);
    });


    this.then(function () {
        this.trigger_keydown('esc');
        this.select_cell(4);
        // shift-m on single selection does nothing.
        this.trigger_keydown('shift-m');
        this.trigger_keydown('esc');
        this.test.assertEquals(this.get_cells_length(), N-2 , 'Merge cell 4 with 5: There are now '+(N-2)+' cells');
        this.test.assertEquals(this.get_cell_text(0), a, 'Merge cell 4 with 5: Cell 0 is unchanged');
        this.test.assertEquals(this.get_cell_text(1), b, 'Merge cell 4 with 5: Cell 1 is unchanged');
        this.test.assertEquals(this.get_cell_text(2), c, 'Merge cell 4 with 5: Cell 2 is unchanged');
        this.test.assertEquals(this.get_cell_text(3), d+'\n\n'+e, 'Merge cell 4 with 5: Cell 3  is unchanged');
        this.test.assertEquals(this.get_cell_text(4), f+'\n\n'+g, 'Merge cell 4 with 5: Cell 4 and 5 are merged');
        this.validate_notebook_state('merge on single cell merge with below', 'command', 4);
    });


});
