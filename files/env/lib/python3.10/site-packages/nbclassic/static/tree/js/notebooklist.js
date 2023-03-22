// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
    'base/js/events',
    'base/js/keyboard',
    'moment',
    'bidi/bidi',
    'components/marked/lib/marked'
], function($, IPython, utils, i18n, dialog, events, keyboard, moment, bidi, marked) {
    "use strict";

    var extension = function(path){
      /**
       *  return the last pat after the dot in a filepath
       *  or the filepath itself if no dots present.
       *  Empty string if the filepath ends with a dot.
       **/
      var parts = path.split('.');
      return parts[parts.length-1];
    };

    var item_in = function(item, list) {
      // Normalize list and item to lowercase
      var normalized_list = list.map(function(_item) {
        return _item.toLowerCase();
      });
      return normalized_list.indexOf(item.toLowerCase()) !== -1;
    };

    var includes_extension = function(filepath, extensionslist) {
      return item_in(extension(filepath), extensionslist);
    };

    function name_sorter(ascending) {
        return (function(a, b) {
            if (type_order[a['type']] < type_order[b['type']]) {
                return -1;
            }
            if (type_order[a['type']] > type_order[b['type']]) {
                return 1;
            }
            if (a['name'].toLowerCase() < b['name'].toLowerCase()) {
                return (ascending) ? -1 : 1;
            }
            if (a['name'].toLowerCase() > b['name'].toLowerCase()) {
                return (ascending) ? 1 : -1;
            }
            return 0;
        });
    }

    function modified_sorter(ascending) {
        var order = ascending ? 1 : 0;
        return (function(a, b) {
            return utils.datetime_sort_helper(a.last_modified, b.last_modified,
                                              order)
        });
    }

    function size_sorter(ascending) {
        var order = ascending ? 1 : 0;
        // directories have file size of undefined
        return (function(a, b) {
          if (a.size === undefined) {
             return (ascending) ? -1 : 1;
          }

          if (b.size === undefined) {
             return (ascending) ? 1 : -1;
          }

          if (a.size > b.size) {
            return (ascending) ? -1 : 1;
          }

          if (b.size > a.size) {
            return (ascending) ? 1 : -1;
          }

          return 0;
        });
    }

    var sort_functions = {
        'sort-name': name_sorter,
        'last-modified': modified_sorter,
        'file-size': size_sorter
    };

    var NotebookList = function (selector, options) {
        /**
         * Constructor
         *
         * Parameters:
         *  selector: string
         *  options: dictionary
         *      Dictionary of keyword arguments.
         *          session_list: SessionList instance
         *          element_name: string
         *          base_url: string
         *          notebook_path: string
         *          contents: Contents instance
         */
        var that = this;
        this.session_list = options.session_list;
        this.events = this.session_list.events;
        // allow code re-use by just changing element_name in kernellist.js
        this.element_name = options.element_name || 'notebook';
        this.selector = selector;
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.style();
            this.bind_events();
        }
        this.notebooks_list = [];
        this.sessions = {};
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url || utils.get_body_data("baseUrl");
        this.notebook_path = options.notebook_path || utils.get_body_data("notebookPath");
        this.initial_notebook_path = this.notebook_path;
        this.contents = options.contents;
        if (this.session_list && this.session_list.events) {
            this.session_list.events.on('sessions_loaded.Dashboard',
                function(e, d) { that.sessions_loaded(d); });
        }
        this.selected = [];
        this.sort_function = name_sorter(1);
        // 0 => descending, 1 => ascending
        this.sort_id = 'sort-name';
        this.sort_direction = 1;
        this._max_upload_size_mb = 25;
        this.EDIT_MIMETYPES = [
          'application/javascript',
          'application/x-sh',
          'application/vnd.groove-tool-template'
        ];
    };

    NotebookList.prototype.style = function () {
        var prefix = '#' + this.element_name;
        $(prefix + '_toolbar').addClass('list_toolbar');
        $(prefix + '_list_info').addClass('toolbar_info');
        $(prefix + '_buttons').addClass('toolbar_buttons');
        $(prefix + '_list_header').addClass('list_header');
        this.element.addClass("list_container");
    };

    NotebookList.prototype.bind_events = function () {
        var that = this;
        $('#refresh_' + this.element_name + '_list').click(function () {
            that.load_sessions();
        });
        this.element.bind('dragover', function () {
            return false;
        });
        this.element.bind('drop', function(event){
            that.handleFilesUpload(event,'drop');
            return false;
        });

        // Bind events for singleton controls.
        if (!NotebookList._bound_singletons) {
            NotebookList._bound_singletons = true;
            $('#new-file').click(function(e) {
                var w = window.open('', IPython._target);
                that.contents.new_untitled(that.notebook_path || '', {type: 'file', ext: '.txt'}).then(function(data) {
                    w.location = utils.url_path_join(
                        that.base_url, that.nbclassic_path, 'edit',
                        utils.encode_uri_components(data.path)
                    );
                }).catch(function (e) {
                    w.close();
                    dialog.modal({
                        title: i18n.msg._('Creating File Failed'),
                        body: $('<div/>')
                            .text(i18n.msg._("An error occurred while creating a new file."))
                            .append($('<div/>')
                                .addClass('alert alert-danger')
                                .text(e.message || e)),
                        buttons: {
                            OK: {'class': 'btn-primary'}
                        }
                    });
                    console.warn('Error during New file creation', e);
                });
                that.load_sessions();
                e.preventDefault();
            });
            $('#new-folder').click(function(e) {
                that.contents.new_untitled(that.notebook_path || '', {type: 'directory'})
                .then(function(){
                    that.load_list();
                }).catch(function (e) {
                    dialog.modal({
                        title: i18n.msg._('Creating Folder Failed'),
                        body: $('<div/>')
                            .text(i18n.msg._("An error occurred while creating a new folder."))
                            .append($('<div/>')
                                .addClass('alert alert-danger')
                                .text(e.message || e)),
                        buttons: {
                            OK: {'class': 'btn-primary'}
                        }
                    });
                    console.warn('Error during New directory creation', e);
                });
                that.load_sessions();
                e.preventDefault();
            });

            // Bind events for action buttons.
            $('.rename-button').click($.proxy(this.rename_selected, this));
            $('.move-button').click($.proxy(this.move_selected, this));
            $('.download-button').click($.proxy(this.download_selected, this));
            $('.shutdown-button').click($.proxy(this.shutdown_selected, this));
            $('.duplicate-button').click($.proxy(this.duplicate_selected, this));
            $('.view-button').click($.proxy(this.view_selected, this));
            $('.edit-button').click($.proxy(this.edit_selected, this));
            $('.delete-button').click($.proxy(this.delete_selected, this));

            // Bind events for selection menu buttons.
            $('#selector-menu').click(function (event) {
                that.select($(event.target).attr('id'));
            });
            var select_all = $('#select-all');
            select_all.change(function () {
                if (!select_all.prop('checked') || select_all.data('indeterminate')) {
                    that.select('select-none');
                } else {
                    that.select('select-all');
                }
            });

            $('#button-select-all').click(function (e) {
                // toggle checkbox if the click doesn't come from the checkbox already
                if (!$(e.target).is('input[type=checkbox]')) {
                    if (select_all.prop('checked') || select_all.data('indeterminate')) {
                        that.select('select-none');
                    } else {
                        that.select('select-all');
                    }
                }
            });

            $('.sort-action').click(function(e) {
                var sort_on = e.target.id;

                // Clear sort indications in UI
                $(".sort-action i").removeClass("fa-arrow-up").removeClass("fa-arrow-down");

                if ((that.sort_id === sort_on) && (that.sort_direction === 1)) {
                    that.sort_list(sort_on, 0);
                    $("#" + sort_on + " i").addClass("fa-arrow-up");
                    that.sort_direction = 0;
                } else {
                    that.sort_list(sort_on, 1);
                    $("#" + sort_on + " i").addClass("fa-arrow-down");
                    that.sort_direction = 1;
                }
                that.sort_id = sort_on;
            });
        }
    };

    NotebookList.prototype.sort_list = function(id, order) {
        if (sort_functions.hasOwnProperty(id)) {
            this.sort_function = sort_functions[id](order);
            this.draw_notebook_list(this.model_list, this.error_msg);
        } else {
            console.error("No such sort id: '" + id + "'")
        }
    };

    NotebookList.prototype.handleFilesUpload =  function(event, dropOrForm) {
        var that = this;
        var files;
        if(dropOrForm === 'drop'){
            files = event.originalEvent.dataTransfer.files;
        } else  {
            files = event.originalEvent.target.files;
        }

        var reader_onload = function (event) {
            var item = $(event.target).data('item');
            that.add_file_data(event.target.result, item);
            that.add_upload_button(item);
        };
        var reader_onerror = function (event) {
            var item = $(event.target).data('item');
            var name = item.data('name');
            item.remove();
            dialog.modal({
                title : i18n.msg._('Failed to read file'),
                body : i18n.msg.sprintf(i18n.msg._("Failed to read file %s"),name),
                buttons : {'OK' : { 'class' : 'btn-primary' }}
            });
        };

        Array.from(files).forEach(function(f) {
            var name_and_ext = utils.splitext(f.name);
            var file_ext = name_and_ext[1];

            if (f.size > that._max_upload_size_mb * 1024 * 1024) {
            	var body_msg = i18n.msg.sprintf(i18n.msg._("The file size is %d MB. Do you still want to upload it?"),
            			Math.round(f.size / (1024 * 1024)));
                dialog.modal({
                    title : i18n.msg._('Large file size warning'),
                    body : body_msg,
                    buttons : {
                        Cancel: {},
                        Ok: {
                            class: "btn-primary",
                            click: function() {
                                that.add_large_file_upload_button(f);
                            }
                        }
                    }
                });
            }
            else{
                var reader = new FileReader();
                if (file_ext === '.ipynb') {
                    reader.readAsText(f);
                } else {
                    // read non-notebook files as binary
                    reader.readAsArrayBuffer(f);
                }
                var item = that.new_item(0, true);
                item.addClass('new-file');
                that.add_name_input(f.name, item, file_ext === '.ipynb' ? 'notebook' : 'file');
                // Store the list item in the reader so we can use it later
                // to know which item it belongs to.
                $(reader).data('item', item);
                reader.onload = reader_onload;
                reader.onerror = reader_onerror;
            }
        });
        // Clear fileinput value. This is required to
        // reset the form. Otherwise, if you upload a file, delete it and try to
        // upload it again, the changed event won't fire.
        var form = $('input.fileinput');
        form.val('');
        return false;
    };

    NotebookList.prototype.clear_list = function (remove_uploads) {
        /**
         * Clears the navigation tree.
         *
         * Parameters
         * remove_uploads: bool=False
         *      Should upload prompts also be removed from the tree.
         */
        if (remove_uploads) {
            this.element.children('.list_item').remove();
        } else {
            this.element.children('.list_item:not(.new-file)').remove();
        }
    };

    NotebookList.prototype.load_sessions = function(){
        this.session_list.load_sessions();
    };


    NotebookList.prototype.sessions_loaded = function(data){
        this.sessions = data;
        this.load_list();
    };

    NotebookList.prototype.load_list = function () {
        var that = this;
        // Add an event handler browser back and forward events
        window.onpopstate = function(e) {
            var path = (window.history.state && window.history.state.path) ?
                    window.history.state.path : that.initial_notebook_path;
            that.update_location(path);
        };
        var breadcrumb = $('.breadcrumb');
        breadcrumb.empty();
        var list_item = $('<li/>');
        var root_url = utils.url_path_join(that.base_url, that.nbclassic_path, '/tree');
        var root = $('<li/>').append(
            $("<a/>")
            .attr('href', root_url)
            .attr('title', i18n.msg._('Link to root folder'))
            .append(
                $("<i/>")
                .addClass('fa fa-folder')
            )
            .click(function(e) {
                // Allow the default browser action when the user holds a modifier (e.g., Ctrl-Click)
                if(e.altKey || e.metaKey || e.shiftKey) {
                    return true;
                }
                var path = '';
                window.history.pushState(
                    {path: path},
                    'Home',
                    utils.url_path_join(that.base_url, that.nbclassic_path, 'tree')
                );
                that.update_location(path);
                return false;
            })
        );
        breadcrumb.append(root);
        var path_parts = [];
        this.notebook_path.split('/').forEach(function(path_part) {
            path_parts.push(path_part);
            var path = path_parts.join('/');
            var url = utils.url_path_join(
                that.base_url,
                that.nbclassic_path,
                '/tree',
                utils.encode_uri_components(path)
            );
            var crumb = $('<li/>').append(
                $('<a/>')
                .attr('href', url)
                .text(path_part)
                .click(function(e) {
                    // Allow the default browser action when the user holds a modifier (e.g., Ctrl-Click)
                    if(e.altKey || e.metaKey || e.shiftKey) {
                        return true;
                    }
                    window.history.pushState(
                        {path: path},
                        path,
                        url
                    );
                    that.update_location(path);
                    return false;
                })
            );
            breadcrumb.append(crumb);
        });
        this.contents.list_contents(that.notebook_path).then(
            $.proxy(this.draw_notebook_list, this),
            function(error) {
                that.draw_notebook_list({content: []}, i18n.msg._("Server error: ") + error.message);
            }
        );
    };

    NotebookList.prototype.update_location = function (path) {
        this.notebook_path = path;
        $('body').attr('data-notebook-path', path);
        // Update the file tree list without reloading the page
        this.load_list();
        // Update the page title so the browser tab reflects it
        // Match how the title appears with a trailing slash or
        // "Home" if the page loads from the server.
        $('title').text(path ? path+'/' : i18n.msg._("Home"));
    };

    /**
     * Draw the list of notebooks
     * @method draw_notebook_list
     * @param {Array} list An array of dictionaries representing files or
     *     directories.
     * @param {String} error_msg An error message
     */


    var type_order = {'directory':0,'notebook':1,'file':2};

    NotebookList.prototype.draw_notebook_list = function (list, error_msg) {
        // Remember what was selected before the refresh.
        var selected_before = this.selected;

        // Store the data to be redrawn by sorting
        this.model_list = list;
        this.error_msg = error_msg;

        list.content.sort(this.sort_function);
        var message = error_msg || i18n.msg._('The notebook list is empty.');
        var item = null;
        var model = null;
        var len = list.content.length;
        this.clear_list();
        var n_uploads = this.element.children('.list_item').length;
        if (len === 0) {
            item = this.new_item(0);
            var span12 = item.children().first();
            span12.empty();
            span12.append($('<div style="margin:auto;text-align:center;color:grey"/>').text(message));
        }
        var path = this.notebook_path;
        var offset = n_uploads;
        if (path !== '') {
            item = this.new_item(offset, false);
            model = {
                type: 'directory',
                name: '..',
                path: utils.url_path_split(path)[0]
            };
            this.add_link(model, item);
            offset += 1;
        }
        for (var i=0; i<len; i++) {
            model = list.content[i];
            item = this.new_item(i+offset, true);
            try {
                this.add_link(model, item);
            } catch(err) {
                console.log('Error adding link: ' + err);
            }
        }
        this.add_header_footer(list)
        // Trigger an event when we've finished drawing the notebook list.
        events.trigger('draw_notebook_list.NotebookList');

        // Reselect the items that were selected before.  Notify listeners
        // that the selected items may have changed.  O(n^2) operation.
        selected_before.forEach(function(item) {
            var list_items = $('.list_item');
            for (var i=0; i<list_items.length; i++) {
                var $list_item = $(list_items[i]);
                if ($list_item.data('path') === item.path) {
                    $list_item.find('input[type=checkbox]').prop('checked', true);
                    break;
                }
            }
        });
        this._selection_changed();
    };


    /**
     * Adds header and/or footer
     * @param  {Array} list - list of folder contents
     */
    NotebookList.prototype.add_header_footer = function (list) {
      var that = this;
      function create_markdown_row(index, list_item) {
	var item = that.new_item(index);
	var span12 = item.children().first();
	span12.empty();
	that.contents.get(list_item.path, {"content": true}).then(
          function (data) {
	    span12.append($('<div style="margin:auto;text-align:center;color:grey"/>').innerHTML = marked(data.content));
	  },
          function(error) {
            span12.append(i18n.msg._("Server error: ") + error.message);
	  });
      };
      var f = list.content.find(function (el) {return el.name == "header.md"})
      if (f !== undefined) {
	create_markdown_row(0, f)
      }
      var f = list.content.find(function (el) {return el.name == "footer.md"})
      if (f !== undefined) {
	create_markdown_row(-1, f)
      }
    }


    /**
     * Creates a new item.
     * @param  {integer} index
     * @param  {boolean} [selectable] - tristate, undefined: don't draw checkbox,
     *                                  false: don't draw checkbox but pad
     *                                  where it should be, true: draw checkbox.
     * @return {JQuery} row
     */
    NotebookList.prototype.new_item = function (index, selectable) {
        var row = $('<div/>')
            .addClass("list_item")
            .addClass("row");

        var item = $("<div/>")
            .addClass("col-md-12")
            .appendTo(row);

        var checkbox;
        if (selectable !== undefined) {
            checkbox = $('<input/>')
                .attr('type', 'checkbox')
                .attr('title', i18n.msg._('Click here to rename, delete, etc.'))
                .appendTo(item);
        }

        $('<i/>')
            .addClass('item_icon')
            .appendTo(item);

        var link = $("<a/>")
            .addClass("item_link")
            .appendTo(item);

        $("<span/>")
            .addClass("item_name")
            .appendTo(link);

        var div = $('<div/>')
            .addClass('pull-right')
            .appendTo(item);

        var buttons = $('<div/>')
            .addClass("item_buttons pull-left")
            .appendTo(div);

        var div2 = $('<div/>')
            .addClass('pull-right')
            .appendTo(div);

        $("<span/>")
            .addClass("item_modified")
            .addClass("pull-left")
            .appendTo(div2);

        $("<span/>")
            .addClass("file_size")
            .addClass("pull-right")
            .appendTo(div2);

        if (selectable === false) {
            checkbox.css('visibility', 'hidden');
        } else if (selectable === true) {
            var that = this;
            row.click(function(e) {
                // toggle checkbox only if the click doesn't come from the checkbox or the link
                if (!$(e.target).is('span[class=item_name]') && !$(e.target).is('input[type=checkbox]')) {
                    checkbox.prop('checked', !checkbox.prop('checked'));
                }
                that._selection_changed();
            });
        }

        $('<div/>')
            .addClass('running-indicator')
            .text(i18n.msg._('Running'))
            .css('visibility', 'hidden')
            .appendTo(buttons);

        if (index === -1) {
            this.element.append(row);
        } else {
            this.element.children().eq(index).after(row);
        }
        return row;
    };


    NotebookList.icons = {
        directory: 'folder_icon',
        notebook: 'notebook_icon',
        file: 'file_icon'
    };

    NotebookList.uri_prefixes = {
        directory: 'tree',
        notebook: 'notebooks',
        file: 'edit'
    };

    /**
     * Select all items in the tree of specified type.
     * selection_type : string among "select-all", "select-folders", "select-notebooks", "select-running-notebooks", "select-files"
     *                  any other string (like "select-none") deselects all items
     */
    NotebookList.prototype.select = function(selection_type) {
        var that = this;
        $('.list_item').each(function(index, item) {
            var item_type = $(item).data('type');
            var state = false;
            state = state || (selection_type === "select-all");
            state = state || (selection_type === "select-folders" && item_type === 'directory');
            state = state || (selection_type === "select-notebooks" && item_type === 'notebook');
            state = state || (selection_type === "select-running-notebooks" && item_type === 'notebook' && that.sessions[$(item).data('path')] !== undefined);
            state = state || (selection_type === "select-files" && item_type === 'file');
            $(item).find('input[type=checkbox]').prop('checked', state);
        });
        this._selection_changed();
    };

    NotebookList.prototype._is_notebook = function(model) {
      var ipynb_extensions = ['ipynb'];
      return includes_extension(model.path, ipynb_extensions);
    };

    NotebookList.prototype._is_editable = function(model) {
      // Allow any file to be "edited"
      // Non-text files will display the following error:
      //   Error: [FILE] is not UTF-8 encoded
      //   Saving is disabled.
      //   See Console for more details.
      return true;
    };

    NotebookList.prototype._is_viewable = function(model) {
      var html_types = ['htm', 'html', 'xhtml', 'xml', 'mht', 'mhtml'];
      var media_extension = ['3gp', 'avi', 'mov', 'mp4', 'm4v', 'm4a', 'mp3', 'mkv', 'ogv', 'ogm', 'ogg', 'oga', 'webm', 'wav'];
      var image_type = ['bmp', 'gif', 'jpg', 'jpeg', 'png', 'webp'];
      var other_type = ['ico'];
      var viewable_extensions = [].concat(html_types, media_extension, image_type, other_type);
      return model.mimetype === 'text/html'
        || includes_extension(model.path, viewable_extensions);
    };

    // Files like PDF that should be opened using `/files` prefix
    NotebookList.prototype._is_pdflike = function(model) {
      var pdflike_extensions = ['pdf'];
      return includes_extension(model.path, pdflike_extensions);
    };

    /**
     * Handles when any row selector checkbox is toggled.
     */
    NotebookList.prototype._selection_changed = function() {
        // Use a JQuery selector to find each row with a checked checkbox.  If
        // we decide to add more checkboxes in the future, this code will need
        // to be changed to distinguish which checkbox is the row selector.
        var that = this;
        var selected = [];
        var has_running_notebook = false;
        var has_directory = false;
        var has_file = false;
        var checked = 0;
        $('.list_item :checked').each(function(index, item) {
            var parent = $(item).parent().parent();

            // If the item doesn't have an upload button, isn't the
            // breadcrumbs and isn't the parent folder '..', then it can be selected.
            // Breadcrumbs path == ''.
            if (parent.find('.upload_button').length === 0 && parent.data('path') !== '' && parent.data('path') !== utils.url_path_split(that.notebook_path)[0]) {
                checked++;
                selected.push({
                    name: parent.data('name'),
                    path: parent.data('path'),
                    type: parent.data('type')
                });

                // Set flags according to what is selected.  Flags are later
                // used to decide which action buttons are visible.
                has_running_notebook = has_running_notebook ||
                    (parent.data('type') === 'notebook' && that.sessions[parent.data('path')] !== undefined);
                has_file = has_file || (parent.data('type') === 'file');
                has_directory = has_directory || (parent.data('type') === 'directory');
            }
        });
        this.selected = selected;

        // Rename is only visible when one item is selected, and it is not a running notebook
        if (selected.length === 1 && !has_running_notebook) {
            $('.rename-button').css('display', 'inline-block');
        } else {
            $('.rename-button').css('display', 'none');
        }

        // Move is visible if at least one item is selected, and none of them
        // are a running notebook.
        if (selected.length > 0 && !has_running_notebook) {
            $('.move-button').css('display', 'inline-block');
        } else {
            $('.move-button').css('display', 'none');
        }

        // Download is only visible when items are selected, and none are
        // running notebooks or a directories
        if (selected.length > 0 && !has_running_notebook && !has_directory) {
            $('.download-button').css('display', 'inline-block');
        } else {
            $('.download-button').css('display', 'none');
        }

        // Shutdown is only visible when one or more notebooks running notebooks
        // are selected and no non-notebook items are selected.
        if (has_running_notebook && !(has_file || has_directory)) {
            $('.shutdown-button').css('display', 'inline-block');
        } else {
            $('.shutdown-button').css('display', 'none');
        }

        // Duplicate isn't visible when a directory is selected.
        if (selected.length > 0 && !has_directory) {
            $('.duplicate-button').css('display', 'inline-block');
        } else {
            $('.duplicate-button').css('display', 'none');
        }

        // Delete is visible if one or more items are selected.
        if (selected.length > 0) {
            $('.delete-button').css('display', 'inline-block');
        } else {
            $('.delete-button').css('display', 'none');
        }

        // View is visible in the following case:
        //
        //   - the item is editable
        //   - it is not a notebook
        //
        // If it's not editable or unknown, the default action should be view
        // already so no need to show the button.
        // That should include things like, html, py, txt, json....
        if (selected.length >= 1 && !has_directory) {
            $('.view-button').css('display', 'inline-block');
        } else {
            $('.view-button').css('display', 'none');
        }

        // Edit is visible when an item is unknown, that is to say:
        //    - not in the editable list
        //    - not in the known non-editable list.
        //    - not a notebook.
        // Indeed if it's editable the default action is already to edit.
        // And non editable files should not show edit button.
        // for unknown we'll assume users know what they are doing.
        if (selected.length >= 1 && !has_directory && selected.every(function(el) {
            return that._is_editable(el);
        })) {
            $('.edit-button').css('display', 'inline-block');
        } else {
            $('.edit-button').css('display', 'none');
        }

        // If all of the items are selected, show the selector as checked.  If
        // some of the items are selected, show it as checked.  Otherwise,
        // uncheck it.
        var total = 0;
        $('.list_item input[type=checkbox]').each(function(index, item) {
            var parent = $(item).parent().parent();
            // If the item doesn't have an upload button and it's not the
            // breadcrumbs, it can be selected.  Breadcrumbs path == ''.
            if (parent.find('.upload_button').length === 0 && parent.data('path') !== '' && parent.data('path') !== utils.url_path_split(that.notebook_path)[0]) {
                total++;
            }
        });

        var select_all = $("#select-all");
        if (checked === 0) {
            select_all.prop('checked', false);
            select_all.prop('indeterminate', false);
            select_all.data('indeterminate', false);
        } else if (checked === total) {
            select_all.prop('checked', true);
            select_all.prop('indeterminate', false);
            select_all.data('indeterminate', false);
        } else {
            select_all.prop('checked', false);
            select_all.prop('indeterminate', true);
            select_all.data('indeterminate', true);
        }
        // Update total counter
        checked = bidi.applyBidi(checked);
        $('#counter-select-all').html(checked===0 ? '&nbsp;' : checked);

        //#issue 3961, update the checkbox aria-label when it changed
        if(selected.length>=1){
          if($('#select-all').prop("checked")){
            // $('#button-select-all').attr("aria-label", i18n.msg._("Selected All "+ selected.length +" items"));
            var msg1 = i18n.msg._("Selected All %d items")
            $('#button-select-all').attr("aria-label", i18n.msg.sprintf(msg1, selected.length));
          }
          else{
            // $('#button-select-all').attr("aria-label", i18n.msg._("Selected, "+ selected.length+" items"));
            var msg2 = i18n.msg._("Selected, %d items")
            $('#button-select-all').attr("aria-label", i18n.msg.sprintf(msg2, selected.length));
          }
        }
        else{
          $('#button-select-all').attr("aria-label", i18n.msg._("Select All/None"));
        }

        // If at aleast on item is selected, hide the selection instructions.
        if (checked > 0) {
            $('.dynamic-instructions').hide();
        } else {
            $('.dynamic-instructions').show();
        }
    };

    NotebookList.prototype.add_link = function (model, item) {
        var that = this;
        var running = (model.type === 'notebook' && this.sessions[model.path] !== undefined);
        item.data('name',model.name);
        item.data('path', model.path);
        item.data('modified', model.last_modified);
        item.data('type', model.type);
        item.find(".item_name").text(bidi.applyBidi(model.name));
        var icon = NotebookList.icons[model.type];
        if (running) {
            icon = 'running_' + icon;
        }
        var uri_prefix = NotebookList.uri_prefixes[model.type];
        if (model.type === 'file' && this._is_viewable(model))
        {
            uri_prefix = 'view';
        }
        if (model.type === 'file' && this._is_pdflike(model))
        {
            uri_prefix = 'files';
        }
        if (model.type === 'file' && this._is_notebook(model))
        {
            uri_prefix = 'notebooks';
        }

        item.find(".item_icon").addClass(icon).addClass('icon-fixed-width');
        var link = item.find("a.item_link")
            .attr('href',
                utils.url_path_join(
                    this.base_url,
                    this.nbclassic_path,
                    uri_prefix,
                    utils.encode_uri_components(model.path)
                )
            );

        item.find(".item_buttons .running-indicator").css('visibility', running ? '' : 'hidden');

        // directory nav doesn't open new tabs
        // files, notebooks do
        if (model.type !== "directory") {
            link.attr('target', IPython._target);
        } else {
            // Replace with a click handler that will use the History API to
            // push a new route without reloading the page if the click is
            // not modified (e.g., Ctrl-Click)
            link.click(function (e) {
                if(e.altKey || e.metaKey || e.shiftKey) {
                    return true;
                }
                window.history.pushState({
                    path: model.path
                }, model.path, utils.url_path_join(
                    that.base_url,
                    that.nbclassic_path,
                    'tree',
                    utils.encode_uri_components(model.path)
                ));
                that.update_location(model.path);
                return false;
            });
        }

        // Add in the date that the file was last modified
        item.find(".item_modified").text(utils.format_datetime(model.last_modified));
        item.find(".item_modified").attr("title", moment(model.last_modified).format("YYYY-MM-DD HH:mm"));

        var filesize = utils.format_filesize(model.size);
        item.find(".file_size").text(filesize || '\xA0');
    };


    NotebookList.prototype.add_name_input = function (name, item, icon_type) {
        item.data('name', name);
        item.find(".item_icon").addClass(NotebookList.icons[icon_type]).addClass('icon-fixed-width');
        item.find(".item_name").empty().append(
            $('<input/>')
            .addClass("filename_input")
            .attr('value', name)
            .attr('size', '30')
            .attr('type', 'text')
            .keyup(function(event){
                if(event.keyCode === 13){item.find('.upload_button').click();}
                else if(event.keyCode === 27){item.remove();}
            })
        );
    };


    NotebookList.prototype.add_file_data = function (data, item) {
        item.data('filedata', data);
    };


    NotebookList.prototype.shutdown_selected = function() {
        var that = this;
        this.selected.forEach(function(item) {
            if (item.type === 'notebook') {
                that.shutdown_notebook(item.path);
            }
        });
        // Deselect items after successful shutdown.
        that.select('select-none');
    };

    NotebookList.prototype.shutdown_notebook = function(path) {
        var that = this;
        var settings = {
            processData : false,
            cache : false,
            type : "DELETE",
            dataType : "json",
            success : function () {
                that.load_sessions();
            },
            error : utils.log_ajax_error
        };

        var session = this.sessions[path];
        if (session) {
            var url = utils.url_path_join(
                this.base_url,
                'api/sessions',
                encodeURIComponent(session.id)
            );
            utils.ajax(url, settings);
        }
    };

    NotebookList.prototype.rename_selected = function() {
        if (this.selected.length !== 1){
            return;
        }

        var that = this;
        var item_path = this.selected[0].path;
        var item_name = this.selected[0].name;
        var item_type = this.selected[0].type;
        var input = $('<input/>')
            .attr('type','text')
            .attr('size','25')
            .attr('aria-labelledby','rename-message')
            .addClass('form-control')
            .val(item_name);
        var rename_msg = function (type) {
        	switch(type) {
        	case 'file': return i18n.msg._("Enter a new file name:");
        	case 'directory': return i18n.msg._("Enter a new directory name:");
        	case 'notebook': return i18n.msg._("Enter a new notebook name:");
        	default: return i18n.msg._("Enter a new name:");
        	}
        };
        var rename_title = function (type) {
           	switch(type) {
           	case 'file': return i18n.msg._("Rename file");
           	case 'directory': return i18n.msg._("Rename directory");
           	case 'notebook': return i18n.msg._("Rename notebook");
           	default: return i18n.msg._("Rename");
           	}
        };
        var dialog_body = $('<div/>').append(
            $("<p/>").addClass("rename-message")
                .attr('id', 'rename-message')
                .text(rename_msg(item_type))
        ).append(
            $("<br/>")
        ).append(input);

        // This statement is used simply so that message extraction
        // will pick up the strings.  The actual setting of the text
        // for the button is in dialog.js.
        var button_labels = [ i18n.msg._("Cancel"), i18n.msg._("Rename"), i18n.msg._("OK"), i18n.msg._("Move")];

        var d = dialog.modal({
            title : rename_title(item_type),
            body : dialog_body,
            default_button: "Cancel",
            buttons : {
                Cancel: {},
                Rename : {
                    class: "btn-primary",
                    click: function() {
                        that.contents.rename(item_path, utils.url_path_join(that.notebook_path, input.val())).then(function() {
                            that.load_list();
                            // Deselect items after successful rename.
                            that.select('select-none');
                        }).catch(function(e) {
                        	var template = i18n.msg._("An error occurred while renaming \"%1$s\" to \"%2$s\".");
                        	var failmsg = i18n.msg.sprintf(template,item_name,input.val());
                            dialog.modal({
                                title: i18n.msg._("Rename Failed"),
                                body: $('<div/>')
                                    .text(failmsg)
                                    .append($('<div/>')
                                        .addClass('alert alert-danger')
                                        .text(e.message || e)),
                                buttons: {
                                    OK: {'class': 'btn-primary'}
                                }
                            });
                            console.warn('Error during renaming :', e);
                        });
                    }
                }
            },
            open : function () {
                // Upon ENTER, click the OK button.
                input.keydown(function (event) {
                    if (event.which === keyboard.keycodes.enter) {
                        d.find('.btn-primary').first().click();
                        return false;
                    }
                });
                input.focus();
                // Highlight the filename (up to the filetype suffix) in the input field.
                if (input.val().indexOf(".") > 0) {
                    input[0].setSelectionRange(0,input.val().indexOf("."));
                } else {
                    input.select();
                }
            }
        });
    };

    NotebookList.prototype.move_selected = function() {
        var that = this;
        var selected = that.selected.slice(); // Don't let that.selected change out from under us
        var num_items = selected.length;

        // Can move one or more selected items.
        if (!(num_items >= 1)) {
            return;
        }

        // Open a dialog to enter the new path, with current path as default.
        var input = $('<input/>').attr('type','text').attr('size','25').attr('aria-labelledby','move-message').addClass('form-control')
            .val(utils.url_path_join('/', that.notebook_path));
        var dialog_body = $('<div/>').append(
            $("<p/>").addClass("rename-message").attr('id', 'move-message')
                .text(i18n.msg.sprintf(i18n.msg.ngettext("Enter a new destination directory path for this item:",
                					"Enter a new destination directory path for these %d items:", num_items),num_items))
        ).append(
            $("<br/>")
        ).append(
            $("<div/>").append(
                // $("<i/>").addClass("fa fa-folder").addClass("server-root")
                $("<span/>").text(utils.get_body_data("serverRoot")).addClass("server-root")
            ).append(
              input.addClass("path-input")
            ).addClass("move-path")
        );
        var d = dialog.modal({
            title : i18n.msg.sprintf(i18n.msg.ngettext("Move an Item","Move %d Items",num_items),num_items),
            body : dialog_body,
            default_button: "Cancel",
            buttons : {
                Cancel : {},
                Move : {
                    class: "btn-primary",
                    click: function() {
                        // Move all the items.
                        selected.forEach(function(item) {
                            var item_path = item.path;
                            var item_name = item.name;
                            // Construct the new path using the user input and the item's name.
                            var new_path = utils.url_path_join(input.val(), item_name);
                            that.contents.rename(item_path, new_path).then(function() {
                                // After each move finishes, reload the list.
                                that.load_list();
                            }).catch(function(e) {
                                // If any of the moves fails, show this dialog for that move.
                            	var failmsg = i18n.msg._("An error occurred while moving \"%1$s\" from \"%2$s\" to \"%3$s\".");
                                dialog.modal({
                                    title: i18n.msg._("Move Failed"),
                                    body: $('<div/>')
                                        .text(i18n.msg.sprintf(failmsg,item_name,item_path,new_path))
                                        .append($('<div/>')
                                            .addClass('alert alert-danger')
                                            .text(e.message || e)),
                                    buttons: {
                                        OK: {'class': 'btn-primary'}
                                    }
                                });
                                console.warn('Error during moving :', e);
                            });
                        });  // End of forEach.
                    }
                }
            },
            // TODO: Consider adding fancier UI per Issue #941.
            open : function () {
                // Upon ENTER, click the OK button.
                input.keydown(function (event) {
                    if (event.which === keyboard.keycodes.enter) {
                        d.find('.btn-primary').first().click();
                        return false;
                    }
                });
                // Put the cursor at the end of the input.
                input.focus();
            }
        });
    };

    NotebookList.prototype.download_selected = function() {
        var that = this;

        that.selected.forEach(function(item) {
            var item_path = utils.encode_uri_components(item.path);
            window.open(utils.url_path_join(that.base_url, 'files', item_path) + '?download=1', IPython._target);
      	});
    };

    NotebookList.prototype.delete_selected = function() {
        var selected = this.selected.slice(); // Don't let that.selected change out from under us
        var template = i18n.msg.ngettext("Are you sure you want to permanently delete: \"%s\"?",
        						"Are you sure you want to permanently delete the %d files or folders selected?",
        						selected.length);
        var delete_msg;
        if (selected.length === 1) {
            delete_msg = i18n.msg.sprintf(template, selected[0].name);
        } else {
            delete_msg = i18n.msg.sprintf(template, selected.length);
        }
        var that = this;
        dialog.modal({
            title : i18n.msg._("Delete"),
            body : delete_msg,
            default_button: "Cancel",
            buttons : {
                Cancel: {},
                Delete : {
                    class: "btn-danger",
                    click: function() {
                        // Shutdown any/all selected notebooks before deleting
                        // the files.
                        that.shutdown_selected();

                        // Delete selected.
                        selected.forEach(function(item) {
                            that.contents.delete(item.path).then(function() {
                                    that.notebook_deleted(item.path);
                            }).catch(function(e) {
                            	var failmsg = i18n.msg._("An error occurred while deleting \"%s\".");
                                dialog.modal({
                                    title: i18n.msg._("Delete Failed"),
                                    body: $('<div/>')
                                        .text(i18n.msg.sprintf(failmsg, item.path))
                                        .append($('<div/>')
                                            .addClass('alert alert-danger')
                                            .text(e.message || e)),
                                    buttons: {
                                        OK: {'class': 'btn-primary'}
                                    }
                                });
                                console.warn('Error during content deletion:', e);
                            });
                        });
                    }
                }
            }
        });
    };

    NotebookList.prototype.view_selected = function() {
        var that = this;
        that.selected.forEach(function(item) {
            var item_path = utils.encode_uri_components(item.path);
            var item_type = that._is_notebook(item) ? 'notebooks' : that._is_viewable(item) ? 'view' : 'files';
            window.open(utils.url_path_join(that.base_url, item_type, item_path), IPython._target);
      	});
    };

    NotebookList.prototype.edit_selected = function() {
        var that = this;
        that.selected.forEach(function(item) {
            var item_path = utils.encode_uri_components(item.path);
            window.open(utils.url_path_join(that.base_url, 'edit', item_path), IPython._target);
      	});
    };

    NotebookList.prototype.duplicate_selected = function() {
        var selected = this.selected.slice(); // Don't let that.selected change out from under us
    	var template = i18n.msg.ngettext("Are you sure you want to duplicate: \"%s\"?",
				"Are you sure you want to duplicate the %d files selected?",selected.length);
    	var dup_msg;
        if (selected.length === 1) {
            dup_msg = i18n.msg.sprintf(template,selected[0].name);
        } else {
            dup_msg = i18n.msg.sprintf(template,selected.length);
        }
        var that = this;
        dialog.modal({
            title : i18n.msg._("Duplicate"),
            body : dup_msg,
            default_button: "Cancel",
            buttons : {
                Cancel: {},
                Duplicate : {
                    class: "btn-primary",
                    click: function() {
                        selected.forEach(function(item) {
                            that.contents.copy(item.path, that.notebook_path).then(function () {
                                that.load_list();
                                // Deselect items after successful duplication.
                                that.select('select-none');
                            }).catch(function(e) {
                            	var failmsg = i18n.msg._("An error occurred while duplicating \"%s\".");
                                dialog.modal({
                                    title: i18n.msg._("Duplicate Failed"),
                                    body: $('<div/>')
                                        .text(i18n.msg.sprintf(failmsg,item.path))
                                        .append($('<div/>')
                                            .addClass('alert alert-danger')
                                            .text(e.message || e)),
                                    buttons: {
                                        OK: {'class': 'btn-primary'}
                                    }
                                });
                                console.warn('Error during content duplication', e);
                            });
                        });
                    }
                }
            }
        });
    };

    NotebookList.prototype.notebook_deleted = function(path) {
        /**
         * Remove the deleted notebook.
         */
        var that = this;
        $(".list_item").each(function() {
            var element = $(this);
            if (element.data("path") === path) {
                element.remove();
                events.trigger('notebook_deleted.NotebookList');
                that._selection_changed();
            }
        });
    };

    // Add a new class for large file upload
    NotebookList.prototype.add_large_file_upload_button = function (file) {
        var that = this;
        var item = that.new_item(0, true);
        var stop_signal = false;
        item.addClass('new-file');
        that.add_name_input(file.name, item, 'file');
        var cancel_button = $('<button/>').text("Cancel")
            .addClass("btn btn-default btn-xs")
            .click(function (e) {
                item.remove();
                stop_signal = true;
                return false;
            });

        var upload_button = $('<button/>').text("Upload")
            .addClass('btn btn-primary btn-xs upload_button')
            .click(function (e) {
                var filename = item.find('.item_name > input').val();
                var path = utils.url_path_join(that.notebook_path, filename);
                var format = 'text';
                if (filename.length === 0 || filename[0] === '.') {
                    dialog.modal({
                        title : 'Invalid file name',
                        body : "File names must be at least one character and not start with a dot",
                        buttons : {'OK' : { 'class' : 'btn-primary' }}
                    });
                    return false;
                }

                var check_exist = function () {
                    var exists = false;
                    $.each(that.element.find('.list_item:not(.new-file)'), function(k,v){
                    if ($(v).data('name') === filename) { exists = true; return false; }
                    });
                    return exists
                };
                var exists = check_exist();

                var add_uploading_button = function (f, item) {
                    // change buttons, add a progress bar
                    var uploading_button = item.find('.upload_button').text("Uploading");
                    uploading_button.off('click');  // Prevent double upload
                    var progress_bar = $('<span/>')
                        .addClass('progress-bar')
                        .css('top', '0')
                        .css('left', '0')
                        .css('width', '0')
                        .css('height', '3px')
                        .css('border-radius', '0 0 0 0')
                        .css('display', 'inline-block')
                        .css('position', 'absolute');

                    var parse_large_file = function (f, item) {
                        // codes inspired by https://stackoverflow.com/a/28318964
                        // 8MB chunk size chosen to match chunk sizes used by benchmark reference (AWS S3)
                        var chunk_size = 1024 * 1024 * 8;
                        var offset = 0;
                        var chunk = 0;
                        var chunk_reader = null;

                        var large_reader_onload = function (event) {
                            if (stop_signal === true) {
                                return;
                            }
                            if (event.target.error == null) {
                                offset += chunk_size;
                                if (offset >= f.size) {
                                    chunk = -1;
                                } else {
                                    chunk += 1;
                                }
                                // callback for handling reading: reader_onload in add_upload_button
                                var item = $(event.target).data('item');
                                that.add_file_data(event.target.result, item);
                                upload_file(item, chunk);  // Do the upload
                            } else {
                                console.log("Read error: " + event.target.error);
                            }
                        };
                        var on_error = function (event) {
                            var item = $(event.target).data('item');
                            var name = item.data('name');
                            item.remove();
                            var _exists = check_exist();
                            if (_exists) {
                                that.contents.delete(path);
                            }
                            dialog.modal({
                                title : 'Failed to read file',
                                body : "Failed to read file '" + name + "'",
                                buttons : {'OK' : { 'class' : 'btn-primary' }}
                            });
                        };

                        chunk_reader = function (_offset, _f) {
                            var reader = new FileReader();
                            var blob = _f.slice(_offset, chunk_size + _offset);
                            // Load everything as ArrayBuffer
                            reader.readAsArrayBuffer(blob);
                            // Store the list item in the reader so we can use it later
                            // to know which item it belongs to.
                            $(reader).data('item', item);
                            reader.onload = large_reader_onload;
                            reader.onerror = on_error;
                        };

                        // This approach avoids triggering multiple GC pauses for large files.
                        // Borrowed from kanaka's answer at:
                        // https://stackoverflow.com/questions/12710001/how-to-convert-uint8-array-to-base64-encoded-string
                        var  Uint8ToString = function(u8a){
                            var CHUNK_SZ = 0x8000;
                            var c = [];
                            for (var i=0; i < u8a.length; i+=CHUNK_SZ) {
                              c.push(String.fromCharCode.apply(null, u8a.subarray(i, i+CHUNK_SZ)));
                            }
                            return c.join("");
                        };

                        // These codes to upload file in original class
                        var upload_file = function(item, chunk) {
                            var filedata = item.data('filedata');
                            if (filedata instanceof ArrayBuffer) {
                                // base64-encode binary file data
                                var buf = new Uint8Array(filedata);
                                filedata = btoa(Uint8ToString(buf));
                                format = 'base64';
                            }
                            var model = { name: filename, path: path };

                            var name_and_ext = utils.splitext(filename);
                            var file_ext = name_and_ext[1];
                            var content_type;
                            // Treat everything as generic file
                            model.type = 'file';
                            model.format = format;
                            content_type = 'application/octet-stream';

                            model.chunk = chunk;
                            model.content = filedata;

                            var on_success = function () {
                                if (offset < f.size) {
                                    // of to the next chunk
                                    chunk_reader(offset, f);
                                    // change progress bar and progress button
                                    var progress = offset / f.size * 100;
                                    progress = progress > 100 ? 100 : progress;
                                    uploading_button.text(progress.toFixed(0)+'%');
                                    progress_bar.css('width', progress+'%')
                                        .attr('aria-valuenow', progress.toString());
                                } else {
                                    item.removeClass('new-file');
                                    that.add_link(model, item);
                                    that.session_list.load_sessions();
                                }
                            };
                            that.contents.save(path, model).then(on_success, on_error);
                        };

                        // now let's start the read with the first block
                        chunk_reader(offset, f);
                    };
                    item.find('.item_buttons')
                        .append(progress_bar);
                    parse_large_file(f, item);
                };
                if (exists) {
                    dialog.modal({
                        title : "Replace file",
                        body : 'There is already a file named ' + filename + ', do you want to replace it?',
                        default_button: "Cancel",
                        buttons : {
                            Overwrite : {
                                class: "btn-danger",
                                click: function () {
                                    add_uploading_button(file, item);
                                }
                            },
                            Cancel : {
                                click: function() { item.remove(); }
                            }
                        }
                    });
                } else {
                    add_uploading_button(file, item);
                }

                return false;
            });
        item.find(".item_buttons").empty()
            .append(upload_button)
            .append(cancel_button);
    };

    NotebookList.prototype.add_upload_button = function (item) {
        var that = this;
        var upload_button = $('<button/>').text(i18n.msg._("Upload"))
            .addClass('btn btn-primary btn-xs upload_button')
            .click(function (e) {
                item.find('.upload_button').text("Uploading...");
                var filename = item.find('.item_name > input').val();
                var path = utils.url_path_join(that.notebook_path, filename);
                var filedata = item.data('filedata');
                var format = 'text';
                if (filename.length === 0 || filename[0] === '.') {
                    dialog.modal({
                        title : i18n.msg._('Invalid file name'),
                        body : i18n.msg._("File names must be at least one character and not start with a period"),
                        buttons : {'OK' : { 'class' : 'btn-primary' }}
                    });
                    return false;
                }
                if (filedata instanceof ArrayBuffer) {
                    // base64-encode binary file data
                    var bytes = '';
                    var buf = new Uint8Array(filedata);
                    var nbytes = buf.byteLength;
                    for (var i=0; i<nbytes; i++) {
                        bytes += String.fromCharCode(buf[i]);
                    }
                    filedata = btoa(bytes);
                    format = 'base64';
                }
                var model = { name: filename, path: path };

                var name_and_ext = utils.splitext(filename);
                var file_ext = name_and_ext[1];
                var content_type;
                if (file_ext === '.ipynb') {
                    model.type = 'notebook';
                    model.format = 'json';
                    try {
                        model.content = JSON.parse(filedata);
                    } catch (e) {
                    	var failbody = i18n.msg._("The error was: %s");
                        dialog.modal({
                            title : i18n.msg._('Cannot upload invalid Notebook'),
                            body : i18n.msg.sprintf(failbody,e),
                            buttons : {'OK' : {
                                'class' : 'btn-primary',
                                click: function () {
                                    item.remove();
                                }
                            }}
                        });
                        console.warn('Error during notebook uploading', e);
                        return false;
                    }
                    content_type = 'application/json';
                } else {
                    model.type = 'file';
                    model.format = format;
                    model.content = filedata;
                    content_type = 'application/octet-stream';
                }

                var on_success = function () {
                    item.removeClass('new-file');
                    that.add_link(model, item);
                    that.session_list.load_sessions();
                };

                var exists = false;
                $.each(that.element.find('.list_item:not(.new-file)'), function(k,v){
                    if ($(v).data('name') === filename) { exists = true; return false; }
                });

                if (exists) {
                	var body = i18n.msg._("There is already a file named \"%s\". Do you want to replace it?");
                    dialog.modal({
                        title : i18n.msg._("Replace file"),
                        body : i18n.msg.sprintf(body,filename),
                        default_button: "Cancel",
                        buttons : {
                            Cancel : {
                                click: function() { item.remove(); }
                            },
                            Overwrite : {
                                class: "btn-danger",
                                click: function () {
                                    that.contents.save(path, model).then(on_success);
                                }
                            }
                        }
                    });
                } else {
                    that.contents.save(path, model).then(on_success);
                }

                return false;
            });
        var cancel_button = $('<button/>').text(i18n.msg._("Cancel"))
            .addClass("btn btn-default btn-xs")
            .click(function (e) {
                item.remove();
                return false;
            });
        item.find(".item_buttons").empty()
            .append(upload_button)
            .append(cancel_button);
    };

    return {'NotebookList': NotebookList};
});
