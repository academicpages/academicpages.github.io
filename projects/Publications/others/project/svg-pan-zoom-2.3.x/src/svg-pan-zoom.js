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
