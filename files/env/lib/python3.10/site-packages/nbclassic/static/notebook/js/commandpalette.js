// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'typeahead',
    'base/js/i18n',
    'notebook/js/quickhelp'
],function($, typeahead, i18n, QH){
    "use strict";

    /**
     * Humanize the action name to be consumed by user.
     * internally the actions anem are of the form
     * <namespace>:<description-with-dashes>
     * we drop <namespace> and replace dashes for space.
     */
    var humanize_action_id = function(str) {
      return str.split(':')[1].replace(/-/g, ' ').replace(/_/g, '-');
    };

    /**
     * given an action id return 'command-shortcut', 'edit-shortcut' or 'no-shortcut'
     * for the action. This allows us to tag UI in order to visually distinguish
     * wether an action have a keybinding or not.
     **/
    var get_mode_for_action_id = function(name, notebook) {
      var shortcut = notebook.keyboard_manager.command_shortcuts.get_action_shortcut(name);
      if (shortcut) {
        return 'command-shortcut';
      }
      shortcut = notebook.keyboard_manager.edit_shortcuts.get_action_shortcut(name);
      if (shortcut) {
        return 'edit-shortcut';
      }
      return 'no-shortcut';
    };

    var CommandPalette = function(notebook) {
        if(!notebook){
          throw new Error("CommandPalette takes a notebook non-null mandatory argument");
        }

        // typeahead lib need a specific layout with specific class names.
        // the following just does that
        var form = $('<form/>');
        var container = $('<div/>').addClass('typeahead__container');
        var field = $('<div/>').addClass('typeahead__field');
        var input = $('<input/>').attr('type', 'search');

        field
          .append(
            $('<span>').addClass('typeahead__query').append(
              input
            )
          )
          .append(
            $('<span/>').addClass('typeahead__button').append(
              $('<button/>').attr('type', 'submit').append(
                $('<span/>').addClass('typeahead__search-icon')
              )
            )
          );

        container.append(field);
        form.append(container);


        var mod = $('<div/>').addClass('modal cmd-palette').append(
          $('<div/>').addClass('modal-dialog')
          .append(
            $('<div/>').addClass('modal-content').append(
              $('<div/>').addClass('modal-body')
              .append(
                form
              )
            )
          )
        )
        // end setting up right layout
        .modal({show: false, backdrop:true})
        .on('shown.bs.modal', function () {
              // click on button trigger de-focus on mouse up.
              // or something like that.
              setTimeout(function(){input.focus();}, 100);
        });

        notebook.keyboard_manager.disable();

        var before_close = function() {
          // little trick to trigger early in onsubmit
          // when the action called pop-up a dialog
          // insure this function is only called once
          if (before_close.ok) {
            return;
          }
          var cell = notebook.get_selected_cell();
          if (cell) {
            cell.select();
          }
          if (notebook.keyboard_manager) {
            notebook.keyboard_manager.enable();
            notebook.keyboard_manager.command_mode();
          }
          before_close.ok = true; // avoid double call.
        };
        
        mod.on("hide.bs.modal", before_close);
        

        // will be trigger when user select action
        var onSubmit = function(node, query, result, resultCount) {
          if (actions.indexOf(result.key) >= 0) {
            before_close();
            notebook.keyboard_manager.actions.call(result.key);
          } else {
            console.warning("No command " + result.key);
          }
          mod.modal('hide');
        };

        /* Whenever a result is rendered, if there is only one resulting
         * element then automatically select that element.
         */
        var onResult = function(node, query, result, resultCount) {
            if (resultCount == 1) {
                requestAnimationFrame(function() {
                    $('.typeahead-list > li:nth-child(2)').addClass('active');
                });
            }
        };

        // generate structure needed for typeahead layout and ability to search
        var src = {};

        var actions = Object.keys(notebook.keyboard_manager.actions._actions);

        for (var i = 0; i < actions.length; i++) {
          var action_id = actions[i];
          var action = notebook.keyboard_manager.actions.get(action_id);
          var group = action_id.split(':')[0];

          src[group] = src[group] || {
            data: [],
            display: 'display'
          };

          var short = notebook.keyboard_manager.command_shortcuts.get_action_shortcut(action_id) ||
            notebook.keyboard_manager.edit_shortcuts.get_action_shortcut(action_id);
          if (short) {
            short = QH.humanize_sequence(short);
          }

          var display_text;
          if (action.cmd) {
              display_text = i18n.msg._(action.cmd);
          } else {
              display_text = humanize_action_id(action_id);
          }

          var help = null;
          if (action.help) {
              help = i18n.msg._(action.help);
          }
          
          src[group].data.push({
            display: display_text,
            shortcut: short,
            mode_shortcut: get_mode_for_action_id(action_id, notebook),
            group: group,
            icon: action.icon,
            help: help,
            key: action_id,
          });
        }

        // now src is the right structure for typeahead

        input.typeahead({
          emptyTemplate: function(query) {
            return $('<div>').text("No results found for ").append(
                $('<code>').text(query)
            );
          },
          maxItem: 1e3,
          minLength: 0,
          hint: true,
          group: {
            template:"{{group}} command group"
          },
          searchOnFocus: true,
          mustSelectItem: true,
          template: '<i class="fa fa-icon {{icon}}"></i>{{display}}  <div title={{key}} class="pull-right {{mode_shortcut}}">{{shortcut}}</div>',
          order: "asc",
          source: src,
          callback: {
            onSubmit: onSubmit,
            onClickAfter: onSubmit,
            onResult: onResult
          },
          debug: false,
        });

        mod.modal('show');
    };
    return {'CommandPalette': CommandPalette};
});
