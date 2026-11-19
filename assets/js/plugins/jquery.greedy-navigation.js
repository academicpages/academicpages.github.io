/*
* Greedy Navigation
*
* http://codepen.io/lukejacksonn/pen/PwmwWV
*
*/

var $nav = $('#site-nav');
var $btn = $('#site-nav > .greedy-nav__toggle');
var $vlinks = $('#site-nav .visible-links');
var $navLinks = $vlinks.find('.masthead__nav-link-list');
var $navBrand = $vlinks.children('.masthead__menu-item--lg');
var $hlinks = $('#site-nav .hidden-links');

var breaks = [];

function getVisibleLinksWidth() {

  var width = 0;

  $navLinks.children('li').each(function () {
    width += $(this).outerWidth(true);
  });

  return width;
}

function getAvailableSpace() {

  var brandWidth = $navBrand.outerWidth(true);

  return Math.max(0, $nav.outerWidth() - (brandWidth * 2));
}

function updateNav() {

  // The visible list is overflowing the nav
  if (getVisibleLinksWidth() > getAvailableSpace()) {

    while (getVisibleLinksWidth() > getAvailableSpace() && $navLinks.children('li').length > 0) {
      // Record the width of the list
      breaks.push(getVisibleLinksWidth());

      // Move item to the hidden list
      $navLinks.children('li').last().prependTo($hlinks);

      // Show the dropdown btn
      $btn.removeClass("hidden");
    }

    // The visible list is not overflowing
  } else {

    var availableSpace = getAvailableSpace();

    // There is space for another item in the nav
    while (breaks.length > 0 && availableSpace > breaks[breaks.length - 1]) {
      // Move the item to the visible list
      $hlinks.children().first().appendTo($navLinks);
      breaks.pop();
    }

    // Hide the dropdown btn if hidden list is empty
    if (breaks.length < 1) {
      $btn.addClass('hidden');
      $btn.removeClass('close');
      $hlinks.addClass('hidden');
    }
  }

  // Keep counter updated
  $btn.attr("count", breaks.length);

}

// Window listeners

$(window).on('resize', function () {
  updateNav();
});
screen.orientation.addEventListener("change", function () {
  updateNav();
});

$btn.on('click', function () {
  $hlinks.toggleClass('hidden');
  $(this).toggleClass('close');
});

updateNav();