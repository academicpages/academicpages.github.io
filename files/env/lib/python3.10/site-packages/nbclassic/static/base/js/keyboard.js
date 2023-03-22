// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
/**
 *
 *
 * @module keyboard
 * @namespace keyboard
 * @class ShortcutManager
 */

define([
    'jquery',
    'base/js/utils',
    'underscore',
], function($, utils, _) {
    "use strict";


    /**
     * Setup global keycodes and inverse keycodes.
     *
     * See http://unixpapa.com/js/key.html for a complete description. The short of
     * it is that there are different keycode sets. Firefox uses the "Mozilla keycodes"
     * and Webkit/IE use the "IE keycodes". These keycode sets are mostly the same
     * but have minor differences.
     **/

     // These apply to Firefox, (Webkit and IE)
     // This does work **only** on US keyboard.
    var _keycodes = {
        'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73,
        'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81, 'r': 82,
        's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 'z': 90,
        '1 !': 49, '2 @': 50, '3 #': 51, '4 $': 52, '5 %': 53, '6 ^': 54,
        '7 &': 55, '8 *': 56, '9 (': 57, '0 )': 48, 
        '[ {': 219, '] }': 221, '` ~': 192,  ', <': 188, '. >': 190, '/ ?': 191,
        '\\ |': 220, '\' "': 222,
        'numpad0': 96, 'numpad1': 97, 'numpad2': 98, 'numpad3': 99, 'numpad4': 100,
        'numpad5': 101, 'numpad6': 102, 'numpad7': 103, 'numpad8': 104, 'numpad9': 105,
        'multiply': 106, 'add': 107, 'subtract': 109, 'decimal': 110, 'divide': 111,
        'f1': 112, 'f2': 113, 'f3': 114, 'f4': 115, 'f5': 116, 'f6': 117, 'f7': 118,
        'f8': 119, 'f9': 120, 'f10': 121, 'f11': 122, 'f12': 123, 'f13': 124, 'f14': 125, 'f15': 126,
        'backspace': 8, 'tab': 9, 'enter': 13, 'shift': 16, 'ctrl': 17, 'alt': 18,
        'meta': 91, 'capslock': 20, 'esc': 27, 'space': 32, 'pageup': 33, 'pagedown': 34,
        'end': 35, 'home': 36, 'left': 37, 'up': 38, 'right': 39, 'down': 40,
        'insert': 45, 'delete': 46, 'numlock': 144,
    };
    
    // These apply to Firefox and Opera
    var _mozilla_keycodes = {
        '; :': 59, '= +': 61, '- _': 173, 'meta': 224, 'minus':173
    };
    
    // This apply to Webkit and IE
    var _ie_keycodes = {
        '; :': 186, '= +': 187, '- _': 189, 'minus':189
    };
    
    var browser = utils.browser[0];
    var platform = utils.platform;
    
    if (browser === 'Firefox' || browser === 'Opera' || browser === 'Netscape') {
        $.extend(_keycodes, _mozilla_keycodes);
    } else if (browser === 'Safari' || browser === 'Chrome' || browser === 'MSIE') {
        $.extend(_keycodes, _ie_keycodes);
    }

    var keycodes = {};
    var inv_keycodes = {};
    for (var name in _keycodes) {
        var names = name.split(' ');
        if (names.length === 1) {
            var n = names[0];
            keycodes[n] = _keycodes[n];
            inv_keycodes[_keycodes[n]] = n;
        } else {
            var primary = names[0];
            var secondary = names[1];
            keycodes[primary] = _keycodes[name];
            keycodes[secondary] = _keycodes[name];
            inv_keycodes[_keycodes[name]] = primary;
        }
    }

    var normalize_key = function (key) {
        return inv_keycodes[keycodes[key]];
    };

    var normalize_shortcut = function (shortcut) {
        /**
         * @function _normalize_shortcut
         * @private
         * return a dict containing the normalized shortcut and the number of time it should be pressed:
         *
         * Put a shortcut into normalized form:
         * 1. Make lowercase
         * 2. Replace cmd by meta
         * 3. Sort '-' separated modifiers into the order alt-ctrl-meta-shift
         * 4. Normalize keys
         **/
        if (platform === 'MacOS') {
            shortcut = shortcut.toLowerCase().replace('cmdtrl-', 'cmd-');
        } else {
            shortcut = shortcut.toLowerCase().replace('cmdtrl-', 'ctrl-');
        }

        shortcut = shortcut.toLowerCase().replace('cmd', 'meta');
        shortcut = shortcut.replace(/-$/, 'minus');  // catch shortcuts using '-' key
        shortcut = shortcut.replace(/,$/, 'comma');  // catch shortcuts using '-' key
        if(shortcut.indexOf(',') !== -1){
            var sht = shortcut.split(',');
            sht = _.map(sht, normalize_shortcut);
            return shortcut;
        }
        shortcut = shortcut.replace(/comma/g, ',');  // catch shortcuts using '-' key
        var values = shortcut.split("-");
        if (values.length === 1) {
            return normalize_key(values[0]);
        } else {
            var modifiers = values.slice(0,-1);
            var key = normalize_key(values[values.length-1]);
            modifiers.sort();
            return modifiers.join('-') + '-' + key;
        }
    };

    var shortcut_to_event = function (shortcut, type) {
        /**
         * Convert a shortcut (shift-r) to a jQuery Event object
         **/
        type = type || 'keydown';
        shortcut = normalize_shortcut(shortcut);
        shortcut = shortcut.replace(/-$/, 'minus');  // catch shortcuts using '-' key
        var values = shortcut.split("-");
        var modifiers = values.slice(0,-1);
        var key = values[values.length-1];
        var opts = {which: keycodes[key]};
        if (modifiers.indexOf('alt') !== -1) {opts.altKey = true;}
        if (modifiers.indexOf('ctrl') !== -1) {opts.ctrlKey = true;}
        if (modifiers.indexOf('meta') !== -1) {opts.metaKey = true;}
        if (modifiers.indexOf('shift') !== -1) {opts.shiftKey = true;}
        return $.Event(type, opts);
    };

    var only_modifier_event = function(event){
        /**
         * Return `true` if the event only contains modifiers keys.
         * false otherwise
         **/
        var key = inv_keycodes[event.which];
        return ((event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) &&
         (key === 'alt'|| key === 'ctrl'|| key === 'meta'|| key === 'shift'));

    };

    var event_to_shortcut = function (event) {
        /**
         * Convert a jQuery Event object to a normalized shortcut string (shift-r)
         **/
        var shortcut = '';
        var key = inv_keycodes[event.which];
        if (event.altKey && key !== 'alt') {shortcut += 'alt-';}
        if (event.ctrlKey && key !== 'ctrl') {shortcut += 'ctrl-';}
        if (event.metaKey && key !== 'meta') {shortcut += 'meta-';}
        if (event.shiftKey && key !== 'shift') {shortcut += 'shift-';}
        shortcut += key;
        return shortcut;
    };

    // Shortcut manager class

    var ShortcutManager = function (delay, events, actions, env, config, mode) {
        /**
         * A class to deal with keyboard event and shortcut
         *
         * @class ShortcutManager
         * @constructor
         *
         * :config: configobjet on which to call `update(....)` to persist the config.
         * :mode: mode of this shortcut manager where to persist config.
         */
        mode = mode || 'command';
        this._shortcuts = {};
        this._defaults_bindings = [];
        this.delay = delay || 800; // delay in milliseconds
        this.events = events;
        this.actions = actions;
        this.actions.extend_env(env);
        this._queue = [];
        this._cleartimeout = null;
        this._config = config;
        this._mode = mode;
        Object.seal(this);
    };

    ShortcutManager.prototype.clearsoon = function(){
        /**
         * Clear the pending shortcut soon, and cancel previous clearing
         * that might be registered.
         **/
         var that = this;
         clearTimeout(this._cleartimeout);
         this._cleartimeout = setTimeout(function(){that.clearqueue();}, this.delay);
    };


    ShortcutManager.prototype.clearqueue = function(){
        /**
         * clear the pending shortcut sequence now. 
         **/
        this._queue = [];
        clearTimeout(this._cleartimeout);
    };


    var flatten_shorttree = function(tree){
        /**
         * Flatten a tree of shortcut sequences. 
         * use full to iterate over all the key/values of available shortcuts.
         **/
        var dct = {};
        _.forEach(tree, function(value, key) {
            if(typeof(value) === 'string'){
                dct[key] = value;
            } else {
                var ftree=flatten_shorttree(value);
                _.forEach(ftree, function(v2, subkey) {
                    dct[key+','+subkey] = ftree[subkey];
                });
            } 
        });
        return dct;
    };


    ShortcutManager.prototype.get_action_shortcuts = function(name){
      var ftree = flatten_shorttree(this._shortcuts);
      var res = [];
      _.forEach(ftree, function(value, key) {
        if(value === name){
          res.push(key);
        }
      });
      return res;
    };
    
    ShortcutManager.prototype.get_action_shortcut = function(name){
      var matches = this.get_action_shortcuts(name);
      if (matches.length > 0) {
          return matches[0];
      }
      return undefined;
    };

    ShortcutManager.prototype.help = function () {
        var that = this;
        var help = [];
        var ftree = flatten_shorttree(this._shortcuts);
        _.forEach(ftree, function(value, key) {
            var action = that.actions.get(value);
            var help_string = action.help||'== no help ==';
            var help_index = action.help_index;
            if (help_string) {
                var shortstring = (action.shortstring||key);
                help.push({
                    shortcut: shortstring,
                    help: help_string,
                    help_index: help_index}
                );
            }
        });
        help.sort(function (a, b) {
            if (a.help_index === b.help_index) {
                if (a.shortcut === b.shortcut) {
                    return 0;
                }
                if (a.shortcut > b.shortcut) {
                    return 1;
                }
                return -1;
            }
            if (a.help_index === undefined || a.help_index > b.help_index){
                return 1;
            }
            return -1;
        });
        return help;
    };

    ShortcutManager.prototype.clear_shortcuts = function () {
        this._shortcuts = {};
    };

    ShortcutManager.prototype.get_shortcut = function (shortcut){
        /**
         * return a node of the shortcut tree which an action name (string) if leaf,
         * and an object with `object.subtree===true`
         **/
        if(typeof(shortcut) === 'string'){
            shortcut = shortcut.split(',');
        }
        
        return this._get_leaf(shortcut, this._shortcuts);
    };


    ShortcutManager.prototype._get_leaf = function(shortcut_array, tree){
        /**
         * @private
         * find a leaf/node in a subtree of the keyboard shortcut
         *
         **/
        if(shortcut_array.length === 1){
            return tree[shortcut_array[0]];
        } else if(  typeof(tree[shortcut_array[0]]) !== 'string'){
            return this._get_leaf(shortcut_array.slice(1), tree[shortcut_array[0]]);
        }
        return null;
    };

    ShortcutManager.prototype.set_shortcut = function( shortcut, action_name){
        if( typeof(action_name) !== 'string'){throw new Error('action is not a string', action_name);}
        if( typeof(shortcut) === 'string'){
            shortcut = shortcut.split(',');
        }
        return this._set_leaf(shortcut, action_name, this._shortcuts);
    };

    ShortcutManager.prototype._is_leaf = function(shortcut_array, tree){
        if(shortcut_array.length === 1){
           return(typeof(tree[shortcut_array[0]]) === 'string');
        } else {
            var subtree = tree[shortcut_array[0]];
            return this._is_leaf(shortcut_array.slice(1), subtree );
        }
    };

    ShortcutManager.prototype._remove_leaf = function(shortcut_array, tree, allow_node){
        if(shortcut_array.length === 1){
            var current_node = tree[shortcut_array[0]];
            if(typeof(current_node) === 'string'){
                delete tree[shortcut_array[0]];
            } else {
                throw new Error('try to delete non-leaf');
            }
        } else {
            this._remove_leaf(shortcut_array.slice(1),  tree[shortcut_array[0]], allow_node);
            if(_.keys(tree[shortcut_array[0]]).length === 0){
                delete tree[shortcut_array[0]];
            }
        }
    };

    ShortcutManager.prototype.is_available_shortcut = function(shortcut){
        var shortcut_array = shortcut.split(',');
        return this._is_available_shortcut(shortcut_array, this._shortcuts);
    };

    ShortcutManager.prototype._is_available_shortcut = function(shortcut_array, tree){
        var current_node = tree[shortcut_array[0]];
        if(!shortcut_array[0]){
            return false;
        }
        if(current_node === undefined){
            return true;
        } else {
            if (typeof(current_node) === 'string'){
                return false;
            } else { // assume is a sub-shortcut tree
                return this._is_available_shortcut(shortcut_array.slice(1), current_node);
            }
        }
    };

    ShortcutManager.prototype._set_leaf = function(shortcut_array, action_name, tree){
        var current_node = tree[shortcut_array[0]];

        if(shortcut_array.length === 1){
            if(current_node !== undefined && typeof(current_node) !== 'string'){
                console.warn('[warning], you are overriting a long shortcut with a shorter one');
            }
            tree[shortcut_array[0]] = action_name;
            return true;
        } else {
            if(typeof(current_node) === 'string'){
                console.warn('you are trying to set a shortcut that will be shadowed'+
                             'by a more specific one. Aborting for :', action_name, 'the following '+
                             'will take precedence', current_node);
                return false;
            } else {
                tree[shortcut_array[0]] = tree[shortcut_array[0]]||{};
            }
            this._set_leaf(shortcut_array.slice(1), action_name, tree[shortcut_array[0]]);
            return true;
        }
    };

    ShortcutManager.prototype._persist_shortcut = function(shortcut, data) {
        /**
         * add a shortcut to this manager and persist it to the config file. 
         **/ 
        shortcut = shortcut.toLowerCase();
        this.add_shortcut(shortcut, data);
        var patch = {keys:{}};
        patch.keys[this._mode] = {bind:{}};
        patch.keys[this._mode].bind[shortcut] = data;
        this._config.update(patch);
    };

    ShortcutManager.prototype._persist_remove_shortcut = function(shortcut){
        /**
         * Remove a shortcut from this manager and persist its removal.
         */

        shortcut = shortcut.toLowerCase();
        this.remove_shortcut(shortcut);
        var patch = {keys: {}};
        patch.keys[this._mode] = {bind:{}};
        patch.keys[this._mode].bind[shortcut] = null;
        this._config.update(patch);

        // if the shortcut we unbind is a default one, we add it to the list of
        // things to unbind at startup
        if( this._defaults_bindings.indexOf(shortcut) !== -1 ){
            var cnf = (this._config.data.keys || {})[this._mode];
            var unbind_array = cnf.unbind || [];


            // unless it's already there (like if we have remapped a default
            // shortcut to another command): unbind it)
            if(unbind_array.indexOf(shortcut) === -1){
                var _parray = unbind_array.concat(shortcut);
                var unbind_patch = {keys:{}};
                unbind_patch.keys[this._mode] = {unbind:_parray};
                console.warn('up:', unbind_patch);
                this._config.update(unbind_patch);
            }
        }
    };


    ShortcutManager.prototype.add_shortcut = function (shortcut, data, suppress_help_update) {
        /**
         * Add an action to be handled by shortcut manager. 
         * 
         * - `shortcut` should be a `Shortcut Sequence` of the for `Ctrl-Alt-C,Meta-X`...
         * - `data` could be an `action name`, an `action` or a `function`.
         *   if a `function` is passed it will be converted to an anonymous `action`. 
         *
         **/
        var action_name = this.actions.get_name(data);
        if (! action_name){
          if (typeof data === 'string') {
            // If we have an action name, allow it to be bound anyway.
            console.log("Unknown action '" + data + "' for shortcut " + shortcut
                + "; it may be defined by an extension which is not yet loaded.");
            action_name = data;
          } else {
            throw new Error('does not know how to deal with : ' + data);
          }
        }
        var _shortcut = normalize_shortcut(shortcut);
        this.set_shortcut(_shortcut, action_name);

        if (!suppress_help_update) {
            // update the keyboard shortcuts notebook help
            this.events.trigger('rebuild.QuickHelp');
        }
    };

    ShortcutManager.prototype.add_shortcuts = function (data) {
        /**
         * Convenient methods to call `add_shortcut(key, value)` on several items
         * 
         *  data : Dict of the form {key:value, ...}
         **/
        var that = this;
        _.forEach(data, function(value, key) {
            that.add_shortcut(key, value, true);
        });
        // update the keyboard shortcuts notebook help
        this.events.trigger('rebuild.QuickHelp');
    };

    ShortcutManager.prototype._add_default_shortcuts = function (data) {
        /**
         * same as add_shortcuts, but register them as "default" that if persistently unbound, with
         * persist_remove_shortcut, need to be on the "unbind" list. 
         **/
        this._defaults_bindings = this._defaults_bindings.concat(Object.keys(data));
        this.add_shortcuts(data);

    };

    ShortcutManager.prototype.remove_shortcut = function (shortcut, suppress_help_update) {
        /**
         * Remove the binding of shortcut `shortcut` with its action.
         * throw an error if trying to remove a non-exiting shortcut
         **/
        if(!shortcut){
            console.warn('trying to remove empty shortcut');
            return;
        }
        shortcut = normalize_shortcut(shortcut);
        if( typeof(shortcut) === 'string'){
            shortcut = shortcut.split(',');
        }
        /*
         *  The shortcut error should be explicit here, because it will be
         *  seen by users.
         */
        try {
          this._remove_leaf(shortcut, this._shortcuts);
          if (!suppress_help_update) {
            // update the keyboard shortcuts notebook help
            this.events.trigger('rebuild.QuickHelp');
          }
        } catch (ex) {
          throw new Error('trying to remove a non-existent shortcut', shortcut, typeof shortcut);
        }
    };



    ShortcutManager.prototype.call_handler = function (event) {
        /**
         * Call the corresponding shortcut handler for a keyboard event
         * @method call_handler
         * @return {Boolean} `true|false`, `false` if no handler was found, otherwise the  value return by the handler. 
         * @param event {event}
         *
         * given an event, call the corresponding shortcut. 
         * return false is event wan handled, true otherwise 
         * in any case returning false stop event propagation
         **/


        this.clearsoon();
        if(only_modifier_event(event)){
            return true;
        }
        var shortcut = event_to_shortcut(event);
        this._queue.push(shortcut);
        var action_name = this.get_shortcut(this._queue);

        if (typeof(action_name) === 'undefined'|| action_name === null){
            this.clearqueue();
            return true;
        }
        
        if (this.actions.exists(action_name)) {
            event.preventDefault();
            this.clearqueue();
            return this.actions.call(action_name, event);
        }

        return false;
    };


    ShortcutManager.prototype.handles = function (event) {
        var shortcut = event_to_shortcut(event);
        var action_name = this.get_shortcut(this._queue.concat(shortcut));
        return (typeof(action_name) !== 'undefined');
    };

    return {
        keycodes : keycodes,
        inv_keycodes : inv_keycodes,
        ShortcutManager : ShortcutManager,
        normalize_key : normalize_key,
        normalize_shortcut : normalize_shortcut,
        shortcut_to_event : shortcut_to_event,
        event_to_shortcut : event_to_shortcut,
    };
});
