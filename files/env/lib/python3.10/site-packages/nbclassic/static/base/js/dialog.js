// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['jquery',
    'codemirror/lib/codemirror',
    'bootstrap',
	'base/js/i18n'],
	function($, CodeMirror, bs, i18n) {
    "use strict";

    /**
     * A wrapper around bootstrap modal for easier use
     * Pass it an option dictionary with the following properties:
     *
     *    - body : <string> or <DOM node>, main content of the dialog
     *            if pass a <string> it will be wrapped in a p tag and
     *            html element escaped, unless you specify sanitize=false
     *            option.
     *    - title : Dialog title, default to empty string.
     *    - buttons : dict of btn_options who keys are button label.
     *            see btn_options below for description
     *    - open : callback to trigger on dialog open.
     *    - destroy:
     *    - notebook : notebook instance
     *    - keyboard_manager: keyboard manager instance.
     *
     *  Unlike bootstrap modals, the backdrop options is set by default 
     *  to 'static'.
     *
     *  The rest of the options are passed as is to bootstrap modals. 
     *
     *  btn_options: dict with the following property:
     *  
     *    - click : callback to trigger on click
     *    - class : css classes to add to button.
     *
     *
     *
     **/
    var modal = function (options) {

        var modal = $("<div/>")
            .addClass("modal")
            .addClass("fade")
            .attr("role", "dialog");
        var dialog = $("<div/>")
            .addClass("modal-dialog")
            .appendTo(modal);
        var dialog_content = $("<div/>")
            .addClass("modal-content")
            .appendTo(dialog);
        if(typeof(options.body) === 'string' && options.sanitize !== false){
            options.body = $("<p/>").text(options.body);
        }
        dialog_content.append(
            $("<div/>")
                .addClass("modal-header")
                .mousedown(function() {
                  $(".modal").draggable({handle: '.modal-header'});
                })
                .append($("<button>")
                    .attr("type", "button")
                    .attr("aria-label", i18n.msg._("close"))
                    .addClass("close")
                    .attr("data-dismiss", "modal")
                    .attr("aria-hidden", "true")
                    .html("&times;")
                ).append(
                    $("<h4/>")
                        .addClass('modal-title')
                        .text(options.title || "")
                )
        ).append(
            $("<div/>")
                .addClass("modal-body")
                .append(
                    options.body || $("<p/>")
                )
        );
        
        var footer = $("<div/>").addClass("modal-footer");
        
        var default_button;
        
        for (var label in options.buttons) {
            var btn_opts = options.buttons[label];
            var button = $("<button/>")
                .addClass("btn btn-default btn-sm")
                .attr("data-dismiss", "modal")
                .text(i18n.msg.translate(label).fetch());
            if (btn_opts.id) {
                button.attr('id', btn_opts.id);
            }
            if (btn_opts.click) {
                button.click($.proxy(btn_opts.click, dialog_content));
            }
            if (btn_opts.class) {
                button.addClass(btn_opts.class);
            }
            footer.append(button);
            if (options.default_button && label === options.default_button) {
                default_button = button;
            }
        }
        if (!options.default_button) {
            default_button = footer.find("button").last();
        }
        dialog_content.append(footer);
        // hook up on-open event
        modal.on("shown.bs.modal", function () {
            setTimeout(function () {
                default_button.focus();
                if (options.open) {
                    $.proxy(options.open, modal)();
                }
            }, 0);
        });
        
        // destroy modal on hide, unless explicitly asked not to
        if (options.destroy === undefined || options.destroy) {
            modal.on("hidden.bs.modal", function () {
                modal.remove();
            });
        }
        modal.on("hidden.bs.modal", function () {
            if (options.notebook) {
                var cell = options.notebook.get_selected_cell();
                if (cell) cell.select();
            }
            if (options.keyboard_manager) {
                options.keyboard_manager.enable();
                options.keyboard_manager.command_mode();
            }
	    if (options.focus_button) {
            	$(options.focus_button).focus();
	    }
        });
        
        if (options.keyboard_manager) {
            options.keyboard_manager.disable();
        }
        
        if(options.backdrop === undefined){
          options.backdrop = 'static';
        }
        
        return modal.modal(options);
    };

    var kernel_modal = function (options) {
        /**
         * only one kernel dialog should be open at a time -- but
         * other modal dialogs can still be open
         */
        $('.kernel-modal').modal('hide');
        var dialog = modal(options);
        dialog.addClass('kernel-modal');
        return dialog;
    };

    var edit_metadata = function (options) {
        options.name = options.name || "Cell";
        var error_div = $('<div/>').css('color', 'red');
        var message_cell = 
            i18n.msg._("Manually edit the JSON below to manipulate the metadata for this cell.");
        var message_notebook = 
            i18n.msg._("Manually edit the JSON below to manipulate the metadata for this notebook.");
        var message_end = 
            i18n.msg._(" We recommend putting custom metadata attributes in an appropriately named substructure," +
            " so they don't conflict with those of others.");

        var message;
        if (options.name === 'Notebook') {
        	message = message_notebook + message_end;
        } else {
        	message = message_cell + message_end;
        }
        var textarea = $('<textarea/>')
            .attr('rows', '13')
            .attr('cols', '80')
            .attr('name', 'metadata')
            .text(JSON.stringify(options.md || {}, null, 2));
        
        var dialogform = $('<div/>').attr('title', i18n.msg._('Edit the metadata'))
            .append(
                $('<form/>').append(
                    $('<fieldset/>').append(
                        $('<label/>')
                        .attr('for','metadata')
                        .text(message)
                        )
                        .append(error_div)
                        .append($('<br/>'))
                        .append(textarea)
                    )
            );
        var editor = CodeMirror.fromTextArea(textarea[0], {
            lineNumbers: true,
            matchBrackets: true,
            indentUnit: 2,
            autoIndent: true,
            mode: 'application/json',
        });
        var title_msg;
        if (options.name === "Notebook") {
        	title_msg = i18n.msg._("Edit Notebook Metadata");
        } else {
        	title_msg = i18n.msg._("Edit Cell Metadata");
        }
        // This statement is used simply so that message extraction
        // will pick up the strings.
        var button_labels = [ i18n.msg._("Cancel"), i18n.msg._("Edit"), i18n.msg._("OK"), i18n.msg._("Apply")];
        var modal_obj = modal({
            title: title_msg,
            body: dialogform,
            default_button: "Cancel",
            buttons: {
                Cancel: {},
                Edit: { class : "btn-primary",
                    click: function() {
                        /**
                         * validate json and set it
                         */
                        var new_md;
                        try {
                            new_md = JSON.parse(editor.getValue());
                        } catch(e) {
                            console.log(e);
                            error_div.text(i18n.msg._('WARNING: Could not save invalid JSON.'));
                            return false;
                        }
                        options.callback(new_md);
                        options.notebook.apply_directionality();
                    }
                }
            },
            notebook: options.notebook,
            keyboard_manager: options.keyboard_manager,
        });

        modal_obj.on('shown.bs.modal', function(){ editor.refresh(); });
        modal_obj.on('hide.bs.modal', function(){
            options.edit_metadata_button ? options.edit_metadata_button.focus() : "";});
    };

    var edit_attachments = function (options) {
        // This shows the Edit Attachments dialog. This dialog allows the
        // user to delete attachments. We show a list of attachments to
        // the user and he can mark some of them for deletion. The deletion
        // is applied when the 'Apply' button of this dialog is pressed.
        var message;
        var attachments_list;
        if (Object.keys(options.attachments).length == 0) {
            message = i18n.msg._("There are no attachments for this cell.");
            attachments_list = $('<div>');
        } else {
            message = i18n.msg._("Current cell attachments");

            attachments_list = $('<div>')
                .addClass('list_container')
                .append(
                    $('<div>')
                    .addClass('row list_header')
                    .append(
                        $('<div>')
                        .text(i18n.msg._('Attachments'))
                    )
                );

            // This is a set containing keys of attachments to be deleted when
            // the Apply button is clicked
            var to_delete = {};

            var refresh_attachments_list = function() {
                $(attachments_list).find('.row').remove();
                for (var key in options.attachments) {
                    var mime = Object.keys(options.attachments[key])[0];
                    var deleted = key in to_delete;

                    // This ensures the current value of key is captured since
                    // javascript only has function scope
                    var btn;
                    // Trash/restore button
                    (function(){
                        var _key = key;
                        btn = $('<button>')
                            .addClass('btn btn-default btn-xs')
                            .css('display', 'inline-block');
                        if (deleted) {
                            btn.attr('title', i18n.msg._('Restore'))
                               .append(
                                   $('<i>')
                                   .addClass('fa fa-plus')
                               );
                            btn.click(function() {
                                delete to_delete[_key];
                                refresh_attachments_list();
                            });
                        } else {
                            btn.attr('title', i18n.msg._('Delete'))
                               .addClass('btn-danger')
                               .append(
                                   $('<i>')
                                   .addClass('fa fa-trash')
                               );
                            btn.click(function() {
                                to_delete[_key] = true;
                                refresh_attachments_list();
                            });
                        }
                        return btn;
                    })();
                    var row = $('<div>')
                        .addClass('col-md-12 att_row')
                        .append(
                            $('<div>')
                            .addClass('row')
                            .append(
                                $('<div>')
                                .addClass('att-name col-xs-4')
                                .text(key)
                            )
                            .append(
                                $('<div>')
                                .addClass('col-xs-4 text-muted')
                                .text(mime)
                            )
                            .append(
                                $('<div>')
                                .addClass('item-buttons pull-right')
                                .append(btn)
                            )
                        );
                    if (deleted) {
                        row.find('.att-name')
                           .css('text-decoration', 'line-through');
                    }

                    attachments_list.append($('<div>')
                        .addClass('list_item row')
                        .append(row)
                    );
                }
            };
            refresh_attachments_list();
        }

        var dialogform = $('<div/>')
            .attr('title', i18n.msg._('Edit attachments'))
            .append(message)
            .append('<br />')
            .append(attachments_list);
        var title_msg;
        if ( options.name === "Notebook" ) {
        	title_msg = i18n.msg._("Edit Notebook Attachments");
        } else {
        	title_msg = i18n.msg._("Edit Cell Attachments");
        }
        var modal_obj = modal({
            title: title_msg,
            body: dialogform,
            buttons: {
                Apply: { class : "btn-primary",
                    click: function() {
                        for (var key in to_delete) {
                            delete options.attachments[key];
                        }
                        options.callback(options.attachments);
                    }
                },
                Cancel: {}
            },
            notebook: options.notebook,
            keyboard_manager: options.keyboard_manager,
        });
    };

    var insert_image = function (options) {
        var message =
            i18n.msg._("Select a file to insert.");
        var file_input = $('<input/>')
            .attr('type', 'file')
            .attr('accept', 'image/*')
            .attr('name', 'file')
            .on('change', function(file) {
                var $btn = $(modal_obj).find('#btn_ok');
                if (this.files.length > 0) {
                    $btn.removeClass('disabled');
                } else {
                    $btn.addClass('disabled');
                }
            });
        var dialogform = $('<div/>').attr('title', i18n.msg._('Edit attachments'))
            .append(
                $('<form id="insert-image-form" />').append(
                    $('<fieldset/>').append(
                        $('<label/>')
                        .attr('for','file')
                        .text(message)
                        )
                        .append($('<br/>'))
                        .append(file_input)
                    )
            );
        var modal_obj = modal({
            title: i18n.msg._("Select a file"),
            body: dialogform,
            buttons: {
                OK: {
                    id : 'btn_ok',
                    class : "btn-primary disabled",
                    click: function() {
                        options.callback(file_input[0].files[0]);
                    }
                },
                Cancel: {}
            },
            notebook: options.notebook,
            keyboard_manager: options.keyboard_manager,
        });
    };

    
    var dialog = {
        modal : modal,
        kernel_modal : kernel_modal,
        edit_metadata : edit_metadata,
        edit_attachments : edit_attachments,
        insert_image : insert_image
    };

    return dialog;
});
