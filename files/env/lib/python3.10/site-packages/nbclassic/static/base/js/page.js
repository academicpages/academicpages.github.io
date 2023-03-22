// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/events',
], function($, events){
    "use strict";

    var Page = function (header_div_selector, site_div_selector) {
        /**
        * Constructor
        *
        * Parameters
        * header_div_selector: string
        * site_div_selector: string
        */
        this.header_div_element = $(header_div_selector || 'div#header');
        this.site_div_element = $(site_div_selector || 'div#site');

        this.bind_events();
    };

    Page.prototype.bind_events = function () {
        // resize site on:
        // - window resize
        // - header change
        // - page load
        var _handle_resize = $.proxy(this._resize_site, this);

        $(window).resize(_handle_resize);

        // On document ready, resize codemirror.
        $(document).ready(_handle_resize);
        events.on('resize-header.Page', _handle_resize);
    };

    Page.prototype.show = function () {
        /**
         * The header and site divs start out hidden to prevent FLOUC.
         * Main scripts should call this method after styling everything.
         */
        this.show_header();
        this.show_site();
    };

    Page.prototype.show_header = function () {
        /**
         * The header and site divs start out hidden to prevent FLOUC.
         * Main scripts should call this method after styling everything.
         */
        this.header_div_element.css('display','block');
    };

    Page.prototype.show_site = function () {
        /**
         * The header and site divs start out hidden to prevent FLOUC.
         * Main scripts should call this method after styling everything.
         */
        this.site_div_element.css('display', 'block');
        this._resize_site();
    };

    Page.prototype._resize_site = function(e) {
        /**
         * Update the site's size.
         */

        // In the case an event is passed in, only trigger if the event does
        // *not* have a target DOM node (i.e., it is not bubbling up). See
        // https://bugs.jquery.com/ticket/9841#comment:8
        if (!(e && e.target && e.target.tagName)) {
            $('div#site').height($(window).height() - $('#header').height());
        }
    };

    return {'Page': Page};
});
