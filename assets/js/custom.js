$(document).ready(function() {
  // LAYOUT FIX: Force correct positioning of sidebar and main content
  function fixLayout() {
    // Get window width
    var windowWidth = $(window).width();
    
    if (windowWidth >= 1024) { // Large screens
      $('.sidebar').css({
        'position': 'relative',
        'transform': 'none',
        'float': 'left',
        'width': '250px',
        'margin-left': '0',
        'padding-left': '0'
      });
      
      $('.page').css({
        'float': 'right',
        'width': 'calc(100% - 280px)',
        'margin-left': '0',
        'margin-right': '0',
        'clear': 'none'
      });
      
      $('.archive, .page__related').css({
        'width': 'calc(100% - 280px)',
        'float': 'right'
      });
    } 
    else if (windowWidth >= 768 && windowWidth < 1024) { // Medium screens
      $('.sidebar').css({
        'position': 'relative',
        'transform': 'none',
        'float': 'left',
        'width': '200px',
        'margin-left': '0',
        'padding-left': '0'
      });
      
      $('.page').css({
        'float': 'right',
        'width': 'calc(100% - 220px)',
        'margin-left': '0',
        'margin-right': '0',
        'clear': 'none'
      });
      
      $('.archive, .page__related').css({
        'width': 'calc(100% - 220px)',
        'float': 'right'
      });
    }
    else { // Small screens
      $('.sidebar').css({
        'position': 'relative',
        'transform': 'none',
        'float': 'none',
        'width': '100%'
      });
      
      $('.page').css({
        'float': 'none',
        'width': '100%',
        'margin-left': '0'
      });
      
      $('.archive, .page__related').css({
        'width': '100%',
        'float': 'none'
      });
    }
  }
  
  // Run layout fix on page load
  fixLayout();
  
  // Run layout fix on window resize
  $(window).resize(function() {
    fixLayout();
  });
  
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