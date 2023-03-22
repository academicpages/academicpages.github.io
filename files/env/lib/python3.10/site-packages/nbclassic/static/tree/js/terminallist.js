// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils',
    'base/js/i18n',
    'tree/js/notebooklist',
], function($, IPython, utils, i18n, notebooklist) {
    "use strict";

    var TerminalList = function (selector, options) {
        /**
         * Constructor
         *
         * Parameters:
         *  selector: string
         *  options: dictionary
         *      Dictionary of keyword arguments.
         *          base_url: string
         */
         this.nbclassic_path = options.nbclassic_path;
         this.base_url = options.base_url || utils.get_body_data("baseUrl");
        this.element_name = options.element_name || 'running';
        this.selector = selector;
        this.terminals = [];
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.style();
            this.bind_events();
            this.load_terminals();
        }
    };

    TerminalList.prototype = Object.create(notebooklist.NotebookList.prototype);

    TerminalList.prototype.bind_events = function () {
        var that = this;
        $('#refresh_' + this.element_name + '_list').click(function () {
            that.load_terminals();
        });
        $('#new-terminal').click($.proxy(this.new_terminal, this));
    };

    TerminalList.prototype.new_terminal = function (event) {
        if (event) {
            event.preventDefault();
        }
        var w = window.open('#', IPython._target);
        var base_url = this.base_url;
        var settings = {
            type : "POST",
            dataType: "json",
            success : function (data, status, xhr) {
                var name = data.name;
                w.location = utils.url_path_join(base_url, 'terminals', 
                    utils.encode_uri_components(name));
            },
            error : function(jqXHR, status, error){
                w.close();
                utils.log_ajax_error(jqXHR, status, error);
            },
        };
        var url = utils.url_path_join(
            this.base_url,
            'api/terminals'
        );
        utils.ajax(url, settings);
    };
    
    TerminalList.prototype.load_terminals = function() {
        var url = utils.url_path_join(this.base_url, 'api/terminals');
        utils.ajax(url, {
            type: "GET",
            cache: false,
            dataType: "json",
            success: $.proxy(this.terminals_loaded, this),
            error : utils.log_ajax_error
        });
    };

    TerminalList.prototype.terminals_loaded = function (data) {
        this.terminals = data;
        this.clear_list();
        var item, term;
        for (var i=0; i < this.terminals.length; i++) {
            term = this.terminals[i];
            item = this.new_item(-1);
            this.add_link(term.name, item);
            this.add_shutdown_button(term.name, item);
        }
        $('#terminal_list_header').toggle(data.length === 0);
    };
    
    TerminalList.prototype.add_link = function(name, item) {
        item.data('term-name', name);
        item.find(".item_name").text("terminals/" + name);
        item.find(".item_icon").addClass("fa fa-terminal");
        var link = item.find("a.item_link")
            .attr('href', utils.url_path_join(this.base_url, "terminals",
                utils.encode_uri_components(name)));
        link.attr('target', IPython._target||'_blank');
        this.add_shutdown_button(name, item);
    };
    
    TerminalList.prototype.add_shutdown_button = function(name, item) {
        var that = this;
        var shutdown_button = $("<button/>").text(i18n._("Shutdown")).addClass("btn btn-xs btn-warning").
            click(function (e) {
                var settings = {
                    processData : false,
                    type : "DELETE",
                    dataType : "json",
                    success : function () {
                        that.load_terminals();
                    },
                    error : utils.log_ajax_error,
                };
                var url = utils.url_path_join(that.base_url, 'api/terminals',
                    utils.encode_uri_components(name));
                utils.ajax(url, settings);
                return false;
            });
        item.find(".item_buttons").text("").append(shutdown_button);
    };

    return {TerminalList: TerminalList};
});
