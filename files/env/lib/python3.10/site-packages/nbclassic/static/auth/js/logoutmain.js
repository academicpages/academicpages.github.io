// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['base/js/namespace', 'base/js/page'], function(IPython, page) {
    function logout_main() {
        var page_instance = new page.Page('div#header', 'div#site');
        page_instance.show();

        IPython.page = page_instance;
    }
    return logout_main;
});
