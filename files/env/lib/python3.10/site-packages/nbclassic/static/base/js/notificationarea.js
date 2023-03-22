// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/notificationwidget',
], function($, notificationwidget) {
    "use strict";

    // store reference to the NotificationWidget class
    var NotificationWidget = notificationwidget.NotificationWidget;

    /**
     * Construct the NotificationArea object. Options are:
     *     events: $(Events) instance
     *     save_widget: SaveWidget instance
     *     notebook: Notebook instance
     *     keyboard_manager: KeyboardManager instance
     *
     * @constructor
     * @param {string} selector - a jQuery selector string for the
     * notification area element
     * @param {Object} [options] - a dictionary of keyword arguments.
     */
    var NotificationArea = function (selector, options) {
        this.selector = selector;
        this.events = options.events;
        if (this.selector !== undefined) {
            this.element = $(selector);
        }
        this.widget_dict = {};
    };

    /**
     * Get a widget by name, creating it if it doesn't exist.
     *
     * @method widget
     * @param {string} name - the widget name
     */
    NotificationArea.prototype.widget = function (name) {
        if (this.widget_dict[name] === undefined) {
            return this.new_notification_widget(name);
        }
        return this.get_widget(name);
    };

    /**
     * Get a widget by name, throwing an error if it doesn't exist.
     *
     * @method get_widget
     * @param {string} name - the widget name
     */
    NotificationArea.prototype.get_widget = function (name) {
        if(this.widget_dict[name] === undefined) {
            throw new Error('no widgets with this name');
        }
        return this.widget_dict[name];
    };

    /**
     * Create a new notification widget with the given name. The
     * widget must not already exist.
     *
     * @method new_notification_widget
     * @param {string} name - the widget name
     */
    NotificationArea.prototype.new_notification_widget = function (name) {
        if (this.widget_dict[name] !== undefined) {
            throw new Error('widget with that name already exists!');
        }

        // create the element for the notification widget and add it
        // to the notification aread element
        var div = $('<div/>').attr('id', 'notification_' + name);
        $(this.selector).append(div);

        // create the widget object and return it
        this.widget_dict[name] = new NotificationWidget('#notification_' + name);
        return this.widget_dict[name];
    };

    return {'NotificationArea': NotificationArea};
});
