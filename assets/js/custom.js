$(document).ready(function() {
  // Smooth scrolling for anchor links
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top - 50
        }, 500);
        return false;
      }
    }
  });
  
  // Add a subtle hover effect to navigation items
  $('.greedy-nav .visible-links a').hover(
    function() {
      $(this).addClass('animated pulse');
    },
    function() {
      $(this).removeClass('animated pulse');
    }
  );
  
  // Add a subtle entrance animation to page content
  $('.page__content').addClass('animated fadeIn');
  
  // Add a subtle entrance animation to archive items
  $('.archive__item').each(function(i) {
    var $item = $(this);
    setTimeout(function() {
      $item.addClass('animated fadeInUp');
    }, 100 * i);
  });
  
  // Add a back-to-top button
  $('body').append('<a href="#" class="back-to-top">↑</a>');
  
  var amountScrolled = 300;
  
  $(window).scroll(function() {
    if ($(window).scrollTop() > amountScrolled) {
      $('a.back-to-top').fadeIn('slow');
    } else {
      $('a.back-to-top').fadeOut('slow');
    }
  });
  
  $('a.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 500);
    return false;
  });
}); 