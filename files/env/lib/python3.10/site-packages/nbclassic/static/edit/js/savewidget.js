// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/dialog',
    'base/js/keyboard',
    'moment',
    'bidi/bidi',
], function($, utils, dialog, keyboard, moment, bidi) {
    "use strict";
    
    var SaveWidget = function (selector, options) {
        this.editor = undefined;
        this.selector = selector;
        this.events = options.events;
        this.editor = options.editor;
        this._last_modified = undefined;
        this._filename = undefined;
        this.keyboard_manager = options.keyboard_manager;
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.bind_events();
        }
    };


    SaveWidget.prototype.bind_events = function () {
        var that = this;
        this.element.find('span.filename').click(function () {
            that.rename();
        });
        this.events.on('save_status_clean.Editor', function (evt) {
            that.update_document_title();
        });
        this.events.on('save_status_dirty.Editor', function (evt) {
            that.update_document_title(undefined, true);
        });
        this.events.on('file_loaded.Editor', function (evt, model) {
            that.update_filename(model.name);
            that.update_document_title(model.name);
            that.update_last_modified(model.last_modified);
        });
        this.events.on('file_saved.Editor', function (evt, model) {
            that.update_filename(model.name);
            that.update_document_title(model.name);
            that.update_last_modified(model.last_modified);
        });
        this.events.on('file_renamed.Editor', function (evt, model) {
            that.update_filename(model.name);
            that.update_document_title(model.name);
            that.update_address_bar(model.path);
        });
        this.events.on('file_save_failed.Editor', function () {
            that.set_save_status('Save Failed!');
        });
    };


    SaveWidget.prototype.rename = function (options) {
        options = options || {};
        var that = this;
        var dialog_body = $('<div/>').append(
            $("<p/>").addClass("rename-message")
                .text('Enter a new filename:')
        ).append(
            $("<br/>")
        ).append(
            $('<input/>').attr('type','text').attr('size','25').addClass('form-control')
            .val(that.editor.get_filename())
        );
        var d = dialog.modal({
            title: "Rename File",
            body: dialog_body,
            default_button: "Cancel",
            buttons : {
                "Cancel": {},
                "OK": {
                    class: "btn-primary",
                    click: function () {
                        var new_name = d.find('input').val();
                        if (!new_name) {
                            // Reset the message
                            d.find('.rename-message').text("Enter a new filename:");
                            return false;
                        }
                        d.find('.rename-message').text("Renaming...");
                        d.find('input[type="text"]').prop('disabled', true);
                        that.editor.rename(new_name).then(
                            function () {
                                d.modal('hide');
                            }, function (error) {
                                d.find('.rename-message').text(error.message || 'Unknown error');
                                d.find('input[type="text"]').prop('disabled', false).focus().select();
                            }
                        );
                        return false;
                    }
                }
            },
            open : function () {
                // Upon ENTER, click the OK button.
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


    SaveWidget.prototype.update_filename = function (filename) {
    	filename = bidi.applyBidi(filename);
        this.element.find('span.filename').text(filename);
    };

    SaveWidget.prototype.update_document_title = function (filename, dirty) {
        if(filename){
            this._filename = filename;
        }
        document.title = (dirty ? '*' : '') + this._filename + ' - Jupyter Text Editor';
    };

    SaveWidget.prototype.update_address_bar = function (path) {
        var state = {path : path};
        window.history.replaceState(state, "", utils.url_path_join(
            this.editor.base_url,
            "edit",
            utils.encode_uri_components(path)
        ));
    };

    SaveWidget.prototype.update_last_modified = function (last_modified) {
        if (last_modified) {
            this._last_modified = new Date(last_modified);
        } else {
            this._last_modified = null;
        }
        this._render_last_modified();
    };
    
    SaveWidget.prototype._render_last_modified = function () {
        /** actually set the text in the element, from our _last_modified value
        
        called directly, and periodically in timeouts.
        */
        this._schedule_render_last_modified();
        var el = this.element.find('span.last_modified');
        if (!this._last_modified) {
            el.text('').attr('title', 'never saved');
            return;
	 }
        var chkd = moment(this._last_modified);
        var long_date = chkd.format('llll');
        var human_date;
        var tdelta = Math.ceil(new Date() - this._last_modified);
        if (tdelta < utils.time.milliseconds.d){
            // less than 24 hours old, use relative date
            human_date = chkd.fromNow();
        } else {
            // otherwise show calendar
            // <Today | yesterday|...> at hh,mm,ss
            human_date = chkd.calendar();
        }
        el.text(human_date).attr('title', long_date);
    };
    
    SaveWidget.prototype._schedule_render_last_modified = function () {
        /** schedule the next update to relative date
        
        periodically updated, so short values like 'a few seconds ago' don't get stale.
        */
        if (!this._last_modified) {
            return;
        }
        if ((this._last_modified_timeout)) {
            clearTimeout(this._last_modified_timeout);
        }
        var dt = Math.ceil(new Date() - this._last_modified);
        this._last_modified_timeout = setTimeout(
            $.proxy(this._render_last_modified, this),
            utils.time.timeout_from_dt(dt)
        );
    };

    return {'SaveWidget': SaveWidget};

});
