// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// Define promises for notebook events.

define(['base/js/events', 'base/js/promises'], function(events, promises) {
    "use strict";

    // Promise to be resolved when the notebook is *initially* loaded.
    // The event may fire again if the notebook is reloaded later, but this
    // promise only tracks the initial load.
    promises.notebook_loaded = new Promise(function(resolve, reject) {
        events.one('notebook_loaded.Notebook', function() {
            resolve();
        });
        events.one('notebook_load_failed.Notebook', function() {
            reject();
        });
    });

    return promises;
});
