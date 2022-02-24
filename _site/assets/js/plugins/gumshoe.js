/*!
 * gumshoejs v5.1.1
 * A simple, framework-agnostic scrollspy script.
 * (c) 2019 Chris Ferdinandi
 * MIT License
 * http://github.com/cferdinandi/gumshoe
 */

(function (root, factory) {
	if ( typeof define === 'function' && define.amd ) {
		define([], (function () {
			return factory(root);
		}));
	} else if ( typeof exports === 'object' ) {
		module.exports = factory(root);
	} else {
		root.Gumshoe = factory(root);
	}
})(typeof global !== 'undefined' ? global : typeof window !== 'undefined' ? window : this, (function (window) {

	'use strict';

	//
	// Defaults
	//

	var defaults = {

		// Active classes
		navClass: 'active',
		contentClass: 'active',

		// Nested navigation
		nested: false,
		nestedClass: 'active',

		// Offset & reflow
		offset: 0,
		reflow: false,

		// Event support
		events: true

	};


	//
	// Methods
	//

	/**
	 * Merge two or more objects together.
	 * @param   {Object}   objects  The objects to merge together
	 * @returns {Object}            Merged values of defaults and options
	 */
	var extend = function () {
		var merged = {};
		Array.prototype.forEach.call(arguments, (function (obj) {
			for (var key in obj) {
				if (!obj.hasOwnProperty(key)) return;
				merged[key] = obj[key];
			}
		}));
		return merged;
	};

	/**
	 * Emit a custom event
	 * @param  {String} type   The event type
	 * @param  {Node}   elem   The element to attach the event to
	 * @param  {Object} detail Any details to pass along with the event
	 */
	var emitEvent = function (type, elem, detail) {

		// Make sure events are enabled
		if (!detail.settings.events) return;

		// Create a new event
		var event = new CustomEvent(type, {
			bubbles: true,
			cancelable: true,
			detail: detail
		});

		// Dispatch the event
		elem.dispatchEvent(event);

	};

	/**
	 * Get an element's distance from the top of the Document.
	 * @param  {Node} elem The element
	 * @return {Number}    Distance from the top in pixels
	 */
	var getOffsetTop = function (elem) {
		var location = 0;
		if (elem.offsetParent) {
			while (elem) {
				location += elem.offsetTop;
				elem = elem.offsetParent;
			}
		}
		return location >= 0 ? location : 0;
	};

	/**
	 * Sort content from first to last in the DOM
	 * @param  {Array} contents The content areas
	 */
	var sortContents = function (contents) {
		if(contents) {
			contents.sort((function (item1, item2) {
				var offset1 = getOffsetTop(item1.content);
				var offset2 = getOffsetTop(item2.content);
				if (offset1 < offset2) return -1;
				return 1;
			}));
		}
	};

	/**
	 * Get the offset to use for calculating position
	 * @param  {Object} settings The settings for this instantiation
	 * @return {Float}           The number of pixels to offset the calculations
	 */
	var getOffset = function (settings) {

		// if the offset is a function run it
		if (typeof settings.offset === 'function') {
			return parseFloat(settings.offset());
		}

		// Otherwise, return it as-is
		return parseFloat(settings.offset);

	};

	/**
	 * Get the document element's height
	 * @private
	 * @returns {Number}
	 */
	var getDocumentHeight = function () {
		return Math.max(
			document.body.scrollHeight, document.documentElement.scrollHeight,
			document.body.offsetHeight, document.documentElement.offsetHeight,
			document.body.clientHeight, document.documentElement.clientHeight
		);
	};

	/**
	 * Determine if an element is in view
	 * @param  {Node}    elem     The element
	 * @param  {Object}  settings The settings for this instantiation
	 * @param  {Boolean} bottom   If true, check if element is above bottom of viewport instead
	 * @return {Boolean}          Returns true if element is in the viewport
	 */
	var isInView = function (elem, settings, bottom) {
		var bounds = elem.getBoundingClientRect();
		var offset = getOffset(settings);
		if (bottom) {
			return parseInt(bounds.bottom, 10) < (window.innerHeight || document.documentElement.clientHeight);
		}
		return parseInt(bounds.top, 10) <= offset;
	};

	/**
	 * Check if at the bottom of the viewport
	 * @return {Boolean} If true, page is at the bottom of the viewport
	 */
	var isAtBottom = function () {
		if (window.innerHeight + window.pageYOffset >= getDocumentHeight()) return true;
		return false;
	};

	/**
	 * Check if the last item should be used (even if not at the top of the page)
	 * @param  {Object} item     The last item
	 * @param  {Object} settings The settings for this instantiation
	 * @return {Boolean}         If true, use the last item
	 */
	var useLastItem = function (item, settings) {
		if (isAtBottom() && isInView(item.content, settings, true)) return true;
		return false;
	};

	/**
	 * Get the active content
	 * @param  {Array}  contents The content areas
	 * @param  {Object} settings The settings for this instantiation
	 * @return {Object}          The content area and matching navigation link
	 */
	var getActive = function (contents, settings) {
		var last = contents[contents.length-1];
		if (useLastItem(last, settings)) return last;
		for (var i = contents.length - 1; i >= 0; i--) {
			if (isInView(contents[i].content, settings)) return contents[i];
		}
	};

	/**
	 * Deactivate parent navs in a nested navigation
	 * @param  {Node}   nav      The starting navigation element
	 * @param  {Object} settings The settings for this instantiation
	 */
	var deactivateNested = function (nav, settings) {

		// If nesting isn't activated, bail
		if (!settings.nested) return;

		// Get the parent navigation
		var li = nav.parentNode.closest('li');
		if (!li) return;

		// Remove the active class
		li.classList.remove(settings.nestedClass);

		// Apply recursively to any parent navigation elements
		deactivateNested(li, settings);

	};

	/**
	 * Deactivate a nav and content area
	 * @param  {Object} items    The nav item and content to deactivate
	 * @param  {Object} settings The settings for this instantiation
	 */
	var deactivate = function (items, settings) {

		// Make sure their are items to deactivate
		if (!items) return;

		// Get the parent list item
		var li = items.nav.closest('li');
		if (!li) return;

		// Remove the active class from the nav and content
		li.classList.remove(settings.navClass);
		items.content.classList.remove(settings.contentClass);

		// Deactivate any parent navs in a nested navigation
		deactivateNested(li, settings);

		// Emit a custom event
		emitEvent('gumshoeDeactivate', li, {
			link: items.nav,
			content: items.content,
			settings: settings
		});

	};


	/**
	 * Activate parent navs in a nested navigation
	 * @param  {Node}   nav      The starting navigation element
	 * @param  {Object} settings The settings for this instantiation
	 */
	var activateNested = function (nav, settings) {

		// If nesting isn't activated, bail
		if (!settings.nested) return;

		// Get the parent navigation
		var li = nav.parentNode.closest('li');
		if (!li) return;

		// Add the active class
		li.classList.add(settings.nestedClass);

		// Apply recursively to any parent navigation elements
		activateNested(li, settings);

	};

	/**
	 * Activate a nav and content area
	 * @param  {Object} items    The nav item and content to activate
	 * @param  {Object} settings The settings for this instantiation
	 */
	var activate = function (items, settings) {

		// Make sure their are items to activate
		if (!items) return;

		// Get the parent list item
		var li = items.nav.closest('li');
		if (!li) return;

		// Add the active class to the nav and content
		li.classList.add(settings.navClass);
		items.content.classList.add(settings.contentClass);

		// Activate any parent navs in a nested navigation
		activateNested(li, settings);

		// Emit a custom event
		emitEvent('gumshoeActivate', li, {
			link: items.nav,
			content: items.content,
			settings: settings
		});

	};

	/**
	 * Create the Constructor object
	 * @param {String} selector The selector to use for navigation items
	 * @param {Object} options  User options and settings
	 */
	var Constructor = function (selector, options) {

		//
		// Variables
		//

		var publicAPIs = {};
		var navItems, contents, current, timeout, settings;


		//
		// Methods
		//

		/**
		 * Set variables from DOM elements
		 */
		publicAPIs.setup = function () {

			// Get all nav items
			navItems = document.querySelectorAll(selector);

			// Create contents array
			contents = [];

			// Loop through each item, get it's matching content, and push to the array
			Array.prototype.forEach.call(navItems, (function (item) {

				// Get the content for the nav item
				var content = document.getElementById(decodeURIComponent(item.hash.substr(1)));
				if (!content) return;

				// Push to the contents array
				contents.push({
					nav: item,
					content: content
				});

			}));

			// Sort contents by the order they appear in the DOM
			sortContents(contents);

		};

		/**
		 * Detect which content is currently active
		 */
		publicAPIs.detect = function () {

			// Get the active content
			var active = getActive(contents, settings);

			// if there's no active content, deactivate and bail
			if (!active) {
				if (current) {
					deactivate(current, settings);
					current = null;
				}
				return;
			}

			// If the active content is the one currently active, do nothing
			if (current && active.content === current.content) return;

			// Deactivate the current content and activate the new content
			deactivate(current, settings);
			activate(active, settings);

			// Update the currently active content
			current = active;

		};

		/**
		 * Detect the active content on scroll
		 * Debounced for performance
		 */
		var scrollHandler = function (event) {

			// If there's a timer, cancel it
			if (timeout) {
				window.cancelAnimationFrame(timeout);
			}

			// Setup debounce callback
			timeout = window.requestAnimationFrame(publicAPIs.detect);

		};

		/**
		 * Update content sorting on resize
		 * Debounced for performance
		 */
		var resizeHandler = function (event) {

			// If there's a timer, cancel it
			if (timeout) {
				window.cancelAnimationFrame(timeout);
			}

			// Setup debounce callback
			timeout = window.requestAnimationFrame((function () {
				sortContents(contents);
				publicAPIs.detect();
			}));

		};

		/**
		 * Destroy the current instantiation
		 */
		publicAPIs.destroy = function () {

			// Undo DOM changes
			if (current) {
				deactivate(current, settings);
			}

			// Remove event listeners
			window.removeEventListener('scroll', scrollHandler, false);
			if (settings.reflow) {
				window.removeEventListener('resize', resizeHandler, false);
			}

			// Reset variables
			contents = null;
			navItems = null;
			current = null;
			timeout = null;
			settings = null;

		};

		/**
		 * Initialize the current instantiation
		 */
		var init = function () {

			// Merge user options into defaults
			settings = extend(defaults, options || {});

			// Setup variables based on the current DOM
			publicAPIs.setup();

			// Find the currently active content
			publicAPIs.detect();

			// Setup event listeners
			window.addEventListener('scroll', scrollHandler, false);
			if (settings.reflow) {
				window.addEventListener('resize', resizeHandler, false);
			}

		};


		//
		// Initialize and return the public APIs
		//

		init();
		return publicAPIs;

	};


	//
	// Return the Constructor
	//

	return Constructor;

}));