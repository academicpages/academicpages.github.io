$(document).ready(function() {
  var preEls = $('pre');

  $('.example-code-link').click(function(e) {
    e.preventDefault();
    $(this).parent().next().slideToggle();
  });

  // Dynamically add PrismJS class for syntax highlight
  preEls.filter('[class*="js"]').find('code').addClass('language-javascript');
  preEls.filter('.css').find('code').addClass('language-css');
});
