// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

requirejs([
    'jquery',
    'contents',
    'base/js/namespace',
    'base/js/utils',
    'base/js/page',
    'base/js/events',
    'services/config',
    'edit/js/editor',
    'edit/js/menubar',
    'edit/js/savewidget',
    'edit/js/notificationarea',
    'bidi/bidi',
    'auth/js/loginwidget', 
    'custom-preload'
], function(
    $,
    contents_service,
    IPython,
    utils,
    page,
    events,
    configmod,
    editmod,
    menubar,
    savewidget,
    notificationarea,
    bidi,
    loginwidget,
    ){
    "use strict";

    try {
        requirejs(['custom/custom'], function() {});
        bidi.loadLocale();
    } catch(err) {
        console.log("Error loading custom.js from edition service. Continuing and logging");
        console.warn(err);
    }
    
    page = new page.Page('div#header', 'div#site');

    var base_url = utils.get_body_data('baseUrl');
    var file_path = utils.get_body_data('filePath');
    // This enables logout
    var login_widget = new loginwidget.LoginWidget('#login_widget', {
        base_url: base_url
    });
    var config = new configmod.ConfigSection('edit', {base_url: base_url});
    config.load();
    var common_config = new configmod.ConfigSection('common', {base_url: base_url});
    common_config.load();
    var contents = new contents_service.Contents({
        base_url: base_url,
        common_config: common_config
    });
    
    var editor = new editmod.Editor('#texteditor-container', {
        base_url: base_url,
        events: events,
        contents: contents,
        file_path: file_path,
        config: config,
    });
    
    // Make it available for debugging
    IPython.editor = editor;
    
    var save_widget = new savewidget.SaveWidget('span#save_widget', {
        editor: editor,
        events: events,
    });
    
    var menus = new menubar.MenuBar('#menubar', {
        base_url: base_url,
        editor: editor,
        events: events,
        save_widget: save_widget,
    });
    
    var notification_area = new notificationarea.EditorNotificationArea(
        '#notification_area', {
        events: events,
    });
    editor.notification_area = notification_area;
    notification_area.init_notification_widgets();

    utils.load_extensions_from_config(config);
    utils.load_extensions_from_config(common_config);
    editor.load();
    page.show();

    window.onbeforeunload = function () {
        if (editor.save_enabled && !editor.codemirror.isClean(editor.generation)) {
            return "Unsaved changes will be lost. Close anyway?";
        }
    };

    // Make sure the codemirror editor is sized appropriately.
    var _handle_resize = function() {
        var backdrop = $("#texteditor-backdrop");

        // account for padding on the backdrop wrapper
        var padding = backdrop.outerHeight(true) - backdrop.height();
        $('div.CodeMirror').height($("#site").height() - padding);
    };
    $(window).resize(_handle_resize);

    // On document ready, resize codemirror.
    $(document).ready(_handle_resize);
});
