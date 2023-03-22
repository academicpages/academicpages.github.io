// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'notebook/js/celltoolbar',
    'base/js/dialog',
    'base/js/keyboard',
    'base/js/i18n'
], function(celltoolbar, dialog, keyboard, i18n) {
    "use strict";

  var CellToolbar = celltoolbar.CellToolbar;
  var raw_cell_preset = [];

  var select_type = CellToolbar.utils.select_ui_generator([
    [i18n.msg._("None"), "-"],
    ["LaTeX", "text/latex"],
    ["reST", "text/restructuredtext"],
    ["HTML", "text/html"],
    ["Markdown", "text/markdown"],
    ["Python", "text/x-python"],
    [i18n.msg._("Custom"), "dialog"],

    ],
      // setter
      function(cell, value) {
        if (value === "-") {
          delete cell.metadata.raw_mimetype;
        } else if (value === 'dialog') {
            var message =
                i18n.msg._("Set the MIME type of the raw cell:");

            var mimeinput = $('<input/>')
                .attr('type', 'text')
                .attr('size', '25')
                .attr('name', 'mimetype')
                .val(cell.metadata.raw_mimetype || "-");

            var dialogform = $('<div/>').attr('title', i18n.msg._("Edit MIME type"))
                .append(
                    $('<form/>').append(
                        $('<fieldset/>').append(
                            $('<label/>')
                            .attr('for', 'mimetype')
                            .text(message)
                            )
                        .append($('<br/>'))
                        .append(mimeinput)
                        )
                );

            dialog.modal({
                title: i18n.msg._("Raw Cell MIME Type"),
                body: dialogform,
                buttons : {
                    Cancel: {},
                    OK: {
                        class: "btn-primary",
                        click: function () {
                            console.log(cell);
                            cell.metadata.raw_mimetype = $(this).find('input').val();
                            console.log(cell.metadata);
                        }
                    }
                },
                notebook: cell.notebook,
                keyboard_manager: cell.keyboard_manager,
                open : function (event, ui) {
                    var that = $(this);
                    // Upon ENTER, click the OK button.
                    that.find('input[type="text"]').keydown(function (event, ui) {
                        if (event.which === keyboard.keycodes.enter) {
                            that.find('.btn-primary').first().click();
                            return false;
                        }
                    });
                    that.find('input[type="text"]').focus().select();
                }
            });
        } else {
          cell.metadata.raw_mimetype = value;
        }
      },
      //getter
      function(cell) {
        return cell.metadata.raw_mimetype || "";
      },
      // name
      i18n.msg._("Raw NBConvert Format")
  );

  var register = function (notebook) {
    CellToolbar.register_callback('raw_cell.select', select_type, ['raw']);
    raw_cell_preset.push('raw_cell.select');

    CellToolbar.register_preset(i18n.msg._('Raw Cell Format'), raw_cell_preset, notebook);
  };
  return {'register': register};

});
