// Created by: Farukham: (https://github.com/farukham/Bootstrap-Animated-Progress-Bars)
// Progress Bar
var ProgressBar = function() {
    "use strict";

    // Handle Progress Bar Horizontal
    var handleProgressBars = function() {
        $(document).ready(function() {
            $('.progress').each(function() {
                $(this).appear(function() {
                    $(this).animate({
                        opacity: 1,
                        left: "0px"
                    }, 800);
                    var w = $(this).find(".progress-bar").attr("data-width");
                    var h = $(this).find(".progress-bar").attr("data-height");
                    $(this).find(".progress-bar").animate({
                        width: w + "%",
                        height: h + "%"
                    }, 100, "linear");
                });
            });
        });
    }

    return {
        init: function() {
            handleProgressBars(); // initial setup for progressbars
        }
    }
}();

$(document).ready(function() {
    ProgressBar.init();
});
