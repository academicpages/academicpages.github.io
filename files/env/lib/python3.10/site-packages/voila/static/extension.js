/*
 * Copyright (c) 2018, Voilà Contributors
 * Copyright (c) 2018, QuantStack
 *
 * Distributed under the terms of the BSD 3-Clause License.
 *
 * The full license is in the file LICENSE, distributed with this software.
 */

define(['jquery', 'base/js/namespace'], function($, Jupyter) {
    "use strict";
    var open_voila = function() {
        Jupyter.notebook.save_notebook().then(function () {
            let voila_url = Jupyter.notebook.base_url + "voila/render/" + Jupyter.notebook.notebook_path;
            window.open(voila_url)
        });
    }
    var load_ipython_extension = function() {
        Jupyter.toolbar.add_buttons_group([{
            id : 'toggle_codecells',
            label : 'Voilà',
            icon : 'fa-desktop',
            callback : open_voila
        }]);
    };
    return {
        load_ipython_extension : load_ipython_extension
    };
});
