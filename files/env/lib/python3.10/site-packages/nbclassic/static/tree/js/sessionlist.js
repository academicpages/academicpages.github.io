// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define([
    'jquery',
    'base/js/utils',
    'bidi/bidi',
], function($, utils, bidi) {
    "use strict";

    var isRTL = bidi.isMirroringEnabled();
    var SesssionList = function (options) {
        /**
         * Constructor
         *
         * Parameters:
         *  options: dictionary
         *      Dictionary of keyword arguments.
         *          events: $(Events) instance
         *          base_url : string
         */
        this.events = options.events;
        this.sessions = {};
        this.nbclassic_path = options.nbclassic_path;
        this.base_url = options.base_url || utils.get_body_data("baseUrl");

        // Add collapse arrows.
        $('#running .panel-group .panel .panel-heading a').each(function(index, el) {
            var $link = $(el);
            var $icon = $('<i />')
                .addClass('fa fa-caret-down');
            $link.append($icon);
            $link.down = true;
            $link.click(function () {
                if ($link.down) {
                    $link.down = false;
                    // jQeury doesn't know how to animate rotations.  Abuse
                    // jQueries animate function by using an unused css attribute
                    // to do the animation (borderSpacing).
                    $icon.animate({ borderSpacing: 90 }, {
                        step: function(now,fx) {
                        	isRTL ? $icon.css('transform','rotate(' + now + 'deg)') : $icon.css('transform','rotate(-' + now + 'deg)');
                        }
                    }, 250);
                } else {
                    $link.down = true;
                    // See comment above.
                    $icon.animate({ borderSpacing: 0 }, {
                        step: function(now,fx) {
                        	isRTL ? $icon.css('transform','rotate(' + now + 'deg)') : $icon.css('transform','rotate(-' + now + 'deg)'); 
                        }
                    }, 250);
                }
            });
        });
    };
    
    SesssionList.prototype.load_sessions = function(){
        var that = this;
        var settings = {
            processData : false,
            cache : false,
            type : "GET",
            dataType : "json",
            success : $.proxy(that.sessions_loaded, this),
            error : utils.log_ajax_error,
        };
        var url = utils.url_path_join(this.base_url, 'api/sessions');
        utils.ajax(url, settings);
    };

    SesssionList.prototype.sessions_loaded = function(data){
        this.sessions = {};
        var len = data.length;
        var nb_path;
        for (var i=0; i<len; i++) {
            // The classic notebook only knows about sessions for notebooks,
            // but the server now knows about more general sessions for
            // things like consoles.
            if (data[i].type === 'notebook') {
                nb_path = data[i].notebook.path;
                this.sessions[nb_path] = {
                    id: data[i].id,
                    kernel: {
                    name: data[i].kernel.name
                    }
                };
            }
        }
        this.events.trigger('sessions_loaded.Dashboard', this.sessions);
    };

    return {'SesssionList': SesssionList};
});
