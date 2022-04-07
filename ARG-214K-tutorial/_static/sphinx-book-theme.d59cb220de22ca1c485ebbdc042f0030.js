var initTriggerNavBar=()=>{if($(window).width()<768){$("#navbar-toggler").trigger("click")}}
var scrollToActive=()=>{var navbar=document.getElementById('site-navigation')
var active_pages=navbar.querySelectorAll(".active")
var active_page=active_pages[active_pages.length-1]
if(active_page!==undefined&&active_page.offsetTop>($(window).height()*.5)){navbar.scrollTop=active_page.offsetTop-($(window).height()*.2)}}
var sbRunWhenDOMLoaded=cb=>{if(document.readyState!='loading'){cb()}else if(document.addEventListener){document.addEventListener('DOMContentLoaded',cb)}else{document.attachEvent('onreadystatechange',function(){if(document.readyState=='complete')cb()})}}
function toggleFullScreen(){var navToggler=$("#navbar-toggler");if(!document.fullscreenElement){document.documentElement.requestFullscreen();if(!navToggler.hasClass("collapsed")){navToggler.click();}}else{if(document.exitFullscreen){document.exitFullscreen();if(navToggler.hasClass("collapsed")){navToggler.click();}}}}
var initTooltips=()=>{$(document).ready(function(){$('[data-toggle="tooltip"]').tooltip();});}
var initTocHide=()=>{var scrollTimeout;var throttle=200;var tocHeight=$("#bd-toc-nav").outerHeight(true)+$(".bd-toc").outerHeight(true);var hideTocAfter=tocHeight+200;var checkTocScroll=function(){var margin_content=$(".margin, .tag_margin, .full-width, .full_width, .tag_full-width, .tag_full_width, .sidebar, .tag_sidebar, .popout, .tag_popout");margin_content.each((index,item)=>{var topOffset=$(item).offset().top-$(window).scrollTop();var bottomOffset=topOffset+$(item).outerHeight(true);var removeToc=(topOffset<hideTocAfter&&bottomOffset>=0);if(removeToc&&window.pageYOffset>20){$("div.bd-toc").removeClass("show")
return false}else{$("div.bd-toc").addClass("show")};})};var manageScrolledClassOnBody=function(){if(window.scrollY>0){document.body.classList.add("scrolled");}else{document.body.classList.remove("scrolled");}}
$(window).on('scroll',function(){if(!scrollTimeout){scrollTimeout=setTimeout(function(){checkTocScroll();manageScrolledClassOnBody();scrollTimeout=null;},throttle);}});}
var printPdf=(el)=>{let tooltipID=$(el).attr("aria-describedby")
let tooltipTextDiv=$("#"+tooltipID).detach()
window.print()
$("body").append(tooltipTextDiv)}
var initThebeSBT=()=>{var title=$("div.section h1")[0]
if(!$(title).next().hasClass("thebe-launch-button")){$("<button class='thebe-launch-button'></button>").insertAfter($(title))}
initThebe();}
sbRunWhenDOMLoaded(initTooltips)
sbRunWhenDOMLoaded(initTriggerNavBar)
sbRunWhenDOMLoaded(scrollToActive)
sbRunWhenDOMLoaded(initTocHide)
