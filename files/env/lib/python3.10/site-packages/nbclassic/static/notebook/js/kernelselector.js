// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/dialog',
    'base/js/utils',
    'base/js/i18n'
], function($, IPython, dialog, utils, i18n) {
    "use strict";
    
    var KernelSelector = function(selector, notebook, options) {
        options = options || {};
        var that = this;
        this.selector = selector;
        this.notebook = notebook;
        this.nbclassic_path = options.nbclassic_path;
        this.notebook.set_kernelselector(this);
        this.events = notebook.events;
        this.current_selection = null;
        this.kernelspecs = {};
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.request_kernelspecs();
        }
        this.bind_events();
        // Make the object globally available for user convenience & inspection
        IPython.kernelselector = this;
        this._finish_load = null;
        this._loaded = false;
        this.loaded = new Promise(function(resolve) {
            that._finish_load = resolve;
        });
        
        Object.seal(this);
    };
    
    KernelSelector.prototype.request_kernelspecs = function() {
        // Preliminary documentation for kernelspecs api is at 
        // https://github.com/ipython/ipython/wiki/IPEP-25%3A-Registry-of-installed-kernels#rest-api
        var url = utils.url_path_join(this.notebook.base_url, 'api/kernelspecs');
        utils.promising_ajax(url).then($.proxy(this._got_kernelspecs, this));
    };
    
    var _sorted_names = function(kernelspecs) {
        // sort kernel names
        return Object.keys(kernelspecs).sort(function (a, b) {
            // sort by display_name
            var da = kernelspecs[a].spec.display_name;
            var db = kernelspecs[b].spec.display_name;
            if (da === db) {
                return 0;
            } else if (da > db) {
                return 1;
            } else {
                return -1;
            }
        });
    };
    
    KernelSelector.prototype._got_kernelspecs = function(data) {
        var that = this;
        this.kernelspecs = data.kernelspecs;
        var change_kernel_submenu = $("#menu-change-kernel-submenu");
        var new_notebook_submenu = $("#menu-new-notebook-submenu");
        var keys = _sorted_names(data.kernelspecs);
        
        keys.map(function (key) {
            // Create the Kernel > Change kernel submenu
            var ks = data.kernelspecs[key];
            change_kernel_submenu.append(
                $("<li>").attr("id", "kernel-submenu-"+ks.name).append(
                    $('<a>')
                        .attr('href', '#')
                        .click( function () {
                            that.set_kernel(ks.name);
                        })
                        .text(ks.spec.display_name)
                )
            );
            // Create the File > New Notebook submenu
            new_notebook_submenu.append(
                $("<li>").attr("id", "new-notebook-submenu-"+ks.name).append(
                    $('<a>')
                        .attr('href', '#')
                        .click( function () {
                            that.new_notebook(ks.name);
                        })
                        .text(ks.spec.display_name)
                )
            );

        });
        // trigger loaded promise
        this._loaded = true;
        this._finish_load();
    };
    
    KernelSelector.prototype._spec_changed = function (event, ks) {
        /** event handler for spec_changed */
        var that = this;
        
        // update selection
        this.current_selection = ks.name;
        
        // put the current kernel at the top of File > New Notebook
        var cur_kernel_entry = $("#new-notebook-submenu-" + ks.name);
        var parent = cur_kernel_entry.parent();
        // do something only if there is more than one kernel
        if (parent.children().length > 1) {
            // first, sort back the submenu
            parent.append(
                parent.children("li[class!='divider']").sort(
                    function (a,b) {
                        var da = $("a",a).text();
                        var db = $("a",b).text();
                        if (da === db) {
                            return 0;
                        } else if (da > db) {
                            return 1;
                        } else {
                            return -1;
                        }}));
            // then, if there is no divider yet, add one
            if (!parent.children("li[class='divider']").length) {
                parent.prepend($("<li>").attr("class","divider"));
            } 
            // finally, put the current kernel at the top
            parent.prepend(cur_kernel_entry);
        }
        
        // load logo
        var logo_img = this.element.find("img.current_kernel_logo");
        $("#kernel_indicator").find('.kernel_indicator_name').text(ks.spec.display_name);
        if (ks.resources['logo-64x64']) {
            logo_img.attr("src", ks.resources['logo-64x64']);
            logo_img.attr("title", ks.spec.display_name);
            logo_img.show();
        } else {
            logo_img.hide();
        }
        
        // load kernel css
        var css_url = ks.resources['kernel.css'];
        if (css_url) {
            $('#kernel-css').attr('href', css_url);
        } else {
            $('#kernel-css').attr('href', '');
        }
        
        // load kernel js
        if (ks.resources['kernel.js']) {

            // Debug added for Notebook 4.2, please remove at some point in the
            // future if the following does not append anymore when kernels
            // have kernel.js
            //
            // > Uncaught (in promise) TypeError: require is not a function
            // 
            console.info('Dynamically requiring kernel.js, `requirejs` is ', requirejs);
            requirejs([ks.resources['kernel.js']],
                function (kernel_mod) {
                    if (kernel_mod && kernel_mod.onload) {
                        kernel_mod.onload();
                    } else {
                        console.warn("Kernel " + ks.name + " has a kernel.js file that does not contain "+
                                     "any asynchronous module definition. This is undefined behavior "+
                                     "and not recommended.");
                    }
                }, function (err) {
                    console.warn("Failed to load kernel.js from ", ks.resources['kernel.js'], err);
                }
            );
            this.events.on('spec_changed.Kernel', function (evt, new_ks) {
                if (ks.name != new_ks.name) {
                    console.warn("kernelspec %s had custom kernel.js. Forcing page reload for %s.",
                        ks.name, new_ks.name);
                    that.notebook.save_notebook().then(function () {
                        window.location.reload();
                    });
                }
            });
        }
    };

    KernelSelector.prototype.set_kernel = function (selected) {
        /** set the kernel by name, ensuring kernelspecs have been loaded, first 
        
        kernel can be just a kernel name, or a notebook kernelspec metadata
        (name, language, display_name).
        */
        var that = this;
        if (typeof selected === 'string') {
            selected = {
                name: selected
            };
        }
        if (this._loaded) {
            this._set_kernel(selected);
        } else {
            return this.loaded.then(function () {
                that._set_kernel(selected);
            });
        }
    };

    KernelSelector.prototype._set_kernel = function (selected) {
        /** Actually set the kernel (kernelspecs have been loaded) */
        if (selected.name === this.current_selection) {
            // only trigger event if value changed
            return;
        }
        var kernelspecs = this.kernelspecs;
        var ks = kernelspecs[selected.name];
        if (ks === undefined) {
            var available = _sorted_names(kernelspecs);
            var matches = [];
            if (selected.language && selected.language.length > 0) {
                available.map(function (name) {
                    if (kernelspecs[name].spec.language.toLowerCase() === selected.language.toLowerCase()) {
                        matches.push(name);
                    }
                });
            }
            if (matches.length === 1) {
                ks = kernelspecs[matches[0]];
                console.log("No exact match found for " + selected.name +
                    ", using only kernel that matches language=" + selected.language, ks);
                this.events.trigger("spec_match_found.Kernel", {
                    selected: selected,
                    found: ks,
                });
            }
            // if still undefined, trigger failure event
            if (ks === undefined) {
                this.events.trigger("spec_not_found.Kernel", {
                    selected: selected,
                    matches: matches,
                    available: available,
                });
                return;
            }
        }
        if (this.notebook._session_starting &&
            this.notebook.session.kernel.name !== ks.name) {
            console.error("Cannot change kernel while waiting for pending session start.");
            return;
        }
        this.current_selection = ks.name;
        this.events.trigger('spec_changed.Kernel', ks);
    };
    
    KernelSelector.prototype._spec_not_found = function (event, data) {
        var that = this;
        var select = $("<select>").addClass('form-control');
        console.warn("Kernelspec not found:", data);
        var names;
        if (data.matches.length > 1) {
            names = data.matches;
        } else {
            names = data.available;
        }
        names.map(function (name) {
            var ks = that.kernelspecs[name];
            select.append(
                $('<option/>').attr('value', ks.name).text(ks.spec.display_name || ks.name)
            );
        });
        
        var no_kernel_msg = i18n.msg.sprintf(i18n.msg._("Could not find a kernel matching %s. Please select a kernel:"),
                (data.selected.display_name || data.selected.name))
        var body = $("<form>").addClass("form-inline").append(
            $("<span>").text(no_kernel_msg)
        ).append(select);

        // This statement is used simply so that message extraction
        // will pick up the strings.  The actual setting of the text
        // for the button is in dialog.js.
        var button_labels = [ i18n.msg._("Continue Without Kernel"), i18n.msg._("Set Kernel"), i18n.msg._("OK") ];
        
        dialog.modal({
            title : i18n.msg._('Kernel not found'),
            body : body,
            buttons : {
                'Continue Without Kernel' : {
                    class : 'btn-danger',
                    click : function () {
                        that.events.trigger('no_kernel.Kernel');
                    }
                },
                'Set Kernel' : {
                    class : 'btn-primary',
                    click : function () {
                        that.set_kernel(select.val());
                    }
                }
            }
        });
    };

    KernelSelector.prototype.new_notebook = function (kernel_name) {
        
        var w = window.open('', IPython._target);
        // Create a new notebook in the same path as the current
        // notebook's path.
        var that = this;
        var parent = utils.url_path_split(that.notebook.notebook_path)[0];
        that.notebook.contents.new_untitled(parent, {type: "notebook"}).then(
            function (data) {
                var url = utils.url_path_join(
                    that.notebook.base_url, that.nbclassic_path, 'notebooks',
                    utils.encode_uri_components(data.path)
                );
                url += "?kernel_name=" + kernel_name;
                w.location = url;
            },
            function(error) {
                w.close();
                dialog.modal({
                    title : i18n.msg._('Creating Notebook Failed'),
                    body : i18n.msg.sprintf(i18n.msg._("The error was: %s"), error.message),
                    buttons : {'OK' : {'class' : 'btn-primary'}}
                });
            }
        );
    };

    KernelSelector.prototype.lock_switch = function() {
        // should set a flag and display warning+reload if user want to
        // re-change kernel. As UI discussion never finish
        // making that a separate PR.
        console.warn('switching kernel is not guaranteed to work !');
    };

    KernelSelector.prototype.bind_events = function() {
        var that = this;
        this.events.on('spec_changed.Kernel', $.proxy(this._spec_changed, this));
        this.events.on('spec_not_found.Kernel', $.proxy(this._spec_not_found, this));
        this.events.on('kernel_created.Session', function (event, data) {
            that.set_kernel(data.kernel.name);
        });
        
        var logo_img = this.element.find("img.current_kernel_logo");
        logo_img.on("load", function() {
            logo_img.show();
        });
        logo_img.on("error", function() {
            logo_img.hide();
        });
    };

    return {'KernelSelector': KernelSelector};
});
