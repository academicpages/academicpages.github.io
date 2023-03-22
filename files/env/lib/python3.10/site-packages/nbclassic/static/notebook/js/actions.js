// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// How to pick action names:
//
// * First pick a noun and a verb for the action. For example, if the action is "restart kernel," the verb is
//   "restart" and the noun is "kernel".
// * Omit terms like "selected" and "active" by default, so "delete-cell", rather than "delete-selected-cell".
//   Only provide a scope like "-all-" if it is other than the default "selected" or "active" scope.
// * If an action has a secondary action, separate the secondary action with "-and-", so
//   "restart-kernel-and-clear-output".
// * Don't ever use before/after as they have a temporal connotation that is confusing when used in a spatial
//   context.
// * Use above/below or previous/next to indicate spacial and sequential relationships.
// * For dialogs, use a verb that indicates what the dialog will accomplish, such as "confirm-restart-kernel".


define([
    'base/js/i18n',
    ], function(i18n){
    "use strict";

    var warn_bad_name = function(name){
        if(name !== "" && !name.match(/:/)){
            console.warn('You are trying to use an action/command name, where the separator between prefix and name is not `:`\n'+
                         '"'+name+'"\n'+
                         'You are likely to not use the API in a correct way. Typically use the following:\n'+
                         '`var key = actions.register(<object>, "<name>", "<prefix>");` and reuse the `key` variable'+
                         'instead of re-generating the key yourself.'
                    );
        }
    };

    var ActionHandler = function (env) {
        this.env = env || {};
        Object.seal(this);
    };

    var $ = requirejs('jquery');
    var events =  requirejs('base/js/events');

    /**
     *  A bunch of predefined `Simple Actions` used by Jupyter.
     *  `Simple Actions` have the following keys:
     *  help (optional): a short string the describe the action.
     *      will be used in various context, like as menu name, tool tips on buttons,
     *      and short description in help menu.
     *  help_index (optional): a string used to sort action in help menu.
     *  icon (optional): a short string that represent the icon that have to be used with this
     *  action. this should mainly correspond to a Font_awesome class.
     *  handler : a function which is called when the action is activated. It will receive at first parameter
     *      a dictionary containing various handle to element of the notebook.
     *
     *  action need to be registered with a **name** that can be use to refer to this action.
     *
     *  if `help` is not provided it will be derived by replacing any dash by space
     *  in the **name** of the action. It is advised to provide a prefix to action name to
     *  avoid conflict the prefix should be all lowercase and end with a dot `.`
     *  in the absence of a prefix the behavior of the action is undefined.
     *
     *  All action provided by the Jupyter notebook are prefixed with `jupyter-notebook:`.
     *
     *  One can register extra actions or replace an existing action with another one is possible
     *  but is considered undefined behavior.
     *
     **/
    var _actions = {
        'toggle-cell-rtl-layout': {
            cmd: i18n.msg._('toggle current cell ltr/rtl direction'),
            help: i18n.msg._('Toggle current cell directionality between left-to-right and right-to-left'),
            handler: function (env) {
              var notebook_direction = document.body.getAttribute('dir') == 'rtl' ? 'rtl' : 'ltr';
              var current_cell_default_direction = env.notebook.get_selected_cell().cell_type == 'code' ? 'ltr' : notebook_direction;
              var current_cell_direction = env.notebook.get_selected_cell().metadata.direction || current_cell_default_direction;
              var new_direction = current_cell_direction == 'rtl' ? 'ltr' : 'rtl';
              env.notebook.get_selected_cells().forEach(
                  function(cell) { cell.metadata.direction = new_direction; }
              );
              env.notebook.set_dirty(true);
              env.notebook.apply_directionality();
            }
        },
        'toggle-rtl-layout': {
            cmd: i18n.msg._('toggle notebook ltr/rtl direction'),
            help: i18n.msg._('Toggle notebook directionality between left-to-right and right-to-left'),
            handler: function (env) {
              var new_direction = document.body.getAttribute('dir') == 'rtl' ? 'ltr' : 'rtl';
              env.notebook.metadata.direction = new_direction;
              env.notebook.set_dirty(true);
              env.notebook.apply_directionality();
            }
        },
        'edit-command-mode-keyboard-shortcuts': {
            cmd: i18n.msg._('edit command mode keyboard shortcuts'),
            help: i18n.msg._('Open a dialog to edit the command mode keyboard shortcuts'),
            handler: function (env) {
                env.notebook.show_shortcuts_editor();
            }
        },
        'shutdown-kernel': {
            help: 'Shutdown the kernel (no confirmation dialog)',
            handler: function (env) {
                env.notebook.shutdown_kernel({confirm: false});
            }
        },
        'confirm-shutdown-kernel':{
            icon: 'fa-repeat',
            help_index : 'hb',
            help: 'Shutdown the kernel (with confirmation dialog)',
            handler : function (env) {
                env.notebook.shutdown_kernel();
            }
        },
        'restart-kernel': {
            cmd: i18n.msg._('restart kernel'),
            help: i18n.msg._('restart the kernel (no confirmation dialog)'),
            handler: function (env) {
                env.notebook.restart_kernel({confirm: false});
            },
        },
        'confirm-restart-kernel':{
            icon: 'fa-repeat',
            help_index : 'hb',
            cmd: i18n.msg._('confirm restart kernel'),
            help: i18n.msg._('restart the kernel (with dialog)'),
            handler : function (env) {
                env.notebook.restart_kernel();
            }
        },
        'restart-kernel-and-run-all-cells': {
            cmd: i18n.msg._('restart kernel and run all cells'),
            help: i18n.msg._('restart the kernel, then re-run the whole notebook (no confirmation dialog)'),
            handler: function (env) {
                env.notebook.restart_run_all({confirm: false});
            }
        },
        'confirm-restart-kernel-and-run-all-cells': {
            icon: 'fa-forward',
            cmd: i18n.msg._('confirm restart kernel and run all cells'),
            help: i18n.msg._('restart the kernel, then re-run the whole notebook (with dialog)'),
            handler: function (env) {
                env.notebook.restart_run_all();
            }
        },
        'restart-kernel-and-clear-output': {
            cmd: i18n.msg._('restart kernel and clear output'),
            help: i18n.msg._('restart the kernel and clear all output (no confirmation dialog)'),
            handler: function (env) {
                env.notebook.restart_clear_output({confirm: false});
            }
        },
        'confirm-restart-kernel-and-clear-output': {
            cmd: i18n.msg._('confirm restart kernel and clear output'),
            help: i18n.msg._('restart the kernel and clear all output (with dialog)'),
            handler: function (env) {
                env.notebook.restart_clear_output();
            }
        },
        'interrupt-kernel':{
            icon: 'fa-stop',
            cmd: i18n.msg._('interrupt the kernel'),
            help: i18n.msg._('interrupt the kernel'),
            help_index : 'ha',
            handler : function (env) {
                env.notebook.kernel.interrupt();
            }
        },
        'run-cell-and-select-next': {
            cmd: i18n.msg._('run cell and select next'),
            icon: 'fa-play',
            help: i18n.msg._('run cell, select below'),
            help_index : 'ba',
            handler : function (env) {
                env.notebook.execute_cell_and_select_below();
            }
        },
        'run-cell':{
            cmd: i18n.msg._('run selected cells'),
            help    : i18n.msg._('run selected cells'),
            help_index : 'bb',
            handler : function (env) {
                env.notebook.execute_selected_cells();
            }
        },
        'run-cell-and-insert-below':{
            cmd: i18n.msg._('run cell and insert below'),
            help    : i18n.msg._('run cell and insert below'),
            help_index : 'bc',
            handler : function (env) {
                env.notebook.execute_cell_and_insert_below();
            }
        },
        'run-all-cells': {
            cmd: i18n.msg._('run all cells'),
            help: i18n.msg._('run all cells'),
            help_index: 'bd',
            handler: function (env) {
                env.notebook.execute_all_cells();
            }
        },
        'run-all-cells-above':{
            cmd: i18n.msg._('run all cells above'),
            help: i18n.msg._('run all cells above'),
            handler : function (env) {
                env.notebook.execute_cells_above();
            }
        },
        'run-all-cells-below':{
            cmd: i18n.msg._('run all cells below'),
            help: i18n.msg._('run all cells below'),
            handler : function (env) {
                env.notebook.execute_cells_below();
            }
        },
        'enter-command-mode': {
            cmd: i18n.msg._('enter command mode'),
            help    : i18n.msg._('enter command mode'),
            help_index : 'aa',
            handler : function (env) {
                env.notebook.command_mode();
            }
        },
        'insert-image': {
            cmd: i18n.msg._('insert image'),
            help      : i18n.msg._('insert image'),
            help_index : 'dz',
            handler : function (env) {
                env.notebook.insert_image();
            }
        },
        'cut-cell-attachments': {
            cmd: i18n.msg._('cut cell attachments'),
            help    : i18n.msg._('cut cell attachments'),
            help_index : 'dza',
            handler: function (env) {
                env.notebook.cut_cell_attachments();
            }
        },
        'copy-cell-attachments': {
            cmd: i18n.msg._('copy cell attachments'),
            help    : i18n.msg._('copy cell attachments'),
            help_index: 'dzb',
            handler: function (env) {
                env.notebook.copy_cell_attachments();
            }
        },
        'paste-cell-attachments': {
            cmd: i18n.msg._('paste cell attachments'),
            help    : i18n.msg._('paste cell attachments'),
            help_index: 'dzc',
            handler: function (env) {
                env.notebook.paste_cell_attachments();
            }
        },
        'split-cell-at-cursor': {
            cmd: i18n.msg._('split cell at cursor(s)'),
            help    : i18n.msg._('split cell at cursor(s)'),
            help_index : 'ea',
            handler : function (env) {
                env.notebook.split_cell();
            }
        },
        'enter-edit-mode' : {
            cmd: i18n.msg._('enter edit mode'),
            help : i18n.msg._('enter edit mode'),
            help_index : 'aa',
            handler : function (env) {
                env.notebook.edit_mode();
            }
        },
        'select-previous-cell' : {
            cmd: i18n.msg._('select previous cell'),
            help: i18n.msg._('select cell above'),
            help_index : 'da',
            handler : function (env) {
                var index = env.notebook.get_selected_index();
                if (index !== 0 && index !== null) {
                    env.notebook.select_prev(true);
                    env.notebook.focus_cell();
                }
            }
        },
        'select-next-cell' : {
            cmd: i18n.msg._('select next cell'),
            help: i18n.msg._('select cell below'),
            help_index : 'db',
            handler : function (env) {
                var index = env.notebook.get_selected_index();
                if (index !== (env.notebook.ncells()-1) && index !== null) {
                    env.notebook.select_next(true);
                    env.notebook.focus_cell();
                }
            }
        },
        'extend-selection-above' : {
            cmd: i18n.msg._('extend selection above'),
            help: i18n.msg._('extend selected cells above'),
            help_index : 'dc',
            handler : function (env) {
                env.notebook.extend_selection_by(-1);
                // scroll into view,
                // do not call notebook.focus_cell(), or
                // all the selection get thrown away
                env.notebook.get_selected_cell().element.focus();
            }
        },
        'extend-selection-below' : {
            cmd: i18n.msg._('extend selection below'),
            help: i18n.msg._('extend selected cells below'),
            help_index : 'dd',
            handler : function (env) {
                env.notebook.extend_selection_by(1);
                // scroll into view,
                // do not call notebook.focus_cell(), or
                // all the selection get thrown away
                env.notebook.get_selected_cell().element.focus();
            }
        },
        'select-all' : {
            cmd: i18n.msg._('select all'),
            help: i18n.msg._('select all cells'),
            help_index : 'de',
            handler : function (env) {
                env.notebook.select_all();
                env.notebook.get_selected_cell().element.focus();
            }
        },
        'cut-cell' : {
            cmd: i18n.msg._('cut selected cells'),
            help: i18n.msg._('cut selected cells'),
            icon: 'fa-cut',
            help_index : 'ee',
            handler : function (env) {
                var index = env.notebook.get_selected_index();
                env.notebook.cut_cell();
                env.notebook.select(index);
            }
        },
        'copy-cell' : {
            cmd: i18n.msg._('copy selected cells'),
            help: i18n.msg._('copy selected cells'),
            icon: 'fa-copy',
            help_index : 'ef',
            handler : function (env) {
                env.notebook.copy_cell();
            }
        },
        'paste-cell-replace' : {
            help: 'paste cells replace',
            handler : function (env) {
                env.notebook.paste_cell_replace();
            }
        },
        'paste-cell-above' : {
            cmd: i18n.msg._('paste cells above'),
            help: i18n.msg._('paste cells above'),
            help_index : 'eg',
            handler : function (env) {
                env.notebook.paste_cell_above();
            }
        },
        'paste-cell-below' : {
            cmd: i18n.msg._('paste cells below'),
            help: i18n.msg._('paste cells below'),
            icon: 'fa-paste',
            help_index : 'eh',
            handler : function (env) {
                env.notebook.paste_cell_below();
            }
        },
        'insert-cell-above' : {
            cmd: i18n.msg._('insert cell above'),
            help: i18n.msg._('insert cell above'),
            help_index : 'ec',
            handler : function (env) {
                env.notebook.insert_cell_above();
                env.notebook.select_prev(true);
                env.notebook.focus_cell();
            }
        },
        'insert-cell-below' : {
            cmd: i18n.msg._('insert cell below'),
            help: i18n.msg._('insert cell below'),
            icon : 'fa-plus',
            help_index : 'ed',
            handler : function (env) {
                env.notebook.insert_cell_below();
                env.notebook.select_next(true);
                env.notebook.focus_cell();
            }
        },
        'change-cell-to-code' : {
            cmd: i18n.msg._('change cell to code'),
            help    : i18n.msg._('change cell to code'),
            help_index : 'ca',
            handler : function (env) {
                env.notebook.cells_to_code();
            }
        },
        'change-cell-to-markdown' : {
            cmd: i18n.msg._('change cell to markdown'),
            help    : i18n.msg._('change cell to markdown'),
            help_index : 'cb',
            handler : function (env) {
                env.notebook.cells_to_markdown();
            }
        },
        'change-cell-to-raw' : {
            cmd: i18n.msg._('change cell to raw'),
            help    : i18n.msg._('change cell to raw'),
            help_index : 'cc',
            handler : function (env) {
                env.notebook.cells_to_raw();
            }
        },
        'change-cell-to-heading-1' : {
            cmd: i18n.msg._('change cell to heading 1'),
            help    : i18n.msg._('change cell to heading 1'),
            help_index : 'cd',
            handler : function (env) {
                env.notebook.to_heading(undefined, 1);
            }
        },
        'change-cell-to-heading-2' : {
            cmd: i18n.msg._('change cell to heading 2'),
            help    : i18n.msg._('change cell to heading 2'),
            help_index : 'ce',
            handler : function (env) {
                env.notebook.to_heading(undefined, 2);
            }
        },
        'change-cell-to-heading-3' : {
            cmd: i18n.msg._('change cell to heading 3'),
            help    : i18n.msg._('change cell to heading 3'),
            help_index : 'cf',
            handler : function (env) {
                env.notebook.to_heading(undefined, 3);
            }
        },
        'change-cell-to-heading-4' : {
            cmd: i18n.msg._('change cell to heading 4'),
            help    : i18n.msg._('change cell to heading 4'),
            help_index : 'cg',
            handler : function (env) {
                env.notebook.to_heading(undefined, 4);
            }
        },
        'change-cell-to-heading-5' : {
            cmd: i18n.msg._('change cell to heading 5'),
            help    : i18n.msg._('change cell to heading 5'),
            help_index : 'ch',
            handler : function (env) {
                env.notebook.to_heading(undefined, 5);
            }
        },
        'change-cell-to-heading-6' : {
            cmd: i18n.msg._('change cell to heading 6'),
            help    : i18n.msg._('change cell to heading 6'),
            help_index : 'ci',
            handler : function (env) {
                env.notebook.to_heading(undefined, 6);
            }
        },
        'toggle-cell-output-collapsed' : {
            cmd: i18n.msg._('toggle cell output'),
            help    : i18n.msg._('toggle output of selected cells'),
            help_index : 'gb',
            handler : function (env) {
                env.notebook.toggle_cells_outputs();
            }
        },
        'toggle-cell-output-scrolled' : {
            cmd: i18n.msg._('toggle cell scrolling'),
            help    : i18n.msg._('toggle output scrolling of selected cells'),
            help_index : 'gc',
            handler : function (env) {
                env.notebook.toggle_cells_outputs_scroll();
            }
        },
        'clear-cell-output' : {
            cmd: i18n.msg._('clear cell output'),
            help    : i18n.msg._('clear output of selected cells'),
            handler : function (env) {
                env.notebook.clear_cells_outputs();
            }
        },
        'move-cell-down' : {
            cmd: i18n.msg._('move cells down'),
            help: i18n.msg._('move selected cells down'),
            icon: 'fa-arrow-down',
            help_index : 'eb',
            handler : function (env) {
                env.notebook.move_cell_down();
            }
        },
        'move-cell-up' : {
            cmd: i18n.msg._('move cells up'),
            help: i18n.msg._('move selected cells up'),
            icon: 'fa-arrow-up',
            help_index : 'ea',
            handler : function (env) {
                env.notebook.move_cell_up();
            }
        },
        'toggle-cell-line-numbers' : {
            cmd: i18n.msg._('toggle line numbers'),
            help    : i18n.msg._('toggle line numbers'),
            help_index : 'ga',
            handler : function (env) {
                env.notebook.cell_toggle_line_numbers();
            }
        },
        'show-keyboard-shortcuts' : {
            cmd: i18n.msg._('show keyboard shortcuts'),
            help    : i18n.msg._('show keyboard shortcuts'),
            help_index : 'ge',
            handler : function (env) {
                env.quick_help.show_keyboard_shortcuts();
            }
        },
        'delete-cell': {
            cmd: i18n.msg._('delete cells'),
            help: i18n.msg._('delete selected cells'),
            help_index : 'ej',
            handler : function (env) {
                env.notebook.delete_cell();
            }
        },
        'undo-cell-deletion' : {
            cmd: i18n.msg._('undo cell deletion'),
            help: i18n.msg._('undo cell deletion'),
            help_index : 'ei',
            handler : function (env) {
                env.notebook.undelete_cell();
            }
        },
        // TODO reminder
        // open an issue, merge with above merge with last cell of notebook if at top.
        'merge-cell-with-previous-cell' : {
            cmd: i18n.msg._('merge cell with previous cell'),
            help    : i18n.msg._('merge cell above'),
            handler : function (env) {
                env.notebook.merge_cell_above();
            }
        },
        'merge-cell-with-next-cell' : {
            cmd: i18n.msg._('merge cell with next cell'),
            help    : i18n.msg._('merge cell below'),
            help_index : 'ek',
            handler : function (env) {
                env.notebook.merge_cell_below();
            }
        },
        'merge-selected-cells' : {
            cmd: i18n.msg._('merge selected cells'),
            help : i18n.msg._('merge selected cells'),
            help_index: 'el',
            handler: function(env) {
                env.notebook.merge_selected_cells();
            }
        },
        'merge-cells' : {
            cmd: i18n.msg._('merge cells'),
            help : i18n.msg._('merge selected cells, or current cell with cell below if only one cell is selected'),
            help_index: 'el',
            handler: function(env) {
                var l = env.notebook.get_selected_cells_indices().length;
                if(l == 1){
                    env.notebook.merge_cell_below();
                } else {
                    env.notebook.merge_selected_cells();
                }
            }
        },
        'show-command-palette': {
            help_index : 'aa',
            cmd: i18n.msg._('show command pallette'),
            help: i18n.msg._('open the command palette'),
            icon: 'fa-keyboard-o',
            handler : function(env){
                env.notebook.show_command_palette();
            }
        },
        'toggle-all-line-numbers': {
            cmd: i18n.msg._('toggle all line numbers'),
            help : i18n.msg._('toggles line numbers in all cells, and persist the setting'),
            icon: 'fa-list-ol',
            handler: function(env) {
                var value = !env.notebook.line_numbers;
                env.notebook.get_cells().map(function(c) {
                    c.code_mirror.setOption('lineNumbers', value);
                });
                env.notebook.line_numbers = value;
            }
        },
        'show-all-line-numbers': {
            cmd: i18n.msg._('show all line numbers'),
            help : i18n.msg._('show line numbers in all cells, and persist the setting'),
            handler: function(env) {
                env.notebook.get_cells().map(function(c) {
                    c.code_mirror.setOption('lineNumbers', true);
                });
                env.notebook.line_numbers = true;
            }
        },
        'hide-all-line-numbers': {
            cmd: i18n.msg._('hide all line numbers'),
            help : i18n.msg._('hide line numbers in all cells, and persist the setting'),
            handler: function(env) {
                env.notebook.get_cells().map(function(c) {
                    c.code_mirror.setOption('lineNumbers', false);
                });
                env.notebook.line_numbers = false;
            }
        },
        'toggle-header':{
            cmd: i18n.msg._('toggle header'),
            help: i18n.msg._('switch between showing and hiding the header'),
            handler : function(env) {
                var value = !env.notebook.header;
                if (value === true) {
                    $('#header-container').show();
                    $('.header-bar').show();
                } else if (value === false) {
                    $('#header-container').hide();
                    $('.header-bar').hide();
                }
                events.trigger('resize-header.Page');
                env.notebook.header = value;
            }
        },
        'show-header':{
            cmd: i18n.msg._('show the header'),
            help: i18n.msg._('show the header'),
            handler : function(env) {
                $('#header-container').show();
                $('.header-bar').show();
                events.trigger('resize-header.Page');
                env.notebook.header = true;
            }
        },
        'hide-header':{
            cmd: i18n.msg._('hide the header'),
            help: i18n.msg._('hide the header'),
            handler : function(env) {
                $('#header-container').hide();
                $('.header-bar').hide();
                events.trigger('resize-header.Page');
                env.notebook.header = false;
            }
        },
        'toggle-menubar':{
            help: 'hide/show the menu bar',
            handler : function(env) {
                $('#menubar-container').toggle();
                events.trigger('resize-header.Page');
            }
        },
        'show-menubar':{
            help: 'show the menu bar',
            handler : function(env) {
                $('#menubar-container').show();
                events.trigger('resize-header.Page');
            }
        },
        'hide-menubar':{
            help: 'hide the menu bar',
            handler : function(env) {
                $('#menubar-container').hide();
                events.trigger('resize-header.Page');
            }
        },
        'toggle-toolbar':{
            cmd: i18n.msg._('toggle toolbar'),
            help: i18n.msg._('switch between showing and hiding the toolbar'),
            handler : function(env) {
                var value = !env.notebook.toolbar;
                if (value === true) {
                    $('div#maintoolbar').show();
                } else if (value === false) {
                    $('div#maintoolbar').hide();
                }
                events.trigger('resize-header.Page');
                env.notebook.toolbar = value;
            }
        },
        'show-toolbar':{
            cmd: i18n.msg._('show the toolbar'),
            help: i18n.msg._('show the toolbar'),
            handler : function(env) {
                $('div#maintoolbar').show();
                events.trigger('resize-header.Page');
                env.notebook.toolbar = true;
            }
        },
        'hide-toolbar':{
            cmd: i18n.msg._('hide the toolbar'),
            help: i18n.msg._('hide the toolbar'),
            handler : function(env) {
                $('div#maintoolbar').hide();
                events.trigger('resize-header.Page');
                env.notebook.toolbar = false;
            }
        },
        'close-pager': {
            cmd: i18n.msg._('close the pager'),
            help : i18n.msg._('close the pager'),
            handler : function(env) {
                // Collapse the page if it is open
                if (env.pager && env.pager.expanded) {
                    env.pager.collapse();
                }
            }
        },
        'auto-indent': {
            cmd: i18n.msg._('automatically indent selection'),
            help : i18n.msg._('automatically indent selection'),
            handler : function(env) {
              // Get selected cell
              var selected_cell = env.notebook.get_selected_cell();
              // Execute a CM command
              selected_cell.code_mirror.execCommand('indentAuto');
            }
        },
        'close-and-halt': {
            cmd: i18n.msg._('shutdown kernel and close window'),
            help : i18n.msg._('shutdown kernel and close window'),
            handler : function(env) {
                env.notebook.close_and_halt();
            }
        }
    };

    /**
     * A bunch of `Advance actions` for Jupyter.
     * Cf `Simple Action` plus the following properties.
     *
     * handler: first argument of the handler is the event that triggered the action
     *      (typically keypress). The handler is responsible for any modification of the
     *      event and event propagation.
     *      Is also responsible for returning false if the event have to be further ignored,
     *      true, to tell keyboard manager that it ignored the event.
     *
     *      the second parameter of the handler is the environment passed to Simple Actions
     *
     **/
    var custom_ignore = {
        'ignore':{
            cmd: i18n.msg._('ignore'),
            handler : function () {
                return true;
            }
        },
        'move-cursor-up':{
            cmd: i18n.msg._('move cursor up'),
            help: i18n.msg._("move cursor up"),
            handler : function (env, event) {
                var index = env.notebook.get_selected_index();
                var cell = env.notebook.get_cell(index);
                var cm = env.notebook.get_selected_cell().code_mirror;
                var cur = cm.getCursor();
                if (cell && cell.at_top() && index !== 0 && cur.ch === 0) {
                    if(event){
                        event.preventDefault();
                    }
                    env.notebook.command_mode();
                    env.notebook.select_prev(true);
                    env.notebook.edit_mode();
                    cm = env.notebook.get_selected_cell().code_mirror;
                    cm.setCursor(cm.lastLine(), 0);
                }
                return false;
            }
        },
        'move-cursor-down':{
            cmd: i18n.msg._('move cursor down'),
            help: i18n.msg._("move cursor down"),
            handler : function (env, event) {
                var index = env.notebook.get_selected_index();
                var cell = env.notebook.get_cell(index);
                if (cell.at_bottom() && index !== (env.notebook.ncells()-1)) {
                    if(event){
                        event.preventDefault();
                    }
                    env.notebook.command_mode();
                    env.notebook.select_next(true);
                    env.notebook.edit_mode();
                    var cm = env.notebook.get_selected_cell().code_mirror;
                    cm.setCursor(0, 0);
                }
                return false;
            }
        },
        'scroll-notebook-down': {
            cmd: i18n.msg._('scroll notebook down'),
            help: i18n.msg._("scroll notebook down"),
            handler: function(env, event) {
                if(event){
                    event.preventDefault();
                }
                return env.notebook.scroll_manager.scroll(1);
            },
        },
        'scroll-notebook-up': {
            cmd: i18n.msg._('scroll notebook up'),
            help: i18n.msg._("scroll notebook up"),
            handler: function(env, event) {
                if(event){
                    event.preventDefault();
                }
                return env.notebook.scroll_manager.scroll(-1);
            },
        },
        'scroll-cell-center': {
            cmd: i18n.msg._('scroll cell center'),
            help: i18n.msg._("Scroll the current cell to the center"),
            handler: function (env, event) {
                if(event){
                    event.preventDefault();
                }
                var cell = env.notebook.get_selected_index();
                return env.notebook.scroll_cell_percent(cell, 50, 0);
            }
        },
        'scroll-cell-top': {
            cmd: i18n.msg._('scroll cell top'),
            help: i18n.msg._("Scroll the current cell to the top"),
            handler: function (env, event) {
                if(event){
                    event.preventDefault();
                }
                var cell = env.notebook.get_selected_index();
                return env.notebook.scroll_cell_percent(cell, 0, 0);
            }
        },
        'duplicate-notebook':{
            cmd: i18n.msg._('duplicate notebook'),
            help: i18n.msg._("Create and open a copy of the current notebook"),
            handler : function (env, event) {
                env.notebook.copy_notebook();
            }
        },
        'trust-notebook':{
            cmd: i18n.msg._('trust notebook'),
            help: i18n.msg._("Trust the current notebook"),
            handler : function (env, event) {
                env.notebook.trust_notebook();
            }
        },
        'rename-notebook':{
            cmd: i18n.msg._('rename notebook'),
            help: i18n.msg._("Rename the current notebook"),
            handler : function (env, event) {
                env.notebook.save_widget.rename_notebook({notebook: env.notebook});
            }
        },
        'toggle-all-cells-output-collapsed':{
            cmd: i18n.msg._('toggle all cells output collapsed'),
            help: i18n.msg._("Toggle the hidden state of all output areas"),
            handler : function (env, event) {
                env.notebook.toggle_all_output();
            }
        },
        'toggle-all-cells-output-scrolled':{
            cmd: i18n.msg._('toggle all cells output scrolled'),
            help: i18n.msg._("Toggle the scrolling state of all output areas"),
            handler : function (env, event) {
                env.notebook.toggle_all_output_scroll();
            }
        },

        'clear-all-cells-output':{
            cmd: i18n.msg._('clear all cells output'),
            help: i18n.msg._("Clear the content of all the outputs"),
            handler : function (env, event) {
                env.notebook.clear_all_output();
            }
        },
        'save-notebook':{
            cmd: i18n.msg._('save notebook'),
            help: i18n.msg._("Save and Checkpoint"),
            help_index : 'fb',
            icon: 'fa-save',
            handler : function (env, event) {
                env.notebook.save_checkpoint();
                if(event){
                    event.preventDefault();
                }
                return false;
            }
        },
    };

    // private stuff that prepend `jupyter-notebook:` to actions names
    // and uniformize/fill in missing pieces in of an action.
    var _prepare_handler = function(registry, subkey, source){
        registry['jupyter-notebook:'+subkey] = {};
        registry['jupyter-notebook:'+subkey].cmd = source[subkey].cmd;
        registry['jupyter-notebook:'+subkey].help = source[subkey].help||subkey.replace(/-/g,' ');
        registry['jupyter-notebook:'+subkey].help_index = source[subkey].help_index;
        registry['jupyter-notebook:'+subkey].icon = source[subkey].icon;
        return source[subkey].handler;
    };

    // Will actually generate/register all the Jupyter actions
    var fun = function(){
        var final_actions = {};
        var k;
        for(k in _actions){
            if(_actions.hasOwnProperty(k)){
                // Js closure are function level not block level need to wrap in a IIFE
                // and append jupyter-notebook: to event name these things do intercept event so are wrapped
                // in a function that return false.
                var handler = _prepare_handler(final_actions, k, _actions);
                (function(key, handler){
                    final_actions['jupyter-notebook:'+key].handler = function(env, event){
                        handler(env);
                        if(event){
                            event.preventDefault();
                        }
                        return false;
                    };
                })(k, handler);
            }
        }

        for(k in custom_ignore){
            // Js closure are function level not block level need to wrap in a IIFE
            // same as above, but decide for themselves whether or not they intercept events.
            if(custom_ignore.hasOwnProperty(k)){
                handler = _prepare_handler(final_actions, k, custom_ignore);
                (function(key, handler){
                    final_actions['jupyter-notebook:'+key].handler = function(env, event){
                        return handler(env, event);
                    };
                })(k, handler);
            }
        }

        return final_actions;
    };
    ActionHandler.prototype._actions = fun();


    /**
     *  extend the environment variable that will be pass to handlers
     **/
    ActionHandler.prototype.extend_env = function(env){
        for(var k in env){
            this.env[k] = env[k];
        }
    };

    ActionHandler.prototype.register = function(action, name, prefix){
        /**
         * Register an `action` with an optional name and prefix.
         *
         * if name and prefix are not given they will be determined automatically.
         * if action if just a `function` it will be wrapped in an anonymous action.
         *
         * @return the full name to access this action .
         **/
        action = this.normalise(action);
        if( !name ){
            name = 'autogenerated-'+String(action.handler);
        }
        prefix = prefix || 'auto';
        var full_name = prefix+':'+name;
        this._actions[full_name] = action;
        return full_name;

    };


    ActionHandler.prototype.normalise = function(data){
        /**
         * given an `action` or `function`, return a normalised `action`
         * by setting all known attributes and removing unknown attributes;
         **/
        if(typeof(data) === 'function'){
            data = {handler:data};
        }
        if(typeof(data.handler) !== 'function'){
            throw new Error('unknown datatype, cannot register');
        }
        var _data = data;
        data = {};
        data.handler = _data.handler;
        data.help = _data.help || '';
        data.icon = _data.icon || '';
        data.help_index = _data.help_index || '';
        return data;
    };

    ActionHandler.prototype.get_name = function(name_or_data){
        /**
         * given an `action` or `name` of an action, return the name attached to this action.
         * if given the name of and corresponding actions does not exist in registry, return `null`.
         **/

        if(typeof(name_or_data) === 'string'){
            warn_bad_name(name_or_data);
            if(this.exists(name_or_data)){
                return name_or_data;
            } else {
                return null;
            }
        } else {
            return this.register(name_or_data);
        }
    };

    ActionHandler.prototype.get = function(name){
        warn_bad_name(name);
        return this._actions[name];
    };

    ActionHandler.prototype.call = function(name, event, env){
        return this._actions[name].handler(env|| this.env, event);
    };

    ActionHandler.prototype.exists = function(name){
        return (typeof(this._actions[name]) !== 'undefined');
    };

    return {init:ActionHandler};

});
