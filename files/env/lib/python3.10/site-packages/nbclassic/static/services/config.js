// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'base/js/utils',
    ],
function(utils) {
    "use strict";
    var ConfigSection = function(section_name, options) {
        this.section_name = section_name;
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url;
        this.data = {};
        
        var that = this;
        
        /* .loaded is a promise, fulfilled the first time the config is loaded
         * from the server. Code can do:
         *      conf.loaded.then(function() { ... using conf.data ... });
         */
        this._one_load_finished = false;
        this.loaded = new Promise(function(resolve, reject) {
            that._finish_firstload = resolve;
        });
    };

    ConfigSection.prototype.api_url = function() {
        return utils.url_path_join(this.base_url, 'api/config',
            utils.encode_uri_components(this.section_name));
    };
    
    ConfigSection.prototype._load_done = function() {
        if (!this._one_load_finished) {
            this._one_load_finished = true;
            this._finish_firstload();
        }
    };
    
    ConfigSection.prototype.load = function() {
        var that = this;
        return utils.promising_ajax(this.api_url(), {
            cache: false,
            type: "GET",
            dataType: "json",
        }).then(function(data) {
            that.data = data;
            that._load_done();
            return data;
        });
    };
    
    /**
     * Modify the config values stored. Update the local data immediately,
     * send the change to the server, and use the updated data from the server
     * when the reply comes.
     */
    ConfigSection.prototype.update = function(newdata) {
        $.extend(true, this.data, newdata);  // true -> recursive update
        
        var that = this;
        return utils.promising_ajax(this.api_url(), {
            processData: false,
            type : "PATCH",
            data: JSON.stringify(newdata),
            dataType : "json",
            contentType: 'application/json',
        }).then(function(data) {
            that.data = data;
            that._load_done();
            return data;
        });
    };
    
    
    var ConfigWithDefaults = function(section, defaults, classname) {
        this.section = section;
        this.defaults = defaults;
        this.classname = classname;
    };
    
    ConfigWithDefaults.prototype._class_data = function() {
        if (this.classname) {
            return this.section.data[this.classname] || {};
        } else {
            return this.section.data;
        }
    };
    
    /**
     * Wait for config to have loaded, then get a value or the default.
     * Returns a promise.
     */
    ConfigWithDefaults.prototype.get = function(key) {
        var that = this;
        return this.section.loaded.then(function() {
            return that.get_sync(key);
        });
    };
    
    /**
     * Return a config value. If config is not yet loaded, return the default
     * instead of waiting for it to load.
     */
    ConfigWithDefaults.prototype.get_sync = function(key) {
        var data = this._class_data();
        if (key === undefined) {
            // no key specified, return full config data
            return $.extend(true, {}, this.defaults, data);
        }

        var value = data[key];
        if (value !== undefined) {
            if (typeof value == 'object') {
                // merge with defaults if it's an object
                return $.extend(true, {}, this.defaults[key], value);
            } else {
                return value;
            }
        }
        return this.defaults[key];
    };
    
    /**
     * Set a config value. Send the update to the server, and change our
     * local copy of the data immediately.
     * Returns a promise which is fulfilled when the server replies to the
     * change.
     */
     ConfigWithDefaults.prototype.set = function(key, value) {
         var d = {};
         d[key] = value;
         if (this.classname) {
            var d2 = {};
            d2[this.classname] = d;
            return this.section.update(d2);
        } else {
            return this.section.update(d);
        }
    };
    
    return {ConfigSection: ConfigSection,
            ConfigWithDefaults: ConfigWithDefaults,
           };

});
