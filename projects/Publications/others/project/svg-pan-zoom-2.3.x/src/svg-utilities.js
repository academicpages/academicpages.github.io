var Utils = require('./utilities');

module.exports = {
  svgNS:  'http://www.w3.org/2000/svg'
, xmlNS:  'http://www.w3.org/XML/1998/namespace'
, xmlnsNS:  'http://www.w3.org/2000/xmlns/'
, xlinkNS:  'http://www.w3.org/1999/xlink'
, evNS:  'http://www.w3.org/2001/xml-events'

  /**
   * Get svg dimensions: width and height
   *
   * @param  {object} svg
   * @return {object}     {width: 0, height: 0}
   */
, getBoundingClientRectNormalized: function(svg) {
    // Firefox returns values in the SVG coordinate system for getBoundingClientRect(),
    // whereas other browsers return values in the HTML page coordinate system.
    // This harmonizes the behavior to use the HTML page coordinate system.
    if (this._browser === 'firefox') {
      var svgComputedStyle = window.getComputedStyle(svg, null);
      var selectedSvgStyleAttributeNames = ['width', 'height', 'left', 'top', 'transform', 'position'];
      var svgComputedStyleString = '';
      selectedSvgStyleAttributeNames.forEach(function(styleAttributeName) {
        var styleAttributeValue = svgComputedStyle[styleAttributeName];
        if (!!styleAttributeValue) {
          svgComputedStyleString += ' ' + styleAttributeName + ': ' + styleAttributeValue + ';';
        }
      });

      var parent = svg.parentNode;
      parent.removeChild(svg);

      var testDiv = document.createElement('div');
      testDiv.setAttribute('style', svgComputedStyleString);
      parent.appendChild(testDiv);
      var testDivBoundingClientRect = testDiv.getBoundingClientRect();

      parent.removeChild(testDiv);
      parent.appendChild(svg);

      return testDivBoundingClientRect;
    } else if (!!svg.getBoundingClientRect()) {
      return svg.getBoundingClientRect();
    } else {
      throw new Error('Cannot get BoundingClientRect for SVG.');
    }
  }

  /**
   * Gets g element with class of "viewport" or creates it if it doesn't exist
   * @param  {object} svg
   * @return {object}     g element
   */
, getOrCreateViewport: function(svg) {
    var viewport = svg.querySelector('g.viewport')

    // If no g element with class 'viewport' exists, create one
    if (!viewport) {
      var viewportId = 'viewport-' + new Date().toISOString().replace(/\D/g, '');
      viewport = document.createElementNS(this.svgNS, 'g');
      viewport.setAttribute('id', viewportId);
      viewport.setAttribute('class', 'viewport');

      // Internet Explorer (all versions?) can't use childNodes, but other browsers prefer (require?) using childNodes
      var svgChildren = svg.childNodes || svg.children;
      if (!!svgChildren && svgChildren.length > 0) {
        do {
          viewport.appendChild(svgChildren[0]);
        } while (svgChildren.length > 0);
      }
      svg.appendChild(viewport);
    }

    return viewport
  }

  , setupSvgAttributes: function(svg) {
    // Setting default attributes

    svg.setAttribute('xmlns', this.svgNS);
    svg.setAttributeNS(this.xmlnsNS, 'xmlns:xlink', this.xlinkNS);
    svg.setAttributeNS(this.xmlnsNS, 'xmlns:ev', this.evNS);

    // Needed for Internet Explorer, otherwise the viewport overflows
    if (svg.parentNode !== null) {
      var style = svg.getAttribute('style') || '';
      if (style.toLowerCase().indexOf('overflow') === -1) {
        svg.setAttribute('style', 'overflow: hidden; ' + style);
      }
    }
  }

/**
 * How long Internet Explorer takes to finish updating its display.
 * (ms)
 *
 * @return
 */
, internetExplorerRedisplayInterval: 300

/**
 * Forces the browser to redisplay all SVG elements that rely on an
 * element defined in a 'defs' section. It works globally, for every
 * available defs element on the page.
 * The throttling is intentionally global.
 *
 * This is only needed for IE. It is as a hack to make markers (and 'use' elements?)
 * visible after pan/zoom when there are multiple SVGs on the page.
 * See bug report: https://connect.microsoft.com/IE/feedback/details/781964/
 * also see svg-pan-zoom issue: https://github.com/ariutta/svg-pan-zoom/issues/62
 */
, refreshDefsGlobal: Utils.throttle(function() {
    var allDefs = document.querySelectorAll('defs');
    var allDefsCount = allDefs.length;
    for (var i = 0; i < allDefsCount; i++) {
      var thisDefs = allDefs[i];
      thisDefs.parentNode.insertBefore(thisDefs, thisDefs);
    }
  }, this.internetExplorerRedisplayInterval)

  /**
   * Sets the current transform matrix of an element
   * @param {object} element SVG Element
   * @param {object} matrix  CTM
   */
, setCTM: function(element, matrix, defs) {
    var that = this;
    // this throttling causes problems when trying to synchronize the zoom between two different SVGs.
    //Utils.throttle(function() {
      var s = 'matrix(' + matrix.a + ',' + matrix.b + ',' + matrix.c + ',' + matrix.d + ',' + matrix.e + ',' + matrix.f + ')';
      element.setAttributeNS(null, 'transform', s);

      // IE has a bug that makes markers disappear on zoom (when the matrix "a" and/or "d" elements change)
      // see http://stackoverflow.com/questions/17654578/svg-marker-does-not-work-in-ie9-10
      // and http://srndolha.wordpress.com/2013/11/25/svg-line-markers-may-disappear-in-internet-explorer-11/
      if (that._browser === 'ie' && !!defs) {
        // this refresh is intended for redisplaying the SVG during zooming
        defs.parentNode.insertBefore(defs, defs);
        // this refresh is intended for redisplaying the other SVGs on a page when panning a given SVG
        // it is also needed for the given SVG itself, on zoomEnd, if the SVG contains any markers that
        // are located under any other element(s).
        window.setTimeout(function() {
          that.refreshDefsGlobal();
        }, that.internetExplorerRedisplayInterval);
      }
    //}, 1000/that.refreshRate)();
  }

  /**
   * Time-based cache for svg.getScreenCTM().
   * Needed because getScreenCTM() is very slow on Firefox (FF 28 at time of writing).
   * The cache expires every 300ms... this is a pretty safe time because it's only called
   * when we're zooming, when the screenCTM is unlikely/impossible to change.
   *
   * @param {object} svg SVG Element
   * @return {[type]} [description]
   */
, getScreenCTMCached: (function() {
    var svgs = {};
    return function(svg) {
      var cur = Date.now();
      if (svgs.hasOwnProperty(svg)) {
        var cached = svgs[svg];
        if (cur - cached.time > 300) {
          // Cache expired
          cached.time = cur;
          cached.ctm = svg.getScreenCTM();
        }
        return cached.ctm;
      } else {
        var ctm = svg.getScreenCTM();
        svgs[svg] = {time: cur, ctm: ctm};
        return ctm;
      }
    };
  })()

  /**
   * Get an SVGPoint of the mouse co-ordinates of the event, relative to the SVG element
   *
   * @param  {object} svg SVG Element
   * @param  {object} evt Event
   * @return {object}     point
   */
, getRelativeMousePoint: function(svg, evt) {
    Utils.mouseAndTouchNormalize(evt, svg)

    var point = svg.createSVGPoint()

    point.x = evt.clientX
    point.y = evt.clientY

    return point.matrixTransform(this.getScreenCTMCached(svg).inverse())
  }

  /**
   * Instantiate an SVGPoint object with given event coordinates
   *
   * @param {object} evt Event
   */
, getEventPoint: function(evt) {
    var svg = (evt.target.tagName === 'svg' || evt.target.tagName === 'SVG') ? evt.target : evt.target.ownerSVGElement || evt.target.correspondingElement.ownerSVGElement
      , point = svg.createSVGPoint()

    Utils.mouseAndTouchNormalize(evt, svg)

    point.x = evt.clientX
    point.y = evt.clientY

    return point
  }

  /**
   * Get SVG center point
   *
   * @param  {object} svg SVG Element
   * @return {object}     SVG Point
   */
, getSvgCenterPoint: function(svg) {
    var boundingClientRect = this.getBoundingClientRectNormalized(svg)
      , width = boundingClientRect.width
      , height = boundingClientRect.height
      , point = svg.createSVGPoint()

    point.x = width / 2
    point.y = height / 2

    return point
  }
}
