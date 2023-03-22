// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

/**
 * @module notebook
 */
"use strict";
define([
    'jquery',
    'base/js/namespace',
    'underscore',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
    'base/js/markdown',
    './cell',
    './textcell',
    './codecell',
    'moment',
    'services/config',
    'services/sessions/session',
    './celltoolbar',
    'codemirror/lib/codemirror',
    'codemirror/addon/runmode/runmode',
    'base/js/mathjaxutils',
    'base/js/keyboard',
    './tooltip',
    './celltoolbarpresets/default',
    './celltoolbarpresets/rawcell',
    './celltoolbarpresets/slideshow',
    './celltoolbarpresets/attachments',
    './celltoolbarpresets/tags',
    './scrollmanager',
    './commandpalette',
    './shortcuteditor',
], function (
    $,
    IPython,
    _,
    utils,
    i18n,
    dialog,
    markdown,
    cellmod,
    textcell,
    codecell,
    moment,
    configmod,
    session,
    celltoolbar,
    CodeMirror,
    runMode,
    mathjaxutils,
    keyboard,
    tooltip,
    default_celltoolbar,
    rawcell_celltoolbar,
    slideshow_celltoolbar,
    attachments_celltoolbar,
    tags_celltoolbar,
    scrollmanager,
    commandpalette,
    shortcuteditor
) {

    var ShortcutEditor = shortcuteditor.ShortcutEditor;

    var _SOFT_SELECTION_CLASS = 'jupyter-soft-selected';

    function soft_selected(cell){
        return cell.element.hasClass(_SOFT_SELECTION_CLASS);
    }

    /**
     * Contains and manages cells.
     * @class Notebook
     * @param {string}          selector
     * @param {object}          options - Dictionary of keyword arguments.  
     * @param {jQuery}          options.events - selector of Events
     * @param {KeyboardManager} options.keyboard_manager
     * @param {Contents}        options.contents
     * @param {SaveWidget}      options.save_widget
     * @param {object}          options.config
     * @param {string}          options.base_url
     * @param {string}          options.notebook_path
     * @param {string}          options.notebook_name
     */
    function Notebook(selector, options) {
        this.config = options.config;
        this.config.loaded.then(this.validate_config.bind(this));
        this.class_config = new configmod.ConfigWithDefaults(this.config, 
                                        Notebook.options_default, 'Notebook');
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url;
        this.notebook_path = options.notebook_path;
        this.notebook_name = options.notebook_name;
        this.events = options.events;
        this.keyboard_manager = options.keyboard_manager;
        this.contents = options.contents;
        this.save_widget = options.save_widget;
        this.tooltip = new tooltip.Tooltip(this.events);
        this.ws_url = options.ws_url;
        this._session_starting = false;
        this.last_modified = null;
        // debug 484
        this._last_modified = 'init';
        // Firefox workaround
        this._ff_beforeunload_fired = false;

        //  Create default scroll manager.
        this.scroll_manager = new scrollmanager.ScrollManager(this);

        // TODO: This code smells (and the other `= this` line a couple lines down)
        // We need a better way to deal with circular instance references.
        this.keyboard_manager.notebook = this;
        this.save_widget.notebook = this;
        
        mathjaxutils.init();

        this.element = $(selector);
        this.element.scroll();
        this.element.data("notebook", this);
        this.session = null;
        this.kernel = null;
        this.kernel_busy = false;
        this.clipboard = null;
        this.clipboard_attachments = null;
        this.undelete_backup_stack = [];
        this.paste_enabled = false;
        this.paste_attachments_enabled = false;
        this.writable = false;
        // It is important to start out in command mode to match the initial mode
        // of the KeyboardManager.
        this.mode = 'command';
        this.set_dirty(false);
        this.metadata = {};
        this._checkpoint_after_save = false;
        this.last_checkpoint = null;
        this.checkpoints = [];
        this.autosave_interval = 0;
        this.autosave_timer = null;
        // autosave *at most* every two minutes
        this.minimum_autosave_interval = 120000;
        this.notebook_name_blacklist_re = /[\/\\:]/;
        this.nbformat = 4; // Increment this when changing the nbformat
        this.nbformat_minor = this.current_nbformat_minor = 1; // Increment this when changing the nbformat
        this.codemirror_mode = 'text';
        this.create_elements();
        this.bind_events();
        this.kernel_selector = null;
        this.dirty = null;
        this.trusted = null;
        this._changed_on_disk_dialog = null;
        this._fully_loaded = false;

        // Trigger cell toolbar registration.
        default_celltoolbar.register(this);
        rawcell_celltoolbar.register(this);
        slideshow_celltoolbar.register(this);
        attachments_celltoolbar.register(this);
        tags_celltoolbar.register(this);

        var that = this;

        Object.defineProperty(this, 'line_numbers', {
            get: function() {
                var d = that.config.data || {};
                var cmc =  (d['Cell'] || {}) ['cm_config'] || {};
                return cmc['lineNumbers'] || false;
            },
            set: function(value) {
                that.config.update({
                    'Cell': {
                        'cm_config': {
                            'lineNumbers':value
                        }
                    }
                });
            }
        });
        
        Object.defineProperty(this, 'header', {
            get: function() {
                return that.class_config.get_sync('Header');
            },
            set: function(value) {
                that.class_config.set('Header', value);
            }
        });
                
        Object.defineProperty(this, 'toolbar', {
            get: function() {
                return that.class_config.get_sync('Toolbar');
            },
            set: function(value) {
                that.class_config.set('Toolbar', value);
            }
        });
        
        this.class_config.get('Header').then(function(header) {
            if (header === false) {
                that.keyboard_manager.actions.call('jupyter-notebook:hide-header');
            }
        });
        
        this.class_config.get('Toolbar').then(function(toolbar) {
          if (toolbar === false) {
              that.keyboard_manager.actions.call('jupyter-notebook:hide-toolbar');
          }
        });
        
        // prevent assign to miss-typed properties.
        Object.seal(this);
    }

    Notebook.options_default = {
        // can be any cell type, or the special values of
        // 'above', 'below', or 'selected' to get the value from another cell.
        default_cell_type: 'code',
        Header: true,
        Toolbar: true,
        kill_kernel: false
    };

    Notebook.prototype.validate_config = function() {
        var code_cell = this.config.data['CodeCell'] || {};
        var cm_keymap = (code_cell['cm_config'] || {})['keyMap'];
        if (cm_keymap && CodeMirror.keyMap[cm_keymap] === undefined) {
            console.warn('CodeMirror keymap not found, ignoring: ' + cm_keymap);
            delete code_cell.cm_config.keyMap;
        }
    };

    /**
     * Create an HTML and CSS representation of the notebook.
     */
    Notebook.prototype.create_elements = function () {
        var that = this;
        this.element.attr('tabindex','-1');
        this.container = $("<div/>").addClass("container").attr("id", "notebook-container");
        // We add this end_space div to the end of the notebook div to:
        // i) provide a margin between the last cell and the end of the notebook
        // ii) to prevent the div from scrolling up when the last cell is being
        // edited, but is too low on the page, which browsers will do automatically.
        var end_space = $('<div/>')
            .addClass('end_space');
        end_space.dblclick(function () {
            var ncells = that.ncells();
            that.insert_cell_below('code',ncells-1);
        });
        this.element.append(this.container);
        this.container.after(end_space);
    };

    /**
     * Bind JavaScript events: key presses and custom Jupyter events.
     */
    Notebook.prototype.bind_events = function () {
        var that = this;


        this.events.on('set_next_input.Notebook', function (event, data) {
            if (data.replace) {
                data.cell.set_text(data.text);
                if (data.clear_output !== false) {
                  // default (undefined) is true to preserve prior behavior
                  data.cell.clear_output();
                }
            } else {
                var index = that.find_cell_index(data.cell);
                var new_cell = that.insert_cell_below('code',index);
                new_cell.set_text(data.text);
            }
            that.dirty = true;
        });

        this.events.on('unrecognized_cell.Cell', function () {
            that.warn_nbformat_minor();
        });

        this.events.on('unrecognized_output.OutputArea', function () {
            that.warn_nbformat_minor();
        });

        this.events.on('set_dirty.Notebook', function (event, data) {
            that.dirty = data.value;
        });

        this.events.on('trust_changed.Notebook', function (event, trusted) {
            that.trusted = trusted;
        });

        this.events.on('select.Cell', function (event, data) {
            var index = that.find_cell_index(data.cell);
            that.select(index, !data.extendSelection);
        });

        this.events.on('edit_mode.Cell', function (event, data) {
            that.handle_edit_mode(data.cell);
        });

        this.events.on('command_mode.Cell', function (event, data) {
            that.handle_command_mode(data.cell);
        });
        
        this.events.on('spec_changed.Kernel', function(event, data) {
            var existing_spec = that.metadata.kernelspec;
            that.metadata.kernelspec = {
                name: data.name,
                display_name: data.spec.display_name,
                language: data.spec.language,
            };
            if (!existing_spec || ! _.isEqual(existing_spec, that.metadata.kernelspec)) {
                that.set_dirty(true);
            }
            // start a new session
            that.start_session(data.name);
        });

        this.events.on('kernel_ready.Kernel', function(event, data) {
            var kinfo = data.kernel.info_reply;
            if (!kinfo.language_info) {
                delete that.metadata.language_info;
                return;
            }
            var existing_info = that.metadata.language_info;
            var langinfo = kinfo.language_info;
            that.metadata.language_info = langinfo;
            if (!existing_info || ! _.isEqual(existing_info, langinfo)) {
                that.set_dirty(true);
            }
            // Mode 'null' should be plain, unhighlighted text.
            var cm_mode = langinfo.codemirror_mode || langinfo.name || 'null';
            that.set_codemirror_mode(cm_mode);
        });
        
        this.events.on('kernel_idle.Kernel', function () {
            that.kernel_busy = false;
        });
        
        this.events.on('kernel_busy.Kernel', function () {
            that.kernel_busy = true;
        });

        var collapse_time = function (time) {
            var app_height = $('#ipython-main-app').height(); // content height
            var splitter_height = $('div#pager_splitter').outerHeight(true);
            var new_height = app_height - splitter_height;
            that.element.animate({height : new_height + 'px'}, time);
        };

        this.element.bind('collapse_pager', function (event, extrap) {
            var time = (extrap !== undefined) ? ((extrap.duration !== undefined ) ? extrap.duration : 'fast') : 'fast';
            collapse_time(time);
        });

        var expand_time = function (time) {
            var app_height = $('#ipython-main-app').height(); // content height
            var splitter_height = $('div#pager_splitter').outerHeight(true);
            var pager_height = $('div#pager').outerHeight(true);
            var new_height = app_height - pager_height - splitter_height;
            that.element.animate({height : new_height + 'px'}, time);
        };

        this.element.bind('expand_pager', function (event, extrap) {
            var time = (extrap !== undefined) ? ((extrap.duration !== undefined ) ? extrap.duration : 'fast') : 'fast';
            expand_time(time);
        });


        // Firefox 22 broke $(window).on("beforeunload")
        // I'm not sure why or how.
        window.onbeforeunload = function () {
            /* Make kill kernel configurable.
            example in custom.js:
                var notebook = Jupyter.notebook;
                var config = notebook.config;
                var patch = {
                    Notebook:{
                        kill_kernel: true
                    }
                };
                config.update(patch);
            */
            var kill_kernel = that.class_config.get_sync("kill_kernel");
            if (kill_kernel) {
                that.session.delete();
            }
            if ( utils.browser[0] === "Firefox") {
                // Workaround ancient Firefox bug showing beforeunload twice: https://bugzilla.mozilla.org/show_bug.cgi?id=531199
                if (that._ff_beforeunload_fired) {
                    return; // don't show twice on FF
                }
                that._ff_beforeunload_fired = true;
                // unset flag immediately after dialog is dismissed
                setTimeout(function () {
                    that._ff_beforeunload_fired = false;
                }, 1);
            }
            // if we are autosaving, trigger an autosave on nav-away.
            // still warn, because if we don't the autosave may fail.
            if (that.dirty) {
                if ( that.autosave_interval ) {
                    // schedule autosave in a timeout
                    // this gives you a chance to forcefully discard changes
                    // by reloading the page if you *really* want to.
                    // the timer doesn't start until you *dismiss* the dialog.
                    setTimeout(function () {
                        if (that.dirty) {
                            that.save_notebook();
                        }
                    }, 1000);
                    return i18n.msg._("Autosave in progress, latest changes may be lost.");
                } else {
                    return i18n.msg._("Unsaved changes will be lost.");
                }
            }
            // if the kernel is busy, prompt the user if he’s sure
            if (that.kernel_busy) {
                return i18n.msg._("The Kernel is busy, outputs may be lost.");
            }
            // IE treats null as a string.  Instead just return which will avoid the dialog.
            return;
        };
    };
    

    Notebook.prototype.show_command_palette = function() {
        new commandpalette.CommandPalette(this);
    };

    Notebook.prototype.show_shortcuts_editor = function() {
        new ShortcutEditor(this);
    };

    /**
     * Trigger a warning dialog about missing functionality from newer minor versions
     */
    Notebook.prototype.warn_nbformat_minor = function () {
        var v = 'v' + this.nbformat + '.';
        var orig_vs = v + this.nbformat_minor;
        var this_vs = v + this.current_nbformat_minor;
        var msg = i18n.msg.sprintf(i18n.msg._("This notebook is version %1$s, but we only fully support up to %2$s."),
                orig_vs,this_vs) + " " +
                i18n.msg._("You can still work with this notebook, but cell and output types introduced in later notebook versions will not be available.");

        // This statement is used simply so that message extraction
        // will pick up the strings.  The actual setting of the text
        // for the button is in dialog.js.
        var button_labels = [ 
            i18n.msg._("OK"),
            i18n.msg._("Restart and Run All Cells"),
            i18n.msg._("Restart and Clear All Outputs"),
            i18n.msg._("Restart"),
            i18n.msg._("Continue Running"),
            i18n.msg._("Reload"),
            i18n.msg._("Cancel"),
            i18n.msg._("Overwrite"),
            i18n.msg._("Trust"),
            i18n.msg._("Revert")];
        
        dialog.modal({
            notebook: this,
            keyboard_manager: this.keyboard_manager,
            title : i18n.msg._("Newer Notebook"),
            body : msg,
            buttons : {
                OK : {
                    "class" : "btn-danger"
                }
            }
        });
    };

    /**
     * Set the dirty flag, and trigger the set_dirty.Notebook event
     */
    Notebook.prototype.set_dirty = function (value) {
        if (value === undefined) {
            value = true;
        }
        if (this.dirty === value) {
            return;
        }
        this.events.trigger('set_dirty.Notebook', {value: value});
    };

    /**
     * Scroll the top of the page to a given cell.
     * 
     * @param {integer}  index - An index of the cell to view
     * @param {integer}  time - Animation time in milliseconds
     * @return {integer} Pixel offset from the top of the container
     */
    Notebook.prototype.scroll_to_cell = function (index, time) {
        return this.scroll_cell_percent(index, 0, time);
    };

    /**
     * Scroll the middle of the page to a given cell.
     *
     * @param {integer}  index - An index of the cell to view
     * @param {integer}  percent - 0-100, the location on the screen to scroll.
     *                   0 is the top, 100 is the bottom.
     * @param {integer}  time - Animation time in milliseconds
     * @return {integer} Pixel offset from the top of the container
     */
    Notebook.prototype.scroll_cell_percent = function (index, percent, time) {
        var cells = this.get_cells();
        time = time || 0;
        percent = percent || 0;
        index = Math.min(cells.length-1,index);
        index = Math.max(0             ,index);
        var sme = this.scroll_manager.element;
        var h = sme.height();
        var st = sme.scrollTop();
        var t = sme.offset().top;
        var ct = cells[index].element.offset().top;
        var scroll_value =  st + ct - (t + 0.01 * percent * h);
        this.scroll_manager.element.animate({scrollTop:scroll_value}, time);
        return scroll_value;
    };

    /**
     * Scroll to the bottom of the page.
     */
    Notebook.prototype.scroll_to_bottom = function () {
        this.scroll_manager.element.animate({scrollTop:this.element.get(0).scrollHeight}, 0);
    };

    /**
     * Scroll to the top of the page.
     */
    Notebook.prototype.scroll_to_top = function () {
        this.scroll_manager.element.animate({scrollTop:0}, 0);
    };

    // Edit Notebook metadata

    /**
     * Display a dialog that allows the user to edit the Notebook's metadata.
     */
    Notebook.prototype.edit_metadata = function () {
        var that = this;
        dialog.edit_metadata({
            md: this.metadata, 
            callback: function (new_md) {
                if(!_.isEqual(that.metadata, new_md)){
                    that.set_dirty(true);
                }
                that.metadata = new_md;
            },
            name: 'Notebook',
            notebook: this,
            keyboard_manager: this.keyboard_manager});
    };

    // Cell indexing, retrieval, etc.

    /**
     * Get all cell elements in the notebook.
     * 
     * @return {jQuery} A selector of all cell elements
     */
    Notebook.prototype.get_cell_elements = function () {
        var container = this.container || $('#notebook-container');
        return container.find(".cell").not('.cell .cell');
    };

    /**
     * Get a particular cell element.
     * 
     * @param {integer} index An index of a cell to select
     * @return {jQuery} A selector of the given cell.
     */
    Notebook.prototype.get_cell_element = function (index) {
        var result = null;
        var e = this.get_cell_elements().eq(index);
        if (e.length !== 0) {
            result = e;
        }
        return result;
    };

    /**
     * Try to get a particular cell by msg_id.
     * 
     * @param {string} msg_id A message UUID
     * @return {Cell} Cell or null if no cell was found.
     */
    Notebook.prototype.get_msg_cell = function (msg_id) {
        return codecell.CodeCell.msg_cells[msg_id] || null;
    };

    /**
     * Count the cells in this notebook.
     * 
     * @return {integer} The number of cells in this notebook
     */
    Notebook.prototype.ncells = function () {
        return this.get_cell_elements().length;
    };

    /**
     * Get all cell objects in this notebook.
     * 
     * @return {Array} This notebook's Cell objects
     */
    Notebook.prototype.get_cells = function () {
        // TODO: we are often calling cells as cells()[i], which we should optimize
        // to cells(i) or a new method.
        return this.get_cell_elements().toArray().map(function (e) {
            return $(e).data("cell");
        });
    };

    /**
     * Get a cell object from this notebook.
     * 
     * @param {integer} index - An index of a cell to retrieve
     * @return {Cell} Cell or null if no cell was found.
     */
    Notebook.prototype.get_cell = function (index) {
        var result = null;
        var ce = this.get_cell_element(index);
        if (ce !== null) {
            result = ce.data('cell');
        }
        return result;
    };

    /**
     * Get the cell below a given cell.
     * 
     * @param {Cell} cell
     * @return {Cell} the next cell or null if no cell was found.
     */
    Notebook.prototype.get_next_cell = function (cell) {
        var result = null;
        var index = this.find_cell_index(cell);
        if (this.is_valid_cell_index(index+1)) {
            result = this.get_cell(index+1);
        }
        return result;
    };
    
    /**
     * Toggles the display of line numbers in all cells.
     */
    Notebook.prototype.toggle_all_line_numbers = function () {
        this.line_numbers = !this.line_numbers;
    };

    /**
     * Reads direction settings (LTR/RTL) from nbclassic/cells metadata
     * and applies them to display elements.
     */
    Notebook.prototype.apply_directionality = function () {
        var notebook_direction = this.metadata.direction || 'ltr';
        // html
        document.body.setAttribute('dir', notebook_direction);
        // existing cells
        this.get_cells().forEach( function(cell) {
            if (cell.cell_type == 'markdown') {
                cell.code_mirror.setOption('direction', cell.metadata.direction || notebook_direction);
                cell.element.find('.rendered_html').attr('dir', cell.metadata.direction || notebook_direction);
            } else if (cell.cell_type == 'code') {
                cell.element.find('.output_text').attr('dir', cell.metadata.direction || 'auto');
            }
        });
        // new cells
        textcell.MarkdownCell.options_default.cm_config.direction = notebook_direction;
    };

    /**
     * Get the cell above a given cell.
     * 
     * @param {Cell} cell
     * @return {Cell} The previous cell or null if no cell was found.
     */
    Notebook.prototype.get_prev_cell = function (cell) {
        var result = null;
        var index = this.find_cell_index(cell);
        if (index !== null && index > 0) {
            result = this.get_cell(index-1);
        }
        return result;
    };
    
    /**
     * Get the numeric index of a given cell.
     * 
     * @param {Cell} cell
     * @return {integer} The cell's numeric index or null if no cell was found.
     */
    Notebook.prototype.find_cell_index = function (cell) {
        var result = null;
        this.get_cell_elements().filter(function (index) {
            if ($(this).data("cell") === cell) {
                result = index;
            }
        });
        return result;
    };

    /**
     * Return given index if defined, or the selected index if not.
     * 
     * @param {integer} [index] - A cell's index
     * @return {integer} cell index
     */
    Notebook.prototype.index_or_selected = function (index) {
        var i;
        if (index === undefined || index === null) {
            i = this.get_selected_index();
            if (i === null) {
                i = 0;
            }
        } else {
            i = index;
        }
        return i;
    };

    /**
     * Get the selected cells.
     * 
     * @return {Cell} The selected cells or null if no cell was found.
     */
    Notebook.prototype.get_selected_cells = function () {
        return this.get_cells().filter(function(cell, index){ return cell.selected || soft_selected(cell) || cell.anchor;});
    };
    
     /**
     * Get the selected cells.
     * 
     * @return {array} cell indicies
     */
    Notebook.prototype.get_selected_cells_indices = function () {
        var result = [];
        this.get_cells().filter(function (cell, index) {
            if (cell.selected || soft_selected(cell) || cell.anchor) {
                result.push(index);
            }
        });
        return result;
    };

    /**
     * Get the currently selected cell.
     * 
     * @return {Cell} The selected cell
     */
    Notebook.prototype.get_selected_cell = function () {
        var index = this.get_selected_index();
        return this.get_cell(index);
    };

    /**
     * Check whether a cell index is valid.
     * 
     * @param {integer} index - A cell index
     * @return True if the index is valid, false otherwise
     */
    Notebook.prototype.is_valid_cell_index = function (index) {
        if (index !== null && index >= 0 && index < this.ncells()) {
            return true;
        } else {
            return false;
        }
    };

    /**
     * Returns the index of the cell that the selection is currently anchored on.
     *
     * @return {integer} Index of first cell selected in selection
     */
    Notebook.prototype.get_anchor_index = function () {
        var result = null;
        this.get_cell_elements().filter(function (index) {
            if ($(this).data("cell").anchor === true) {
                result = index;
            }
        });
        return result;
    };

    /**
     * Get the index of the currently selected cell.
     *
     * @return {integer} The selected cell's numeric index
     */
    Notebook.prototype.get_selected_index = function () {
        var result = null;
        this.get_cell_elements().filter(function (index) {
            if ($(this).data("cell").selected === true) {
                result = index;
            }
        });
        return result;
    };


    // Cell selection.

    Notebook.prototype.extend_selection_by = function(delta) {
        var index = this.get_selected_index();
        // do not move anchor
        return this.select(index+delta, false);
    };


    Notebook.prototype.update_soft_selection = function(){
        var i1 = this.get_selected_index();
        var i2 = this.get_anchor_index();
        var low  = Math.min(i1, i2);
        var high = Math.max(i1, i2);
        this.get_cells().map(function(cell, index, all){
            if( low <= index && index <= high && low !== high){
                cell.element.addClass(_SOFT_SELECTION_CLASS);
            } else {
                cell.element.removeClass(_SOFT_SELECTION_CLASS);
            }
        });
    };


    Notebook.prototype.select_all = function(){
        this.select(0, true);
        this.select(this.ncells()-1, false);
    };

    Notebook.prototype._contract_selection = function(){
        var i = this.get_selected_index();
        this.select(i, true);
    };

    /**
     * Programmatically select a cell.
     * 
     * @param {integer} index - A cell's index
     * @param {boolean} moveanchor – whether to move the selection
     *               anchor, default to true.
     * @return {Notebook} This notebook
     */
    Notebook.prototype.select = function (index, moveanchor) {
        moveanchor = (moveanchor===undefined)? true : moveanchor;

        if (this.is_valid_cell_index(index)) {
            var sindex = this.get_selected_index();
            if (sindex !== null && index !== sindex) {
                // If we are about to select a different cell, make sure we are
                // first in command mode.
                if (this.mode !== 'command') {
                    this.command_mode();
                }
                this.get_cell(sindex).unselect(moveanchor);
            }
            if(moveanchor){
                this.get_cell(this.get_anchor_index()).unselect(moveanchor);
            }
            var cell = this.get_cell(index);
            cell.select(moveanchor);
            this.update_soft_selection();
            if (cell.cell_type === 'heading') {
                this.events.trigger('selected_cell_type_changed.Notebook',
                    {
                        'cell_type': cell.cell_type,
                        'level': cell.level,
                        'editable': cell.is_editable()
                    }
                );
            } else {
                this.events.trigger('selected_cell_type_changed.Notebook',
                    {
                        'cell_type': cell.cell_type,
                        'editable': cell.is_editable()
                    }
                );
            }
        }
        return this;
    };

    /**
     * Programmatically select the next cell.
     *
     * @param {bool} moveanchor – whether to move the selection
     *               anchor, default to true.
     * @return {Notebook} This notebook
     */
    Notebook.prototype.select_next = function (moveanchor) {
        var index = this.get_selected_index();
        this.select(index+1, moveanchor);
        return this;
    };

    /**
     * Programmatically select the previous cell.
     *
     * @return {Notebook} This notebook
     */
    Notebook.prototype.select_prev = function (moveanchor) {
        var index = this.get_selected_index();
        this.select(index-1, moveanchor);
        return this;
    };


    // Edit/Command mode

    /**
     * Gets the index of the cell that is in edit mode.
     *
     * @return {integer} index
     */
    Notebook.prototype.get_edit_index = function () {
        var result = null;
        this.get_cell_elements().filter(function (index) {
            if ($(this).data("cell").mode === 'edit') {
                result = index;
            }
        });
        return result;
    };

    /**
     * Handle when a a cell blurs and the notebook should enter command mode.
     *
     * @param {Cell} [cell] - Cell to enter command mode on.
     */
    Notebook.prototype.handle_command_mode = function (cell) {
        if (this.mode !== 'command') {
            cell.command_mode();
            this.mode = 'command';
            this.events.trigger('command_mode.Notebook');
            this.keyboard_manager.command_mode();
        }
    };

    /**
     * Make the notebook enter command mode.
     */
    Notebook.prototype.command_mode = function () {
        var cell = this.get_cell(this.get_edit_index());
        if (cell && this.mode !== 'command') {
            // We don't call cell.command_mode, but rather blur the CM editor
            // which will trigger the call to handle_command_mode.
            cell.code_mirror.getInputField().blur();
        }
    };

    /**
     * Handle when a cell fires it's edit_mode event.
     *
     * @param {Cell} [cell] Cell to enter edit mode on.
     */
    Notebook.prototype.handle_edit_mode = function (cell) {
        this._contract_selection();
        if (cell && this.mode !== 'edit') {
            cell.edit_mode();
            this.mode = 'edit';
            this.events.trigger('edit_mode.Notebook');
            this.keyboard_manager.edit_mode();
        }
    };

    /**
     * Make a cell enter edit mode.
     */
    Notebook.prototype.edit_mode = function () {
        this._contract_selection();
        var cell = this.get_selected_cell();
        if (cell && this.mode !== 'edit') {
            cell.unrender();
            cell.focus_editor();
        }
    };
    
    /**
     * Ensure either cell or codemirror is focused. If none 
     * is focused, focus the cell.
     */
    Notebook.prototype.ensure_focused = function(){
        var cell = this.get_selected_cell();
        if (cell === null) {return;}  // No cell is selected
        cell.ensure_focused();
    };

    /**
     * Focus the currently selected cell.
     */
    Notebook.prototype.focus_cell = function () {
        var cell = this.get_selected_cell();
        if (cell === null) {return;}  // No cell is selected
        cell.focus_cell();
    };

    // Cell movement

    /**
     * Move the current selection up, keeping the same cells selected
     * No op if the selection is at the beginning of the notebook
     */
    Notebook.prototype.move_selection_up = function(){
        // actually will move the cell before the selection, after the selection
        var indices = this.get_selected_cells_indices();
        var first = indices[0];
        var last = indices[indices.length - 1];

        var selected = this.get_selected_index();
        var anchored = this.get_anchor_index();

        if (first === 0){
            return;
        }
        var tomove = this.get_cell_element(first - 1);
        var pivot = this.get_cell_element(last);

        tomove.detach();
        pivot.after(tomove);

        this.get_cell(selected-1).focus_cell();
        this.select(anchored - 1);
        this.select(selected - 1, false);
    };

    /**
     * Move the current selection down, keeping the same cells selected.
     * No op if the selection is at the end of the notebook
     */
    Notebook.prototype.move_selection_down = function(){
        // actually will move the cell after the selection, before the selection
        var indices = this.get_selected_cells_indices();
        var first = indices[0];
        var last = indices[indices.length - 1];

        var selected = this.get_selected_index();
        var anchored = this.get_anchor_index();

        if(!this.is_valid_cell_index(last + 1)){
            return;
        }
        var tomove = this.get_cell_element(last + 1);
        var pivot = this.get_cell_element(first);

        tomove.detach();
        pivot.before(tomove);

        this.get_cell(selected+1).focus_cell();
        this.select(first);
        this.select(anchored + 1);
        this.select(selected + 1, false);
    };

    /**
     * Move given (or selected) cell up and select it.
     * 
     * @param {integer} [index] - cell index
     * @return {Notebook} This notebook
     */
    Notebook.prototype.move_cell_up = function (index) {
        console.warn('Notebook.move_cell_up is deprecated as of v4.1 and will be removed in v5.0');

        if(index === undefined){
            this.move_selection_up();
            return this;
        }
        
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i) && i > 0) {
            var pivot = this.get_cell_element(i-1);
            var tomove = this.get_cell_element(i);
            if (pivot !== null && tomove !== null) {
                tomove.detach();
                pivot.before(tomove);
                this.select(i-1);
                var cell = this.get_selected_cell();
                cell.focus_cell();
            }
            this.set_dirty(true);
        }
        return this;
    };


    /**
     * Move given (or selected) cell down and select it.
     * 
     * @param {integer} [index] - cell index
     * @return {Notebook} This notebook
     */
    Notebook.prototype.move_cell_down = function (index) {
        console.warn('Notebook.move_cell_down is deprecated as of v4.1 and will be removed in v5.0');

        if(index === undefined){
            this.move_selection_down();
            return this;
        }
        
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i) && this.is_valid_cell_index(i+1)) {
            var pivot = this.get_cell_element(i+1);
            var tomove = this.get_cell_element(i);
            if (pivot !== null && tomove !== null) {
                tomove.detach();
                pivot.after(tomove);
                this.select(i+1);
                var cell = this.get_selected_cell();
                cell.focus_cell();
            }
        }
        this.set_dirty();
        return this;
    };


    // Insertion, deletion.

    /**
     * Delete a cell from the notebook without any precautions
     * Needed to reload checkpoints and other things like that.
     * 
     * @param {integer} [index] - cell's numeric index
     * @return {Notebook} This notebook
     */
    Notebook.prototype._unsafe_delete_cell = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);

        $('#undelete_cell').addClass('disabled');
        $('#undelete_cell > a').attr('aria-disabled','true');
        if (this.is_valid_cell_index(i)) {
            var old_ncells = this.ncells();
            var ce = this.get_cell_element(i);
            ce.remove();
            this.set_dirty(true);
        }
        return this;
    };


    /**
     * Delete cells from the notebook
     *
     * @param {Array} [indices] - the numeric indices of cells to delete.
     * @return {Notebook} This notebook
     */
    Notebook.prototype.delete_cells = function(indices) {
        if (indices === undefined) {
            indices = this.get_selected_cells_indices();
        }

        var undelete_backup = {
            cells: [],
            below: false,
            index: 0,
        };

        var cursor_ix_before = this.get_selected_index();
        var deleting_before_cursor = 0;
        for (var i=0; i < indices.length; i++) {
            if (!this.get_cell(indices[i]).is_deletable()) {
                // If any cell is marked undeletable, cancel
                return this;
            }

            if (indices[i] < cursor_ix_before) {
                deleting_before_cursor++;
            }
        }

        // If we started deleting cells from the top, the later indices would
        // get offset. We sort them into descending order to avoid that.
        indices.sort(function(a, b) {return b-a;});
        for (i=0; i < indices.length; i++) {
            var cell = this.get_cell(indices[i]);
            undelete_backup.cells.push(cell.toJSON());
            this.get_cell_element(indices[i]).remove();
            this.events.trigger('delete.Cell', {'cell': cell, 'index': indices[i]});
        }

        var new_ncells = this.ncells();
        // Always make sure we have at least one cell.
        if (new_ncells === 0) {
            this.insert_cell_below('code');
            new_ncells = 1;
        }

        var cursor_ix_after = this.get_selected_index();
        if (cursor_ix_after === null) {
            // Selected cell was deleted
            cursor_ix_after = cursor_ix_before - deleting_before_cursor;
            if (cursor_ix_after >= new_ncells) {
                cursor_ix_after = new_ncells - 1;
                undelete_backup.below = true;
            }
            this.select(cursor_ix_after);
        }

        // Check if the cells were after the cursor
        for (i=0; i < indices.length; i++) {
            if (indices[i] > cursor_ix_before) {
                undelete_backup.below = true;
            }
        }

        // This will put all the deleted cells back in one location, rather than
        // where they came from. It will do until we have proper undo support.
        undelete_backup.index = cursor_ix_after;
        $('#undelete_cell').removeClass('disabled');
        $('#undelete_cell > a').attr('aria-disabled','false');
        this.undelete_backup_stack.push(undelete_backup);
        this.set_dirty(true);

        return this;
    };

    /**
     * Delete a cell from the notebook.
     * 
     * @param {integer} [index] - cell's numeric index
     * @return {Notebook} This notebook
     */
    Notebook.prototype.delete_cell = function (index) {
        if (index === undefined) {
            return this.delete_cells();
        } else {
            return this.delete_cells([index]);
        }
    };

    /**
     * Restore the most recently deleted cells.
     */
    Notebook.prototype.undelete_cell = function() {
        if (this.undelete_backup_stack.length > 0) {
            var undelete_backup = this.undelete_backup_stack.pop();
            var i, cell_data, new_cell, insert;
            if (undelete_backup.below) {
                insert = $.proxy(this.insert_cell_below, this);
            } else {
                insert = $.proxy(this.insert_cell_above, this);
            }
            for (i=0; i < undelete_backup.cells.length; i++) {
                cell_data = undelete_backup.cells[i];
                new_cell = insert(cell_data.cell_type, undelete_backup.index);
                new_cell.fromJSON(cell_data);
            }

            this.set_dirty(true);
        }
        if (this.undelete_backup_stack.length === 0) {
            $('#undelete_cell').addClass('disabled');
            $('#undelete_cell > a').attr('aria-disabled','true');
        }
    };

    /**
     * Insert a cell so that after insertion the cell is at given index.
     *
     * If cell type is not provided, it will default to the type of the
     * currently active cell.
     *
     * Similar to insert_above, but index parameter is mandatory.
     *
     * Index will be brought back into the accessible range [0,n].
     *
     * @param {string} [type] - in ['code','markdown', 'raw'], defaults to 'code'
     * @param {integer} [index] - a valid index where to insert cell
     * @return {Cell|null} created cell or null
     */
    Notebook.prototype.insert_cell_at_index = function(type, index){

        var ncells = this.ncells();
        index = Math.min(index, ncells);
        index = Math.max(index, 0);
        var cell = null;
        type = type || this.class_config.get_sync('default_cell_type');
        if (type === 'above') {
            if (index > 0) {
                type = this.get_cell(index-1).cell_type;
            } else {
                type = 'code';
            }
        } else if (type === 'below') {
            if (index < ncells) {
                type = this.get_cell(index).cell_type;
            } else {
                type = 'code';
            }
        } else if (type === 'selected') {
            type = this.get_selected_cell().cell_type;
        }

        if (ncells === 0 || this.is_valid_cell_index(index) || index === ncells) {
            var cell_options = {
                events: this.events, 
                config: this.config, 
                keyboard_manager: this.keyboard_manager, 
                notebook: this,
                tooltip: this.tooltip
            };
            switch(type) {
            case 'code':
                cell = new codecell.CodeCell(this.kernel, cell_options);
                cell.set_input_prompt();
                break;
            case 'markdown':
                cell = new textcell.MarkdownCell(cell_options);
                break;
            case 'raw':
                cell = new textcell.RawCell(cell_options);
                break;
            default:
                console.log("Unrecognized cell type: ", type, cellmod);
                cell = new cellmod.UnrecognizedCell(cell_options);
            }

            if(this._insert_element_at_index(cell.element,index)) {
                cell.render();
                this.events.trigger('create.Cell', {'cell': cell, 'index': index});
                cell.refresh();
                // We used to select the cell after we refresh it, but there
                // are now cases were this method is called where select is
                // not appropriate. The selection logic should be handled by the
                // caller of the the top level insert_cell methods.
                this.set_dirty(true);
            }
        }
        return cell;

    };

    /**
     * Insert an element at given cell index.
     *
     * @param {HTMLElement} element - a cell element
     * @param {integer}     [index] - a valid index where to inser cell
     * @returns {boolean}   success
     */
    Notebook.prototype._insert_element_at_index = function(element, index){
        if (element === undefined){
            return false;
        }

        var ncells = this.ncells();

        if (ncells === 0) {
            // special case append if empty
            this.container.append(element);
        } else if ( ncells === index ) {
            // special case append it the end, but not empty
            this.get_cell_element(index-1).after(element);
        } else if (this.is_valid_cell_index(index)) {
            // otherwise always somewhere to append to
            this.get_cell_element(index).before(element);
        } else {
            return false;
        }
        
        this.undelete_backup_stack.map(function (undelete_backup) {
            if (index < undelete_backup.index) {
                undelete_backup.index += 1;
            }
        });
        this.set_dirty(true);
        return true;
    };

    /**
     * Insert a cell of given type above given index, or at top
     * of notebook if index smaller than 0.
     *
     * @param {string}     [type] - cell type
     * @param {integer}    [index] - defaults to the currently selected cell
     * @return {Cell|null} handle to created cell or null
     */
    Notebook.prototype.insert_cell_above = function (type, index) {
        if (index === null || index === undefined) {
            index = Math.min(this.get_selected_index(index), this.get_anchor_index());
        }
        return this.insert_cell_at_index(type, index);
    };

    /**
     * Insert a cell of given type below given index, or at bottom
     * of notebook if index greater than number of cells
     *
     * @param {string}     [type] - cell type
     * @param {integer}    [index] - defaults to the currently selected cell
     * @return {Cell|null} handle to created cell or null
     */
    Notebook.prototype.insert_cell_below = function (type, index) {
        if (index === null || index === undefined) {            
            index = Math.max(this.get_selected_index(index), this.get_anchor_index());
        }
        return this.insert_cell_at_index(type, index+1);
    };


    /**
     * Insert cell at end of notebook
     *
     * @param {string} type - cell type
     * @return {Cell|null} handle to created cell or null
     */
    Notebook.prototype.insert_cell_at_bottom = function (type){
        var len = this.ncells();
        return this.insert_cell_below(type,len-1);
    };

    /**
     * Transfer contents from one cell to a new type cell
     */
    Notebook.prototype.transfer_to_new_cell = function (source_cell, target_cell){
        var text = source_cell.get_text();

        if (text === source_cell.placeholder) {
            text = '';
        }
        // metadata
        target_cell.metadata = source_cell.metadata;
        target_cell.attachments = source_cell.attachments;

        // We must show the editor before setting its contents
        target_cell.unrender();
        target_cell.set_text(text);
        // make this value the starting point, so that we can only undo
        // to this state, instead of a blank cell
        target_cell.code_mirror.clearHistory();
        source_cell.element.remove();
    }
    
    /**
     * Turn one or more cells into code.
     *
     * @param {Array} indices - cell indices to convert
     */
    Notebook.prototype.cells_to_code = function (indices) {
        if (indices === undefined){
            indices = this.get_selected_cells_indices();
        }
        
        for (var i=0; i <indices.length; i++){
            this.to_code(indices[i]);
        }
    };

    /**
     * Turn a cell into a code cell.
     * 
     * @param {integer} [index] - cell index
     */
    Notebook.prototype.to_code = function (index) {
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i)) {
            var source_cell = this.get_cell(i);
            if (!(source_cell instanceof codecell.CodeCell) && source_cell.is_editable()) {
                var target_cell = this.insert_cell_below('code',i);
                var text = source_cell.get_text();
                if (text === source_cell.placeholder) {
                    text = '';
                }
                //metadata
                target_cell.metadata = source_cell.metadata;
                // attachments (we transfer them so they aren't lost if the
                // cell is turned back into markdown)
                target_cell.attachments = source_cell.attachments;

                target_cell.set_text(text);
                // make this value the starting point, so that we can only undo
                // to this state, instead of a blank cell
                target_cell.code_mirror.clearHistory();
                source_cell.element.remove();
                this.select(i);
                var cursor = source_cell.code_mirror.getCursor();
                target_cell.code_mirror.setCursor(cursor);
                this.set_dirty(true);
            }
        }
    };

    /**
     * Turn one or more cells into Markdown.
     *
     * @param {Array} indices - cell indices to convert
     */
     Notebook.prototype.cells_to_markdown = function (indices) {
        if (indices === undefined) {
            indices = this.get_selected_cells_indices();
        }

        for(var i=0; i < indices.length; i++) {
            this.to_markdown(indices[i]);
        }
     };

    /**
     * Turn a cell into a Markdown cell.
     * 
     * @param {integer} [index] - cell index
     */
    Notebook.prototype.to_markdown = function (index) {
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i)) {
            var source_cell = this.get_cell(i);

            if (!(source_cell instanceof textcell.MarkdownCell) && source_cell.is_editable()) {
                var target_cell = this.insert_cell_below('markdown',i);

                this.transfer_to_new_cell(source_cell, target_cell);
                this.select(i);

                if ((source_cell instanceof textcell.TextCell) && source_cell.rendered) {
                    target_cell.render();
                }
                var cursor = source_cell.code_mirror.getCursor();
                target_cell.code_mirror.setCursor(cursor);
                this.set_dirty(true);
            }
        }
    };

    /**
     * Turn one or more cells into a raw text cell.
     *
     * @param {Array} indices - cell indices to convert
     */
     Notebook.prototype.cells_to_raw = function (indices) {
        if (indices === undefined) {
            indices = this.get_selected_cells_indices();
        }

        for(var i=0; i < indices.length; i++) {
            this.to_raw(indices[i]);
        }
     };

    /**
     * Turn a cell into a raw text cell.
     * 
     * @param {integer} [index] - cell index
     */
    Notebook.prototype.to_raw = function (index) {
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i)) {
            var target_cell = null;
            var source_cell = this.get_cell(i);

            if (!(source_cell instanceof textcell.RawCell) && source_cell.is_editable()) {
                target_cell = this.insert_cell_below('raw',i);
                
                this.transfer_to_new_cell(source_cell, target_cell);
                this.select(i);
                
                var cursor = source_cell.code_mirror.getCursor();
                target_cell.code_mirror.setCursor(cursor);
                this.set_dirty(true);
            }
        }
    };
    
    /**
     * Warn about heading cell support removal.
     */
    Notebook.prototype._warn_heading = function () {
        dialog.modal({
            notebook: this,
            keyboard_manager: this.keyboard_manager,
            title : i18n.msg._("Use markdown headings"),
            body : $("<p/>").text(
                i18n.msg._('Jupyter no longer uses special heading cells. ' + 
                'Instead, write your headings in Markdown cells using # characters:')
            ).append($('<pre/>').text(
                i18n.msg._('## This is a level 2 heading')
            )),
            buttons : {
                "OK" : {}
            }
        });
    };
    
    /**
     * Turn a cell into a heading containing markdown cell.
     * 
     * @param {integer} [index] - cell index
     * @param {integer} [level] - heading level (e.g., 1 for h1)
     */
    Notebook.prototype.to_heading = function (index, level) {
        this.to_markdown(index);
        level = level || 1;
        var i = this.index_or_selected(index);
        if (this.is_valid_cell_index(i)) {
            var cell = this.get_cell(i);
            cell.set_heading_level(level);
            this.set_dirty(true);
        }
    };


    // Cut/Copy/Paste

    /**
     * Enable the UI elements for pasting cells.
     */
    Notebook.prototype.enable_paste = function () {
        var that = this;
        if (!this.paste_enabled) {
            $('#paste_cell_replace').removeClass('disabled')
            $('#paste_cell_replace > a').attr('aria-disabled', 'false');
            $('#paste_cell_above').removeClass('disabled')
            $('#paste_cell_above > a').attr('aria-disabled', 'false');
            $('#paste_cell_below').removeClass('disabled')
            $('#paste_cell_below > a').attr('aria-disabled', 'false');
            this.paste_enabled = true;
        }
    };

    /**
     * Disable the UI elements for pasting cells.
     */
    Notebook.prototype.disable_paste = function () {
        if (this.paste_enabled) {
            $('#paste_cell_replace').addClass('disabled');
            $('#paste_cell_replace > a').attr('aria-disabled', 'true');
            $('#paste_cell_above').addClass('disabled');
            $('#paste_cell_above > a').attr('aria-disabled', 'true');
            $('#paste_cell_below').addClass('disabled');
            $('#paste_cell_below > a').attr('aria-disabled', 'true');
            this.paste_enabled = false;
        }
    };

    /**
     * Cut a cell.
     */
    Notebook.prototype.cut_cell = function () {
        this.copy_cell();
        this.delete_cell();
    };

    /**
     * Copy cells.
     */
    Notebook.prototype.copy_cell = function () {
        var cells = this.get_selected_cells();
        if (cells.length === 0) {
            cells = [this.get_selected_cell()];
        }
        
        this.clipboard = [];
        var cell_json;
        for (var i=0; i < cells.length; i++) {
            cell_json = cells[i].toJSON();
            if (cell_json.metadata.deletable !== undefined) {
                delete cell_json.metadata.deletable;
            }
            if (cell_json.id !== undefined) {
                delete cell_json.id;
            }
            this.clipboard.push(cell_json);
        }
        this.enable_paste();
    };

    /**
     * Replace the selected cell with the cells in the clipboard.
     */
    Notebook.prototype.paste_cell_replace = function () {

        if (!(this.clipboard !== null && this.paste_enabled)) {
            return;
        }

        var selected =  this.get_selected_cells_indices();
        var insertion_index = selected[0];
        this.delete_cells(selected);

        for (var i=this.clipboard.length-1; i >= 0; i--) {
            var cell_data = this.clipboard[i];
            var new_cell = this.insert_cell_at_index(cell_data.cell_type, insertion_index);
            new_cell.fromJSON(cell_data);
        }

        this.select(insertion_index+this.clipboard.length-1);
    };

    /**
     * Paste cells from the clipboard above the selected cell.
     */
    Notebook.prototype.paste_cell_above = function () {
        if (this.clipboard !== null && this.paste_enabled) {
            var first_inserted = null;
            for (var i=0; i < this.clipboard.length; i++) {
                var cell_data = this.clipboard[i];
                var new_cell = this.insert_cell_above(cell_data.cell_type);
                new_cell.fromJSON(cell_data);
                if (first_inserted === null) {
                    first_inserted = new_cell;
                }
            }
            first_inserted.focus_cell();
        }
    };

    /**
     * Paste cells from the clipboard below the selected cell.
     */
    Notebook.prototype.paste_cell_below = function () {
        if (this.clipboard !== null && this.paste_enabled) {
            var first_inserted = null;
            for (var i = this.clipboard.length-1; i >= 0; i--) {
                var cell_data = this.clipboard[i];
                var new_cell = this.insert_cell_below(cell_data.cell_type);
                new_cell.fromJSON(cell_data);
                if (first_inserted === null) {
                    first_inserted = new_cell;
                }
            }
            first_inserted.focus_cell();
        }
    };
    
    /**
     * Re-render the output of a code cell.
     */
    Notebook.prototype.render_cell_output = function (code_cell) {
        var cell_data = code_cell.toJSON();
        var cell_index = this.find_cell_index(code_cell);
        var trusted = code_cell.output_area.trusted;
        this.clear_output(cell_index);
        code_cell.output_area.trusted = trusted;
        code_cell.fromJSON(cell_data);
    };

    // Split/merge

    /**
     * Split the selected cell into two cells.
     */
    Notebook.prototype.split_cell = function () {
        var cell = this.get_selected_cell();
        if (cell.is_splittable()) {
            var text_list = cell.get_split_text();
            for (var i = 0; i < text_list.length-1; i++) {
                // Create new cell with same type
                var new_cell = this.insert_cell_above(cell.cell_type);
                // Unrender the new cell so we can call set_text.
                new_cell.unrender();
                new_cell.set_text(text_list[i]);
                // Duplicate metadata
                new_cell.metadata = JSON.parse(JSON.stringify(cell.metadata));
            }
            // Original cell becomes the last one
            // so we don't need to worry about selection
            cell.set_text(text_list[text_list.length-1]);
        }
    };

    /**
     * Merge a series of cells into one
     *
     * @param {Array} indices - the numeric indices of the cells to be merged
     * @param {boolean} into_last - merge into the last cell instead of the first
     */
    Notebook.prototype.merge_cells = function(indices, into_last) {
        if (indices.length <= 1) {
            return;
        }

        // Check if trying to merge above on topmost cell or wrap around
        // when merging above, see #330
        if (indices.filter(function(item) {return item < 0;}).length > 0) {
            return;
        }

        for (var i=0; i < indices.length; i++) {
            if (!this.get_cell(indices[i]).is_mergeable()) {
                return;
            }
        }
        var target = this.get_cell(into_last ? indices.pop() : indices.shift());

        // Get all the cells' contents
        var contents = [];
        for (i=0; i < indices.length; i++) {
            contents.push(this.get_cell(indices[i]).get_text());
        }
        if (into_last) {
            contents.push(target.get_text());
        } else {
            contents.unshift(target.get_text());
        }

        // Update the contents of the target cell
        if (target instanceof codecell.CodeCell) {
            target.set_text(contents.join('\n\n'));
        } else {
            var was_rendered = target.rendered;
            target.unrender(); // Must unrender before we set_text.
            target.set_text(contents.join('\n\n'));
            if (was_rendered) {
                // The rendered state of the final cell should match
                // that of the original selected cell;
                target.render();
            }
        }

        // Delete the other cells
        this.delete_cells(indices);
        
        // Reset the target cell's undo history
        target.code_mirror.clearHistory();

        this.select(this.find_cell_index(target));
    };

    /**
     * Merge the selected range of cells
     */
    Notebook.prototype.merge_selected_cells = function() {
        this.merge_cells(this.get_selected_cells_indices());
    };

    /**
     * Merge the selected cell into the cell above it.
     */
    Notebook.prototype.merge_cell_above = function () {
        var index = this.get_selected_index();
        this.merge_cells([index-1, index], true);
    };

    /**
     * Merge the selected cell into the cell below it.
     */
    Notebook.prototype.merge_cell_below = function () {
        var index = this.get_selected_index();
        this.merge_cells([index, index+1], false);
    };

    // Attachments handling

    /**
     * Shows a dialog letting the user pick an image from her computer and
     * insert it into the edited markdown cell
     */
    Notebook.prototype.insert_image = function () {
        var that = this;
        var cell = this.get_selected_cell();
        // The following should not happen as the menu item is greyed out
        // when those conditions are not fulfilled (see MarkdownCell
        // unselect/select/unrender handlers)
        if (cell.cell_type !== 'markdown') {
            console.log('Error: insert_image called on non-markdown cell');
            return;
        }
        if (cell.rendered) {
            console.log('Error: insert_image called on rendered cell');
            return;
        }
        dialog.insert_image({
            callback: function(file) {
                cell.edit_mode();
                cell.insert_inline_image_from_blob(file);
            },
            notebook: this,
            keyboard_manager: this.keyboard_manager
        });
    };

    /**
     * Cut the attachments of a cell
     */
    Notebook.prototype.cut_cell_attachments = function() {
        var cell = this.get_selected_cell();
        if (cell.attachments !== undefined) {
            this.clipboard_attachments = cell.attachments;
            this.enable_attachments_paste();
            delete cell.attachments;
            cell.unrender();
            cell.render();
        }
    };

    /**
     * Copy the attachments of a cell
     */
    Notebook.prototype.copy_cell_attachments = function() {
        var cell = this.get_selected_cell();
        if (cell.attachments !== undefined) {
          // Do a deep copy of attachments to avoid subsequent modification
          // to the cell to modify the clipboard
          this.clipboard_attachments = $.extend(true, {}, cell.attachments);
          this.enable_attachments_paste();
        }
    };

    /**
     * Paste the attachments in the clipboard into the currently selected
     * cell
     */
    Notebook.prototype.paste_cell_attachments = function() {
        if (this.clipboard_attachments !== null &&
            this.paste_attachments_enabled) {
            var cell = this.get_selected_cell();
            if (cell.attachments === undefined) {
              cell.attachments = {};
            }
            // Do a deep copy so we can paste multiple times
            $.extend(true, cell.attachments, this.clipboard_attachments);
            cell.unrender();
            cell.render();
        }
    };

    /**
     * Disable the "Paste Cell Attachments" menu item
     */
    Notebook.prototype.disable_attachments_paste = function () {
        if (this.paste_attachments_enabled) {
            $('#paste_cell_attachments').addClass('disabled');
            $('#paste_cell_attachments > a').attr('disabled','true');
            this.paste_attachments_enabled = false;
        }
    };

    /**
     * Enable the "Paste Cell Attachments" menu item
     */
    Notebook.prototype.enable_attachments_paste = function () {
        if (!this.paste_attachments_enabled) {
            $('#paste_cell_attachments').removeClass('disabled');
            $('#paste_cell_attachments > a').attr('aria-disabled','false');
            this.paste_attachments_enabled = true;
        }
    };

    /**
     * Enable/disable the "Insert image" menu item
     */
    Notebook.prototype.set_insert_image_enabled = function(enabled) {
        if (enabled) {
            $('#insert_image').removeClass('disabled');
            $('#insert_image > a').attr('aria-disabled', 'false');
        } else {
            $('#insert_image').addClass('disabled');
            $('#insert_image > a').attr('aria-disabled', 'true');
        }
    };

    // Cell collapsing and output clearing

    /**
     * Hide a cell's output.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.collapse_output = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.collapse_output();
            this.set_dirty(true);
        }
    };

    /**
     * Hide each code cell's output area.
     */
    Notebook.prototype.collapse_all_output = function () {
        this.get_cells().map(function (cell) {
            if (cell instanceof codecell.CodeCell) {
                cell.collapse_output();
            }
        });
        // this should not be set if the `collapse` key is removed from nbformat
        this.set_dirty(true);
    };

    /**
     * Show a cell's output.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.expand_output = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.expand_output();
            this.set_dirty(true);
        }
    };

    /**
     * Expand each code cell's output area, and remove scrollbars.
     */
    Notebook.prototype.expand_all_output = function () {
        this.get_cells().map(function (cell) {
            if (cell instanceof codecell.CodeCell) {
                cell.expand_output();
            }
        });
        // this should not be set if the `collapse` key is removed from nbformat
        this.set_dirty(true);
    };

    /**
     * Clear a code cell's output area.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.clear_output = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.clear_output();
            this.set_dirty(true);
        }
    };

    /**
     * Clear multiple selected code cells' output areas.
     *
     */
    Notebook.prototype.clear_cells_outputs = function(indices) {
        if (!indices) {
           indices = this.get_selected_cells_indices();
        }

        for (var i = 0; i < indices.length; i++){
            this.clear_output(indices[i]);
        }
    };

    /**
     * Clear each code cell's output area.
     */
    Notebook.prototype.clear_all_output = function () {
        this.get_cells().map(function (cell) {
            if (cell instanceof codecell.CodeCell) {
                cell.clear_output();
            }
        });
        this.set_dirty(true);
    };

    /**
     * Scroll the selected CodeCell's output area.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.scroll_output = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.scroll_output();
            this.set_dirty(true);
        }
    };

    /**
     * Expand each code cell's output area and add a scrollbar for long output.
     */
    Notebook.prototype.scroll_all_output = function () {
        this.get_cells().map(function (cell, i) {
            if (cell instanceof codecell.CodeCell) {
                cell.scroll_output();
            }
        });
        // this should not be set if the `collapse` key is removed from nbformat
        this.set_dirty(true);
    };

    /** 
     * Toggle whether a cell's output is collapsed or expanded.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.toggle_output = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.toggle_output();
            this.set_dirty(true);
        }
    };

    /**
     * Toggle whether all selected cells' outputs are collapsed or expanded.
     *
     * @param {integer} indices - the indices of the cells to toggle
     */
    Notebook.prototype.toggle_cells_outputs = function(indices) {
        if (!indices) {
            indices = this.get_selected_cells_indices();
        }

        for (var i = 0; i < indices.length; i++){
            this.toggle_output(indices[i]);
        }
    };

    /**
     * Toggle the output of all cells.
     */
    Notebook.prototype.toggle_all_output = function () {
        this.get_cells().map(function (cell) {
            if (cell instanceof codecell.CodeCell) {
                cell.toggle_output();
            }
        });
        // this should not be set if the `collapse` key is removed from nbformat
        this.set_dirty(true);
    };

    /**
     * Toggle a scrollbar for long cell outputs.
     * 
     * @param {integer} index - cell index
     */
    Notebook.prototype.toggle_output_scroll = function (index) {
        var i = this.index_or_selected(index);
        var cell = this.get_cell(i);
        if (cell !== null && (cell instanceof codecell.CodeCell)) {
            cell.toggle_output_scroll();
            this.set_dirty(true);
        }
    };

    /**
     * Toggle a scrollbar for selected long cells' outputs.
     *
     * @param {integer} indices - the indices of the cells to toggle
     */
    Notebook.prototype.toggle_cells_outputs_scroll = function(indices) {
        if (!indices) {
            indices = this.get_selected_cells_indices();
        }

        for (var i = 0; i < indices.length; i++){
            this.toggle_output_scroll(indices[i]);
        }
    };

    /**
     * Toggle the scrolling of long output on all cells.
     */
    Notebook.prototype.toggle_all_output_scroll = function () {
        this.get_cells().map(function (cell) {
            if (cell instanceof codecell.CodeCell) {
                cell.toggle_output_scroll();
            }
        });
        // this should not be set if the `collapse` key is removed from nbformat
        this.set_dirty(true);
    };

    // Other cell functions: line numbers, ...

    /**
     * Toggle line numbers in the selected cell's input area.
     */
    Notebook.prototype.cell_toggle_line_numbers = function() {
        this.get_selected_cells().map(function(cell){cell.toggle_line_numbers();});
    };


    //dispatch codemirror mode to all cells.
    Notebook.prototype._dispatch_mode = function(spec, newmode){
        this.codemirror_mode = newmode;
        codecell.CodeCell.options_default.cm_config.mode = newmode;
        this.get_cells().map(function(cell) {
            if (cell.cell_type === 'code'){
                cell.code_mirror.setOption('mode', spec);
                // This is currently redundant, because cm_config ends up as
                // codemirror's own .options object, but I don't want to
                // rely on that.
                cell._options.cm_config.mode = spec;
            }
        });

    };

    // roughly try to check mode equality
    var _mode_equal = function(mode1, mode2){
        return ((mode1||{}).name||mode1)===((mode2||{}).name||mode2);
    };
    
    /**
     * Set the codemirror mode for all code cells, including the default for
     * new code cells.
     * Set the mode to 'null' (no highlighting) if it can't be found.
     */
    Notebook.prototype.set_codemirror_mode = function(newmode){
        // if mode is the same don't reset,
        // to avoid n-time re-highlighting.
        if (_mode_equal(newmode, this.codemirror_mode)) {
            return;
        }
        
        var that = this;
        utils.requireCodeMirrorMode(newmode, function (spec) {
            that._dispatch_mode(spec, newmode);
        }, function(){
            // on error don't dispatch the new mode as re-setting it later will not work.
            // don't either set to null mode if it has been changed in the meantime
            if( _mode_equal(newmode, that.codemirror_mode) ){
                that._dispatch_mode('null','null');
            }
        });
    };

    // Session related things

    /**
     * Start a new session and set it on each code cell.
     */
    Notebook.prototype.start_session = function (kernel_name) {
        if (this._session_starting) {
            throw new session.SessionAlreadyStarting();
        }
        this._session_starting = true;

        var options = {
            base_url: this.base_url,
            ws_url: this.ws_url,
            notebook_path: this.notebook_path,
            notebook_name: this.notebook_name,
            kernel_name: kernel_name,
            notebook: this
        };

        var success = $.proxy(this._session_started, this);
        var failure = $.proxy(this._session_start_failed, this);

        if (this.session && this.session.kernel) {
            this.session.restart(options, success, failure);
        } else {
            this.session = new session.Session(options);
            this.session.start(success, failure);
        }
    };


    /**
     * Once a session is started, link the code cells to the kernel and pass the 
     * comm manager to the widget manager.
     */
    Notebook.prototype._session_started = function (){
        this._session_starting = false;
        this.kernel = this.session.kernel;
        var ncells = this.ncells();
        for (var i=0; i<ncells; i++) {
            var cell = this.get_cell(i);
            if (cell instanceof codecell.CodeCell) {
                cell.set_kernel(this.session.kernel);
            }
        }
    };

    /**
     * Called when the session fails to start.
     */
    Notebook.prototype._session_start_failed = function(jqxhr, status, error){
        this._session_starting = false;
        utils.log_ajax_error(jqxhr, status, error);
    };
    
    /**
     * Prompt the user to restart the kernel and re-run everything.
     * if options.confirm === false, no confirmation dialog is shown.
     */
    Notebook.prototype.restart_run_all = function (options) {
        var that = this;
        var restart_options = {};
        restart_options.confirm = (options || {}).confirm;
        restart_options.dialog = {
            notebook: that,
            keyboard_manager: that.keyboard_manager,
            title : i18n.msg._("Restart kernel and re-run the whole notebook?"),
            body : $("<p/>").text(
                i18n.msg._('Are you sure you want to restart the current kernel and re-execute the whole notebook?  All variables and outputs will be lost.')
            ),
            buttons : {
                "Restart and Run All Cells" : {
                    "class" : "btn-danger",
                    "click" : function () {
                        that.execute_all_cells();
                    },
                },
            }
        };
        return this._restart_kernel(restart_options);
    };

    /**
     * Prompt the user to restart the kernel and clear output.
     * if options.confirm === false, no confirmation dialog is shown.
     */
    Notebook.prototype.restart_clear_output = function (options) {
        var that = this;
        var restart_options = {};
        restart_options.confirm = (options || {}).confirm;
        restart_options.dialog = {
            notebook: that,
            keyboard_manager: that.keyboard_manager,
            title : i18n.msg._("Restart kernel and clear all output?"),
            body : $("<p/>").text(
                i18n.msg._('Do you want to restart the current kernel and clear all output?  All variables and outputs will be lost.')
            ),
            buttons : {
                "Restart and Clear All Outputs" : {
                    "class" : "btn-danger",
                    "click" : function (){
                        that.clear_all_output();
                    },
                },
            }
        };
        return this._restart_kernel(restart_options);
    };

    /**
     * Prompt the user to restart the kernel.
     * if options.confirm === false, no confirmation dialog is shown.
     */
    Notebook.prototype.shutdown_kernel = function (options) {
        var that = this;
        var shutdown_options = {};
        shutdown_options.confirm = (options || {}).confirm;
        shutdown_options.dialog = {
            title : "Shutdown kernel?",
            body : $("<p/>").text(
                i18n.msg._('Do you want to shutdown the current kernel?  All variables will be lost.')
            ),
            buttons : {
                "Shutdown" : {
                    "class" : "btn-danger",
                    "click" : function () {},
                },
            }
        };
        shutdown_options.kernel_action = function() {
            that.session.delete();
        };
        return this._restart_kernel(shutdown_options);
    };

    Notebook.prototype.restart_kernel = function (options) {
        var restart_options = {};
        restart_options.confirm = (options || {}).confirm;
        restart_options.dialog = {
            title : i18n.msg._("Restart kernel?"),
            body : $("<p/>").text(
                i18n.msg._('Do you want to restart the current kernel?  All variables will be lost.')
            ),
            buttons : {
                "Restart" : {
                    "class" : "btn-danger",
                    "click" : function () {},
                },
            }
        };
        return this._restart_kernel(restart_options);
    };
    
    // inner implementation of restart dialog & promise
    Notebook.prototype._restart_kernel = function (options) {
        var that = this;
        options = options || {};
        var resolve_promise, reject_promise;
        var promise = new Promise(function (resolve, reject){
            resolve_promise = resolve;
            reject_promise = reject;
        });
        
        function restart_and_resolve () {
            that.kernel.restart(function () {
                // resolve when the kernel is *ready* not just started
                that.events.one('kernel_ready.Kernel', resolve_promise);
            }, reject_promise);
        }

        var do_kernel_action = options.kernel_action || restart_and_resolve;
       
        // no need to confirm if the kernel is not connected
        if (options.confirm === false || !that.kernel.is_connected()) {
            var default_button = options.dialog.buttons[Object.keys(options.dialog.buttons)[0]];
            promise.then(default_button.click);
            do_kernel_action();
            return promise;
        }
        options.dialog.notebook = this;
        options.dialog.keyboard_manager = this.keyboard_manager;
        // add 'Continue running' cancel button
        var buttons = {
            "Continue Running": {},
        };
        // hook up button.click actions after restart promise resolves
        Object.keys(options.dialog.buttons).map(function (key) {
            var button = buttons[key] = options.dialog.buttons[key];
            var click = button.click;
            button.click = function () {
                promise.then(click);
                do_kernel_action();
            };
        });
        options.dialog.buttons = buttons;
        dialog.modal(options.dialog);
        return promise;
    };

    /**
     * 
     * Halt the kernel and close the notebook window
     */
    Notebook.prototype.close_and_halt = function () {
        var close_window = function () {
            /**
             * allow closing of new tabs in Chromium, impossible in FF
             */
                window.open('', '_self', '');
                window.close();
        };
            // finish with close on success or failure
            this.session.delete(close_window, close_window);
    };
    
    /**
     * Execute cells corresponding to the given indices.
     *
     * @param {Array} indices - indices of the cells to execute
     */
    Notebook.prototype.execute_cells = function (indices) {
        if (indices.length === 0) {
            return;
        }

        var cell;
        for (var i = 0; i < indices.length; i++) {
            cell = this.get_cell(indices[i]);
            cell.execute();
        }

        this.select(indices[indices.length - 1]);
        this.command_mode();
        this.set_dirty(true);
    };

    /**
     * Execute or render cell outputs and go into command mode.
     */
    Notebook.prototype.execute_selected_cells = function () {
        this.execute_cells(this.get_selected_cells_indices());
    };

    
    /**
     * Alias for execute_selected_cells, for backwards compatibility --
     * previously, doing "Run Cell" would only ever run a single cell (hence
     * `execute_cell`), but now it runs all marked cells, so that's the
     * preferable function to use. But it is good to keep this function to avoid
     * breaking existing extensions, etc.
     */
    Notebook.prototype.execute_cell = function () {
        this.execute_selected_cells();
    };

    /**
     * Execute or render cell outputs and insert a new cell below.
     */
    Notebook.prototype.execute_cell_and_insert_below = function () {
        var indices = this.get_selected_cells_indices();
        var cell_index;
        if (indices.length > 1) {
            this.execute_cells(indices);
            cell_index = Math.max.apply(Math, indices);
        } else {
            var cell = this.get_selected_cell();
            cell_index = this.find_cell_index(cell);
            cell.execute();
        }

        // If we are at the end always insert a new cell and return
        if (cell_index === (this.ncells()-1)) {
            this.command_mode();
            this.insert_cell_below();
            this.select(cell_index+1);
            this.edit_mode();
            this.scroll_to_bottom();
            this.set_dirty(true);
            return;
        }

        this.command_mode();
        this.insert_cell_below();
        this.select(cell_index+1);
        this.edit_mode();
        this.set_dirty(true);
    };

    /**
     * Execute or render cell outputs and select the next cell.
     */
    Notebook.prototype.execute_cell_and_select_below = function () {
        var indices = this.get_selected_cells_indices();
        var cell_index;
        if (indices.length > 1) {
            this.execute_cells(indices);
            cell_index = Math.max.apply(Math, indices);
        } else {
            var cell = this.get_selected_cell();
            cell_index = this.find_cell_index(cell);
            cell.execute();
        }

        // If we are at the end always insert a new cell and return
        if (cell_index === (this.ncells()-1)) {
            this.command_mode();
            this.insert_cell_below();
            this.select(cell_index+1);
            this.edit_mode();
            this.scroll_to_bottom();
            this.set_dirty(true);
            return;
        }

        this.command_mode();
        this.select(cell_index+1);
        this.focus_cell();
        this.set_dirty(true);
    };

    /**
     * Execute all cells below the selected cell.
     */
    Notebook.prototype.execute_cells_below = function () {
        this.execute_cell_range(this.get_selected_index(), this.ncells());
        this.scroll_to_bottom();
    };

    /**
     * Execute all cells above the selected cell.
     */
    Notebook.prototype.execute_cells_above = function () {
        this.execute_cell_range(0, this.get_selected_index());
    };

    /**
     * Execute all cells.
     */
    Notebook.prototype.execute_all_cells = function () {
        this.execute_cell_range(0, this.ncells());
        this.scroll_to_bottom();
    };

    /**
     * Execute a contiguous range of cells.
     * 
     * @param {integer} start - index of the first cell to execute (inclusive)
     * @param {integer} end - index of the last cell to execute (exclusive)
     */
    Notebook.prototype.execute_cell_range = function (start, end) {
        this.command_mode();
        var indices = [];
        for (var i=start; i<end; i++) {
            indices.push(i);
        }
        this.execute_cells(indices);
    };

    // Persistance and loading

    /**
     * Getter method for this notebook's name.
     * 
     * @return {string} This notebook's name (excluding file extension)
     */
    Notebook.prototype.get_notebook_name = function () {
        return utils.splitext(this.notebook_name)[0];
    };

    /**
     * Setter method for this notebook's name.
     *
     * @param {string} name
     */
    Notebook.prototype.set_notebook_name = function (name) {
        var parent = utils.url_path_split(this.notebook_path)[0];
        this.notebook_name = name;
        this.notebook_path = utils.url_path_join(parent, name);
    };

    /**
     * Check that a notebook's name is valid.
     * 
     * @param {string} nbname - A name for this notebook
     * @return {boolean} True if the name is valid, false if invalid
     */
    Notebook.prototype.test_notebook_name = function (nbname) {
        nbname = nbname || '';
        return nbname.length > 0 && !this.notebook_name_blacklist_re.test(nbname);
    };

    /**
     Move the unused attachments garbage collection logic to TextCell.toJSON.
     * Load a notebook from JSON (.ipynb).
     *
     * @param {object} data - JSON representation of a notebook
     */
    Notebook.prototype.fromJSON = function (data) {

        var content = data.content;
        var ncells = this.ncells();
        var i;
        for (i=0; i<ncells; i++) {
            // Always delete cell 0 as they get renumbered as they are deleted.
            this._unsafe_delete_cell(0);
        }
        // Save the metadata and name.
        this.metadata = content.metadata;
        this.notebook_name = data.name;
        this.notebook_path = data.path;
        var trusted = true;
        
        // Set the codemirror mode from language_info metadata
        if (this.metadata.language_info !== undefined) {
            var langinfo = this.metadata.language_info;
            // Mode 'null' should be plain, unhighlighted text.
            var cm_mode = langinfo.codemirror_mode || langinfo.name || 'null';
            this.set_codemirror_mode(cm_mode);
        }
        
        var new_cells = content.cells;
        ncells = new_cells.length;
        var cell_data = null;
        var new_cell = null;
        for (i=0; i<ncells; i++) {
            cell_data = new_cells[i];
            new_cell = this.insert_cell_at_index(cell_data.cell_type, i);
            new_cell.fromJSON(cell_data);
            if (new_cell.cell_type === 'code' && !new_cell.output_area.trusted) {
                trusted = false;
            }
        }
        if (trusted !== this.trusted) {
            this.trusted = trusted;
            this.events.trigger("trust_changed.Notebook", trusted);
        }

        this.apply_directionality();

    };

    /**
     * Dump this notebook into a JSON-friendly object.
     * 
     * @return {object} A JSON-friendly representation of this notebook.
     */
    Notebook.prototype.toJSON = function () {
        // remove the conversion indicator, which only belongs in-memory
        delete this.metadata.orig_nbformat;
        delete this.metadata.orig_nbformat_minor;

        var cells = this.get_cells();
        var ncells = cells.length;
        var cell_array = new Array(ncells);
        var trusted = true;
        for (var i=0; i<ncells; i++) {
            var cell = cells[i];
            if (cell.cell_type === 'code' && !cell.output_area.trusted) {
                trusted = false;
            }
            cell_array[i] = cell.toJSON(true);
        }
        var data = {
            cells: cell_array,
            metadata: this.metadata,
            nbformat: this.nbformat,
            nbformat_minor: this.nbformat_minor
        };
        if (trusted !== this.trusted) {
            this.trusted = trusted;
            this.events.trigger("trust_changed.Notebook", trusted);
        }
        return data;
    };

    /**
     * Start an autosave timer which periodically saves the notebook.
     * 
     * @param {integer} interval - the autosave interval in milliseconds
     */
    Notebook.prototype.set_autosave_interval = function (interval) {
        var that = this;
        // clear previous interval, so we don't get simultaneous timers
        if (this.autosave_timer) {
            clearInterval(this.autosave_timer);
        }
        if (!this.writable) {
            // disable autosave if not writable
            interval = 0;
        }
        
        this.autosave_interval = this.minimum_autosave_interval = interval;
        if (interval) {
            this.autosave_timer = setInterval(function() {
                if (that.dirty) {
                    that.save_notebook();
                }
            }, interval);
            this.events.trigger("autosave_enabled.Notebook", interval);
        } else {
            this.autosave_timer = null;
            this.events.trigger("autosave_disabled.Notebook");
        }
    };
    
    /**
     * Save this notebook on the server. This becomes a notebook instance's
     * .save_notebook method *after* the entire notebook has been loaded.
     *
     */
    Notebook.prototype.save_notebook = function (check_last_modified) {
        if (check_last_modified === undefined) {
            check_last_modified = true;
        }

        var error;
        if (!this._fully_loaded) {
            error = new Error("Load failed, save is disabled");
            this.events.trigger('notebook_save_failed.Notebook', error);
            return Promise.reject(error);
        } else if (!this.writable) {
            error = new Error("Notebook is read-only");
            this.events.trigger('notebook_save_failed.Notebook', error);
            return Promise.reject(error);
        }

        // Trigger an event before save, which allows listeners to modify
        // the notebook as needed.
        this.events.trigger('before_save.Notebook');

        // Create a JSON model to be sent to the server.
        var model = {
            type : "notebook",
            content : this.toJSON()
        };
        // time the ajax call for autosave tuning purposes.
        var start =  new Date().getTime();

        var that = this;
        var _save = function () {
            return that.contents.save(that.notebook_path, model).then(
                $.proxy(that.save_notebook_success, that, start),
                function (error) {
                    that.events.trigger('notebook_save_failed.Notebook', error);
                    // This hasn't handled the error, so propagate it up
                    return Promise.reject(error);
                }
            );
        };

        if (check_last_modified) {
            return this.contents.get(this.notebook_path, {content: false}).then(
                function (data) {
                    var last_modified = new Date(data.last_modified);
                    var last_modified_check_margin = (that.config.data['last_modified_check_margin'] || 0.5) * 1000; // 500 ms
                    // We want to check last_modified (disk) > that.last_modified (our last save)
                    // In some cases the filesystem reports an inconsistent time,
                    // so we allow 0.5 seconds difference before complaining.
                    // This is configurable in nbconfig/notebook.json as `last_modified_check_margin`.
                    if ((last_modified.getTime() - that.last_modified.getTime()) > last_modified_check_margin) {  
                        console.warn("Last saving was done on `"+that.last_modified+"`("+that._last_modified+"), "+
                                    "while the current file seem to have been saved on `"+data.last_modified+"`");
                        if (that._changed_on_disk_dialog !== null) {
                            // update save callback on the confirmation button
                            that._changed_on_disk_dialog.find('.save-confirm-btn').click(_save);
                            //Rebind Click Event on Reload
                            that._changed_on_disk_dialog.find('.btn-warning').click(function () {window.location.reload()});
                            // redisplay existing dialog
                            that._changed_on_disk_dialog.modal('show');
                        } else {
                          // create new dialog
                          that._changed_on_disk_dialog = dialog.modal({
                            notebook: that,
                            keyboard_manager: that.keyboard_manager,
                            title: i18n.msg._("Notebook changed"),
                            body: i18n.msg._("The notebook file has changed on disk since the last time we opened or saved it. "
                                  + "Do you want to overwrite the file on disk with the version open here, or load "
                                  + "the version on disk (reload the page)?"),
                            buttons: {
                                Reload: {
                                    class: 'btn-warning',
                                    click: function() {
                                        window.location.reload();
                                    }
                                },
                                Cancel: {},
                                Overwrite: {
                                    class: 'btn-danger save-confirm-btn',
                                    click: function () {
                                        _save();
                                    }
                                },
                            }
                          });
                        }
                    } else {
                        return _save();
                    }
                }, function () {
                    // maybe it has been deleted or renamed? Go ahead and save.
                    return _save();
                }
            );
        } else {
            return _save();
        }
    };
    
    /**
     * Success callback for saving a notebook.
     * 
     * @param {integer} start - Time when the save request start
     * @param {object}  data - JSON representation of a notebook
     */
    Notebook.prototype.save_notebook_success = function (start, data) {
        this.set_dirty(false);
        this.last_modified = new Date(data.last_modified);
        // debug 484
        this._last_modified = 'save-success:'+data.last_modified;
        if (data.message) {
            // save succeeded, but validation failed.
            var body = $("<div>");
            var title = i18n.msg._("Notebook validation failed");

            body.append($("<p>").text(
                i18n.msg._("The save operation succeeded," +
                " but the notebook does not appear to be valid." +
                " The validation error was:")
            )).append($("<div>").addClass("validation-error").append(
                $("<pre>").text(data.message)
            ));
            dialog.modal({
                notebook: this,
                keyboard_manager: this.keyboard_manager,
                title: title,
                body: body,
                buttons : {
                    OK : {
                        "class" : "btn-primary"
                    }
                }
            });
        }
        this.events.trigger('notebook_saved.Notebook');
        this._update_autosave_interval(start);
        if (this._checkpoint_after_save) {
            this.create_checkpoint();
            this._checkpoint_after_save = false;
        }
        return data;
    };

    Notebook.prototype.save_notebook_as = function() {
        var that = this;
        var current_dir = $('body').attr('data-notebook-path').split('/').slice(0, -1).join("/");
        current_dir = current_dir? current_dir + "/": "";
        current_dir = decodeURIComponent(current_dir);
        var dialog_body = $('<div/>').append(
            $('<p/>').addClass('save-message')
                .text(i18n.msg._('Enter a notebook path relative to notebook dir'))
        ).append(
            $('<br/>')
        ).append(
            $('<input/>').attr('type','text').attr('size','25')
            .attr('data-testid', 'save-as')
            .addClass('form-control')
        );

        var d = dialog.modal({
            title: 'Save As',
            body: dialog_body,
            keyboard_manager: this.keyboard_manager,
            notebook: this,
            buttons: {
                Cancel: {},
                Save: {
                    class: 'btn-primary',
                    click: function() {
                        var nb_path = d.find('input').val();
                        var nb_name = nb_path.split('/').slice(-1).pop();
                        if (!nb_name) {
                            $(".save-message").html(
                                    $("<span>")
                                        .attr("style", "color:red;")
                                        .text($(".save-message").text())
                                );
                            return false;
                        }
                        // If notebook name does not contain extension '.ipynb' add it
                        var ext = utils.splitext(nb_name)[1];
                        if (ext === '') {
                            nb_name = nb_name + '.ipynb';
                            nb_path = nb_path + '.ipynb';
                        }
                        var save_thunk = function() {
                            var model = {
                                'type': 'notebook',
                                'content': that.toJSON(),
                                'name': nb_name
                            };
                            var start = new Date().getTime();
                            return that.contents.save(nb_path, model)
                                .then(function(data) {
                                    d.modal('hide');
                                    that.writable = true;
                                    that.notebook_name = data.name;
                                    that.notebook_path = data.path;
                                    that.session.rename_notebook(data.path);
                                    that.events.trigger('notebook_renamed.Notebook', data);
                                    that.save_notebook_success(start, data);
                                }, function(error) {
                                    var msg = i18n.msg._(error.message || 'Unknown error saving notebook');
                                    $(".save-message").html(
                                        $("<span>")
                                            .attr("style", "color:red;")
                                            .text(msg)
                                    );
                                });
                        };
                        that.contents.get(nb_path, {type: 'notebook', content: false}).then(function(data) {
                            var warning_body = $('<div/>').append(
                                $("<p/>").text(i18n.msg._('Notebook with that name exists.')));
                            dialog.modal({
                                title: 'Save As',
                                body: warning_body,
                                buttons: {Cancel: {},
                                Overwrite: {
                                    class: 'btn-warning',
                                    click: function() {
                                        return save_thunk();
                                    }
                                }
                            }
                            });
                        }, function(err) {
                            return save_thunk();
                        });
                        return false;
                    }
                },
            },
            open : function () {
                d.find('input[type="text"]').keydown(function (event) {
                    if (event.which === keyboard.keycodes.enter) {
                        d.find('.btn-primary').first().click();
                        return false;
                    }
                });
                d.find('input[type="text"]').val(current_dir).focus();
             }
         });
    };

    /**
     * Update the autosave interval based on the duration of the last save.
     * 
     * @param {integer} start - when the save request started
     */
    Notebook.prototype._update_autosave_interval = function (start) {
        var duration = (new Date().getTime() - start);
        if (this.autosave_interval) {
            // new save interval: higher of 10x save duration or parameter (default 30 seconds)
            var interval = Math.max(10 * duration, this.minimum_autosave_interval);
            // ceil to 10 seconds, otherwise we will be setting a new interval too often
            // do not round or anything below 5000ms will desactivate saving.
            interval = 10000 * Math.ceil(interval / 10000);
            // set new interval, if it's changed
            if (interval !== this.autosave_interval) {
                this.set_autosave_interval(interval);
            }
        }
    };

    /**
     * Explicitly trust the output of this notebook.
     */
    Notebook.prototype.trust_notebook = function (from_notification) {
        var body = $("<div>").append($("<p>")
            .text(i18n.msg._("A trusted Jupyter notebook may execute hidden malicious code when you open it. " +
                    "Selecting trust will immediately reload this notebook in a trusted state. " +
                    "For more information, see the Jupyter security documentation: "))
            .append($("<a>").attr("href", "https://jupyter-notebook.readthedocs.io/en/stable/security.html")
                .text(i18n.msg._("here"))
            )
        );

        var nb = this;
        dialog.modal({
            notebook: this,
            keyboard_manager: this.keyboard_manager,
            title: i18n.msg._("Trust this notebook?"),
            body: body,
            focus_button: from_notification,

            buttons: {
                Cancel : {},
                Trust : {
                    class : "btn-danger",
                    click : function () {
                        var cells = nb.get_cells();
                        for (var i = 0; i < cells.length; i++) {
                            var cell = cells[i];
                            if (cell.cell_type === 'code') {
                                cell.output_area.trusted = true;
                            }
                        }
                        // If its write only and dirty, save before 
                        // trusting
                        var pr;
                        if(nb.writable && nb.dirty) {
                            pr = nb.save_notebook();
                        }
                        else {
                            pr = Promise.resolve();
                        }
                        return pr.then(function() {                            
                            nb.contents.trust(nb.notebook_path)
                            .then(function() {
                                nb.events.trigger("trust_changed.Notebook", true);
                                window.location.reload();
                            }, function(err) {
                                console.log(err);
                            });
                        });
                    }
                }
            }
        });
    };

    /**
     * Make a copy of the current notebook.
     * If the notebook has unsaved changes, it is saved first.
     */
    Notebook.prototype.copy_notebook = function () {
        var that = this;
        var base_url = this.base_url;
        var w = window.open('', IPython._target);
        var parent = utils.url_path_split(this.notebook_path)[0];
        var p;
        if (this.dirty && this.writable) {
            p = this.save_notebook(true);
        } else {
            p = Promise.resolve();
        }
        return p.then(function () {
            return that.contents.copy(that.notebook_path, parent).then(
                function (data) {
                    w.location = utils.url_path_join(
                        base_url, 'notebooks', utils.encode_uri_components(data.path)
                    );
                },
                function(error) {
                    w.close();
                    that.events.trigger('notebook_copy_failed', error);
                }
            );
        });
    };
    
    /**
     * Ensure a filename has the right extension
     * Returns the filename with the appropriate extension, appending if necessary.
     */
    Notebook.prototype.ensure_extension = function (name) {
        var ext = utils.splitext(this.notebook_path)[1];
        if (ext.length && name.slice(-ext.length) !== ext) {
            name = name + ext;
        }
        return name;
    };

    /**
     * Rename the notebook.
     * @param  {string} new_name
     * @return {Promise} promise that resolves when the notebook is renamed.
     */
    Notebook.prototype.rename = function (new_name) {
        new_name = this.ensure_extension(new_name);

        var that = this;
        var parent = utils.url_path_split(this.notebook_path)[0];
        var new_path = utils.url_path_join(parent, new_name);
        return this.contents.rename(this.notebook_path, new_path).then(
            function (json) {
                that.notebook_name = json.name;
                that.notebook_path = json.path;
                that.last_modified = new Date(json.last_modified);
                // debug 484
                that._last_modified = json.last_modified;
                that.session.rename_notebook(json.path);
                that.events.trigger('notebook_renamed.Notebook', json);
            }
        );
    };

    /**
     * Delete this notebook
     */
    Notebook.prototype.delete = function () {
        this.contents.delete(this.notebook_path);
    };

    /**
     * Request a notebook's data from the server.
     * 
     * @param {string} notebook_path - A notebook to load
     */
    Notebook.prototype.load_notebook = function (notebook_path) {
        this.notebook_path = notebook_path;
        this.notebook_name = utils.url_path_split(this.notebook_path)[1];
        this.events.trigger('notebook_loading.Notebook');
        this.contents.get(notebook_path, {type: 'notebook'}).then(
            $.proxy(this.load_notebook_success, this),
            $.proxy(this.load_notebook_error, this)
        );
    };

    /**
     * Success callback for loading a notebook from the server.
     * 
     * Load notebook data from the JSON response.
     * 
     * @param {object} data JSON representation of a notebook
     */
    Notebook.prototype.load_notebook_success = function (data) {
        var failed, msg;
        try {
            this.fromJSON(data);
        } catch (e) {
            failed = e;
            console.error("Notebook failed to load from JSON:", e);
        }
        if (failed || data.message) {
            // *either* fromJSON failed or validation failed
            var body = $("<div>");
            var title;
            if (failed) {
                title = i18n.msg._("Notebook failed to load");
                body.append($("<p>").text(
                    i18n.msg._("The error was: ")
                )).append($("<div>").addClass("js-error").text(
                    failed.toString()
                )).append($("<p>").text(
                    i18n.msg._("See the error console for details.")
                ));
            } else {
                title = i18n.msg._("Notebook validation failed");
            }

            if (data.message) {
                if (failed) {
                    msg = i18n.msg._("The notebook also failed validation:");
                } else {
                    msg = i18n.msg._("An invalid notebook may not function properly." +
                    " The validation error was:");
                }
                body.append($("<p>").text(
                    msg
                )).append($("<div>").addClass("validation-error").append(
                    $("<pre>").text(data.message)
                ));
            }

            dialog.modal({
                notebook: this,
                keyboard_manager: this.keyboard_manager,
                title: title,
                body: body,
                buttons : {
                    OK : {
                        "class" : "btn-primary"
                    }
                }
            });
        }
        if (this.ncells() === 0) {
            this.insert_cell_below('code');
            this.edit_mode(0);
        } else {
            this.select(0);
            this.handle_command_mode(this.get_cell(0));
        }
        this.set_dirty(false);
        this.scroll_to_top();
        this.writable = data.writable || false;
        this.last_modified = new Date(data.last_modified);
        // debug 484
        this._last_modified = 'load-success:'+data.last_modified;
        var nbmodel = data.content;
        var orig_nbformat = nbmodel.metadata.orig_nbformat;
        var orig_nbformat_minor = nbmodel.metadata.orig_nbformat_minor;
        if (orig_nbformat !== undefined && nbmodel.nbformat !== orig_nbformat) {
            var oldmsg = i18n.msg._("This notebook has been converted from an older notebook format" +
            " to the current notebook format v(%s).");
            var newmsg = i18n.msg._("This notebook has been converted from a newer notebook format" +
            " to the current notebook format v(%s).");
            if (nbmodel.nbformat > orig_nbformat) {
                msg = i18n.msg.sprintf(oldmsg,nbmodel.nbformat);
            } else {
                msg = i18n.msg.sprintf(newmsg,nbmodel.nbformat);
            }
            msg += " ";
            msg += i18n.msg._("The next time you save this notebook, the " +
            "current notebook format will be used.");
            
            msg += " ";
            if (nbmodel.nbformat > orig_nbformat) {
                msg += i18n.msg._("Older versions of Jupyter may not be able to read the new format.");
            } else {
                msg += i18n.msg._("Some features of the original notebook may not be available.");
            }
            msg += " ";
            msg += i18n.msg._("To preserve the original version, close the " +
                "notebook without saving it.");
            dialog.modal({
                notebook: this,
                keyboard_manager: this.keyboard_manager,
                title : i18n.msg._("Notebook converted"),
                body : msg,
                buttons : {
                    OK : {
                        class : "btn-primary"
                    }
                }
            });
        } else if (this.nbformat_minor < nbmodel.nbformat_minor) {
            this.nbformat_minor = nbmodel.nbformat_minor;
        }

        if (this.session === null) {
            var kernel_name = utils.get_url_param('kernel_name');
            if (kernel_name) {
                this.kernel_selector.set_kernel(kernel_name);
            } else if (this.metadata.kernelspec) {
                this.kernel_selector.set_kernel(this.metadata.kernelspec);
            } else if (this.metadata.language) {
                // compat with IJulia, IHaskell, and other early kernels
                // adopters that where setting a language metadata.
                this.kernel_selector.set_kernel({
                    name: i18n.msg._("(No name)"),
                    language: this.metadata.language
                  });
                // this should be stored in kspec now, delete it.
                // remove once we do not support notebook v3 anymore.
                delete this.metadata.language;
            } else {
                // setting kernel via set_kernel above triggers start_session,
                // otherwise start a new session with the server's default kernel
                // spec_changed events will fire after kernel is loaded
                this.start_session();
            }
        }
        // load our checkpoint list
        this.list_checkpoints();
        
        // load toolbar state
        if (this.metadata.celltoolbar) {
            celltoolbar.CellToolbar.global_show();
            celltoolbar.CellToolbar.activate_preset(this.metadata.celltoolbar);
        } else {
            celltoolbar.CellToolbar.global_hide();
        }
        
        if (!this.writable) {
            this.set_autosave_interval(0);
            this.events.trigger('notebook_read_only.Notebook');
        }
        
        // now that we're fully loaded, it is safe to restore save functionality
        this._fully_loaded = true;
        this.events.trigger('notebook_loaded.Notebook');
    };

    Notebook.prototype.set_kernelselector = function(k_selector){
        this.kernel_selector = k_selector;
    };

    /**
     * Failure callback for loading a notebook from the server.
     * 
     * @param {Error} error
     */
    Notebook.prototype.load_notebook_error = function (error) {
        var isSanitized = true;
        this.events.trigger('notebook_load_failed.Notebook', error);
        var msg;
        if (error.name === utils.XHR_ERROR && error.xhr.status === 500) {
            utils.log_ajax_error(error.xhr, error.xhr_status, error.xhr_error);
            msg = i18n.msg.sprintf(i18n.msg._("An unknown error occurred while loading this notebook. " +
            "This version can load notebook formats %s or earlier. See the server log for details.",
            "v" + this.nbformat));
        } else {
            msg = error.message;
            console.warn('Error stack trace while loading notebook was:');
            console.warn(error.stack);
        }
        if (navigator.cookieEnabled == false){
            msg = i18n.msg._("Jupyter requires cookies to work; please enable cookies" +
                " and refresh page. <a href=\"https://www.wikihow.com/Enable-Cookies-in-Your-Internet-Web-Browser\"> Learn more about enabling cookies. </a>");
            isSanitized = false;
        }
        dialog.modal({
            notebook: this,
            keyboard_manager: this.keyboard_manager,
            title: i18n.msg._("Error loading notebook"),
            body : msg,
            buttons : {
                "Close": {
                    class : 'btn-danger',
                    click : function () {
                        window.close();
                    }
                }
              },
              sanitize: isSanitized
          
        });
    };

    /*********************  checkpoint-related  ********************/
    
    /**
     * Save the notebook then immediately create a checkpoint.
     */
    Notebook.prototype.save_checkpoint = function () {
        this._checkpoint_after_save = true;
        return this.save_notebook(true);
    };
    
    /**
     * Add a checkpoint for this notebook.
     */
    Notebook.prototype.add_checkpoint = function (checkpoint) {
        var found = false;
        for (var i = 0; i < this.checkpoints.length; i++) {
            var existing = this.checkpoints[i];
            if (existing.id === checkpoint.id) {
                found = true;
                this.checkpoints[i] = checkpoint;
                break;
            }
        }
        if (!found) {
            this.checkpoints.push(checkpoint);
        }
        this.last_checkpoint = this.checkpoints[this.checkpoints.length - 1];
    };
    
    /**
     * List checkpoints for this notebook.
     */
    Notebook.prototype.list_checkpoints = function () {
        var that = this;
        this.contents.list_checkpoints(this.notebook_path).then(
            $.proxy(this.list_checkpoints_success, this),
            function(error) {
                that.events.trigger('list_checkpoints_failed.Notebook', error);
            }
        );
    };

    /**
     * Success callback for listing checkpoints.
     * 
     * @param {object} data - JSON representation of a checkpoint
     */
    Notebook.prototype.list_checkpoints_success = function (data) {
        this.checkpoints = data;
        if (data.length) {
            this.last_checkpoint = data[data.length - 1];
        } else {
            this.last_checkpoint = null;
        }
        this.events.trigger('checkpoints_listed.Notebook', [data]);
    };

    /**
     * Create a checkpoint of this notebook on the server from the most recent save.
     */
    Notebook.prototype.create_checkpoint = function () {
        var that = this;
        this.contents.create_checkpoint(this.notebook_path).then(
            $.proxy(this.create_checkpoint_success, this),
            function (error) {
                that.events.trigger('checkpoint_failed.Notebook', error);
            }
        );
    };

    /**
     * Success callback for creating a checkpoint.
     * 
     * @param {object} data - JSON representation of a checkpoint
     */
    Notebook.prototype.create_checkpoint_success = function (data) {
        this.add_checkpoint(data);
        this.events.trigger('checkpoint_created.Notebook', data);
    };

    /**
     * Display the restore checkpoint dialog
     * @param  {string} checkpoint ID
     */
    Notebook.prototype.restore_checkpoint_dialog = function (checkpoint) {
        var that = this;
        checkpoint = checkpoint || this.last_checkpoint;
        if ( ! checkpoint ) {
            console.log("restore dialog, but no checkpoint to restore to!");
            return;
        }
        var body = $('<div/>').append(
            $('<p/>').addClass("p-space").text(
                i18n.msg._("Are you sure you want to revert the notebook to " +
                "the latest checkpoint?")
            ).append(
                $("<strong/>").text(" "+i18n.msg._("This cannot be undone."))
            )
        ).append(
            $('<p/>').addClass("p-space").text(i18n.msg._("The checkpoint was last updated at:"))
        ).append(
            $('<p/>').addClass("p-space").text(
                moment(checkpoint.last_modified).format('LLLL') +
                ' ('+moment(checkpoint.last_modified).fromNow()+')'// Long form:  Tuesday, January 27, 2015 12:15 PM
            ).css("text-align", "center")
        );
        
        dialog.modal({
            notebook: this,
            keyboard_manager: this.keyboard_manager,
            title : i18n.msg._("Revert notebook to checkpoint"),
            body : body,
            default_button: "Cancel",
            buttons : {
                Cancel: {},
                Revert : {
                    class : "btn-danger",
                    click : function () {
                        that.restore_checkpoint(checkpoint.id);
                    }
                }
            }
        });
    };
    
    /**
     * Restore the notebook to a checkpoint state.
     * 
     * @param {string} checkpoint ID
     */
    Notebook.prototype.restore_checkpoint = function (checkpoint) {
        this.events.trigger('notebook_restoring.Notebook', checkpoint);
        var that = this;
        this.contents.restore_checkpoint(this.notebook_path, checkpoint).then(
            $.proxy(this.restore_checkpoint_success, this),
            function (error) {
                that.events.trigger('checkpoint_restore_failed.Notebook', error);
            }
        );
    };
    
    /**
     * Success callback for restoring a notebook to a checkpoint.
     */
    Notebook.prototype.restore_checkpoint_success = function () {
        this.events.trigger('checkpoint_restored.Notebook');
        this.load_notebook(this.notebook_path);
    };

    /**
     * Delete a notebook checkpoint.
     * 
     * @param {string} checkpoint ID
     */
    Notebook.prototype.delete_checkpoint = function (checkpoint) {
        this.events.trigger('notebook_restoring.Notebook', checkpoint);
        var that = this;
        this.contents.delete_checkpoint(this.notebook_path, checkpoint).then(
            $.proxy(this.delete_checkpoint_success, this),
            function (error) {
                that.events.trigger('checkpoint_delete_failed.Notebook', error);
            }
        );
    };
    
    /**
     * Success callback for deleting a notebook checkpoint.
     */
    Notebook.prototype.delete_checkpoint_success = function () {
        this.events.trigger('checkpoint_deleted.Notebook');
        this.load_notebook(this.notebook_path);
    };

    return {Notebook: Notebook};
});
