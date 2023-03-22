// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/dialog',
    'base/js/utils',
    'base/js/i18n',
    'notebook/js/quickhelp',
    './celltoolbar',
    './tour',
    'moment',
], function($, IPython, dialog, utils, i18n, quickhelp, celltoolbar, tour, moment) {
    "use strict";

    var MenuBar = function (selector, options) {
        /**
         * Constructor
         *
         * A MenuBar Class to generate the menubar of Jupyter notebook
         *
         * Parameters:
         *  selector: string
         *  options: dictionary
         *      Dictionary of keyword arguments.
         *          notebook: Notebook instance
         *          render keyboard shortcuts from KeyboardManager
         *          contents: ContentManager instance
         *          events: $(Events) instance
         *          save_widget: SaveWidget instance
         *          quick_help: QuickHelp instance
         *          base_url : string
         *          notebook_path : string
         *          notebook_name : string
         *          config: ConfigSection instance
         */
        options = options || {};
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url || utils.get_body_data("baseUrl");
        this.selector = selector;
        this.notebook = options.notebook;
        this.keyboard_manager = this.notebook.keyboard_manager;
        this.actions = this.keyboard_manager.actions;
        this.contents = options.contents;
        this.events = options.events;
        this.save_widget = options.save_widget;
        this.quick_help = options.quick_help;
        this.actions = options.actions;
        this.config = options.config;

        try {
            this.tour = new tour.Tour(this.notebook, this.events);
        } catch (e) {
            this.tour = undefined;
            console.log("Failed to instantiate Notebook Tour", e);
        }

        if (this.selector !== undefined) {
            this.element = $(selector);
            this.style();
            this.add_bundler_items();
            this.bind_events();
        }
    };

    // TODO: This has definitively nothing to do with style ...
    MenuBar.prototype.style = function () {
        var that = this;
        this.element.find("li").click(function (event, ui) {
                // The selected cell loses focus when the menu is entered, so we
                // re-select it upon selection.
                var i = that.notebook.get_selected_index();
                that.notebook.select(i, false);
            }
        );
    };
    
    MenuBar.prototype.add_bundler_items = function() {
        var that = this;
        this.config.loaded.then(function() {
            var bundlers = that.config.data.bundlerextensions;
            if(bundlers) {
                // Stable sort the keys to ensure menu items don't hop around
                var ids = Object.keys(bundlers).sort()
                ids.forEach(function(bundler_id) {
                    var bundler = bundlers[bundler_id];
                    var group = that.element.find('#'+bundler.group+'_menu')
                    
                    // Validate menu item metadata
                    if(!group.length) {
                        console.warn('unknown group', bundler.group, 'for bundler ID', bundler_id, '; skipping');
                        return;
                    } else if(!bundler.label) {
                        console.warn('no label for bundler ID', bundler_id, '; skipping');
                        return;
                    }
                    
                    // Insert menu item into correct group, click handler
                    group.parent().removeClass('hidden');
                    var $li = $('<li>')
                        .appendTo(group);
                    $('<a>')
                        .attr('href', '#')
                        .text(bundler.label)
                        .appendTo($li)
                        .on('click', that._bundle.bind(that, bundler_id))
                        .appendTo($li);
                });
            }
        });
    };

    MenuBar.prototype._new_window = function(url) {
        var w = window.open('', IPython._target);
        if (this.notebook.dirty && this.notebook.writable) {
            this.notebook.save_notebook().then(function() {
                w.location = url;
            });
        } else {
            w.location = url;
        }
    };
    
    MenuBar.prototype._bundle = function(bundler_id) {
        // Read notebook path and base url here in case they change
        var notebook_path = utils.encode_uri_components(this.notebook.notebook_path);
        var url = utils.url_path_join(
            this.base_url,
            'bundle',
            notebook_path
        ) + '?bundler=' + utils.encode_uri_components(bundler_id);

        this._new_window(url);
    };

    MenuBar.prototype._nbconvert = function (format, download) {
        download = download || false;
        var notebook_path = utils.encode_uri_components(this.notebook.notebook_path);
        var url = utils.url_path_join(
            this.base_url,
            'nbconvert',
            format,
            notebook_path
        ) + "?download=" + download.toString();
        
        this._new_window(url);
    };

    MenuBar.prototype._size_header = function() {
        /** 
         * Update header spacer size.
         */
        console.warn('`_size_header` is deprecated and will be removed in future versions.'+
                     ' Please trigger the `resize-header.Page` manually if you rely on it.');
        this.events.trigger('resize-header.Page');
    };

    (function($){
        $(document).ready(function(){
            $('ul.dropdown-menu [data-toggle=dropdown]').on('click', function(event) {
                event.preventDefault(); 
                event.stopPropagation(); 
                $(this).parent().siblings().removeClass('open');
                $(this).parent().toggleClass('open');
            });
        });
    })(jQuery);

    MenuBar.prototype.bind_events = function () {
        /**
         *  File
         */
        var that = this;
        

        this.element.find('#open_notebook').click(function () {
            var parent = utils.url_path_split(that.notebook.notebook_path)[0];
            window.open(
                utils.url_path_join(
                    that.base_url, that.nbclassic_path, 'tree',
                    utils.encode_uri_components(parent)
                ), IPython._target);
        });
        this.element.find('#copy_notebook').click(function () {
            that.notebook.copy_notebook();
            return false;
        });
        this.element.find('#save_notebook_as').click(function() {
            that.notebook.save_notebook_as();
            return false;
        });
        
        this.element.find('#print_preview').click(function () {
            that._nbconvert('html', false);
        });

        this.element.find('#download_menu li').click(function (ev) {
            that._nbconvert(ev.target.parentElement.getAttribute('id').substring(9), true);
        });

        this.events.on('trust_changed.Notebook', function (event, trusted) {
            if (trusted) {
                that.element.find('#trust_notebook')
                    .addClass("disabled").off('click')
                    .find("a").text(i18n.msg._("Trusted Notebook"));
            } else {
                that.element.find('#trust_notebook')
                    .removeClass("disabled").on('click', function () {
                        that.notebook.trust_notebook();
                    })
                    .find("a").text(i18n.msg._("Trust Notebook"));
            }
        });

        // View
        this._add_celltoolbar_list();

        // Edit
        this.element.find('#edit_nb_metadata').click(function () {
            that.notebook.edit_metadata({
                notebook: that.notebook,
                keyboard_manager: that.notebook.keyboard_manager});
        });

        var id_actions_dict = {
            '#trust_notebook' : 'trust-notebook',
            '#rename_notebook' : 'rename-notebook',
            '#find_and_replace' : 'find-and-replace',
            '#save_checkpoint': 'save-notebook',
            '#shutdown_kernel': 'confirm-shutdown-kernel',
            '#restart_kernel': 'confirm-restart-kernel',
            '#restart_clear_output': 'confirm-restart-kernel-and-clear-output',
            '#restart_run_all': 'confirm-restart-kernel-and-run-all-cells',
            '#close_and_halt': 'close-and-halt',
            '#int_kernel': 'interrupt-kernel',
            '#cut_cell': 'cut-cell',
            '#copy_cell': 'copy-cell',
            '#paste_cell_above': 'paste-cell-above',
            '#paste_cell_below': 'paste-cell-below',
            '#paste_cell_replace': 'paste-cell-replace',
            '#delete_cell': 'delete-cell',
            '#undelete_cell': 'undo-cell-deletion',
            '#split_cell': 'split-cell-at-cursor',
            '#merge_cell_above': 'merge-cell-with-previous-cell',
            '#merge_cell_below': 'merge-cell-with-next-cell',
            '#move_cell_up': 'move-cell-up',
            '#move_cell_down': 'move-cell-down',
            '#toggle_header': 'toggle-header',
            '#toggle_toolbar': 'toggle-toolbar',
            '#toggle_line_numbers': 'toggle-all-line-numbers',
            '#insert_cell_above': 'insert-cell-above',
            '#insert_cell_below': 'insert-cell-below',
            '#run_cell': 'run-cell',
            '#run_cell_select_below': 'run-cell-and-select-next',
            '#run_cell_insert_below': 'run-cell-and-insert-below',
            '#run_all_cells': 'run-all-cells',
            '#run_all_cells_above': 'run-all-cells-above',
            '#run_all_cells_below': 'run-all-cells-below',
            '#to_code': 'change-cell-to-code',
            '#to_markdown': 'change-cell-to-markdown',
            '#to_raw': 'change-cell-to-raw',
            '#toggle_current_output': 'toggle-cell-output-collapsed',
            '#toggle_current_output_scroll': 'toggle-cell-output-scrolled',
            '#clear_current_output': 'clear-cell-output',
            '#toggle_all_output': 'toggle-all-cells-output-collapsed',
            '#toggle_all_output_scroll': 'toggle-all-cells-output-scrolled',
            '#clear_all_output': 'clear-all-cells-output',
            '#cut_cell_attachments': 'cut-cell-attachments',
            '#copy_cell_attachments': 'copy-cell-attachments',
            '#paste_cell_attachments': 'paste-cell-attachments',
            '#insert_image': 'insert-image',
            '#keyboard_shortcuts' : 'show-keyboard-shortcuts',
            '#edit_keyboard_shortcuts' : 'edit-command-mode-keyboard-shortcuts',
        };

        for(var idx in id_actions_dict){
            if (!id_actions_dict.hasOwnProperty(idx)){
                continue;
            }
            var id_act = 'jupyter-notebook:'+id_actions_dict[idx];
            if(!that.actions.exists(id_act)){
                console.warn('actions', id_act, 'does not exist, still binding it in case it will be defined later...');
            }
            // Immediately-Invoked Function Expression cause JS.
            (function(that, id_act, idx){
                var el = that.element.find(idx);
                el.click(function(event){
                    that.actions.call(id_act, event);
                });
                
                var keybinding = that.keyboard_manager.command_shortcuts.get_action_shortcut(id_act) || that.keyboard_manager.edit_shortcuts.get_action_shortcut(id_act);
                
                if (keybinding) {
                    var shortcut = quickhelp.humanize_sequence(keybinding);
                    var link_element = el.children('a');
                    var text = link_element.text();
                    link_element.text('');
                    link_element.addClass('menu-shortcut-container');
                    link_element.append('<span class="action">' + text + '</span>');
                    link_element.append('<span class="kb">' + shortcut + '</span>');
                }
            })(that, id_act, idx);
        }

        
        // Kernel
        this.element.find('#reconnect_kernel').click(function () {
            that.notebook.kernel.reconnect();
        });
        // Help
        if (this.tour) {
            this.element.find('#notebook_tour').click(function () {
                that.tour.start();
            });
        } else {
            this.element.find('#notebook_tour').addClass("disabled");
        }
        
        this.update_restore_checkpoint(null);
        
        this.events.on('checkpoints_listed.Notebook', function (event, data) {
            that.update_restore_checkpoint(that.notebook.checkpoints);
        });
        
        this.events.on('checkpoint_created.Notebook', function (event, data) {
            that.update_restore_checkpoint(that.notebook.checkpoints);
        });
        
        this.events.on('notebook_loaded.Notebook', function() {
            var langinfo = that.notebook.metadata.language_info || {};
            that.update_nbconvert_script(langinfo);
        });
        
        this.events.on('kernel_ready.Kernel', function(event, data) {
            var langinfo = data.kernel.info_reply.language_info || {};
            that.update_nbconvert_script(langinfo);
            that.add_kernel_help_links(data.kernel.info_reply.help_links || []);
        });
    };
    
    MenuBar.prototype._add_celltoolbar_list = function () {
        var that = this;
        var submenu = $("#menu-cell-toolbar-submenu");
        
        function preset_added(event, data) {
            var name = data.name;
            submenu.append(
                $("<li/>")
                .attr('data-name', encodeURIComponent(name))
                .append(
                    $("<a/>")
                    .attr('href', '#')
                    .text(name)
                    .click(function () {
                        if (name ==='None') {
                            celltoolbar.CellToolbar.global_hide();
                            delete that.notebook.metadata.celltoolbar;
                        } else {
                            celltoolbar.CellToolbar.global_show();
                            celltoolbar.CellToolbar.activate_preset(name, that.events);
                            that.notebook.metadata.celltoolbar = name;
                        }
                        that.notebook.focus_cell();
                    })
                )
            );
        }
        
        // Setup the existing presets
        var presets = celltoolbar.CellToolbar.list_presets();
        preset_added(null, {name: i18n.msg._("None")});
        presets.map(function (name) {
            preset_added(null, {name: name});
        });

        // Setup future preset registrations
        this.events.on('preset_added.CellToolbar', preset_added);
        
        // Handle unregistered presets
        this.events.on('unregistered_preset.CellToolbar', function (event, data) {
            submenu.find("li[data-name='" + encodeURIComponent(data.name) + "']").remove();
        });
    };

    MenuBar.prototype.update_restore_checkpoint = function(checkpoints) {
        var ul = this.element.find("#restore_checkpoint").find("ul");
        ul.empty();
        if (!checkpoints || checkpoints.length === 0) {
            ul.append(
                $("<li/>")
                .addClass("disabled")
                .append(
                    $("<a/>")
                    .text(i18n.msg._("No checkpoints"))
                )
            );
            return;
        }
        
        var that = this;
        checkpoints.map(function (checkpoint) {
            var d = new Date(checkpoint.last_modified);
            ul.append(
                $("<li/>").append(
                    $("<a/>")
                    .attr("href", "#")
                    .text(moment(d).format("LLLL"))
                    .click(function () {
                        that.notebook.restore_checkpoint_dialog(checkpoint);
                    })
                )
            );
        });
    };
    
    MenuBar.prototype.update_nbconvert_script = function(langinfo) {
        /**
         * Set the 'Download as foo' menu option for the relevant language.
         */
        var el = this.element.find('#download_script');
        
        // Set menu entry text to e.g. "Python (.py)"
        var langname = (langinfo.name || 'Script');
        langname = langname.charAt(0).toUpperCase()+langname.substr(1); // Capitalise
        el.find('a').text(langname + ' ('+(langinfo.file_extension || 'txt')+')');
    };

    MenuBar.prototype.add_kernel_help_links = function(help_links) {
        /** add links from kernel_info to the help menu */
        var divider = $("#kernel-help-links");
        if (divider.length === 0) {
            // insert kernel help section above about link
            var about = $("#notebook_about").parent();
            divider = $("<li>")
                .attr('id', "kernel-help-links")
                .addClass('divider');
            about.prev().before(divider);
        }
        // remove previous entries
        while (!divider.next().hasClass('divider')) {
            divider.next().remove();
        }
        if (help_links.length === 0) {
            // no help links, remove the divider
            divider.remove();
            return;
        }
        var cursor = divider;
        help_links.map(function (link) {
            cursor.after($("<li>")
                .append($("<a>")
                    .attr('target', '_blank')
                    .attr('title', i18n.msg._('Opens in a new window'))
                    .attr('href', requirejs.toUrl(link.url))
                    .append($("<i>")
                        .addClass("fa fa-external-link menu-icon pull-right")
                    )
                    .append($("<span>")
                        .text(link.text)
                    )
                )
            );
            cursor = cursor.next();
        });
        
    };

    return {'MenuBar': MenuBar};
});
