// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
    'codemirror/lib/codemirror',
    'codemirror/mode/meta',
    'codemirror/addon/comment/comment',
    'codemirror/addon/dialog/dialog',
    'codemirror/addon/edit/closebrackets',
    'codemirror/addon/edit/matchbrackets',
    'codemirror/addon/search/searchcursor',
    'codemirror/addon/search/search',
    'codemirror/keymap/emacs',
    'codemirror/keymap/sublime',
    'codemirror/keymap/vim',
    ],
function(
    $,
    utils,
    i18n,
    dialog,
    CodeMirror
) {
    "use strict";

    var Editor = function(selector, options) {
        var that = this;
        this.selector = selector;
        this.clean = false;
        this.contents = options.contents;
        this.events = options.events;
        this.base_url = options.base_url;
        this.file_path = options.file_path;
        this.config = options.config;
        this.file_extension_modes = options.file_extension_modes || {};
        this.last_modified = null;
        this._changed_on_disk_dialog = null;

        this.codemirror = new CodeMirror($(this.selector)[0]);
        this.codemirror.on('changes', function(cm, changes){
            that._clean_state();
        });
        this.generation = -1;
        
        // It appears we have to set commands on the CodeMirror class, not the
        // instance. I'd like to be wrong, but since there should only be one CM
        // instance on the page, this is good enough for now.
        CodeMirror.commands.save = $.proxy(this.save, this);
        
        this.save_enabled = false;
        
        this.config.loaded.then(function () {
            // load codemirror config
            var cfg = that.config.data.Editor || {};
            var cmopts = $.extend(true, {}, // true = recursive copy
                Editor.default_codemirror_options,
                cfg.codemirror_options || {}
            );
            that._set_codemirror_options(cmopts);
            that.events.trigger('config_changed.Editor', {config: that.config});
            if (cfg.file_extension_modes) {
                // check for file extension in user preferences
                var modename = cfg.file_extension_modes[that._get_file_extension()];
                if (modename) {
                    var modeinfo = CodeMirror.findModeByName(modename);
                    if (modeinfo) {
                        that.set_codemirror_mode(modeinfo);
                    }
                }
            }
            that._clean_state();
        });
        this.clean_sel = $('<div/>');
        $('.last_modified').before(this.clean_sel);
        this.clean_sel.addClass('dirty-indicator-dirty');
    };
    
    // default CodeMirror options
    Editor.default_codemirror_options = {
        extraKeys: {
            "Cmd-Right": "goLineRight",
            "End": "goLineRight",
            "Cmd-Left": "goLineLeft",
            "Tab": "indentMore",
            "Shift-Tab" : "indentLess",
            "Cmd-/" : "toggleComment",
            "Ctrl-/" : "toggleComment",
        },
        indentUnit: 4,
        theme: "ipython",
        lineNumbers: true,
        lineWrapping: true
    };
    
    Editor.prototype.load = function() {
        /** load the file */
        var that = this;
        var cm = this.codemirror;
        return this.contents.get(this.file_path, {type: 'file', format: 'text'})
            .then(function(model) {
                cm.setValue(model.content);

                // Setting the file's initial value creates a history entry,
                // which we don't want.
                cm.clearHistory();
                that._set_mode_for_model(model);
                that.save_enabled = true;
                that.generation = cm.changeGeneration();
                that.events.trigger("file_loaded.Editor", model);
                that._clean_state();
                that.last_modified = new Date(model.last_modified);
            }).catch(
            function(error) {
                that.events.trigger("file_load_failed.Editor", error);
                console.warn('Error loading: ', error);
                cm.setValue("Error! " + error.message +
                                "\nSaving disabled.\nSee Console for more details.");
                cm.setOption('readOnly','nocursor');
                that.save_enabled = false;
            }
        );
    };
    
    Editor.prototype._set_mode_for_model = function (model) {
        /** Set the CodeMirror mode based on the file model */

        // Find and load the highlighting mode,
        // first by mime-type, then by file extension

        var modeinfo;
        var ext = this._get_file_extension();
        if (ext) {
            // check if a mode has been remembered for this extension
            var modename = this.file_extension_modes[ext];
            if (modename) {
                modeinfo = CodeMirror.findModeByName(modename);
            }
        }
        // prioritize CodeMirror's filename identification
        if (!modeinfo || modeinfo.mode === "null") {
            modeinfo = CodeMirror.findModeByFileName(model.name);
            // codemirror's filename identification is case-sensitive.
            // try once more with lowercase extension
            if (!modeinfo && ext) {
                // CodeMirror wants lowercase ext without leading '.'
                modeinfo = CodeMirror.findModeByExtension(ext.slice(1).toLowerCase());
            }
        }
        if (model.mimetype && (!modeinfo || modeinfo.mode === "null")) {
            // mimetype is not set on file rename
            modeinfo = CodeMirror.findModeByMIME(model.mimetype);
        }
        if (modeinfo) {
            this.set_codemirror_mode(modeinfo);
        }
    };

    Editor.prototype.set_codemirror_mode = function (modeinfo) {
        /** set the codemirror mode from a modeinfo struct */
        var that = this;
        utils.requireCodeMirrorMode(modeinfo, function () {
            that.codemirror.setOption('mode', modeinfo.mime);
            that.events.trigger("mode_changed.Editor", modeinfo);
        }, function(err) {
            console.log('Error getting CodeMirror mode: ' + err);
        });
    };

    Editor.prototype.save_codemirror_mode = function (modeinfo) {
        /** save the selected codemirror mode for the current extension in config */
        var update_mode_map = {};
        var ext = this._get_file_extension();
        // no extension, nothing to save
        // TODO: allow remembering no-extension things like Makefile?
        if (!ext) return;

        update_mode_map[ext] = modeinfo.name;
        return this.config.update({
            Editor: {
                file_extension_modes: update_mode_map,
            }
        });
    };

    Editor.prototype.get_filename = function () {
        return utils.url_path_split(this.file_path)[1];
    };

    Editor.prototype._get_file_extension = function () {
        /** return file extension *including* . 
        
        Returns undefined if no extension is found.
        */
        var filename = this.get_filename();
        var ext_idx = filename.lastIndexOf('.');
        if (ext_idx < 0) {
            return;
        } else {
            return filename.slice(ext_idx);
        }
    };

    /**
     * Rename the file.
     * @param  {string} new_name
     * @return {Promise} promise that resolves when the file is renamed.
     */
    Editor.prototype.rename = function (new_name) {
        /** rename the file */
        var that = this;
        var parent = utils.url_path_split(this.file_path)[0];
        var new_path = utils.url_path_join(parent, new_name);
        return this.contents.rename(this.file_path, new_path).then(
            function (model) {
                that.file_path = model.path;
                that.events.trigger('file_renamed.Editor', model);
                that.last_modified = new Date(model.last_modified);
                that._set_mode_for_model(model);
                that._clean_state();
            }
        );
    };
    

    /**
     * Save this file on the server.
     *
     * @param {boolean} check_last_modified - checks if file has been modified on disk
     * @return {Promise} - promise that resolves when the notebook is saved.
     */
    Editor.prototype.save = function (check_last_modified) {
        /** save the file */
        if (!this.save_enabled) {
            console.log("Not saving, save disabled");
            return;
        }

        // used to check for last modified saves
        if (check_last_modified === undefined) {
            check_last_modified = true;
        }

        var model = {
            path: this.file_path,
            type: 'file',
            format: 'text',
            content: this.codemirror.getValue(),
        };
        var that = this;

        var _save = function () {
            that.events.trigger("file_saving.Editor");
            return that.contents.save(that.file_path, model).then(function(data) {
                // record change generation for isClean
                that.generation = that.codemirror.changeGeneration();
                that.events.trigger("file_saved.Editor", data);
                that.last_modified = new Date(data.last_modified);
                that._clean_state();
            });
        };

        /* 
         * Gets the current working file, and checks if the file has been modified on disk. If so, it
         * creates & opens a modal that issues the user a warning and prompts them to overwrite the file.
         * 
         * If it can't get the working file, it builds a new file and saves.
         */ 
        if (check_last_modified) {
            return this.contents.get(that.file_path, {content: false}).then(
                function check_if_modified(data) {
                    var last_modified = new Date(data.last_modified);
                    // We want to check last_modified (disk) > that.last_modified (our last save)
                    // In some cases the filesystem reports an inconsistent time,
                    // so we allow 0.5 seconds difference before complaining.
                    if ((last_modified.getTime() - that.last_modified.getTime()) > 500) {  // 500 ms
                        console.warn("Last saving was done on `"+that.last_modified+"`("+that._last_modified+"), "+
                                     "while the current file seem to have been saved on `"+data.last_modified+"`");
                        if (that._changed_on_disk_dialog !== null) {
                            // since the modal's event bindings are removed when destroyed, we reinstate
                            // save & reload callbacks on the confirmation & reload buttons
                            that._changed_on_disk_dialog.find('.save-confirm-btn').click(_save);
                            that._changed_on_disk_dialog.find('.btn-warning').click(function () {window.location.reload()});
                            
                            // redisplay existing dialog
                            that._changed_on_disk_dialog.modal('show');
                        } else {
                            // create new dialog
                            that._changed_on_disk_dialog = dialog.modal({
                                keyboard_manager: that.keyboard_manager,
                                title: i18n.msg._("File changed"),
                                body: i18n.msg._("The file has changed on disk since the last time we opened or saved it. "
                                        + "Do you want to overwrite the file on disk with the version open here, or load "
                                        + "the version on disk (reload the page)?"),
                                buttons: {
                                    Reload: {
                                        class: 'btn-warning',
                                        click: function () {
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
            }, function (error) {
                console.log(error);
                // maybe it has been deleted or renamed? Go ahead and save.
                return _save();
            })
        } else {
            return _save();
        }
    };

    Editor.prototype._clean_state = function(){
        var clean = this.codemirror.isClean(this.generation);
        if (clean === this.clean){
            return;
        } else {
            this.clean = clean;
        }
        if(clean){
            this.events.trigger("save_status_clean.Editor");
            this.clean_sel.attr('class','dirty-indicator-clean').attr('title','No changes to save');
        } else {
            this.events.trigger("save_status_dirty.Editor");
            this.clean_sel.attr('class','dirty-indicator-dirty').attr('title','Unsaved changes');
        }
    };

    Editor.prototype._set_codemirror_options = function (options) {
        // update codemirror options from a dict
        var codemirror = this.codemirror;
        $.map(options, function (value, opt) {
            if (value === null) {
                value = CodeMirror.defaults[opt];
            }
            codemirror.setOption(opt, value);
        });
        var that = this;
    };

    Editor.prototype.update_codemirror_options = function (options) {
        /** update codemirror options locally and save changes in config */
        var that = this;
        this._set_codemirror_options(options);
        return this.config.update({
            Editor: {
                codemirror_options: options
            }
        }).then(
            that.events.trigger('config_changed.Editor', {config: that.config})
        );
    };

    return {Editor: Editor};
});
