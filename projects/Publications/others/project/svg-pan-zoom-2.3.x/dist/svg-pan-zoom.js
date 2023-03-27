(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);throw new Error("Cannot find module '"+o+"'")}var f=n[o]={exports:{}};t[o][0].call(f.exports,function(e){var n=t[o][1][e];return s(n?n:e)},f,f.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
module.exports = {
  enable: function(instance) {

    /*
    // TODO should we create a new SVG or insert the control icons into the existing SVG?
    // The code below does not work entirely correctly, but it's a start if we want to
    // create a new SVG
    // create svg for control icons
    var controlIconsSvgId = 'svg-pan-zoom-control-icons-' + new Date().toISOString().replace(/\D/g, '');
    var controlIconsSvg = document.createElementNS(instance.svgNS, 'svg');
    controlIconsSvg.setAttributeNS(instance.xmlnsNS, 'xmlns', instance.svgNS);
    controlIconsSvg.setAttributeNS(instance.xmlnsNS, 'xmlns:xlink', instance.xlinkNS);
    controlIconsSvg.setAttributeNS(instance.xmlnsNS, 'xmlns:ev', instance.evNS);
    controlIconsSvg.setAttribute('id', controlIconsSvgId);
    controlIconsSvg.setAttribute('version', '1.1');
    controlIconsSvg.setAttribute('baseProfile', 'full');
    controlIconsSvg.setAttribute('preserveAspectRatio', 'xMidYMid');
    controlIconsSvg.setAttribute('style', 'left:' + ( instance.dimensions.right - 70 ) + '; top:' + ( instance.dimensions.bottom - 76 ) + '; position: absolute;');
    //controlIconsSvg.setAttribute('width', width);
    //controlIconsSvg.setAttribute('height', height);
    //controlIconsSvg.setAttribute('style', 'background-color:' + backgroundColor + '; ');
    document.body.appendChild(controlIconsSvg);

    // Create defs
    var defs = document.createElementNS(instance.svgNS, 'defs');
    controlIconsSvg.appendChild(defs);
    //*/

    // Select (and create if necessary) defs
    var defs = instance.svg.querySelector('defs')
    if (!defs) {
      defs = document.createElementNS(instance.svgNS, 'defs')
      instance.svg.appendChild(defs)
    }

    // Create style element
    var style = document.createElementNS(instance.svgNS, 'style')
    style.setAttribute('type', 'text/css')
    style.textContent = '.svg-pan-zoom-control { cursor: pointer; fill: black; fill-opacity: 0.333; } .svg-pan-zoom-control:hover { fill-opacity: 0.8; } .svg-pan-zoom-control-background { fill: white; fill-opacity: 0.5; } .svg-pan-zoom-control-background { fill-opacity: 0.8; }'
    defs.appendChild(style)


    // Zoom Group
    var zoomGroup = document.createElementNS(instance.svgNS, 'g');
    zoomGroup.setAttribute('id', 'svg-pan-zoom-controls');
    zoomGroup.setAttribute('transform', 'translate(' + ( instance.width - 70 ) + ' ' + ( instance.height - 76 ) + ') scale(0.75)');
    zoomGroup.setAttribute('class', 'svg-pan-zoom-control');

    // Control elements
    zoomGroup.appendChild(this._createZoomIn(instance))
    zoomGroup.appendChild(this._createZoomReset(instance))
    zoomGroup.appendChild(this._createZoomOut(instance))

    // Finally append created element
    instance.svg.appendChild(zoomGroup)

    // Cache control instance
    instance.controlIcons = zoomGroup
  }

, _createZoomIn: function(instance) {
    var zoomIn = document.createElementNS(instance.svgNS, 'g');
    zoomIn.setAttribute('id', 'svg-pan-zoom-zoom-in');
    zoomIn.setAttribute('transform', 'translate(30.5 5) scale(0.015)');
    zoomIn.setAttribute('class', 'svg-pan-zoom-control');
    zoomIn.addEventListener('click', function() {instance.getPublicInstance().zoomIn()}, false)
    zoomIn.addEventListener('touchstart', function() {instance.getPublicInstance().zoomIn()}, false)

    var zoomInBackground = document.createElementNS(instance.svgNS, 'rect'); // TODO change these background space fillers to rounded rectangles so they look prettier
    zoomInBackground.setAttribute('x', '0');
    zoomInBackground.setAttribute('y', '0');
    zoomInBackground.setAttribute('width', '1500'); // larger than expected because the whole group is transformed to scale down
    zoomInBackground.setAttribute('height', '1400');
    zoomInBackground.setAttribute('class', 'svg-pan-zoom-control-background');
    zoomIn.appendChild(zoomInBackground);

    var zoomInShape = document.createElementNS(instance.svgNS, 'path');
    zoomInShape.setAttribute('d', 'M1280 576v128q0 26 -19 45t-45 19h-320v320q0 26 -19 45t-45 19h-128q-26 0 -45 -19t-19 -45v-320h-320q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h320v-320q0 -26 19 -45t45 -19h128q26 0 45 19t19 45v320h320q26 0 45 19t19 45zM1536 1120v-960 q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5t84.5 -203.5z');
    zoomInShape.setAttribute('class', 'svg-pan-zoom-control-element');
    zoomIn.appendChild(zoomInShape);

    return zoomIn
  }

, _createZoomReset: function(instance){
    // reset
    var resetPanZoomControl = document.createElementNS(instance.svgNS, 'g');
    resetPanZoomControl.setAttribute('id', 'svg-pan-zoom-reset-pan-zoom');
    resetPanZoomControl.setAttribute('transform', 'translate(5 35) scale(0.4)');
    resetPanZoomControl.setAttribute('class', 'svg-pan-zoom-control');
    resetPanZoomControl.addEventListener('click', function() {instance.getPublicInstance().resetZoom()}, false);
    resetPanZoomControl.addEventListener('touchstart', function() {instance.getPublicInstance().resetZoom()}, false);

    var resetPanZoomControlBackground = document.createElementNS(instance.svgNS, 'rect'); // TODO change these background space fillers to rounded rectangles so they look prettier
    resetPanZoomControlBackground.setAttribute('x', '2');
    resetPanZoomControlBackground.setAttribute('y', '2');
    resetPanZoomControlBackground.setAttribute('width', '182'); // larger than expected because the whole group is transformed to scale down
    resetPanZoomControlBackground.setAttribute('height', '58');
    resetPanZoomControlBackground.setAttribute('class', 'svg-pan-zoom-control-background');
    resetPanZoomControl.appendChild(resetPanZoomControlBackground);

    var resetPanZoomControlShape1 = document.createElementNS(instance.svgNS, 'path');
    resetPanZoomControlShape1.setAttribute('d', 'M33.051,20.632c-0.742-0.406-1.854-0.609-3.338-0.609h-7.969v9.281h7.769c1.543,0,2.701-0.188,3.473-0.562c1.365-0.656,2.048-1.953,2.048-3.891C35.032,22.757,34.372,21.351,33.051,20.632z');
    resetPanZoomControlShape1.setAttribute('class', 'svg-pan-zoom-control-element');
    resetPanZoomControl.appendChild(resetPanZoomControlShape1);

    var resetPanZoomControlShape2 = document.createElementNS(instance.svgNS, 'path');
    resetPanZoomControlShape2.setAttribute('d', 'M170.231,0.5H15.847C7.102,0.5,0.5,5.708,0.5,11.84v38.861C0.5,56.833,7.102,61.5,15.847,61.5h154.384c8.745,0,15.269-4.667,15.269-10.798V11.84C185.5,5.708,178.976,0.5,170.231,0.5z M42.837,48.569h-7.969c-0.219-0.766-0.375-1.383-0.469-1.852c-0.188-0.969-0.289-1.961-0.305-2.977l-0.047-3.211c-0.03-2.203-0.41-3.672-1.142-4.406c-0.732-0.734-2.103-1.102-4.113-1.102h-7.05v13.547h-7.055V14.022h16.524c2.361,0.047,4.178,0.344,5.45,0.891c1.272,0.547,2.351,1.352,3.234,2.414c0.731,0.875,1.31,1.844,1.737,2.906s0.64,2.273,0.64,3.633c0,1.641-0.414,3.254-1.242,4.84s-2.195,2.707-4.102,3.363c1.594,0.641,2.723,1.551,3.387,2.73s0.996,2.98,0.996,5.402v2.32c0,1.578,0.063,2.648,0.19,3.211c0.19,0.891,0.635,1.547,1.333,1.969V48.569z M75.579,48.569h-26.18V14.022h25.336v6.117H56.454v7.336h16.781v6H56.454v8.883h19.125V48.569z M104.497,46.331c-2.44,2.086-5.887,3.129-10.34,3.129c-4.548,0-8.125-1.027-10.731-3.082s-3.909-4.879-3.909-8.473h6.891c0.224,1.578,0.662,2.758,1.316,3.539c1.196,1.422,3.246,2.133,6.15,2.133c1.739,0,3.151-0.188,4.236-0.562c2.058-0.719,3.087-2.055,3.087-4.008c0-1.141-0.504-2.023-1.512-2.648c-1.008-0.609-2.607-1.148-4.796-1.617l-3.74-0.82c-3.676-0.812-6.201-1.695-7.576-2.648c-2.328-1.594-3.492-4.086-3.492-7.477c0-3.094,1.139-5.664,3.417-7.711s5.623-3.07,10.036-3.07c3.685,0,6.829,0.965,9.431,2.895c2.602,1.93,3.966,4.73,4.093,8.402h-6.938c-0.128-2.078-1.057-3.555-2.787-4.43c-1.154-0.578-2.587-0.867-4.301-0.867c-1.907,0-3.428,0.375-4.565,1.125c-1.138,0.75-1.706,1.797-1.706,3.141c0,1.234,0.561,2.156,1.682,2.766c0.721,0.406,2.25,0.883,4.589,1.43l6.063,1.43c2.657,0.625,4.648,1.461,5.975,2.508c2.059,1.625,3.089,3.977,3.089,7.055C108.157,41.624,106.937,44.245,104.497,46.331z M139.61,48.569h-26.18V14.022h25.336v6.117h-18.281v7.336h16.781v6h-16.781v8.883h19.125V48.569z M170.337,20.14h-10.336v28.43h-7.266V20.14h-10.383v-6.117h27.984V20.14z');
    resetPanZoomControlShape2.setAttribute('class', 'svg-pan-zoom-control-element');
    resetPanZoomControl.appendChild(resetPanZoomControlShape2);

    return resetPanZoomControl
  }

, _createZoomOut: function(instance){
    // zoom out
    var zoomOut = document.createElementNS(instance.svgNS, 'g');
    zoomOut.setAttribute('id', 'svg-pan-zoom-zoom-out');
    zoomOut.setAttribute('transform', 'translate(30.5 70) scale(0.015)');
    zoomOut.setAttribute('class', 'svg-pan-zoom-control');
    zoomOut.addEventListener('click', function() {instance.getPublicInstance().zoomOut()}, false);
    zoomOut.addEventListener('touchstart', function() {instance.getPublicInstance().zoomOut()}, false);

    var zoomOutBackground = document.createElementNS(instance.svgNS, 'rect'); // TODO change these background space fillers to rounded rectangles so they look prettier
    zoomOutBackground.setAttribute('x', '0');
    zoomOutBackground.setAttribute('y', '0');
    zoomOutBackground.setAttribute('width', '1500'); // larger than expected because the whole group is transformed to scale down
    zoomOutBackground.setAttribute('height', '1400');
    zoomOutBackground.setAttribute('class', 'svg-pan-zoom-control-background');
    zoomOut.appendChild(zoomOutBackground);

    var zoomOutShape = document.createElementNS(instance.svgNS, 'path');
    zoomOutShape.setAttribute('d', 'M1280 576v128q0 26 -19 45t-45 19h-896q-26 0 -45 -19t-19 -45v-128q0 -26 19 -45t45 -19h896q26 0 45 19t19 45zM1536 1120v-960q0 -119 -84.5 -203.5t-203.5 -84.5h-960q-119 0 -203.5 84.5t-84.5 203.5v960q0 119 84.5 203.5t203.5 84.5h960q119 0 203.5 -84.5 t84.5 -203.5z');
    zoomOutShape.setAttribute('class', 'svg-pan-zoom-control-element');
    zoomOut.appendChild(zoomOutShape);

    return zoomOut
  }

, disable: function(instance) {
    if (instance.controlIcons) {
      instance.controlIcons.parentNode.removeChild(instance.controlIcons)
      instance.controlIcons = null
    }
  }
}

},{}],2:[function(require,module,exports){
// Cross-browser wheel event, from: https://developer.mozilla.org/en-US/docs/Web/Reference/Events/wheel
if (!window.hasOwnProperty('addWheelListener')) {
  // creates a global "addWheelListener" method
  // example: addWheelListener( elem, function( e ) { console.log( e.deltaY ); e.preventDefault(); } );
  (function(window,document) {

    var prefix = "", _addEventListener, onwheel, support;

    // detect event model
    if ( window.addEventListener ) {
      _addEventListener = "addEventListener";
    } else {
      _addEventListener = "attachEvent";
      prefix = "on";
    }

    // detect available wheel event
    support = "onwheel" in document.createElement("div") ? "wheel" : // Modern browsers support "wheel"
      document.onmousewheel !== undefined ? "mousewheel" : // Webkit and IE support at least "mousewheel"
      "DOMMouseScroll"; // let's assume that remaining browsers are older Firefox

        window.addWheelListener = function( elem, callback, useCapture ) {
      _addWheelListener( elem, support, callback, useCapture );

      // handle MozMousePixelScroll in older Firefox
      if( support == "DOMMouseScroll" ) {
        _addWheelListener( elem, "MozMousePixelScroll", callback, useCapture );
      }
    };

    function _addWheelListener( elem, eventName, callback, useCapture ) {
      elem[ _addEventListener ]( prefix + eventName, support == "wheel" ? callback : function( originalEvent ) {
        !originalEvent && ( originalEvent = window.event );

        // create a normalized event object
        var event = {
          // keep a ref to the original event object
          originalEvent: originalEvent,
          // NOTE: clientX and clientY are not in Mozilla example, but are needed for svg-pan-zoom
          clientX: originalEvent.clientX,
          clientY: originalEvent.clientY,
          target: originalEvent.target || originalEvent.srcElement,
          type: "wheel",
          deltaMode: originalEvent.type == "MozMousePixelScroll" ? 0 : 1,
          deltaX: 0,
          deltaZ: 0,
          preventDefault: function() {
            originalEvent.preventDefault ?
              originalEvent.preventDefault() :
              originalEvent.returnValue = false;
          }
        };

        // calculate deltaY (and deltaX) according to the event
        if ( support == "mousewheel" ) {
          event.deltaY = - 1/40 * originalEvent.wheelDelta;
          // Webkit also support wheelDeltaX
          originalEvent.wheelDeltaX && ( event.deltaX = - 1/40 * originalEvent.wheelDeltaX );
        } else {
          event.deltaY = originalEvent.detail;
        }

        // it's time to fire the callback
        return callback(event);

      }, useCapture || false );
    }

  })(window,document);
}

},{}],3:[function(require,module,exports){
var svgPanZoom = require('./svg-pan-zoom.js');

// UMD module definition
(function(window, document){
  // AMD
  if (typeof define === "function" && define.amd) {
    define("svg-pan-zoom", function () {
      return svgPanZoom;
    });
  // CMD
  } else if (typeof module !== 'undefined' && module.exports) {
    module.exports = svgPanZoom;

    // Browser
    // Keep exporting globally as module.exports is available because of browserify
    window.svgPanZoom = svgPanZoom;
  }
})(window, document)

},{"./svg-pan-zoom.js":4}],4:[function(require,module,exports){
var Mousewheel = require('./mousewheel')  // Keep it here so that mousewheel is initialised
, ControlIcons = require('./control-icons')
, Utils = require('./utilities')
, SvgUtils = require('./svg-utilities')

var SvgPanZoom = function(svg, options) {
  this.init(svg, options)
}

var optionsDefaults = {
  panEnabled: true // enable or disable panning (default enabled)
, controlIconsEnabled: false // insert icons to give user an option in addition to mouse events to control pan/zoom (default disabled)
, zoomEnabled: true // enable or disable zooming (default enabled)
, dblClickZoomEnabled: true // enable or disable zooming by double clicking (default enabled)
, zoomScaleSensitivity: 0.2 // Zoom sensitivity
, minZoom: 0.5 // Minimum Zoom level
, maxZoom: 10 // Maximum Zoom level
, fit: true // enable or disable viewport fit in SVG (default true)
, center: true // enable or disable viewport centering in SVG (default true)
, beforeZoom: null
, onZoom: function(){}
, beforePan: null
, onPan: function(){}
, refreshRate: 60 // in hz
}

SvgPanZoom.prototype.init = function(svg, options) {
  this.xmlNS = 'http://www.w3.org/XML/1998/namespace';
  this.svgNS = 'http://www.w3.org/2000/svg';
  this.xmlnsNS = 'http://www.w3.org/2000/xmlns/';
  this.xlinkNS = 'http://www.w3.org/1999/xlink';
  this.evNS = 'http://www.w3.org/2001/xml-events';

  this.svg = svg
  this.defs = svg.querySelector('defs')

  // thanks to http://stackoverflow.com/questions/9847580/how-to-detect-safari-chrome-ie-firefox-and-opera-browser
  if (/*@cc_on!@*/false || !!document.documentMode) { // internet explorer
    SvgUtils._browser = 'ie';
  } else if (typeof InstallTrigger !== 'undefined') { // firefox
    SvgUtils._browser = 'firefox';
  }

  // Set options
  this.options = Utils.extend(Utils.extend({}, optionsDefaults), options)
  SvgUtils.refreshRate = this.options.refreshRate;

  // Set default state
  this.state = 'none'

  // Get dimensions
  var boundingClientRectNormalized = SvgUtils.getBoundingClientRectNormalized(svg)
  this.width = boundingClientRectNormalized.width
  this.height = boundingClientRectNormalized.height

  // Get viewport
  this.viewport = SvgUtils.getOrCreateViewport(svg)

  // Create zoom and pan cache
  this._zoom = 1
  this._pan = {x: 0, y: 0}

  // Sets initialCTM
  this.processCTM()

  if (this.options.controlIconsEnabled) {
    ControlIcons.enable(this)
  }

  // Add default attributes to SVG
  SvgUtils.setupSvgAttributes(this.svg)

  // Init events handlers
  this.setupHandlers()

  // TODO what for do we need this?
  // It is replacing window.svgPanZoom constructor with this instance
  //
  // if (this.svg.ownerDocument.documentElement.tagName.toLowerCase() !== 'svg') {
  //   this.svg.ownerDocument.defaultView.svgPanZoom = this
  // }
}

/**
 * Get CTM and save it into initialCTM attribute
 * Parse viewBox and if any update initialCTM based on this values
 */
SvgPanZoom.prototype.processCTM = function() {
  var svgViewBox = this.svg.getAttribute('viewBox')

  this.cacheViewBox()
  this.svg.removeAttribute('viewBox')

  if (this.options.fit) {
    var newCTM = this.viewport.getCTM()
      , newScale = Math.min(this.width/(this._viewBox.width - this._viewBox.x), this.height/(this._viewBox.height - this._viewBox.y));

    newCTM.a = newCTM.a * newScale; //x-scale
    newCTM.d = newCTM.d * newScale; //y-scale
    newCTM.e = (newCTM.e - this._viewBox.x) * newScale; //x-transform
    newCTM.f = (newCTM.f - this._viewBox.y) * newScale; //y-transform
    this.initialCTM = newCTM;

    // Update viewport CTM
    SvgUtils.setCTM(this.viewport, newCTM, this.defs);
  } else {
    // Leave sizes as they are
    this.svg.removeAttribute('viewBox')
    this.initialCTM = this.viewport.getCTM();
  }

  // Cache zoom level
  this._zoom = this.initialCTM.a

  // Cache pan level
  this._pan.x = this.initialCTM.e
  this._pan.y = this.initialCTM.f

  if (this.options.center) {
    var that = this;
    window.setTimeout(function() {
      that.center();
      window.setTimeout(function() {
        that.viewport.getCTM();
        that.initialCTM = that.viewport.getCTM();

        // Cache zoom level
        that._zoom = that.initialCTM.a

        // Cache pan level
        that._pan.x = that.initialCTM.e
        that._pan.y = that.initialCTM.f
      }, 1000/this.refreshRate + 1);
    }, 1000/this.refreshRate + 1);
  }
}

/**
 * Cache initial viewBox value
 * If no viewBox is defined, then use viewport size/position instead for viewBox values
 */
SvgPanZoom.prototype.cacheViewBox = function() {
  // ViewBox cache
  this._viewBox = {x: 0, y: 0, width: 0, height: 0}

  var svgViewBox = this.svg.getAttribute('viewBox')

  if (svgViewBox) {
    var viewBoxValues = svgViewBox.split(' ').map(parseFloat)

    // Cache viewbox x and y offset
    this._viewBox.x = viewBoxValues[0]
    this._viewBox.y = viewBoxValues[1]
    this._viewBox.width = viewBoxValues[2]
    this._viewBox.height = viewBoxValues[3]
  } else {
    var bBox = this.viewport.getBBox();

    // Cache viewbox sizes
    this._viewBox.x = bBox.x;
    this._viewBox.y = bBox.y;
    this._viewBox.width = bBox.width
    this._viewBox.height = bBox.height
  }
}

/**
 * Recalculate viewport sizes and update viewBox cache
 */
SvgPanZoom.prototype.recacheViewBox = function() {
  var boundingClientRect = this.viewport.getBoundingClientRect()
    , viewBoxWidth = boundingClientRect.width / this.getZoom()
    , viewBoxHeight = boundingClientRect.height / this.getZoom()

  // Cache viewbox
  this._viewBox.x = 0
  this._viewBox.y = 0
  this._viewBox.width = viewBoxWidth
  this._viewBox.height = viewBoxHeight
}

/**
 * Register event handlers
 */
SvgPanZoom.prototype.setupHandlers = function() {
  var that = this
    , prevEvt = null // use for touchstart event to detect double tap
    ;

  // Mouse down group
  this.svg.addEventListener("mousedown", function(evt) {
    return that.handleMouseDown(evt, null);
  }, false);
  this.svg.addEventListener("touchstart", function(evt) {
    var result = that.handleMouseDown(evt, prevEvt);
    prevEvt = evt
    return result;
  }, false);

  // Mouse up group
  this.svg.addEventListener("mouseup", function(evt) {
    return that.handleMouseUp(evt);
  }, false);
  this.svg.addEventListener("touchend", function(evt) {
    return that.handleMouseUp(evt);
  }, false);

  // Mouse move group
  this.svg.addEventListener("mousemove", function(evt) {
    return that.handleMouseMove(evt);
  }, false);
  this.svg.addEventListener("touchmove", function(evt) {
    return that.handleMouseMove(evt);
  }, false);

  // Mouse leave group
  this.svg.addEventListener("mouseleave", function(evt) {
    return that.handleMouseUp(evt);
  }, false);
  this.svg.addEventListener("touchleave", function(evt) {
    return that.handleMouseUp(evt);
  }, false);
  this.svg.addEventListener("touchcancel", function(evt) {
    return that.handleMouseUp(evt);
  }, false);

  // Mouse wheel listener
  window.addWheelListener(this.svg, function(evt) {
    return that.handleMouseWheel(evt);
  })
}

/**
 * Handle mouse wheel event
 *
 * @param  {object} evt Event object
 */
SvgPanZoom.prototype.handleMouseWheel = function(evt) {
  if (!this.options.zoomEnabled) {
    return;
  }

  if (evt.preventDefault) {
    evt.preventDefault();
  } else {
    evt.returnValue = false;
  }

  var delta = 0

  if ('deltaMode' in evt && evt.deltaMode === 0) {
    // Make empirical adjustments for browsers that give deltaY in pixels (deltaMode=0)

    if (evt.wheelDelta) {
      // Normalizer for Chrome
      delta = evt.deltaY / Math.abs(evt.wheelDelta/3)
    } else {
      // Others. Possibly tablets? Use a value just in case
      delta = evt.deltaY / 120
    }
  } else if ('mozPressure' in evt) {
    // Normalizer for newer Firefox
    // NOTE: May need to change detection at some point if mozPressure disappears.
    delta = evt.deltaY / 3;
  } else {
    // Others should be reasonably normalized by the mousewheel code at the end of the file.
    delta = evt.deltaY;
  }

  var svg = (evt.target.tagName === 'svg' || evt.target.tagName === 'SVG') ? evt.target : evt.target.ownerSVGElement || evt.target.correspondingElement.ownerSVGElement
    , relativeMousePoint = SvgUtils.getRelativeMousePoint(svg, evt)
    , zoom = Math.pow(1 + this.options.zoomScaleSensitivity, (-1) * delta); // multiplying by neg. 1 so as to make zoom in/out behavior match Google maps behavior

  this.zoomAtPoint(svg, relativeMousePoint, zoom)
}

/**
 * Zoom in at an SVG point
 *
 * @param  {object} svg          SVG Element
 * @param  {object} point        SVG Point
 * @param  {float} zoomScale    Number representing how much to zoom
 * @param  {bool} zoomAbsolute [description]
 * @return {[type]}              Default false. If true, zoomScale is treated as an absolute value.
 *                               Otherwise, zoomScale is treated as a multiplied (e.g. 1.10 would zoom in 10%)
 */
SvgPanZoom.prototype.zoomAtPoint = function(svg, point, zoomScale, zoomAbsolute) {
  if (Utils.isFunction(this.options.beforeZoom)) {
    this.options.beforeZoom()
  }

  // Fit zoomScale in set bounds
  if (this._zoom * zoomScale < this.options.minZoom * this.initialCTM.a) {
    zoomScale = (this.options.minZoom * this.initialCTM.a) / this._zoom
  } else if (this._zoom * zoomScale > this.options.maxZoom * this.initialCTM.a) {
    zoomScale = (this.options.maxZoom * this.initialCTM.a) / this._zoom
  }

  var viewportCTM = this.viewport.getCTM()

  point = point.matrixTransform(viewportCTM.inverse())

  var k = svg.createSVGMatrix().translate(point.x, point.y).scale(zoomScale).translate(-point.x, -point.y)
    , wasZoom = viewportCTM
    , setZoom = viewportCTM.multiply(k)

  if (zoomAbsolute) {
    setZoom.a = setZoom.d = zoomScale
  }

  if (setZoom.a !== wasZoom.a) {
    SvgUtils.setCTM(this.viewport, setZoom, this.defs)

    // Cache zoom level
    this._zoom = setZoom.a

    // Cache new pan coordinates
    this._pan.x = setZoom.e
    this._pan.y = setZoom.f
  }

  if (this.options.onZoom) {
    this.options.onZoom(setZoom.a)
  }
}

SvgPanZoom.prototype.publicZoomAtPoint = function(scale, point, absolute) {
  // If not a SVGPoint but has x and y than create new point
  if (Utils.getType(point) !== 'SVGPoint' && 'x' in point && 'y' in point) {
    var _point = this.svg.createSVGPoint()
    _point.x = point.x
    _point.y = point.y
    point = _point
  } else {
    throw new Error('Given point is invalid')
    return
  }

  this.zoomAtPoint(this.svg, point, scale, absolute)
}

/**
 * Get zoom scale/level
 *
 * @return {float} zoom scale
 */
SvgPanZoom.prototype.getZoom = function() {
  return this._zoom
}

SvgPanZoom.prototype.resetZoom = function() {
  var publicInstance = this.getPublicInstance()

  var zoomScale = this.initialCTM.a;
  publicInstance.zoom(zoomScale);
  // Cache zoom level
  this._zoom = zoomScale;

  var x = this.initialCTM.e;
  var y = this.initialCTM.f;
  // Cache pan level
  this._pan.x = x;
  this._pan.y = y;

  if (this.options.center) {
    var that = this;
    window.setTimeout(function() {
      publicInstance.pan({x: x, y: y})
    }, 1000/this.refreshRate + 1);
  }
}

/**
 * Handle mouse move event
 *
 * @param  {object} evt Event
 */
SvgPanZoom.prototype.handleMouseMove = function(evt) {
  if (evt.preventDefault) {
    evt.preventDefault()
  } else {
    evt.returnValue = false
  }

  if (this.state === 'pan' && this.options.panEnabled) {
    // Trigger beforePan
    if (Utils.isFunction(this.options.beforePan)) {
      this.options.beforePan()
    }

    // Pan mode
    var point = SvgUtils.getEventPoint(evt).matrixTransform(this.stateTf)
      , viewportCTM = this.stateTf.inverse().translate(point.x - this.stateOrigin.x, point.y - this.stateOrigin.y)

    SvgUtils.setCTM(this.viewport, viewportCTM, this.defs)

    // Cache pan level
    this._pan.x = viewportCTM.e
    this._pan.y = viewportCTM.f

    // Trigger onPan
    this.options.onPan(this._pan.x, this._pan.y)
  }
}

/**
 * Handle double click event
 * See handleMouseDown() for alternate detection method
 *
 * @param {object} evt Event
 */
SvgPanZoom.prototype.handleDblClick = function(evt) {
  var target = evt.target
    , svg = (target.tagName === 'svg' || target.tagName === 'SVG') ? target : target.ownerSVGElement || target.correspondingElement.ownerSVGElement

  if (evt.preventDefault) {
    evt.preventDefault()
  } else {
    evt.returnValue = false
  }

  // Check if target was a control button
  if (this.options.controlIconsEnabled) {
    var targetClass = target.getAttribute('class') || ''
    if (targetClass.indexOf('svg-pan-zoom-control') > -1) {
      return false
    }
  }

  var zoomFactor

  if (evt.shiftKey) {
    zoomFactor = 1/((1 + this.options.zoomScaleSensitivity) * 2) // zoom out when shift key pressed
  }
  else {
    zoomFactor = (1 + this.options.zoomScaleSensitivity) * 2
  }

  var point = SvgUtils.getRelativeMousePoint(svg, evt)
  this.zoomAtPoint(svg, point, zoomFactor)
}

/**
 * Handle click event
 *
 * @param {object} evt Event
 */
SvgPanZoom.prototype.handleMouseDown = function(evt, prevEvt) {
  if (evt.preventDefault) {
    evt.preventDefault()
  } else {
    evt.returnValue = false
  }

  var svg = (evt.target.tagName === 'svg' || evt.target.tagName === 'SVG') ? evt.target : evt.target.ownerSVGElement || evt.target.correspondingElement.ownerSVGElement
  Utils.mouseAndTouchNormalize(evt, svg)

  // Double click detection; more consistent than ondblclick
  if (this.options.dblClickZoomEnabled && Utils.isDblClick(evt, prevEvt)){
    this.handleDblClick(evt)
  } else {
    // Pan mode
    this.state = 'pan'
    this.stateTf = this.viewport.getCTM().inverse()
    this.stateOrigin = SvgUtils.getEventPoint(evt).matrixTransform(this.stateTf)
  }
}

/**
 * Handle mouse button release event
 *
 * @param {object} evt Event
 */
SvgPanZoom.prototype.handleMouseUp = function(evt) {
  if (evt.preventDefault) {
    evt.preventDefault()
  } else {
    evt.returnValue = false
  }

  if (this.state === 'pan') {
    // Quit pan mode
    this.state = 'none'
  }
}

/**
 * Adjust viewport size (only) so it will fit in SVG
 * Does not center image
 *
 * @param  {bool} dropCache drop viewBox cache and recalculate SVG's viewport sizes. Default false
 */
SvgPanZoom.prototype.fit = function(dropCache) {
  if (dropCache) {
    this.recacheViewBox()
  }

  var newScale = Math.min(this.width/(this._viewBox.width - this._viewBox.x), this.height/(this._viewBox.height - this._viewBox.y))

  this.getPublicInstance().zoom(newScale)
}

/**
 * Adjust viewport pan (only) so it will be centered in SVG
 * Does not zoom/fit image
 *
 * @param  {bool} dropCache drop viewBox cache and recalculate SVG's viewport sizes. Default false
 */
SvgPanZoom.prototype.center = function(dropCache) {
  if (dropCache) {
    this.recacheViewBox()
  }

  var offsetX = (this.width - (this._viewBox.width + this._viewBox.x) * this.getZoom()) * 0.5
    , offsetY = (this.height - (this._viewBox.height + this._viewBox.y) * this.getZoom()) * 0.5

  this.getPublicInstance().pan({x: offsetX, y: offsetY})
}

/**
 * Pan to a rendered position
 *
 * @param  {object} point {x: 0, y: 0}
 */
SvgPanZoom.prototype.pan = function(point) {
  // Trigger beforePan
  if (Utils.isFunction(this.options.beforePan)) {
    this.options.beforePan()
  }

  var viewportCTM = this.viewport.getCTM()
  viewportCTM.e = point.x
  viewportCTM.f = point.y
  SvgUtils.setCTM(this.viewport, viewportCTM, this.defs)

  // Cache pan level
  this._pan.x = viewportCTM.e
  this._pan.y = viewportCTM.f

  // Trigger onPan
  this.options.onPan(this._pan.x, this._pan.y)
}

/**
 * Relatively pan the graph by a specified rendered position vector
 *
 * @param  {object} point {x: 0, y: 0}
 */
SvgPanZoom.prototype.panBy = function(point) {
  // Trigger beforePan
  if (Utils.isFunction(this.options.beforePan)) {
    this.options.beforePan()
  }

  var viewportCTM = this.viewport.getCTM()
  viewportCTM.e += point.x
  viewportCTM.f += point.y
  SvgUtils.setCTM(this.viewport, viewportCTM, this.defs)

  // Cache pan level
  this._pan.x = viewportCTM.e
  this._pan.y = viewportCTM.f

  // Trigger onPan
  this.options.onPan(this._pan.x, this._pan.y)
}

/**
 * Get pan vector
 *
 * @return {object} {x: 0, y: 0}
 */
SvgPanZoom.prototype.getPan = function() {
  // Do not return object directly because it will be possible to modify it using the reference
  return {x: this._pan.x, y: this._pan.y}
}

/**
 * Recalculates cached svg dimensions and controls position
 */
SvgPanZoom.prototype.resize = function() {
  // Get dimensions
  var boundingClientRectNormalized = SvgUtils.getBoundingClientRectNormalized(this.svg)
  this.width = boundingClientRectNormalized.width
  this.height = boundingClientRectNormalized.height

  // Reposition control icons by re-enabling them
  if (this.options.controlIconsEnabled) {
    this.getPublicInstance().disableControlIcons()
    this.getPublicInstance().enableControlIcons()
  }
}

/**
 * Returns a public instance object
 * @return {object} Public instance object
 */
SvgPanZoom.prototype.getPublicInstance = function() {
  var that = this

  // Create cache
  if (!this.publicInstance) {
    this.publicInstance = {
      // Pan
      enablePan: function() {that.options.panEnabled = true}
    , disablePan: function() {that.options.panEnabled = false}
    , isPanEnabled: function() {return !!that.options.panEnabled}
    , pan: function(point) {that.pan(point)}
    , panBy: function(point) {that.panBy(point)}
    , getPan: function() {return that.getPan()}
      // Pan event
    , setBeforePan: function(fn) {that.options.beforePan = Utils.proxy(fn, that.publicInstance)}
    , setOnPan: function(fn) {that.options.onPan = Utils.proxy(fn, that.publicInstance)}
      // Zoom and Control Icons
    , enableZoom: function() {
        that.options.zoomEnabled = true;
      }
    , disableZoom: function() {
        that.options.zoomEnabled = false;
      }
    , isZoomEnabled: function() {return !!that.options.zoomEnabled}
    , enableControlIcons: function() {
        if (!that.options.controlIconsEnabled) {
          that.options.controlIconsEnabled = true
          ControlIcons.enable(that)
        }
      }
    , disableControlIcons: function() {
        if (that.options.controlIconsEnabled) {
          that.options.controlIconsEnabled = false;
          ControlIcons.disable(that)
        }
      }
    , isControlIconsEnabled: function() {return !!that.options.controlIconsEnabled}
      // Double click zoom
    , enableDblClickZoom: function() {that.options.dblClickZoomEnabled = true}
    , disableDblClickZoom: function() {that.options.dblClickZoomEnabled = false}
      // Zoom scale and bounds
    , setZoomScaleSensitivity: function(scale) {that.options.zoomScaleSensitivity = scale}
    , setMinZoom: function(zoom) {that.options.minZoom = zoom}
    , setMaxZoom: function(zoom) {that.options.maxZoom = zoom}
      // Zoom event
    , setBeforeZoom: function(fn) {that.options.beforeZoom = Utils.proxy(fn, that.publicInstance)}
    , setOnZoom: function(fn) {that.options.onZoom = Utils.proxy(fn, that.publicInstance)}
      // Zooming
    , zoom: function(scale) {
        that.zoomAtPoint(that.svg, SvgUtils.getSvgCenterPoint(that.svg), scale, true)
      }
    , zoomBy: function(scale) {
        that.zoomAtPoint(that.svg, SvgUtils.getSvgCenterPoint(that.svg), scale, false)
      }
    , zoomAtPoint: function(scale, point) {
        that.publicZoomAtPoint(scale, point, true)
      }
    , zoomAtPointBy: function(scale, point) {
        that.publicZoomAtPoint(scale, point, false)
      }
    , zoomIn: function() {
        this.zoomBy(1 + that.options.zoomScaleSensitivity)
      }
    , zoomOut: function() {
        this.zoomBy(1 / (1 + that.options.zoomScaleSensitivity))
      }
    , resetZoom: function() {that.resetZoom()}
    , getZoom: function() {return that.getZoom()}
    , fit: function(dropCache) {return that.fit(dropCache)}
    , center: function(dropCache) {return that.center(dropCache)}
    , resize: function() {that.resize()}
    }
  }

  return this.publicInstance
}

/**
 * Stores pairs of instances of SvgPanZoom and SVG
 * Each pair is represented by an object {svg: SVG, instance: SvgPanZoom}
 *
 * @type {Array}
 */
var instancesStore = []

var svgPanZoom = function(elementOrSelector, options){
  var svg = Utils.getSvg(elementOrSelector)

  if (svg === null) {
    return null
  } else {
    // Look for existent instance
    for(var i = instancesStore.length - 1; i >= 0; i--) {
      if (instancesStore[i].svg === svg) {
        return instancesStore[i].instance.getPublicInstance()
      }
    }

    // If instance not found - create one
    instancesStore.push({
      svg: svg
    , instance: new SvgPanZoom(svg, options)
    })

    // Return just pushed instance
    return instancesStore[instancesStore.length - 1].instance.getPublicInstance()
  }
}

module.exports = svgPanZoom;

},{"./control-icons":1,"./mousewheel":2,"./svg-utilities":5,"./utilities":6}],5:[function(require,module,exports){
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

},{"./utilities":6}],6:[function(require,module,exports){
module.exports = {
  /**
   * Extends an object
   *
   * @param  {object} target object to extend
   * @param  {object} source object to take properties from
   * @return {object}        extended object
   */
  extend: function(target, source) {
    target = target || {};
    for (var prop in source) {
      // Go recursively
      if (this.isObject(source[prop])) {
        target[prop] = this.extend(target[prop], source[prop])
      } else {
        target[prop] = source[prop]
      }
    }
    return target;
  }

  /**
   * Checks if an object is a DOM element
   *
   * @param  {object}  o HTML element or String
   * @return {Boolean}   returns true if object is a DOM element
   */
, isElement: function(o){
    return (
      typeof HTMLElement === "object" ? (o instanceof HTMLElement || o instanceof SVGElement || o instanceof SVGSVGElement) : //DOM2
      o && typeof o === "object" && o !== null && o.nodeType === 1 && typeof o.nodeName==="string"
    );
  }

  /**
   * Checks if an object is an Object
   *
   * @param  {object}  o Object
   * @return {Boolean}   returns true if object is an Object
   */
, isObject: function(o){
    return Object.prototype.toString.call(o) === '[object Object]';
  }

  /**
   * Checks if an object is a Function
   *
   * @param  {object}  f Function
   * @return {Boolean}   returns true if object is a Function
   */
, isFunction: function(f){
    return Object.prototype.toString.call(f) === '[object Function]';
  }

  /**
   * Search for an SVG element
   *
   * @param  {object|string} elementOrSelector DOM Element or selector String
   * @return {object|null}                   SVG or null
   */
, getSvg: function(elementOrSelector) {
    var element
      , svg;

    if (!this.isElement(elementOrSelector)) {
      // If selector provided
      if (typeof elementOrSelector == 'string' || elementOrSelector instanceof String) {
        // Try to find the element
        element = document.querySelector(elementOrSelector)

        if (!element) {
          throw new Error('Provided selector did not find any elements')
          return null
        }

      } else {
        throw new Error('Provided selector is not an HTML object nor String')
        return null
      }
    } else {
      element = elementOrSelector
    }

    if (element.tagName.toLowerCase() === 'svg') {
      svg = element;
    } else {
      if (element.tagName.toLowerCase() === 'object') {
        svg = element.contentDocument.documentElement;
      } else {
        if (element.tagName.toLowerCase() === 'embed') {
          svg = element.getSVGDocument().documentElement;
        } else {
          if (element.tagName.toLowerCase() === 'img') {
            throw new Error('Cannot script an SVG in an "img" element. Please use an "object" element or an in-line SVG.');
          } else {
            throw new Error('Cannot get SVG.');
          }
          return null
        }
      }
    }

    return svg
  }

  /**
   * Attach a given context to a function
   * @param  {Function} fn      Function
   * @param  {object}   context Context
   * @return {Function}           Function with certain context
   */
, proxy: function(fn, context) {
    return function() {
      fn.apply(context, arguments)
    }
  }

  /**
   * Returns object type
   * Uses toString that returns [object SVGPoint]
   * And than parses object type from string
   *
   * @param  {object} o Any object
   * @return {string}   Object type
   */
, getType: function(o) {
    return Object.prototype.toString.apply(o).replace(/^\[object\s/, '').replace(/\]$/, '')
  }

  /**
   * If it is a touch event than add clientX and clientY to event object
   *
   * @param  {object} evt Event object
   */
, mouseAndTouchNormalize: function(evt, svg) {
    // If no cilentX and but touch objects are available
    if (evt.clientX === void 0 || evt.clientX === null) {
      // If it is a touch event
      if (evt.changedTouches !== void 0 && evt.changedTouches.length) {
        // If touch event has changedTouches
        if (evt.changedTouches[0].clientX !== void 0) {
          evt.clientX = evt.changedTouches[0].clientX
          evt.clientY = evt.changedTouches[0].clientY
        }
        // If changedTouches has pageX attribute
        else if (evt.changedTouches[0].pageX !== void 0) {
          var rect = svg.getBoundingClientRect();

          evt.clientX = evt.changedTouches[0].pageX - rect.left
          evt.clientY = evt.changedTouches[0].pageY - rect.top
        }
      } else {
        // Fallback
        evt.clientX = 0
        evt.clientY = 0
      }
    }
  }

  /**
   * Check if an event is a double click/tap
   * TODO: For touch gestures use a library (hammer.js) that takes in account other events
   * (touchmove and touchend). It should take in account tap duration and traveled distance
   *
   * @param  {object}  evt     Event
   * @param  {object}  prevEvt Previous Event
   * @return {Boolean}         [description]
   */
, isDblClick: function(evt, prevEvt) {
    // Double click detected by browser
    if (evt.detail === 2) {
      return true;
    }
    // Try to compare events
    else if (prevEvt !== void 0 && prevEvt !== null) {
      var timeStampDiff = evt.timeStamp - prevEvt.timeStamp // should be lower than 250 ms
        , touchesDistance = Math.sqrt(Math.pow(evt.clientX - prevEvt.clientX, 2) + Math.pow(evt.clientY - prevEvt.clientY, 2))

      return timeStampDiff < 250 && touchesDistance < 10
    }

    // Nothing found
    return false;
  }
  // A (possibly faster) way to get the current timestamp as an integer.
, now: Date.now || function() {
    return new Date().getTime();
  }
  // From underscore.
  // Returns a function, that, when invoked, will only be triggered at most once
  // during a given window of time. Normally, the throttled function will run
  // as much as it can, without ever going more than once per `wait` duration;
  // but if you'd like to disable the execution on the leading edge, pass
  // `{leading: false}`. To disable execution on the trailing edge, ditto.
, throttle: function(func, wait, options) {
    var that = this;
    var context, args, result;
    var timeout = null;
    var previous = 0;
    if (!options) options = {};
    var later = function() {
      previous = options.leading === false ? 0 : that.now();
      timeout = null;
      result = func.apply(context, args);
      if (!timeout) context = args = null;
    };
    return function() {
      var now = that.now();
      if (!previous && options.leading === false) previous = now;
      var remaining = wait - (now - previous);
      context = this;
      args = arguments;
      if (remaining <= 0 || remaining > wait) {
        clearTimeout(timeout);
        timeout = null;
        previous = now;
        result = func.apply(context, args);
        if (!timeout) context = args = null;
      } else if (!timeout && options.trailing !== false) {
        timeout = setTimeout(later, remaining);
      }
      return result;
    };
  }
}

},{}]},{},[3])