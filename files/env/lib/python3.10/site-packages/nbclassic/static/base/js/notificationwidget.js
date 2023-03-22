// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['jquery'], function($) {
    "use strict";

    /**
     * Construct a NotificationWidget object.
     *
     * @constructor
     * @param {string} selector - a jQuery selector string for the
     * notification widget element
     */
    var NotificationWidget = function (selector) {
        this.selector = selector;
        this.timeout = null;
        this.busy = false;
        if (this.selector !== undefined) {
            this.element = $(selector);
            this.style();
        }
        this.element.hide();
        this.inner = $('<span/>');
        this.element.append(this.inner);
    };

    /**
     * Add the 'notification_widget' CSS class to the widget element.
     *
     * @method style
     */
    NotificationWidget.prototype.style = function () {
        // use explicit bootstrap classes here,
        // because multiple inheritance in LESS doesn't work
        // for this particular combination
        this.element.addClass('notification_widget btn btn-xs navbar-btn');
    };
   
    /**
     * hide the widget and empty the text
     **/
    NotificationWidget.prototype.hide = function () {
        var that = this;
        this.element.fadeOut(100, function(){that.inner.text('');});
    };

    /**
     * Set the notification widget message to display for a certain
     * amount of time (timeout).  The widget will be shown forever if
     * timeout is <= 0 or undefined. If the widget is clicked while it
     * is still displayed, execute an optional callback
     * (click_callback). If the callback returns false, it will
     * prevent the notification from being dismissed.
     *
     * Options:
     *    class - CSS class name for styling
     *    icon - CSS class name for the widget icon
     *    title - HTML title attribute for the widget
     *
     * @method set_message
     * @param {string} msg - The notification to display
     * @param {integer} [timeout] - The amount of time in milliseconds to display the widget
     * @param {function} [click_callback] - The function to run when the widget is clicked
     * @param {Object} [options] - Additional options
     */
    NotificationWidget.prototype.set_message = function (msg, timeout, click_callback, options) {
        options = options || {};

        // unbind potential previous callback
        this.element.unbind('click');
        this.inner.attr('class', options.icon);
        this.inner.attr('title', options.title);
        this.inner.text(msg);
        this.element.fadeIn(100);

        // reset previous set style
        this.element.removeClass();
        this.style();
        if (options.class) {
            this.element.addClass(options.class);
        }

        // clear previous timer
        if (this.timeout !== null) {
            clearTimeout(this.timeout);
            this.timeout = null;
        }

        // set the timer if a timeout is given
        var that = this;
        if (timeout !== undefined && timeout >= 0) {
            this.timeout = setTimeout(function () {
                that.element.fadeOut(100, function () {that.inner.text('');});
                that.element.unbind('click');
                that.timeout = null;
            }, timeout);
        }

        // if no click callback assume we will just dismiss the notification
        if (click_callback === undefined) {
            click_callback = function(){return true};
        }
        // on click, remove widget if click callback say so
        // and unbind click event.
        this.element.click(function () {
            if (click_callback() !== false) {
                that.element.fadeOut(100, function () {that.inner.text('');});
                that.element.unbind('click');
            }
            if (that.timeout !== null) {
                clearTimeout(that.timeout);
                that.timeout = null;
            }
        });
    };

    /**
     * Display an information message (styled with the 'info'
     * class). Arguments are the same as in set_message. Default
     * timeout is 3500 milliseconds.
     *
     * @method info
     */
    NotificationWidget.prototype.info = function (msg, timeout, click_callback, options) {
        options = options || {};
        options.class = options.class + ' info';
        timeout = timeout || 3500;
        this.set_message(msg, timeout, click_callback, options);
    };

    /**
     * Display a warning message (styled with the 'warning'
     * class). Arguments are the same as in set_message. Messages are
     * sticky by default.
     *
     * @method warning
     */
    NotificationWidget.prototype.warning = function (msg, timeout, click_callback, options) {
        options = options || {};
        options.class = options.class + ' warning';
        this.set_message(msg, timeout, click_callback, options);
    };

    /**
     * Display a danger message (styled with the 'danger'
     * class). Arguments are the same as in set_message. Messages are
     * sticky by default.
     *
     * @method danger
     */
    NotificationWidget.prototype.danger = function (msg, timeout, click_callback, options) {
        options = options || {};
        options.class = options.class + ' danger';
        this.set_message(msg, timeout, click_callback, options);
    };

    /**
     * Get the text of the widget message.
     *
     * @method get_message
     * @return {string} - the message text
     */
    NotificationWidget.prototype.get_message = function () {
        return this.inner.html();
    };

    return {'NotificationWidget': NotificationWidget};
});
