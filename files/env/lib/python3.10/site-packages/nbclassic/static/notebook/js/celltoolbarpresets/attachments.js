// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'notebook/js/celltoolbar',
    'base/js/dialog',
    'base/js/i18n'
], function(celltoolbar, dialog, i18n) {
    "use strict";

    var CellToolbar = celltoolbar.CellToolbar;

    var edit_attachments_dialog = function(cell) {
        dialog.edit_attachments({
          attachments: cell.attachments,
          callback: function(attachments) {
            cell.attachments = attachments;
            // Force cell refresh
            cell.unrender();
            cell.render();
          },
          name: 'Cell',
          notebook: cell.notebook,
          keyboard_manager: cell.keyboard_manager
        });
    };

    var add_dialog_button = function(div, cell) {
        var button_container = $(div);
        var button = $('<button />')
            .addClass('btn btn-default btn-xs')
            .text(i18n.msg._('Edit Attachments'))
            .click( function() {
              edit_attachments_dialog(cell);
              return false;
            });
        button_container.append(button);
    };

    var register = function(notebook) {
      CellToolbar.register_callback('attachments.edit', add_dialog_button);

      var attachments_preset = [];
      attachments_preset.push('attachments.edit');

      CellToolbar.register_preset(i18n.msg._('Attachments'), attachments_preset, notebook);

    };
    return {'register' : register};
});
