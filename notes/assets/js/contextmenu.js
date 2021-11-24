(function() {

"use strict";

/* Helper function to check if the click event happened 
   inside the specfied css element or outside */
function clickInsideElement(e, className) {
    var el = e.srsElement || e.target;
    if (el.classList.contains(className)) {
        return el;
    } else {
        while (el = el.parentNode) {
            if (el.classList && el.classList.contains(className)) {
                return el;
            }
        }
    }

    return false;
}

/* Helper function to get the position of the event */
function getPosition(e) {
    var posX = 0;
    var posY = 0;

    if (!e) var e = window.event;

    if (e.pageX || e.pageY) {
        posX = e.pageX;
        posY = e.pageY;
    } else if (e.clientX || e.clientY) {
        posX = e.clientX + document.body.scrollLeft + 
            document.documentElement.scrollLeft;
        posY = e.clientY + document.body.srollTop +
            document.documentElement.scrollTop;
    }

    return  {
        x: posX,
        y: posY
    }
}

/* Variables related to main context menu */
var contextMenuClassName = "context-menu";
var contextMenuItemClassName = "context-menu__item";
var contextMenuLinkClassName = "context-menu__link";
var contextMenuActive = "context-menu--active";

/* Variables related to context menu results */
var contextMenuResActive = "context-menu-res--active";
var contextMenuResClassName = "context-menu-res"
var contextMenuResLinkClassName = "context-menu-res__link";



var feedItemClassName = "feed-title-excerpt-block";
var feedItemInContext;

var clickCoords;
var clickCoordsX;
var clickCoordsY;

var menu = document.querySelector("#context-menu");
var menuItems = menu.querySelectorAll(".context-menu__item");
var menuState = 0;
var menuWidth;
var menuHeight;
var menuPosition;
var menuPositionX;
var menuPositionY;

var resMenu = document.querySelector("#context-menu-res");
var resMenuState = 0;
var resMenuWidth;
var resMenuHeight;

var windowWidth;
var windowHeight;

function positionMenu(e) {
    clickCoords = getPosition(e);
    clickCoordsX = clickCoords.x;
    clickCoordsY = clickCoords.y;
  
    menuWidth = menu.offsetWidth + 4;
    menuHeight = menu.offsetHeight + 4;
  
    windowWidth = window.innerWidth;
    windowHeight = window.innerHeight;
  
    if ( (windowWidth - clickCoordsX) < menuWidth ) {
      menu.style.left = windowWidth - menuWidth + "px";
    } else {
      menu.style.left = clickCoordsX + "px";
    }
  
    
    menu.style.top = clickCoordsY + "px";
}

function positionContextMenuRes() {
    
    resMenuWidth = resMenu.offsetWidth + 10;
    resMenuHeight = resMenu.offsetHeight + 10;
  
    windowWidth = window.innerWidth;
    windowHeight = window.innerHeight;
  
    if ( (windowWidth - clickCoordsX) < resMenuWidth ) {
      resMenu.style.left = windowWidth - resMenuWidth + "px";
    } else {
      resMenu.style.left = clickCoordsX + "px";
    }
  
    resMenu.style.top = clickCoordsY + "px";

} 



function init() {
    contextListener();
    clickListener();
    contextResClickListener();
    keyupListener();
    resizeListener();
}

function resizeListener() {
    window.onresize = function(e) {
      toggleMenuOff();
      toggleContextResMenuOff();
    };
}


async function getRelatedHTML(dataUrl) {
  let response = await fetch(dataUrl);
  let responseText = response.text();
  return responseText;
}


function showRelated(dataAction, dataUrl) {
  getRelatedHTML(dataUrl)
   .then(function (responseText) {
    let parser = new DOMParser();
    let doc = parser.parseFromString(responseText, "text/html");
    var relatedItems;
    var contextMenuResTitle;
    if(dataAction == "backlinks") {
        relatedItems = doc.getElementById("jekyll-seamless-backlinks");
        contextMenuResTitle = document.createTextNode("Linked References");
    } else {
        relatedItems = doc.getElementById("jekyll-seamless-relatedposts");
        contextMenuResTitle = document.createTextNode("Related by Tag");
    }
    var relatedItemHTMLTitle = document.createElement("p");
    relatedItemHTMLTitle.setAttribute("class", "feed-relatedItems");
    relatedItemHTMLTitle.style.fontSize = "14px";
    relatedItemHTMLTitle.style.color = "#777";
    relatedItemHTMLTitle.style.fontWeight = "600";
    relatedItemHTMLTitle.style.fontFamily = "Inter";
    var relatedItemHTML = document.createElement("ul");

    if (relatedItems == null) {
        contextMenuResTitle = document.createTextNode("Nothing Found ");
        relatedItemHTMLTitle.appendChild(contextMenuResTitle);
    } else {
    var urls = relatedItems.getElementsByTagName("a");
    var titles = relatedItems.querySelectorAll(".related-title");
    relatedItemHTMLTitle.appendChild(contextMenuResTitle);
    for (var i = 0; i < urls.length; i++) {
        var newLink = document.createElement("li");
        newLink.style.listStyle = "none";
        
        var newAnchor = document.createElement("a");
        newAnchor.setAttribute("href", urls[i].getAttribute("href"));
        newAnchor.setAttribute("class", contextMenuResLinkClassName);
        newAnchor.appendChild(document.createTextNode(titles[i].innerHTML));
        newAnchor.style.textDecoration = "none";
        newAnchor.style.fontSize = "12px";
        newAnchor.style.color = "#4183c4";
        
        newLink.appendChild(newAnchor);
        
        relatedItemHTML.appendChild(newLink);
    }
    }
    relatedItemHTML.prepend(relatedItemHTMLTitle);
    relatedItemHTML.style.marginLeft = "-20px";
    relatedItemHTML.style.paddingRight = "10px";
    toggleContextResMenuOn();
    resMenu.appendChild(relatedItemHTML);
    positionContextMenuRes();
   }).catch(function(err) {
      console.warn("Oops, something went wrong.",err);
   });

}

/* No More Ajaxing
function showRelated(dataAction, dataUrl) {
    var xhr = new XMLHttpRequest();
      xhr.open("GET", dataUrl, true);
      xhr.onload = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            let parser = new DOMParser();
            let doc = parser.parseFromString(xhr.responseText, "text/html");
            var relatedItems;
            var contextMenuResTitle;
            if(dataAction == "backlinks") {
                relatedItems = doc.getElementById("backlinks");
                contextMenuResTitle = document.createTextNode("Linked References");
            } else {
                relatedItems = doc.getElementById("relatedposts");
                contextMenuResTitle = document.createTextNode("Related by Tag");
            }

            var relatedItemHTMLTitle = document.createElement("p");
            relatedItemHTMLTitle.setAttribute("class", "feed-relatedItems");
            relatedItemHTMLTitle.style.fontSize = "14px";
            relatedItemHTMLTitle.style.color = "#777";
            relatedItemHTMLTitle.style.fontWeight = "600";
            var relatedItemHTML = document.createElement("ul");

            if (relatedItems == null) {
                contextMenuResTitle = document.createTextNode("Nothing Found ");
                relatedItemHTMLTitle.appendChild(contextMenuResTitle);
            } else {
            var urls = relatedItems.getElementsByTagName("a");
            var titles = relatedItems.querySelectorAll(".related-title");
            relatedItemHTMLTitle.appendChild(contextMenuResTitle);
            for (var i = 0; i < urls.length; i++) {
                var newLink = document.createElement("li");
                newLink.style.listStyle = "none";
                
                var newAnchor = document.createElement("a");
                newAnchor.setAttribute("href", urls[i].getAttribute("href"));
                newAnchor.setAttribute("class", contextMenuResLinkClassName);
                newAnchor.appendChild(document.createTextNode(titles[i].innerHTML));
                newAnchor.style.textDecoration = "none";
                newAnchor.style.fontSize = "12px";
                newAnchor.style.color = "#4183c4";
                
                newLink.appendChild(newAnchor);
                
                relatedItemHTML.appendChild(newLink);
            }
            }
            relatedItemHTML.prepend(relatedItemHTMLTitle);
            relatedItemHTML.style.marginLeft = "-20px";
            relatedItemHTML.style.paddingRight = "10px";
            toggleContextResMenuOn();
            resMenu.appendChild(relatedItemHTML);
            positionContextMenuRes();
        } else {
            console.error(xhr.statusText);
          }
        }
      };
      xhr.onerror = function (e) {
        console.error(xhr.statusText);
      };
      xhr.send(null);
}
*/

function menuItemListener( link , e ) {
      var dataUrl = feedItemInContext.getAttribute("data-url");
      var dataAction = link.getAttribute("data-action");
      switch(dataAction)  {
        case 'backlinks':
            showRelated(dataAction, dataUrl);
            break;
        case 'related-posts':
            showRelated(dataAction, dataUrl);
            break;
        case 'new-tab':
            window.open(dataUrl, '_blank');
            break;
        default:
            break;
      }

     /*  */

    toggleMenuOff();
  }


function contextListener() {
  document.addEventListener( "contextmenu", function(e) {
    feedItemInContext = clickInsideElement( e, feedItemClassName );
    if ( feedItemInContext ) {
      e.preventDefault();
      toggleContextResMenuOff();
      toggleMenuOn();
      positionMenu(e);
    } else {
      feedItemInContext = null;
      toggleContextResMenuOff();
      toggleMenuOff();
    }
  });
}

function clickListener() {
    document.addEventListener( "click", function(e) {
      var clickeElIsLink = clickInsideElement( e, contextMenuLinkClassName );
  
      if ( clickeElIsLink ) {
        e.preventDefault();
        menuItemListener( clickeElIsLink, e );
      } else {
        var button = e.which || e.button;
        if ( button === 1 ) {
          toggleMenuOff();
        }
      }
    });
  }

function contextResClickListener() {
    document.addEventListener( "click", function(e) {
      var clickeElIsLink = clickInsideElement( e, contextMenuResLinkClassName );
  
      if ( !clickeElIsLink ) {
        var button = e.which || e.button;
        if ( button === 1 ) {
          toggleContextResMenuOff();
        }
      }
    });
  }

  function keyupListener() {
    window.onkeyup = function(e) {
      if ( e.keyCode === 27 ) {
        toggleMenuOff();
      }
    }
  }

function toggleMenuOn() {
  if ( menuState !== 1 ) {
    menuState = 1;
    menu.classList.add(contextMenuActive);
  }
}

function toggleMenuOff() {
    if ( menuState !== 0 ) {
      menuState = 0;
      menu.classList.remove(contextMenuActive);
    }
}

function toggleContextResMenuOn() {
    if ( resMenuState !== 1 ) {
        while (resMenu.firstChild) {
            resMenu.removeChild(resMenu.lastChild);
        }   
        resMenuState = 1;
        resMenu.classList.add(contextMenuResActive);
    }
}

function toggleContextResMenuOff() {
    if ( resMenuState !== 0 ) {
        resMenuState = 0;
        resMenu.classList.remove(contextMenuResActive);
        while (resMenu.firstChild) {
            resMenu.removeChild(resMenu.lastChild);
        }   
    }
}


init();

})();