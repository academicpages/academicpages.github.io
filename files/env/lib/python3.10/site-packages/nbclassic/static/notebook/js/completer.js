// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/keyboard',
    'notebook/js/contexthint',
    'codemirror/lib/codemirror',
], function($, utils, keyboard, CodeMirror) {
    "use strict";

    // easier key mapping
    var keycodes = keyboard.keycodes;

    var prepend_n_prc = function(str, n) {
        for( var i =0 ; i< n ; i++){
            str = '%'+str ;
        }
        return str;
    };

    var _existing_completion = function(item, completion_array){
        for( var i=0; i < completion_array.length; i++) {
            if (completion_array[i].trim().substr(-item.length) == item) {
                return true;
            }
        }
        return false;
    };

    // what is the common start of all completions
    function shared_start(B, drop_prct) {
        if (B.length == 1) {
            return B[0];
        }
        var A = [];
        var common;
        var min_lead_prct = 10;
        for (var i = 0; i < B.length; i++) {
            var str = B[i].str;
            var localmin = 0;
            if(drop_prct === true){
                while ( str.substr(0, 1) == '%') {
                    localmin = localmin+1;
                    str = str.substring(1);
                }
            }
            min_lead_prct = Math.min(min_lead_prct, localmin);
            A.push(str);
        }

        if (A.length > 1) {
            var tem1, tem2, s;
            A = A.slice(0).sort();
            tem1 = A[0];
            s = tem1.length;
            tem2 = A.pop();
            while (s && tem2.indexOf(tem1) == -1) {
                tem1 = tem1.substring(0, --s);
            }
            if (tem1 === "" || tem2.indexOf(tem1) !== 0) {
                return {
                    str:prepend_n_prc('', min_lead_prct),
                    type: "computed",
                    from: B[0].from,
                    to: B[0].to
                    };
            }
            return {
                str: prepend_n_prc(tem1, min_lead_prct),
                type: "computed",
                from: B[0].from,
                to: B[0].to
            };
        }
        return null;
    }


    var Completer = function (cell, events) {
        this.cell = cell;
        this.editor = cell.code_mirror;
        var that = this;
        events.on('kernel_busy.Kernel', function () {
            that.skip_kernel_completion = true;
        });
        events.on('kernel_idle.Kernel', function () {
            that.skip_kernel_completion = false;
        });
    };

    Completer.prototype.startCompletion = function () {
        /**
         * call for a 'first' completion, that will set the editor and do some
         * special behavior like autopicking if only one completion available.
         */
        if (this.editor.somethingSelected()|| this.editor.getSelections().length > 1) return;
        this.done = false;
        // use to get focus back on opera
        this.carry_on_completion(true);
    };


    // easy access for julia to monkeypatch
    //
    Completer.reinvoke_re = /[%0-9a-z._/\\:~-]/i;

    Completer.prototype.reinvoke= function(pre_cursor, block, cursor){
        return Completer.reinvoke_re.test(pre_cursor);
    };

    /**
     *
     * pass true as parameter if this is the first invocation of the completer
     * this will prevent the completer to dismiss itself if it is not on a
     * word boundary like pressing tab after a space, and make it autopick the
     * only choice if there is only one which prevent from popping the UI.  as
     * well as fast-forwarding the typing if all completion have a common
     * shared start
     **/
    Completer.prototype.carry_on_completion = function (first_invocation) {
        /**
         * Pass true as parameter if you want the completer to autopick when
         * only one completion. This function is automatically reinvoked at
         * each keystroke with first_invocation = false
         */
        var cur = this.editor.getCursor();
        var line = this.editor.getLine(cur.line);
        var pre_cursor = this.editor.getRange({
            line: cur.line,
            ch: cur.ch - 1
        }, cur);

        // we need to check that we are still on a word boundary
        // because while typing the completer is still reinvoking itself
        // so dismiss if we are on a "bad" character
        if (!this.reinvoke(pre_cursor) && !first_invocation) {
            this.close();
            return;
        }

        this.autopick = false;
        if (first_invocation) {
            this.autopick = true;
        }

        // We want a single cursor position.
        if (this.editor.somethingSelected()|| this.editor.getSelections().length > 1) {
            return;
        }

        // one kernel completion came back, finish_completing will be called with the results
        // we fork here and directly call finish completing if kernel is busy
        var cursor_pos = this.editor.indexFromPos(cur);
        var text = this.editor.getValue();
        cursor_pos = utils.js_idx_to_char_idx(cursor_pos, text);
        if (this.skip_kernel_completion) {
            this.finish_completing({ content: {
                matches: [],
                cursor_start: cursor_pos,
                cursor_end: cursor_pos,
            }});
        } else {
            this.cell.kernel.complete(text, cursor_pos,
                $.proxy(this.finish_completing, this)
            );
        }
    };

    Completer.prototype.finish_completing = function (msg) {
        /**
         * let's build a function that wrap all that stuff into what is needed
         * for the new completer:
         */
        var content = msg.content;
        var start = content.cursor_start;
        var end = content.cursor_end;
        var matches = content.matches;
        console.log(content);

        var cur = this.editor.getCursor();
        if (end === null) {
            // adapted message spec replies don't have cursor position info,
            // interpret end=null as current position,
            // and negative start relative to that
            end = this.editor.indexFromPos(cur);
            if (start === null) {
                start = end;
            } else if (start < 0) {
                start = end + start;
            }
        } else {
            // handle surrogate pairs
            var text = this.editor.getValue();
            end = utils.char_idx_to_js_idx(end, text);
            start = utils.char_idx_to_js_idx(start, text);
        }

        var results = CodeMirror.contextHint(this.editor);
        var filtered_results = [];
        //remove results from context completion
        //that are already in kernel completion
        var i;
        for (i=0; i < results.length; i++) {
            if (!_existing_completion(results[i].str, matches)) {
                filtered_results.push(results[i]);
            }
        }

        // append the introspection result, in order, at at the beginning of
        // the table and compute the replacement range from current cursor
        // position and matched_text length.
        var from = this.editor.posFromIndex(start);
        var to = this.editor.posFromIndex(end);
        for (i = matches.length - 1; i >= 0; --i) {
            filtered_results.unshift({
                str: matches[i],
                type: "introspection",
                from: from,
                to: to
            });
        }

        // one the 2 sources results have been merge, deal with it
        this.raw_result = filtered_results;

        // if empty result return
        if (!this.raw_result || !this.raw_result.length) return;

        // When there is only one completion, use it directly.
        if (this.autopick && this.raw_result.length == 1) {
            this.insert(this.raw_result[0]);
            return;
        }

        if (this.raw_result.length == 1) {
            // test if first and only completion totally matches
            // what is typed, in this case dismiss
            var str = this.raw_result[0].str;
            var pre_cursor = this.editor.getRange({
                line: cur.line,
                ch: cur.ch - str.length
            }, cur);
            if (pre_cursor == str) {
                this.close();
                return;
            }
        }

        if (!this.visible) {
            this.complete = $('<div/>').addClass('completions');
            this.complete.attr('id', 'complete');

            // Currently webkit doesn't use the size attr correctly. See:
            // https://code.google.com/p/chromium/issues/detail?id=4579
            this.sel = $('<select/>')
                .attr('tabindex', -1)
                .attr('multiple', 'true');
            this.complete.append(this.sel);
            this.visible = true;
            $('body').append(this.complete);

            //build the container
            var that = this;
            this.sel.click(function () {
                that.pick();
                that.editor.focus();
            });
            this._handle_keydown = function (cm, event) {
                that.keydown(event);
            };
            this.editor.on('keydown', this._handle_keydown);
            this._handle_keypress = function (cm, event) {
                that.keypress(event);
            };
            this.editor.on('keypress', this._handle_keypress);
        }
        this.sel.attr('size', Math.min(10, this.raw_result.length));

        // After everything is on the page, compute the position.
        // We put it above the code if it is too close to the bottom of the page.
        var pos = this.editor.cursorCoords(
            this.editor.posFromIndex(start)
        );
        var left = pos.left-3;
        var top;
        var cheight = this.complete.height();
        var wheight = $(window).height();
        if (pos.bottom+cheight+5 > wheight) {
            top = pos.top-cheight-4;
        } else {
            top = pos.bottom+1;
        }
        this.complete.css('left', left + 'px');
        this.complete.css('top', top + 'px');

        // Clear and fill the list.
        this.sel.text('');
        this.build_gui_list(this.raw_result);
        return true;
    };

    Completer.prototype.insert = function (completion) {
        this.editor.replaceRange(completion.str, completion.from, completion.to);
    };

    Completer.prototype.build_gui_list = function (completions) {
        var MAXIMUM_GUI_LIST_LENGTH = 1000;
        for (var i = 0; i < completions.length && i < MAXIMUM_GUI_LIST_LENGTH; ++i) {
            var opt = $('<option/>').text(completions[i].str).addClass(completions[i].type);
            this.sel.append(opt);
        }
        this.sel.children().first().attr('selected', 'true');
        this.sel.scrollTop(0);
    };

    Completer.prototype.close = function () {
        this.done = true;
        $('#complete').remove();
        this.editor.off('keydown', this._handle_keydown);
        this.editor.off('keypress', this._handle_keypress);
        this.visible = false;
    };

    Completer.prototype.pick = function () {
        this.insert(this.raw_result[this.sel[0].selectedIndex]);
        this.close();
    };

    Completer.prototype.keydown = function (event) {
        var code = event.keyCode;

        // Enter
        var options;
        var index;
        if (code == keycodes.enter) {
            event.codemirrorIgnore = true;
            event._ipkmIgnore = true;
            event.preventDefault();
            this.pick();
        // Escape or backspace
        } else if (code == keycodes.esc || code == keycodes.backspace) {
            event.codemirrorIgnore = true;
            event._ipkmIgnore = true;
            event.preventDefault();
            this.close();
        } else if (code == keycodes.tab) {
            //all the fastforwarding operation,
            //Check that shared start is not null which can append with prefixed completion
            // like %pylab , pylab have no shared start, and ff will result in py<tab><tab>
            // to erase py
            var sh = shared_start(this.raw_result, true);
            if (sh.str !== '') {
                this.insert(sh);
            }
            this.close();
            this.carry_on_completion();
        } else if (code == keycodes.up || code == keycodes.down) {
            // need to do that to be able to move the arrow
            // when on the first or last line of a code cell
            event.codemirrorIgnore = true;
            event._ipkmIgnore = true;
            event.preventDefault();

            options = this.sel.find('option');
            index = this.sel[0].selectedIndex;
            if (code == keycodes.up) {
                index--;
            }
            if (code == keycodes.down) {
                index++;
            }
            index = Math.min(Math.max(index, 0), options.length-1);
            this.sel[0].selectedIndex = index;
        } else if (code == keycodes.pageup || code == keycodes.pagedown) {
            event.codemirrorIgnore = true;
            event._ipkmIgnore = true;

            options = this.sel.find('option');
            index = this.sel[0].selectedIndex;
            if (code == keycodes.pageup) {
                index -= 10; // As 10 is the hard coded size of the drop down menu
            } else {
                index += 10;
            }
            index = Math.min(Math.max(index, 0), options.length-1);
            this.sel[0].selectedIndex = index;
        } else if (code == keycodes.left || code == keycodes.right) {
            this.close();
        }
    };

    Completer.prototype.keypress = function (event) {
        /**
         * FIXME: This is a band-aid.
         * on keypress, trigger insertion of a single character.
         * This simulates the old behavior of completion as you type,
         * before events were disconnected and CodeMirror stopped
         * receiving events while the completer is focused.
         */
        
        var that = this;
        var code = event.keyCode;
        
        // don't handle keypress if it's not a character (arrows on FF)
        // or ENTER/TAB
        if (event.charCode === 0 ||
            code == keycodes.tab ||
            code == keycodes.enter
        ) return;
        
        this.close();
        this.editor.focus();
        setTimeout(function () {
            that.carry_on_completion();
        }, 50);
    };

    return {'Completer': Completer};
});
