// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

define(['jquery', 'bootstraptour', 'base/js/i18n'], function($, Tour, i18n) {
    "use strict";

    var tour_style = "<div class='popover tour'>\n" +
        "<div class='arrow'></div>\n" +
        "<div style='position:absolute; top:7px; right:7px'>\n" +
            "<button class='btn btn-default btn-sm fa fa-times' data-role='end'></button>\n" +
        "</div><h3 class='popover-title'></h3>\n" +
        "<div class='popover-content'></div>\n" +
        "<div class='popover-navigation'>\n" +
            "<button class='btn btn-default fa fa-step-backward' data-role='prev'></button>\n" +
            "<button class='btn btn-default fa fa-step-forward pull-right' data-role='next'></button>\n" +
            "<button id='tour-pause' class='btn btn-sm btn-default fa fa-pause' data-resume-text='' data-pause-text='' data-role='pause-resume'></button>\n" +
        "</div>\n" +
    "</div>";

    var NotebookTour = function (notebook, events) {
        var that = this;
        this.notebook = notebook;
        this.step_duration = 0;
        this.events = events;
        this.tour_steps = [
            { 
                title: i18n.msg._("Welcome to the Notebook Tour"),
                placement: 'bottom',
                orphan: true,
                content: i18n.msg._("You can use the left and right arrow keys to go backwards and forwards.")
            }, {
                element: "#notebook_name",
                title: i18n.msg._("Filename"),
                placement: 'bottom',
                content: i18n.msg._("Click here to change the filename for this notebook.")
            }, {
                element: $("#menus").parent(),
                placement: 'bottom',
                title: i18n.msg._("Notebook Menubar"),
                content: i18n.msg._("The menubar has menus for actions on the notebook, its cells, and the kernel it communicates with.")
            }, {
                element: "#maintoolbar",
                placement: 'bottom',
                title: i18n.msg._("Notebook Toolbar"),
                content: i18n.msg._("The toolbar has buttons for the most common actions. Hover your mouse over each button for more information.")
            }, {
                element: "#modal_indicator",
                title: i18n.msg._("Mode Indicator"),
                placement: 'bottom',
                content: i18n.msg._("The Notebook has two modes: Edit Mode and Command Mode. In this area, an indicator can appear to tell you which mode you are in."),
                onShow: function(tour) { that.command_icon_hack(); }
            }, {
                element: "#modal_indicator",
                title: i18n.msg._("Command Mode"),
                placement: 'bottom',
                onShow: function(tour) { notebook.command_mode(); that.command_icon_hack(); },
                onNext: function(tour) { that.edit_mode(); },
                content: i18n.msg._("Right now you are in Command Mode, and many keyboard shortcuts are available. In this mode, no icon is displayed in the indicator area.")
            }, {
                element: "#modal_indicator",
                title: i18n.msg._("Edit Mode"),
                placement: 'bottom',
                onShow: function(tour) { that.edit_mode(); },
                content: i18n.msg._("Pressing <code>Enter</code> or clicking in the input text area of the cell switches to Edit Mode.")
            }, {
                element: '.selected',
                title: i18n.msg._("Edit Mode"),
                placement: 'bottom',
                onShow: function(tour) { that.edit_mode(); },
                content: i18n.msg._("Notice that the border around the currently active cell changed color. Typing will insert text into the currently active cell.")
            }, {
                element: '.selected',
                title: i18n.msg._("Back to Command Mode"),
                placement: 'bottom',
                onShow: function(tour) { notebook.command_mode(); },
                content: i18n.msg._("Pressing <code>Esc</code> or clicking outside of the input text area takes you back to Command Mode.")
            }, {
                element: '#keyboard_shortcuts',
                title: i18n.msg._("Keyboard Shortcuts"),
                placement: 'bottom',
                onShow: function(tour) {
                    /** need to add `open` and `pulse` classes in 2 calls */
                    $('#help_menu').parent().addClass('open');
                    $('#help_menu').parent().addClass('pulse');
                    $('#keyboard_shortcuts').addClass('pulse');
                  },
                onHide: function(tour) { 
                    $('#help_menu').parent().removeClass('open pulse');
                    $('#keyboard_shortcuts').removeClass('pulse');
                  },
                content: i18n.msg._("You can click here to get a list of all of the keyboard shortcuts.")
            }, {
                element: "#kernel_indicator_icon",
                title: i18n.msg._("Kernel Indicator"),
                placement: 'bottom',
                onShow: function(tour) { events.trigger('kernel_idle.Kernel');},
                content: i18n.msg._("This is the Kernel indicator. It looks like this when the Kernel is idle.")
            }, {
                element: "#kernel_indicator_icon",
                title: i18n.msg._("Kernel Indicator"),
                placement: 'bottom',
                onShow: function(tour) { events.trigger('kernel_busy.Kernel'); },
                content: i18n.msg._("The Kernel indicator looks like this when the Kernel is busy.")
            }, {
                element: ".fa-stop",
                placement: 'bottom',
                title: i18n.msg._("Interrupting the Kernel"),
                onHide: function(tour) { events.trigger('kernel_idle.Kernel'); },
                content: i18n.msg._("To cancel a computation in progress, you can click here.")
            }, {
                element: "#notification_kernel",
                placement: 'bottom',
                onShow: function(tour) { $('.fa-stop').click(); },
                title: i18n.msg._("Notification Area"),
                content: i18n.msg._("Messages in response to user actions (Save, Interrupt, etc.) appear here.")
            }, {
                title: i18n.msg._("End of Tour"),
                placement: 'bottom',
                orphan: true,
                content: i18n.msg._("This concludes the Jupyter Notebook User Interface Tour.")
            }
        ];

        this.tour = new Tour({
            storage: false, // start tour from beginning every time
            debug: true,
            reflex: true, // click on element to continue tour
            animation: false,
            duration: this.step_duration,
            onStart: function() { console.log('tour started'); },
            // TODO: remove the onPause/onResume logic once pi's patch has been
            // merged upstream to make this work via data-resume-class and 
            // data-resume-text attributes.
            onPause: this.toggle_pause_play,
            onResume: this.toggle_pause_play,
            steps: this.tour_steps,
            template: tour_style,
            orphan: true
        });
        
    };

    NotebookTour.prototype.start = function () {
        console.log("let's start the tour");
        this.tour.init();
        this.tour.start();
        if (this.tour.ended())
        {
            this.tour.restart();
        }
    };

    NotebookTour.prototype.command_icon_hack =  function() {
        $('#modal_indicator').css('min-height', '18px');
    };
    
    NotebookTour.prototype.toggle_pause_play = function () { 
        $('#tour-pause').toggleClass('fa-pause fa-play'); 
    };
    
    NotebookTour.prototype.edit_mode = function() { 
        this.notebook.focus_cell(); 
        this.notebook.edit_mode();
    };

    return {'Tour': NotebookTour};

});

