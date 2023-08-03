/*
 * Reveal.js menu plugin
 * MIT licensed
 * (c) Greg Denehy 2020
 */

const Plugin = () => {
  const ieVersion = (function () {
    let browser = /(msie) ([\w.]+)/.exec(
      window.navigator.userAgent.toLowerCase()
    );
    if (browser && browser[1] === 'msie') {
      return parseFloat(browser[2]);
    }
    return null;
  })();

  var deck;
  var config;
  var options;
  var initialised = false;

  function scriptPath() {
    // obtain plugin path from the script element
    var path;

    const script = document.querySelector('script[src$="menu.js"]');
    if (script) {
      var sel = document.querySelector('script[src$="menu.js"]');
      if (sel) {
        path = sel.src.slice(0, -7);
      }
    } else {
      path = import.meta.url.slice(0, import.meta.url.lastIndexOf('/') + 1);
    }

    return path;
  }

  function initOptions(config) {
    options = config.menu || {};
    options.path = options.path || scriptPath() || 'plugin/menu/';
    if (!options.path.endsWith('/')) {
      options.path += '/';
    }

    // Set defaults
    if (options.side === undefined) options.side = 'left';

    if (options.numbers === undefined) options.numbers = false;

    if (typeof options.titleSelector !== 'string')
      options.titleSelector = 'h1, h2, h3, h4, h5';

    if (options.hideMissingTitles === undefined)
      options.hideMissingTitles = false;

    if (options.useTextContentForMissingTitles === undefined)
      options.useTextContentForMissingTitles = false;

    if (options.markers === undefined) options.markers = true;

    if (typeof options.themesPath !== 'string')
      options.themesPath = 'dist/theme/';
    if (!options.themesPath.endsWith('/')) options.themesPath += '/';

    if (!select('link#theme')) options.themes = false;
    if (options.themes === true) {
      options.themes = [
        { name: 'Black', theme: options.themesPath + 'black.css' },
        { name: 'White', theme: options.themesPath + 'white.css' },
        { name: 'League', theme: options.themesPath + 'league.css' },
        { name: 'Sky', theme: options.themesPath + 'sky.css' },
        { name: 'Beige', theme: options.themesPath + 'beige.css' },
        { name: 'Simple', theme: options.themesPath + 'simple.css' },
        { name: 'Serif', theme: options.themesPath + 'serif.css' },
        { name: 'Blood', theme: options.themesPath + 'blood.css' },
        { name: 'Night', theme: options.themesPath + 'night.css' },
        { name: 'Moon', theme: options.themesPath + 'moon.css' },
        { name: 'Solarized', theme: options.themesPath + 'solarized.css' }
      ];
    } else if (!Array.isArray(options.themes)) {
      options.themes = false;
    }

    if (options.transitions === undefined) options.transitions = false;
    if (options.transitions === true) {
      options.transitions = [
        'None',
        'Fade',
        'Slide',
        'Convex',
        'Concave',
        'Zoom'
      ];
    } else if (
      options.transitions !== false &&
      (!Array.isArray(options.transitions) ||
        !options.transitions.every(function (e) {
          return typeof e === 'string';
        }))
    ) {
      console.error(
        "reveal.js-menu error: transitions config value must be 'true' or an array of strings, eg ['None', 'Fade', 'Slide')"
      );
      options.transitions = false;
    }
    if (ieVersion && ieVersion <= 9) {
      // transitions aren't support in IE9 anyway, so no point in showing them
      options.transitions = false;
    }

    if (typeof options.openButton === 'undefined') options.openButton = true;

    if (typeof options.openSlideNumber === 'undefined')
      options.openSlideNumber = false;

    if (typeof options.keyboard === 'undefined') options.keyboard = true;

    if (typeof options.sticky === 'undefined') options.sticky = false;

    if (typeof options.autoOpen === 'undefined') options.autoOpen = true;

    if (typeof options.delayInit === 'undefined') options.delayInit = false;

    if (typeof options.openOnInit === 'undefined') options.openOnInit = false;
  }

  var mouseSelectionEnabled = true;
  function disableMouseSelection() {
    mouseSelectionEnabled = false;
  }

  function reenableMouseSelection() {
    // wait until the mouse has moved before re-enabling mouse selection
    // to avoid selections on scroll
    select('nav.slide-menu').addEventListener('mousemove', function fn(e) {
      select('nav.slide-menu').removeEventListener('mousemove', fn);
      //XXX this should select the item under the mouse
      mouseSelectionEnabled = true;
    });
  }

  //
  // Keyboard handling
  //
  function getOffset(el) {
    var _x = 0;
    var _y = 0;
    while (el && !isNaN(el.offsetLeft) && !isNaN(el.offsetTop)) {
      _x += el.offsetLeft - el.scrollLeft;
      _y += el.offsetTop - el.scrollTop;
      el = el.offsetParent;
    }
    return { top: _y, left: _x };
  }

  function visibleOffset(el) {
    var offsetFromTop = getOffset(el).top - el.offsetParent.offsetTop;
    if (offsetFromTop < 0) return -offsetFromTop;
    var offsetFromBottom =
      el.offsetParent.offsetHeight -
      (el.offsetTop - el.offsetParent.scrollTop + el.offsetHeight);
    if (offsetFromBottom < 0) return offsetFromBottom;
    return 0;
  }

  function keepVisible(el) {
    var offset = visibleOffset(el);
    if (offset) {
      disableMouseSelection();
      el.scrollIntoView(offset > 0);
      reenableMouseSelection();
    }
  }

  function scrollItemToTop(el) {
    disableMouseSelection();
    el.offsetParent.scrollTop = el.offsetTop;
    reenableMouseSelection();
  }

  function scrollItemToBottom(el) {
    disableMouseSelection();
    el.offsetParent.scrollTop =
      el.offsetTop - el.offsetParent.offsetHeight + el.offsetHeight;
    reenableMouseSelection();
  }

  function selectItem(el) {
    el.classList.add('selected');
    keepVisible(el);
    if (options.sticky && options.autoOpen) openItem(el);
  }

  function onDocumentKeyDown(event) {
    // opening menu is handled by registering key binding with Reveal below
    if (isOpen()) {
      event.stopImmediatePropagation();
      switch (event.keyCode) {
        // case 77:
        // 	closeMenu();
        // 	break;
        // h, left - change panel
        case 72:
        case 37:
          prevPanel();
          break;
        // l, right - change panel
        case 76:
        case 39:
          nextPanel();
          break;
        // k, up
        case 75:
        case 38:
          var currItem =
            select('.active-menu-panel .slide-menu-items li.selected') ||
            select('.active-menu-panel .slide-menu-items li.active');
          if (currItem) {
            selectAll('.active-menu-panel .slide-menu-items li').forEach(
              function (item) {
                item.classList.remove('selected');
              }
            );
            var nextItem =
              select(
                '.active-menu-panel .slide-menu-items li[data-item="' +
                  (parseInt(currItem.getAttribute('data-item')) - 1) +
                  '"]'
              ) || currItem;
            selectItem(nextItem);
          } else {
            var item = select(
              '.active-menu-panel .slide-menu-items li.slide-menu-item'
            );
            if (item) selectItem(item);
          }
          break;
        // j, down
        case 74:
        case 40:
          var currItem =
            select('.active-menu-panel .slide-menu-items li.selected') ||
            select('.active-menu-panel .slide-menu-items li.active');
          if (currItem) {
            selectAll('.active-menu-panel .slide-menu-items li').forEach(
              function (item) {
                item.classList.remove('selected');
              }
            );
            var nextItem =
              select(
                '.active-menu-panel .slide-menu-items li[data-item="' +
                  (parseInt(currItem.getAttribute('data-item')) + 1) +
                  '"]'
              ) || currItem;
            selectItem(nextItem);
          } else {
            var item = select(
              '.active-menu-panel .slide-menu-items li.slide-menu-item'
            );
            if (item) selectItem(item);
          }
          break;
        // pageup, u
        case 33:
        case 85:
          var itemsAbove = selectAll(
            '.active-menu-panel .slide-menu-items li'
          ).filter(function (item) {
            return visibleOffset(item) > 0;
          });
          var visibleItems = selectAll(
            '.active-menu-panel .slide-menu-items li'
          ).filter(function (item) {
            return visibleOffset(item) == 0;
          });

          var firstVisible =
            itemsAbove.length > 0 &&
            Math.abs(visibleOffset(itemsAbove[itemsAbove.length - 1])) <
              itemsAbove[itemsAbove.length - 1].clientHeight
              ? itemsAbove[itemsAbove.length - 1]
              : visibleItems[0];
          if (firstVisible) {
            if (
              firstVisible.classList.contains('selected') &&
              itemsAbove.length > 0
            ) {
              // at top of viewport already, page scroll (if not at start)
              // ...move selected item to bottom, and change selection to last fully visible item at top
              scrollItemToBottom(firstVisible);
              visibleItems = selectAll(
                '.active-menu-panel .slide-menu-items li'
              ).filter(function (item) {
                return visibleOffset(item) == 0;
              });
              if (visibleItems[0] == firstVisible) {
                // prev item is still beyond the viewport (for custom panels)
                firstVisible = itemsAbove[itemsAbove.length - 1];
              } else {
                firstVisible = visibleItems[0];
              }
            }
            selectAll('.active-menu-panel .slide-menu-items li').forEach(
              function (item) {
                item.classList.remove('selected');
              }
            );
            selectItem(firstVisible);
            // ensure selected item is positioned at the top of the viewport
            scrollItemToTop(firstVisible);
          }
          break;
        // pagedown, d
        case 34:
        case 68:
          var visibleItems = selectAll(
            '.active-menu-panel .slide-menu-items li'
          ).filter(function (item) {
            return visibleOffset(item) == 0;
          });
          var itemsBelow = selectAll(
            '.active-menu-panel .slide-menu-items li'
          ).filter(function (item) {
            return visibleOffset(item) < 0;
          });

          var lastVisible =
            itemsBelow.length > 0 &&
            Math.abs(visibleOffset(itemsBelow[0])) < itemsBelow[0].clientHeight
              ? itemsBelow[0]
              : visibleItems[visibleItems.length - 1];
          if (lastVisible) {
            if (
              lastVisible.classList.contains('selected') &&
              itemsBelow.length > 0
            ) {
              // at bottom of viewport already, page scroll (if not at end)
              // ...move selected item to top, and change selection to last fully visible item at bottom
              scrollItemToTop(lastVisible);
              visibleItems = selectAll(
                '.active-menu-panel .slide-menu-items li'
              ).filter(function (item) {
                return visibleOffset(item) == 0;
              });
              if (visibleItems[visibleItems.length - 1] == lastVisible) {
                // next item is still beyond the viewport (for custom panels)
                lastVisible = itemsBelow[0];
              } else {
                lastVisible = visibleItems[visibleItems.length - 1];
              }
            }
            selectAll('.active-menu-panel .slide-menu-items li').forEach(
              function (item) {
                item.classList.remove('selected');
              }
            );
            selectItem(lastVisible);
            // ensure selected item is positioned at the bottom of the viewport
            scrollItemToBottom(lastVisible);
          }
          break;
        // home
        case 36:
          selectAll('.active-menu-panel .slide-menu-items li').forEach(
            function (item) {
              item.classList.remove('selected');
            }
          );
          var item = select(
            '.active-menu-panel .slide-menu-items li:first-of-type'
          );
          if (item) {
            item.classList.add('selected');
            keepVisible(item);
          }
          break;
        // end
        case 35:
          selectAll('.active-menu-panel .slide-menu-items li').forEach(
            function (item) {
              item.classList.remove('selected');
            }
          );
          var item = select(
            '.active-menu-panel .slide-menu-items:last-of-type li:last-of-type'
          );
          if (item) {
            item.classList.add('selected');
            keepVisible(item);
          }
          break;
        // space, return
        case 32:
        case 13:
          var currItem = select(
            '.active-menu-panel .slide-menu-items li.selected'
          );
          if (currItem) {
            openItem(currItem, true);
          }
          break;
        // esc
        case 27:
          closeMenu(null, true);
          break;
      }
    }
  }

  //
  // Utilty functions
  //

  function openMenu(event) {
    if (event) event.preventDefault();
    if (!isOpen()) {
      select('body').classList.add('slide-menu-active');
      select('.reveal').classList.add(
        'has-' + options.effect + '-' + options.side
      );
      select('.slide-menu').classList.add('active');
      select('.slide-menu-overlay').classList.add('active');

      // identify active theme
      if (options.themes) {
        selectAll('div[data-panel="Themes"] li').forEach(function (i) {
          i.classList.remove('active');
        });
        selectAll(
          'li[data-theme="' + select('link#theme').getAttribute('href') + '"]'
        ).forEach(function (i) {
          i.classList.add('active');
        });
      }

      // identify active transition
      if (options.transitions) {
        selectAll('div[data-panel="Transitions"] li').forEach(function (i) {
          i.classList.remove('active');
        });
        selectAll('li[data-transition="' + config.transition + '"]').forEach(
          function (i) {
            i.classList.add('active');
          }
        );
      }

      // set item selections to match active items
      var items = selectAll('.slide-menu-panel li.active');
      items.forEach(function (i) {
        i.classList.add('selected');
        keepVisible(i);
      });
    }
  }

  function closeMenu(event, force) {
    if (event) event.preventDefault();
    if (!options.sticky || force) {
      select('body').classList.remove('slide-menu-active');
      select('.reveal').classList.remove(
        'has-' + options.effect + '-' + options.side
      );
      select('.slide-menu').classList.remove('active');
      select('.slide-menu-overlay').classList.remove('active');
      selectAll('.slide-menu-panel li.selected').forEach(function (i) {
        i.classList.remove('selected');
      });
    }
  }

  function toggleMenu(event) {
    if (isOpen()) {
      closeMenu(event, true);
    } else {
      openMenu(event);
    }
  }

  function isOpen() {
    return select('body').classList.contains('slide-menu-active');
  }

  function openPanel(event, ref) {
    openMenu(event);
    var panel = ref;
    if (typeof ref !== 'string') {
      panel = event.currentTarget.getAttribute('data-panel');
    }
    select('.slide-menu-toolbar > li.active-toolbar-button').classList.remove(
      'active-toolbar-button'
    );
    select('li[data-panel="' + panel + '"]').classList.add(
      'active-toolbar-button'
    );
    select('.slide-menu-panel.active-menu-panel').classList.remove(
      'active-menu-panel'
    );
    select('div[data-panel="' + panel + '"]').classList.add(
      'active-menu-panel'
    );
  }

  function nextPanel() {
    var next =
      (parseInt(select('.active-toolbar-button').getAttribute('data-button')) +
        1) %
      buttons;
    openPanel(
      null,
      select('.toolbar-panel-button[data-button="' + next + '"]').getAttribute(
        'data-panel'
      )
    );
  }

  function prevPanel() {
    var next =
      parseInt(select('.active-toolbar-button').getAttribute('data-button')) -
      1;
    if (next < 0) {
      next = buttons - 1;
    }
    openPanel(
      null,
      select('.toolbar-panel-button[data-button="' + next + '"]').getAttribute(
        'data-panel'
      )
    );
  }

  function openItem(item, force) {
    var h = parseInt(item.getAttribute('data-slide-h'));
    var v = parseInt(item.getAttribute('data-slide-v'));
    var theme = item.getAttribute('data-theme');
    var highlightTheme = item.getAttribute('data-highlight-theme');
    var transition = item.getAttribute('data-transition');

    if (!isNaN(h) && !isNaN(v)) {
      deck.slide(h, v);
    }

    if (theme) {
      changeStylesheet('theme', theme);
    }

    if (highlightTheme) {
      changeStylesheet('highlight-theme', highlightTheme);
    }

    if (transition) {
      deck.configure({ transition: transition });
    }

    var link = select('a', item);
    if (link) {
      if (
        force ||
        !options.sticky ||
        (options.autoOpen && link.href.startsWith('#')) ||
        link.href.startsWith(
          window.location.origin + window.location.pathname + '#'
        )
      ) {
        link.click();
      }
    }

    closeMenu();
  }

  function clicked(event) {
    if (event.target.nodeName !== 'A') {
      event.preventDefault();
    }
    openItem(event.currentTarget);
  }

  function highlightCurrentSlide() {
    var state = deck.getState();
    selectAll('li.slide-menu-item, li.slide-menu-item-vertical').forEach(
      function (item) {
        item.classList.remove('past');
        item.classList.remove('active');
        item.classList.remove('future');

        var h = parseInt(item.getAttribute('data-slide-h'));
        var v = parseInt(item.getAttribute('data-slide-v'));
        if (h < state.indexh || (h === state.indexh && v < state.indexv)) {
          item.classList.add('past');
        } else if (h === state.indexh && v === state.indexv) {
          item.classList.add('active');
        } else {
          item.classList.add('future');
        }
      }
    );
  }

  function matchRevealStyle() {
    var revealStyle = window.getComputedStyle(select('.reveal'));
    var element = select('.slide-menu');
    element.style.fontFamily = revealStyle.fontFamily;
    //XXX could adjust the complete menu style to match the theme, ie colors, etc
  }

  var buttons = 0;
  function initMenu() {
    if (!initialised) {
      var parent = select('.reveal').parentElement;
      var top = create('div', { class: 'slide-menu-wrapper' });
      parent.appendChild(top);
      var panels = create('nav', {
        class: 'slide-menu slide-menu--' + options.side
      });
      if (typeof options.width === 'string') {
        if (
          ['normal', 'wide', 'third', 'half', 'full'].indexOf(options.width) !=
          -1
        ) {
          panels.classList.add('slide-menu--' + options.width);
        } else {
          panels.classList.add('slide-menu--custom');
          panels.style.width = options.width;
        }
      }
      top.appendChild(panels);
      matchRevealStyle();
      var overlay = create('div', { class: 'slide-menu-overlay' });
      top.appendChild(overlay);
      overlay.onclick = function () {
        closeMenu(null, true);
      };

      var toolbar = create('ol', { class: 'slide-menu-toolbar' });
      select('.slide-menu').appendChild(toolbar);

      function addToolbarButton(title, ref, icon, style, fn, active) {
        var attrs = {
          'data-button': '' + buttons++,
          class:
            'toolbar-panel-button' + (active ? ' active-toolbar-button' : '')
        };
        if (ref) {
          attrs['data-panel'] = ref;
        }
        var button = create('li', attrs);

        if (icon.startsWith('fa-')) {
          button.appendChild(create('i', { class: style + ' ' + icon }));
        } else {
          button.innerHTML = icon + '</i>';
        }
        button.appendChild(create('br'), select('i', button));
        button.appendChild(
          create('span', { class: 'slide-menu-toolbar-label' }, title),
          select('i', button)
        );
        button.onclick = fn;
        toolbar.appendChild(button);
        return button;
      }

      addToolbarButton('Slides', 'Slides', 'fa-images', 'fas', openPanel, true);

      if (options.custom) {
        options.custom.forEach(function (element, index, array) {
          addToolbarButton(
            element.title,
            'Custom' + index,
            element.icon,
            null,
            openPanel
          );
        });
      }

      if (options.themes) {
        addToolbarButton('Themes', 'Themes', 'fa-adjust', 'fas', openPanel);
      }
      if (options.transitions) {
        addToolbarButton(
          'Transitions',
          'Transitions',
          'fa-sticky-note',
          'fas',
          openPanel
        );
      }
      var button = create('li', {
        id: 'close',
        class: 'toolbar-panel-button'
      });
      button.appendChild(create('i', { class: 'fas fa-times' }));
      button.appendChild(create('br'));
      button.appendChild(
        create('span', { class: 'slide-menu-toolbar-label' }, 'Close')
      );
      button.onclick = function () {
        closeMenu(null, true);
      };
      toolbar.appendChild(button);

      //
      // Slide links
      //
      function generateItem(type, section, i, h, v) {
        var link = '/#/' + h;
        if (typeof v === 'number' && !isNaN(v)) link += '/' + v;

        function text(selector, parent) {
          if (selector === '') return null;
          var el = parent ? select(selector, section) : select(selector);
          if (el) return el.textContent;
          return null;
        }
        var title =
          section.getAttribute('data-menu-title') ||
          text('.menu-title', section) ||
          text(options.titleSelector, section);

        if (!title && options.useTextContentForMissingTitles) {
          // attempt to figure out a title based on the text in the slide
          title = section.textContent.trim();
          if (title) {
            title =
              title
                .split('\n')
                .map(function (t) {
                  return t.trim();
                })
                .join(' ')
                .trim()
                .replace(/^(.{16}[^\s]*).*/, '$1') // limit to 16 chars plus any consecutive non-whitespace chars (to avoid breaking words)
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;') + '...';
          }
        }

        if (!title) {
          if (options.hideMissingTitles) return '';
          type += ' no-title';
          title = 'Slide ' + (i + 1);
        }

        var item = create('li', {
          class: type,
          'data-item': i,
          'data-slide-h': h,
          'data-slide-v': v === undefined ? 0 : v
        });

        if (options.markers) {
          item.appendChild(
            create('i', { class: 'fas fa-check-circle fa-fw past' })
          );
          item.appendChild(
            create('i', {
              class: 'fas fa-arrow-alt-circle-right fa-fw active'
            })
          );
          item.appendChild(
            create('i', { class: 'far fa-circle fa-fw future' })
          );
        }

        if (options.numbers) {
          // Number formatting taken from reveal.js
          var value = [];
          var format = 'h.v';

          // Check if a custom number format is available
          if (typeof options.numbers === 'string') {
            format = options.numbers;
          } else if (typeof config.slideNumber === 'string') {
            // Take user defined number format for slides
            format = config.slideNumber;
          }

          switch (format) {
            case 'c':
              value.push(i + 1);
              break;
            case 'c/t':
              value.push(i + 1, '/', deck.getTotalSlides());
              break;
            case 'h/v':
              value.push(h + 1);
              if (typeof v === 'number' && !isNaN(v)) value.push('/', v + 1);
              break;
            default:
              value.push(h + 1);
              if (typeof v === 'number' && !isNaN(v)) value.push('.', v + 1);
          }

          item.appendChild(
            create(
              'span',
              { class: 'slide-menu-item-number' },
              value.join('') + '. '
            )
          );
        }

        item.appendChild(
          create('span', { class: 'slide-menu-item-title' }, title)
        );

        return item;
      }

      function createSlideMenu() {
        if (
          !document.querySelector(
            'section[data-markdown]:not([data-markdown-parsed])'
          )
        ) {
          var panel = create('div', {
            'data-panel': 'Slides',
            class: 'slide-menu-panel active-menu-panel'
          });
          panel.appendChild(create('ul', { class: 'slide-menu-items' }));
          panels.appendChild(panel);
          var items = select(
            '.slide-menu-panel[data-panel="Slides"] > .slide-menu-items'
          );
          var slideCount = 0;
          selectAll('.slides > section').forEach(function (section, h) {
            var subsections = selectAll('section', section);
            if (subsections.length > 0) {
              subsections.forEach(function (subsection, v) {
                var type =
                  v === 0 ? 'slide-menu-item' : 'slide-menu-item-vertical';
                var item = generateItem(type, subsection, slideCount, h, v);
                if (item) {
                  items.appendChild(item);
                }
                slideCount++;
              });
            } else {
              var item = generateItem(
                'slide-menu-item',
                section,
                slideCount,
                h
              );
              if (item) {
                items.appendChild(item);
              }
              slideCount++;
            }
          });
          selectAll('.slide-menu-item, .slide-menu-item-vertical').forEach(
            function (i) {
              i.onclick = clicked;
            }
          );
          highlightCurrentSlide();
        } else {
          // wait for markdown to be loaded and parsed
          setTimeout(createSlideMenu, 100);
        }
      }

      createSlideMenu();
      deck.addEventListener('slidechanged', highlightCurrentSlide);

      //
      // Custom menu panels
      //
      if (options.custom) {
        function xhrSuccess() {
          if (this.status >= 200 && this.status < 300) {
            this.panel.innerHTML = this.responseText;
            enableCustomLinks(this.panel);
          } else {
            showErrorMsg(this);
          }
        }
        function xhrError() {
          showErrorMsg(this);
        }
        function loadCustomPanelContent(panel, sURL) {
          var oReq = new XMLHttpRequest();
          oReq.panel = panel;
          oReq.arguments = Array.prototype.slice.call(arguments, 2);
          oReq.onload = xhrSuccess;
          oReq.onerror = xhrError;
          oReq.open('get', sURL, true);
          oReq.send(null);
        }
        function enableCustomLinks(panel) {
          selectAll('ul.slide-menu-items li.slide-menu-item', panel).forEach(
            function (item, i) {
              item.setAttribute('data-item', i + 1);
              item.onclick = clicked;
              item.addEventListener('mouseenter', handleMouseHighlight);
            }
          );
        }

        function showErrorMsg(response) {
          var msg =
            '<p>ERROR: The attempt to fetch ' +
            response.responseURL +
            ' failed with HTTP status ' +
            response.status +
            ' (' +
            response.statusText +
            ').</p>' +
            '<p>Remember that you need to serve the presentation HTML from a HTTP server.</p>';
          response.panel.innerHTML = msg;
        }

        options.custom.forEach(function (element, index, array) {
          var panel = create('div', {
            'data-panel': 'Custom' + index,
            class: 'slide-menu-panel slide-menu-custom-panel'
          });
          if (element.content) {
            panel.innerHTML = element.content;
            enableCustomLinks(panel);
          } else if (element.src) {
            loadCustomPanelContent(panel, element.src);
          }
          panels.appendChild(panel);
        });
      }

      //
      // Themes
      //
      if (options.themes) {
        var panel = create('div', {
          class: 'slide-menu-panel',
          'data-panel': 'Themes'
        });
        panels.appendChild(panel);
        var menu = create('ul', { class: 'slide-menu-items' });
        panel.appendChild(menu);
        options.themes.forEach(function (t, i) {
          var attrs = {
            class: 'slide-menu-item',
            'data-item': '' + (i + 1)
          };
          if (t.theme) {
            attrs['data-theme'] = t.theme;
          }
          if (t.highlightTheme) {
            attrs['data-highlight-theme'] = t.highlightTheme;
          }
          var item = create('li', attrs, t.name);
          menu.appendChild(item);
          item.onclick = clicked;
        });
      }

      //
      // Transitions
      //
      if (options.transitions) {
        var panel = create('div', {
          class: 'slide-menu-panel',
          'data-panel': 'Transitions'
        });
        panels.appendChild(panel);
        var menu = create('ul', { class: 'slide-menu-items' });
        panel.appendChild(menu);
        options.transitions.forEach(function (name, i) {
          var item = create(
            'li',
            {
              class: 'slide-menu-item',
              'data-transition': name.toLowerCase(),
              'data-item': '' + (i + 1)
            },
            name
          );
          menu.appendChild(item);
          item.onclick = clicked;
        });
      }

      //
      // Open menu options
      //
      if (options.openButton) {
        // add menu button
        var div = create('div', { class: 'slide-menu-button' });
        var link = create('a', { href: '#' });
        link.appendChild(create('i', { class: 'fas fa-bars' }));
        div.appendChild(link);
        select('.reveal').appendChild(div);
        div.onclick = openMenu;
      }

      if (options.openSlideNumber) {
        var slideNumber = select('div.slide-number');
        slideNumber.onclick = openMenu;
      }

      //
      // Handle mouse overs
      //
      selectAll('.slide-menu-panel .slide-menu-items li').forEach(function (
        item
      ) {
        item.addEventListener('mouseenter', handleMouseHighlight);
      });

      function handleMouseHighlight(event) {
        if (mouseSelectionEnabled) {
          selectAll('.active-menu-panel .slide-menu-items li.selected').forEach(
            function (i) {
              i.classList.remove('selected');
            }
          );
          event.currentTarget.classList.add('selected');
        }
      }
    }

    if (options.keyboard) {
      //XXX add keyboard option for custom key codes, etc.

      document.addEventListener('keydown', onDocumentKeyDown, false);

      // handle key presses within speaker notes
      window.addEventListener('message', function (event) {
        var data;
        try {
          data = JSON.parse(event.data);
        } catch (e) {}
        if (data && data.method === 'triggerKey') {
          onDocumentKeyDown({
            keyCode: data.args[0],
            stopImmediatePropagation: function () {}
          });
        }
      });

      // Prevent reveal from processing keyboard events when the menu is open
      if (
        config.keyboardCondition &&
        typeof config.keyboardCondition === 'function'
      ) {
        // combine user defined keyboard condition with the menu's own condition
        var userCondition = config.keyboardCondition;
        config.keyboardCondition = function (event) {
          return userCondition(event) && (!isOpen() || event.keyCode == 77);
        };
      } else {
        config.keyboardCondition = function (event) {
          return !isOpen() || event.keyCode == 77;
        };
      }

      deck.addKeyBinding(
        { keyCode: 77, key: 'M', description: 'Toggle menu' },
        toggleMenu
      );
    }

    if (options.openOnInit) {
      openMenu();
    }

    initialised = true;
  }

  /**
   * Extend object a with the properties of object b.
   * If there's a conflict, object b takes precedence.
   */
  function extend(a, b) {
    for (var i in b) {
      a[i] = b[i];
    }
  }

  /**
   * Dispatches an event of the specified type from the
   * reveal DOM element.
   */
  function dispatchEvent(type, args) {
    var event = document.createEvent('HTMLEvents', 1, 2);
    event.initEvent(type, true, true);
    extend(event, args);
    document.querySelector('.reveal').dispatchEvent(event);

    // If we're in an iframe, post each reveal.js event to the
    // parent window. Used by the notes plugin
    if (config.postMessageEvents && window.parent !== window.self) {
      window.parent.postMessage(
        JSON.stringify({
          namespace: 'reveal',
          eventName: type,
          state: deck.getState()
        }),
        '*'
      );
    }
  }

  function select(selector, el) {
    if (!el) {
      el = document;
    }
    return el.querySelector(selector);
  }

  function selectAll(selector, el) {
    if (!el) {
      el = document;
    }
    return Array.prototype.slice.call(el.querySelectorAll(selector));
  }

  function create(tagName, attrs, content) {
    var el = document.createElement(tagName);
    if (attrs) {
      Object.getOwnPropertyNames(attrs).forEach(function (n) {
        el.setAttribute(n, attrs[n]);
      });
    }
    if (content) el.innerHTML = content;
    return el;
  }

  function changeStylesheet(id, href) {
    // take note of the previous theme and remove it, then create a new stylesheet reference and insert it
    // this is required to force a load event so we can change the menu style to match the new style
    var stylesheet = select('link#' + id);
    var parent = stylesheet.parentElement;
    var sibling = stylesheet.nextElementSibling;
    stylesheet.remove();

    var newStylesheet = stylesheet.cloneNode();
    newStylesheet.setAttribute('href', href);
    newStylesheet.onload = function () {
      matchRevealStyle();
    };
    parent.insertBefore(newStylesheet, sibling);
  }

  // modified from math plugin
  function loadResource(url, type, callback) {
    var head = document.querySelector('head');
    var resource;

    if (type === 'script') {
      resource = document.createElement('script');
      resource.type = 'text/javascript';
      resource.src = url;
    } else if (type === 'stylesheet') {
      resource = document.createElement('link');
      resource.rel = 'stylesheet';
      resource.href = url;
    }

    // Wrapper for callback to make sure it only fires once
    var finish = function () {
      if (typeof callback === 'function') {
        callback.call();
        callback = null;
      }
    };

    resource.onload = finish;

    // IE
    resource.onreadystatechange = function () {
      if (this.readyState === 'loaded') {
        finish();
      }
    };

    // Normal browsers
    head.appendChild(resource);
  }

  function loadPlugin() {
    // does not support IE8 or below
    var supported = !ieVersion || ieVersion >= 9;

    // do not load the menu in the upcoming slide panel in the speaker notes
    if (
      deck.isSpeakerNotes() &&
      window.location.search.endsWith('controls=false')
    ) {
      supported = false;
    }

    if (supported) {
      if (!options.delayInit) initMenu();
      dispatchEvent('menu-ready');
    }
  }

  return {
    id: 'menu',
    init: reveal => {
      deck = reveal;
      config = deck.getConfig();
      initOptions(config);
      loadResource(options.path + 'menu.css', 'stylesheet', function () {
        if (options.loadIcons === undefined || options.loadIcons) {
          loadResource(
            options.path + 'font-awesome/css/all.css',
            'stylesheet',
            loadPlugin
          );
        } else {
          loadPlugin();
        }
      });
    },

    toggle: toggleMenu,
    openMenu: openMenu,
    closeMenu: closeMenu,
    openPanel: openPanel,
    isOpen: isOpen,
    initialiseMenu: initMenu,
    isMenuInitialised: function () {
      return initialised;
    }
  };
};

// polyfill
if (!String.prototype.startsWith) {
  String.prototype.startsWith = function (searchString, position) {
    return this.substr(position || 0, searchString.length) === searchString;
  };
}
if (!String.prototype.endsWith) {
  String.prototype.endsWith = function (search, this_len) {
    if (this_len === undefined || this_len > this.length) {
      this_len = this.length;
    }
    return this.substring(this_len - search.length, this_len) === search;
  };
}

export default Plugin;
