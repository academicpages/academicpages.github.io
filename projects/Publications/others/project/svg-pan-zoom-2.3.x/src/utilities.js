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
