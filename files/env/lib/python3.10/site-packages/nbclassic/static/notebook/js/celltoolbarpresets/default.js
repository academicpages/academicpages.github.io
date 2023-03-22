// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'notebook/js/celltoolbar',
    'base/js/dialog',
    'base/js/i18n'
], function(celltoolbar, dialog, i18n) {
    "use strict";

    var CellToolbar = celltoolbar.CellToolbar;

    var raw_edit = function (cell , edit_metadata_button) {
        dialog.edit_metadata({
            md: cell.metadata,
            callback: function (md) {
                cell.metadata = md;
            },
            name: i18n.msg._('Cell'),
            notebook: this.notebook,
            keyboard_manager: this.keyboard_manager,
            edit_metadata_button: edit_metadata_button
        });
    };

    var add_raw_edit_button = function(div, cell) {
        var button_container = $(div);
        var button = $('<button/>')
            .addClass("btn btn-default btn-xs")
            .text(i18n.msg._("Edit Metadata"))
            .click( function () {
                raw_edit(cell, this);
                return false;
            });

        button_container.append(button);
    };

    var register = function (notebook) {
        CellToolbar.register_callback('default.rawedit', add_raw_edit_button);
        raw_edit = $.proxy(raw_edit, {
            notebook: notebook,
            keyboard_manager: notebook.keyboard_manager
        });

        var example_preset = [];
        example_preset.push('default.rawedit');

        CellToolbar.register_preset(i18n.msg._('Edit Metadata'), example_preset, notebook);
    };
    return {'register': register};
});
