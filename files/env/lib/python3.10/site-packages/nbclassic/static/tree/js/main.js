// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

// adapted from Mozilla Developer Network example at
// https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Function/bind
// shim `bind` for testing under casper.js
var bind = function bind(obj) {
  var slice = [].slice;
  var args = slice.call(arguments, 1),
    self = this,
    nop = function() {
    },
    bound = function() {
      return self.apply(this instanceof nop ? this : (obj || {}), args.concat(slice.call(arguments)));
    };
  nop.prototype = this.prototype || {}; // Firefox cries sometimes if prototype is undefined
  bound.prototype = new nop();
  return bound;
};
Function.prototype.bind = Function.prototype.bind || bind ;


requirejs([
    'jquery',
    'contents',
    'base/js/namespace',
    'base/js/dialog',
    'base/js/events',
    'base/js/promises',
    'base/js/page',
    'base/js/utils',
    'services/config',
    'tree/js/notebooklist',
    'tree/js/sessionlist',
    'tree/js/kernellist',
    'tree/js/terminallist',
    'tree/js/newnotebook',
    'tree/js/shutdownbutton',
    'auth/js/loginwidget',
    'bidi/bidi',
    'custom-preload'
], function(
    $,
    contents_service,
    IPython,
    dialog,
    events,
    promises,
    page,
    utils,
    config,
    notebooklist,
    sesssionlist,
    kernellist,
    terminallist,
    newnotebook,
    shutdownbutton,
    loginwidget,
    bidi){
    "use strict";
    
    try{
        requirejs(['custom/custom'], function() {});
        bidi.loadLocale();
    } catch(err) {
        console.log("Error loading custom.js from tree service. Continuing and logging");
        console.warn(err);
    }

    console.log('Welcome to Project Jupyter! Explore the various tools available and their corresponding documentation. If you are interested in contributing to the platform, please visit the community resources section at http://jupyter.org/community.html.');


    // Setup all of the config related things

    var common_options = {
        base_url: utils.get_body_data("baseUrl"),
        nbclassic_path: document.nbclassicPath || "",
        notebook_path: utils.get_body_data("notebookPath"),
    };
    var cfg = new config.ConfigSection('tree', common_options);
    cfg.load();
    common_options.config = cfg;
    var common_config = new config.ConfigSection('common', common_options);
    common_config.load();

    // Instantiate the main objects

    page = new page.Page('div#header', 'div#site');

    var session_list = new sesssionlist.SesssionList($.extend({
        events: events},
        common_options));
    var contents = new contents_service.Contents({
        base_url: common_options.base_url,
        common_config: common_config
    });
    IPython.NotebookList = notebooklist.NotebookList;
    var notebook_list = new notebooklist.NotebookList('#notebook_list', $.extend({
        contents: contents,
        session_list:  session_list},
        common_options));
    var kernel_list = new kernellist.KernelList('#running_list',  $.extend({
        session_list:  session_list},
        common_options));
    
    var terminal_list;
    if (utils.get_body_data("terminalsAvailable") === "True") {
        terminal_list = new terminallist.TerminalList('#terminal_list', common_options);
    }

    var login_widget = new loginwidget.LoginWidget('#login_widget', common_options);

    var new_buttons = new newnotebook.NewNotebookWidget("#new-buttons",
        $.extend(
            {contents: contents, events: events},
            common_options
        )
    );

    var interval_id=0;
    // auto refresh every xx secondes, no need to be fast,
    //  update is done most of the time when page get focus
    IPython.tree_time_refresh = 60; // in sec

    // limit refresh on focus at 1/10sec, otherwise this
    // can cause too frequent refresh on switching through windows or tabs.
    IPython.min_delta_refresh = 10; // in sec

    var _last_refresh = null;

    var _refresh_list = function(){
        _last_refresh = new Date();
        session_list.load_sessions();
        if (terminal_list) {
            terminal_list.load_terminals();
        }
    };

    var enable_autorefresh = function(){
        /**
         *refresh immediately , then start interval
         */
        var now = new Date();

        if (now - _last_refresh < IPython.min_delta_refresh*1000){
            console.log("Reenabling autorefresh too close to last tree refresh, not refreshing immediately again.");
        } else {
            _refresh_list();
        }
        if (!interval_id){
            interval_id = setInterval(_refresh_list,
                    IPython.tree_time_refresh*1000
            );
        }
    };

    var disable_autorefresh = function(){
        clearInterval(interval_id);
        interval_id = 0;
    };

    // stop autorefresh when page lose focus
    $(window).blur(function() {
        disable_autorefresh();
    });

    //re-enable when page get focus back
    $(window).focus(function() {
        enable_autorefresh();
    });

    // finally start it, it will refresh immediately
    enable_autorefresh();

    page.show();

    // For backwards compatibility.
    IPython.page = page;
    IPython.notebook_list = notebook_list;
    IPython.session_list = session_list;
    IPython.kernel_list = kernel_list;
    IPython.login_widget = login_widget;
    IPython.new_notebook_widget = new_buttons;

    events.trigger('app_initialized.DashboardApp');
    
    // Now actually load nbextensions
    utils.load_extensions_from_config(cfg);
    utils.load_extensions_from_config(common_config);
    
    // bound the upload method to the on change of the file select list
    $("#alternate_upload").change(function (event){
        notebook_list.handleFilesUpload(event,'form');
    });

    // bound the the span around the input file upload to enable keyboard click
    $("#upload_span").keydown(function (event) {
        var key = event.which;
        if ((key === 13) || (key === 32)) {
            event.preventDefault();
            $("#upload_span_input").click();
        }
    })
    
    // set hash on tab click
    $("#tabs").find("a").click(function(e) {
        // Prevent the document from jumping when the active tab is changed to a 
        // tab that has a lot of content.
        e.preventDefault();

        // Set the hash without causing the page to jump.
        // https://stackoverflow.com/a/14690177/2824256
        var hash = $(this).attr("href");
        if(window.history.pushState) {
            window.history.pushState(null, null, hash);
        } else {
            window.location.hash = hash;
        }
    });
    
    // load tab if url hash
    if (window.location.hash) {
        $("#tabs").find("a[href='" + window.location.hash + "']").click();
    }
    
    shutdownbutton.activate();
});
