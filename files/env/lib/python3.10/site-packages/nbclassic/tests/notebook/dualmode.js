// Test the notebook dual mode feature.

// Test
casper.notebook_test(function () {
    var a = 'print("a")';
    var index = this.append_cell(a);
    this.execute_cell_then(index);

    var b = 'print("b")';
    index = this.append_cell(b);
    this.execute_cell_then(index);

    var c = 'print("c")';
    index = this.append_cell(c);
    this.execute_cell_then(index);

    this.then(function () {
        if (this.slimerjs) {
            // When running in xvfb, the Slimer window doesn't always have focus
            // immediately.  By clicking on a new element on the page we can force
            // it to gain focus.
            this.click_cell_editor(1);
            this.click_cell_editor(0);
        }

        this.validate_notebook_state('initial state', 'edit', 0);
        this.trigger_keydown('esc');
        this.validate_notebook_state('esc', 'command', 0);
        this.trigger_keydown('down');
        this.validate_notebook_state('down', 'command', 1);
        this.trigger_keydown('enter');
        this.validate_notebook_state('enter', 'edit', 1);
        this.trigger_keydown('j');
        this.validate_notebook_state('j in edit mode', 'edit', 1);
        this.trigger_keydown('esc');
        this.validate_notebook_state('esc', 'command', 1);
        this.trigger_keydown('j');
        this.validate_notebook_state('j in command mode', 'command', 2);
        this.click_cell_editor(0);
        this.validate_notebook_state('click cell 0', 'edit', 0);
        this.click_cell_editor(3);
        this.validate_notebook_state('click cell 3', 'edit', 3);
        this.trigger_keydown('esc');
        this.validate_notebook_state('esc', 'command', 3);

        // Open keyboard help
        this.evaluate(function(){
            $('#keyboard_shortcuts a').click();
        }, {});
    });

    // Wait for the dialog to fade in completely.
    this.waitForSelector('div.modal', function() {
        this.evaluate(function(){
            IPython.modal_shown = false;
            $('div.modal').on('shown.bs.modal', function (){
                IPython.modal_shown = true;
            });
            $('div.modal').on('hidden.bs.modal', function (){
                IPython.modal_shown = false;
            });
        });
        
    });

    this.waitFor(function () {
        return this.evaluate(function(){
            return IPython.modal_shown;
        });
    },
    function() {
        this.trigger_keydown('k');
        this.validate_notebook_state('k in command mode while keyboard help is up', 'command', 3);

        // Close keyboard help
        this.evaluate(function(){
            $('div.modal-footer button.btn-default').click();
        }, {});
    });

    // Wait for the dialog to fade out completely.
    this.waitFor(function () {
        return this.evaluate(function(){
            return !IPython.modal_shown;
        });
    },
    function() {

        this.trigger_keydown('k');
        this.validate_notebook_state('k in command mode', 'command', 2);
        this.click_cell_editor(0);
        this.validate_notebook_state('click cell 0', 'edit', 0);
        this.focus_notebook();
        this.validate_notebook_state('focus #notebook', 'command', 0);
        this.click_cell_editor(0);
        this.validate_notebook_state('click cell 0', 'edit', 0);
        this.focus_notebook();
        this.validate_notebook_state('focus #notebook', 'command', 0);
        this.click_cell_editor(3);
        this.validate_notebook_state('click cell 3', 'edit', 3);

        // Cell deletion
        this.trigger_keydown('esc', 'd', 'd');
        this.test.assertEquals(this.get_cells_length(), 3, 'dd actually deletes a cell');
        this.validate_notebook_state('dd', 'command', 2);

        // Make sure that if the time between d presses is too long, nothing gets removed.
        this.trigger_keydown('d');
    });
    this.wait(1000);
    this.then(function () {
        this.trigger_keydown('d');
        this.test.assertEquals(this.get_cells_length(), 3, "d, 1 second wait, d doesn't delete a cell");
        this.validate_notebook_state('d, 1 second wait, d', 'command', 2);
    });
});
