// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'base/js/i18n',
    'base/js/security',
    'base/js/keyboard',
    'base/js/markdown',
    'services/config',
], function($, utils, i18n, security, keyboard, markdown, configmod) {
    "use strict";

    /**
     * @class OutputArea
     *
     * @constructor
     */

    var OutputArea = function (options) {
        this.config = options.config;
        this.selector = options.selector;
        this.events = options.events;
        this.keyboard_manager = options.keyboard_manager;
        this.wrapper = $(options.selector);
        this.outputs = [];
        this.collapsed = false;
        this.scrolled = false;
        this.scroll_state = 'auto';
        this.trusted = true;
        this.clear_queued = null;
        if (options.prompt_area === undefined) {
            this.prompt_area = true;
        } else {
            this.prompt_area = options.prompt_area;
        }
        this._display_id_targets = {};
        this.create_elements();
        this.style();
        this.bind_events();
        this.class_config = new configmod.ConfigWithDefaults(this.config,
                                        OutputArea.config_defaults, 'OutputArea');

        this.handle_appended = utils.throttle(this.handle_appended.bind(this));
    };

    OutputArea.config_defaults = {
        stream_chunk_size: 8192, // chunk size for stream output
    };

    /**
     * Class prototypes
     **/

    OutputArea.prototype.create_elements = function () {
        var element = this.element = $("<div/>");
        // wrap element in safe trigger,
        // so that errors (e.g. in widget extensions) are logged instead of
        // breaking everything.
        this.element._original_trigger = this.element.trigger;
        this.element.trigger = function (name, data) {
            try {
                this._original_trigger.apply(this, arguments);
            } catch (e) {
                console.error("Exception in event handler for " + name, e, arguments);
            }
        }
        this.collapse_button = $("<div/>");
        this.prompt_overlay = $("<div/>");
        this.wrapper.append(this.prompt_overlay);
        this.wrapper.append(this.element);
        this.wrapper.append(this.collapse_button);
    };


    OutputArea.prototype.style = function () {
        this.collapse_button.hide();
        if (!this.prompt_area) {
            this.prompt_overlay.hide();
        }

        this.wrapper.addClass('output_wrapper');
        this.element.addClass('output');

        this.collapse_button.addClass("btn btn-default output_collapsed");
        this.collapse_button.attr('title', i18n.msg._('click to expand output'));
        this.collapse_button.text('. . .');

        this.prompt_overlay.addClass('out_prompt_overlay prompt');
        this.prompt_overlay.attr('title', i18n.msg._('click to expand output; double click to hide output'));

        this.expand();
    };

    /**
     * Should the OutputArea scroll?
     * Returns whether the height (in lines) exceeds the current threshold.
     * Threshold will be OutputArea.minimum_scroll_threshold if scroll_state=true (manually requested)
     * or OutputArea.auto_scroll_threshold if scroll_state='auto'.
     * This will always return false if scroll_state=false (scroll disabled).
     *
     */
    OutputArea.prototype._should_scroll = function () {
        var threshold;
        if (this.scroll_state === false) {
            return false;
        } else if (this.scroll_state === true) {
            threshold = OutputArea.minimum_scroll_threshold;
        } else {
            threshold = OutputArea.auto_scroll_threshold;
        }
        if (threshold <=0) {
            return false;
        }
        // line-height from https://stackoverflow.com/questions/1185151
        var fontSize = this.element.css('font-size') || '14px';
        var lineHeight = Math.floor((parseFloat(fontSize.replace('px','')) || 14) * 1.3);
        return (this.element.height() > threshold * lineHeight);
    };


    OutputArea.prototype.bind_events = function () {
        var that = this;
        this.prompt_overlay.dblclick(function () { that.toggle_output(); });
        this.prompt_overlay.click(function () { that.toggle_scroll(); });

        this.element.on('resizeOutput', function () {
            // maybe scroll output,
            // if it's grown large enough and hasn't already been scrolled.
            if (!that.scrolled && that._should_scroll()) {
                that.scroll_area();
            }
        });
        this.collapse_button.click(function () {
            that.expand();
        });
    };


    OutputArea.prototype.collapse = function () {
        if (!this.collapsed) {
            this.element.hide();
            this.prompt_overlay.hide();
            if (this.element.html()){
                this.collapse_button.show();
            }
            this.collapsed = true;
            // collapsing output clears scroll state
            this.scroll_state = 'auto';
        }
    };


    OutputArea.prototype.expand = function () {
        if (this.collapsed) {
            this.collapse_button.hide();
            this.element.show();
            if (this.prompt_area) {
                this.prompt_overlay.show();
            }
            this.collapsed = false;
            this.scroll_if_long();
        }
    };


    OutputArea.prototype.toggle_output = function () {
        if (this.collapsed) {
            this.expand();
        } else {
            this.collapse();
        }
    };


    OutputArea.prototype.scroll_area = function () {
        this.element.addClass('output_scroll');
        this.prompt_overlay.attr('title', i18n.msg._('click to unscroll output; double click to hide'));
        this.scrolled = true;
    };


    OutputArea.prototype.unscroll_area = function () {
        this.element.removeClass('output_scroll');
        this.prompt_overlay.attr('title', i18n.msg._('click to scroll output; double click to hide'));
        this.scrolled = false;
    };

    /**
     * Scroll OutputArea if height exceeds a threshold.
     *
     * Threshold is OutputArea.minimum_scroll_threshold if scroll_state = true,
     * OutputArea.auto_scroll_threshold if scroll_state='auto'.
     *
     **/
    OutputArea.prototype.scroll_if_long = function () {
        var should_scroll = this._should_scroll();
        if (!this.scrolled && should_scroll) {
            // only allow scrolling long-enough output
            this.scroll_area();
        } else if (this.scrolled && !should_scroll) {
            // scrolled and shouldn't be
            this.unscroll_area();
        }
    };


    OutputArea.prototype.toggle_scroll = function () {
        if (this.scroll_state == 'auto') {
            this.scroll_state = !this.scrolled;
        } else {
            this.scroll_state = !this.scroll_state;
        }
        if (this.scrolled) {
            this.unscroll_area();
        } else {
            // only allow scrolling long-enough output
            this.scroll_if_long();
        }
    };


    // typeset with MathJax if MathJax is available
    OutputArea.prototype.typeset = function () {
        utils.typeset(this.element);
    };


    OutputArea.prototype.handle_output = function (msg) {
        var json = {};
        var msg_type = json.output_type = msg.header.msg_type;
        var content = msg.content;
        switch(msg_type) {
        case "stream" :
            json.text = content.text;
            json.name = content.name;
            break;
        case "execute_result":
            json.execution_count = content.execution_count;
        case "update_display_data":
        case "display_data":
            json.transient = content.transient;
            json.data = content.data;
            json.metadata = content.metadata;
            break;
        case "error":
            json.ename = content.ename;
            json.evalue = content.evalue;
            json.traceback = content.traceback;
            break;
        default:
            console.error("unhandled output message", msg);
            return;
        }
        this.append_output(json);
    };

    // Declare mime type as constants
    var MIME_JAVASCRIPT = 'application/javascript';
    var MIME_HTML = 'text/html';
    var MIME_MARKDOWN = 'text/markdown';
    var MIME_LATEX = 'text/latex';
    var MIME_SVG = 'image/svg+xml';
    var MIME_PNG = 'image/png';
    var MIME_JPEG = 'image/jpeg';
    var MIME_GIF = 'image/gif';
    var MIME_PDF = 'application/pdf';
    var MIME_TEXT = 'text/plain';


    OutputArea.output_types = [
        MIME_JAVASCRIPT,
        MIME_HTML,
        MIME_MARKDOWN,
        MIME_LATEX,
        MIME_SVG,
        MIME_PNG,
        MIME_JPEG,
        MIME_GIF,
        MIME_PDF,
        MIME_TEXT,
    ];

    OutputArea.prototype.validate_mimebundle = function (bundle) {
        /** scrub invalid outputs */
        if (typeof bundle.data !== 'object') {
            console.warn("mimebundle missing data", bundle);
            bundle.data = {};
        }
        if (typeof bundle.metadata !== 'object') {
            console.warn("mimebundle missing metadata", bundle);
            bundle.metadata = {};
        }
        var data = bundle.data;
        $.map(OutputArea.output_types, function(key){
            if ((key.indexOf('application/') === -1 || key.indexOf('json') === -1) &&
                data[key] !== undefined &&
                typeof data[key] !== 'string'
            ) {
                console.log("Invalid type for " + key, data[key]);
                delete data[key];
            }
        });
        return bundle;
    };

    OutputArea.prototype.append_output = function (json) {
        this.expand();

        if (this.clear_queued) {
            this.clear_output(false);
            this._needs_height_reset = true;
        }

        var record_output = true;
        switch(json.output_type) {
            case 'update_display_data':
                record_output = false;
                json = this.validate_mimebundle(json);
                this.update_display_data(json);
                return;
            case 'execute_result':
                json = this.validate_mimebundle(json);
                this.append_execute_result(json);
                break;
            case 'stream':
                // append_stream might have merged the output with earlier stream output
                record_output = this.append_stream(json);
                break;
            case 'error':
                this.append_error(json);
                break;
            case 'display_data':
                // append handled below
                json = this.validate_mimebundle(json);
                break;
            default:
                console.log("unrecognized output type: " + json.output_type);
                this.append_unrecognized(json);
        }

        if (json.output_type === 'display_data') {
            var that = this;
            this.append_display_data(json, this.handle_appended);
        } else {
            this.handle_appended();
        }

        if (record_output) {
            this.outputs.push(json);
        }

        this.events.trigger('output_added.OutputArea', {
            output: json,
            output_area: this,
        });
    };

    OutputArea.prototype.handle_appended = function () {
        if (this._needs_height_reset) {
            this.element.height('');
            this._needs_height_reset = false;
        }

        this.element.trigger('resizeOutput', {output_area: this});
    };

    OutputArea.prototype.create_output_area = function () {
        var oa = $("<div/>").addClass("output_area");
        if (this.prompt_area) {
            oa.append($('<div/>').addClass('run_this_cell'));
            oa.append($('<div/>').addClass('prompt'));
        }
        return oa;
    };


    function _get_metadata_key(metadata, key, mime) {
        var mime_md = metadata[mime];
        // mime-specific higher priority
        if (mime_md && mime_md[key] !== undefined) {
            return mime_md[key];
        }
        // fallback on global
        return metadata[key];
    }

    OutputArea.prototype.create_output_subarea = function(md, classes, mime) {
        var subarea = $('<div/>').addClass('output_subarea').addClass(classes);
        // Unforce RTL
        subarea.attr("dir","auto");
        if (_get_metadata_key(md, 'isolated', mime)) {
            // Create an iframe to isolate the subarea from the rest of the
            // document
            var iframe = $('<iframe/>').addClass('box-flex1');
            iframe.css({'height':1, 'width':'100%', 'display':'block'});
            iframe.attr('frameborder', 0);
            iframe.attr('scrolling', 'auto');

            // Once the iframe is loaded, the subarea is dynamically inserted
            iframe.on('load', function() {
                // Workaround needed by Firefox, to properly render svg inside
                // iframes, see https://stackoverflow.com/questions/10177190/
                // svg-dynamically-added-to-iframe-does-not-render-correctly
                this.contentDocument.open();

                // Insert the subarea into the iframe
                // We must directly write the html. When using Jquery's append
                // method, javascript is evaluated in the parent document and
                // not in the iframe document.  At this point, subarea doesn't
                // contain any user content.
                this.contentDocument.write(subarea.html());

                this.contentDocument.close();

                var body = this.contentDocument.body;
                // Adjust the iframe height automatically
                iframe.height(body.scrollHeight + 'px');
            });

            // Elements should be appended to the inner subarea and not to the
            // iframe
            iframe.append = function(that) {
                subarea.append(that);
            };

            return iframe;
        } else {
            return subarea;
        }
    };


    OutputArea.prototype._append_javascript_error = function (err, element) {
        /**
         * display a message when a javascript error occurs in display output
         */
        var msg = i18n.msg._("Javascript error adding output!");
        if ( element === undefined ) return;
        element
            .append($('<div/>').text(msg).addClass('js-error'))
            .append($('<div/>').text(err.toString()).addClass('js-error'))
            .append($('<div/>').text(i18n.msg._('See your browser Javascript console for more details.')).addClass('js-error'));
    };

    OutputArea.prototype._safe_append = function (toinsert, toreplace) {
        /**
         * safely append an item to the document
         * this is an object created by user code,
         * and may have errors, which should not be raised
         * under any circumstances.
         */
        try {
            if (toreplace) {
                toreplace.replaceWith(toinsert);
            } else {
                this.element.append(toinsert);
            }
        } catch(err) {
            console.error(err);
            // Create an actual output_area and output_subarea, which creates
            // the prompt area and the proper indentation.
            toinsert = this.create_output_area();
            var subarea = $('<div/>').addClass('output_subarea');
            // Unforce RTL
            subarea.attr("dir","auto");
            toinsert.append(subarea);
            this._append_javascript_error(err, subarea);
            this.element.append(toinsert);
        }

        // Notify others of changes.
        this.element.trigger('changed', {output_area: this});
    };

    OutputArea.output_prompt_classical = function(prompt_value) {
        return $('<bdi>').text(i18n.msg.sprintf(i18n.msg._('Out[%s]:'),prompt_value));
    };

    OutputArea.output_prompt_function = OutputArea.output_prompt_classical;

    OutputArea.prototype.append_execute_result = function (json) {
        var n = json.execution_count || ' ';
        var toinsert = this.create_output_area();
        this._record_display_id(json, toinsert);
        if (this.prompt_area) {
            toinsert.find('div.prompt')
                    .addClass('output_prompt')
                    .empty()
                    .append(OutputArea.output_prompt_function(n));
        }
        var inserted = this.append_mime_type(json, toinsert);
        if (inserted) {
            inserted.addClass('output_result');
        }
        this._safe_append(toinsert);
        // If we just output latex, typeset it.
        if ((json.data[MIME_LATEX] !== undefined) ||
            (json.data[MIME_HTML] !== undefined) ||
            (json.data[MIME_MARKDOWN] !== undefined)) {
            this.typeset();
        }
    };


    OutputArea.prototype.append_error = function (json) {
        var ename = json.ename;
        var evalue = json.evalue;
        var tb = json.traceback;
        var s = '';
        if (tb !== undefined && tb.length > 0) {
            var len = tb.length;
            for (var i=0; i<len; i++) {
                s = s + tb[i] + '\n';
            }
            s = s + '\n';
        } else if (ename !== undefined && ename.length > 0 && evalue !== undefined && evalue.length > 0) {
            // If traceback is empty, and we have ename and evalue entries, concatenate the two to display
            s = ename + ': ' + evalue;
        }
        if (s.length > 0) {
            var toinsert = this.create_output_area();
            var append_text = OutputArea.append_map[MIME_TEXT];
            if (append_text) {
                append_text.apply(this, [s, {}, toinsert]).addClass('output_error');
            }
            this._safe_append(toinsert);
        }
    };


    OutputArea.prototype.append_stream = function (json) {
        var text = json.text;
        if (typeof text !== 'string') {
            console.error("Stream output is invalid (missing text)", json);
            return false;
        }
        var subclass = "output_"+json.name;

        if (this.outputs.length > 0){
            // have at least one output to consider
            var last = this.outputs[this.outputs.length-1];
            if (last.output_type == 'stream' && json.name == last.name){
                if (last.text.length > this.class_config.get_sync('stream_chunk_size')) {
                    // don't keep extending long blocks
                    var last_newline_idx = last.text.lastIndexOf('\n');
                    // if the last stream output doesn't end on a newline,
                    // split on last newline and take the tail with the new output
                    if (last_newline_idx !== -1 && last_newline_idx !== last.text.length - 1) {
                        // truncate last.text to its last newline,
                        // and take the tail with the new output.
                        var tail = last.text.slice(last_newline_idx + 1);
                        last.text = last.text.slice(0, last_newline_idx + 1);
                        // we changed last's content, so we have to re-render it
                        text = json.text = tail + json.text;
                        var pre = this.element.find('div.'+subclass).last().find('pre');
                        var html = utils.fixConsole(last.text);
                        html = utils.autoLinkUrls(html);
                        pre.html(html);
                    }
                } else {
                    // latest output was in the same stream,
                    // so append to it instead of making a new output.
                    // escape ANSI & HTML specials:
                    last.text = utils.fixOverwrittenChars(last.text + json.text);
                    var pre = this.element.find('div.'+subclass).last().find('pre');
                    var html = utils.fixConsole(last.text);
                    html = utils.autoLinkUrls(html);
                    // The only user content injected with this HTML call is
                    // escaped by the fixConsole() method.
                    pre.html(html);
                    // return false signals that we merged this output with the previous one,
                    // and the new output shouldn't be recorded.
                    return false;
                }
            }
        }

        if (!text.replace("\r", "")) {
            // text is nothing (empty string, \r, etc.)
            // so don't append any elements, which might add undesirable space
            // return true to indicate the output should be recorded.
            return true;
        }

        // If we got here, attach a new div
        var toinsert = this.create_output_area();
        var append_text = OutputArea.append_map[MIME_TEXT];
        if (append_text) {
            append_text.apply(this, [text, {}, toinsert]).addClass("output_stream " + subclass);
        }
        this._safe_append(toinsert);
        return true;
    };


    OutputArea.prototype.append_unrecognized = function (json) {
        var that = this;
        var toinsert = this.create_output_area();
        var subarea = $('<div/>').addClass('output_subarea output_unrecognized');
        // Unforce RTL
        subarea.attr("dir","auto");
        toinsert.append(subarea);
        subarea.append(
            $("<a>")
                .attr("href", "#")
                .text(i18n.msg.sprintf(i18n.msg._("Unrecognized output: %s"),json.output_type))
                .click(function () {
                    that.events.trigger('unrecognized_output.OutputArea', {output: json});
                })
        );
        this._safe_append(toinsert);
    };


    OutputArea.prototype.update_display_data = function (json, handle_inserted) {
        var oa = this;
        var targets;
        var display_id = (json.transient || {}).display_id;
        if (!display_id) {
            console.warn("Handling update_display with no display_id", json);
            return;
        }
        targets = this._display_id_targets[display_id];
        if (!targets) {
            console.warn("No targets for display_id", display_id, json);
            return;
        }
        // we've seen it before, update output data
        targets.map(function (target) {
            oa.outputs[target.index].data = json.data;
            oa.outputs[target.index].metadata = json.metadata;
            var toinsert = oa.create_output_area();
            if (oa.append_mime_type(json, toinsert, handle_inserted)) {
                oa._safe_append(toinsert, target.element);
            }
            target.element = toinsert;
        });

        // If we just output something that could contain latex, typeset it.
        if ((json.data[MIME_LATEX] !== undefined) ||
            (json.data[MIME_HTML] !== undefined) ||
            (json.data[MIME_MARKDOWN] !== undefined)) {
            this.typeset();
        }
        this.events.trigger('output_updated.OutputArea', {
            output: json,
            output_area: this,
        });
    };

    OutputArea.prototype._record_display_id = function (json, element) {
        // record display_id of a display_data / execute_result
        var display_id = (json.transient || {}).display_id;
        if (!display_id) return;
        // it has a display_id;
        var targets = this._display_id_targets[display_id];
        if (!targets) {
            targets = this._display_id_targets[display_id] = [];
        }
        targets.push({
            index: this.outputs.length,
            element: element,
        });
    };

    OutputArea.prototype.append_display_data = function (json, handle_inserted) {
        var toinsert = this.create_output_area();
        this._record_display_id(json, toinsert);
        if (this.append_mime_type(json, toinsert, handle_inserted)) {
            this._safe_append(toinsert);
            // If we just output latex, typeset it.
            if ((json.data[MIME_LATEX] !== undefined) ||
                (json.data[MIME_HTML] !== undefined) ||
                (json.data[MIME_MARKDOWN] !== undefined)) {
                this.typeset();
            }
        }
    };

    OutputArea.safe_outputs = {};
    OutputArea.safe_outputs[MIME_TEXT] = true;
    OutputArea.safe_outputs[MIME_LATEX] = true;
    OutputArea.safe_outputs[MIME_PNG] = true;
    OutputArea.safe_outputs[MIME_JPEG] = true;
    OutputArea.safe_outputs[MIME_GIF] = true;

    OutputArea.prototype.append_mime_type = function (json, element, handle_inserted) {
        for (var i=0; i < OutputArea.display_order.length; i++) {
            var type = OutputArea.display_order[i];
            var append = OutputArea.append_map[type];
            if ((json.data[type] !== undefined) && append) {
                var md = json.metadata || {};
                var value = json.data[type];
                var toinsert;

                try {
                    if (!this.trusted && !OutputArea.safe_outputs[type]) {
                        // not trusted, sanitize HTML
                        if (type===MIME_HTML || type==='text/svg') {
                            var parsed = $(security.sanitize_html_and_parse(value));
                            toinsert = append.apply(this, [parsed, md, element, handle_inserted]);
                        } else {
                            // don't display if we don't know how to sanitize it
                            console.log("Ignoring untrusted " + type + " output.");
                            continue;
                        }
                    } else {
                        toinsert = append.apply(this, [value, md, element, handle_inserted]);
                    }
                } catch (e) {
                    console.error('Failed to render mimetype "' + type + '" with: ', e);
                    continue;
                }

                // Since only the png and jpeg mime types call the inserted
                // callback, if the mime type is something other we must call the
                // inserted callback only when the element is actually inserted
                // into the DOM.  Use a timeout of 0 to do this.
                if ([MIME_PNG, MIME_JPEG, MIME_GIF].indexOf(type) < 0 && handle_inserted !== undefined) {
                    setTimeout(handle_inserted, 0);
                }
                this.events.trigger('output_appended.OutputArea', [type, value, md, toinsert]);
                return toinsert;
            }
        }

        return null;
    };


    var append_html = function (html, md, element) {
        var type = MIME_HTML;
        var toinsert = this.create_output_subarea(md, "output_html rendered_html", type);
        this.keyboard_manager.register_events(toinsert);
        toinsert.append(html);
        dblclick_to_reset_size(toinsert.find('img'));
        element.append(toinsert);
        return toinsert;
    };


    var append_markdown = function(text, md, element) {
        var type = MIME_MARKDOWN;
        var toinsert = this.create_output_subarea(md, "output_markdown rendered_html", type);
        markdown.render(text, {
            with_math: true,
            clean_tables: true
        }, function (err, html) {
            toinsert.append(html);
        });
        dblclick_to_reset_size(toinsert.find('img'));
        element.append(toinsert);
        return toinsert;
    };


    var append_javascript = function (js, md, element) {
        /**
         * We just eval the JS code, element appears in the local scope.
         */
        var type = MIME_JAVASCRIPT;
        var toinsert = this.create_output_subarea(md, "output_javascript rendered_html", type);
        this.keyboard_manager.register_events(toinsert);
        element.append(toinsert);

        // Fix for ipython/issues/5293, make sure `element` is the area which
        // output can be inserted into at the time of JS execution.
        element = toinsert;
        try {
            eval(js);
        } catch(err) {
            console.log(err);
            this._append_javascript_error(err, toinsert);
        }
        return toinsert;
    };


    var append_text = function (data, md, element) {
        var type = MIME_TEXT;
        var toinsert = this.create_output_subarea(md, "output_text", type);
        data = utils.fixOverwrittenChars(data);
        // escape ANSI & HTML specials in plaintext:
        data = utils.fixConsole(data);
        data = utils.autoLinkUrls(data);
        // The only user content injected with this HTML call is
        // escaped by the fixConsole() method.
        toinsert.append($("<pre/>").html(data));
        element.append(toinsert);
        return toinsert;
    };


    var append_svg = function (svg_html, md, element) {
        var type = MIME_SVG;
        var toinsert = this.create_output_subarea(md, "output_svg", type);

        // Get the svg element from within the HTML.
        // One svg is supposed, but could embed other nested svgs
        var svg = $($('<div \>').html(svg_html).find('svg')[0]);
        var svg_area = $('<div />');
        var width = svg.attr('width');
        var height = svg.attr('height');
        svg
            .width('100%')
            .height('100%');
        svg_area
            .width(width)
            .height(height);

        svg_area.append(svg);
        toinsert.append(svg_area);
        element.append(toinsert);

        return toinsert;
    };

    function dblclick_to_reset_size (img) {
        /**
         * Double-click on an image toggles confinement to notebook width
         *
         * img: jQuery element
         */

        img.dblclick(function () {
            // dblclick toggles *raw* size, disabling max-width confinement.
            if (img.hasClass('unconfined')) {
                img.removeClass('unconfined');
            } else {
                img.addClass('unconfined');
            }
        });
    }

    var set_width_height = function (img, md, mime) {
        /**
         * set width and height of an img element from metadata
         */
        var height = _get_metadata_key(md, 'height', mime);
        if (height !== undefined) img.attr('height', height);
        var width = _get_metadata_key(md, 'width', mime);
        if (width !== undefined) img.attr('width', width);
        if (_get_metadata_key(md, 'unconfined', mime)) {
            img.addClass('unconfined');
        }
    };

    OutputArea.prototype._append_img = function (src_type, md, element, handle_inserted, MIME, type_string) {
        var type = MIME;
        var toinsert = this.create_output_subarea(md, 'output_' + type_string, type);
        var img = $("<img/>");
        if (handle_inserted !== undefined) {
            img.on('load', function(){
                handle_inserted(img);
            });
        }
        img[0].src = 'data:image/' + type_string + ';base64,'+ src_type;
        set_width_height(img, md, type);
        dblclick_to_reset_size(img);
        toinsert.append(img);
        element.append(toinsert);
        return toinsert;
    };

    var append_png = function (png, md, element, handle_inserted) {
        return this._append_img(png, md, element, handle_inserted, MIME_PNG, 'png');
    };

    var append_jpeg = function (jpeg, md, element, handle_inserted) {
        return this._append_img(jpeg, md, element, handle_inserted, MIME_JPEG, 'jpeg');
    };

    var append_gif = function (gif, md, element, handle_inserted) {
        return this._append_img(gif, md, element, handle_inserted, MIME_GIF, 'gif');
    };

    var append_pdf = function (pdf, md, element) {
        var type = MIME_PDF;
        var toinsert = this.create_output_subarea(md, "output_pdf", type);
        var a = $('<a/>').attr('href', 'data:application/pdf;base64,'+pdf);
        a.attr('target', '_blank');
        a.text('View PDF');
        toinsert.append(a);
        element.append(toinsert);
        return toinsert;
     };

    var append_latex = function (latex, md, element) {
        /**
         * This method cannot do the typesetting because the latex first has to
         * be on the page.
         */
        var type = MIME_LATEX;
        var toinsert = this.create_output_subarea(md, "output_latex", type);
        toinsert.text(latex);
        element.append(toinsert);
        return toinsert;
    };

    OutputArea.prototype.append_raw_input = function (msg) {
        var that = this;
        this.expand();
        var content = msg.content;
        var area = this.create_output_area();

        // disable any other raw_inputs, if they are left around
        $("div.output_subarea.raw_input_container").remove();

        var input_type = content.password ? 'password' : 'text';

        area.append(
            $("<div/>")
            .addClass("box-flex1 output_subarea raw_input_container")
            .append(
                $("<pre/>")
                .addClass("raw_input_prompt")
                .html(utils.fixConsole(content.prompt))
                .append(
                    $("<input/>")
                    .addClass("raw_input")
                    .attr('type', input_type)
                    .attr("size", 47)
                    .keydown(function (event, ui) {
                        // make sure we submit on enter,
                        // and don't re-execute the *cell* on shift-enter
                        if (event.which === keyboard.keycodes.enter) {
                            that._submit_raw_input();
                            return false;
                        }
                    })
                )
            )
            .attr("dir","auto")
        );

        this.element.append(area);
        var raw_input = area.find('input.raw_input');
        // Register events that enable/disable the keyboard manager while raw
        // input is focused.
        this.keyboard_manager.register_events(raw_input);
        // Note, the following line used to read raw_input.focus().focus().
        // This seemed to be needed otherwise only the cell would be focused.
        // But with the modal UI, this seems to work fine with one call to focus().
        raw_input.focus();
    };

    OutputArea.prototype._submit_raw_input = function (evt) {
        var container = this.element.find("div.raw_input_container");
        var theprompt = container.find("pre.raw_input_prompt");
        var theinput = container.find("input.raw_input");
        var value = theinput.val();
        var echo  = value;
        // don't echo if it's a password
        if (theinput.attr('type') == 'password') {
            echo = '········';
        }
        var content = {
            output_type : 'stream',
            name : 'stdout',
            text : theprompt.text() + echo + '\n'
        };
        // remove form container
        container.parent().remove();
        // replace with plaintext version in stdout
        this.append_output(content);
        this.events.trigger('send_input_reply.Kernel', value);
    };


    OutputArea.prototype.handle_clear_output = function (msg) {
        /**
         * msg spec v4 had stdout, stderr, display keys
         * v4.1 replaced these with just wait
         * The default behavior is the same (stdout=stderr=display=True, wait=False),
         * so v4 messages will still be properly handled,
         * except for the rarely used clearing less than all output.
         */
        this.clear_output(msg.content.wait || false);
    };


    OutputArea.prototype.clear_output = function(wait, ignore_clear_queue) {
        if (wait) {

            // If a clear is queued, clear before adding another to the queue.
            if (this.clear_queued) {
                this.clear_output(false);
            }

            this.clear_queued = true;
        } else {

            // Fix the output div's height if the clear_output is waiting for
            // new output (it is being used in an animation).
            if (!ignore_clear_queue && this.clear_queued) {
                // this.element.height() rounds the height, so we get the exact value
                var height = this.element[0].getBoundingClientRect().height;
                this.element.height(height);
                this.clear_queued = false;
            }

            // Clear all
            // Remove load event handlers from img tags because we don't want
            // them to fire if the image is never added to the page.
            this.element.find('img').off('load');
            this.element.trigger('clearing', {output_area: this});
            this.element.html("");

            // Notify others of changes.
            this.element.trigger('changed', {output_area: this});
            this.element.trigger('cleared', {output_area: this});

            this.outputs = [];
            this._display_id_targets = {};
            this.trusted = true;
            this.unscroll_area();
            this.expand();
            return;
        }
    };


    // JSON serialization

    OutputArea.prototype.fromJSON = function (outputs, metadata) {
        var len = outputs.length;
        metadata = metadata || {};

        for (var i=0; i<len; i++) {
            this.append_output(outputs[i]);
        }
        if (metadata.collapsed !== undefined) {
            if (metadata.collapsed) {
                this.collapse();
            } else {
                this.expand();
            }
        }
        if (metadata.scrolled !== undefined) {
            this.scroll_state = metadata.scrolled;
            if (metadata.scrolled) {
                this.scroll_if_long();
            } else {
                this.unscroll_area();
            }
        }
    };

    /**
     * Return for-saving version of outputs.
     * Excludes transient values.
     */
    OutputArea.prototype.toJSON = function () {
        return this.outputs.map(function (out) {
            var out2 = {};
            Object.keys(out).map(function (key) {
                if (key != 'transient') {
                    out2[key] = out[key];
                }
            });
            return out2;
        });
    };

    /**
     * Class properties
     **/

    /**
     * Threshold to trigger autoscroll when the OutputArea is resized,
     * typically when new outputs are added.
     *
     * Behavior is undefined if autoscroll is lower than minimum_scroll_threshold,
     * unless it is < 0, in which case autoscroll will never be triggered
     *
     * @property auto_scroll_threshold
     * @type Number
     * @default 100
     *
     **/
    OutputArea.auto_scroll_threshold = 100;

    /**
     * Lower limit (in lines) for OutputArea to be made scrollable. OutputAreas
     * shorter than this are never scrolled.
     *
     * @property minimum_scroll_threshold
     * @type Number
     * @default 20
     *
     **/
    OutputArea.minimum_scroll_threshold = 20;


    OutputArea.display_order = [
        MIME_JAVASCRIPT,
        MIME_HTML,
        MIME_MARKDOWN,
        MIME_LATEX,
        MIME_SVG,
        MIME_PNG,
        MIME_JPEG,
        MIME_GIF,
        MIME_PDF,
        MIME_TEXT
    ];

    OutputArea.append_map = {};
    OutputArea.append_map[MIME_TEXT] = append_text;
    OutputArea.append_map[MIME_HTML] = append_html;
    OutputArea.append_map[MIME_MARKDOWN] = append_markdown;
    OutputArea.append_map[MIME_SVG] = append_svg;
    OutputArea.append_map[MIME_PNG] = append_png;
    OutputArea.append_map[MIME_JPEG] = append_jpeg;
    OutputArea.append_map[MIME_GIF] = append_gif;
    OutputArea.append_map[MIME_LATEX] = append_latex;
    OutputArea.append_map[MIME_JAVASCRIPT] = append_javascript;
    OutputArea.append_map[MIME_PDF] = append_pdf;

    OutputArea.prototype.mime_types = function () {
        return OutputArea.display_order;
    };

    OutputArea.prototype.register_mime_type = function (mimetype, append, options) {
        if (mimetype && typeof(append) === 'function') {
            OutputArea.output_types.push(mimetype);
            if (options.safe) OutputArea.safe_outputs[mimetype] = true;
            OutputArea.display_order.splice(options.index || 0, 0, mimetype);
            OutputArea.append_map[mimetype] = append;
        }
    };

    return {'OutputArea': OutputArea};
});
