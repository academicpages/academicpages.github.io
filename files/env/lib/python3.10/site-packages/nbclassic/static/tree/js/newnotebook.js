// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog',
], function ($, IPython, utils, i18n, dialog) {
    "use strict";
    
    var NewNotebookWidget = function (selector, options) {
        this.selector = selector;
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url;
        this.contents = options.contents;
        this.events = options.events;
        this.default_kernel = null;
        this.kernelspecs = {};
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.request_kernelspecs();
        }
        this.bind_events();
    };
    
    NewNotebookWidget.prototype.bind_events = function () {
        var that = this;
        this.element.find('#new_notebook').click(function () {
            that.new_notebook();
        });
    };
    
    NewNotebookWidget.prototype.request_kernelspecs = function () {
        /** request and then load kernel specs */
        var url = utils.url_path_join(this.base_url, 'api/kernelspecs');
        utils.promising_ajax(url).then($.proxy(this._load_kernelspecs, this));
    };
    
    NewNotebookWidget.prototype._load_kernelspecs = function (data) {
        /** load kernelspec list */
        var that = this;
        this.kernelspecs = data.kernelspecs;
        var menu = this.element.find("#notebook-kernels");
        var keys = Object.keys(data.kernelspecs).sort(function (a, b) {
            var da = data.kernelspecs[a].spec.display_name;
            var db = data.kernelspecs[b].spec.display_name;
            if (da === db) {
                return 0;
            } else if (da > db) {
                return 1;
            } else {
                return -1;
            }
        });

        // Create the kernel list in reverse order because
        // the .after insertion causes each item to be added
        // to the top of the list.
        for (var i = keys.length - 1; i >= 0; i--) {
            var ks = this.kernelspecs[keys[i]];
            var li = $("<li>")
                .attr("id", "kernel-" +ks.name)
                .data('kernelspec', ks).append(
                    $('<a>')
                        .attr("aria-label", ks.name)
                        .attr("role", "menuitem")
                        .attr('href', '#')
                        .click($.proxy(this.new_notebook, this, ks.name))
                        .text(ks.spec.display_name)
                        .attr('title', i18n.sprintf(i18n._('Create a new notebook with %s'), ks.spec.display_name))
                );
            menu.after(li);
        }
        this.events.trigger('kernelspecs_loaded.KernelSpec', data.kernelspecs);
    };
    
    NewNotebookWidget.prototype.new_notebook = function (kernel_name, evt) {
        /** create and open a new notebook */
        var that = this;
        kernel_name = kernel_name || this.default_kernel;
        var w = window.open(undefined, IPython._target);
        var dir_path = $('body').attr('data-notebook-path');
        this.contents.new_untitled(dir_path, {type: "notebook"}).then(
            function (data) {
                var url = utils.url_path_join(
                    that.base_url, that.nbclassic_path, 'notebooks',
                    utils.encode_uri_components(data.path)
                );
                if (kernel_name) {
                    url += "?kernel_name=" + kernel_name;
                }
                w.location = url;
        }).catch(function (e) {
            w.close();
            // This statement is used simply so that message extraction
            // will pick up the strings.  The actual setting of the text
            // for the button is in dialog.js.
            var button_labels = [ i18n._("OK")];
            dialog.modal({
                title : i18n._('Creating Notebook Failed'),
                body : $('<div/>')
                    .text(i18n._("An error occurred while creating a new notebook."))
                    .append($('<div/>')
                        .addClass('alert alert-danger')
                        .text(e.message || e)),
                buttons: {
                    OK: {'class' : 'btn-primary'}
                }
            });
        });
        if (evt !== undefined) {
            evt.preventDefault();
        }
    };
    
    return {'NewNotebookWidget': NewNotebookWidget};
});
