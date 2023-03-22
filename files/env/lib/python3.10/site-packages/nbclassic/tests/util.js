//
// Utility functions for the HTML notebook's CasperJS tests.
//
casper.get_notebook_server = function () {
    // Get the URL of a notebook server on which to run tests.
    var port = casper.cli.get("port");
    port = (typeof port === 'undefined') ? '8888' : port;
    return casper.cli.get("url") || ('http://127.0.0.1:' + port);
};

// casper.thenClick doesn't seem to trigger click events properly
casper.thenClick = function (selector) {
    return this.thenEvaluate(function(selector) {
        var el = $(selector);
        if (el.length === 0) {
            console.error("Missing element!", selector)
        }
        el.click();
    }, {selector: selector})
}

casper.open_new_notebook = function () {
    // Create and open a new notebook.
    var baseUrl = this.get_notebook_server();
    this.start(baseUrl);
    this.waitFor(this.page_loaded);
    this.waitForSelector('#kernel-python2 a, #kernel-python3 a');
    this.thenClick('#kernel-python2 a, #kernel-python3 a');
    
    this.waitForPopup('');

    this.withPopup('', function () {this.waitForSelector('.CodeMirror-code');});
    this.then(function () {
        this.open(this.popups[0].url);
    });
    this.waitFor(this.page_loaded);

    // Hook the log and error methods of the console, forcing them to
    // serialize their arguments before printing.  This allows the
    // Objects to cross into the phantom/slimer regime for display.
    this.thenEvaluate(function(){
        var serialize_arguments = function(f, context) {
            return function() {
                var pretty_arguments = [];
                for (var i = 0; i < arguments.length; i++) {
                    var value = arguments[i];
                    if (value instanceof Object) {
                        var name = value.name || 'Object';
                        // Print a JSON string representation of the object.
                        // If we don't do this, [Object object] gets printed
                        // by casper, which is useless.  The long regular
                        // expression reduces the verbosity of the JSON.
                        pretty_arguments.push(name + ' {' + JSON.stringify(value, null, '  ')
                            .replace(/(\s+)?({)?(\s+)?(}(\s+)?,?)?(\s+)?(\s+)?\n/g, '\n')
                            .replace(/\n(\s+)?\n/g, '\n'));
                    } else {
                        pretty_arguments.push(value);
                    }
                }
                f.apply(context, pretty_arguments);
            };
        };
        console.log = serialize_arguments(console.log, console);
        console.error = serialize_arguments(console.error, console);
    });

    // Make sure the kernel has started
    this.waitFor(this.kernel_running);
    // track the IPython busy/idle state
    this.thenEvaluate(function () {
        require(['base/js/namespace', 'base/js/events'], function (IPython, events) {
        
            events.on('kernel_idle.Kernel',function () {
                IPython._status = 'idle';
            });
            events.on('kernel_busy.Kernel',function () {
                IPython._status = 'busy';
            });
        });
    });
};

casper.page_loaded = function() {
    // Return whether or not the page has been loaded.
    return this.evaluate(function() {
        return typeof IPython !== "undefined" &&
            IPython.page !== undefined;
    });
};

casper.kernel_running = function() {
    // Return whether or not the kernel is running.
    return this.evaluate(function() {
        return IPython &&
        IPython.notebook &&
        IPython.notebook.kernel &&
        IPython.notebook.kernel.is_connected();
    });
};

casper.kernel_disconnected = function() {
    return this.evaluate(function() {
        return IPython.notebook.kernel.is_fully_disconnected();
    });
};

casper.wait_for_kernel_ready = function () {
    this.waitFor(this.kernel_running);
    this.thenEvaluate(function () {
        IPython._kernel_ready = false;
        IPython.notebook.kernel.kernel_info(
            function () {
                IPython._kernel_ready = true;
            });
    });
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._kernel_ready;
        });
    });
};

casper.shutdown_current_kernel = function () {
    // Shut down the current notebook's kernel.
    this.thenEvaluate(function() {
        IPython.notebook.session.delete();
    });
    // We close the page right after this so we need to give it time to complete.
    this.wait(1000);
};

casper.delete_current_notebook = function () {
    // Delete created notebook.

    // For some unknown reason, this doesn't work?!?
    this.thenEvaluate(function() {
        IPython.notebook.delete();
    });
};

casper.wait_for_busy = function () {
    // Waits for the notebook to enter a busy state.
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._status == 'busy';
        });
    });
};

casper.wait_for_idle = function () {
    // Waits for the notebook to idle.
    this.waitFor(function () {
        return this.evaluate(function () {
            return IPython._status == 'idle';
        });
    });
};

casper.wait_for_output = function (cell_num, out_num) {
    // wait for the nth output in a given cell
    this.wait_for_idle();
    out_num = out_num || 0;
    this.then(function() {
        this.waitFor(function (c, o) {
            return this.evaluate(function get_output(c, o) {
                var cell = IPython.notebook.get_cell(c);
                return cell.output_area.outputs.length > o;
            },
            // pass parameter from the test suite js to the browser code js
            {c : cell_num, o : out_num});
        },
        function then() { },
        function timeout() {
            this.echo("wait_for_output timed out on cell "+cell_num+", waiting for "+out_num+" outputs .");
            var pn = this.evaluate(function get_prompt(c) {
                return (IPython.notebook.get_cell(c)|| {'input_prompt_number':'no cell'}).input_prompt_number;
            });
            this.echo("cell prompt was :'"+pn+"'.");
        });
    });
};

casper.wait_for_widget = function (widget_info) {
    // wait for a widget msg que to reach 0
    //
    // Parameters
    // ----------
    // widget_info : object
    //      Object which contains info related to the widget.  The model_id property
    //      is used to identify the widget.

    // Clear the results of a previous query, if they exist.  Make sure a
    // dictionary exists to store the async results in.
    this.thenEvaluate(function(model_id) {
        if (window.pending_msgs === undefined) { 
            window.pending_msgs = {}; 
        } else {
            window.pending_msgs[model_id] = -1;
        } 
    }, {model_id: widget_info.model_id});

    // Wait for the pending messages to be 0.
    this.waitFor(function () {
        var pending = this.evaluate(function (model_id) {

            // Get the model.  Once the model is had, store it's pending_msgs
            // count in the window's dictionary.
            IPython.notebook.kernel.widget_manager.get_model(model_id)
            .then(function(model) {     
                window.pending_msgs[model_id] = model.pending_msgs; 
            });

            // Return the pending_msgs result.
            return window.pending_msgs[model_id];
        }, {model_id: widget_info.model_id});

        if (pending === 0) {
            return true;
        } else {
            return false;
        }
    });
};

casper.cell_has_outputs = function (cell_num) {
    var result = casper.evaluate(function (c) {
        var cell = IPython.notebook.get_cell(c);
        return cell.output_area.outputs.length;
    },
    {c : cell_num});
    return result > 0;
};

casper.get_output_cell = function (cell_num, out_num, message) {
    messsge  = message+': ' ||'no category :'
    // return an output of a given cell
    out_num = out_num || 0;
    var result = casper.evaluate(function (c, o) {
        var cell = IPython.notebook.get_cell(c);
        return cell.output_area.outputs[o];
    },
    {c : cell_num, o : out_num});
    if (!result) {
        var num_outputs = casper.evaluate(function (c) {
            var cell = IPython.notebook.get_cell(c);
            return cell.output_area.outputs.length;
        },
        {c : cell_num});
        this.test.assertTrue(false,
            message+"Cell " + cell_num + " has no output #" + out_num + " (" + num_outputs + " total)"
        );
    } else {
        return result;
    }
};

casper.get_cells_length = function () {
    // return the number of cells in the notebook
    var result = casper.evaluate(function () {
        return IPython.notebook.get_cells().length;
    });
    return result;
};

casper.set_cell_text = function(index, text){
    // Set the text content of a cell.
    this.evaluate(function (index, text) {
        var cell = IPython.notebook.get_cell(index);
        cell.set_text(text);
    }, index, text);
};

casper.get_cell_text = function(index){
    // Get the text content of a cell.
    return this.evaluate(function (index) {
        var cell = IPython.notebook.get_cell(index);
        return cell.get_text();
    }, index);
};

casper.insert_cell_at_bottom = function(cell_type){
    // Inserts a cell at the bottom of the notebook
    // Returns the new cell's index.
    return this.evaluate(function (cell_type) {
        var cell = IPython.notebook.insert_cell_at_bottom(cell_type);
        return IPython.notebook.find_cell_index(cell);
    }, cell_type);
};

casper.append_cell = function(text, cell_type) { 
    // Insert a cell at the bottom of the notebook and set the cells text.
    // Returns the new cell's index.
    var index = this.insert_cell_at_bottom(cell_type);
    if (text !== undefined) {
        this.set_cell_text(index, text);
    }
    return index;
};

casper.execute_cell = function(index, expect_failure){
    // Asynchronously executes a cell by index.
    // Returns the cell's index.
    
    if (expect_failure === undefined) expect_failure = false;
    var that = this;
    this.then(function(){
        that.evaluate(function (index) {
            var cell = IPython.notebook.get_cell(index);
            cell.execute();
        }, index);
    });
    this.wait_for_idle();
    
    this.then(function () {
        var error = that.evaluate(function (index) {
            var cell = IPython.notebook.get_cell(index);
            var outputs = cell.output_area.outputs;
            for (var i = 0; i < outputs.length; i++) {
                if (outputs[i].output_type == 'error') {
                    return outputs[i];
                }
            }
            return false;
        }, index);
        if (error === null) {
            this.test.fail("Failed to check for error output");
        }
        if (expect_failure && error === false) {
            this.test.fail("Expected error while running cell");
        } else if (!expect_failure && error !== false) {
            this.test.fail("Error running cell:\n" + error.traceback.join('\n'));
        }
    });
    return index;
};

casper.execute_cell_then = function(index, then_callback, expect_failure) {
    // Synchronously executes a cell by index.
    // Optionally accepts a then_callback parameter.  then_callback will get called
    // when the cell  has finished executing.
    // Returns the cell's index.
    var return_val = this.execute_cell(index, expect_failure);

    this.wait_for_idle();

    var that = this;
    this.then(function(){ 
        if (then_callback!==undefined) {
            then_callback.apply(that, [index]);
        }
    });

    return return_val;
};

casper.append_cell_execute_then = function(text, then_callback, expect_failure) {
    // Append a code cell and execute it, optionally calling a then_callback
    var c = this.append_cell(text);
    return this.execute_cell_then(c, then_callback, expect_failure);
};

casper.assert_output_equals = function(text, output_text, message) {
    // Append a code cell with the text, then assert the output is equal to output_text
    this.append_cell_execute_then(text, function(index) {
        this.test.assertEquals(this.get_output_cell(index).text.trim(), output_text, message);
    });
};

casper.wait_for_element = function(index, selector){
    // Utility function that allows us to easily wait for an element 
    // within a cell.  Uses JQuery selector to look for the element.
    var that = this;
    this.waitFor(function() {
        return that.cell_element_exists(index, selector);
    });
};

casper.cell_element_exists = function(index, selector){
    // Utility function that allows us to easily check if an element exists 
    // within a cell.  Uses JQuery selector to look for the element.
    return casper.evaluate(function (index, selector) {
        var $cell = IPython.notebook.get_cell(index).element;
        return $cell.find(selector).length > 0;
    }, index, selector);
};

casper.cell_element_function = function(index, selector, function_name, function_args){
    // Utility function that allows us to execute a jQuery function on an 
    // element within a cell.
    return casper.evaluate(function (index, selector, function_name, function_args) {
        var $cell = IPython.notebook.get_cell(index).element;
        var $el = $cell.find(selector);
        return $el[function_name].apply($el, function_args);
    }, index, selector, function_name, function_args);
};

casper.validate_notebook_state = function(message, mode, cell_index) {
    // Validate the entire dual mode state of the notebook.  Make sure no more than
    // one cell is selected, focused, in edit mode, etc...
    // General tests.
    this.test.assertEquals(this.get_keyboard_mode(), this.get_notebook_mode(),
        message + '; keyboard and notebook modes match');
    // Is the selected cell the only cell that is selected?
    if (cell_index!==undefined) {
        this.test.assert(this.is_only_cell_selected(cell_index),
            message + '; expecting cell ' + cell_index + ' to be the only cell selected. Got selected cell(s):'+
            (function(){
                return casper.evaluate(function(){
                    return IPython.notebook.get_selected_cells_indices();
                })
            })()
            );
    }

    // Mode specific tests.
    if (mode==='command') {
        // Are the notebook and keyboard manager in command mode?
        this.test.assertEquals(this.get_keyboard_mode(), 'command',
            message + '; in command mode');
        // Make sure there isn't a single cell in edit mode.
        this.test.assert(this.is_only_cell_edit(null),
            message + '; all cells in command mode');
        this.test.assert(this.is_cell_editor_focused(null),
            message + '; no cell editors are focused while in command mode');

    } else if (mode==='edit') {
        // Are the notebook and keyboard manager in edit mode?
        this.test.assertEquals(this.get_keyboard_mode(), 'edit',
            message + '; in edit mode');
        if (cell_index!==undefined) {
            // Is the specified cell the only cell in edit mode?
            this.test.assert(this.is_only_cell_edit(cell_index),
                message + '; cell ' + cell_index + ' is the only cell in edit mode '+ this.cells_modes());
            // Is the specified cell the only cell with a focused code mirror?
            this.test.assert(this.is_cell_editor_focused(cell_index),
                message + '; cell ' + cell_index + '\'s editor is appropriately focused');
        }

    } else {
        this.test.assert(false, message + '; ' + mode + ' is an unknown mode');
    }
};

casper.select_cell = function(index, moveanchor) {
    // Select a cell in the notebook.
    this.evaluate(function (i, moveanchor) {
        IPython.notebook.select(i, moveanchor);
    }, {i: index, moveanchor: moveanchor});
};

casper.select_cells = function(index, bound, moveanchor) {
    // Select a block of cells in the notebook.
    // like Python range, selects [index,bound)
    this.evaluate(function (i, n, moveanchor) {
        Jupyter.notebook.select(i, moveanchor);
        Jupyter.notebook.extend_selection_by(n);
    }, {i: index, n: (bound - index - 1), moveanchor: moveanchor});
};

casper.click_cell_editor = function(index) {
    // Emulate a click on a cell's editor.
    
    // Code Mirror does not play nicely with emulated brower events.  
    // Instead of trying to emulate a click, here we run code similar to
    // the code used in Code Mirror that handles the mousedown event on a
    // region of codemirror that the user can focus.
    this.evaluate(function (i) {
        var cm = IPython.notebook.get_cell(i).code_mirror;
        if (cm.options.readOnly != "nocursor" && (document.activeElement != cm.display.input)){
            cm.display.input.focus();
        }
    }, {i: index});
};

casper.set_cell_editor_cursor = function(index, line_index, char_index) {
    // Set the Code Mirror instance cursor's location.
    this.evaluate(function (i, l, c) {
        IPython.notebook.get_cell(i).code_mirror.setCursor(l, c);
    }, {i: index, l: line_index, c: char_index});
};

casper.focus_notebook = function() {
    // Focus the notebook div.
    this.evaluate(function (){
        $('#notebook').focus();
    }, {});
};

casper.trigger_keydown = function() {
    // Emulate a keydown in the notebook.
    for (var i = 0; i < arguments.length; i++) {
        this.evaluate(function (k) {
            var element = $(document);
            var event = IPython.keyboard.shortcut_to_event(k, 'keydown');
            element.trigger(event);
        }, {k: arguments[i]});    
    }
};

casper.get_keyboard_mode = function() {
    // Get the mode of the keyboard manager.
    return this.evaluate(function() {
        return IPython.keyboard_manager.mode;
    }, {});
};

casper.get_notebook_mode = function() {
    // Get the mode of the notebook.
    return this.evaluate(function() {
        return IPython.notebook.mode;
    }, {});
};

casper.get_cell = function(index) {
    // Get a single cell.
    //
    // Note: Handles to DOM elements stored in the cell will be useless once in
    //       CasperJS context.
    return this.evaluate(function(i) {
        var cell = IPython.notebook.get_cell(i);
        if (cell) {
            return cell;
        }
        return null;
    }, {i : index});
};

casper.is_cell_editor_focused = function(index) {
    // Make sure a cell's editor is the only editor focused on the page.
    return this.evaluate(function(i) {
        var focused_textarea = $('#notebook .CodeMirror-focused textarea');
        if (focused_textarea.length > 1) { throw 'More than one Code Mirror editor is focused at once!'; }
        if (i === null) {
            return focused_textarea.length === 0;
        } else {
            var cell = IPython.notebook.get_cell(i);
            if (cell) {
                return cell.code_mirror.getInputField() == focused_textarea[0];
            }    
        }
        return false;
    }, {i : index});
};

casper.is_only_cell_selected = function(index) {
    // Check if a cell is the only cell selected.
    // Pass null as the index to check if no cells are selected.
    return this.is_only_cell_on(index, 'selected', 'unselected');
};

casper.is_only_cell_edit = function(index) {
    // Check if a cell is the only cell in edit mode.
    // Pass null as the index to check if all of the cells are in command mode.
    var cells_length = this.get_cells_length();
    for (var j = 0; j < cells_length; j++) {
        if (j === index) {
            if (!this.cell_mode_is(j, 'edit')) {
                return false;
            }
        } else {
            if (this.cell_mode_is(j, 'edit')) {
                return false;
            }
        }
    }
    return true;
};

casper.is_only_cell_on = function(i, on_class, off_class) {
    // Check if a cell is the only cell with the `on_class` DOM class applied to it.
    // All of the other cells are checked for the `off_class` DOM class.
    // Pass null as the index to check if all of the cells have the `off_class`.
    var cells_length = this.get_cells_length();
    for (var j = 0; j < cells_length; j++) {
        if (j === i) {
            if (this.cell_has_class(j, off_class) || !this.cell_has_class(j, on_class)) {
                return false;
            }
        } else {
            if (!this.cell_has_class(j, off_class) || this.cell_has_class(j, on_class)) {
                return false;
            }
        }
    }
    return true;
};

casper.cells_modes = function(){
    return this.evaluate(function(){
        return IPython.notebook.get_cells().map(function(x,c){return x.mode})
    }, {});
};

casper.cell_mode_is = function(index, mode) {
    // Check if a cell is in a specific mode
    return this.evaluate(function(i, m) {
        var cell = IPython.notebook.get_cell(i);
        if (cell) {
            return cell.mode === m;
        }
        return false;
    }, {i : index, m: mode});
};


casper.cell_has_class = function(index, classes) {
    // Check if a cell has a class.
    return this.evaluate(function(i, c) {
        var cell = IPython.notebook.get_cell(i);
        if (cell) {
            return cell.element.hasClass(c);
        }
        return false;
    }, {i : index, c: classes});
};

casper.is_cell_rendered = function (index) {
    return this.evaluate(function(i) {
        return !!IPython.notebook.get_cell(i).rendered;
    }, {i:index});
};

casper.assert_colors_equal = function (hex_color, local_color, msg) {
    // Tests to see if two colors are equal.
    //
    // Parameters
    // hex_color: string
    //      Hexadecimal color code, with or without preceding hash character.
    // local_color: string
    //      Local color representation.  Can either be hexadecimal (default for 
    //      phantom) or rgb (default for slimer).

    // Remove parentheses, hashes, semi-colons, and space characters.
    hex_color = hex_color.replace(/[\(\); #]/, '');
    local_color = local_color.replace(/[\(\); #]/, '');

    // If the local color is rgb, clean it up and replace 
    if (local_color.substr(0,3).toLowerCase() == 'rgb') {
        var components = local_color.substr(3).split(',');
        local_color = '';
        for (var i = 0; i < components.length; i++) {
            var part = parseInt(components[i]).toString(16);
            while (part.length < 2) part = '0' + part;
            local_color += part;
        }
    }
    
    this.test.assertEquals(hex_color.toUpperCase(), local_color.toUpperCase(), msg);
};

casper.notebook_test = function(test) {
    // Wrap a notebook test to reduce boilerplate.
    this.open_new_notebook();

    // Echo whether or not we are running this test using SlimerJS
    if (this.evaluate(function(){
        return typeof InstallTrigger !== 'undefined';   // Firefox 1.0+
    })) { 
        console.log('This test is running in SlimerJS.'); 
        this.slimerjs = true;
    }
    
    // Make sure to remove the onbeforeunload callback.  This callback is 
    // responsible for the "Are you sure you want to quit?" type messages.
    // PhantomJS ignores these prompts, SlimerJS does not which causes hangs.
    this.then(function(){
        this.evaluate(function(){
            window.onbeforeunload = function(){};
        });
    });

    this.then(test);
    
    // Kill the kernel and delete the notebook.
    this.shutdown_current_kernel();
    // This is still broken but shouldn't be a problem for now.
    // this.delete_current_notebook();
    
    // This is required to clean up the page we just finished with. If we don't call this
    // casperjs will leak file descriptors of all the open WebSockets in that page. We
    // have to set this.page=null so that next time casper.start runs, it will create a
    // new page from scratch.
    this.then(function () {
        this.page.close();
        this.page = null;
    });
    
    // Run the browser automation.
    this.run(function() {
        this.test.done();
    });
};

casper.wait_for_dashboard = function () {
    // Wait for the dashboard list to load.
    casper.waitForSelector('.list_item');
};

/**
 * Open the dashboard page
 * @param {bool} use_start - If true, will use casper.start(), otherwise
 *      casper.open(). You should only set it to true if the dashboard
 *      is the first URL to be opened in the test, because calling
 *      casper.start() multiple times causes casper to skip subsequent then()
 */
casper.open_dashboard = function (use_start) {
    if (use_start === undefined) {
        use_start = false;
    }
    // Start casper by opening the dashboard page.
    var baseUrl = this.get_notebook_server();
    if (use_start) {
        this.start(baseUrl);
    } else {
        this.open(baseUrl);
    }
    this.waitFor(this.page_loaded);
    this.wait_for_dashboard();
};

casper.dashboard_test = function (test) {
    // Open the dashboard page and run a test.
    this.open_dashboard(true);
    this.then(test);

    this.then(function () {
        this.page.close();
        this.page = null;
    });
    
    // Run the browser automation.
    this.run(function() {
        this.test.done();
    });
};

// note that this will only work for UNIQUE events -- if you want to
// listen for the same event twice, this will not work!
casper.event_test = function (name, events, action, timeout) {

    // set up handlers to listen for each of the events
    this.thenEvaluate(function (events) {
        var make_handler = function (event) {
            return function () {
                IPython._events_triggered.push(event);
                IPython.notebook.events.off(event, null, IPython._event_handlers[event]);
                delete IPython._event_handlers[event];
            };
        };
        IPython._event_handlers = {};
        IPython._events_triggered = [];
        for (var i=0; i < events.length; i++) {
            IPython._event_handlers[events[i]] = make_handler(events[i]);
            IPython.notebook.events.on(events[i], IPython._event_handlers[events[i]]);
        }
    }, [events]);

    // execute the requested action
    this.then(action);

    // wait for all the events to be triggered
    this.waitFor(function () {
        return this.evaluate(function (events) {
            return IPython._events_triggered.length >= events.length;
        }, [events]);
    }, undefined, undefined, timeout);

    // test that the events were triggered in the proper order
    this.then(function () {
        var triggered = this.evaluate(function () {
            return IPython._events_triggered;
        });
        var handlers = this.evaluate(function () {
            return Object.keys(IPython._event_handlers);
        });
        this.test.assertEquals(triggered.length, events.length, name + ': ' + events.length + ' events were triggered');
        this.test.assertEquals(handlers.length, 0, name + ': all handlers triggered');
        for (var i=0; i < events.length; i++) {
            this.test.assertEquals(triggered[i], events[i], name + ': ' + events[i] + ' was triggered');
        }
    });

    // turn off any remaining event listeners
    this.thenEvaluate(function () {
        for (var event in IPython._event_handlers) {
            IPython.notebook.events.off(event, null, IPython._event_handlers[event]);
            delete IPython._event_handlers[event];
        }
    });
};

casper.options.waitTimeout=10000;
casper.on('waitFor.timeout', function onWaitForTimeout(timeout) {
    this.echo("Timeout for " + casper.get_notebook_server());
    this.echo("Is the notebook server running?");
});

casper.print_log = function () {
    // Pass `console.log` calls from page JS to casper.
    this.on('remote.message', function(msg) {
        this.echo('Remote message caught: ' + msg);
    });
};

casper.on("page.error", function onError(msg, trace) {
    // show errors in the browser
    this.echo("Page Error");
    this.echo("  Message:   " + msg.split('\n').join('\n             '));
    this.echo("  Call stack:");
    var local_path = this.get_notebook_server();
    for (var i = 0; i < trace.length; i++) {
        var frame = trace[i];
        var file = frame.file;
        // shorten common phantomjs evaluate url
        // this will have a different value on slimerjs
        if (file === "phantomjs://webpage.evaluate()") {
            file = "evaluate";
        }
        // remove the version tag from the path
        file = file.replace(/(\?v=[0-9abcdef]+)/, '');
        // remove the local address from the beginning of the path
        if (file.indexOf(local_path) === 0) {
            file = file.substr(local_path.length);
        }
        var frame_text = (frame.function.length > 0) ? " in " + frame.function : "";
        this.echo("    line " + frame.line + " of " + file + frame_text);
    }
});


casper.capture_log = function () {
    // show captured errors
    var captured_log = [];
    var seen_errors = 0;
    this.on('remote.message', function(msg) {
        captured_log.push(msg);
    });

    var that = this;
    this.test.on("test.done", function (result) {
        // test.done runs per-file,
        // but suiteResults is per-suite (directory)
        var current_errors;
        if (this.suiteResults) {
            // casper 1.1 has suiteResults
            current_errors = this.suiteResults.countErrors() + this.suiteResults.countFailed();
        } else {
            // casper 1.0 has testResults instead
            current_errors = this.testResults.failed;
        }

        if (current_errors > seen_errors && captured_log.length > 0) {
            casper.echo("\nCaptured console.log:");
            for (var i = 0; i < captured_log.length; i++) {
                var output = String(captured_log[i]).split('\n');
                for (var j = 0; j < output.length; j++) {
                    casper.echo("    " + output[j]);
                }
            }
        }

        seen_errors = current_errors;
        captured_log = [];
    });
};

casper.interact = function() {
    // Start an interactive Javascript console.
    var system = require('system');
    system.stdout.writeLine('JS interactive console.');
    system.stdout.writeLine('Type `exit` to quit.');

    function read_line() {
        system.stdout.writeLine('JS: ');
        var line = system.stdin.readLine();
        return line;
    }

    var input = read_line();
    while (input.trim() != 'exit') {
        var output = this.evaluate(function(code) {
            return String(eval(code));
        }, {code: input});
        system.stdout.writeLine('\nOut: ' + output);
        input = read_line();
    }
};

casper.capture_log();
