document.addEventListener('DOMContentLoaded', function() {
  const themeSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
  
  if (themeSwitch) {
    // Set initial state of checkbox
    themeSwitch.checked = sessionStorage.getItem('theme') === 'dark';

    themeSwitch.addEventListener('change', function(e) {
      if(e.target.checked) {
        sessionStorage.setItem('theme', 'dark');
        document.getElementById('theme_source').setAttribute('rel', 'stylesheet alternate');
        document.getElementById('theme_source_2').setAttribute('rel', 'stylesheet');
      } else {
        sessionStorage.setItem('theme', 'sunrise');
        document.getElementById('theme_source').setAttribute('rel', 'stylesheet');
        document.getElementById('theme_source_2').setAttribute('rel', 'stylesheet alternate');
      }
      
      // Call updateImages when theme changes
      updateImages();
    });
  }
});
