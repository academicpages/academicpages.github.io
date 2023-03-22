// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.


var Jupyter = Jupyter || {};

var jprop = function(name, module_path){
    Object.defineProperty(Jupyter, name, {
      get: function() { 
          console.warn('accessing `'+name+'` is deprecated. Use `requirejs("'+module_path+'")`');
          return requirejs(module_path); 
      },
      enumerable: true,
      configurable: false
    });
}

var jglobal = function(name, module_path){
    Object.defineProperty(Jupyter, name, {
      get: function() { 
          console.warn('accessing `'+name+'` is deprecated. Use `requirejs("'+module_path+'").'+name+'`');
          return requirejs(module_path)[name]; 
      },
      enumerable: true,
      configurable: false
    });
}

define(function(){
    "use strict";

    // expose modules
    
    jprop('utils','base/js/utils')
    jprop('mathjaxutils','base/js/mathjaxutils');

    //Jupyter.load_extensions = Jupyter.utils.load_extensions;
    // 
    jprop('security','base/js/security');
    jprop('keyboard','base/js/keyboard');
    jprop('dialog','base/js/dialog');


    //// exposed constructors
    jglobal('CommManager','services/kernels/comm')
    jglobal('Comm','services/kernels/comm')

    jglobal('NotificationWidget','base/js/notificationwidget');
    jglobal('Kernel','services/kernels/kernel');
    jglobal('Session','services/sessions/session');
    jglobal('LoginWidget','auth/js/loginwidget');
    jglobal('Page','base/js/page');

    // notebook
    jglobal('TextCell','notebook/js/textcell');
    jglobal('OutputArea','notebook/js/outputarea');
    jglobal('KeyboardManager','notebook/js/keyboardmanager');
    jglobal('Completer','notebook/js/completer');
    jglobal('Notebook','notebook/js/notebook');
    jglobal('Tooltip','notebook/js/tooltip');
    jglobal('Toolbar','notebook/js/toolbar');
    jglobal('SaveWidget','notebook/js/savewidget');
    jglobal('Pager','notebook/js/pager');
    jglobal('QuickHelp','notebook/js/quickhelp');
    jglobal('MarkdownCell','notebook/js/textcell');
    jglobal('RawCell','notebook/js/textcell');
    jglobal('Cell','notebook/js/cell');
    jglobal('MainToolBar','notebook/js/maintoolbar');
    jglobal('NotebookNotificationArea','notebook/js/notificationarea');
    jglobal('NotebookTour', 'notebook/js/tour');
    jglobal('MenuBar', 'notebook/js/menubar');

    // tree
    jglobal('SessionList','tree/js/sessionlist');

    Jupyter.version = "0.4.8";
    Jupyter._target = '_blank';

    return Jupyter;
});

// deprecated since 4.0, remove in 5+
var IPython = Jupyter;
