// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'notebook/js/celltoolbar',
    'base/js/dialog',
    'base/js/i18n'
], function(celltoolbar, dialog, i18n) {
    "use strict";

    var CellToolbar = celltoolbar.CellToolbar;

    var array_difference = function(a, b) {
        return a.filter(function(n) {
            return b.indexOf(n) === -1;
        });
    };

    var write_tag = function(cell, name, add) {
        if (add) {
            // Add to metadata
            if (cell.metadata.tags === undefined) {
                cell.metadata.tags = [];
            } else if (cell.metadata.tags.indexOf(name) !== -1) {
                // Tag already exists
                return false;
            }
            cell.metadata.tags.push(name);
        } else {
            // Remove from metadata
            if (!cell.metadata || !cell.metadata.tags) {
                // No tags to remove
                return false;
            }
            // Remove tag from tags list
            var index = cell.metadata.tags.indexOf(name);
            if (index !== -1) {
                cell.metadata.tags.splice(index, 1);
            }
            // If tags list is empty, remove it
            if (cell.metadata.tags.length === 0) {
                delete cell.metadata.tags;
            }
        }
        cell.events.trigger('set_dirty.Notebook', {value: true});
        return true;
    };

    var preprocess_input = function(input) {
        // Split on whitespace + commas:
        return input.split(/[,\s]+/)
    };

    var add_tag = function(cell, tag_container, on_remove) {
        return function(name) {
            if (name === '') {
                // Skip empty strings
                return;
            }
            // Write tag to metadata
            var changed = write_tag(cell, name, true);

            if (changed) {
                // Make tag UI
                var tag = make_tag(name, on_remove, cell.is_editable());
                tag_container.append(tag);
                var tag_map = jQuery.data(tag_container, "tag_map") || {};
                tag_map[name] = tag;
                jQuery.data(tag_container, 'tag_map', tag_map);
            }
        };
    };

    var remove_tag = function(cell, tag_container) {
        return function(name) {
            var changed = write_tag(cell, name, false);
            if (changed) {
                // Remove tag UI
                var tag_map = jQuery.data(tag_container, "tag_map") || {};
                var tag_UI = tag_map[name];
                delete tag_map[name];
                tag_UI.remove();
            }
        };
    };

    var init_tag_container = function(cell, tag_container, on_remove) {    
        var tag_list = cell.metadata.tags || [];
        if (!Array.isArray(tag_list)) {
            // We cannot make tags UI for this cell!
            // Maybe someone else used "tags" for something?
            return false;  // Fail gracefully
        }

        var tag_map = {};
        for (var i=0; i < tag_list.length; ++i) {
            var tag_name = tag_list[i];
            if (typeof tag_name !== 'string') {
                // Unexpected type, disable toolbar for safety
                return false;
            }
            var tag = make_tag(tag_name, on_remove, cell.is_editable());
            tag_container.append(tag);
            tag_map[tag_name] = tag;
        }
        jQuery.data(tag_container, 'tag_map', tag_map);
        return true;
    };

    var make_tag = function(name, on_remove, is_editable) {
        var tag_UI = $('<span/>')
            .addClass('cell-tag')
            .text(name);

        if(is_editable){
            var remove_button = $('<i/>')
                .addClass('remove-tag-btn')
                .addClass('fa fa-times')
                .click(function () {
                    on_remove(name);
                    return false;
                });
            tag_UI.append(remove_button);
        }
        return tag_UI;
    };

    // Single edit with button to add tags
    var add_tag_edit = function(div, cell, on_add, on_remove) {
        var button_container = $(div);

        var text = $('<input/>').attr('type', 'text');
        var button = $('<button />')
            .addClass('btn btn-default btn-xs')
            .text(i18n.msg._('Add tag'))
            .click(function() {
                var tags = preprocess_input(text[0].value);
                for (var i=0; i < tags.length; ++i) {
                    on_add(tags[i]);
                }
                // Clear input after adding:
                text[0].value = '';
                return false;
            });
        // Wire enter in input to button click
        text.keyup(function(event){
            if(event.keyCode == 13){
                button.click();
            }
        });
        var input_container = $('<span/>')
            .addClass('tags-input');
        add_dialog_button(input_container, cell, on_add, on_remove);
        button_container.append(input_container
                .append(text)
                .append(button)
            );
        IPython.keyboard_manager.register_events(text);
    };

    var tag_dialog = function(cell, on_add, on_remove) {
        var tag_list = cell.metadata.tags || [];

        var message =
            i18n.msg._("Edit the list of tags below. All whitespace " +
            "is treated as tag separators.");

        var textarea = $('<textarea/>')
            .attr('aria-label', i18n.msg._('Edit the tags in the text area'))
            .attr('rows', '13')
            .attr('cols', '80')
            .attr('name', 'tags')
            .text(tag_list.join('\n'));

        var dialogform = $('<div/>').attr('title', i18n.msg._('Edit the tags'))
            .append(
                $('<form/>').append(
                    $('<fieldset/>').append(
                        $('<label/>')
                        .attr('for','tags')
                        .text(message)
                        )
                    .append($('<br/>'))
                    .append(textarea)
                    )
            );

        var modal_obj = dialog.modal({
            title: i18n.msg._("Edit Tags"),
            body: dialogform,
            default_button: "Cancel",
            buttons: {
                Cancel: {},
                Edit: { class : "btn-primary",
                    click: function() {
                        var old_tags = cell.metadata.tags || [];
                        var new_tags = preprocess_input(textarea[0].value);
                        var added_tags = array_difference(new_tags, old_tags);
                        var removed_tags = array_difference(old_tags, new_tags);
                        for (var i=0; i < added_tags.length; ++i) {
                            on_add(added_tags[i]);
                        }
                        for (var i=0; i < removed_tags.length; ++i) {
                            on_remove(removed_tags[i]);
                        }
                    }
                }
            },
            notebook: cell.notebook,
            keyboard_manager: cell.keyboard_manager,
        });
    };

    var add_dialog_button = function(container, cell, on_add, on_remove) {
        var button = $('<button />')
            .addClass('btn btn-default btn-xs tags-dialog-btn')
            .text('...')
            .click( function() {
              tag_dialog(cell, on_add, on_remove);
              return false;
            });
        container.append(button);
    };

    var add_tags_cellbar = function(div, cell) {
        var button_container = $(div);

        button_container.addClass('tags_button_container');

        var tag_container = $('<span/>').
            addClass('tag-container');
        var on_remove = remove_tag(cell, tag_container);
        var ok = init_tag_container(cell, tag_container, on_remove);
        if (!ok) {
            return;
        }
        button_container.append(tag_container);

        var on_add = add_tag(cell, tag_container, on_remove);
        if(cell.is_editable()){
            add_tag_edit(div, cell, on_add, on_remove);
        }
    };

    var register = function(notebook) {
      CellToolbar.register_callback('tags.edit', add_tags_cellbar);

      var tags_preset = [];
      tags_preset.push('tags.edit');

      CellToolbar.register_preset('Tags', tags_preset, notebook);

    };
    return {'register' : register};
});
