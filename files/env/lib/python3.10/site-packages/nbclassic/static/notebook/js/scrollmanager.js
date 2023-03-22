// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.
define(['jquery'], function($) {
    "use strict";

    var ScrollManager = function(notebook, options) {
        /**
         * Public constructor.
         */
        this.notebook = notebook;
        this.element = $('#site');
        options = options || {};
        this.animation_speed = options.animation_speed || 250; //ms
    };

    ScrollManager.prototype.onScroll = function (func, rate) {
        /**
         * Register a function to be called when the page is scrolled, throttled
         * at a particular rate limit.
         */
         rate = rate || 100; // default rate limit
         this.element.scroll(function () {
             clearTimeout(func._timeout);
             func._timeout = setTimeout(func, rate);
         });
    };

    ScrollManager.prototype.scroll = function (delta) {
        /**
         * Scroll the document.
         *
         * Parameters
         * ----------
         * delta: integer
         *  direction to scroll the document.  Positive is downwards. 
         *  Unit is one page length.
         */
        this.scroll_some(delta);
        return false;
    };

    ScrollManager.prototype.scroll_to = function(selector) {
        /**
         * Scroll to an element in the notebook.
         */
        this.element.animate({'scrollTop': $(selector).offset().top + this.element.scrollTop() - this.element.offset().top}, this.animation_speed);
    };

    ScrollManager.prototype.scroll_some = function(pages) {
        /**
         * Scroll up or down a given number of pages.
         *
         * Parameters
         * ----------
         * pages: integer
         *  number of pages to scroll the document, may be positive or negative.
         */
        this.element.animate({'scrollTop': this.element.scrollTop() + pages * this.element.height()}, this.animation_speed);
    };

    ScrollManager.prototype.get_first_visible_cell = function() {
        /**
         * Gets the index of the first visible cell in the document.
         *
         * First, attempt to be smart by guessing the index of the cell we are
         * scrolled to.  Then, walk from there up or down until the right cell 
         * is found.  To guess the index, get the top of the last cell, and
         * divide that by the number of cells to get an average cell height.  
         * Then divide the scroll height by the average cell height.
         */
        var cell_count = this.notebook.ncells();
        var first_cell_top = this.notebook.get_cell(0).element.offset().top;
        var last_cell_top = this.notebook.get_cell(cell_count-1).element.offset().top;
        var avg_cell_height = (last_cell_top - first_cell_top) / cell_count;
        var i = Math.ceil(this.element.scrollTop() / avg_cell_height);
        i = Math.min(Math.max(i , 0), cell_count - 1);

        while (this.notebook.get_cell(i).element.offset().top - first_cell_top < this.element.scrollTop() && i < cell_count - 1) {
            i += 1;
        } 

        while (this.notebook.get_cell(i).element.offset().top - first_cell_top > this.element.scrollTop() - 50 && i >= 0) {
            i -= 1;
        } 
        return Math.min(i + 1, cell_count - 1);
    };

    ScrollManager.prototype.is_cell_visible = function (cell) {
        var cell_rect = cell.element[0].getBoundingClientRect();
        var scroll_rect = this.element[0].getBoundingClientRect();
        return ((cell_rect.top <= scroll_rect.bottom) && (cell_rect.bottom >= scroll_rect.top));
    };


    var TargetScrollManager = function(notebook, options) {
        /**
         * Public constructor.
         */
        ScrollManager.apply(this, [notebook, options]);
    };
    TargetScrollManager.prototype = Object.create(ScrollManager.prototype);

    TargetScrollManager.prototype.is_target = function (index) {
        /**
         * Check if a cell should be a scroll stop.
         *
         * Returns `true` if the cell is a cell that the scroll manager
         * should scroll to.  Otherwise, false is returned. 
         *
         * Parameters
         * ----------
         * index: integer
         *  index of the cell to test.
         */
        return false;
    };

    TargetScrollManager.prototype.scroll = function (delta) {
        /**
         * Scroll the document.
         *
         * Parameters
         * ----------
         * delta: integer
         *  direction to scroll the document.  Positive is downwards.
         *  Units are targets.
         *
         * Try to scroll to the next slide.
         */
        var cell_count = this.notebook.ncells();
        var selected_index = this.get_first_visible_cell() + delta;
        while (0 <= selected_index && selected_index < cell_count && !this.is_target(selected_index)) {
            selected_index += delta;
        }

        if (selected_index < 0 || cell_count <= selected_index) {
            return ScrollManager.prototype.scroll.apply(this, [delta]);
        } else {
            this.scroll_to(this.notebook.get_cell(selected_index).element);
            
            // Cancel browser keyboard scroll.
            return false;
        }
    };


    var SlideScrollManager = function(notebook, options) {
        /**
         * Public constructor.
         */
        TargetScrollManager.apply(this, [notebook, options]);
    };
    SlideScrollManager.prototype = Object.create(TargetScrollManager.prototype);

    SlideScrollManager.prototype.is_target = function (index) {
        var cell = this.notebook.get_cell(index);
        return cell.metadata && cell.metadata.slideshow && 
            cell.metadata.slideshow.slide_type && 
            (cell.metadata.slideshow.slide_type === "slide" ||
            cell.metadata.slideshow.slide_type === "subslide");
    };


    var HeadingScrollManager = function(notebook, options) {
        /**
         * Public constructor.
         */
        ScrollManager.apply(this, [notebook, options]);
        options = options || {};
        this._level = options.heading_level || 1;
    };
    HeadingScrollManager.prototype = Object.create(ScrollManager.prototype);

    HeadingScrollManager.prototype.scroll = function (delta) {
        /**
         * Scroll the document.
         *
         * Parameters
         * ----------
         * delta: integer
         *  direction to scroll the document.  Positive is downwards.
         *  Units are headers.
         *
         * Get all of the header elements that match the heading level or are of
         * greater magnitude (a smaller header number).
         */
        var headers = $();
        var i;
        for (i = 1; i <= this._level; i++) {
            headers = headers.add('#notebook-container h' + i);
        }

        // Find the header the user is on or below.
        var first_cell_top = this.notebook.get_cell(0).element.offset().top;
        var current_scroll = this.element.scrollTop();
        var header_scroll = 0;
        i = -1;
        while (current_scroll >= header_scroll && i < headers.length) {
            if (++i < headers.length) {
                header_scroll = $(headers[i]).offset().top - first_cell_top;
            }
        }
        i--;

        // Check if the user is below the header.
        if (i < 0 || current_scroll > $(headers[i]).offset().top - first_cell_top + 30) {
            // Below the header, count the header as a target.
            if (delta < 0) {
                delta += 1;
            }
        }
        i += delta;

        // Scroll!
        if (0 <= i && i < headers.length) {
            this.scroll_to(headers[i]);
            return false;
        } else {
            // Default to the base's scroll behavior when target header doesn't
            // exist.
            return ScrollManager.prototype.scroll.apply(this, [delta]);
        }
    };

    // Return namespace for require.js loads
    return {
        'ScrollManager': ScrollManager,
        'SlideScrollManager': SlideScrollManager,
        'HeadingScrollManager': HeadingScrollManager,
        'TargetScrollManager': TargetScrollManager
    };
});
