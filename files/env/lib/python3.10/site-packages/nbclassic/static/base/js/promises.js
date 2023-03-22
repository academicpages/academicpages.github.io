// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// Define an object to attach promises to for one-time events.

define(['base/js/events', 'base/js/namespace'], function(events, Jupyter) {
    "use strict";

    // Promise to be resolved when the application is initialized.
    // The value is the name of the app on the current page.
    var app_initialized = new Promise(function(resolve, reject) {
        events.on('app_initialized.NotebookApp', function() {
            resolve('NotebookApp');
        });
        events.on('app_initialized.DashboardApp', function() {
            resolve('DashboardApp');
        });
    });

    var promises = {
        app_initialized: app_initialized
    };
    Jupyter.promises = promises;

    return promises;
});
