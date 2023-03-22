// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 *
 *
 * @module keyboardmanager
 * @namespace keyboardmanager
 * @class KeyboardManager
 */

define([
    'jquery',
    'base/js/utils',
    'base/js/keyboard',
], function($, utils, keyboard) {
    "use strict";
    
    // Main keyboard manager for the notebook
    var keycodes = keyboard.keycodes;

    var KeyboardManager = function (options) {
        /**
         * A class to deal with keyboard event and shortcut
         *
         * @class KeyboardManager
         * @constructor
         * @param options {dict} Dictionary of keyword arguments :
         *    @param options.events {$(Events)} instance 
         *    @param options.pager: {Pager}  pager instance
         */
        this.mode = 'command';
        this.enabled = true;
        this.pager = options.pager;
        this.quick_help = undefined;
        this.notebook = undefined;
        this.last_mode = undefined;
        this.bind_events();
        this.env = {pager:this.pager};
        this.actions = options.actions;
        this.command_shortcuts = new keyboard.ShortcutManager(undefined, options.events, this.actions, this.env, options.config, 'command');
        this.command_shortcuts._add_default_shortcuts(this.get_default_common_shortcuts());
        this.command_shortcuts._add_default_shortcuts(this.get_default_command_shortcuts());
        this.edit_shortcuts = new keyboard.ShortcutManager(undefined, options.events, this.actions, this.env);
        this.edit_shortcuts._add_default_shortcuts(this.get_default_common_shortcuts());
        this.edit_shortcuts._add_default_shortcuts(this.get_default_edit_shortcuts());


        this.config = options.config;
        var that = this;

        this.config.loaded.then(function(){ 
            var edit_unbind;

            try {
                edit_unbind = that.config.data.keys.edit.unbind||[];
            } catch (e) {
                if (e instanceof TypeError) {
                    edit_unbind = [];
                } else {
                    throw e;
                }
            }

            edit_unbind.forEach(function(u){that.edit_shortcuts.remove_shortcut(u);});

            var command_unbind;

            try {
                command_unbind = that.config.data.keys.command.unbind||[];
            } catch (e) {
                if (e instanceof TypeError) {
                    command_unbind = [];
                } else {
                    throw e;
                }
            }

            command_unbind.forEach(function(u){that.command_shortcuts.remove_shortcut(u);});

            that.command_shortcuts.add_shortcuts( ((that.config.data.keys||{}).command||{}).bind);
            that.edit_shortcuts.add_shortcuts(    ((that.config.data.keys||{}).edit   ||{}).bind);

            }
        );

        Object.seal(this);
    };




    /**
     * Return a dict of common shortcut
     * @method get_default_common_shortcuts
     *
     * @example Example of returned shortcut
     * ```
     * 'shortcut-key': 'action-name'
     * // a string representing the shortcut as dash separated value.
     * // e.g. 'shift' , 'shift-enter', 'cmd-t'
     *```
     */
    KeyboardManager.prototype.get_default_common_shortcuts = function() {
        return {
            'shift'       : 'jupyter-notebook:ignore',
            'shift-enter' : 'jupyter-notebook:run-cell-and-select-next',
            'alt-enter'   : 'jupyter-notebook:run-cell-and-insert-below',
            'ctrl-enter'  : 'jupyter-notebook:run-cell',
            // cmd on mac, ctrl otherwise
            'cmdtrl-enter'  : 'jupyter-notebook:run-cell',
            'cmdtrl-s'    : 'jupyter-notebook:save-notebook'
        };
    };

    KeyboardManager.prototype.get_default_edit_shortcuts = function() {
        return {
            'cmdtrl-shift-p'      : 'jupyter-notebook:show-command-palette',
            'cmdtrl-shift-f'      : 'jupyter-notebook:show-command-palette',
            'esc'                 : 'jupyter-notebook:enter-command-mode',
            'ctrl-m'              : 'jupyter-notebook:enter-command-mode',
            'up'                  : 'jupyter-notebook:move-cursor-up',
            'down'                : 'jupyter-notebook:move-cursor-down',
            'ctrl-shift--'        : 'jupyter-notebook:split-cell-at-cursor',
        };
    };

    KeyboardManager.prototype.get_default_command_shortcuts = function() {
        return {
            'cmdtrl-shift-p': 'jupyter-notebook:show-command-palette',
            'cmdtrl-shift-f': 'jupyter-notebook:show-command-palette',
            'shift-space': 'jupyter-notebook:scroll-notebook-up',
            'shift-v' : 'jupyter-notebook:paste-cell-above',
            'shift-m' : 'jupyter-notebook:merge-cells',
            'shift-o' : 'jupyter-notebook:toggle-cell-output-scrolled',
            'enter' : 'jupyter-notebook:enter-edit-mode',
            'space' : 'jupyter-notebook:scroll-notebook-down',
            'down' : 'jupyter-notebook:select-next-cell',
            'i,i' : 'jupyter-notebook:interrupt-kernel',
            '0,0' : 'jupyter-notebook:confirm-restart-kernel',
            'd,d' : 'jupyter-notebook:delete-cell',
            'esc': 'jupyter-notebook:close-pager',
            'up' : 'jupyter-notebook:select-previous-cell',
            'k' : 'jupyter-notebook:select-previous-cell',
            'j' : 'jupyter-notebook:select-next-cell',
            'shift-k': 'jupyter-notebook:extend-selection-above',
            'shift-j': 'jupyter-notebook:extend-selection-below',
            'shift-up': 'jupyter-notebook:extend-selection-above',
            'shift-down': 'jupyter-notebook:extend-selection-below',
            'cmdtrl-a': 'jupyter-notebook:select-all',
            'x' : 'jupyter-notebook:cut-cell',
            'c' : 'jupyter-notebook:copy-cell',
            'v' : 'jupyter-notebook:paste-cell-below',
            'a' : 'jupyter-notebook:insert-cell-above',
            'b' : 'jupyter-notebook:insert-cell-below',
            'y' : 'jupyter-notebook:change-cell-to-code',
            'm' : 'jupyter-notebook:change-cell-to-markdown',
            'r' : 'jupyter-notebook:change-cell-to-raw',
            '1' : 'jupyter-notebook:change-cell-to-heading-1',
            '2' : 'jupyter-notebook:change-cell-to-heading-2',
            '3' : 'jupyter-notebook:change-cell-to-heading-3',
            '4' : 'jupyter-notebook:change-cell-to-heading-4',
            '5' : 'jupyter-notebook:change-cell-to-heading-5',
            '6' : 'jupyter-notebook:change-cell-to-heading-6',
            'o' : 'jupyter-notebook:toggle-cell-output-collapsed',
            's' : 'jupyter-notebook:save-notebook',
            'l' : 'jupyter-notebook:toggle-cell-line-numbers',
            'shift-l' : 'jupyter-notebook:toggle-all-line-numbers',
            'h' : 'jupyter-notebook:show-keyboard-shortcuts',
            'z' : 'jupyter-notebook:undo-cell-deletion',
            'q' : 'jupyter-notebook:close-pager',
            'p' : 'jupyter-notebook:show-command-palette',
        };
    };

    KeyboardManager.prototype.bind_events = function () {
        var that = this;
        $(document).keydown(function (event) {
            if(event._ipkmIgnore===true||(event.originalEvent||{})._ipkmIgnore===true){
                return false;
            }
            return that.handle_keydown(event);
        });
    };

    KeyboardManager.prototype.set_notebook = function (notebook) {
        this.notebook = notebook;
        this.actions.extend_env({notebook:notebook});
    };
    
    KeyboardManager.prototype.set_quickhelp = function (notebook) {
        this.actions.extend_env({quick_help:notebook});
    };


    KeyboardManager.prototype.handle_keydown = function (event) {
        /**
         *  returning false from this will stop event propagation
         **/

        if (event.which === keycodes.esc) {
            // Intercept escape at highest level to avoid closing
            // websocket connection with firefox
            event.preventDefault();
        }
        
        if (!this.enabled) {
            if (event.which === keycodes.esc) {
                this.notebook.command_mode();
                return false;
            }
            return true;
        }
        
        if (this.mode === 'edit') {
            return this.edit_shortcuts.call_handler(event);
        } else if (this.mode === 'command') {
            return this.command_shortcuts.call_handler(event);
        }
        return true;
    };

    KeyboardManager.prototype.edit_mode = function () {
        this.last_mode = this.mode;
        this.mode = 'edit';
    };

    KeyboardManager.prototype.command_mode = function () {
        this.last_mode = this.mode;
        this.mode = 'command';
    };

    KeyboardManager.prototype.enable = function () {
        this.enabled = true;
    };

    KeyboardManager.prototype.disable = function () {
        this.enabled = false;
    };

    KeyboardManager.prototype.register_events = function (e) {
        e = $(e);
        var that = this;
        var handle_focus = function () {
            that.disable();
        };
        var handle_blur = function () {
            that.enable();
        };
        e.on('focusin', handle_focus);
        e.on('focusout', handle_blur);
        // TODO: Very strange. The focusout event does not seem fire for the 
        // bootstrap textboxes on FF25&26...  This works around that by 
        // registering focus and blur events recursively on all inputs within
        // registered element.
        e.find('input').blur(handle_blur);
        e.on('DOMNodeInserted', function (event) {
            var target = $(event.target);
            if (target.is('input')) {
                target.blur(handle_blur);
            } else {
                target.find('input').blur(handle_blur);    
            }
          });
        // There are times (raw_input) where we remove the element from the DOM before
        // focusout is called. In this case we bind to the remove event of jQueryUI,
        // which gets triggered upon removal, iff it is focused at the time.
        // is_focused must be used to check for the case where an element within
        // the element being removed is focused.
        e.on('remove', function () {
            if (utils.is_focused(e[0])) {
                that.enable();
            }
        });
    };

    return {'KeyboardManager': KeyboardManager};
});
