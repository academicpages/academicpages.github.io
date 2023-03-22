// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

requirejs([
    'jquery',
    'base/js/utils',
    'base/js/page',
    'auth/js/loginwidget',
    'services/config',
    'terminal/js/terminado',
    'custom-preload'
], function(
    $,
    utils,
    page,
    loginwidget,
    configmod,
    terminado
    ){
    "use strict";
    requirejs(['custom/custom'], function() {});
    page = new page.Page('div#header', 'div#site');

    var common_options = {
        base_url : utils.get_body_data("baseUrl"),
        nbclassic_path: document.nbclassicPath || ""
    };

    var config = new configmod.ConfigSection('terminal', common_options);
    config.load();
    var common_config = new configmod.ConfigSection('common', common_options);
    common_config.load();

    // This makes the 'logout' button in the top right work.
    var login_widget = new loginwidget.LoginWidget('span#login_widget', common_options);

    var base_url = utils.get_body_data('baseUrl').replace(/\/?$/, '/');
    var ws_path = utils.get_body_data('wsPath');
    var ws_url = utils.get_body_data('wsUrl');
    if (!ws_url) {
        // trailing 's' in https will become wss for secure web sockets
        ws_url = location.protocol.replace('http', 'ws') + "//" + location.host;
    }
    ws_url = ws_url + base_url + ws_path;
    
    page.show_header();
    
    var terminal = terminado.make_terminal($("#terminado-container")[0], ws_url);
    
    page.show_site();
    
    utils.load_extensions_from_config(config);
    utils.load_extensions_from_config(common_config);
    
    window.onresize = function() {
      terminal.term.fit();
      // send the new size to the server so that it can trigger a resize in the running process.
      terminal.socket.send(JSON.stringify(["set_size", terminal.term.rows, terminal.term.cols,
                                    $(window).height(), $(window).width()]));
    };

    // Expose terminal for fiddling with in the browser
    window.terminal = terminal;

});
