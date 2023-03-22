// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils',
    'base/js/dialog',
    'codemirror/lib/codemirror',
    'codemirror/mode/meta',
], function($, IPython, utils, dialog, CodeMirror) {
    "use strict";
    
    var MenuBar = function (selector, options) {
        /**
         * Constructor
         *
         * A MenuBar Class to generate the menubar of IPython notebook
         *
         * Parameters:
         *  selector: string
         *  options: dictionary
         *      Dictionary of keyword arguments.
         *          codemirror: CodeMirror instance
         *          contents: ContentManager instance
         *          events: $(Events) instance
         *          base_url : string
         *          file_path : string
         */
        options = options || {};
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url || utils.get_body_data("baseUrl");
        this.selector = selector;
        this.editor = options.editor;
        this.events = options.events;
        this.save_widget = options.save_widget;

        if (this.selector !== undefined) {
            this.element = $(selector);
            this.bind_events();
        }
        this._load_mode_menu();
        Object.seal(this);
    };

    MenuBar.prototype.bind_events = function () {
        var that = this;
        var editor = that.editor;
        
        //  File
        this.element.find('#new-file').click(function () {
            var w = window.open(undefined, IPython._target);
            // Create a new file in the current directory
            var parent = utils.url_path_split(editor.file_path)[0];
            editor.contents.new_untitled(parent, {type: "file"}).then(
                function (data) {
                    w.location = utils.url_path_join(
                        that.base_url, that.nbclassic_path, 'edit', utils.encode_uri_components(data.path)
                    );
                },
                function(error) {
                    w.close();
                    dialog.modal({
                        title : 'Creating New File Failed',
                        body : "The error was: " + error.message,
                        buttons : {'OK' : {'class' : 'btn-primary'}}
                    });
                }
            );
        });
        this.element.find('#save-file').click(function () {
            editor.save();
        });
        this.element.find('#rename-file').click(function () {
            that.save_widget.rename();
        });
        this.element.find('#download-file').click(function () {
            window.open(utils.url_path_join(
                that.base_url, 'files',
                utils.encode_uri_components(that.editor.file_path)
            ) + '?download=1');
        });
        
        // Edit
        this.element.find('#menu-find').click(function () {
            editor.codemirror.execCommand("find");
        });
        this.element.find('#menu-replace').click(function () {
            editor.codemirror.execCommand("replace");
        });
        this.element.find('#menu-keymap-default').click(function () {
            editor.update_codemirror_options({
                vimMode: false,
                keyMap: 'default'
            });
        });
        this.element.find('#menu-keymap-sublime').click(function () {
            editor.update_codemirror_options({
                vimMode: false,
                keyMap: 'sublime'
            });
        });
        this.element.find('#menu-keymap-emacs').click(function () {
            editor.update_codemirror_options({
                vimMode: false,
                keyMap: 'emacs'
            });
        });
        this.element.find('#menu-keymap-vim').click(function () {
            editor.update_codemirror_options({
                vimMode: true,
                keyMap: 'vim'
            });
        });
        
        // View

        this.element.find('#toggle_header').click(function (){
            $("#header-container").toggle();
        });
        
        this.element.find('#menu-line-numbers').click(function () {
            var current = editor.codemirror.getOption('lineNumbers');
            var value = Boolean(1-current);
            editor.update_codemirror_options({lineNumbers: value});
        });
        
        this.events.on("config_changed.Editor", function () {
            var keyMap = editor.codemirror.getOption('keyMap') || 'default';
            that.element.find(".selected-keymap").removeClass("selected-keymap");
            that.element.find("#menu-keymap-" + keyMap).addClass("selected-keymap");
        });
        
        this.events.on("mode_changed.Editor", function (evt, modeinfo) {
            that.element.find("#current-mode")
                .text(modeinfo.name)
                .attr(
                    'title',
                    "The current language is " + modeinfo.name
                );
        });
    };
    
    MenuBar.prototype._load_mode_menu = function () {
        var list = this.element.find("#mode-menu");
        var editor = this.editor;
        function make_set_mode(info) {
            return function () {
                editor.set_codemirror_mode(info);
                // save codemirror mode for extension when explicitly selected
                editor.save_codemirror_mode(info);
            };
        }
        for (var i = 0; i < CodeMirror.modeInfo.length; i++) {
            var info = CodeMirror.modeInfo[i];
            list.append($("<li>").append(
                $("<a>").attr("href", "#")
                    .text(info.name)
                    .click(make_set_mode(info))
                    .attr('title',
                        "Set language to " + info.name
                    )
            ));
        }
    };

    return {'MenuBar': MenuBar};
});
