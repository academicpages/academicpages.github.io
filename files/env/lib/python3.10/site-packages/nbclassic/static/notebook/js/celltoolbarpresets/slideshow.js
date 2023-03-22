// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'notebook/js/celltoolbar',
    'base/js/i18n'
], function(celltoolbar, i18n) {
    "use strict";

    var CellToolbar = celltoolbar.CellToolbar;
    var slideshow_preset = [];

    var select_type = CellToolbar.utils.select_ui_generator([
            ["-"            ,"-"            ],
            [i18n.msg._("Slide")        ,"slide"        ],
            [i18n.msg._("Sub-Slide")    ,"subslide"     ],
            [i18n.msg._("Fragment")     ,"fragment"     ],
            [i18n.msg._("Skip")         ,"skip"         ],
            [i18n.msg._("Notes")        ,"notes"        ],
            ],
            // setter
            function(cell, value){
                // we check that the slideshow namespace exist and create it if needed
                if (cell.metadata.slideshow === undefined){cell.metadata.slideshow = {};}
                // set the value
                cell.metadata.slideshow.slide_type = value;
                },
            // getter
            function(cell){ var ns = cell.metadata.slideshow;
                // if the slideshow namespace does not exist return `undefined`
                // (will be interpreted as `false` by checkbox) otherwise
                // return the value
                return (ns === undefined)? undefined: ns.slide_type;
                },
            i18n.msg._("Slide Type"));

    var register = function (notebook) {
        CellToolbar.register_callback('slideshow.select',select_type);
        slideshow_preset.push('slideshow.select');

        CellToolbar.register_preset(i18n.msg._('Slideshow'),slideshow_preset, notebook);
    };
    return {'register': register};
});
