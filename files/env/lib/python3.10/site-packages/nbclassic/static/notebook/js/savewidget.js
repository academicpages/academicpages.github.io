// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
    'base/js/keyboard',
    'moment',
    'bidi/bidi',
], function($, utils, i18n, dialog, keyboard, moment, bidi) {
    "use strict";

    var SaveWidget = function (selector, options) {
        /**
         * TODO: Remove circular ref.
         */
        this.notebook = undefined;
        this.selector = selector;
        this.events = options.events;
        this._checkpoint_date = undefined;
        this.keyboard_manager = options.keyboard_manager;
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.bind_events();
        }
    };


    SaveWidget.prototype.bind_events = function () {
        var that = this;
        this.element.find('span.filename').click(function () {
            that.rename_notebook({notebook: that.notebook});
        });
        this.events.on('notebook_loaded.Notebook', function () {
            that.update_notebook_name();
            that.update_document_title();
        });
        this.events.on('notebook_saved.Notebook', function () {
            that.update_notebook_name();
            that.update_document_title();
        });
        this.events.on('notebook_renamed.Notebook', function () {
            that.update_notebook_name();
            that.update_document_title();
            that.update_address_bar();
        });
        this.events.on('notebook_save_failed.Notebook', function () {
            that.set_save_status(i18n.msg._('Autosave Failed!'));
        });
        this.events.on('notebook_read_only.Notebook', function () {
            that.set_save_status('(read only)');
            // disable future set_save_status
            that.set_save_status = function () {};
        });
        this.events.on('checkpoints_listed.Notebook', function (event, data) {
            that._set_last_checkpoint(data[0]);
        });

        this.events.on('checkpoint_created.Notebook', function (event, data) {
            that._set_last_checkpoint(data);
        });
        this.events.on('set_dirty.Notebook', function (event, data) {
            that.set_autosaved(data.value);
        });
    };

    // This statement is used simply so that message extraction
    // will pick up the strings.  The actual setting of the text
    // for the button is in dialog.js.
    var button_labels = [ i18n.msg._("Cancel"), i18n.msg._("Rename"), i18n.msg._("OK")];

    SaveWidget.prototype.rename_notebook = function (options) {
        options = options || {};
        var that = this;
        var dialog_body = $('<div/>').append(
            $("<p/>").addClass("rename-message")
                .text(i18n.msg._('Enter a new notebook name:'))
        ).append(
            $("<br/>")
        ).append(
            $('<input/>').attr('type','text').attr('size','25').addClass('form-control')
            .val(options.notebook.get_notebook_name())
        );
        var d = dialog.modal({
            title: i18n.msg._("Rename Notebook"),
            body: dialog_body,
            notebook: options.notebook,
            keyboard_manager: this.keyboard_manager,
            default_button: "Cancel",
            buttons : {
                "Cancel": {},
                "Rename": {
                    class: "btn-primary",
                    click: function () {
                        var new_name = d.find('input').val();
                        if (!options.notebook.test_notebook_name(new_name)) {
                            d.find('.rename-message').text(i18n.msg._(
                                "Invalid notebook name. Notebook names must have 1 or more characters and can contain any characters except :/\\. Please enter a new notebook name:")
                            );
                            return false;
                        } else {
                            d.find('.rename-message').text(i18n.msg._("Renaming..."));
                            d.find('input[type="text"]').prop('disabled', true);
                            that.notebook.rename(new_name).then(
                                function () {
                                    d.modal('hide');
                                }, function (error) {
                                    d.find('.rename-message').text(error.message || i18n.msg._('Unknown error'));
                                    d.find('input[type="text"]').prop('disabled', false).focus().select();
                                }
                            );
                            return false;
                        }
                    }
                }
            },
            open : function () {
                /**
                 * Upon ENTER, click the OK button.
                 */
                d.find('input[type="text"]').keydown(function (event) {
                    if (event.which === keyboard.keycodes.enter) {
                        d.find('.btn-primary').first().click();
                        return false;
                    }
                });
                d.find('input[type="text"]').focus().select();
            }
        });
    };


    SaveWidget.prototype.update_notebook_name = function () {
        var nbname = this.notebook.get_notebook_name();
        nbname = bidi.applyBidi(nbname);
        this.element.find('span.filename').text(nbname);
    };


    SaveWidget.prototype.update_document_title = function () {
        var nbname = this.notebook.get_notebook_name();
        document.title = nbname + ' - Jupyter Notebook';
    };

    SaveWidget.prototype.update_address_bar = function(){
        var base_url = this.notebook.base_url;
        var path = this.notebook.notebook_path;
        var state = {path : path};
        window.history.replaceState(state, "", utils.url_path_join(
            base_url,
            "notebooks",
            utils.encode_uri_components(path))
        );
    };


    SaveWidget.prototype.set_save_status = function (msg) {
        this.element.find('span.autosave_status').text(msg);
    };

    SaveWidget.prototype._set_last_checkpoint = function (checkpoint) {
        if (checkpoint) {
            this._checkpoint_date = new Date(checkpoint.last_modified);
        } else {
            this._checkpoint_date = null;
        }
        this._render_checkpoint();
    };
    
    SaveWidget.prototype._render_checkpoint = function () {
        /** actually set the text in the element, from our _checkpoint value
        
        called directly, and periodically in timeouts.
        */
        this._schedule_render_checkpoint();
        var el = this.element.find('span.checkpoint_status');
        if (!this._checkpoint_date) {
            el.text('').attr('title', i18n.msg._('no checkpoint'));
            return;
        }
        var chkd = moment(this._checkpoint_date);
        var long_date = chkd.format('llll');
        var human_date;
        var tdelta = Math.ceil(new Date() - this._checkpoint_date);
        if (tdelta < utils.time.milliseconds.d){
            // less than 24 hours old, use relative date
            human_date = chkd.fromNow();
        } else {
            // otherwise show calendar
            // <Today | yesterday|...> at hh,mm,ss
            human_date = chkd.calendar();
        }
        
        el.text(i18n.msg.sprintf(i18n.msg._('Last Checkpoint: %s'),human_date)).attr('title', long_date);
    };

    
    SaveWidget.prototype._schedule_render_checkpoint = function () {
        /** schedule the next update to relative date
        
        periodically updated, so short values like 'a few seconds ago' don't get stale.
        */
        if (!this._checkpoint_date) {
            return;
        }
        if ((this._checkpoint_timeout)) {
            clearTimeout(this._checkpoint_timeout);
        }
        var dt = Math.ceil(new Date() - this._checkpoint_date);
        this._checkpoint_timeout = setTimeout(
            $.proxy(this._render_checkpoint, this),
            utils.time.timeout_from_dt(dt)
        );
    };

    SaveWidget.prototype.set_autosaved = function (dirty) {
        if (dirty) {
            this.set_save_status(i18n.msg._("(unsaved changes)"));
        } else {
            this.set_save_status(i18n.msg._("(autosaved)"));
        }
    };

    return {'SaveWidget': SaveWidget};

});
