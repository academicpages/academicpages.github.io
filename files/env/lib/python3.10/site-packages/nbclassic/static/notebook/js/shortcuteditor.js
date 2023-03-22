// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    "jquery",
    "notebook/js/quickhelp",
    "base/js/dialog",
    "components/marked/lib/marked"
], function (
    $,
    QH,
    dialog,
    marked
) {


/**
 * Humanize the action name to be consumed by user.
 * internally the actions name are of the form
 * <namespace>:<description-with-dashes>
 * we drop <namespace> and replace dashes for space.
 */
var humanize_action_id = function(str) {
  return str.split(':')[1].replace(/-/g, ' ').replace(/_/g, '-');
};

/**
 * given an action id return 'command-shortcut', 'edit-shortcut' or 'no-shortcut'
 * for the action. This allows us to tag UI in order to visually distinguish
 * Wether an action have a keybinding or not.
 **/

var KeyBinding = createReactClass({
  displayName: 'KeyBindings',
  getInitialState: function() {
    return {shrt:''};
  },
  handleShrtChange: function (element){
    this.setState({shrt:element.target.value});
  },
  render: function(){
    var that = this;
    var available = this.props.available(this.state.shrt);
    var empty = (this.state.shrt === '');
    var binding_setter = function(){
      if (available) { 
        that.props.onAddBindings(that.state.shrt, that.props.ckey);
      }
      that.state.shrt='';
      event.preventDefault();
      return false;
    };
    return React.createElement('form', {className:'jupyter-keybindings',
            onSubmit: binding_setter
        },
              React.createElement('i', {className: "pull-right fa fa-plus", alt: 'add-keyboard-shortcut',
                  onClick: binding_setter
              }),
              React.createElement('input', {
                                      type:'text', 
                               placeholder:'add shortcut', 
                                 className:'pull-right'+((available||empty)?'':' alert alert-danger'),
                                     value:that.state.shrt,
                                  onChange:that.handleShrtChange
              }),
              that.props.shortcuts ? that.props.shortcuts.map(function (item, index) {
                return React.createElement('span', {className: 'pull-right'},
                  React.createElement('kbd', {}, [
                    item.h,
                    React.createElement('i', {className: "fa fa-times", alt: 'remove '+item.h,
                      onClick:function () {
                        that.props.unbind(item.raw);
                      }
                    })
                  ])
                );
              }): null,
              React.createElement('div', {title: '(' + that.props.ckey + ')' ,
                className:'jupyter-keybindings-text'}, that.props.display )
      );
  }
});

var KeyBindingList = createReactClass({
  displayName: 'KeyBindingList',
  getInitialState: function(){
    return {data:[]};
  },
  componentDidMount: function(){
      this.setState({data:this.props.callback()});
  },
  render: function() {
      var that = this;
      var children = this.state.data.map(function (binding) {
          return React.createElement(KeyBinding, Object.assign({}, binding, {
          onAddBindings: function (shortcut, action) {
              that.props.bind(shortcut, action);
              that.setState({data:that.props.callback()});
          },
          available: that.props.available,
          unbind: function (shortcut) {
                  that.props.unbind(shortcut);
                  that.setState({data:that.props.callback()});
             }
          }));
      });
      children.unshift(React.createElement('div', {className:'well', key:'disclamer', id:'short-key-binding-intro', dangerouslySetInnerHTML:
            {__html: 
            marked(

            "Here you can modify the keyboard shortcuts available in "+
            "command mode. Your changes will be stored for later sessions. "+
            "See more [**details of defining keyboard shortcuts**](#long-key-binding-intro) below."
            )}
      }));
      children.push(React.createElement('div', {className:'well', key:'disclamer', id:'long-key-binding-intro', dangerouslySetInnerHTML:
            {__html: 
            marked(

            "This dialog allows you to modify the keyboard shortcuts available in command mode. "+ 
            "Any changes will be persisted between sessions and across environments. "+
            "You can define two kinds of shortcuts: **key combinations** and **key sequences**.\n"+
            "\n"+
            " - **Key Combinations**:\n"+
            "   - Use hyphens `-` to represent keys that should be pressed at the same time.\n"+
            "   - This is designed for use with *modifier* keys: `Cmd`, `Ctrl`, `Alt` ,`Meta`, "+
            "`Cmdtrl`, and `Shift`.\n"+ 
            "       - `Cmdtrl` acts like `Cmd` on OS X/MacOS and `Ctrl` on Windows/Linux.\n"+
            "   - At most, one non-modifier key can exist in a key combination.\n"+
            "   - Multiple modifier keys can exist in a key combination.\n"+
            "   - Modifier keys need to precede the non-modifier key in a combination.\n"+
            "   - *Valid Examples*: `Shift-a`, `Ctrl-;`, or `Ctrl-Shift-a`. \n"+
            "   - *Invalid Example*s: `a-b` and `a-Ctrl-Shift`. \n"+
            " - **Key Sequences**:\n"+
            "   - Use commas `,` to represent keys that should be pressed in sequence.\n"+
            "   - The order in which keys must be pressed exactly matches the left-to-right order of "+
            "the characters in the sequence, with no interruptions.\n"+
            "     - E.g., `h,a,l,t` would be triggered by typing <kbd>h</kbd> <kbd>a</kbd> "+
            "<kbd>l</kbd> <kbd>t</kbd> but not <kbd>h</kbd> <kbd>a</kbd> <kbd>a</kbd> <kbd>l</kbd> "+
            "<kbd>t</kbd> or <kbd>a</kbd>  <kbd>h</kbd> <kbd>l</kbd> <kbd>t</kbd>.\n"+
            "   - Sequences can include the same key multiple times (e.g., `d,d`).\n"+
            "   - You cannot include any pairs of sequences where one is a 'prefix' the other.\n"+
            "     - E.g., `d,d,d` cannot be used a the same time as `d,d`.\n"+ 
            "   - Key combinations are unique elements that can be used in a sequence.\n"+ 
            "     - E.g., `Ctrl-d,d` and `d,d` can exist at the same time and are both valid key sequences.\n"+
            "\n"+
            "**Additional notes**:\n"+
            "\n"+
            "The case in which elements are written does not change the binding's meaning. "+
            "E.g., `Ctrl-D` and `cTrl-d` are the same key binding. "+
            "Thus, `Shift` needs to be explicitly included if it is part of the key binding. "+
            "So, for example, if you set a command to be activated by `Shift-D,D`, the second `d` "+
            "cannot be pressed at the same time as the `Shift` modifier key.\n"+
            "\n"+
            "Valid modifiers are specified by writing out their names explicitly: "+
            "e.g., `Shift`, `Cmd`, `Ctrl`, `Alt` ,`Meta`, `Cmdtrl`. You cannot use the symbol equivalents "+
            "(e.g., `⇧`, `⌘`, `⌃`, `⌥`); refer to developer docs for the corresponding keys "+
            "(the mapping of which depends on the platform you are using)."+
            "You can hover on the name/description of a command to see its exact internal name and "+
            "differentiate from actions defined in various plugins. \n"+
            "\n"+
            "Changing the keybindings of edit mode is not currently available."
            )}
      }));
      return React.createElement('div',{}, children);
    }
});

var get_shortcuts_data = function(notebook) {
    var actions = Object.keys(notebook.keyboard_manager.actions._actions);
    var src = [];

    for (var i = 0; i < actions.length; i++) {
      var action_id = actions[i];
      var action = notebook.keyboard_manager.actions.get(action_id);

      var shortcuts = notebook.keyboard_manager.command_shortcuts.get_action_shortcuts(action_id);
      var hshortcuts = [];
      if (shortcuts.length > 0) {
        hshortcuts = shortcuts.map(function (raw) {
          return {h:QH._humanize_sequence(raw),raw:raw};}
        );
      }
      src.push({
        display: humanize_action_id(action_id),
        shortcuts: hshortcuts,
        key:action_id, // react specific thing
        ckey: action_id
      });
    }
    return src;
};


var ShortcutEditor = function(notebook) {

    if(!notebook){
      throw new Error("CommandPalette takes a notebook non-null mandatory argument");
    }

    var body =  $('<div>');
    var mod = dialog.modal({
        notebook: notebook,
        keyboard_manager: notebook.keyboard_manager,
        title : "Edit Command mode Shortcuts",
        body : body,
        buttons : {
            OK : {}
        }
    });
    
    var src = get_shortcuts_data(notebook);

    mod.addClass("modal_stretch");

    mod.modal('show');
    ReactDOM.render(
        React.createElement(KeyBindingList, {
            callback: function () { return  get_shortcuts_data(notebook);},
            bind: function (shortcut, command) {
                return notebook.keyboard_manager.command_shortcuts._persist_shortcut(shortcut, command);
            },
            unbind: function (shortcut) {
                return notebook.keyboard_manager.command_shortcuts._persist_remove_shortcut(shortcut);
            },
            available: function (shrt) { return notebook.keyboard_manager.command_shortcuts.is_available_shortcut(shrt);}
          }),
        body.get(0)
    );
};
    return {ShortcutEditor: ShortcutEditor};
});
