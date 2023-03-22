// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/namespace',
    'base/js/utils',
    'base/js/i18n',
    'base/js/dialog'
], function($, Jupyter, utils, i18n, dialog) {

var jcbprefix = '<pre class="jupyter-nb-cells-json">';
var jcbsuffix = '</pre>';

function store_json(cells, clipboard) {
  // Firefox ignores application/json mime type, so put it in HTML as well.
  // We also copy a text version so you can paste cell sources into a text editor
  var j = JSON.stringify(cells);
  var t = cells.map(function(c) {return c.source;}).join('\n\n');
  clipboard.setData('text/plain', t);
  clipboard.setData('text/html', jcbprefix + j + jcbsuffix);
  clipboard.setData('application/json', j);
}

function load_json(clipboard) {
  var s = clipboard.getData('text/html');
  // System/browsers may add some more stuff before/after our content, so
  // find where our prefix and suffix are.
  var pix = s.indexOf(jcbprefix);
  var six = s.lastIndexOf(jcbsuffix);
  if (pix === -1 || six === -1) {
    return null;
  }
  return JSON.parse(s.slice(pix + jcbprefix.length, six));
}

function isProgrammaticCopy(event) {
  return (typeof(event.target.selectionStart) !== 'undefined'
    && typeof(event.target.selectionEnd) !== 'undefined'
    && ((event.target.selectionEnd - event.target.selectionStart) > 0));
}

function copy(event) {
  if ((Jupyter.notebook.mode !== 'command') ||
        // window.getSelection checks if text is selected, e.g. in output
        !window.getSelection().isCollapsed ||
        // Allow programmatic copy
        isProgrammaticCopy(event)) {
    return;
  }
  var selecn = Jupyter.notebook.get_selected_cells().map(
    function(c) { return c.toJSON();});
  store_json(selecn, event.clipboardData);
  event.preventDefault();
}

function paste(event) {
  if (Jupyter.notebook.mode !== 'command') {
    return;
  }
  console.log(i18n.msg.sprintf(i18n.msg._('Clipboard types: %s'),event.clipboardData.types));
  cells = load_json(event.clipboardData);
  // console.log(cells);
  // Does this JSON look like cells?
  if (Array.isArray(cells) && (cells.length > 0) &&
      cells[0].cell_type && cells[0].source) {
    var first_inserted = null;
    for (var i=0; i < cells.length; i++) {
        var cell_data = cells[i];
        var new_cell = Jupyter.notebook.insert_cell_above(cell_data.cell_type);
        new_cell.fromJSON(cell_data);
        if (first_inserted === null) {
            first_inserted = new_cell;
        }
    }
    first_inserted.focus_cell();
  }
  event.preventDefault();
}

function notebookOnlyEvent(callback) {
    // Only call the callback to redirect the event if the notebook should be
    // handling the events, at the discretion of the keyboard manager.
    // If the focus is in a text widget or something (kbmanager disabled),
    // allow the default event.
    return function() {
        if (Jupyter.keyboard_manager.enabled) {
            callback.apply(this, arguments);
        }
    };
}

function needs_text_box_for_paste_event() {
  // I know this is bad, but I don't know a better way to check this
  return navigator.userAgent.indexOf('Firefox') !== -1;
}

function setup_paste_dialog() {
  // Firefox only fires a paste event if the cursor is in a text input. So, on
  // Ctrl-V, bring up a dialog with an invisible text box and catch the
  // second Ctrl-V
  var action = {
      icon: 'fa-clipboard', // a font-awesome class used on buttons, etc
      help    : i18n.msg._('Dialog for paste from system clipboard'),
      help_index : 'zz',
      handler : function () {
        var entry_box = $('<input type="text"/>');
        entry_box.css('opacity', 0);
        function paste_close_dlg(e) {
          paste(e);
          // There must be a better way to do this, but it's not any of:
          // .hide(), .remove() or .dialog('close')
          paste_dlg.find('.close').click();
          document.removeEventListener('paste', paste_close_dlg);
        }
        document.addEventListener('paste', paste_close_dlg);
        var cmdtrl = i18n.msg._('Ctrl-V');
        if (utils.platform === 'MacOS') {
            cmdtrl = i18n.msg._('Cmd-V');
        }
        var dialog_body = $("<div/>").append("<p>").append(i18n.msg.sprintf(i18n.msg._("Press %s again to paste"),cmdtrl))
            .append("<br/>")
            .append("<p><b>")
            .append(i18n.msg._("Why is this needed? "))
            .append("</b>")
            .append(i18n.msg._("We can't get paste events in this browser without a text box. "))
            .append(i18n.msg._("There's an invisible text box focused in this dialog."))
            .append($("<form/>").append(entry_box));

        var paste_dlg = dialog.modal({
            notebook: Jupyter.notebook,
            keyboard_manager: Jupyter.keyboard_manager,
            title : i18n.msg.sprintf(i18n.msg._("%s to paste"),cmdtrl),
            body : dialog_body,
            open: function() {
                entry_box.focus();
            },
            buttons : {
                "Cancel" : {
                    // click : function() { reject("Dialog cancelled"); },
                }
            }
        });
      }
  };
  var full_action_name = Jupyter.actions.register(action, 'paste-dialog', 'system-clipboard');
  Jupyter.keyboard_manager.command_shortcuts.add_shortcut('Cmdtrl-V', full_action_name);
}

// Set clipboard event listeners on the document.
return {setup_clipboard_events: function() {
  document.addEventListener('copy', notebookOnlyEvent(copy));
  if (needs_text_box_for_paste_event()) {
    setup_paste_dialog();
  } else {
    document.addEventListener('paste', notebookOnlyEvent(paste));
  }
}};
});
