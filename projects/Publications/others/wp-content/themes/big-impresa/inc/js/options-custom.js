/**
 * Custom scripts needed for the colorpicker, image button selectors,
 * and navigation tabs.
 */

jQuery(document).ready(function($) {

	// Loads the color pickers
	$('.of-color').wpColorPicker();

	// Image Options
	$('.of-radio-img-img').click(function(){
		$(this).parent().parent().find('.of-radio-img-img').removeClass('of-radio-img-selected');
		$(this).addClass('of-radio-img-selected');
	});

	$('.of-radio-img-label').hide();
	$('.of-radio-img-img').show();
	$('.of-radio-img-radio').hide();

	// Loads tabbed sections if they exist
	if ( $('.nav-tab-wrapper').length > 0 ) {
		options_framework_tabs();
	}

	function options_framework_tabs() {

		// Hides all the .group sections to start
		$('.group').hide();

		// Find if a selected tab is saved in localStorage
		var active_tab = '';
		if ( typeof(localStorage) != 'undefined' ) {
			active_tab = localStorage.getItem("active_tab");
		}

		// If active tab is saved and exists, load it's .group
		if (active_tab != '' && $(active_tab).length ) {
			$(active_tab).fadeIn();
			$(active_tab + '-tab').addClass('nav-tab-active');
		} else {
			$('.group:first').fadeIn();
			$('.nav-tab-wrapper a:first').addClass('nav-tab-active');
		}

		// Bind tabs clicks
		$('.nav-tab-wrapper a').click(function(evt) {

			evt.preventDefault();

			// Remove active class from all tabs
			$('.nav-tab-wrapper a').removeClass('nav-tab-active');

			$(this).addClass('nav-tab-active').blur();

			var group = $(this).attr('href');

			if (typeof(localStorage) != 'undefined' ) {
				localStorage.setItem("active_tab", $(this).attr('href') );
			}

			$('.group').hide();
			$(group).fadeIn();

			// Editor height sometimes needs adjustment when unhidden
			$('.wp-editor-wrap').each(function() {
				var editor_iframe = $(this).find('iframe');
				if ( editor_iframe.height() < 30 ) {
					editor_iframe.css({'height':'auto'});
				}
			});

		});
	}

});