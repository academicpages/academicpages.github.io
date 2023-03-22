// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/i18n'
], function($, utils, i18n) {
    "use strict";

    // tooltip constructor
    var Tooltip = function (events) {
        var that = this;
        this.events = events;
        this.time_before_tooltip = 1200;

        // handle to html
        this.tooltip = $('#tooltip');
        this._hidden = true;

        // variable for consecutive call
        this._old_cell = null;
        this._old_request = null;
        this._consecutive_counter = 0;

        // 'sticky ?'
        this._sticky = false;

        // display tooltip if the docstring is empty?
        this._hide_if_no_docstring = false;

        // contain the button in the upper right corner
        this.buttons = $('<div/>').addClass('tooltipbuttons');

        // will contain the docstring
        this.text = $('<div/>').addClass('tooltiptext').addClass('smalltooltip');

        // build the buttons menu on the upper right
        // expand the tooltip to see more
        var expandlink = $('<a/>').attr('href', "#").attr('role', "button").addClass('ui-button')
        .attr('id', 'expanbutton').attr('title', i18n.msg._('Grow the tooltip vertically (press shift-tab twice)')).click(function () {
            that.expand();
            event.preventDefault();
        }).append(
        $('<span/>').text('Expand').addClass('ui-icon').addClass('ui-icon-plus'));

        // open in pager
        var morelink = $('<a/>').attr('href', "#").attr('role', "button").addClass('ui-button').attr('title', i18n.msg._('show the current docstring in pager (press shift-tab 4 times)'));
        var morespan = $('<span/>').text(i18n.msg._('Open in Pager')).addClass('ui-icon').addClass('ui-icon-arrowstop-l-n');
        morelink.append(morespan);
        morelink.click(function () {
            that.showInPager(that._old_cell);
            event.preventDefault();
        });

        // close the tooltip
        var closelink = $('<a/>').attr('href', "#").attr('role', "button").addClass('ui-button');
        var closespan = $('<span/>').text(i18n.msg._('Close')).addClass('ui-icon').addClass('ui-icon-close');
        closelink.append(closespan);
        closelink.click(function () {
            that.remove_and_cancel_tooltip(true);
            event.preventDefault();
        });

        this._clocklink = $('<a/>').attr('href', "#");
        this._clocklink.attr('role', "button");
        this._clocklink.addClass('ui-button');
        this._clocklink.attr('title', i18n.msg._('Tooltip will linger for 10 seconds while you type'));
        var clockspan = $('<span/>').text(i18n.msg._('Close'));
        clockspan.addClass('ui-icon');
        clockspan.addClass('ui-icon-clock');
        this._clocklink.append(clockspan);
        this._clocklink.click(function () {
            that.cancel_stick();
            event.preventDefault();
        });




        //construct the tooltip
        // add in the reverse order you want them to appear
        this.buttons.append(closelink);
        this.buttons.append(expandlink);
        this.buttons.append(morelink);
        this.buttons.append(this._clocklink);
        this._clocklink.hide();


        // we need a phony element to make the small arrow
        // of the tooltip in css
        // we will move the arrow later
        this.arrow = $('<div/>').addClass('pretooltiparrow');
        this.tooltip.append(this.buttons);
        this.tooltip.append(this.arrow);
        this.tooltip.append(this.text);

        // function that will be called if you press tab 1, 2, 3... times in a row
        this.tabs_functions = [function (cell, text, cursor) {
            that._request_tooltip(cell, text, cursor);
        }, function () {
            that.expand();
        }, function () {
            that.stick();
        }, function (cell) {
            that.cancel_stick();
            that.showInPager(cell);
        }];
        // call after all the tabs function above have bee call to clean their effects
        // if necessary
        this.reset_tabs_function = function (cell, text) {
            this._old_cell = (cell) ? cell : null;
            this._old_request = (text) ? text : null;
            this._consecutive_counter = 0;
        };
    };

    Tooltip.prototype.is_visible = function () {
        return !this._hidden;
    };

    Tooltip.prototype.showInPager = function (cell) {
        /**
         * reexecute last call in pager by appending ? to show back in pager
         */
        this.events.trigger('open_with_text.Pager', this._reply.content);
        this.remove_and_cancel_tooltip();
    };

    // grow the tooltip vertically
    Tooltip.prototype.expand = function () {
        this.text.removeClass('smalltooltip');
        this.text.addClass('bigtooltip');
        $('#expanbutton').hide('slow');
    };

    // deal with all the logic of hiding the tooltip
    // and reset its status
    Tooltip.prototype._hide = function () {
        this._hidden = true;
        this.tooltip.fadeOut('fast');
        $('#expanbutton').show('slow');
        this.text.removeClass('bigtooltip');
        this.text.addClass('smalltooltip');
        // keep scroll top to be sure to always see the first line
        this.text.scrollTop(0);
        this.code_mirror = null;
    };

    // return true on successfully removing a visible tooltip; otherwise return
    // false.
    Tooltip.prototype.remove_and_cancel_tooltip = function (force) {
        /**
         * note that we don't handle closing directly inside the calltip
         * as in the completer, because it is not focusable, so won't
         * get the event.
         */
        this.cancel_pending();
        if (!this._hidden) {
          if (force || !this._sticky) {
              this.cancel_stick();
              this._hide();
          }
          this.reset_tabs_function();
          return true;
        } else {
          return false;
        }
    };

    // cancel autocall done after '(' for example.
    Tooltip.prototype.cancel_pending = function () {
        if (this._tooltip_timeout !== null) {
            clearTimeout(this._tooltip_timeout);
            this._tooltip_timeout = null;
        }
    };

    // will trigger tooltip after timeout
    Tooltip.prototype.pending = function (cell, hide_if_no_docstring) {
        var that = this;
        this._tooltip_timeout = setTimeout(function () {
            that.request(cell, hide_if_no_docstring);
        }, that.time_before_tooltip);
    };

    // easy access for julia monkey patching.
    Tooltip.last_token_re = /[a-z_][0-9a-z._]*$/gi;

    Tooltip.prototype._request_tooltip = function (cell, text, cursor_pos) {
        var callbacks = $.proxy(this._show, this);
        var msg_id = cell.kernel.inspect(text, cursor_pos, callbacks);
    };

    // make an immediate completion request
    Tooltip.prototype.request = function (cell, hide_if_no_docstring) {
        /**
         * request(codecell)
         * Deal with extracting the text from the cell and counting
         * call in a row
         */
        this.cancel_pending();
        var editor = cell.code_mirror;
        var cursor = editor.getCursor();
        var text = cell.get_text();
        var cursor_pos = utils.js_idx_to_char_idx(editor.indexFromPos(cursor), text);

        this._hide_if_no_docstring = hide_if_no_docstring;

        if(editor.somethingSelected()){
            // get only the most recent selection.
            text = editor.getSelection();
        }

        // need a permanent handle to code_mirror for future auto recall
        this.code_mirror = editor;

        // now we treat the different number of keypress
        // first if same cell, same text, increment counter by 1
        if (this._old_cell == cell && this._old_request == text && this._hidden === false) {
            this._consecutive_counter++;
        } else {
            // else reset
            this.cancel_stick();
            this.reset_tabs_function (cell, text);
        }

        this.tabs_functions[this._consecutive_counter](cell, text, cursor_pos);

        // then if we are at the end of list function, reset
        if (this._consecutive_counter == this.tabs_functions.length) {
            this.reset_tabs_function (cell, text, cursor);
        }

        return;
    };

    // cancel the option of having the tooltip to stick
    Tooltip.prototype.cancel_stick = function () {
        clearTimeout(this._stick_timeout);
        this._stick_timeout = null;
        this._clocklink.hide('slow');
        this._sticky = false;
    };

    // put the tooltip in a sticky state for 10 seconds
    // it won't be removed by remove_and_cancel() unless you called with
    // the first parameter set to true.
    // remove_and_cancel_tooltip(true)
    Tooltip.prototype.stick = function (time) {
        time = (time !== undefined) ? time : 10;
        var that = this;
        this._sticky = true;
        this._clocklink.show('slow');
        this._stick_timeout = setTimeout(function () {
            that._sticky = false;
            that._clocklink.hide('slow');
        }, time * 1000);
    };

    // should be called with the kernel reply to actually show the tooltip
    Tooltip.prototype._show = function (reply) {
        /**
         * move the bubble if it is not hidden
         * otherwise fade it
         */
        this._reply = reply;
        var content = reply.content;
        if (!content.found) {
            // object not found, nothing to show
            return;
        }
        this.name = content.name;

        // do some math to have the tooltip arrow on more or less on left or right
        // position of the editor
        var cm_pos = $(this.code_mirror.getWrapperElement()).position();
        var cell_pos = $(this.code_mirror.getWrapperElement().offsetParent).position();

        // anchor and head positions are local within CodeMirror element
        var anchor = this.code_mirror.cursorCoords(false, 'local');
        var head = this.code_mirror.cursorCoords(true, 'local');
        // locate the target at the center of anchor, head
        var center_left = (head.left + anchor.left) / 2;
        // locate the left edge of the tooltip, at most 450 px left of the arrow
        var edge_left = Math.max(center_left - 450, 0);
        // locate the arrow at the cursor. A 24 px offset seems necessary.
        var arrow_left = center_left - edge_left - 24;
        
        // locate left, top within container element
        var left = (cell_pos.left + cm_pos.left + edge_left) + 'px';
        var top = (cell_pos.top + cm_pos.top + head.bottom + 10) + 'px';

        if (this._hidden === false) {
            this.tooltip.animate({
                left: left,
                top: top
            });
        } else {
            this.tooltip.css({
                left: left
            });
            this.tooltip.css({
                top: top
            });
        }
        this.arrow.animate({
            'left': arrow_left + 'px'
        });
        
        this._hidden = false;
        this.tooltip.fadeIn('fast');
        this.text.children().remove();
        
        // This should support rich data types, but only text/plain for now
        // Any HTML within the docstring is escaped by the fixConsole() method.
        var pre = $('<pre/>').html(utils.fixConsole(content.data['text/plain']));
        this.text.append(pre);
        // keep scroll top to be sure to always see the first line
        this.text.scrollTop(0);
    };

    return {'Tooltip': Tooltip};
});
