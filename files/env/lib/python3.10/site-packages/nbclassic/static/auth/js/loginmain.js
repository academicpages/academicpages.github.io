// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['jquery', 'base/js/namespace', 'base/js/page'], function($, IPython, page) {
    function login_main() {
      var page_instance = new page.Page('div#header', 'div#site');
      page_instance.show();
      $('input#password_input').focus();
      IPython.page = page_instance;
    }
    return login_main;
});
