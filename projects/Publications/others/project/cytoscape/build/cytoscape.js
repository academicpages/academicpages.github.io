/*!
 * This file is part of Cytoscape.js 2.3.10.
 * 
 * Cytoscape.js is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation, either version 3 of the License, or (at your option) any
 * later version.
 * 
 * Cytoscape.js is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU Lesser General Public License along with
 * Cytoscape.js. If not, see <http://www.gnu.org/licenses/>.
 */
 

// this is put as a global var in the browser
// or it's just a global to this module if commonjs

var cytoscape;

(function(window){ 'use strict';

  // the object iteself is a function that init's an instance of cytoscape

  var $$ = cytoscape = function(){ // jshint ignore:line
    return cytoscape.init.apply(cytoscape, arguments);
  };

  $$.version = '2.3.10';
  
  // allow functional access to cytoscape.js
  // e.g. var cyto = $.cytoscape({ selector: "#foo", ... });
  //      var nodes = cyto.nodes();
  $$.init = function( options ){
    
    // if no options specified, use default
    if( options === undefined ){
      options = {};
    }

    // create instance
    if( $$.is.plainObject( options ) ){
      return new $$.Core( options );
    } 
    
    // allow for registration of extensions
    // e.g. $.cytoscape('renderer', 'svg', SvgRenderer);
    // e.g. $.cytoscape('renderer', 'svg', 'nodeshape', 'ellipse', SvgEllipseNodeShape);
    // e.g. $.cytoscape('core', 'doSomething', function(){ /* doSomething code */ });
    // e.g. $.cytoscape('collection', 'doSomething', function(){ /* doSomething code */ });
    else if( $$.is.string( options ) ) {
      return $$.extension.apply($$.extension, arguments);
    }
  };

  // define the function namespace here, since it has members in many places
  $$.fn = {};

  if( typeof module !== 'undefined' && module.exports ){ // expose as a commonjs module
    module.exports = cytoscape;
  }

  if( typeof define !== 'undefined' && define.amd ){ // expose as an amd/requirejs module
    define('cytoscape', function(){
      return cytoscape;
    });
  }

  // make sure we always register in the window just in case (e.g. w/ derbyjs)
  if( window ){
    window.cytoscape = cytoscape;
  }
  
})( typeof window === 'undefined' ? null : window );

// type testing utility functions

;(function($$, window){ 'use strict';

  $$.is = {
    defined: function(obj){
      return obj != null; // not undefined or null
    },

    string: function(obj){
      return obj != null && typeof obj == typeof '';
    },
    
    fn: function(obj){
      return obj != null && typeof obj === typeof function(){};
    },
    
    array: function(obj){
      return Array.isArray ? Array.isArray(obj) : obj != null && obj instanceof Array;
    },
    
    plainObject: function(obj){
      return obj != null && typeof obj === typeof {} && !$$.is.array(obj) && obj.constructor === Object;
    },
    
    number: function(obj){
      return obj != null && typeof obj === typeof 1 && !isNaN(obj);
    },

    integer: function( obj ){
      return $$.is.number(obj) && Math.floor(obj) === obj;
    },
    
    color: function(obj){
      return obj != null && typeof obj === typeof '' && $.Color(obj).toString() !== '';
    },
    
    bool: function(obj){
      return obj != null && typeof obj === typeof true;
    },
    
    elementOrCollection: function(obj){
      return $$.is.element(obj) || $$.is.collection(obj);
    },
    
    element: function(obj){
      return obj instanceof $$.Element && obj._private.single;
    },
    
    collection: function(obj){
      return obj instanceof $$.Collection && !obj._private.single;
    },
    
    core: function(obj){
      return obj instanceof $$.Core;
    },

    style: function(obj){
      return obj instanceof $$.Style;
    },

    stylesheet: function(obj){
      return obj instanceof $$.Stylesheet;
    },

    event: function(obj){
      return obj instanceof $$.Event;
    },

    emptyString: function(obj){
      if( !obj ){ // null is empty
        return true; 
      } else if( $$.is.string(obj) ){
        if( obj === '' || obj.match(/^\s+$/) ){
          return true; // empty string is empty
        }
      }
      
      return false; // otherwise, we don't know what we've got
    },
    
    nonemptyString: function(obj){
      if( obj && $$.is.string(obj) && obj !== '' && !obj.match(/^\s+$/) ){
        return true;
      }

      return false;
    },

    domElement: function(obj){
      if( typeof HTMLElement === 'undefined' ){
        return false; // we're not in a browser so it doesn't matter
      } else {
        return obj instanceof HTMLElement;
      }
    },

    boundingBox: function(obj){
      return $$.is.plainObject(obj) && 
        $$.is.number(obj.x1) && $$.is.number(obj.x2) &&
        $$.is.number(obj.y1) && $$.is.number(obj.y2)
      ;
    },

    touch: function(){
      return window && ( ('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch );
    },

    gecko: function(){
      return typeof InstallTrigger !== 'undefined' || ('MozAppearance' in document.documentElement.style);
    },

    webkit: function(){
      return typeof webkitURL !== 'undefined' || ('WebkitAppearance' in document.documentElement.style);
    },

    chromium: function(){
      return typeof chrome !== 'undefined';
    },

    khtml: function(){
      return navigator.vendor.match(/kde/i); // TODO probably a better way to detect this...
    },

    khtmlEtc: function(){
      return $$.is.khtml() || $$.is.webkit() || $$.is.blink();
    },

    trident: function(){
       return typeof ActiveXObject !== 'undefined' || /*@cc_on!@*/false;
    },

    windows: function(){
      return typeof navigator !== 'undefined' && navigator.appVersion.match(/Win/i);
    },

    mac: function(){
      return typeof navigator !== 'undefined' && navigator.appVersion.match(/Mac/i);
    },

    linux: function(){
      return typeof navigator !== 'undefined' && navigator.appVersion.match(/Linux/i);
    },

    unix: function(){
      return typeof navigator !== 'undefined' && navigator.appVersion.match(/X11/i);
    }
  };  
  
})( cytoscape, typeof window === 'undefined' ? null : window );

;(function($$, window){ 'use strict';
  
  // utility functions only for internal use

  $$.util = {

    // the jquery extend() function
    // NB: modified to use $$.is etc since we can't use jquery functions
    extend: function() {
      var options, name, src, copy, copyIsArray, clone,
        target = arguments[0] || {},
        i = 1,
        length = arguments.length,
        deep = false;

      // Handle a deep copy situation
      if ( typeof target === 'boolean' ) {
        deep = target;
        target = arguments[1] || {};
        // skip the boolean and the target
        i = 2;
      }

      // Handle case when target is a string or something (possible in deep copy)
      if ( typeof target !== 'object' && !$$.is.fn(target) ) {
        target = {};
      }

      // extend jQuery itself if only one argument is passed
      if ( length === i ) {
        target = this;
        --i;
      }

      for ( ; i < length; i++ ) {
        // Only deal with non-null/undefined values
        if ( (options = arguments[ i ]) != null ) {
          // Extend the base object
          for ( name in options ) {
            src = target[ name ];
            copy = options[ name ];

            // Prevent never-ending loop
            if ( target === copy ) {
              continue;
            }

            // Recurse if we're merging plain objects or arrays
            if ( deep && copy && ( $$.is.plainObject(copy) || (copyIsArray = $$.is.array(copy)) ) ) {
              if ( copyIsArray ) {
                copyIsArray = false;
                clone = src && $$.is.array(src) ? src : [];

              } else {
                clone = src && $$.is.plainObject(src) ? src : {};
              }

              // Never move original objects, clone them
              target[ name ] = $$.util.extend( deep, clone, copy );

            // Don't bring in undefined values
            } else if ( copy !== undefined ) {
              target[ name ] = copy;
            }
          }
        }
      }

      // Return the modified object
      return target;
    },

    // require that pulls in module from commonjs, amd, or window (falling back until found)
    require: function( name, callback, options ){
      var ret;
      options = $$.util.extend({
        msgIfNotFound: true
      }, options);

      var done = false;
      var fulfil = function( ret ){
        done = true;
        callback( ret );
      };

      var checkWindow = function( next ){
        if( window ){ // detected browser/window env
          ret = window[ name ];
        }

        if( ret !== undefined ){ fulfil(ret); }
        if( next ){ next(); }
      };
      var onCheckWindowDone = function(){
        if( !done ){
          checkCommonJs( onCheckCommonJsDone );
        }
      };

      var checkCommonJs = function( next ){
        if( typeof module !== 'undefined' && module.exports && require ){ // detected commonjs env
          ret = require( name ); // regular require
        }

        if( ret !== undefined ){ fulfil(ret); }
        if( next ){ next(); }
      };
      var onCheckCommonJsDone = function(){
        if( !done ){
          checkAmd( onCheckAmdDone );
        }
      };

      var checkAmd = function( next ){
        if( typeof define !== 'undefined' && define.amd && require ){ // detected amd env w/ defined module
          require([ name ], function( nameImpl ){
            ret = nameImpl;
            
            if( ret !== undefined ){ fulfil(ret); }
            if( next ){ next(); }
          });
        }
      };
      var onCheckAmdDone = function(){
        if( !done && options.msgIfNotFound ){
          $$.util.error('Cytoscape.js tried to pull in dependency `' + name + '` but no module (i.e. CommonJS, AMD, or window) was found');
        }
      };

      // kick off 1st check: window
      checkWindow( onCheckWindowDone );

    },

    // multiple requires in one callback
    requires: function( names, callback ){
      var impls = [];
      var gotImpl = [];

      var checkDone = function(){
        for( var i = 0; i < names.length; i++ ){ // check have all impls
          if( !gotImpl[i] ){ return; }
        }

        // otherwise, all got all impls => done
        callback.apply( callback, impls ); 
      };

      for( var i = 0; i < names.length; i++ ){ (function(){ // w/scope
        var name = names[i];
        var index = i;

        $$.util.require(name, function(impl){
          impls[index] = impl;
          gotImpl[index] = true;

          checkDone();
        });
      })(); }
    },

    // ported lodash throttle function
    throttle: function(func, wait, options) {
      var leading = true,
          trailing = true;

      if (options === false) {
        leading = false;
      } else if ($$.is.plainObject(options)) {
        leading = 'leading' in options ? options.leading : leading;
        trailing = 'trailing' in options ? options.trailing : trailing;
      }
      options = options || {};
      options.leading = leading;
      options.maxWait = wait;
      options.trailing = trailing;

      return $$.util.debounce(func, wait, options);
    },

    now: function(){
      return +new Date();
    },

    // ported lodash debounce function
    debounce: function(func, wait, options) {
      var args,
          maxTimeoutId,
          result,
          stamp,
          thisArg,
          timeoutId,
          trailingCall,
          lastCalled = 0,
          maxWait = false,
          trailing = true;

      if (!$$.is.fn(func)) {
        return;
      }
      wait = Math.max(0, wait) || 0;
      if (options === true) {
        var leading = true;
        trailing = false;
      } else if ($$.is.plainObject(options)) {
        leading = options.leading;
        maxWait = 'maxWait' in options && (Math.max(wait, options.maxWait) || 0);
        trailing = 'trailing' in options ? options.trailing : trailing;
      }
      var delayed = function() {
        var remaining = wait - ($$.util.now() - stamp);
        if (remaining <= 0) {
          if (maxTimeoutId) {
            clearTimeout(maxTimeoutId);
          }
          var isCalled = trailingCall;
          maxTimeoutId = timeoutId = trailingCall = undefined;
          if (isCalled) {
            lastCalled = $$.util.now();
            result = func.apply(thisArg, args);
            if (!timeoutId && !maxTimeoutId) {
              args = thisArg = null;
            }
          }
        } else {
          timeoutId = setTimeout(delayed, remaining);
        }
      };

      var maxDelayed = function() {
        if (timeoutId) {
          clearTimeout(timeoutId);
        }
        maxTimeoutId = timeoutId = trailingCall = undefined;
        if (trailing || (maxWait !== wait)) {
          lastCalled = $$.util.now();
          result = func.apply(thisArg, args);
          if (!timeoutId && !maxTimeoutId) {
            args = thisArg = null;
          }
        }
      };

      return function() {
        args = arguments;
        stamp = $$.util.now();
        thisArg = this;
        trailingCall = trailing && (timeoutId || !leading);

        if (maxWait === false) {
          var leadingCall = leading && !timeoutId;
        } else {
          if (!maxTimeoutId && !leading) {
            lastCalled = stamp;
          }
          var remaining = maxWait - (stamp - lastCalled),
              isCalled = remaining <= 0;

          if (isCalled) {
            if (maxTimeoutId) {
              maxTimeoutId = clearTimeout(maxTimeoutId);
            }
            lastCalled = stamp;
            result = func.apply(thisArg, args);
          }
          else if (!maxTimeoutId) {
            maxTimeoutId = setTimeout(maxDelayed, remaining);
          }
        }
        if (isCalled && timeoutId) {
          timeoutId = clearTimeout(timeoutId);
        }
        else if (!timeoutId && wait !== maxWait) {
          timeoutId = setTimeout(delayed, wait);
        }
        if (leadingCall) {
          isCalled = true;
          result = func.apply(thisArg, args);
        }
        if (isCalled && !timeoutId && !maxTimeoutId) {
          args = thisArg = null;
        }
        return result;
      };
    },

    error: function( msg ){
      if( console ){
        if( console.error ){
          console.error.apply( console, arguments );
        } else if( console.log ){
          console.log.apply( console, arguments );
        } else {
          throw msg;
        }
      } else {
        throw msg;
      }
    },    

    clone: function( obj ){
      var target = {};
      for (var i in obj) {
        if ( obj.hasOwnProperty(i) ) { // TODO is this hasOwnProperty() call necessary for our use?
          target[i] = obj[i];
        }
      }
      return target;
    },

    // gets a shallow copy of the argument
    copy: function( obj ){
      if( obj == null ){
        return obj;
      } if( $$.is.array(obj) ){
        return obj.slice();
      } else if( $$.is.plainObject(obj) ){
        return $$.util.clone( obj );
      } else {
        return obj;
      }
    },
    
    // makes a full bb (x1, y1, x2, y2, w, h) from implicit params
    makeBoundingBox: function( bb ){
      if( bb.x1 != null && bb.y1 != null ){
        if( bb.x2 != null && bb.y2 != null && bb.x2 >= bb.x1 && bb.y2 >= bb.y1 ){
          return {
            x1: bb.x1,
            y1: bb.y1,
            x2: bb.x2,
            y2: bb.y2,
            w: bb.x2 - bb.x1,
            h: bb.y2 - bb.y1
          };
        } else if( bb.w != null && bb.h != null && bb.w >= 0 && bb.h >= 0 ){
          return {
            x1: bb.x1,
            y1: bb.y1,
            x2: bb.x1 + bb.w,
            y2: bb.y1 + bb.h,
            w: bb.w,
            h: bb.h
          };
        }
      } 
    },

    // has anything been set in the map
    mapEmpty: function( map ){
      var empty = true;

      if( map != null ){
        for(var i in map){ // jshint ignore:line
          empty = false;
          break;
        }
      }

      return empty;
    },

    // pushes to the array at the end of a map (map may not be built)
    pushMap: function( options ){
      var array = $$.util.getMap(options);

      if( array == null ){ // if empty, put initial array
        $$.util.setMap( $.extend({}, options, {
          value: [ options.value ]
        }) );
      } else {
        array.push( options.value );
      }
    },

    // sets the value in a map (map may not be built)
    setMap: function( options ){
      var obj = options.map;
      var key;
      var keys = options.keys;
      var l = keys.length;

      for(var i = 0; i < l; i++){
        var key = keys[i];

        if( $$.is.plainObject( key ) ){
          $$.util.error('Tried to set map with object key');
        }

        if( i < keys.length - 1 ){
          
          // extend the map if necessary
          if( obj[key] == null ){
            obj[key] = {};
          }
          
          obj = obj[key];
        } else {
          // set the value
          obj[key] = options.value;
        }
      }
    },
    
    // gets the value in a map even if it's not built in places
    getMap: function( options ){
      var obj = options.map;
      var keys = options.keys;
      var l = keys.length;
      
      for(var i = 0; i < l; i++){
        var key = keys[i];

        if( $$.is.plainObject( key ) ){
          $$.util.error('Tried to get map with object key');
        }

        obj = obj[key];
        
        if( obj == null ){
          return obj;
        }
      }
      
      return obj;
    },

    // deletes the entry in the map
    deleteMap: function( options ){
      var obj = options.map;
      var keys = options.keys;
      var l = keys.length;
      var keepChildren = options.keepChildren;
      
      for(var i = 0; i < l; i++){
        var key = keys[i];

        if( $$.is.plainObject( key ) ){
          $$.util.error('Tried to delete map with object key');
        }

        var lastKey = i === options.keys.length - 1;
        if( lastKey ){
          
          if( keepChildren ){ // then only delete child fields not in keepChildren
            for( var child in obj ){
              if( !keepChildren[child] ){
                obj[child] = undefined;
              }
            }
          } else {
            obj[key] = undefined;
          }

        } else {
          obj = obj[key];
        }
      }
    },
    
    capitalize: function(str){
      if( $$.is.emptyString(str) ){
        return str;
      }
      
      return str.charAt(0).toUpperCase() + str.substring(1);
    },

    camel2dash: function( str ){
      var ret = [];

      for( var i = 0; i < str.length; i++ ){
        var ch = str[i];
        var chLowerCase = ch.toLowerCase();
        var isUpperCase = ch !== chLowerCase;

        if( isUpperCase ){
          ret.push( '-' );
          ret.push( chLowerCase );
        } else {
          ret.push( ch );
        }
      }

      var noUpperCases = ret.length === str.length;
      if( noUpperCases ){ return str; } // cheaper than .join()

      return ret.join('');
    },

    dash2camel: function( str ){
      var ret = [];
      var nextIsUpper = false;

      for( var i = 0; i < str.length; i++ ){
        var ch = str[i];
        var isDash = ch === '-';

        if( isDash ){
          nextIsUpper = true;
        } else {
          if( nextIsUpper ){
            ret.push( ch.toUpperCase() );
          } else {
            ret.push( ch );
          }

          nextIsUpper = false;
        }
      }

      return ret.join('');
    },

    // strip spaces from beginning of string and end of string
    trim: function( str ){
      var first, last;

      // find first non-space char
      for( first = 0; first < str.length && str[first] === ' '; first++ ){}

      // find last non-space char
      for( last = str.length - 1; last > first && str[last] === ' '; last-- ){}

      return str.substring(first, last + 1);
    },

    // get [r, g, b] from #abc or #aabbcc
    hex2tuple: function( hex ){
      if( !(hex.length === 4 || hex.length === 7) || hex[0] !== "#" ){ return; }

      var shortHex = hex.length === 4;
      var r, g, b;
      var base = 16;

      if( shortHex ){
        r = parseInt( hex[1] + hex[1], base );
        g = parseInt( hex[2] + hex[2], base );
        b = parseInt( hex[3] + hex[3], base );
      } else {
        r = parseInt( hex[1] + hex[2], base );
        g = parseInt( hex[3] + hex[4], base );
        b = parseInt( hex[5] + hex[6], base );
      }

      return [r, g, b];
    },

    // get [r, g, b, a] from hsl(0, 0, 0) or hsla(0, 0, 0, 0)
    hsl2tuple: function( hsl ){
      var ret;
      var h, s, l, a, r, g, b;
      function hue2rgb(p, q, t){
        if(t < 0) t += 1;
        if(t > 1) t -= 1;
        if(t < 1/6) return p + (q - p) * 6 * t;
        if(t < 1/2) return q;
        if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
        return p;
      }

      var m = new RegExp("^" + $$.util.regex.hsla + "$").exec(hsl);
      if( m ){

        // get hue
        h = parseInt( m[1] ); 
        if( h < 0 ){
          h = ( 360 - (-1*h % 360) ) % 360;
        } else if( h > 360 ){
          h = h % 360;
        }
        h /= 360; // normalise on [0, 1]

        s = parseFloat( m[2] );
        if( s < 0 || s > 100 ){ return; } // saturation is [0, 100]
        s = s/100; // normalise on [0, 1]

        l = parseFloat( m[3] );
        if( l < 0 || l > 100 ){ return; } // lightness is [0, 100]
        l = l/100; // normalise on [0, 1]

        a = m[4];
        if( a !== undefined ){
          a = parseFloat( a );

          if( a < 0 || a > 1 ){ return; } // alpha is [0, 1]
        }

        // now, convert to rgb
        // code from http://mjijackson.com/2008/02/rgb-to-hsl-and-rgb-to-hsv-color-model-conversion-algorithms-in-javascript
        if( s === 0 ){
          r = g = b = Math.round(l * 255); // achromatic
        } else {
          var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
          var p = 2 * l - q;
          r = Math.round( 255 * hue2rgb(p, q, h + 1/3) );
          g = Math.round( 255 * hue2rgb(p, q, h) );
          b = Math.round( 255 * hue2rgb(p, q, h - 1/3) );
        }

        ret = [r, g, b, a];
      }

      return ret;
    },

    // get [r, g, b, a] from rgb(0, 0, 0) or rgba(0, 0, 0, 0)
    rgb2tuple: function( rgb ){
      var ret;

      var m = new RegExp("^" + $$.util.regex.rgba + "$").exec(rgb);
      if( m ){
        ret = [];

        var isPct = [];
        for( var i = 1; i <= 3; i++ ){
          var channel = m[i];

          if( channel[ channel.length - 1 ] === "%" ){
            isPct[i] = true;
          }
          channel = parseFloat( channel );

          if( isPct[i] ){
            channel = channel/100 * 255; // normalise to [0, 255]
          }

          if( channel < 0 || channel > 255 ){ return; } // invalid channel value

          ret.push( Math.floor(channel) );
        }

        var atLeastOneIsPct = isPct[1] || isPct[2] || isPct[3];
        var allArePct = isPct[1] && isPct[2] && isPct[3];
        if( atLeastOneIsPct && !allArePct ){ return; } // must all be percent values if one is

        var alpha = m[4];
        if( alpha !== undefined ){
          alpha = parseFloat( alpha );

          if( alpha < 0 || alpha > 1 ){ return; } // invalid alpha value

          ret.push( alpha );
        }
      }

      return ret;
    },

    colorname2tuple: function( color ){
      return $$.util.colors[ color.toLowerCase() ];
    },

    color2tuple: function( color ){
      return ( $$.is.array(color) ? color : null ) 
        || $$.util.colorname2tuple(color)
        || $$.util.hex2tuple(color)
        || $$.util.rgb2tuple(color)
        || $$.util.hsl2tuple(color);
    },

    tuple2hex: function( tuple ){
      var r = tuple[0];
      var g = tuple[1];
      var b = tuple[2];

      function ch2hex( ch ){
        var hex = ch.toString(16);

        if( hex.length === 1 ){
          hex = '0' + hex;
        }

        return hex;
      }

      return '#' + ch2hex(r) + ch2hex(g) + ch2hex(b);
    },

    colors: {
      // special colour names
      transparent:      [0,0,0,0], // NB alpha === 0

      // regular colours
      aliceblue:        [240,248,255],
      antiquewhite:      [250,235,215],
      aqua:          [0,255,255],
      aquamarine:        [127,255,212],
      azure:          [240,255,255],
      beige:          [245,245,220],
      bisque:          [255,228,196],
      black:          [0,0,0],
      blanchedalmond:      [255,235,205],
      blue:          [0,0,255],
      blueviolet:        [138,43,226],
      brown:          [165,42,42],
      burlywood:        [222,184,135],
      cadetblue:        [95,158,160],
      chartreuse:        [127,255,0],
      chocolate:        [210,105,30],
      coral:          [255,127,80],
      cornflowerblue:      [100,149,237],
      cornsilk:        [255,248,220],
      crimson:        [220,20,60],
      cyan:          [0,255,255],
      darkblue:        [0,0,139],
      darkcyan:        [0,139,139],
      darkgoldenrod:      [184,134,11],
      darkgray:        [169,169,169],
      darkgreen:        [0,100,0],
      darkgrey:        [169,169,169],
      darkkhaki:        [189,183,107],
      darkmagenta:      [139,0,139],
      darkolivegreen:      [85,107,47],
      darkorange:        [255,140,0],
      darkorchid:        [153,50,204],
      darkred:        [139,0,0],
      darksalmon:        [233,150,122],
      darkseagreen:      [143,188,143],
      darkslateblue:      [72,61,139],
      darkslategray:      [47,79,79],
      darkslategrey:      [47,79,79],
      darkturquoise:      [0,206,209],
      darkviolet:        [148,0,211],
      deeppink:        [255,20,147],
      deepskyblue:      [0,191,255],
      dimgray:        [105,105,105],
      dimgrey:        [105,105,105],
      dodgerblue:        [30,144,255],
      firebrick:        [178,34,34],
      floralwhite:      [255,250,240],
      forestgreen:      [34,139,34],
      fuchsia:        [255,0,255],
      gainsboro:        [220,220,220],
      ghostwhite:        [248,248,255],
      gold:          [255,215,0],
      goldenrod:        [218,165,32],
      gray:          [128,128,128],
      grey:          [128,128,128],
      green:          [0,128,0],
      greenyellow:      [173,255,47],
      honeydew:        [240,255,240],
      hotpink:        [255,105,180],
      indianred:        [205,92,92],
      indigo:          [75,0,130],
      ivory:          [255,255,240],
      khaki:          [240,230,140],
      lavender:        [230,230,250],
      lavenderblush:      [255,240,245],
      lawngreen:        [124,252,0],
      lemonchiffon:      [255,250,205],
      lightblue:        [173,216,230],
      lightcoral:        [240,128,128],
      lightcyan:        [224,255,255],
      lightgoldenrodyellow:  [250,250,210],
      lightgray:        [211,211,211],
      lightgreen:        [144,238,144],
      lightgrey:        [211,211,211],
      lightpink:        [255,182,193],
      lightsalmon:      [255,160,122],
      lightseagreen:      [32,178,170],
      lightskyblue:      [135,206,250],
      lightslategray:      [119,136,153],
      lightslategrey:      [119,136,153],
      lightsteelblue:      [176,196,222],
      lightyellow:      [255,255,224],
      lime:          [0,255,0],
      limegreen:        [50,205,50],
      linen:          [250,240,230],
      magenta:        [255,0,255],
      maroon:          [128,0,0],
      mediumaquamarine:    [102,205,170],
      mediumblue:        [0,0,205],
      mediumorchid:      [186,85,211],
      mediumpurple:      [147,112,219],
      mediumseagreen:      [60,179,113],
      mediumslateblue:    [123,104,238],
      mediumspringgreen:    [0,250,154],
      mediumturquoise:    [72,209,204],
      mediumvioletred:    [199,21,133],
      midnightblue:      [25,25,112],
      mintcream:        [245,255,250],
      mistyrose:        [255,228,225],
      moccasin:        [255,228,181],
      navajowhite:      [255,222,173],
      navy:          [0,0,128],
      oldlace:        [253,245,230],
      olive:          [128,128,0],
      olivedrab:        [107,142,35],
      orange:          [255,165,0],
      orangered:        [255,69,0],
      orchid:          [218,112,214],
      palegoldenrod:      [238,232,170],
      palegreen:        [152,251,152],
      paleturquoise:      [175,238,238],
      palevioletred:      [219,112,147],
      papayawhip:        [255,239,213],
      peachpuff:        [255,218,185],
      peru:          [205,133,63],
      pink:          [255,192,203],
      plum:          [221,160,221],
      powderblue:        [176,224,230],
      purple:          [128,0,128],
      red:          [255,0,0],
      rosybrown:        [188,143,143],
      royalblue:        [65,105,225],
      saddlebrown:      [139,69,19],
      salmon:          [250,128,114],
      sandybrown:        [244,164,96],
      seagreen:        [46,139,87],
      seashell:        [255,245,238],
      sienna:          [160,82,45],
      silver:          [192,192,192],
      skyblue:        [135,206,235],
      slateblue:        [106,90,205],
      slategray:        [112,128,144],
      slategrey:        [112,128,144],
      snow:          [255,250,250],
      springgreen:      [0,255,127],
      steelblue:        [70,130,180],
      tan:          [210,180,140],
      teal:          [0,128,128],
      thistle:        [216,191,216],
      tomato:          [255,99,71],
      turquoise:        [64,224,208],
      violet:          [238,130,238],
      wheat:          [245,222,179],
      white:          [255,255,255],
      whitesmoke:        [245,245,245],
      yellow:          [255,255,0],
      yellowgreen:      [154,205,50]
    }
      
  };

  $$.util.regex = {};
  
  $$.util.regex.number = "(?:[-]?\\d*\\.\\d+|[-]?\\d+|[-]?\\d*\\.\\d+[eE]\\d+)";
  
  $$.util.regex.rgba = "rgb[a]?\\(("+ $$.util.regex.number +"[%]?)\\s*,\\s*("+ $$.util.regex.number +"[%]?)\\s*,\\s*("+ $$.util.regex.number +"[%]?)(?:\\s*,\\s*("+ $$.util.regex.number +"))?\\)";
  $$.util.regex.rgbaNoBackRefs = "rgb[a]?\\((?:"+ $$.util.regex.number +"[%]?)\\s*,\\s*(?:"+ $$.util.regex.number +"[%]?)\\s*,\\s*(?:"+ $$.util.regex.number +"[%]?)(?:\\s*,\\s*(?:"+ $$.util.regex.number +"))?\\)";
  
  $$.util.regex.hsla = "hsl[a]?\\(("+ $$.util.regex.number +")\\s*,\\s*("+ $$.util.regex.number +"[%])\\s*,\\s*("+ $$.util.regex.number +"[%])(?:\\s*,\\s*("+ $$.util.regex.number +"))?\\)";
  $$.util.regex.hslaNoBackRefs = "hsl[a]?\\((?:"+ $$.util.regex.number +")\\s*,\\s*(?:"+ $$.util.regex.number +"[%])\\s*,\\s*(?:"+ $$.util.regex.number +"[%])(?:\\s*,\\s*(?:"+ $$.util.regex.number +"))?\\)";
  
  $$.util.regex.hex3 = "\\#[0-9a-fA-F]{3}";
  $$.util.regex.hex6 = "\\#[0-9a-fA-F]{6}";

  var raf = !window ? null : ( window.requestAnimationFrame || window.mozRequestAnimationFrame ||  
        window.webkitRequestAnimationFrame || window.msRequestAnimationFrame );

  raf = raf || function(fn){ if(fn){ setTimeout(fn, 1000/60); } };

  $$.util.requestAnimationFrame = function(fn){
    raf( fn );
  };

})( cytoscape, typeof window === 'undefined' ? null : window  );

;(function($$){ 'use strict';
  
  $$.math = {};
  
  $$.math.signum = function(x){
    if( x > 0 ){
      return 1;
    } else if( x < 0 ){
      return -1;
    } else {
      return 0;
    }
  };

  $$.math.distance = function( p1, p2 ){
    var dx = p2.x - p1.x;
    var dy = p2.y - p1.y;

    return Math.sqrt( dx*dx + dy*dy );
  };

  // from http://en.wikipedia.org/wiki/Bézier_curve#Quadratic_curves
  $$.math.qbezierAt = function(p0, p1, p2, t){
    return (1 - t)*(1 - t)*p0 + 2*(1 - t)*t*p1 + t*t*p2;
  };

  $$.math.qbezierPtAt = function(p0, p1, p2, t){
    return {
      x: $$.math.qbezierAt( p0.x, p1.x, p2.x, t ),
      y: $$.math.qbezierAt( p0.y, p1.y, p2.y, t )
    };
  };

  $$.math.boundingBoxesIntersect = function( bb1, bb2 ){
    // case: one bb to right of other
    if( bb1.x1 > bb2.x2 ){ return false; }
    if( bb2.x1 > bb1.x2 ){ return false; }

    // case: one bb to left of other
    if( bb1.x2 < bb2.x1 ){ return false; }
    if( bb2.x2 < bb1.x1 ){ return false; }

    // case: one bb above other
    if( bb1.y2 < bb2.y1 ){ return false; }
    if( bb2.y2 < bb1.y1 ){ return false; }

    // case: one bb below other
    if( bb1.y1 > bb2.y2 ){ return false; }
    if( bb2.y1 > bb1.y2 ){ return false; }

    // otherwise, must have some overlap
    return true;
  };

  $$.math.inBoundingBox = function( bb, x, y ){
    return bb.x1 <= x && x <= bb.x2 && bb.y1 <= y && y <= bb.y2;
  };

  $$.math.pointInBoundingBox = function( bb, pt ){
    return this.inBoundingBox( bb, pt.x, pt.y );
  };

  $$.math.roundRectangleIntersectLine = function(
    x, y, nodeX, nodeY, width, height, padding) {
    
    var cornerRadius = this.getRoundRectangleRadius(width, height);
    
    var halfWidth = width / 2;
    var halfHeight = height / 2;
    
    // Check intersections with straight line segments
    var straightLineIntersections;
    
    // Top segment, left to right
    {
      var topStartX = nodeX - halfWidth + cornerRadius - padding;
      var topStartY = nodeY - halfHeight - padding;
      var topEndX = nodeX + halfWidth - cornerRadius + padding;
      var topEndY = topStartY;
      
      straightLineIntersections = this.finiteLinesIntersect(
        x, y, nodeX, nodeY, topStartX, topStartY, topEndX, topEndY, false);
      
      if (straightLineIntersections.length > 0) {
        return straightLineIntersections;
      }
    }
    
    // Right segment, top to bottom
    {
      var rightStartX = nodeX + halfWidth + padding;
      var rightStartY = nodeY - halfHeight + cornerRadius - padding;
      var rightEndX = rightStartX;
      var rightEndY = nodeY + halfHeight - cornerRadius + padding;
      
      straightLineIntersections = this.finiteLinesIntersect(
        x, y, nodeX, nodeY, rightStartX, rightStartY, rightEndX, rightEndY, false);
      
      if (straightLineIntersections.length > 0) {
        return straightLineIntersections;
      }
    }
    
    // Bottom segment, left to right
    {
      var bottomStartX = nodeX - halfWidth + cornerRadius - padding;
      var bottomStartY = nodeY + halfHeight + padding;
      var bottomEndX = nodeX + halfWidth - cornerRadius + padding;
      var bottomEndY = bottomStartY;
      
      straightLineIntersections = this.finiteLinesIntersect(
        x, y, nodeX, nodeY, bottomStartX, bottomStartY, bottomEndX, bottomEndY, false);
      
      if (straightLineIntersections.length > 0) {
        return straightLineIntersections;
      }
    }
    
    // Left segment, top to bottom
    {
      var leftStartX = nodeX - halfWidth - padding;
      var leftStartY = nodeY - halfHeight + cornerRadius - padding;
      var leftEndX = leftStartX;
      var leftEndY = nodeY + halfHeight - cornerRadius + padding;
      
      straightLineIntersections = this.finiteLinesIntersect(
        x, y, nodeX, nodeY, leftStartX, leftStartY, leftEndX, leftEndY, false);
      
      if (straightLineIntersections.length > 0) {
        return straightLineIntersections;
      }
    }
    
    // Check intersections with arc segments
    var arcIntersections;
    
    // Top Left
    {
      var topLeftCenterX = nodeX - halfWidth + cornerRadius;
      var topLeftCenterY = nodeY - halfHeight + cornerRadius;
      arcIntersections = this.intersectLineCircle(
        x, y, nodeX, nodeY, 
        topLeftCenterX, topLeftCenterY, cornerRadius + padding);
      
      // Ensure the intersection is on the desired quarter of the circle
      if (arcIntersections.length > 0
        && arcIntersections[0] <= topLeftCenterX
        && arcIntersections[1] <= topLeftCenterY) {
        return [arcIntersections[0], arcIntersections[1]];
      }
    }
    
    // Top Right
    {
      var topRightCenterX = nodeX + halfWidth - cornerRadius;
      var topRightCenterY = nodeY - halfHeight + cornerRadius;
      arcIntersections = this.intersectLineCircle(
        x, y, nodeX, nodeY, 
        topRightCenterX, topRightCenterY, cornerRadius + padding);
      
      // Ensure the intersection is on the desired quarter of the circle
      if (arcIntersections.length > 0
        && arcIntersections[0] >= topRightCenterX
        && arcIntersections[1] <= topRightCenterY) {
        return [arcIntersections[0], arcIntersections[1]];
      }
    }
    
    // Bottom Right
    {
      var bottomRightCenterX = nodeX + halfWidth - cornerRadius;
      var bottomRightCenterY = nodeY + halfHeight - cornerRadius;
      arcIntersections = this.intersectLineCircle(
        x, y, nodeX, nodeY, 
        bottomRightCenterX, bottomRightCenterY, cornerRadius + padding);
      
      // Ensure the intersection is on the desired quarter of the circle
      if (arcIntersections.length > 0
        && arcIntersections[0] >= bottomRightCenterX
        && arcIntersections[1] >= bottomRightCenterY) {
        return [arcIntersections[0], arcIntersections[1]];
      }
    }
    
    // Bottom Left
    {
      var bottomLeftCenterX = nodeX - halfWidth + cornerRadius;
      var bottomLeftCenterY = nodeY + halfHeight - cornerRadius;
      arcIntersections = this.intersectLineCircle(
        x, y, nodeX, nodeY, 
        bottomLeftCenterX, bottomLeftCenterY, cornerRadius + padding);
      
      // Ensure the intersection is on the desired quarter of the circle
      if (arcIntersections.length > 0
        && arcIntersections[0] <= bottomLeftCenterX
        && arcIntersections[1] >= bottomLeftCenterY) {
        return [arcIntersections[0], arcIntersections[1]];
      }
    }

    return []; // if nothing
  };
  
  $$.math.roundRectangleIntersectBox = function(
    boxX1, boxY1, boxX2, boxY2, width, height, centerX, centerY, padding) {
    
    // We have the following shpae
    
    //    _____
    //  _|     |_
    // |         |
    // |_       _|
    //   |_____|
    //
    // With a quarter circle at each corner.
    
    var cornerRadius = this.getRoundRectangleRadius(width, height);
    
    var hBoxTopLeftX = centerX - width / 2 - padding;
    var hBoxTopLeftY = centerY - height / 2 + cornerRadius - padding;
    var hBoxBottomRightX = centerX + width / 2 + padding;
    var hBoxBottomRightY = centerY + height / 2 - cornerRadius + padding;
    
    var vBoxTopLeftX = centerX - width / 2 + cornerRadius - padding;
    var vBoxTopLeftY = centerY - height / 2 - padding;
    var vBoxBottomRightX = centerX + width / 2 - cornerRadius + padding;
    var vBoxBottomRightY = centerY + height / 2 + padding;
    
    // Check if the box is out of bounds
    var boxMinX = Math.min(boxX1, boxX2);
    var boxMaxX = Math.max(boxX1, boxX2);
    var boxMinY = Math.min(boxY1, boxY2);
    var boxMaxY = Math.max(boxY1, boxY2);
    
    if (boxMaxX < hBoxTopLeftX) {
      return false;
    } else if (boxMinX > hBoxBottomRightX) {
      return false;
    }
    
    if (boxMaxY < vBoxTopLeftY) {
      return false;
    } else if (boxMinY > vBoxBottomRightY) {
      return false;
    }
    
    // Check if an hBox point is in given box
    if (hBoxTopLeftX >= boxMinX && hBoxTopLeftX <= boxMaxX
        && hBoxTopLeftY >= boxMinY && hBoxTopLeftY <= boxMaxY) {
      return true;
    }
    
    if (hBoxBottomRightX >= boxMinX && hBoxBottomRightX <= boxMaxX
        && hBoxTopLeftY >= boxMinY && hBoxTopLeftY <= boxMaxY) {
      return true;
    }
    
    if (hBoxBottomRightX >= boxMinX && hBoxBottomRightX <= boxMaxX
        && hBoxBottomRightY >= boxMinY && hBoxBottomRightY <= boxMaxY) {
      return true;
    }
    
    if (hBoxTopLeftX >= boxMinX && hBoxTopLeftX <= boxMaxX
        && hBoxBottomRightY >= boxMinY && hBoxBottomRightY <= boxMaxY) {
      return true;
    }
    
    // Check if a given point box is in the hBox
    if (boxMinX >= hBoxTopLeftX && boxMinX <= hBoxBottomRightX
      && boxMinY >= hBoxTopLeftY && boxMinY <= hBoxBottomRightY) {
      return true;
    }
    
    if (boxMaxX >= hBoxTopLeftX && boxMaxX <= hBoxBottomRightX
      && boxMinY >= hBoxTopLeftY && boxMinY <= hBoxBottomRightY) {
      return true;
    }
    
    if (boxMaxX >= hBoxTopLeftX && boxMaxX <= hBoxBottomRightX
      && boxMaxY >= hBoxTopLeftY && boxMaxY <= hBoxBottomRightY) {
      return true;
    }
    
    if (boxMinX >= hBoxTopLeftX && boxMinX <= hBoxBottomRightX
      && boxMaxY >= hBoxTopLeftY && boxMaxY <= hBoxBottomRightY) {
      return true;
    }
    
    // Check if an vBox point is in given box
    if (vBoxTopLeftX >= boxMinX && vBoxTopLeftX <= boxMaxX
        && vBoxTopLeftY >= boxMinY && vBoxTopLeftY <= boxMaxY) {
      return true;
    }
    
    if (vBoxBottomRightX >= boxMinX && vBoxBottomRightX <= boxMaxX
        && vBoxTopLeftY >= boxMinY && vBoxTopLeftY <= boxMaxY) {
      return true;
    }
    
    if (vBoxBottomRightX >= boxMinX && vBoxBottomRightX <= boxMaxX
        && vBoxBottomRightY >= boxMinY && vBoxBottomRightY <= boxMaxY) {
      return true;
    }
    
    if (vBoxTopLeftX >= boxMinX && vBoxTopLeftX <= boxMaxX
        && vBoxBottomRightY >= boxMinY && vBoxBottomRightY <= boxMaxY) {
      return true;
    }
    
    // Check if a given point box is in the vBox
    if (boxMinX >= vBoxTopLeftX && boxMinX <= vBoxBottomRightX
      && boxMinY >= vBoxTopLeftY && boxMinY <= vBoxBottomRightY) {
      return true;
    }
    
    if (boxMaxX >= vBoxTopLeftX && boxMaxX <= vBoxBottomRightX
      && boxMinY >= vBoxTopLeftY && boxMinY <= vBoxBottomRightY) {
      return true;
    }
    
    if (boxMaxX >= vBoxTopLeftX && boxMaxX <= vBoxBottomRightX
      && boxMaxY >= vBoxTopLeftY && boxMaxY <= vBoxBottomRightY) {
      return true;
    }
    
    if (boxMinX >= vBoxTopLeftX && boxMinX <= vBoxBottomRightX
      && boxMaxY >= vBoxTopLeftY && boxMaxY <= vBoxBottomRightY) {
      return true;
    }
    
    // Lastly, check if one of the ellipses coincide with the box
    
    if (this.boxIntersectEllipse(boxMinX, boxMinY, boxMaxX, boxMaxY, padding,
        cornerRadius * 2, cornerRadius * 2, vBoxTopLeftX + padding, hBoxTopLeftY + padding)) {
      return true;
    }
    
    if (this.boxIntersectEllipse(boxMinX, boxMinY, boxMaxX, boxMaxY, padding,
        cornerRadius * 2, cornerRadius * 2, vBoxBottomRightX - padding, hBoxTopLeftY + padding)) {
      return true;
    }
    
    if (this.boxIntersectEllipse(boxMinX, boxMinY, boxMaxX, boxMaxY, padding,
        cornerRadius * 2, cornerRadius * 2, vBoxBottomRightX - padding, hBoxBottomRightY - padding)) {
      return true;
    }
    
    if (this.boxIntersectEllipse(boxMinX, boxMinY, boxMaxX, boxMaxY, padding,
        cornerRadius * 2, cornerRadius * 2, vBoxTopLeftX + padding, hBoxBottomRightY - padding)) {
      return true;
    }
    
    return false;
  };
  
  // @O Approximate collision functions
  $$.math.checkInBoundingCircle = function(
    x, y, farthestPointSqDistance, padding, width, height, centerX, centerY) {
    
    x = (x - centerX) / (width + padding);
    y = (y - centerY) / (height + padding);
    
    return (x * x + y * y) <= farthestPointSqDistance;
  };
  
  $$.math.boxInBezierVicinity = function(
    x1box, y1box, x2box, y2box, x1, y1, x2, y2, x3, y3, tolerance) {
    
    // Return values:
    // 0 - curve is not in box
    // 1 - curve may be in box; needs precise check
    // 2 - curve is in box
    
    // midpoint
    var midX = 0.25 * x1 + 0.5 * x2 + 0.25 * x3;
    var midY = 0.25 * y1 + 0.5 * y2 + 0.25 * y3;

    var boxMinX = Math.min(x1box, x2box) - tolerance;
    var boxMinY = Math.min(y1box, y2box) - tolerance;
    var boxMaxX = Math.max(x1box, x2box) + tolerance;
    var boxMaxY = Math.max(y1box, y2box) + tolerance;
    
    if (x1 >= boxMinX && x1 <= boxMaxX && y1 >= boxMinY && y1 <= boxMaxY) { // (x1, y1) in box
      return 1;
    } else if (x3 >= boxMinX && x3 <= boxMaxX && y3 >= boxMinY && y3 <= boxMaxY) { // (x3, y3) in box
      return 1;
    } else if (midX >= boxMinX && midX <= boxMaxX && midY >= boxMinY && midY <= boxMaxY) { // (midX, midY) in box
      return 1;
    } else if (x2 >= boxMinX && x2 <= boxMaxX && y2 >= boxMinY && y2 <= boxMaxY) { // ctrl pt in box
      return 1;
    }
    
    var curveMinX = Math.min(x1, midX, x3);
    var curveMinY = Math.min(y1, midY, y3);
    var curveMaxX = Math.max(x1, midX, x3);
    var curveMaxY = Math.max(y1, midY, y3);
    
    /*
    console.log(curveMinX + ", " + curveMinY + ", " + curveMaxX 
      + ", " + curveMaxY);
    if (curveMinX == undefined) {
      console.log("undefined curveMinX: " + x1 + ", " + x2 + ", " + x3);
    }
    */
    
    if (curveMinX > boxMaxX
      || curveMaxX < boxMinX
      || curveMinY > boxMaxY
      || curveMaxY < boxMinY) {
      
      return 0;  
    }
    
    return 1;
  };

  $$.math.checkBezierInBox = function(
    x1box, y1box, x2box, y2box, x1, y1, x2, y2, x3, y3, tolerance) {

    function sampleInBox(t){
      var x = $$.math.qbezierAt(x1, x2, x3, t);
      var y = $$.math.qbezierAt(y1, y2, y3, t);

      return x1box <= x && x <= x2box
        && y1box <= y && y <= y2box
      ;
    }

    for( var t = 0; t <= 1; t += 0.25 ){
      if( !sampleInBox(t) ){
        return false;
      }
    }

    return true;
  };
  
  $$.math.checkStraightEdgeInBox = function(
    x1box, y1box, x2box, y2box, x1, y1, x2, y2, tolerance) {

    return x1box <= x1 && x1 <= x2box
      && x1box <= x2 && x2 <= x2box
      && y1box <= y1 && y1 <= y2box
      && y1box <= y2 && y2 <= y2box
    ;
  };

  $$.math.checkStraightEdgeCrossesBox = function(
    x1box, y1box, x2box, y2box, x1, y1, x2, y2, tolerance) {
    
   //console.log(arguments);
    
    var boxMinX = Math.min(x1box, x2box) - tolerance;
    var boxMinY = Math.min(y1box, y2box) - tolerance;
    var boxMaxX = Math.max(x1box, x2box) + tolerance;
    var boxMaxY = Math.max(y1box, y2box) + tolerance;
    
    // Check left + right bounds
    var aX = x2 - x1;
    var bX = x1;
    var yValue;
    
    // Top and bottom
    var aY = y2 - y1;
    var bY = y1;
    var xValue;
    
    if (Math.abs(aX) < 0.0001) {
      return (x1 >= boxMinX && x1 <= boxMaxX
        && Math.min(y1, y2) <= boxMinY
        && Math.max(y1, y2) >= boxMaxY);  
    }
    
    var tLeft = (boxMinX - bX) / aX;
    if (tLeft > 0 && tLeft <= 1) {
      yValue = aY * tLeft + bY;
      if (yValue >= boxMinY && yValue <= boxMaxY) {
        return true;
      } 
    }
    
    var tRight = (boxMaxX - bX) / aX;
    if (tRight > 0 && tRight <= 1) {
      yValue = aY * tRight + bY;
      if (yValue >= boxMinY && yValue <= boxMaxY) {
        return true;
      } 
    }
    
    var tTop = (boxMinY - bY) / aY;
    if (tTop > 0 && tTop <= 1) {
      xValue = aX * tTop + bX;
      if (xValue >= boxMinX && xValue <= boxMaxX) {
        return true;
      } 
    }
    
    var tBottom = (boxMaxY - bY) / aY;
    if (tBottom > 0 && tBottom <= 1) {
      xValue = aX * tBottom + bX;
      if (xValue >= boxMinX && xValue <= boxMaxX) {
        return true;
      } 
    }
    
    return false;
  };
  
  $$.math.checkBezierCrossesBox = function(
    x1box, y1box, x2box, y2box, x1, y1, x2, y2, x3, y3, tolerance) {
    
    var boxMinX = Math.min(x1box, x2box) - tolerance;
    var boxMinY = Math.min(y1box, y2box) - tolerance;
    var boxMaxX = Math.max(x1box, x2box) + tolerance;
    var boxMaxY = Math.max(y1box, y2box) + tolerance;
    
    if (x1 >= boxMinX && x1 <= boxMaxX && y1 >= boxMinY && y1 <= boxMaxY) {
      return true;
    } else if (x3 >= boxMinX && x3 <= boxMaxX && y3 >= boxMinY && y3 <= boxMaxY) {
      return true;
    }
    
    var aX = x1 - 2 * x2 + x3;
    var bX = -2 * x1 + 2 * x2;
    var cX = x1;

    var xIntervals = [];
    
    if (Math.abs(aX) < 0.0001) {
      var leftParam = (boxMinX - x1) / bX;
      var rightParam = (boxMaxX - x1) / bX;
      
      xIntervals.push(leftParam, rightParam);
    } else {
      // Find when x coordinate of the curve crosses the left side of the box
      var discriminantX1 = bX * bX - 4 * aX * (cX - boxMinX);
      var tX1, tX2;
      if (discriminantX1 > 0) {
        var sqrt = Math.sqrt(discriminantX1);
        tX1 = (-bX + sqrt) / (2 * aX);
        tX2 = (-bX - sqrt) / (2 * aX);
        
        xIntervals.push(tX1, tX2);
      }
      
      var discriminantX2 = bX * bX - 4 * aX * (cX - boxMaxX);
      var tX3, tX4;
      if (discriminantX2 > 0) {
        var sqrt = Math.sqrt(discriminantX2);
        tX3 = (-bX + sqrt) / (2 * aX);
        tX4 = (-bX - sqrt) / (2 * aX);
        
        xIntervals.push(tX3, tX4);
      }
    }
    
    xIntervals.sort(function(a, b) { return a - b; });
    
    var aY = y1 - 2 * y2 + y3;
    var bY = -2 * y1 + 2 * y2;
    var cY = y1;
    
    var yIntervals = [];
    
    if (Math.abs(aY) < 0.0001) {
      var topParam = (boxMinY - y1) / bY;
      var bottomParam = (boxMaxY - y1) / bY;
      
      yIntervals.push(topParam, bottomParam);
    } else {
      var discriminantY1 = bY * bY - 4 * aY * (cY - boxMinY);
      
      var tY1, tY2;
      if (discriminantY1 > 0) {
        var sqrt = Math.sqrt(discriminantY1);
        tY1 = (-bY + sqrt) / (2 * aY);
        tY2 = (-bY - sqrt) / (2 * aY);
        
        yIntervals.push(tY1, tY2);
      }
  
      var discriminantY2 = bY * bY - 4 * aY * (cY - boxMaxY);
      
      var tY3, tY4;
      if (discriminantY2 > 0) {
        var sqrt = Math.sqrt(discriminantY2);
        tY3 = (-bY + sqrt) / (2 * aY);
        tY4 = (-bY - sqrt) / (2 * aY);
        
        yIntervals.push(tY3, tY4);
      }
    }
        
    yIntervals.sort(function(a, b) { return a - b; });

    for (var index = 0; index < xIntervals.length; index += 2) {
      for (var yIndex = 1; yIndex < yIntervals.length; yIndex += 2) {
        
        // Check if there exists values for the Bezier curve
        // parameter between 0 and 1 where both the curve's
        // x and y coordinates are within the bounds specified by the box
        if (xIntervals[index] < yIntervals[yIndex]
          && yIntervals[yIndex] >= 0.0
          && xIntervals[index] <= 1.0
          && xIntervals[index + 1] > yIntervals[yIndex - 1]
          && yIntervals[yIndex - 1] <= 1.0
          && xIntervals[index + 1] >= 0.0) {
          
          return true;
        }
      }
    }
    
    return false;
  };
  
  $$.math.inLineVicinity = function(x, y, lx1, ly1, lx2, ly2, tolerance){
    var t = tolerance;

    var x1 = Math.min(lx1, lx2);
    var x2 = Math.max(lx1, lx2);
    var y1 = Math.min(ly1, ly2);
    var y2 = Math.max(ly1, ly2);

    return x1 - t <= x && x <= x2 + t
      && y1 - t <= y && y <= y2 + t;
  };

  $$.math.inBezierVicinity = function(
    x, y, x1, y1, x2, y2, x3, y3, toleranceSquared) {

    var bb = {
      x1: Math.min( x1, x3, x2 ),
      x2: Math.max( x1, x3, x2 ),
      y1: Math.min( y1, y3, y2 ),
      y2: Math.max( y1, y3, y2 )
    };

    // if outside the rough bounding box for the bezier, then it can't be a hit
    if( x < bb.x1 || x > bb.x2 || y < bb.y1 || y > bb.y2 ){
      // console.log('bezier out of rough bb')
      return false;
    } else {
      // console.log('do more expensive check');
      return true;
    }

  };
  
  $$.math.solveCubic = function(a, b, c, d, result) {
    
    // Solves a cubic function, returns root in form [r1, i1, r2, i2, r3, i3], where
    // r is the real component, i is the imaginary component

    // An implementation of the Cardano method from the year 1545
    // http://en.wikipedia.org/wiki/Cubic_function#The_nature_of_the_roots

    b /= a;
    c /= a;
    d /= a;
    
    var discriminant, q, r, dum1, s, t, term1, r13;

    q = (3.0 * c - (b * b)) / 9.0;
    r = -(27.0 * d) + b * (9.0 * c - 2.0 * (b * b));
    r /= 54.0;
    
    discriminant = q * q * q + r * r;
    result[1] = 0;
    term1 = (b / 3.0);
    
    if (discriminant > 0) {
      s = r + Math.sqrt(discriminant);
      s = ((s < 0) ? -Math.pow(-s, (1.0 / 3.0)) : Math.pow(s, (1.0 / 3.0)));
      t = r - Math.sqrt(discriminant);
      t = ((t < 0) ? -Math.pow(-t, (1.0 / 3.0)) : Math.pow(t, (1.0 / 3.0)));
      result[0] = -term1 + s + t;
      term1 += (s + t) / 2.0;
      result[4] = result[2] = -term1;
      term1 = Math.sqrt(3.0) * (-t + s) / 2;
      result[3] = term1;
      result[5] = -term1;
      return;
    }
    
    result[5] = result[3] = 0;
    
    if (discriminant === 0) {
      r13 = ((r < 0) ? -Math.pow(-r, (1.0 / 3.0)) : Math.pow(r, (1.0 / 3.0)));
      result[0] = -term1 + 2.0 * r13;
      result[4] = result[2] = -(r13 + term1);
      return;
    }
    
    q = -q;
    dum1 = q * q * q;
    dum1 = Math.acos(r / Math.sqrt(dum1));
    r13 = 2.0 * Math.sqrt(q);
    result[0] = -term1 + r13 * Math.cos(dum1 / 3.0);
    result[2] = -term1 + r13 * Math.cos((dum1 + 2.0 * Math.PI) / 3.0);
    result[4] = -term1 + r13 * Math.cos((dum1 + 4.0 * Math.PI) / 3.0);
    
    return;
  };

  $$.math.sqDistanceToQuadraticBezier = function(
    x, y, x1, y1, x2, y2, x3, y3) {
    
    // Find minimum distance by using the minimum of the distance 
    // function between the given point and the curve
    
    // This gives the coefficients of the resulting cubic equation
    // whose roots tell us where a possible minimum is
    // (Coefficients are divided by 4)
    
    var a = 1.0 * x1*x1 - 4*x1*x2 + 2*x1*x3 + 4*x2*x2 - 4*x2*x3 + x3*x3
      + y1*y1 - 4*y1*y2 + 2*y1*y3 + 4*y2*y2 - 4*y2*y3 + y3*y3;
    
    var b = 1.0 * 9*x1*x2 - 3*x1*x1 - 3*x1*x3 - 6*x2*x2 + 3*x2*x3
      + 9*y1*y2 - 3*y1*y1 - 3*y1*y3 - 6*y2*y2 + 3*y2*y3;
    
    var c = 1.0 * 3*x1*x1 - 6*x1*x2 + x1*x3 - x1*x + 2*x2*x2 + 2*x2*x - x3*x
      + 3*y1*y1 - 6*y1*y2 + y1*y3 - y1*y + 2*y2*y2 + 2*y2*y - y3*y;
      
    var d = 1.0 * x1*x2 - x1*x1 + x1*x - x2*x
      + y1*y2 - y1*y1 + y1*y - y2*y;
    
    // debug("coefficients: " + a / a + ", " + b / a + ", " + c / a + ", " + d / a);
    
    var roots = [];
    
    // Use the cubic solving algorithm
    this.solveCubic(a, b, c, d, roots);
    
    var zeroThreshold = 0.0000001;
    
    var params = [];
    
    for (var index = 0; index < 6; index += 2) {
      if (Math.abs(roots[index + 1]) < zeroThreshold
          && roots[index] >= 0
          && roots[index] <= 1.0) {
        params.push(roots[index]);
      }
    }
    
    params.push(1.0);
    params.push(0.0);
    
    var minDistanceSquared = -1;
    var closestParam;
    
    var curX, curY, distSquared;
    for (var i = 0; i < params.length; i++) {
      curX = Math.pow(1.0 - params[i], 2.0) * x1
        + 2.0 * (1 - params[i]) * params[i] * x2
        + params[i] * params[i] * x3;
        
      curY = Math.pow(1 - params[i], 2.0) * y1
        + 2 * (1.0 - params[i]) * params[i] * y2
        + params[i] * params[i] * y3;
        
      distSquared = Math.pow(curX - x, 2) + Math.pow(curY - y, 2);
      // debug('distance for param ' + params[i] + ": " + Math.sqrt(distSquared));
      if (minDistanceSquared >= 0) {
        if (distSquared < minDistanceSquared) {
          minDistanceSquared = distSquared;
          closestParam = params[i];
        }
      } else {
        minDistanceSquared = distSquared;
        closestParam = params[i];
      }
    }
    
    /*
    debugStats.clickX = x;
    debugStats.clickY = y;
    
    debugStats.closestX = Math.pow(1.0 - closestParam, 2.0) * x1
        + 2.0 * (1.0 - closestParam) * closestParam * x2
        + closestParam * closestParam * x3;
        
    debugStats.closestY = Math.pow(1.0 - closestParam, 2.0) * y1
        + 2.0 * (1.0 - closestParam) * closestParam * y2
        + closestParam * closestParam * y3;
    */
    
    // debug("given: " 
    //   + "( " + x + ", " + y + "), " 
    //   + "( " + x1 + ", " + y1 + "), " 
    //   + "( " + x2 + ", " + y2 + "), "
    //   + "( " + x3 + ", " + y3 + ")");
    
    
    // debug("roots: " + roots);
    // debug("params: " + params);
    // debug("closest param: " + closestParam);
    return minDistanceSquared;
  };
  
  $$.math.sqDistanceToFiniteLine = function(x, y, x1, y1, x2, y2) {
    var offset = [x - x1, y - y1];
    var line = [x2 - x1, y2 - y1];
    
    var lineSq = line[0] * line[0] + line[1] * line[1];
    var hypSq = offset[0] * offset[0] + offset[1] * offset[1];
    
    var dotProduct = offset[0] * line[0] + offset[1] * line[1];
    var adjSq = dotProduct * dotProduct / lineSq;
    
    if (dotProduct < 0) {
      return hypSq;
    }
    
    if (adjSq > lineSq) {
      return (x - x2) * (x - x2) + (y - y2) * (y - y2);
    }
    
    return hypSq - adjSq;
  };

  $$.math.pointInsidePolygon = function(
    x, y, basePoints, centerX, centerY, width, height, direction, padding) {

    //var direction = arguments[6];
    var transformedPoints = new Array(basePoints.length);

    // Gives negative angle
    var angle = Math.asin(direction[1] / (Math.sqrt(direction[0] * direction[0] 
      + direction[1] * direction[1])));
    
    if (direction[0] < 0) {
      angle = angle + Math.PI / 2;
    } else {
      angle = -angle - Math.PI / 2;
    }
        
    var cos = Math.cos(-angle);
    var sin = Math.sin(-angle);
    
//    console.log("base: " + basePoints);
    for (var i = 0; i < transformedPoints.length / 2; i++) {
      transformedPoints[i * 2] = 
        width / 2 * (basePoints[i * 2] * cos
          - basePoints[i * 2 + 1] * sin);
      
      transformedPoints[i * 2 + 1] = 
        height / 2 * (basePoints[i * 2 + 1] * cos 
          + basePoints[i * 2] * sin);

      transformedPoints[i * 2] += centerX;
      transformedPoints[i * 2 + 1] += centerY;
    }
    
    var points;
    
    if (padding > 0) {
      var expandedLineSet = this.expandPolygon(
        transformedPoints,
        -padding);
      
      points = this.joinLines(expandedLineSet);
    } else {
      points = transformedPoints;
    }
    
    var x1, y1, x2, y2;
    var y3;
    
    // Intersect with vertical line through (x, y)
    var up = 0;
    var down = 0;
    for (var i = 0; i < points.length / 2; i++) {
      
      x1 = points[i * 2];
      y1 = points[i * 2 + 1];
      
      if (i + 1 < points.length / 2) {
        x2 = points[(i + 1) * 2];
        y2 = points[(i + 1) * 2 + 1];
      } else {
        x2 = points[(i + 1 - points.length / 2) * 2];
        y2 = points[(i + 1 - points.length / 2) * 2 + 1];
      }
      
//*      console.log("line from (" + x1 + ", " + y1 + ") to (" + x2 + ", " + y2 + ")");

//&      console.log(x1, x, x2);

      if (x1 == x && x2 == x) {
        
      } else if ((x1 >= x && x >= x2)
        || (x1 <= x && x <= x2)) {
        
        y3 = (x - x1) / (x2 - x1) * (y2 - y1) + y1;
        
        if (y3 > y) {
          up++;
        }
        
        if (y3 < y) {
          down++;
        }
        
//*        console.log(y3, y);
        
      } else {
//*        console.log('22');
        continue;
      }
      
    }
    
//*    console.log("up: " + up + ", down: " + down);
    
    if (up % 2 === 0) {
      return false;
    } else {
      return true;
    }
  };

  $$.math.joinLines = function(lineSet) {
    
    var vertices = new Array(lineSet.length / 2);
    
    var currentLineStartX, currentLineStartY, currentLineEndX, currentLineEndY;
    var nextLineStartX, nextLineStartY, nextLineEndX, nextLineEndY;
    
    for (var i = 0; i < lineSet.length / 4; i++) {
      currentLineStartX = lineSet[i * 4];
      currentLineStartY = lineSet[i * 4 + 1];
      currentLineEndX = lineSet[i * 4 + 2];
      currentLineEndY = lineSet[i * 4 + 3];
      
      if (i < lineSet.length / 4 - 1) {
        nextLineStartX = lineSet[(i + 1) * 4];
        nextLineStartY = lineSet[(i + 1) * 4 + 1];
        nextLineEndX = lineSet[(i + 1) * 4 + 2];
        nextLineEndY = lineSet[(i + 1) * 4 + 3];
      } else {
        nextLineStartX = lineSet[0];
        nextLineStartY = lineSet[1];
        nextLineEndX = lineSet[2];
        nextLineEndY = lineSet[3];
      }
      
      var intersection = this.finiteLinesIntersect(
        currentLineStartX, currentLineStartY,
        currentLineEndX, currentLineEndY,
        nextLineStartX, nextLineStartY,
        nextLineEndX, nextLineEndY,
        true);
      
      vertices[i * 2] = intersection[0];
      vertices[i * 2 + 1] = intersection[1];
    }
    
    return vertices;
  };

  $$.math.expandPolygon = function(points, pad) {
    
    var expandedLineSet = new Array(points.length * 2);
    
    var currentPointX, currentPointY, nextPointX, nextPointY;
    
    for (var i = 0; i < points.length / 2; i++) {
      currentPointX = points[i * 2];
      currentPointY = points[i * 2 + 1];
      
      if (i < points.length / 2 - 1) {
        nextPointX = points[(i + 1) * 2];
        nextPointY = points[(i + 1) * 2 + 1];
      } else {
        nextPointX = points[0];
        nextPointY = points[1];
      }
      
      // Current line: [currentPointX, currentPointY] to [nextPointX, nextPointY]
      
      // Assume CCW polygon winding
      
      var offsetX = (nextPointY - currentPointY);
      var offsetY = -(nextPointX - currentPointX);
      
      // Normalize
      var offsetLength = Math.sqrt(offsetX * offsetX + offsetY * offsetY);
      var normalizedOffsetX = offsetX / offsetLength;
      var normalizedOffsetY = offsetY / offsetLength;
      
      expandedLineSet[i * 4] = currentPointX + normalizedOffsetX * pad;
      expandedLineSet[i * 4 + 1] = currentPointY + normalizedOffsetY * pad;
      expandedLineSet[i * 4 + 2] = nextPointX + normalizedOffsetX * pad;
      expandedLineSet[i * 4 + 3] = nextPointY + normalizedOffsetY * pad;
    }
    
    return expandedLineSet;
  };

  $$.math.intersectLineEllipse = function(
    x, y, centerX, centerY, ellipseWradius, ellipseHradius) {
    
    var dispX = centerX - x;
    var dispY = centerY - y;
    
    dispX /= ellipseWradius;
    dispY /= ellipseHradius;
    
    var len = Math.sqrt(dispX * dispX + dispY * dispY);
    
    var newLength = len - 1;
    
    if (newLength < 0) {
      return [];
    }
    
    var lenProportion = newLength / len;
    
    return [(centerX - x) * lenProportion + x, (centerY - y) * lenProportion + y];
  };
  
  $$.math.dotProduct = function(
    vec1, vec2) {
    
    if (vec1.length != 2 || vec2.length != 2) {
      throw 'dot product: arguments are not vectors';
    }
    
    return (vec1[0] * vec2[0] + vec1[1] * vec2[1]);
  };
  
  // Returns intersections of increasing distance from line's start point
  $$.math.intersectLineCircle = function(
    x1, y1, x2, y2, centerX, centerY, radius) {
    
    // Calculate d, direction vector of line
    var d = [x2 - x1, y2 - y1]; // Direction vector of line
    var c = [centerX, centerY]; // Center of circle
    var f = [x1 - centerX, y1 - centerY];
    
    var a = d[0] * d[0] + d[1] * d[1];
    var b = 2 * (f[0] * d[0] + f[1] * d[1]);
    var c = (f[0] * f[0] + f[1] * f[1]) - radius * radius ;
    
    var discriminant = b*b-4*a*c;
    
    if (discriminant < 0) {
      return [];
    }
    
    var t1 = (-b + Math.sqrt(discriminant)) / (2 * a);
    var t2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    
    var tMin = Math.min(t1, t2);
    var tMax = Math.max(t1, t2);
    var inRangeParams = [];
    
    if (tMin >= 0 && tMin <= 1) {
      inRangeParams.push(tMin);
    }
    
    if (tMax >= 0 && tMax <= 1) {
      inRangeParams.push(tMax);
    }
    
    if (inRangeParams.length === 0) {
      return [];
    }
    
    var nearIntersectionX = inRangeParams[0] * d[0] + x1;
    var nearIntersectionY = inRangeParams[0] * d[1] + y1;
    
    if (inRangeParams.length > 1) {
    
      if (inRangeParams[0] == inRangeParams[1]) {
        return [nearIntersectionX, nearIntersectionY];
      } else {
        
        var farIntersectionX = inRangeParams[1] * d[0] + x1;
        var farIntersectionY = inRangeParams[1] * d[1] + y1;
      
        return [nearIntersectionX, nearIntersectionY, farIntersectionX, farIntersectionY];
      }
      
    } else {
      return [nearIntersectionX, nearIntersectionY];
    }
    
  };
  
  $$.math.findCircleNearPoint = function(centerX, centerY, 
    radius, farX, farY) {
    
    var displacementX = farX - centerX;
    var displacementY = farY - centerY;
    var distance = Math.sqrt(displacementX * displacementX 
      + displacementY * displacementY);
    
    var unitDisplacementX = displacementX / distance;
    var unitDisplacementY = displacementY / distance;
    
    return [centerX + unitDisplacementX * radius, 
      centerY + unitDisplacementY * radius];
  };
  
  $$.math.findMaxSqDistanceToOrigin = function(points) {
    var maxSqDistance = 0.000001;
    var sqDistance;
    
    for (var i = 0; i < points.length / 2; i++) {
      
      sqDistance = points[i * 2] * points[i * 2] 
        + points[i * 2 + 1] * points[i * 2 + 1];
      
      if (sqDistance > maxSqDistance) {
        maxSqDistance = sqDistance;
      }
    }
    
    return maxSqDistance;
  };
  
  $$.math.finiteLinesIntersect = function(
    x1, y1, x2, y2, x3, y3, x4, y4, infiniteLines) {
    
    var ua_t = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3);
    var ub_t = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3);
    var u_b = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1);

    if (u_b !== 0) {
      var ua = ua_t / u_b;
      var ub = ub_t / u_b;
      
      if (0 <= ua && ua <= 1 && 0 <= ub && ub <= 1) {  
        return [x1 + ua * (x2 - x1), y1 + ua * (y2 - y1)];
        
      } else {
        if (!infiniteLines) {
          return [];
        } else {
          return [x1 + ua * (x2 - x1), y1 + ua * (y2 - y1)];
        }
      }
    } else {
      if (ua_t === 0 || ub_t === 0) {

        // Parallel, coincident lines. Check if overlap

        // Check endpoint of second line
        if ([x1, x2, x4].sort()[1] === x4) {
          return [x4, y4];
        }
        
        // Check start point of second line
        if ([x1, x2, x3].sort()[1] === x3) {
          return [x3, y3];
        }
        
        // Endpoint of first line
        if ([x3, x4, x2].sort()[1] === x2) {
          return [x2, y2];
        }
        
        return [];
      } else {
      
        // Parallel, non-coincident
        return [];
      }
    }
  };
  
  // (boxMinX, boxMinY, boxMaxX, boxMaxY, padding,
  //      cornerRadius * 2, cornerRadius * 2, vBoxTopLeftX + padding, hBoxTopLeftY + padding)) {
  
  $$.math.boxIntersectEllipse = function(
    x1, y1, x2, y2, padding, width, height, centerX, centerY) {
    
    if (x2 < x1) {
      var oldX1 = x1;
      x1 = x2;
      x2 = oldX1;
    }
    
    if (y2 < y1) {
      var oldY1 = y1;
      y1 = y2;
      y2 = oldY1;
    }
    
    // 4 ortho extreme points
    var west = [centerX - width / 2 - padding, centerY];
    var east = [centerX + width / 2 + padding, centerY];
    var north = [centerX, centerY - height / 2 - padding];
    var south = [centerX, centerY + height / 2 + padding];
    
    // out of bounds: return false
    if (x2 < west[0]) {
      return false;
    }
    
    if (x1 > east[0]) {
      return false;
    }
    
    if (y1 > south[1]) {
      return false;
    }
    
    if (y2 < north[1]) {
      return false;
    }
    
    // 1 of 4 ortho extreme points in box: return true
    if (x1 <= east[0] && east[0] <= x2
        && y1 <= east[1] && east[1] <= y2) {
      return true;
    }
    
    if (x1 <= west[0] && west[0] <= x2
        && y1 <= west[1] && west[1] <= y2) {
      return true;
    }
    
    if (x1 <= north[0] && north[0] <= x2
        && y1 <= north[1] && north[1] <= y2) {
      return true;
    }
    
    if (x1 <= south[0] && south[0] <= x2
        && y1 <= south[1] && south[1] <= y2) {
      return true;
    }
    
    // box corner in ellipse: return true    
    x1 = (x1 - centerX) / (width / 2 + padding);
    x2 = (x2 - centerX) / (width / 2 + padding);
    
    y1 = (y1 - centerY) / (height / 2 + padding);
    y2 = (y2 - centerY) / (height / 2 + padding);
    
    if (x1 * x1 + y1 * y1 <= 1) {
      return true;
    }
    
    if (x2 * x2 + y1 * y1 <= 1) {
      return true;
    }
    
    if (x2 * x2 + y2 * y2 <= 1) {
      return true;
    }
    
    if (x1 * x1 + y2 * y2 <= 1) {
      return true;
    }
    
    return false;
  };
  
  $$.math.boxIntersectPolygon = function(
    x1, y1, x2, y2, basePoints, width, height, centerX, centerY, direction, padding) {
    
//    console.log(arguments);
    
    if (x2 < x1) {
      var oldX1 = x1;
      x1 = x2;
      x2 = oldX1;
    }
    
    if (y2 < y1) {
      var oldY1 = y1;
      y1 = y2;
      y2 = oldY1;
    }
    
    var transformedPoints = new Array(basePoints.length);
    
    // Gives negative of angle
    var angle = Math.asin(direction[1] / (Math.sqrt(direction[0] * direction[0] 
      + direction[1] * direction[1])));
    
    if (direction[0] < 0) {
      angle = angle + Math.PI / 2;
    } else {
      angle = -angle - Math.PI / 2;
    }
    
    var cos = Math.cos(-angle);
    var sin = Math.sin(-angle);
    
    for (var i = 0; i < transformedPoints.length / 2; i++) {
      transformedPoints[i * 2] = 
        width / 2 * (basePoints[i * 2] * cos
          - basePoints[i * 2 + 1] * sin);
      
      transformedPoints[i * 2 + 1] = 
        height / 2 * (basePoints[i * 2 + 1] * cos 
          + basePoints[i * 2] * sin);
      
      transformedPoints[i * 2] += centerX;
      transformedPoints[i * 2 + 1] += centerY;
    }
    
    // Assume transformedPoints.length > 0, and check if intersection is possible
    var minTransformedX = transformedPoints[0];
    var maxTransformedX = transformedPoints[0];
    var minTransformedY = transformedPoints[1];
    var maxTransformedY = transformedPoints[1];
    
    for (var i = 1; i < transformedPoints.length / 2; i++) {
      if (transformedPoints[i * 2] > maxTransformedX) {
        maxTransformedX = transformedPoints[i * 2];
      }
      
      if (transformedPoints[i * 2] < minTransformedX) {
        minTransformedX = transformedPoints[i * 2];
      }
      
      if (transformedPoints[i * 2 + 1] > maxTransformedY) {
        maxTransformedY = transformedPoints[i * 2 + 1];
      }
      
      if (transformedPoints[i * 2 + 1] < minTransformedY) {
        minTransformedY = transformedPoints[i * 2 + 1];
      }
    }
    
    if (x2 < minTransformedX - padding) {
      return false;
    }
    
    if (x1 > maxTransformedX + padding) {
      return false;
    }
    
    if (y2 < minTransformedY - padding) {
      return false;
    }
    
    if (y1 > maxTransformedY + padding) {
      return false;
    }
    
    // Continue checking with padding-corrected points
    var points;
    
    if (padding > 0) {
      var expandedLineSet = $$.math.expandPolygon(
        transformedPoints,
        -padding);
      
      points = $$.math.joinLines(expandedLineSet);
    } else {
      points = transformedPoints;
    }
    
    // Check if a point is in box
    for (var i = 0; i < transformedPoints.length / 2; i++) {
      if (x1 <= transformedPoints[i * 2]
          && transformedPoints[i * 2] <= x2) {
        
        if (y1 <= transformedPoints[i * 2 + 1]
            && transformedPoints[i * 2 + 1] <= y2) {
          
          return true;
        }
      }
    }
    
    
    // Check for intersections with the selection box
    for (var i = 0; i < points.length / 2; i++) {
      
      var currentX = points[i * 2];
      var currentY = points[i * 2 + 1];
      var nextX;
      var nextY;
      
      if (i < points.length / 2 - 1) {
        nextX = points[(i + 1) * 2];
        nextY = points[(i + 1) * 2 + 1];
      } else {
        nextX = points[0];
        nextY = points[1];
      }
      
      // Intersection with top of selection box
      if ($$.math.finiteLinesIntersect(currentX, currentY, nextX, nextY, x1, y1, x2, y1, false).length > 0) {
        return true;
      }
      
      // Intersection with bottom of selection box
      if ($$.math.finiteLinesIntersect(currentX, currentY, nextX, nextY, x1, y2, x2, y2, false).length > 0) {
        return true;
      }
      
      // Intersection with left side of selection box
      if ($$.math.finiteLinesIntersect(currentX, currentY, nextX, nextY, x1, y1, x1, y2, false).length > 0) {
        return true;
      }
      
      // Intersection with right side of selection box
      if ($$.math.finiteLinesIntersect(currentX, currentY, nextX, nextY, x2, y1, x2, y2, false).length > 0) {
        return true;
      }
    }

    /*
    // Check if box corner in the polygon
    if ($$.math.pointInsidePolygon(
      x1, y1, points, 0, 0, 1, 1, 0, direction)) {
      
      return true;
    } else if ($$.math.pointInsidePolygon(
      x1, y2, points, 0, 0, 1, 1, 0, direction)) {
      
      return true;
    } else if ($$.math.pointInsidePolygon(
      x2, y2, points, 0, 0, 1, 1, 0, direction)) {
       
      return true; 
    } else if ($$.math.pointInsidePolygon(
      x2, y1, points, 0, 0, 1, 1, 0, direction)) {
      
      return true;
    }
    */
    return false;
  };
  
  $$.math.polygonIntersectLine = function(
    x, y, basePoints, centerX, centerY, width, height, padding) {
    
    var intersections = [];
    var intersection;
    
    var transformedPoints = new Array(basePoints.length);
    
    for (var i = 0; i < transformedPoints.length / 2; i++) {
      transformedPoints[i * 2] = basePoints[i * 2] * width + centerX;
      transformedPoints[i * 2 + 1] = basePoints[i * 2 + 1] * height + centerY;
    }
    
    var points;
    
    if (padding > 0) {
      var expandedLineSet = $$.math.expandPolygon(
        transformedPoints,
        -padding);
      
      points = $$.math.joinLines(expandedLineSet);
    } else {
      points = transformedPoints;
    }
    // var points = transformedPoints;
    
    var currentX, currentY, nextX, nextY;
    
    for (var i = 0; i < points.length / 2; i++) {
    
      currentX = points[i * 2];
      currentY = points[i * 2 + 1];

      if (i < points.length / 2 - 1) {
        nextX = points[(i + 1) * 2]; 
        nextY = points[(i + 1) * 2 + 1];
      } else {
        nextX = points[0]; 
        nextY = points[1];
      }
      
      intersection = this.finiteLinesIntersect(
        x, y, centerX, centerY,
        currentX, currentY,
        nextX, nextY);
      
      if (intersection.length !== 0) {
        intersections.push(intersection[0], intersection[1]);
      }
    }
    
    return intersections;
  };
  
  $$.math.shortenIntersection = function(
    intersection, offset, amount) {
    
    var disp = [intersection[0] - offset[0], intersection[1] - offset[1]];
    
    var length = Math.sqrt(disp[0] * disp[0] + disp[1] * disp[1]);
    
    var lenRatio = (length - amount) / length;
    
    if (lenRatio < 0) {
      lenRatio = 0.00001;
    }

    return [offset[0] + lenRatio * disp[0], offset[1] + lenRatio * disp[1]];
  };

  $$.math.generateUnitNgonPointsFitToSquare = function(sides, rotationRadians) {
    var points = $$.math.generateUnitNgonPoints(sides, rotationRadians);
    points = $$.math.fitPolygonToSquare(points);

    return points;
  };

  $$.math.fitPolygonToSquare = function(points){
    var x, y;
    var sides = points.length/2;
    var minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;

    for (var i = 0; i < sides; i++) {
      x = points[2 * i];
      y = points[2 * i + 1];

      minX = Math.min( minX, x );
      maxX = Math.max( maxX, x );
      minY = Math.min( minY, y );
      maxY = Math.max( maxY, y );
    }
    
    // stretch factors
    var sx = 2 / (maxX - minX);
    var sy = 2 / (maxY - minY);

    for (var i = 0; i < sides; i++){
      x = points[2 * i] = points[2 * i] * sx;
      y = points[2 * i + 1] = points[2 * i + 1] * sy;

      minX = Math.min( minX, x );
      maxX = Math.max( maxX, x );
      minY = Math.min( minY, y );
      maxY = Math.max( maxY, y );
    }

    if( minY < -1 ){
      for (var i = 0; i < sides; i++){
        y = points[2 * i + 1] = points[2 * i + 1] + (-1 -minY);
      }
    }
    
    return points;
  };

  $$.math.generateUnitNgonPoints = function(sides, rotationRadians) {
    
    var increment = 1.0 / sides * 2 * Math.PI;
    var startAngle = sides % 2 === 0 ? 
      Math.PI / 2.0 + increment / 2.0 : Math.PI / 2.0;
//    console.log(nodeShapes['square']);
    startAngle += rotationRadians;
    
    var points = new Array(sides * 2);

    var currentAngle, x, y;
    for (var i = 0; i < sides; i++) {
      currentAngle = i * increment + startAngle;
      
      x = points[2 * i] = Math.cos(currentAngle);// * (1 + i/2);
      y = points[2 * i + 1] = Math.sin(-currentAngle);//  * (1 + i/2);
    }
    
    return points;
  };

  $$.math.getRoundRectangleRadius = function(width, height) {
    
    // Set the default radius, unless half of width or height is smaller than default
    return Math.min(width / 4, height / 4, 8);
  };
  
})( cytoscape );

;(function($$){ 'use strict';
  
  // registered extensions to cytoscape, indexed by name
  var extensions = {};
  $$.extensions = extensions;
  
  // registered modules for extensions, indexed by name
  var modules = {};
  $$.modules = modules;
  
  function setExtension(type, name, registrant){
    var impl = {};
    impl[name] = registrant;
    
    switch( type ){
    case 'core':
    case 'collection':
      $$.fn[type]( impl );
    }
    
    // fill in missing layout functions in the prototype
    if( type === 'layout' ){
      var layoutProto = registrant.prototype;
      var optLayoutFns = ['stop'];

      for( var i = 0; i < optLayoutFns.length; i++ ){
        var fnName = optLayoutFns[i];

        layoutProto[fnName] = layoutProto[fnName] || function(){ return this; };
      }

      // either .start() or .run() is defined, so autogen the other
      if( layoutProto.start && !layoutProto.run ){
        layoutProto.run = function(){ this.start(); return this; };
      } else if( !layoutProto.start && layoutProto.run ){
        layoutProto.start = function(){ this.run(); return this; };
      }

      layoutProto.on = $$.define.on({ layout: true });
      layoutProto.one = $$.define.on({ layout: true, unbindSelfOnTrigger: true });
      layoutProto.once = $$.define.on({ layout: true, unbindAllBindersOnTrigger: true });
      layoutProto.off = $$.define.off({ layout: true });
      layoutProto.trigger = $$.define.trigger({ layout: true });

      // aliases for those folks who like old stuff:
      layoutProto.bind = layoutProto.on;
      layoutProto.unbind = layoutProto.off;
    }

    return $$.util.setMap({
      map: extensions,
      keys: [ type, name ],
      value: registrant
    });
  }
  
  function getExtension(type, name){
    return $$.util.getMap({
      map: extensions,
      keys: [ type, name ]
    });
  }
  
  function setModule(type, name, moduleType, moduleName, registrant){
    return $$.util.setMap({
      map: modules,
      keys: [ type, name, moduleType, moduleName ],
      value: registrant
    });
  }
  
  function getModule(type, name, moduleType, moduleName){
    return $$.util.getMap({
      map: modules,
      keys: [ type, name, moduleType, moduleName ]
    });
  }
  
  $$.extension = function(){
    // e.g. $$.extension('renderer', 'svg')
    if( arguments.length == 2 ){
      return getExtension.apply(this, arguments);
    }
    
    // e.g. $$.extension('renderer', 'svg', { ... })
    else if( arguments.length == 3 ){
      return setExtension.apply(this, arguments);
    }
    
    // e.g. $$.extension('renderer', 'svg', 'nodeShape', 'ellipse')
    else if( arguments.length == 4 ){
      return getModule.apply(this, arguments);
    }
    
    // e.g. $$.extension('renderer', 'svg', 'nodeShape', 'ellipse', { ... })
    else if( arguments.length == 5 ){
      return setModule.apply(this, arguments);
    }
    
    else {
      $$.util.error('Invalid extension access syntax');
    }
  
  };
  
})( cytoscape );

;(function($, $$){ 'use strict';
  
  if( !$ ){ return; } // no jquery => don't need this

  var cyReg = function( $ele ){
    var d = $ele[0]._cyreg = $ele[0]._cyreg || {};

    return d;
  };

  // allow calls on a jQuery selector by proxying calls to $.cytoscape
  // e.g. $("#foo").cytoscape(options) => $.cytoscape(options) on #foo
  $.fn.cytoscape = function(opts){
    var $this = $(this);

    // get object
    if( opts === 'get' ){
      return cyReg( $this ).cy;
    }
    
    // bind to ready
    else if( $$.is.fn(opts) ){

      var ready = opts;
      var cy = cyReg( $this ).cy;
      
      if( cy && cy.isReady() ){ // already ready so just trigger now
        cy.trigger('ready', [], ready);

      } else { // not yet ready, so add to readies list
        var data = cyReg( $this );
        var readies = data.readies = data.readies || [];

        readies.push( ready );
      } 
      
    }
    
    // proxy to create instance
    else if( $$.is.plainObject(opts) ){
      return $this.each(function(){
        var options = $.extend({}, opts, {
          container: $(this)[0]
        });
      
        cytoscape(options);
      });
    }
  };
  
  // allow access to the global cytoscape object under jquery for legacy reasons
  $.cytoscape = cytoscape;
  
  // use short alias (cy) if not already defined
  if( $.fn.cy == null && $.cy == null ){
    $.fn.cy = $.fn.cytoscape;
    $.cy = $.cytoscape;
  }
  
})(typeof jQuery !== 'undefined' ? jQuery : null , cytoscape);

;(function($$){ 'use strict';
  
  // shamelessly taken from jQuery
  // https://github.com/jquery/jquery/blob/master/src/event.js

  $$.Event = function( src, props ) {
    // Allow instantiation without the 'new' keyword
    if ( !(this instanceof $$.Event) ) {
      return new $$.Event( src, props );
    }

    // Event object
    if ( src && src.type ) {
      this.originalEvent = src;
      this.type = src.type;

      // Events bubbling up the document may have been marked as prevented
      // by a handler lower down the tree; reflect the correct value.
      this.isDefaultPrevented = ( src.defaultPrevented ) ? returnTrue : returnFalse;

    // Event type
    } else {
      this.type = src;
    }

    // Put explicitly provided properties onto the event object
    if ( props ) {
      // $$.util.extend( this, props );

      // more efficient to manually copy fields we use
      this.type = props.type !== undefined ? props.type : this.type;
      this.cy = props.cy;
      this.cyTarget = props.cyTarget;
      this.cyPosition = props.cyPosition;
      this.cyRenderedPosition = props.cyRenderedPosition;
      this.namespace = props.namespace;
      this.layout = props.layout;
      this.data = props.data;
    }

    // Create a timestamp if incoming event doesn't have one
    this.timeStamp = src && src.timeStamp || +new Date();
  };

  function returnFalse() {
    return false;
  }
  function returnTrue() {
    return true;
  }

  // jQuery.Event is based on DOM3 Events as specified by the ECMAScript Language Binding
  // http://www.w3.org/TR/2003/WD-DOM-Level-3-Events-20030331/ecma-script-binding.html
  $$.Event.prototype = {
    preventDefault: function() {
      this.isDefaultPrevented = returnTrue;

      var e = this.originalEvent;
      if ( !e ) {
        return;
      }

      // if preventDefault exists run it on the original event
      if ( e.preventDefault ) {
        e.preventDefault();
      }
    },
    stopPropagation: function() {
      this.isPropagationStopped = returnTrue;

      var e = this.originalEvent;
      if ( !e ) {
        return;
      }
      // if stopPropagation exists run it on the original event
      if ( e.stopPropagation ) {
        e.stopPropagation();
      }
    },
    stopImmediatePropagation: function() {
      this.isImmediatePropagationStopped = returnTrue;
      this.stopPropagation();
    },
    isDefaultPrevented: returnFalse,
    isPropagationStopped: returnFalse,
    isImmediatePropagationStopped: returnFalse
  };
  
  
})( cytoscape );

;(function($$){ 'use strict';

  // use this module to cherry pick functions into your prototype
  // (useful for functions shared between the core and collections, for example)

  // e.g.
  // $$.fn.collection({
  //   foo: $$.define.foo({ /* params... */ })
  // });

  $$.define = {

    // access data field
    data: function( params ){
      var defaults = { 
        field: 'data',
        bindingEvent: 'data',
        allowBinding: false,
        allowSetting: false,
        allowGetting: false,
        settingEvent: 'data',
        settingTriggersEvent: false,
        triggerFnName: 'trigger',
        immutableKeys: {}, // key => true if immutable
        updateStyle: false,
        onSet: function( self ){},
        canSet: function( self ){ return true; }
      };
      params = $$.util.extend({}, defaults, params);

      return function dataImpl( name, value ){
        var p = params;
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var single = selfIsArrayLike ? self[0] : self;

        // .data('foo', ...)
        if( $$.is.string(name) ){ // set or get property

          // .data('foo')
          if( p.allowGetting && value === undefined ){ // get

            var ret;
            if( single ){
              ret = single._private[ p.field ][ name ];
            }
            return ret;
          
          // .data('foo', 'bar')
          } else if( p.allowSetting && value !== undefined ) { // set
            var valid = !p.immutableKeys[name];
            if( valid ){
              for( var i = 0, l = all.length; i < l; i++ ){
                if( p.canSet( all[i] ) ){
                  all[i]._private[ p.field ][ name ] = value;
                }
              }

              // update mappers if asked
              if( p.updateStyle ){ self.updateStyle(); }

              // call onSet callback
              p.onSet( self );

              if( p.settingTriggersEvent ){
                self[ p.triggerFnName ]( p.settingEvent );
              }
            }
          }

        // .data({ 'foo': 'bar' })
        } else if( p.allowSetting && $$.is.plainObject(name) ){ // extend
          var obj = name;
          var k, v;

          for( k in obj ){
            v = obj[ k ];

            var valid = !p.immutableKeys[k];
            if( valid ){
              for( var i = 0, l = all.length; i < l; i++ ){
                if( p.canSet( all[i] ) ){
                  all[i]._private[ p.field ][ k ] = v;
                }
              }
            }
          }
          
          // update mappers if asked
          if( p.updateStyle ){ self.updateStyle(); }

          // call onSet callback
          p.onSet( self );

          if( p.settingTriggersEvent ){
            self[ p.triggerFnName ]( p.settingEvent );
          }
        
        // .data(function(){ ... })
        } else if( p.allowBinding && $$.is.fn(name) ){ // bind to event
          var fn = name;
          self.bind( p.bindingEvent, fn );
        
        // .data()
        } else if( p.allowGetting && name === undefined ){ // get whole object
          var ret;
          if( single ){
            ret = single._private[ p.field ];
          }
          return ret;
        }

        return self; // maintain chainability
      }; // function
    }, // data

    // remove data field
    removeData: function( params ){
      var defaults = { 
        field: 'data',
        event: 'data',
        triggerFnName: 'trigger',
        triggerEvent: false,
        immutableKeys: {} // key => true if immutable
      };
      params = $$.util.extend({}, defaults, params);

      return function removeDataImpl( names ){
        var p = params;
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        
        // .removeData('foo bar')
        if( $$.is.string(names) ){ // then get the list of keys, and delete them
          var keys = names.split(/\s+/);
          var l = keys.length;

          for( var i = 0; i < l; i++ ){ // delete each non-empty key
            var key = keys[i];
            if( $$.is.emptyString(key) ){ continue; }

            var valid = !p.immutableKeys[ key ]; // not valid if immutable
            if( valid ){
              for( var i_a = 0, l_a = all.length; i_a < l_a; i_a++ ){
                all[ i_a ]._private[ p.field ][ key ] = undefined;
              }
            }
          }

          if( p.triggerEvent ){
            self[ p.triggerFnName ]( p.event );
          }

        // .removeData()
        } else if( names === undefined ){ // then delete all keys

          for( var i_a = 0, l_a = all.length; i_a < l_a; i_a++ ){
            var _privateFields = all[ i_a ]._private[ p.field ];
            
            for( var key in _privateFields ){
              var validKeyToDelete = !p.immutableKeys[ key ];

              if( validKeyToDelete ){
                _privateFields[ key ] = undefined;
              }
            }
          }

          if( p.triggerEvent ){
            self[ p.triggerFnName ]( p.event );
          }
        }

        return self; // maintain chaining
      }; // function
    }, // removeData

    // event function reusable stuff
    event: {
      regex: /(\w+)(\.\w+)?/, // regex for matching event strings (e.g. "click.namespace")
      optionalTypeRegex: /(\w+)?(\.\w+)?/,
      falseCallback: function(){ return false; }
    },

    // event binding
    on: function( params ){
      var defaults = {
        unbindSelfOnTrigger: false,
        unbindAllBindersOnTrigger: false
      };
      params = $$.util.extend({}, defaults, params);
      
      return function onImpl(events, selector, data, callback){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var eventsIsString = $$.is.string(events);
        var p = params;

        if( $$.is.plainObject(selector) ){ // selector is actually data
          callback = data;
          data = selector;
          selector = undefined;
        } else if( $$.is.fn(selector) || selector === false ){ // selector is actually callback
          callback = selector;
          data = undefined;
          selector = undefined;
        }

        if( $$.is.fn(data) || data === false ){ // data is actually callback
          callback = data;
          data = undefined;
        }

        // if there isn't a callback, we can't really do anything
        // (can't speak for mapped events arg version)
        if( !($$.is.fn(callback) || callback === false) && eventsIsString ){
          return self; // maintain chaining
        }

        if( eventsIsString ){ // then convert to map
          var map = {};
          map[ events ] = callback;
          events = map;
        }

        for( var evts in events ){
          callback = events[evts];
          if( callback === false ){
            callback = $$.define.event.falseCallback;
          }

          if( !$$.is.fn(callback) ){ continue; }

          evts = evts.split(/\s+/);
          for( var i = 0; i < evts.length; i++ ){
            var evt = evts[i];
            if( $$.is.emptyString(evt) ){ continue; }

            var match = evt.match( $$.define.event.regex ); // type[.namespace]

            if( match ){
              var type = match[1];
              var namespace = match[2] ? match[2] : undefined;

              var listener = {
                callback: callback, // callback to run
                data: data, // extra data in eventObj.data
                delegated: selector ? true : false, // whether the evt is delegated
                selector: selector, // the selector to match for delegated events
                selObj: new $$.Selector(selector), // cached selector object to save rebuilding
                type: type, // the event type (e.g. 'click')
                namespace: namespace, // the event namespace (e.g. ".foo")
                unbindSelfOnTrigger: p.unbindSelfOnTrigger,
                unbindAllBindersOnTrigger: p.unbindAllBindersOnTrigger,
                binders: all // who bound together
              };

              for( var j = 0; j < all.length; j++ ){
                all[j]._private.listeners.push( listener );
              }
            }
          } // for events array
        } // for events map
        
        return self; // maintain chaining
      }; // function
    }, // on

    off: function offImpl( params ){
      var defaults = {
      };
      params = $$.util.extend({}, defaults, params);
      
      return function(events, selector, callback){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var eventsIsString = $$.is.string(events);

        if( arguments.length === 0 ){ // then unbind all

          for( var i = 0; i < all.length; i++ ){
            all[i]._private.listeners = [];
          }

          return self; // maintain chaining
        }

        if( $$.is.fn(selector) || selector === false ){ // selector is actually callback
          callback = selector;
          selector = undefined;
        }

        if( eventsIsString ){ // then convert to map
          var map = {};
          map[ events ] = callback;
          events = map;
        }

        for( var evts in events ){
          callback = events[evts];

          if( callback === false ){
            callback = $$.define.event.falseCallback;
          }

          evts = evts.split(/\s+/);
          for( var h = 0; h < evts.length; h++ ){
            var evt = evts[h];
            if( $$.is.emptyString(evt) ){ continue; }

            var match = evt.match( $$.define.event.optionalTypeRegex ); // [type][.namespace]
            if( match ){
              var type = match[1] ? match[1] : undefined;
              var namespace = match[2] ? match[2] : undefined;

              for( var i = 0; i < all.length; i++ ){ //
                var listeners = all[i]._private.listeners;

                for( var j = 0; j < listeners.length; j++ ){
                  var listener = listeners[j];
                  var nsMatches = !namespace || namespace === listener.namespace;
                  var typeMatches = !type || listener.type === type;
                  var cbMatches = !callback || callback === listener.callback;
                  var listenerMatches = nsMatches && typeMatches && cbMatches;

                  // delete listener if it matches
                  if( listenerMatches ){
                    listeners.splice(j, 1);
                    j--;
                  }
                } // for listeners
              } // for all
            } // if match
          } // for events array

        } // for events map
        
        return self; // maintain chaining
      }; // function
    }, // off

    trigger: function( params ){
      var defaults = {};
      params = $$.util.extend({}, defaults, params);
      
      return function triggerImpl(events, extraParams, fnToTrigger){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var eventsIsString = $$.is.string(events);
        var eventsIsObject = $$.is.plainObject(events);
        var eventsIsEvent = $$.is.event(events);
        var cy = this._private.cy || this;
        var hasCompounds = cy.hasCompoundNodes();

        if( eventsIsString ){ // then make a plain event object for each event name
          var evts = events.split(/\s+/);
          events = [];

          for( var i = 0; i < evts.length; i++ ){
            var evt = evts[i];
            if( $$.is.emptyString(evt) ){ continue; }

            var match = evt.match( $$.define.event.regex ); // type[.namespace]
            var type = match[1];
            var namespace = match[2] ? match[2] : undefined;

            events.push( {
              type: type,
              namespace: namespace
            } );
          }
        } else if( eventsIsObject ){ // put in length 1 array
          var eventArgObj = events;

          events = [ eventArgObj ];
        }

        if( extraParams ){
          if( !$$.is.array(extraParams) ){ // make sure extra params are in an array if specified
            extraParams = [ extraParams ];
          }
        } else { // otherwise, we've got nothing
          extraParams = [];
        }

        for( var i = 0; i < events.length; i++ ){ // trigger each event in order
          var evtObj = events[i];
          
          for( var j = 0; j < all.length; j++ ){ // for each
            var triggerer = all[j];
            var listeners = triggerer._private.listeners;
            var triggererIsElement = $$.is.element(triggerer);
            var bubbleUp = triggererIsElement || params.layout;

            // create the event for this element from the event object
            var evt;

            if( eventsIsEvent ){ // then just get the object
              evt = evtObj;
              
              evt.cyTarget = evt.cyTarget || triggerer;
              evt.cy = evt.cy || cy;

            } else { // then we have to make one
              evt = new $$.Event( evtObj, {
                cyTarget: triggerer,
                cy: cy,
                namespace: evtObj.namespace
              } );
            }

            // if a layout was specified, then put it in the typed event
            if( evtObj.layout ){
              evt.layout = evtObj.layout;
            }

            // if triggered by layout, put in event
            if( params.layout ){
              evt.layout = triggerer;
            }

            // create a rendered position based on the passed position
            if( evt.cyPosition ){
              var pos = evt.cyPosition;
              var zoom = cy.zoom();
              var pan = cy.pan();

              evt.cyRenderedPosition = {
                x: pos.x * zoom + pan.x,
                y: pos.y * zoom + pan.y
              };
            }

            if( fnToTrigger ){ // then override the listeners list with just the one we specified
              listeners = [{
                namespace: evt.namespace,
                type: evt.type,
                callback: fnToTrigger
              }];
            }

            for( var k = 0; k < listeners.length; k++ ){ // check each listener
              var lis = listeners[k];
              var nsMatches = !lis.namespace || lis.namespace === evt.namespace;
              var typeMatches = lis.type === evt.type;
              var targetMatches = lis.delegated ? ( triggerer !== evt.cyTarget && $$.is.element(evt.cyTarget) && lis.selObj.matches(evt.cyTarget) ) : (true); // we're not going to validate the hierarchy; that's too expensive
              var listenerMatches = nsMatches && typeMatches && targetMatches;

              if( listenerMatches ){ // then trigger it
                var args = [ evt ];
                args = args.concat( extraParams ); // add extra params to args list

                if( lis.data ){ // add on data plugged into binding
                  evt.data = lis.data;
                } else { // or clear it in case the event obj is reused
                  evt.data = undefined;
                }

                if( lis.unbindSelfOnTrigger || lis.unbindAllBindersOnTrigger ){ // then remove listener
                  listeners.splice(k, 1);
                  k--;
                }

                if( lis.unbindAllBindersOnTrigger ){ // then delete the listener for all binders
                  var binders = lis.binders;
                  for( var l = 0; l < binders.length; l++ ){
                    var binder = binders[l];
                    if( !binder || binder === triggerer ){ continue; } // already handled triggerer or we can't handle it

                    var binderListeners = binder._private.listeners;
                    for( var m = 0; m < binderListeners.length; m++ ){
                      var binderListener = binderListeners[m];

                      if( binderListener === lis ){ // delete listener from list
                        binderListeners.splice(m, 1);
                        m--;
                      }
                    }
                  }
                }

                // run the callback
                var context = lis.delegated ? evt.cyTarget : triggerer;
                var ret = lis.callback.apply( context, args );

                if( ret === false || evt.isPropagationStopped() ){
                  // then don't bubble
                  bubbleUp = false;

                  if( ret === false ){
                    // returning false is a shorthand for stopping propagation and preventing the def. action
                    evt.stopPropagation();
                    evt.preventDefault();
                  }
                }
              } // if listener matches
            } // for each listener

            // bubble up event for elements
            if( bubbleUp ){
              var parent = hasCompounds ? triggerer._private.parent : null;
              var hasParent = parent != null && parent.length !== 0;

              if( hasParent ){ // then bubble up to parent
                parent = parent[0];
                parent.trigger(evt);
              } else { // otherwise, bubble up to the core
                cy.trigger(evt);
              }
            }

          } // for each of all
        } // for each event
        
        return self; // maintain chaining
      }; // function
    }, // trigger


    animated: function( fnParams ){
      var defaults = {};
      fnParams = $$.util.extend({}, defaults, fnParams);

      return function animatedImpl(){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var cy = this._private.cy || this;

        if( !cy.styleEnabled() ){ return false; }

        var ele = all[0];

        if( ele ){
          return ele._private.animation.current.length > 0;
        }
      };
    }, // animated

    clearQueue: function( fnParams ){
      var defaults = {};
      fnParams = $$.util.extend({}, defaults, fnParams);

      return function clearQueueImpl(){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var cy = this._private.cy || this;

        if( !cy.styleEnabled() ){ return this; }

        for( var i = 0; i < all.length; i++ ){
          var ele = all[i];
          ele._private.animation.queue = [];
        }

        return this;
      };
    }, // clearQueue

    delay: function( fnParams ){
      var defaults = {};
      fnParams = $$.util.extend({}, defaults, fnParams);

      return function delayImpl( time, complete ){
        var cy = this._private.cy || this;

        if( !cy.styleEnabled() ){ return this; }

        this.animate({
          delay: time
        }, {
          duration: time,
          complete: complete
        });

        return this;
      };
    }, // delay

    animate: function( fnParams ){
      var defaults = {};
      fnParams = $$.util.extend({}, defaults, fnParams);

      return function animateImpl( properties, params ){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var cy = this._private.cy || this;
        var isCore = !selfIsArrayLike;
        var isEles = !isCore;

        if( !cy.styleEnabled() ){ return this; }

        var callTime = +new Date();
        var style = cy.style();
        var q;
        
        if( params === undefined ){
          params = {};
        }

        if( params.duration === undefined ){
          params.duration = 400;
        }
        
        switch( params.duration ){
        case 'slow':
          params.duration = 600;
          break;
        case 'fast':
          params.duration = 200;
          break;
        }
        
        var propertiesEmpty = true;
        if( properties ){ for( var i in properties ){
          propertiesEmpty = false;
          break;
        } }

        if( propertiesEmpty ){
          return this; // nothing to animate
        }

        if( properties.css && isEles ){
          properties.css = style.getValueStyle( properties.css, { array: true } );
        }

        if( properties.renderedPosition && isEles ){
          var rpos = properties.renderedPosition;
          var pan = cy.pan();
          var zoom = cy.zoom();

          properties.position = {
            x: ( rpos.x - pan.x ) /zoom,
            y: ( rpos.y - pan.y ) /zoom
          };
        }

        // override pan w/ panBy if set
        if( properties.panBy && isCore ){
          var panBy = properties.panBy;
          var cyPan = cy.pan();

          properties.pan = {
            x: cyPan.x + panBy.x,
            y: cyPan.y + panBy.y
          };
        }

        // override pan w/ center if set
        var center = properties.center || properties.centre;
        if( center && isCore ){
          var centerPan = cy.getCenterPan( center.eles, properties.zoom );

          if( centerPan ){
            properties.pan = centerPan;
          }
        }

        // override pan & zoom w/ fit if set
        if( properties.fit && isCore ){
          var fit = properties.fit;
          var fitVp = cy.getFitViewport( fit.eles || fit.boundingBox, fit.padding );

          if( fitVp ){
            properties.pan = fitVp.pan; //{ x: fitVp.pan.x, y: fitVp.pan.y };
            properties.zoom = fitVp.zoom;
          }
        }

        for( var i = 0; i < all.length; i++ ){
          var ele = all[i];
         
          if( ele.animated() && (params.queue === undefined || params.queue) ){
            q = ele._private.animation.queue;
          } else {
            q = ele._private.animation.current;
          }

          q.push({
            properties: properties,
            duration: params.duration,
            params: params,
            callTime: callTime
          });
        }

        if( isEles ){
          cy.addToAnimationPool( this );
        }

        return this; // chaining
      };
    }, // animate

    stop: function( fnParams ){
      var defaults = {};
      fnParams = $$.util.extend({}, defaults, fnParams);

      return function stopImpl( clearQueue, jumpToEnd ){
        var self = this;
        var selfIsArrayLike = self.length !== undefined;
        var all = selfIsArrayLike ? self : [self]; // put in array if not array-like
        var cy = this._private.cy || this;

        if( !cy.styleEnabled() ){ return this; }

        for( var i = 0; i < all.length; i++ ){
          var ele = all[i];
          var anis = ele._private.animation.current;

          for( var j = 0; j < anis.length; j++ ){
            var animation = anis[j];    
            if( jumpToEnd ){
              // next iteration of the animation loop, the animation
              // will go straight to the end and be removed
              animation.duration = 0; 
            }
          }
          
          // clear the queue of future animations
          if( clearQueue ){
            ele._private.animation.queue = [];
          }

          if( !jumpToEnd ){
            ele._private.animation.current = [];
          }
        }
        
        // we have to notify (the animation loop doesn't do it for us on `stop`)
        cy.notify({
          collection: this,
          type: 'draw'
        });
        
        return this;
      };
    } // stop

  }; // define

  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.selector = function(map, options){
    for( var name in map ){
      var fn = map[name];
      $$.Selector.prototype[ name ] = fn;
    }
  };

  $$.Selector = function(onlyThisGroup, selector){
    
    if( !(this instanceof $$.Selector) ){
      return new $$.Selector(onlyThisGroup, selector);
    }
  
    if( selector === undefined && onlyThisGroup !== undefined ){
      selector = onlyThisGroup;
      onlyThisGroup = undefined;
    }
    
    var self = this;
    
    self._private = {
      selectorText: null,
      invalid: true
    };
    
    if( !selector || ( $$.is.string(selector) && selector.match(/^\s*$/) ) ){
      
      if( onlyThisGroup == null ){
        // ignore
        self.length = 0;
      } else {
        self[0] = newQuery();
        self[0].group = onlyThisGroup;
        self.length = 1;
      }
              
    } else if( $$.is.element( selector ) ){
      var collection = new $$.Collection(self.cy(), [ selector ]);
      
      self[0] = newQuery();
      self[0].collection = collection;
      self.length = 1;
      
    } else if( $$.is.collection( selector ) ){
      self[0] = newQuery();
      self[0].collection = selector;
      self.length = 1;
      
    } else if( $$.is.fn( selector ) ) {
      self[0] = newQuery();
      self[0].filter = selector;
      self.length = 1;
      
    } else if( $$.is.string( selector ) ){

      // the current subject in the query
      var currentSubject = null;
      
      // storage for parsed queries
      var newQuery = function(){
        return {
          classes: [], 
          colonSelectors: [],
          data: [],
          group: null,
          ids: [],
          meta: [],

          // fake selectors
          collection: null, // a collection to match against
          filter: null, // filter function

          // these are defined in the upward direction rather than down (e.g. child)
          // because we need to go up in Selector.filter()
          parent: null, // parent query obj
          ancestor: null, // ancestor query obj
          subject: null, // defines subject in compound query (subject query obj; points to self if subject)

          // use these only when subject has been defined
          child: null,
          descendant: null
        };
      };

      // tokens in the query language
      var tokens = {
        metaChar: '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\]\\^\\`\\{\\|\\}\\~]', // chars we need to escape in var names, etc
        comparatorOp: '=|\\!=|>|>=|<|<=|\\$=|\\^=|\\*=', // binary comparison op (used in data selectors)
        boolOp: '\\?|\\!|\\^', // boolean (unary) operators (used in data selectors)
        string: '"(?:\\\\"|[^"])+"' + '|' + "'(?:\\\\'|[^'])+'", // string literals (used in data selectors) -- doublequotes | singlequotes
        number: $$.util.regex.number, // number literal (used in data selectors) --- e.g. 0.1234, 1234, 12e123
        meta: 'degree|indegree|outdegree', // allowed metadata fields (i.e. allowed functions to use from $$.Collection)
        separator: '\\s*,\\s*', // queries are separated by commas, e.g. edge[foo = 'bar'], node.someClass
        descendant: '\\s+',
        child: '\\s+>\\s+',
        subject: '\\$'
      };
      tokens.variable = '(?:[\\w-]|(?:\\\\'+ tokens.metaChar +'))+'; // a variable name
      tokens.value = tokens.string + '|' + tokens.number; // a value literal, either a string or number
      tokens.className = tokens.variable; // a class name (follows variable conventions)
      tokens.id = tokens.variable; // an element id (follows variable conventions)

      // when a token like a variable has escaped meta characters, we need to clean the backslashes out
      // so that values get compared properly in Selector.filter()
      var cleanMetaChars = function(str){
        return str.replace(new RegExp('\\\\(' + tokens.metaChar + ')', 'g'), function(match, $1, offset, original){
          return $1;
        });
      };
      
      // add @ variants to comparatorOp
      var ops = tokens.comparatorOp.split('|');
      for( var i = 0; i < ops.length; i++ ){
        var op = ops[i];
        tokens.comparatorOp += '|@' + op;
      }

      // add ! variants to comparatorOp
      var ops = tokens.comparatorOp.split('|');
      for( var i = 0; i < ops.length; i++ ){
        var op = ops[i];

        if( op.indexOf('!') >= 0 ){ continue; } // skip ops that explicitly contain !
        if( op === '=' ){ continue; } // skip = b/c != is explicitly defined

        tokens.comparatorOp += '|\\!' + op;
      }

      // NOTE: add new expression syntax here to have it recognised by the parser;
      // - a query contains all adjacent (i.e. no separator in between) expressions;
      // - the current query is stored in self[i] --- you can use the reference to `this` in the populate function;
      // - you need to check the query objects in Selector.filter() for it actually filter properly, but that's pretty straight forward
      // - when you add something here, also add to Selector.toString()
      var exprs = {
        group: {
          query: true,
          regex: '(node|edge|\\*)',
          populate: function( group ){
            this.group = group == "*" ? group : group + 's';
          }
        },
        
        state: {
          query: true,
          // NB: if one colon selector is a substring of another from its start, place the longer one first
          // e.g. :foobar|:foo
          regex: '(:selected|:unselected|:locked|:unlocked|:visible|:hidden|:transparent|:grabbed|:free|:removed|:inside|:grabbable|:ungrabbable|:animated|:unanimated|:selectable|:unselectable|:orphan|:nonorphan|:parent|:child|:loop|:simple|:active|:inactive|:touch)',
          populate: function( state ){
            this.colonSelectors.push( state );
          }
        },
        
        id: {
          query: true,
          regex: '\\#('+ tokens.id +')',
          populate: function( id ){
            this.ids.push( cleanMetaChars(id) );
          }
        },
        
        className: {
          query: true,
          regex: '\\.('+ tokens.className +')',
          populate: function( className ){
            this.classes.push( cleanMetaChars(className) );
          }
        },
        
        dataExists: {
          query: true,
          regex: '\\[\\s*('+ tokens.variable +')\\s*\\]',
          populate: function( variable ){
            this.data.push({
              field: cleanMetaChars(variable)
            });
          }
        },
        
        dataCompare: {
          query: true,
          regex: '\\[\\s*('+ tokens.variable +')\\s*('+ tokens.comparatorOp +')\\s*('+ tokens.value +')\\s*\\]',
          populate: function( variable, comparatorOp, value ){ 
            var valueIsString = new RegExp('^' + tokens.string + '$').exec(value) != null;

            if( valueIsString ){
              value = value.substring(1, value.length - 1);
            } else {
              value = parseFloat(value);
            }

            this.data.push({
              field: cleanMetaChars(variable),
              operator: comparatorOp,
              value: value
            });
          }
        },
        
        dataBool: {
          query: true,
          regex: '\\[\\s*('+ tokens.boolOp +')\\s*('+ tokens.variable +')\\s*\\]',
          populate: function( boolOp, variable ){
            this.data.push({
              field: cleanMetaChars(variable),
              operator: boolOp
            });
          }
        },
        
        metaCompare: {
          query: true,
          regex: '\\[\\[\\s*('+ tokens.meta +')\\s*('+ tokens.comparatorOp +')\\s*('+ tokens.number +')\\s*\\]\\]',
          populate: function( meta, comparatorOp, number ){
            this.meta.push({
              field: cleanMetaChars(meta),
              operator: comparatorOp,
              value: parseFloat(number)
            });
          }
        },

        nextQuery: {
          separator: true,
          regex: tokens.separator,
          populate: function(){
            // go on to next query
            self[++i] = newQuery();
            currentSubject = null;
          }
        },

        child: {
          separator: true,
          regex: tokens.child,
          populate: function(){
            // this query is the parent of the following query
            var childQuery = newQuery();
            childQuery.parent = this;
            childQuery.subject = currentSubject;

            // we're now populating the child query with expressions that follow
            self[i] = childQuery;
          }
        },

        descendant: {
          separator: true,
          regex: tokens.descendant,
          populate: function(){
            // this query is the ancestor of the following query
            var descendantQuery = newQuery();
            descendantQuery.ancestor = this;
            descendantQuery.subject = currentSubject;

            // we're now populating the descendant query with expressions that follow
            self[i] = descendantQuery;
          }
        },

        subject: {
          modifier: true,
          regex: tokens.subject,
          populate: function(){
            if( currentSubject != null && this.subject != this ){
              $$.util.error('Redefinition of subject in selector `' + selector + '`');
              return false;
            }

            currentSubject = this;
            this.subject = this;
          }

        }
      };

      var j = 0;
      for( var name in exprs ){
        exprs[j] = exprs[name];
        exprs[j].name = name;

        j++;
      }
      exprs.length = j;

      self._private.selectorText = selector;
      var remaining = selector;
      var i = 0;
      
      // of all the expressions, find the first match in the remaining text
      var consumeExpr = function( expectation ){
        var expr;
        var match;
        var name;
        
        for( var j = 0; j < exprs.length; j++ ){
          var e = exprs[j];
          var n = e.name;

          // ignore this expression if it doesn't meet the expectation function
          if( $$.is.fn( expectation ) && !expectation(n, e) ){ continue; }

          var m = remaining.match(new RegExp( '^' + e.regex ));
          
          if( m != null ){
            match = m;
            expr = e;
            name = n;
            
            var consumed = m[0];
            remaining = remaining.substring( consumed.length );                
            
            break; // we've consumed one expr, so we can return now
          }
        }
        
        return {
          expr: expr,
          match: match,
          name: name
        };
      };
      
      // consume all leading whitespace
      var consumeWhitespace = function(){
        var match = remaining.match(/^\s+/);
        
        if( match ){
          var consumed = match[0];
          remaining = remaining.substring( consumed.length );
        }
      };
      
      self[0] = newQuery(); // get started

      consumeWhitespace(); // get rid of leading whitespace
      for(;;){        
        var check = consumeExpr();
        
        if( check.expr == null ){
          $$.util.error('The selector `'+ selector +'`is invalid');
          return;
        } else {
          var args = [];
          for(var j = 1; j < check.match.length; j++){
            args.push( check.match[j] );
          }
          
          // let the token populate the selector object (i.e. in self[i])
          var ret = check.expr.populate.apply( self[i], args );

          if( ret === false ){ return; } // exit if population failed
        }
        
        // we're done when there's nothing left to parse
        if( remaining.match(/^\s*$/) ){
          break;
        }
      }
      
      self.length = i + 1;

      // adjust references for subject
      for(j = 0; j < self.length; j++){
        var query = self[j];

        if( query.subject != null ){
          // go up the tree until we reach the subject
          for(;;){
            if( query.subject == query ){ break; } // done if subject is self

            if( query.parent != null ){ // swap parent/child reference
              var parent = query.parent;
              var child = query;

              child.parent = null;
              parent.child = child;

              query = parent; // go up the tree
            } else if( query.ancestor != null ){ // swap ancestor/descendant
              var ancestor = query.ancestor;
              var descendant = query;

              descendant.ancestor = null;
              ancestor.descendant = descendant;

              query = ancestor; // go up the tree
            } else {
              $$.util.error('When adjusting references for the selector `'+ query +'`, neither parent nor ancestor was found');
              break;
            }
          } // for

          self[j] = query.subject; // subject should be the root query
        } // if
      } // for

      // make sure for each query that the subject group matches the implicit group if any
      if( onlyThisGroup != null ){
        for(var j = 0; j < self.length; j++){
          if( self[j].group != null && self[j].group != onlyThisGroup ){
            $$.util.error('Group `'+ self[j].group +'` conflicts with implicit group `'+ onlyThisGroup +'` in selector `'+ selector +'`');
            return;
          }

          self[j].group = onlyThisGroup; // set to implicit group
        }
      }
      
    } else {
      $$.util.error('A selector must be created from a string; found ' + selector);
      return;
    }

    self._private.invalid = false;
    
  };

  $$.selfn = $$.Selector.prototype;
  
  $$.selfn.size = function(){
    return this.length;
  };
  
  $$.selfn.eq = function(i){
    return this[i];
  };
  
  // get elements from the core and then filter them
  $$.selfn.find = function(){
    // TODO impl if we decide to use a DB for storing elements
  };
  
  var queryMatches = function(query, element){
    // check group
    if( query.group != null && query.group != '*' && query.group != element._private.group ){
      return false;
    }

    var cy = element.cy();
    
    // check colon selectors
    var allColonSelectorsMatch = true;
    for(var k = 0; k < query.colonSelectors.length; k++){
      var sel = query.colonSelectors[k];
      
      switch(sel){
      case ':selected':
        allColonSelectorsMatch = element.selected();
        break;
      case ':unselected':
        allColonSelectorsMatch = !element.selected();
        break;
      case ':selectable':
        allColonSelectorsMatch = element.selectable();
        break;
      case ':unselectable':
        allColonSelectorsMatch = !element.selectable();
        break;
      case ':locked':
        allColonSelectorsMatch = element.locked();
        break;
      case ':unlocked':
        allColonSelectorsMatch = !element.locked();
        break;
      case ':visible':
        allColonSelectorsMatch = element.visible();
        break;
      case ':hidden':
        allColonSelectorsMatch = !element.visible();
        break;
      case ':transparent':
        allColonSelectorsMatch = element.transparent();
        break;
      case ':grabbed':
        allColonSelectorsMatch = element.grabbed();
        break;
      case ':free':
        allColonSelectorsMatch = !element.grabbed();
        break;
      case ':removed':
        allColonSelectorsMatch = element.removed();
        break;
      case ':inside':
        allColonSelectorsMatch = !element.removed();
        break;
      case ':grabbable':
        allColonSelectorsMatch = element.grabbable();
        break;
      case ':ungrabbable':
        allColonSelectorsMatch = !element.grabbable();
        break;
      case ':animated':
        allColonSelectorsMatch = element.animated();
        break;
      case ':unanimated':
        allColonSelectorsMatch = !element.animated();
        break;
      case ':parent':
        allColonSelectorsMatch = element.isNode() && element.children().nonempty();
        break;
      case ':child':
      case ':nonorphan':
        allColonSelectorsMatch = element.isNode() && element.parent().nonempty();
        break;
      case ':orphan':
        allColonSelectorsMatch = element.isNode() && element.parent().empty();
        break;
      case ':loop':
        allColonSelectorsMatch = element.isEdge() && element.data('source') === element.data('target');
        break;
      case ':simple':
        allColonSelectorsMatch = element.isEdge() && element.data('source') !== element.data('target');
        break;
      case ':active':
        allColonSelectorsMatch = element.active();
        break;
      case ':inactive':
        allColonSelectorsMatch = !element.active();
        break;
      case ':touch':
        allColonSelectorsMatch = $$.is.touch();
        break;
      }
      
      if( !allColonSelectorsMatch ) break;
    }
    if( !allColonSelectorsMatch ) return false;
    
    // check id
    var allIdsMatch = true;
    for(var k = 0; k < query.ids.length; k++){
      var id = query.ids[k];
      var actualId = element._private.data.id;
      
      allIdsMatch = allIdsMatch && (id == actualId);
      
      if( !allIdsMatch ) break;
    }
    if( !allIdsMatch ) return false;
    
    // check classes
    var allClassesMatch = true;
    for(var k = 0; k < query.classes.length; k++){
      var cls = query.classes[k];
      
      allClassesMatch = allClassesMatch && element.hasClass(cls);
      
      if( !allClassesMatch ) break;
    }
    if( !allClassesMatch ) return false;
    
    // generic checking for data/metadata
    var operandsMatch = function(params){
      var allDataMatches = true;
      for(var k = 0; k < query[params.name].length; k++){
        var data = query[params.name][k];
        var operator = data.operator;
        var value = data.value;
        var field = data.field;
        var matches;
        
        if( operator != null && value != null ){
          
          var fieldVal = params.fieldValue(field);
          var fieldStr = !$$.is.string(fieldVal) && !$$.is.number(fieldVal) ? '' : '' + fieldVal;
          var valStr = '' + value;
          
          var caseInsensitive = false;
          if( operator.indexOf('@') >= 0 ){
            fieldStr = fieldStr.toLowerCase();
            valStr = valStr.toLowerCase();
            
            operator = operator.replace('@', '');
            caseInsensitive = true;
          }

          var notExpr = false;
          var handledNotExpr = false;
          if( operator.indexOf('!') >= 0 ){
            operator = operator.replace('!', '');
            notExpr = true;
          }
          
          // if we're doing a case insensitive comparison, then we're using a STRING comparison
          // even if we're comparing numbers
          if( caseInsensitive ){
            value = valStr.toLowerCase();
            fieldVal = fieldStr.toLowerCase();
          }

          switch(operator){
          case '*=':
            matches = fieldStr.search(valStr) >= 0;
            break;
          case '$=':
            matches = new RegExp(valStr + '$').exec(fieldStr) != null;
            break;
          case '^=':
            matches = new RegExp('^' + valStr).exec(fieldStr) != null;
            break;
          case '=':
            matches = fieldVal === value;
            break;
          case '!=':
            matches = fieldVal !== value;
            break;
          case '>':
            matches = !notExpr ? fieldVal > value : fieldVal <= value;
            handledNotExpr = true;
            break;
          case '>=':
            matches = !notExpr ? fieldVal >= value : fieldVal < value;
            handledNotExpr = true;
            break;
          case '<':
            matches = !notExpr ? fieldVal < value : fieldVal >= value;
            handledNotExpr = true;
            break;
          case '<=':
            matches = !notExpr ? fieldVal <= value : fieldVal > value;
            handledNotExpr = true;
            break;
          default:
            matches = false;
            break;
            
          }
        } else if( operator != null ){
          switch(operator){
          case '?':
            matches = params.fieldTruthy(field);
            break;
          case '!':
            matches = !params.fieldTruthy(field);
            break;
          case '^':
            matches = params.fieldUndefined(field);
            break;
          }
        } else {   
          matches = !params.fieldUndefined(field);
        }

        if( notExpr && !handledNotExpr ){
          matches = !matches;
          handledNotExpr = true;
        }
        
        if( !matches ){
          allDataMatches = false;
          break;
        }
      } // for
      
      return allDataMatches;
    }; // operandsMatch
    
    // check data matches
    var allDataMatches = operandsMatch({
      name: 'data',
      fieldValue: function(field){
        return element._private.data[field];
      },
      fieldRef: function(field){
        return 'element._private.data.' + field;
      },
      fieldUndefined: function(field){
        return element._private.data[field] === undefined;
      },
      fieldTruthy: function(field){
        if( element._private.data[field] ){
          return true;
        }
        return false;
      }
    });
    
    if( !allDataMatches ){
      return false;
    }
    
    // check metadata matches
    var allMetaMatches = operandsMatch({
      name: 'meta',
      fieldValue: function(field){
        return element[field]();
      },
      fieldRef: function(field){
        return 'element.' + field + '()';
      },
      fieldUndefined: function(field){
        return element[field]() == null;
      },
      fieldTruthy: function(field){
        if( element[field]() ){
          return true;
        }
        return false;
      }
    });
    
    if( !allMetaMatches ){
      return false;
    }
    
    // check collection
    if( query.collection != null ){
      var matchesAny = query.collection._private.ids[ element.id() ] != null;
      
      if( !matchesAny ){
        return false;
      }
    }
    
    // check filter function
    if( query.filter != null && element.collection().filter( query.filter ).size() === 0 ){
      return false;
    }
    

    // check parent/child relations
    var confirmRelations = function( query, elements ){
      if( query != null ){
        var matches = false;

        if( !cy.hasCompoundNodes() ){
          return false;
        }

        elements = elements(); // make elements functional so we save cycles if query == null

        // query must match for at least one element (may be recursive)
        for(var i = 0; i < elements.length; i++){
          if( queryMatches( query, elements[i] ) ){
            matches = true;
            break;
          }
        }

        return matches;
      } else {
        return true;
      }
    };

    if (! confirmRelations(query.parent, function(){
      return element.parent();
    }) ){ return false; }

    if (! confirmRelations(query.ancestor, function(){
      return element.parents();
    }) ){ return false; }

    if (! confirmRelations(query.child, function(){
      return element.children();
    }) ){ return false; }

    if (! confirmRelations(query.descendant, function(){
      return element.descendants();
    }) ){ return false; }

    // we've reached the end, so we've matched everything for this query
    return true;
  }; // queryMatches

  // filter an existing collection
  $$.selfn.filter = function(collection){
    var self = this;
    var cy = collection.cy();
    
    // don't bother trying if it's invalid
    if( self._private.invalid ){
      return new $$.Collection( cy );
    }
  
    var selectorFunction = function(i, element){
      for(var j = 0; j < self.length; j++){
        var query = self[j];
        
        if( queryMatches(query, element) ){
          return true;
        }
      }
      
      return false;
    };
    
    if( self._private.selectorText == null ){
      selectorFunction = function(){ return true; };
    }
    
    var filteredCollection = collection.filter( selectorFunction );
    
    return filteredCollection;
  }; // filter

  // does selector match a single element?
  $$.selfn.matches = function(ele){
    var self = this;
    
    // don't bother trying if it's invalid
    if( self._private.invalid ){
      return false;
    }
  
    for(var j = 0; j < self.length; j++){
      var query = self[j];
      
      if( queryMatches(query, ele) ){
        return true;
      }
    }
    
    return false;
  }; // filter
  
  // ith query to string
  $$.selfn.toString = $$.selfn.selector = function(){
    
    var str = '';
    
    var clean = function(obj, isValue){
      if( $$.is.string(obj) ){
        return isValue ? '"' + obj + '"' : obj;
      } 
      return '';
    };
    
    var queryToString = function(query){
      var str = '';

      if( query.subject === query ){
        str += '$';
      }

      var group = clean(query.group);
      str += group.substring(0, group.length - 1);
      
      for(var j = 0; j < query.data.length; j++){
        var data = query.data[j];
        
        if( data.value ){
          str += '[' + data.field + clean(data.operator) + clean(data.value, true) + ']';
        } else {
          str += '[' + clean(data.operator) + data.field + ']';
        }
      }

      for(var j = 0; j < query.meta.length; j++){
        var meta = query.meta[j];
        str += '[[' + meta.field + clean(meta.operator) + clean(meta.value, true) + ']]';
      }
      
      for(var j = 0; j < query.colonSelectors.length; j++){
        var sel = query.colonSelectors[i];
        str += sel;
      }
      
      for(var j = 0; j < query.ids.length; j++){
        var sel = '#' + query.ids[i];
        str += sel;
      }
      
      for(var j = 0; j < query.classes.length; j++){
        var sel = '.' + query.classes[i];
        str += sel;
      }

      if( query.parent != null ){
        str = queryToString( query.parent ) + ' > ' + str; 
      }

      if( query.ancestor != null ){
        str = queryToString( query.ancestor ) + ' ' + str; 
      }

      if( query.child != null ){
        str += ' > ' + queryToString( query.child ); 
      }

      if( query.descendant != null ){
        str += ' ' + queryToString( query.descendant ); 
      }

      return str;
    };

    for(var i = 0; i < this.length; i++){
      var query = this[i];
      
      str += queryToString( query );
      
      if( this.length > 1 && i < this.length - 1 ){
        str += ', ';
      }
    }
    
    return str;
  };
  
})( cytoscape );

;(function($$){ 'use strict';
  
  $$.Style = function( cy ){

    if( !(this instanceof $$.Style) ){
      return new $$.Style(cy);
    }

    if( !$$.is.core(cy) ){
      $$.util.error('A style must have a core reference');
      return;
    }

    this._private = {
      cy: cy,
      coreStyle: {},
      newStyle: true
    };
    
    this.length = 0;

    this.addDefaultStylesheet();
  };

  // nice-to-have aliases
  $$.style = $$.Style;
  $$.styfn = $$.Style.prototype;

  // define functions in the Style prototype
  $$.fn.style = function( fnMap, options ){
    for( var fnName in fnMap ){
      var fn = fnMap[ fnName ];
      $$.Style.prototype = fn;
    }
  };

  (function(){
    var number = $$.util.regex.number;
    var rgba = $$.util.regex.rgbaNoBackRefs;
    var hsla = $$.util.regex.hslaNoBackRefs;
    var hex3 = $$.util.regex.hex3;
    var hex6 = $$.util.regex.hex6;
    var data = function( prefix ){ return '^' + prefix + '\\s*\\(\\s*([\\w\\.]+)\\s*\\)$'; };
    var mapData = function( prefix ){ return '^' + prefix + '\\s*\\(([\\w\\.]+)\\s*\\,\\s*(' + number + ')\\s*\\,\\s*(' + number + ')\\s*,\\s*(' + number + '|\\w+|' + rgba + '|' + hsla + '|' + hex3 + '|' + hex6 + ')\\s*\\,\\s*(' + number + '|\\w+|' + rgba + '|' + hsla + '|' + hex3 + '|' + hex6 + ')\\)$'; };

    // each visual style property has a type and needs to be validated according to it
    $$.style.types = {
      time: { number: true, min: 0, units: 's|ms', implicitUnits: 'ms' },
      percent: { number: true, min: 0, max: 100, units: '%' },
      zeroOneNumber: { number: true, min: 0, max: 1, unitless: true },
      nOneOneNumber: { number: true, min: -1, max: 1, unitless: true },
      nonNegativeInt: { number: true, min: 0, integer: true, unitless: true },
      position: { enums: ['parent', 'origin'] },
      autoSize: { number: true, min: 0, enums: ['auto'] },
      number: { number: true },
      size: { number: true, min: 0 },
      bgSize: { number: true, min: 0, allowPercent: true },
      bgPos: { number: true, allowPercent: true },
      bgRepeat: { enums: ['repeat', 'repeat-x', 'repeat-y', 'no-repeat'] },
      bgFit: { enums: ['none', 'contain', 'cover'] },
      bgClip: { enums: ['none', 'node'] },
      color: { color: true },
      lineStyle: { enums: ['solid', 'dotted', 'dashed'] },
      borderStyle: { enums: ['solid', 'dotted', 'dashed', 'double'] },
      curveStyle: { enums: ['bezier', 'unbundled-bezier', 'haystack'] },
      fontFamily: { regex: '^([\\w- ]+(?:\\s*,\\s*[\\w- ]+)*)$' },
      fontVariant: { enums: ['small-caps', 'normal'] },
      fontStyle: { enums: ['italic', 'normal', 'oblique'] },
      fontWeight: { enums: ['normal', 'bold', 'bolder', 'lighter', '100', '200', '300', '400', '500', '600', '800', '900', 100, 200, 300, 400, 500, 600, 700, 800, 900] },
      textDecoration: { enums: ['none', 'underline', 'overline', 'line-through'] },
      textTransform: { enums: ['none', 'uppercase', 'lowercase'] },
      nodeShape: { enums: ['rectangle', 'roundrectangle', 'ellipse', 'triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'star'] },
      arrowShape: { enums: ['tee', 'triangle', 'triangle-tee', 'triangle-backcurve', 'half-triangle-overshot', 'square', 'circle', 'diamond', 'none'] },
      arrowFill: { enums: ['filled', 'hollow'] },
      display: { enums: ['element', 'none'] },
      visibility: { enums: ['hidden', 'visible'] },
      valign: { enums: ['top', 'center', 'bottom'] },
      halign: { enums: ['left', 'center', 'right'] },
      text: { string: true },
      data: { mapping: true, regex: data('data') },
      layoutData: { mapping: true, regex: data('layoutData') },
      mapData: { mapping: true, regex: mapData('mapData') },
      mapLayoutData: { mapping: true, regex: mapData('mapLayoutData') },
      url: { regex: '^url\\s*\\(\\s*([^\\s]+)\\s*\\s*\\)|none|(.+)$' },
      propList: { propList: true },
      angle: { number: true, units: 'deg|rad' }
    };

    // define visual style properties
    var t = $$.style.types;
    var props = $$.style.properties = [
      // labels
      { name: 'text-valign', type: t.valign },
      { name: 'text-halign', type: t.halign },
      { name: 'color', type: t.color },
      { name: 'content', type: t.text },
      { name: 'text-outline-color', type: t.color },
      { name: 'text-outline-width', type: t.size },
      { name: 'text-outline-opacity', type: t.zeroOneNumber },
      { name: 'text-opacity', type: t.zeroOneNumber },
      // { name: 'text-decoration', type: t.textDecoration }, // not supported in canvas
      { name: 'text-transform', type: t.textTransform },
      // { name: 'text-rotation', type: t.angle }, // TODO disabled b/c rotation breaks bounding boxes
      { name: 'font-family', type: t.fontFamily },
      { name: 'font-style', type: t.fontStyle },
      // { name: 'font-variant', type: t.fontVariant }, // not useful
      { name: 'font-weight', type: t.fontWeight },
      { name: 'font-size', type: t.size },
      { name: 'min-zoomed-font-size', type: t.size },

      // visibility
      { name: 'display', type: t.display },
      { name: 'visibility', type: t.visibility },
      { name: 'opacity', type: t.zeroOneNumber },
      { name: 'z-index', type: t.nonNegativeInt },

      // overlays
      { name: 'overlay-padding', type: t.size },
      { name: 'overlay-color', type: t.color },
      { name: 'overlay-opacity', type: t.zeroOneNumber },

      // transition anis
      { name: 'transition-property', type: t.propList },
      { name: 'transition-duration', type: t.time },
      { name: 'transition-delay', type: t.time },

      // node body
      { name: 'height', type: t.autoSize },
      { name: 'width', type: t.autoSize },
      { name: 'shape', type: t.nodeShape },
      { name: 'background-color', type: t.color },
      { name: 'background-opacity', type: t.zeroOneNumber },
      { name: 'background-blacken', type: t.nOneOneNumber },

      // node border
      { name: 'border-color', type: t.color },
      { name: 'border-opacity', type: t.zeroOneNumber },
      { name: 'border-width', type: t.size },
      { name: 'border-style', type: t.borderStyle },
      
      // node background images
      { name: 'background-image', type: t.url },
      { name: 'background-image-opacity', type: t.zeroOneNumber },
      { name: 'background-position-x', type: t.bgPos },
      { name: 'background-position-y', type: t.bgPos },
      { name: 'background-repeat', type: t.bgRepeat },
      { name: 'background-fit', type: t.bgFit },
      { name: 'background-clip', type: t.bgClip },

      // compound props
      { name: 'padding-left', type: t.size },
      { name: 'padding-right', type: t.size },
      { name: 'padding-top', type: t.size },
      { name: 'padding-bottom', type: t.size },
      { name: 'position', type: t.position },

      // edge line
      { name: 'line-style', type: t.lineStyle },
      { name: 'line-color', type: t.color },
      { name: 'control-point-step-size', type: t.size },
      { name: 'control-point-distance', type: t.number },
      { name: 'control-point-weight', type: t.zeroOneNumber },
      { name: 'curve-style', type: t.curveStyle },
      { name: 'haystack-radius', type: t.zeroOneNumber },

      // edge arrows
      { name: 'source-arrow-shape', type: t.arrowShape },
      { name: 'target-arrow-shape', type: t.arrowShape },
      { name: 'mid-source-arrow-shape', type: t.arrowShape },
      { name: 'mid-target-arrow-shape', type: t.arrowShape },
      { name: 'source-arrow-color', type: t.color },
      { name: 'target-arrow-color', type: t.color },
      { name: 'mid-source-arrow-color', type: t.color },
      { name: 'mid-target-arrow-color', type: t.color },
      { name: 'source-arrow-fill', type: t.arrowFill },
      { name: 'target-arrow-fill', type: t.arrowFill },
      { name: 'mid-source-arrow-fill', type: t.arrowFill },
      { name: 'mid-target-arrow-fill', type: t.arrowFill },

      // these are just for the core
      { name: 'selection-box-color', type: t.color },
      { name: 'selection-box-opacity', type: t.zeroOneNumber },
      { name: 'selection-box-border-color', type: t.color },
      { name: 'selection-box-border-width', type: t.size },
      { name: 'active-bg-color', type: t.color },
      { name: 'active-bg-opacity', type: t.zeroOneNumber },
      { name: 'active-bg-size', type: t.size },
      { name: 'outside-texture-bg-color', type: t.color },
      { name: 'outside-texture-bg-opacity', type: t.zeroOneNumber }
    ];

    // pie backgrounds for nodes
    $$.style.pieBackgroundN = 16; // because the pie properties are numbered, give access to a constant N (for renderer use)
    props.push({ name: 'pie-size', type: t.bgSize });
    for( var i = 1; i <= $$.style.pieBackgroundN; i++ ){
      props.push({ name: 'pie-'+i+'-background-color', type: t.color });
      props.push({ name: 'pie-'+i+'-background-size', type: t.percent });
      props.push({ name: 'pie-'+i+'-background-opacity', type: t.zeroOneNumber });
    }

    // allow access of properties by name ( e.g. $$.style.properties.height )
    for( var i = 0; i < props.length; i++ ){
      var prop = props[i];
      
      props[ prop.name ] = prop; // allow lookup by name
    }
  })();

  // adds the default stylesheet to the current style
  $$.styfn.addDefaultStylesheet = function(){
    // to be nice, we build font related style properties from the core container
    // so that cytoscape matches the style of its container by default
    // 
    // unfortunately, this doesn't seem work consistently and can grab the default stylesheet values
    // instead of the developer's values so let's just make it explicit for the dev for now
    //
    // delaying the read of these val's is not an opt'n: that would delay init'l load time
    var fontFamily = 'Helvetica' || this.containerPropertyAsString('font-family') || 'sans-serif';
    var fontStyle = 'normal' || this.containerPropertyAsString('font-style') || 'normal';
    // var fontVariant = 'normal' || this.containerPropertyAsString('font-variant') || 'normal';
    var fontWeight = 'normal' || this.containerPropertyAsString('font-weight') || 'normal';
    var color = '#000' || this.containerPropertyAsString('color') || '#000';
    var textTransform = 'none' || this.containerPropertyAsString('text-transform') || 'none';
    var fontSize = 16 || this.containerPropertyAsString('font-size') || 16;

    // fill the style with the default stylesheet
    this
      .selector('node, edge') // common properties
        .css({
          'text-valign': 'top',
          'text-halign': 'center',
          'color': color,
          'text-outline-color': '#000',
          'text-outline-width': 0,
          'text-outline-opacity': 1,
          'text-opacity': 1,
          'text-decoration': 'none',
          'text-transform': textTransform,
          'font-family': fontFamily,
          'font-style': fontStyle,
          // 'font-variant': fontVariant,
          'font-weight': fontWeight,
          'font-size': fontSize,
          'min-zoomed-font-size': 0,
          'visibility': 'visible',
          'display': 'element',
          'opacity': 1,
          'z-index': 0,
          'content': '',
          'overlay-opacity': 0,
          'overlay-color': '#000',
          'overlay-padding': 10,
          'transition-property': 'none',
          'transition-duration': 0,
          'transition-delay': 0,

          // node props
          'background-blacken': 0,
          'background-color': '#888',
          'background-opacity': 1,
          'background-image': 'none',
          'background-image-opacity': 1,
          'background-position-x': '50%',
          'background-position-y': '50%',
          'background-repeat': 'no-repeat',
          'background-fit': 'none',
          'background-clip': 'node',
          'border-color': '#000',
          'border-opacity': 1,
          'border-width': 0,
          'border-style': 'solid',
          'height': 30,
          'width': 30,
          'shape': 'ellipse',

          // compound props
          'padding-top': 0,
          'padding-bottom': 0,
          'padding-left': 0,
          'padding-right': 0,
          'position': 'origin',
          

          // node pie bg
          'pie-size': '100%',
          'pie-1-background-color': 'black',
          'pie-2-background-color': 'black',
          'pie-3-background-color': 'black',
          'pie-4-background-color': 'black',
          'pie-5-background-color': 'black',
          'pie-6-background-color': 'black',
          'pie-7-background-color': 'black',
          'pie-8-background-color': 'black',
          'pie-9-background-color': 'black',
          'pie-10-background-color': 'black',
          'pie-11-background-color': 'black',
          'pie-12-background-color': 'black',
          'pie-13-background-color': 'black',
          'pie-14-background-color': 'black',
          'pie-15-background-color': 'black',
          'pie-16-background-color': 'black',
          'pie-1-background-size': '0%',
          'pie-2-background-size': '0%',
          'pie-3-background-size': '0%',
          'pie-4-background-size': '0%',
          'pie-5-background-size': '0%',
          'pie-6-background-size': '0%',
          'pie-7-background-size': '0%',
          'pie-8-background-size': '0%',
          'pie-9-background-size': '0%',
          'pie-10-background-size': '0%',
          'pie-11-background-size': '0%',
          'pie-12-background-size': '0%',
          'pie-13-background-size': '0%',
          'pie-14-background-size': '0%',
          'pie-15-background-size': '0%',
          'pie-16-background-size': '0%',
          'pie-1-background-opacity': 1,
          'pie-2-background-opacity': 1,
          'pie-3-background-opacity': 1,
          'pie-4-background-opacity': 1,
          'pie-5-background-opacity': 1,
          'pie-6-background-opacity': 1,
          'pie-7-background-opacity': 1,
          'pie-8-background-opacity': 1,
          'pie-9-background-opacity': 1,
          'pie-10-background-opacity': 1,
          'pie-11-background-opacity': 1,
          'pie-12-background-opacity': 1,
          'pie-13-background-opacity': 1,
          'pie-14-background-opacity': 1,
          'pie-15-background-opacity': 1,
          'pie-16-background-opacity': 1,

          // edge props
          'source-arrow-shape': 'none',
          'mid-source-arrow-shape': 'none',
          'target-arrow-shape': 'none',
          'mid-target-arrow-shape': 'none',
          'source-arrow-color': '#ddd',
          'mid-source-arrow-color': '#ddd',
          'target-arrow-color': '#ddd',
          'mid-target-arrow-color': '#ddd',
          'source-arrow-fill': 'filled',
          'mid-source-arrow-fill': 'filled',
          'target-arrow-fill': 'filled',
          'mid-target-arrow-fill': 'filled',
          'line-style': 'solid',
          'line-color': '#ddd',
          'control-point-step-size': 40,
          'control-point-weight': 0.5,
          'curve-style': 'bezier',
          'haystack-radius': 0.8
        })
      .selector('$node > node') // compound (parent) node properties
        .css({
          'width': 'auto',
          'height': 'auto',
          'shape': 'rectangle',
          'background-opacity': 0.5,
          'padding-top': 10,
          'padding-right': 10,
          'padding-left': 10,
          'padding-bottom': 10
        })
      .selector('edge') // just edge properties
        .css({
          'width': 1
        })
      .selector(':active')
        .css({
          'overlay-color': 'black',
          'overlay-padding': 10,
          'overlay-opacity': 0.25
        })
      .selector('core') // just core properties
        .css({
          'selection-box-color': '#ddd',
          'selection-box-opacity': 0.65,
          'selection-box-border-color': '#aaa',
          'selection-box-border-width': 1,
          'active-bg-color': 'black',
          'active-bg-opacity': 0.15,
          'active-bg-size': $$.is.touch() ? 40 : 15,
          'outside-texture-bg-color': '#000',
          'outside-texture-bg-opacity': 0.125
        })
    ;

    this.defaultLength = this.length;
  };

  // remove all contexts
  $$.styfn.clear = function(){
    for( var i = 0; i < this.length; i++ ){
      this[i] = undefined;
    }
    this.length = 0;
    this._private.newStyle = true;

    return this; // chaining
  };

  $$.styfn.resetToDefault = function(){
    this.clear();
    this.addDefaultStylesheet();

    return this;
  };

  // builds a style object for the 'core' selector
  $$.styfn.core = function(){
    return this._private.coreStyle;
  };

  // parse a property; return null on invalid; return parsed property otherwise
  // fields :
  // - name : the name of the property
  // - value : the parsed, native-typed value of the property
  // - strValue : a string value that represents the property value in valid css
  // - bypass : true iff the property is a bypass property
  $$.styfn.parse = function( name, value, propIsBypass, propIsFlat ){
    
    name = $$.util.camel2dash( name ); // make sure the property name is in dash form (e.g. 'property-name' not 'propertyName')
    var property = $$.style.properties[ name ];
    var passedValue = value;
    
    if( !property ){ return null; } // return null on property of unknown name
    if( value === undefined || value === null ){ return null; } // can't assign null

    var valueIsString = $$.is.string(value);
    if( valueIsString ){ // trim the value to make parsing easier
      value = $$.util.trim( value );
    }

    var type = property.type;
    if( !type ){ return null; } // no type, no luck

    // check if bypass is null or empty string (i.e. indication to delete bypass property)
    if( propIsBypass && (value === '' || value === null) ){
      return {
        name: name,
        value: value,
        bypass: true,
        deleteBypass: true
      };
    }

    // check if value is mapped
    var data, mapData, layoutData, mapLayoutData;
    if( !valueIsString || propIsFlat ){
      // then don't bother to do the expensive regex checks

    } else if(
      ( data = new RegExp( $$.style.types.data.regex ).exec( value ) ) ||
      ( layoutData = new RegExp( $$.style.types.layoutData.regex ).exec( value ) )
    ){
      if( propIsBypass ){ return false; } // mappers not allowed in bypass
      
      var isLayout = layoutData !== undefined;
      data = data || layoutData;

      return {
        name: name,
        value: data,
        strValue: '' + value,
        mapped: isLayout ? $$.style.types.layoutData : $$.style.types.data,
        field: data[1],
        bypass: propIsBypass,
        hasPie: name.match(/pie-(\d+)-background-size/)
      };

    } else if(
      ( mapData = new RegExp( $$.style.types.mapData.regex ).exec( value ) ) ||
      ( mapLayoutData = new RegExp( $$.style.types.mapLayoutData.regex ).exec( value ) )
    ){
      if( propIsBypass ){ return false; } // mappers not allowed in bypass

      var isLayout = mapLayoutData !== undefined;
      mapData = mapData || mapLayoutData;

      // we can map only if the type is a colour or a number
      if( !(type.color || type.number) ){ return false; }

      var valueMin = this.parse( name, mapData[4]); // parse to validate
      if( !valueMin || valueMin.mapped ){ return false; } // can't be invalid or mapped

      var valueMax = this.parse( name, mapData[5]); // parse to validate
      if( !valueMax || valueMax.mapped ){ return false; } // can't be invalid or mapped

      // check if valueMin and valueMax are the same
      if( valueMin.value === valueMax.value ){
        return false; // can't make much of a mapper without a range
      
      } else if( type.color ){
        var c1 = valueMin.value;
        var c2 = valueMax.value;
        
        var same = c1[0] === c2[0] // red
          && c1[1] === c2[1] // green
          && c1[2] === c2[2] // blue
          && ( // optional alpha
            c1[3] === c2[3] // same alpha outright
            || (
              (c1[3] == null || c1[3] === 1) // full opacity for colour 1?
              &&
              (c2[3] == null || c2[3] === 1) // full opacity for colour 2?
            )
          )
        ;

        if( same ){ return false; } // can't make a mapper without a range
      }

      return {
        name: name,
        value: mapData,
        strValue: '' + value,
        mapped: isLayout ? $$.style.types.mapLayoutData : $$.style.types.mapData,
        field: mapData[1],
        fieldMin: parseFloat( mapData[2] ), // min & max are numeric
        fieldMax: parseFloat( mapData[3] ),
        valueMin: valueMin.value,
        valueMax: valueMax.value,
        bypass: propIsBypass,
        hasPie: name.match(/pie-(\d+)-background-size/)
      };
    }

    // check the type and return the appropriate object
    if( type.number ){ 
      var units;
      var implicitUnits = 'px'; // not set => px

      if( type.units ){ // use specified units if set
        units = type.units;
      }

      if( type.implicitUnits ){
        implicitUnits = type.implicitUnits;
      }

      if( !type.unitless ){
        if( valueIsString ){
          var unitsRegex = 'px|em' + (type.allowPercent ? '|\\%' : '');
          if( units ){ unitsRegex = units; } // only allow explicit units if so set 
          var match = value.match( '^(' + $$.util.regex.number + ')(' + unitsRegex + ')?' + '$' );
          
          if( match ){
            value = match[1];
            units = match[2] || implicitUnits;
          }
          
        } else if( !units || type.implicitUnits ) {
          units = implicitUnits; // implicitly px if unspecified
        }
      }

      value = parseFloat( value );

      // if not a number and enums not allowed, then the value is invalid
      if( isNaN(value) && type.enums === undefined ){
        return null;
      }

      // check if this number type also accepts special keywords in place of numbers
      // (i.e. `left`, `auto`, etc)
      if( isNaN(value) && type.enums !== undefined ){
        value = passedValue;

        for( var i = 0; i < type.enums.length; i++ ){
          var en = type.enums[i];

          if( en === value ){
            return {
              name: name,
              value: value,
              strValue: '' + value,
              bypass: propIsBypass
            };
          }
        }

        return null; // failed on enum after failing on number
      }

      // check if value must be an integer
      if( type.integer && !$$.is.integer(value) ){
        return null;
      }

      // check value is within range
      if( (type.min !== undefined && value < type.min) 
      || (type.max !== undefined && value > type.max)
      ){
        return null;
      }

      var ret = {
        name: name,
        value: value,
        strValue: '' + value + (units ? units : ''),
        units: units,
        bypass: propIsBypass,
        hasPie: name.match(/pie-(\d+)-background-size/) && value != null && value !== 0 && value !== ''
      };

      // normalise value in pixels
      if( type.unitless || (units !== 'px' && units !== 'em') ){
        // then pxValue does not apply
      } else {
        ret.pxValue = ( units === 'px' || !units ? (value) : (this.getEmSizeInPixels() * value) );
      }

      // normalise value in ms
      if( units === 'ms' || units === 's' ){
        ret.msValue = units === 'ms' ? value : 1000 * value;
      }

      return ret;

    } else if( type.propList ) {

      var props = [];
      var propsStr = '' + value;      
 
      if( propsStr === 'none' ){
        // leave empty

      } else { // go over each prop

        var propsSplit = propsStr.split(',');
        for( var i = 0; i < propsSplit.length; i++ ){
          var propName = $$.util.trim( propsSplit[i] );

          if( $$.style.properties[propName] ){
            props.push( propName );
          }
        }

        if( props.length === 0 ){ return null; }

      }

      return {
        name: name,
        value: props,
        strValue: props.length === 0 ? 'none' : props.join(', '),
        bypass: propIsBypass
      };

    } else if( type.color ){
      var tuple = $$.util.color2tuple( value );

      if( !tuple ){ return null; }

      return {
        name: name,
        value: tuple,
        strValue: '' + value,
        bypass: propIsBypass
      };

    } else if( type.enums ){
      for( var i = 0; i < type.enums.length; i++ ){
        var en = type.enums[i];

        if( en === value ){
          return {
            name: name,
            value: value,
            strValue: '' + value,
            bypass: propIsBypass
          };
        }
      }

      return null;

    } else if( type.regex ){
      var regex = new RegExp( type.regex ); // make a regex from the type
      var m = regex.exec( value );

      if( m ){ // regex matches
        return {
          name: name,
          value: m,
          strValue: '' + value,
          bypass: propIsBypass
        };
      } else { // regex doesn't match
        return null; // didn't match the regex so the value is bogus
      }

    } else if( type.string ){
      // just return
      return {
        name: name,
        value: value,
        strValue: '' + value,
        bypass: propIsBypass
      };

    } else {
      return null; // not a type we can handle
    }

  };

  // create a new context from the specified selector string and switch to that context
  $$.styfn.selector = function( selectorStr ){
    // 'core' is a special case and does not need a selector
    var selector = selectorStr === 'core' ? null : new $$.Selector( selectorStr );

    var i = this.length++; // new context means new index
    this[i] = {
      selector: selector,
      properties: [],
      mappedProperties: [],
      index: i
    };

    return this; // chaining
  };

  // add one or many css rules to the current context
  $$.styfn.css = function(){
    var args = arguments;

    switch( args.length ){
    case 1:
      var map = args[0];

      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var mapVal = map[ prop.name ];

        if( mapVal === undefined ){
          mapVal = map[ $$.util.dash2camel(prop.name) ];
        }

        if( mapVal !== undefined ){
          this.cssRule( prop.name, mapVal );
        }
      }

      break;

    case 2:
      this.cssRule( args[0], args[1] );
      break;

    default:
      break; // do nothing if args are invalid
    }

    return this; // chaining
  };

  // add a single css rule to the current context
  $$.styfn.cssRule = function( name, value ){ 
    // name-value pair
    var property = this.parse( name, value );

    // add property to current context if valid
    if( property ){
      var i = this.length - 1;
      this[i].properties.push( property );
      this[i].properties[ property.name ] = property; // allow access by name as well

      if( property.hasPie ){
        this._private.hasPie = true;
      }

      if( property.mapped ){
        this[i].mappedProperties.push( property );
      }

      // add to core style if necessary
      var currentSelectorIsCore = !this[i].selector;
      if( currentSelectorIsCore ){
        this._private.coreStyle[ property.name ] = property;
      }
    }

    return this; // chaining
  };

})( cytoscape );
;(function($$){ 'use strict';

  // (potentially expensive calculation)
  // apply the style to the element based on
  // - its bypass
  // - what selectors match it
  $$.styfn.apply = function( eles ){
    var self = this;

    if( self._private.newStyle ){ // clear style caches
      this._private.contextStyles = {};
      this._private.propDiffs = {};
    }

    for( var ie = 0; ie < eles.length; ie++ ){
      var ele = eles[ie];
      var cxtMeta = self.getContextMeta( ele );
      var cxtStyle = self.getContextStyle( cxtMeta );
      var app = self.applyContextStyle( cxtMeta, cxtStyle, ele );

      self.updateTransitions( ele, app.diffProps );
      self.updateStyleHints( ele );

    } // for elements

    self._private.newStyle = false;
  };

  $$.styfn.getPropertiesDiff = function( oldCxtKey, newCxtKey ){
    var self = this;
    var cache = self._private.propDiffs = self._private.propDiffs || {};
    var dualCxtKey = oldCxtKey + '-' + newCxtKey;
    var cachedVal = cache[dualCxtKey];

    if( cachedVal ){
      return cachedVal;
    }

    var diffProps = [];
    var addedProp = {};

    for( var i = 0; i < self.length; i++ ){
      var cxt = self[i];
      var oldHasCxt = oldCxtKey[i] === 't';
      var newHasCxt = newCxtKey[i] === 't';
      var cxtHasDiffed = oldHasCxt !== newHasCxt;
      var cxtHasMappedProps = cxt.mappedProperties.length > 0;

      if( cxtHasDiffed || cxtHasMappedProps ){
        var props;

        if( cxtHasDiffed && cxtHasMappedProps ){
          props = cxt.properties; // suffices b/c mappedProperties is a subset of properties
        } else if( cxtHasDiffed ){
          props = cxt.properties; // need to check them all
        } else if( cxtHasMappedProps ){
          props = cxt.mappedProperties; // only need to check mapped
        }

        for( var j = 0; j < props.length; j++ ){
          var prop = props[j];
          var name = prop.name;

          // if a later context overrides this property, then the fact that this context has switched/diffed doesn't matter
          // (semi expensive check since it makes this function O(n^2) on context length, but worth it since overall result
          // is cached)
          var laterCxtOverrides = false; 
          for( var k = i + 1; k < self.length; k++ ){
            var laterCxt = self[k];
            var hasLaterCxt = newCxtKey[k] === 't';

            if( !hasLaterCxt ){ continue; } // can't override unless the context is active

            laterCxtOverrides = laterCxt.properties[ prop.name ] != null;

            if( laterCxtOverrides ){ break; } // exit early as long as one later context overrides
          }

          if( !addedProp[name] && !laterCxtOverrides ){
            addedProp[name] = true;
            diffProps.push( name );
          }
        } // for props
      } // if

    } // for contexts

    cache[ dualCxtKey ] = diffProps;
    return diffProps;
  };

  $$.styfn.getContextMeta = function( ele ){
    var self = this;
    var cxtKey = '';
    var diffProps;
    var prevKey = ele._private.styleCxtKey || '';

    if( self._private.newStyle ){
      prevKey = ''; // since we need to apply all style if a fresh stylesheet
    }

    // get the cxt key
    for( var i = 0; i < self.length; i++ ){
      var context = self[i];
      var contextSelectorMatches = context.selector && context.selector.matches( ele ); // NB: context.selector may be null for 'core'

      if( contextSelectorMatches ){
        cxtKey += 't';
      } else {
        cxtKey += 'f';
      }
    } // for context

    diffProps = self.getPropertiesDiff( prevKey, cxtKey );

    ele._private.styleCxtKey = cxtKey;

    return {
      key: cxtKey,
      diffPropNames: diffProps
    };
  };

  // gets a computed ele style object based on matched contexts
  $$.styfn.getContextStyle = function( cxtMeta ){
    var cxtKey = cxtMeta.key;
    var self = this;
    var cxtStyles = this._private.contextStyles = this._private.contextStyles || {};

    // if already computed style, returned cached copy
    if( cxtStyles[cxtKey] ){ return cxtStyles[cxtKey]; }

    var style = {
      _private: {
        key: cxtKey
      }
    };

    for( var i = 0; i < self.length; i++ ){
      var cxt = self[i];
      var hasCxt = cxtKey[i] === 't';

      if( !hasCxt ){ continue; }

      for( var j = 0; j < cxt.properties.length; j++ ){
        var prop = cxt.properties[j];
        var styProp = style[ prop.name ] = prop;

        styProp.context = cxt;
      }
    }

    cxtStyles[cxtKey] = style;
    return style;
  };

  $$.styfn.applyContextStyle = function( cxtMeta, cxtStyle, ele ){
    var self = this;
    var diffProps = cxtMeta.diffPropNames;
    var retDiffProps = {};

    for( var i = 0; i < diffProps.length; i++ ){
      var diffPropName = diffProps[i];
      var cxtProp = cxtStyle[ diffPropName ];
      var eleProp = ele._private.style[ diffPropName ];

      // save cycles when the context prop doesn't need to be applied
      if( !cxtProp || eleProp === cxtProp ){ continue; }

      var retDiffProp = retDiffProps[ diffPropName ] = {
        prev: eleProp
      };

      self.applyParsedProperty( ele, cxtProp );

      retDiffProp.next = ele._private.style[ diffPropName ];

      if( retDiffProp.next && retDiffProp.next.bypass ){
        retDiffProp.next = retDiffProp.next.bypassed;
      }
    }

    return {
      diffProps: retDiffProps
    };
  };

  $$.styfn.updateStyleHints = function(ele){
    var _p = ele._private;
    var self = this;
    var style = _p.style;

    // set whether has pie or not; for greater efficiency
    var hasPie = false;
    if( _p.group === 'nodes' && self._private.hasPie ){
      for( var i = 1; i <= $$.style.pieBackgroundN; i++ ){ // 1..N
        var size = _p.style['pie-' + i + '-background-size'].value;

        if( size > 0 ){
          hasPie = true;
          break;
        }
      }
    }

    _p.hasPie = hasPie;

    var transform = style['text-transform'].strValue;
    var content = style['content'].strValue;
    var fStyle = style['font-style'].strValue;
    var size = style['font-size'].pxValue + 'px';
    var family = style['font-family'].strValue;
    // var variant = style['font-variant'].strValue;
    var weight = style['font-weight'].strValue;
    var valign = style['text-valign'].strValue;
    var halign = style['text-valign'].strValue;
    var oWidth = style['text-outline-width'].pxValue;
    _p.labelKey = fStyle +'$'+ size +'$'+ family +'$'+ weight +'$'+ content +'$'+ transform +'$'+ valign +'$'+ halign +'$'+ oWidth;
    _p.fontKey = fStyle +'$'+ weight +'$'+ size +'$'+ family;

    var width = style['width'].pxValue;
    var height = style['height'].pxValue;
    var borderW = style['border-width'].pxValue;
    _p.boundingBoxKey = width +'$'+ height +'$'+ borderW;

    if( ele._private.group === 'edges' ){
      var cpss = style['control-point-step-size'].pxValue;
      var cpd = style['control-point-distance'] ? style['control-point-distance'].pxValue : undefined;
      var cpw = style['control-point-weight'].value;
      var curve = style['curve-style'].strValue;
      
      _p.boundingBoxKey += '$'+ cpss +'$'+ cpd +'$'+ cpw +'$'+ curve;
    }

    _p.styleKey = Date.now(); // probably safe to use applied time and much faster
    // for( var i = 0; i < $$.style.properties.length; i++ ){
    //   var prop = $$.style.properties[i];
    //   var eleProp = _p.style[ prop.name ];
    //   var val = eleProp && eleProp.strValue ? eleProp.strValue : 'undefined';

    //   _p.styleKey += '$' + val;
    // }
  };

  // apply a property to the style (for internal use)
  // returns whether application was successful
  //
  // now, this function flattens the property, and here's how:
  //
  // for parsedProp:{ bypass: true, deleteBypass: true }
  // no property is generated, instead the bypass property in the
  // element's style is replaced by what's pointed to by the `bypassed`
  // field in the bypass property (i.e. restoring the property the
  // bypass was overriding)
  //
  // for parsedProp:{ mapped: truthy }
  // the generated flattenedProp:{ mapping: prop }
  // 
  // for parsedProp:{ bypass: true }
  // the generated flattenedProp:{ bypassed: parsedProp } 
  $$.styfn.applyParsedProperty = function( ele, parsedProp ){
    var prop = parsedProp;
    var style = ele._private.style;
    var fieldVal, flatProp;
    var type = $$.style.properties[ prop.name ].type;
    var propIsBypass = prop.bypass;
    var origProp = style[ prop.name ];
    var origPropIsBypass = origProp && origProp.bypass;

    // can't apply auto to width or height unless it's a parent node
    if( (parsedProp.name === 'height' || parsedProp.name === 'width') && parsedProp.value === 'auto' && ele.isNode() && !ele.isParent() ){
      return false;
    }

    // check if we need to delete the current bypass
    if( propIsBypass && prop.deleteBypass ){ // then this property is just here to indicate we need to delete
      var currentProp = style[ prop.name ];

      // can only delete if the current prop is a bypass and it points to the property it was overriding
      if( !currentProp ){
        return true; // property is already not defined
      } else if( currentProp.bypass && currentProp.bypassed ){ // then replace the bypass property with the original
        
        // because the bypassed property was already applied (and therefore parsed), we can just replace it (no reapplying necessary)
        style[ prop.name ] = currentProp.bypassed;
        return true;
      
      } else {
        return false; // we're unsuccessful deleting the bypass
      }
    }

    var printMappingErr = function(){
      $$.util.error('Do not assign mappings to elements without corresponding data (e.g. ele `'+ ele.id() +'` for property `'+ prop.name +'` with data field `'+ prop.field +'`); try a `['+ prop.field +']` selector to limit scope to elements with `'+ prop.field +'` defined');
    };

    // put the property in the style objects
    switch( prop.mapped ){ // flatten the property if mapped
    case $$.style.types.mapData:
    case $$.style.types.mapLayoutData:
      
      var isLayout = prop.mapped === $$.style.types.mapLayoutData;

      // flatten the field (e.g. data.foo.bar)
      var fields = prop.field.split(".");
      var fieldVal = isLayout ? ele._private.layoutData : ele._private.data;
      for( var i = 0; i < fields.length && fieldVal; i++ ){
        var field = fields[i];
        fieldVal = fieldVal[ field ];
      }

      var percent;
      if( !$$.is.number(fieldVal) ){ // then keep the mapping but assume 0% for now
        percent = 0;
      } else {
        percent = (fieldVal - prop.fieldMin) / (prop.fieldMax - prop.fieldMin);
      }

      // make sure to bound percent value
      if( percent < 0 ){
        percent = 0;
      } else if( percent > 1 ){
        percent = 1;
      }

      if( type.color ){
        var r1 = prop.valueMin[0];
        var r2 = prop.valueMax[0];
        var g1 = prop.valueMin[1];
        var g2 = prop.valueMax[1];
        var b1 = prop.valueMin[2];
        var b2 = prop.valueMax[2];
        var a1 = prop.valueMin[3] == null ? 1 : prop.valueMin[3];
        var a2 = prop.valueMax[3] == null ? 1 : prop.valueMax[3];

        var clr = [
          Math.round( r1 + (r2 - r1)*percent ),
          Math.round( g1 + (g2 - g1)*percent ),
          Math.round( b1 + (b2 - b1)*percent ),
          Math.round( a1 + (a2 - a1)*percent )
        ];

        flatProp = { // colours are simple, so just create the flat property instead of expensive string parsing
          bypass: prop.bypass, // we're a bypass if the mapping property is a bypass
          name: prop.name,
          value: clr,
          strValue: 'rgb(' + clr[0] + ', ' + clr[1] + ', ' + clr[2] + ')'
        };
      
      } else if( type.number ){
        var calcValue = prop.valueMin + (prop.valueMax - prop.valueMin) * percent;
        flatProp = this.parse( prop.name, calcValue, prop.bypass, true );
      
      } else {
        return false; // can only map to colours and numbers
      }

      if( !flatProp ){ // if we can't flatten the property, then use the origProp so we still keep the mapping itself
        flatProp = this.parse( prop.name, origProp.strValue, prop.bypass, true );
      } 

      if( !flatProp ){ printMappingErr(); }
      flatProp.mapping = prop; // keep a reference to the mapping
      prop = flatProp; // the flattened (mapped) property is the one we want

      break;

    // direct mapping  
    case $$.style.types.data: 
    case $$.style.types.layoutData: 

      var isLayout = prop.mapped === $$.style.types.layoutData;

      // flatten the field (e.g. data.foo.bar)
      var fields = prop.field.split(".");
      var fieldVal = isLayout ? ele._private.layoutData : ele._private.data;
      for( var i = 0; i < fields.length && fieldVal; i++ ){
        var field = fields[i];
        fieldVal = fieldVal[ field ];
      }

      flatProp = this.parse( prop.name, fieldVal, prop.bypass, true );

      if( !flatProp ){ // if we can't flatten the property, then use the origProp so we still keep the mapping itself
        var flatPropVal = origProp ? origProp.strValue : '';

        flatProp = this.parse( prop.name, flatPropVal, prop.bypass, true );
      }

      if( !flatProp ){ printMappingErr(); }
      flatProp.mapping = prop; // keep a reference to the mapping
      prop = flatProp; // the flattened (mapped) property is the one we want
      break;

    case undefined:
      break; // just set the property

    default: 
      return false; // not a valid mapping
    }

    // if the property is a bypass property, then link the resultant property to the original one
    if( propIsBypass ){
      if( origPropIsBypass ){ // then this bypass overrides the existing one
        prop.bypassed = origProp.bypassed; // steal bypassed prop from old bypass
      } else { // then link the orig prop to the new bypass
        prop.bypassed = origProp;
      }

      style[ prop.name ] = prop; // and set
    
    } else { // prop is not bypass
      if( origPropIsBypass ){ // then keep the orig prop (since it's a bypass) and link to the new prop
        origProp.bypassed = prop;
      } else { // then just replace the old prop with the new one
        style[ prop.name ] = prop; 
      }
    }

    return true;
  };

  // updates the visual style for all elements (useful for manual style modification after init)
  $$.styfn.update = function(){
    var cy = this._private.cy;
    var eles = cy.elements();

    eles.updateStyle();
  };

  // just update the functional properties (i.e. mappings) in the elements'
  // styles (less expensive than recalculation)
  $$.styfn.updateMappers = function( eles ){
    for( var i = 0; i < eles.length; i++ ){ // for each ele
      var ele = eles[i];
      var style = ele._private.style;

      for( var j = 0; j < $$.style.properties.length; j++ ){ // for each prop
        var prop = $$.style.properties[j];
        var propInStyle = style[ prop.name ];

        if( propInStyle && propInStyle.mapping ){
          var mapping = propInStyle.mapping;
          this.applyParsedProperty( ele, mapping ); // reapply the mapping property
        }
      }

      this.updateStyleHints( ele );
    }
  };

  // diffProps : { name => { prev, next } }
  $$.styfn.updateTransitions = function( ele, diffProps, isBypass ){
    var self = this;
    var style = ele._private.style;

    var props = style['transition-property'].value;
    var duration = style['transition-duration'].msValue;
    var delay = style['transition-delay'].msValue;
    var css = {};

    if( props.length > 0 && duration > 0 ){

      // build up the style to animate towards
      var anyPrev = false;
      for( var i = 0; i < props.length; i++ ){
        var prop = props[i];
        var styProp = style[ prop ];
        var diffProp = diffProps[ prop ];

        if( !diffProp ){ continue; }

        var prevProp = diffProp.prev;
        var fromProp = prevProp;
        var toProp = diffProp.next != null ? diffProp.next : styProp;
        var diff = false;

        if( !fromProp ){ continue; } 

        // consider px values
        if( $$.is.number( fromProp.pxValue ) && $$.is.number( toProp.pxValue ) ){
          diff = fromProp.pxValue !== toProp.pxValue;

        // consider numerical values
        } else if( $$.is.number( fromProp.value ) && $$.is.number( toProp.value ) ){
          diff = fromProp.value !== toProp.value;

        // consider colour values
        } else if( $$.is.array( fromProp.value ) && $$.is.array( toProp.value ) ){
          diff = fromProp.value[0] !== toProp.value[0]
            || fromProp.value[1] !== toProp.value[1]
            || fromProp.value[2] !== toProp.value[2]
          ;
        }

        // the previous value is good for an animation only if it's different
        if( diff ){
          css[ prop ] = toProp.strValue; // to val
          this.applyBypass(ele, prop, fromProp.strValue); // from val
          anyPrev = true;
        }
        
      } // end if props allow ani

      // can't transition if there's nothing previous to transition from
      if( !anyPrev ){ return; }
      
      ele._private.transitioning = true;

      ele.stop();

      if( delay > 0 ){
        ele.delay( delay );
      }

      ele.animate({
        css: css
      }, {
        duration: duration,
        queue: false,
        complete: function(){ 
          if( !isBypass ){
            self.removeBypasses( ele, props );
          }

          ele._private.transitioning = false;
        }
      });

    } else if( ele._private.transitioning ){
      ele.stop();

      this.removeBypasses( ele, props );

      ele._private.transitioning = false;
    }
  }; 

})( cytoscape );
;(function($$){ 'use strict';

  // bypasses are applied to an existing style on an element, and just tacked on temporarily
  // returns true iff application was successful for at least 1 specified property
  $$.styfn.applyBypass = function( eles, name, value, updateTransitions ){
    var props = [];
    var isBypass = true;
    
    // put all the properties (can specify one or many) in an array after parsing them
    if( name === "*" || name === "**" ){ // apply to all property names

      if( value !== undefined ){
        for( var i = 0; i < $$.style.properties.length; i++ ){
          var prop = $$.style.properties[i];
          var name = prop.name;

          var parsedProp = this.parse(name, value, true);
          
          if( parsedProp ){
            props.push( parsedProp );
          }
        }
      }

    } else if( $$.is.string(name) ){ // then parse the single property
      var parsedProp = this.parse(name, value, true);

      if( parsedProp ){
        props.push( parsedProp );
      }
    } else if( $$.is.plainObject(name) ){ // then parse each property
      var specifiedProps = name;
      updateTransitions = value;

      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var name = prop.name;
        var value = specifiedProps[ name ];

        if( value === undefined ){ // try camel case name too
          value = specifiedProps[ $$.util.dash2camel(name) ];
        }

        if( value !== undefined ){
          var parsedProp = this.parse(name, value, true);
          
          if( parsedProp ){
            props.push( parsedProp );
          }
        }
      }
    } else { // can't do anything without well defined properties
      return false;
    }

    // we've failed if there are no valid properties
    if( props.length === 0 ){ return false; }

    // now, apply the bypass properties on the elements
    var ret = false; // return true if at least one succesful bypass applied
    for( var i = 0; i < eles.length; i++ ){ // for each ele
      var ele = eles[i];
      var style = ele._private.style;
      var diffProps = {};
      var diffProp;

      for( var j = 0; j < props.length; j++ ){ // for each prop
        var prop = props[j];

        if( updateTransitions ){
          var prevProp = style[ prop.name ];
          diffProp = diffProps[ prop.name ] = { prev: prevProp };
        }

        ret = this.applyParsedProperty( ele, prop ) || ret;

        if( updateTransitions ){
          diffProp.next = style[ prop.name ];
        }

      } // for props

      if( updateTransitions ){
        this.updateTransitions( ele, diffProps, isBypass );
      }
    } // for eles

    return ret;
  };

  // only useful in specific cases like animation
  $$.styfn.overrideBypass = function( eles, name, value ){
    for( var i = 0; i < eles.length; i++ ){
      var ele = eles[i];
      var prop = ele._private.style[ $$.util.camel2dash(name) ];

      if( !prop.bypass ){ // need a bypass if one doesn't exist
        this.applyBypass( ele, name, value );
        continue;
      }

      prop.value = value;
      prop.pxValue = value;
    }
  };

  $$.styfn.removeAllBypasses = function( eles, updateTransitions ){
    var isBypass = true;

    for( var j = 0; j < eles.length; j++ ){
      var ele = eles[j];
      var diffProps = {};
      var style = ele._private.style;

      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var name = prop.name;
        var value = ''; // empty => remove bypass
        var parsedProp = this.parse(name, value, true);
        var prevProp = style[ prop.name ];
        var diffProp = diffProps[ prop.name ] = { prev: prevProp };

        this.applyParsedProperty(ele, parsedProp);

        diffProp.next = style[ prop.name ];
      } // for props

      if( updateTransitions ){
        this.updateTransitions( ele, diffProps, isBypass );
      }
    } // for eles
  };

  $$.styfn.removeBypasses = function( eles, props, updateTransitions ){
    var isBypass = true;

    for( var j = 0; j < eles.length; j++ ){
      var ele = eles[j];
      var diffProps = {};
      var style = ele._private.style;

      for( var i = 0; i < props.length; i++ ){
        var name = props[i];
        var prop = $$.style.properties[ name ];
        var value = ''; // empty => remove bypass
        var parsedProp = this.parse(name, value, true);
        var prevProp = style[ prop.name ];
        var diffProp = diffProps[ prop.name ] = { prev: prevProp };

        this.applyParsedProperty(ele, parsedProp);

        diffProp.next = style[ prop.name ];
      } // for props

      if( updateTransitions ){
        this.updateTransitions( ele, diffProps, isBypass );
      }
    } // for eles
  };

})( cytoscape );
;(function($$, window){ 'use strict';

  // gets what an em size corresponds to in pixels relative to a dom element
  $$.styfn.getEmSizeInPixels = function(){
    var cy = this._private.cy;
    var domElement = cy.container();

    if( window && domElement && window.getComputedStyle ){
      var pxAsStr = window.getComputedStyle(domElement).getPropertyValue('font-size');
      var px = parseFloat( pxAsStr );
      return px;
    } else {
      return 1; // in case we're running outside of the browser
    }
  };

  // gets css property from the core container
  $$.styfn.containerCss = function( propName ){
    var cy = this._private.cy;
    var domElement = cy.container();

    if( window && domElement && window.getComputedStyle ){
      return window.getComputedStyle(domElement).getPropertyValue( propName );
    }
  };

  $$.styfn.containerProperty = function( propName ){
    var propStr = this.containerCss( propName );
    var prop = this.parse( propName, propStr );
    return prop;
  };

  $$.styfn.containerPropertyAsString = function( propName ){
    var prop = this.containerProperty( propName );

    if( prop ){
      return prop.strValue;
    }
  };

})( cytoscape, typeof window === 'undefined' ? null : window );
;(function($$){ 'use strict';

  // gets the rendered style for an element
  $$.styfn.getRenderedStyle = function( ele ){
    var ele = ele[0]; // insure it's an element

    if( ele ){
      var rstyle = {};
      var style = ele._private.style;
      var cy = this._private.cy;
      var zoom = cy.zoom();

      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var styleProp = style[ prop.name ];

        if( styleProp ){
          var val = styleProp.unitless ? styleProp.strValue : (styleProp.pxValue * zoom) + 'px';
          rstyle[ prop.name ] = val;
          rstyle[ $$.util.dash2camel(prop.name) ] = val;
        }
      }

      return rstyle;
    }
  };

  // gets the raw style for an element
  $$.styfn.getRawStyle = function( ele ){
    var ele = ele[0]; // insure it's an element

    if( ele ){
      var rstyle = {};
      var style = ele._private.style;

      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var styleProp = style[ prop.name ];

        if( styleProp ){
          rstyle[ prop.name ] = styleProp.strValue;
          rstyle[ $$.util.dash2camel(prop.name) ] = styleProp.strValue;
        }
      }

      return rstyle;
    }
  };

  // gets the value style for an element (useful for things like animations)
  $$.styfn.getValueStyle = function( ele, opts ){
    opts = opts || {};

    var rstyle = opts.array ? [] : {}; 
    var style;

    if( $$.is.element(ele) ){
      style = ele._private.style;    
    } else {
      style = ele; // just passed the style itself
    }

    if( style ){
      for( var i = 0; i < $$.style.properties.length; i++ ){
        var prop = $$.style.properties[i];
        var styleProp = style[ prop.name ] || style[ $$.util.dash2camel(prop.name) ];

        if( styleProp !== undefined && !$$.is.plainObject( styleProp ) ){ // then make a prop of it
          styleProp = this.parse(prop.name, styleProp);
        }

        if( styleProp ){
          if( opts.array ){
            rstyle.push( styleProp );
          } else {
            rstyle[ prop.name ] = styleProp;
            rstyle[ $$.util.dash2camel(prop.name) ] = styleProp;
          }
        }
      }
    }

    return rstyle;
  };

})( cytoscape );
;(function($$){ 'use strict';

  $$.style.applyFromJson = function( style, json ){
    for( var i = 0; i < json.length; i++ ){
      var context = json[i];
      var selector = context.selector;
      var props = context.css;

      style.selector(selector); // apply selector

      for( var name in props ){
        var value = props[name];

        style.css( name, value ); // apply property
      }
    }

    return style;
  };

  // static function
  $$.style.fromJson = function( cy, json ){
    var style = new $$.Style(cy);

    $$.style.applyFromJson( style, json );

    return style;
  };

  // accessible cy.style() function
  $$.styfn.fromJson = function( json ){
    var style = this;

    style.resetToDefault();

    $$.style.applyFromJson( style, json );

    return style;
  };

  // get json from cy.style() api
  $$.styfn.json = function(){
    var json = [];

    for( var i = this.defaultLength; i < this.length; i++ ){
      var cxt = this[i];
      var selector = cxt.selector;
      var props = cxt.properties;
      var css = {};

      for( var j = 0; j < props.length; j++ ){
        var prop = props[j];
        css[ prop.name ] = prop.strValue;
      }

      json.push({
        selector: !selector ? 'core' : selector.toString(),
        css: css
      });
    }

    return json;
  };

})( cytoscape );
;(function($$){ 'use strict';

  $$.style.applyFromString = function( style, string ){
    var remaining = '' + string;
    var selAndBlockStr;
    var blockRem;
    var propAndValStr;

    // remove comments from the style string
    remaining = remaining.replace(/[/][*](\s|.)+?[*][/]/g, '');

    function removeSelAndBlockFromRemaining(){
      // remove the parsed selector and block from the remaining text to parse
      if( remaining.length > selAndBlockStr.length ){
        remaining = remaining.substr( selAndBlockStr.length );
      } else {
        remaining = '';
      }
    }

    function removePropAndValFromRem(){
      // remove the parsed property and value from the remaining block text to parse
      if( blockRem.length > propAndValStr.length ){
        blockRem = blockRem.substr( propAndValStr.length );
      } else {
        blockRem = '';
      }
    }

    while(true){
      var nothingLeftToParse = remaining.match(/^\s*$/);
      if( nothingLeftToParse ){ break; }

      var selAndBlock = remaining.match(/^\s*((?:.|\s)+?)\s*\{((?:.|\s)+?)\}/);

      if( !selAndBlock ){
        $$.util.error('Halting stylesheet parsing: String stylesheet contains more to parse but no selector and block found in: ' + remaining);
        break;
      }

      selAndBlockStr = selAndBlock[0];

      // parse the selector
      var selectorStr = selAndBlock[1];
      var selector = new $$.Selector( selectorStr );
      if( selector._private.invalid && selectorStr !== 'core' ){
        $$.util.error('Skipping parsing of block: Invalid selector found in string stylesheet: ' + selectorStr);

        // skip this selector and block
        removeSelAndBlockFromRemaining();
        continue; 
      }

      // parse the block of properties and values
      var blockStr = selAndBlock[2];
      var invalidBlock = false;
      blockRem = blockStr;
      var props = [];

      while(true){
        var nothingLeftToParse = blockRem.match(/^\s*$/);
        if( nothingLeftToParse ){ break; }

        var propAndVal = blockRem.match(/^\s*(.+?)\s*:\s*(.+?)\s*;/);

        if( !propAndVal ){
          $$.util.error('Skipping parsing of block: Invalid formatting of style property and value definitions found in:' + blockStr);
          invalidBlock = true;
          break;
        }

        propAndValStr = propAndVal[0];
        var propStr = propAndVal[1];
        var valStr = propAndVal[2];

        var prop = $$.style.properties[ propStr ];
        if( !prop ){
          $$.util.error('Skipping property: Invalid property name in: ' + propAndValStr);

          // skip this property in the block
          removePropAndValFromRem();
          continue;
        }

        var parsedProp = style.parse( propStr, valStr );

        if( !parsedProp ){
          $$.util.error('Skipping property: Invalid property definition in: ' + propAndValStr);

          // skip this property in the block
          removePropAndValFromRem();
          continue;
        }

        props.push({
          name: propStr,
          val: valStr
        });
        removePropAndValFromRem();
      }

      if( invalidBlock ){
        removeSelAndBlockFromRemaining();
        break;
      }

      // put the parsed block in the style
      style.selector( selectorStr );
      for( var i = 0; i < props.length; i++ ){
        var prop = props[i];
        style.css( prop.name, prop.val );
      }

      removeSelAndBlockFromRemaining();
    }

    return style;
  };

  $$.style.fromString = function( cy, string ){
    var style = new $$.Style(cy);
    
    $$.style.applyFromString( style, string );

    return style;
  };

  $$.styfn.fromString = function( string ){
    var style = this;

    style.resetToDefault();

    $$.style.applyFromString( style, string );

    return style;
  };

})( cytoscape );

;(function($$){ 'use strict';

  // a dummy stylesheet object that doesn't need a reference to the core
  // (useful for init)
  $$.stylesheet = $$.Stylesheet = function(){
    if( !(this instanceof $$.Stylesheet) ){
      return new $$.Stylesheet();
    }

    this.length = 0;
  };

  // just store the selector to be parsed later
  $$.Stylesheet.prototype.selector = function( selector ){
    var i = this.length++;

    this[i] = {
      selector: selector,
      properties: []
    };

    return this; // chaining
  };

  // just store the property to be parsed later
  $$.Stylesheet.prototype.css = function( name, value ){
    var i = this.length - 1;

    if( $$.is.string(name) ){
      this[i].properties.push({
        name: name,
        value: value
      });
    } else if( $$.is.plainObject(name) ){
      var map = name;

      for( var j = 0; j < $$.style.properties.length; j++ ){
        var prop = $$.style.properties[j];
        var mapVal = map[ prop.name ];

        if( mapVal === undefined ){ // also try camel case name
          mapVal = map[ $$.util.dash2camel(prop.name) ];
        }

        if( mapVal !== undefined ){
          var name = prop.name;
          var value = mapVal;

          this[i].properties.push({
            name: name,
            value: value
          });
        }
      }
    }

    return this; // chaining
  };

  // generate a real style object from the dummy stylesheet
  $$.Stylesheet.prototype.generateStyle = function( cy ){
    var style = new $$.Style(cy);

    for( var i = 0; i < this.length; i++ ){
      var context = this[i];
      var selector = context.selector;
      var props = context.properties;

      style.selector(selector); // apply selector

      for( var j = 0; j < props.length; j++ ){
        var prop = props[j];

        style.css( prop.name, prop.value ); // apply property
      }
    }

    return style;
  };

})( cytoscape );
;(function($$, window){ 'use strict';

  var isTouch = $$.is.touch();

  var defaults = {
  };
  
  var origDefaults = $$.util.copy( defaults );

  $$.defaults = function( opts ){
    defaults = $$.util.extend({}, origDefaults, opts);
  };

  $$.fn.core = function( fnMap, options ){
    for( var name in fnMap ){
      var fn = fnMap[name];
      $$.Core.prototype[ name ] = fn;
    }
  };
  
  $$.Core = function( opts ){
    if( !(this instanceof $$.Core) ){
      return new $$.Core(opts);
    }
    var cy = this;

    opts = $$.util.extend({}, defaults, opts);

    var container = opts.container;
    var reg = container ? container._cyreg : null; // e.g. already registered some info (e.g. readies) via jquery
    reg = reg || {};

    if( reg && reg.cy ){ 
      if( container ){
        while( container.firstChild ){ // clean the container
          container.removeChild( container.firstChild );
        }
      }
      
      reg.cy.notify({ type: 'destroy' }); // destroy the renderer

      reg = {}; // old instance => replace reg completely
    }

    var readies = reg.readies = reg.readies || [];
    
    if( container ){ container._cyreg = reg; } // make sure container assoc'd reg points to this cy
    reg.cy = cy;

    var head = window !== undefined && container !== undefined && !opts.headless;
    var options = opts;
    options.layout = $$.util.extend( { name: head ? 'grid' : 'null' }, options.layout );
    options.renderer = $$.util.extend( { name: head ? 'canvas' : 'null' }, options.renderer );
    
    var defVal = function( def, val, altVal ){
      if( val !== undefined ){
        return val;
      } else if( altVal !== undefined ){
        return altVal;
      } else {
        return def;
      }
    };

    var _p = this._private = {
      container: options.container, // html dom ele container
      ready: false, // whether ready has been triggered
      initrender: false, // has initrender has been triggered
      options: options, // cached options
      elements: [], // array of elements
      id2index: {}, // element id => index in elements array
      listeners: [], // list of listeners
      aniEles: $$.Collection(this), // elements being animated
      scratch: {}, // scratch object for core
      layout: null,
      renderer: null,
      notificationsEnabled: true, // whether notifications are sent to the renderer
      minZoom: 1e-50,
      maxZoom: 1e50,
      zoomingEnabled: defVal(true, options.zoomingEnabled),
      userZoomingEnabled: defVal(true, options.userZoomingEnabled),
      panningEnabled: defVal(true, options.panningEnabled),
      userPanningEnabled: defVal(true, options.userPanningEnabled),
      boxSelectionEnabled: defVal(false, options.boxSelectionEnabled),
      autolock: defVal(false, options.autolock, options.autolockNodes),
      autoungrabify: defVal(false, options.autoungrabify, options.autoungrabifyNodes),
      autounselectify: defVal(false, options.autounselectify),
      styleEnabled: options.styleEnabled === undefined ? head : options.styleEnabled,
      zoom: $$.is.number(options.zoom) ? options.zoom : 1,
      pan: {
        x: $$.is.plainObject(options.pan) && $$.is.number(options.pan.x) ? options.pan.x : 0,
        y: $$.is.plainObject(options.pan) && $$.is.number(options.pan.y) ? options.pan.y : 0
      },
      animation: { // object for currently-running animations
        current: [],
        queue: []
      },
      hasCompoundNodes: false,
      deferredExecQueue: []
    };

    // set selection type
    var selType = options.selectionType;
    if( selType === undefined || (selType !== 'additive' && selType !== 'single') ){
      // then set default

      if( isTouch ){
        _p.selectionType = 'additive';
      } else {
        _p.selectionType = 'single';
      }
    } else {
      _p.selectionType = selType;
    }

    // init zoom bounds
    if( $$.is.number(options.minZoom) && $$.is.number(options.maxZoom) && options.minZoom < options.maxZoom ){
      _p.minZoom = options.minZoom;
      _p.maxZoom = options.maxZoom;
    } else if( $$.is.number(options.minZoom) && options.maxZoom === undefined ){
      _p.minZoom = options.minZoom;
    } else if( $$.is.number(options.maxZoom) && options.minZoom === undefined ){
      _p.maxZoom = options.maxZoom;
    }

    // init style
    if( _p.styleEnabled ){
      this.setStyle( options.style );
    }

    // create the renderer
    cy.initRenderer( $$.util.extend({
      hideEdgesOnViewport: options.hideEdgesOnViewport,
      hideLabelsOnViewport: options.hideLabelsOnViewport,
      textureOnViewport: options.textureOnViewport,
      wheelSensitivity: $$.is.number(options.wheelSensitivity) && options.wheelSensitivity > 0 ? options.wheelSensitivity : 1,
      motionBlur: options.motionBlur,
      pixelRatio: $$.is.number(options.pixelRatio) && options.pixelRatio > 0 ? options.pixelRatio : (options.pixelRatio === 'auto' ? undefined : 1),
      tapThreshold: defVal( $$.is.touch() ? 8 : 4, $$.is.touch() ? options.touchTapThreshold : options.desktopTapThreshold )
    }, options.renderer) );

    // trigger the passed function for the `initrender` event
    if( options.initrender ){
      cy.on('initrender', options.initrender);
      cy.on('initrender', function(){
        cy._private.initrender = true;
      });
    }

    // initial load
    cy.load(options.elements, function(){ // onready
      cy.startAnimationLoop();
      cy._private.ready = true;

      // if a ready callback is specified as an option, the bind it
      if( $$.is.fn( options.ready ) ){
        cy.on('ready', options.ready);
      }

      // bind all the ready handlers registered before creating this instance
      for( var i = 0; i < readies.length; i++ ){
        var fn = readies[i];
        cy.on('ready', fn);
      }
      if( reg ){ reg.readies = []; } // clear b/c we've bound them all and don't want to keep it around in case a new core uses the same div etc
      
      cy.trigger('ready');
    }, options.done);
  };

  $$.corefn = $$.Core.prototype; // short alias
  

  $$.fn.core({
    isReady: function(){
      return this._private.ready;
    },

    ready: function( fn ){
      if( this.isReady() ){
        this.trigger('ready', [], fn); // just calls fn as though triggered via ready event
      } else {
        this.on('ready', fn);
      }
    },

    initrender: function(){
      return this._private.initrender;
    },

    destroy: function(){
      this.notify({ type: 'destroy' }); // destroy the renderer

      var domEle = this.container();
      var parEle = domEle.parentNode;
      if( parEle ){
        parEle.removeChild( domEle );
      }

      return this;
    },

    getElementById: function( id ){
      var index = this._private.id2index[ id ];
      if( index !== undefined ){
        return this._private.elements[ index ];
      }

      // worst case, return an empty collection
      return new $$.Collection( this );
    },

    selectionType: function(){
      return this._private.selectionType;
    },

    hasCompoundNodes: function(){
      return this._private.hasCompoundNodes;
    },

    styleEnabled: function(){
      return this._private.styleEnabled;
    },

    addToPool: function( eles ){
      var elements = this._private.elements;
      var id2index = this._private.id2index;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];

        var id = ele._private.data.id;
        var index = id2index[ id ];
        var alreadyInPool = index !== undefined;

        if( !alreadyInPool ){
          index = elements.length;
          elements.push( ele );
          id2index[ id ] = index;
          ele._private.index = index;
        }
      }

      return this; // chaining
    },

    removeFromPool: function( eles ){
      var elements = this._private.elements;
      var id2index = this._private.id2index;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];

        var id = ele._private.data.id;
        var index = id2index[ id ];
        var inPool = index !== undefined;

        if( inPool ){
          this._private.id2index[ id ] = undefined;
          elements.splice(index, 1);

          // adjust the index of all elements past this index
          for( var j = index; j < elements.length; j++ ){
            var jid = elements[j]._private.data.id;
            id2index[ jid ]--;
            elements[j]._private.index--;
          }
        }
      }
    },

    container: function(){
      return this._private.container;
    },

    options: function(){
      return $$.util.copy( this._private.options );
    },
    
    json: function(params){
      var json = {};
      var cy = this;
      
      json.elements = {};
      cy.elements().each(function(i, ele){
        var group = ele.group();
        
        if( !json.elements[group] ){
          json.elements[group] = [];
        }
        
        json.elements[group].push( ele.json() );
      });

      if( this._private.styleEnabled ){
        json.style = cy.style().json();
      }

      json.zoomingEnabled = cy._private.zoomingEnabled;
      json.userZoomingEnabled = cy._private.userZoomingEnabled;
      json.zoom = cy._private.zoom;
      json.minZoom = cy._private.minZoom;
      json.maxZoom = cy._private.maxZoom;
      json.panningEnabled = cy._private.panningEnabled;
      json.userPanningEnabled = cy._private.userPanningEnabled;
      json.pan = cy._private.pan;
      json.boxSelectionEnabled = cy._private.boxSelectionEnabled;
      json.layout = cy._private.options.layout;
      json.renderer = cy._private.options.renderer;
      json.hideEdgesOnViewport = cy._private.options.hideEdgesOnViewport;
      json.hideLabelsOnViewport = cy._private.options.hideLabelsOnViewport;
      json.textureOnViewport = cy._private.options.textureOnViewport;
      json.wheelSensitivity = cy._private.options.wheelSensitivity;
      json.motionBlur = cy._private.options.motionBlur;
      
      return json;
    },

    // defer execution until not busy and guarantee relative execution order of deferred functions
    defer: function( fn ){
      var cy = this;
      var _p = cy._private;
      var q = _p.deferredExecQueue;

      q.push( fn );

      if( !_p.deferredTimeout ){
        _p.deferredTimeout = setTimeout(function(){
          while( q.length > 0 ){
            ( q.shift() )();
          }

          _p.deferredTimeout = null;
        }, 0);
      }
    }
    
  });  
  
})( cytoscape, typeof window === 'undefined' ? null : window );

(function($$, window){ 'use strict';

  function ready(f) {
    var fn = ( document && (document.readyState === 'interactive' || document.readyState === 'complete') )  ? f : ready;

    setTimeout(fn, 9, f);
  }

  $$.fn.core({
    add: function(opts){
      
      var elements;
      var cy = this;
      
      // add the elements
      if( $$.is.elementOrCollection(opts) ){
        var eles = opts;

        if( eles._private.cy === cy ){ // same instance => just restore
          elements = eles.restore();

        } else { // otherwise, copy from json
          var jsons = [];

          for( var i = 0; i < eles.length; i++ ){
            var ele = eles[i];
            jsons.push( ele.json() );
          }

          elements = new $$.Collection( cy, jsons );
        }
      }
      
      // specify an array of options
      else if( $$.is.array(opts) ){
        var jsons = opts;

        elements = new $$.Collection(cy, jsons);
      }
      
      // specify via opts.nodes and opts.edges
      else if( $$.is.plainObject(opts) && ($$.is.array(opts.nodes) || $$.is.array(opts.edges)) ){
        var elesByGroup = opts;
        var jsons = [];

        var grs = ['nodes', 'edges'];
        for( var i = 0, il = grs.length; i < il; i++ ){
          var group = grs[i];
          var elesArray = elesByGroup[group];

          if( $$.is.array(elesArray) ){

            for( var j = 0, jl = elesArray.length; j < jl; j++ ){
              var json = elesArray[j];
              json.group = group;

              jsons.push( json );
            }
          } 
        }

        elements = new $$.Collection(cy, jsons);
      }
      
      // specify options for one element
      else {
        var json = opts;
        elements = (new $$.Element( cy, json )).collection();
      }
      
      return elements;
    },
    
    remove: function(collection){
      if( $$.is.elementOrCollection(collection) ){
        collection = collection;
      } else if( $$.is.string(collection) ){
        var selector = collection;
        collection = this.$( selector );
      }
      
      return collection.remove();
    },
    
    load: function(elements, onload, ondone){
      var cy = this;
      
      cy.notifications(false);

      // remove old elements
      var oldEles = cy.elements();
      if( oldEles.length > 0 ){
        oldEles.remove();
      }
      
      if( elements != null ){
        if( $$.is.plainObject(elements) || $$.is.array(elements) ){
          cy.add( elements );
        } 
      }
      
      function callback(){        
        cy.one('layoutready', function(e){
          cy.notifications(true);
          cy.trigger(e); // we missed this event by turning notifications off, so pass it on

          cy.notify({
            type: 'load',
            collection: cy.elements()
          });

          cy.one('load', onload);
          cy.trigger('load');
        }).one('layoutstop', function(){
          cy.one('done', ondone);
          cy.trigger('done');
        });
        
        var layoutOpts = $$.util.extend({}, cy._private.options.layout);
        layoutOpts.eles = cy.$();

        cy.layout( layoutOpts );

      }

      if( window ){
        ready( callback );
      } else {
        callback();
      }

      return this;
    }
  });
  
})( cytoscape, typeof window === 'undefined' ? null : window );

;(function($$, window){ 'use strict';
  
  $$.fn.core({
    
    // pull in animation functions
    animated: $$.define.animated(),
    clearQueue: $$.define.clearQueue(),
    delay: $$.define.delay(),
    animate: $$.define.animate(),
    stop: $$.define.stop(),

    addToAnimationPool: function( eles ){
      var cy = this;

      if( !cy.styleEnabled() ){ return; } // save cycles when no style used
      
      cy._private.aniEles.merge( eles );
    },

    startAnimationLoop: function(){
      var cy = this;

      if( !cy.styleEnabled() ){ return; } // save cycles when no style used

      // don't execute the animation loop in headless environments
      if( !window ){
        return;
      }
      
      function globalAnimationStep(){
        $$.util.requestAnimationFrame(function(now){
          handleElements(now);
          globalAnimationStep();
        });
      }
      
      globalAnimationStep(); // first call
      
      function handleElements(now){
        now = +new Date();

        var eles = cy._private.aniEles;
        var doneEles = [];

        function handleElement( ele, isCore ){
          var current = ele._private.animation.current;
          var queue = ele._private.animation.queue;
          var ranAnis = false;
          
          // if nothing currently animating, get something from the queue
          if( current.length === 0 ){
            var next = queue.length > 0 ? queue.shift() : null;
            
            if( next ){
              next.callTime = now; // was queued, so update call time
              current.push( next );
            }
          }
          
          // step and remove if done
          var completes = [];
          for(var i = current.length - 1; i >= 0; i--){
            var ani = current[i];

            // start if need be
            if( !ani.started ){ startAnimation( ele, ani ); }
            
            step( ele, ani, now, isCore );

            if( ani.done ){
              completes.push( ani );
              
              // remove current[i]
              current.splice(i, 1);
            }

            ranAnis = true;
          }
          
          // call complete callbacks
          for( var i = 0; i < completes.length; i++ ){
            var ani = completes[i];
            var complete = ani.params.complete;

            if( $$.is.fn(complete) ){
              complete.apply( ele, [ now ] );
            }
          }

          if( !isCore && current.length === 0 && queue.length === 0 ){
            doneEles.push( ele );
          }

          return ranAnis;
        } // handleElements

        // handle all eles
        for( var e = 0; e < eles.length; e++ ){
          var ele = eles[e];
          
          handleElement( ele );
        } // each element

        var ranCoreAni = handleElement( cy, true );
        
        // notify renderer
        if( eles.length > 0 || ranCoreAni ){
          var toNotify;

          if( eles.length > 0 ){
            var updatedEles = eles.updateCompoundBounds();
            toNotify = updatedEles.length > 0 ? eles.add( updatedEles ) : eles;
          }

          cy.notify({
            type: 'draw',
            collection: toNotify
          });
        }

        // remove elements from list of currently animating if its queues are empty
        eles.unmerge( doneEles );

      } // handleElements
      
      function startAnimation( self, ani ){
        var isCore = $$.is.core( self );
        var isEles = !isCore;
        var ele = self;
        var style = cy._private.style;

        if( isEles ){
          var pos = ele._private.position;
          var startPosition = {
            x: pos.x,
            y: pos.y
          };
          var startStyle = style.getValueStyle( ele );
        }

        if( isCore ){
          var pan = cy._private.pan;
          var startPan = {
            x: pan.x,
            y: pan.y
          };

          var startZoom = cy._private.zoom;
        }

        ani.started = true;
        ani.startTime = Date.now();
        ani.startPosition = startPosition;
        ani.startStyle = startStyle;
        ani.startPan = startPan;
        ani.startZoom = startZoom;
      }

      function step( self, animation, now, isCore ){
        var style = cy._private.style;
        var properties = animation.properties;
        var params = animation.params;
        var startTime = animation.startTime;
        var percent;
        var isEles = !isCore;
        
        if( animation.duration === 0 ){
          percent = 1;
        } else {
          percent = Math.min(1, (now - startTime)/animation.duration);
        }

        if( percent < 0 ){
          percent = 0;
        } else if( percent > 1 ){
          percent = 1;
        }
        
        if( properties.delay == null ){ // then update

          var startPos = animation.startPosition;
          var endPos = properties.position;
          var pos = self._private.position;
          if( endPos && isEles ){
            if( valid( startPos.x, endPos.x ) ){
              pos.x = ease( startPos.x, endPos.x, percent );
            }

            if( valid( startPos.y, endPos.y ) ){
              pos.y = ease( startPos.y, endPos.y, percent );
            }
          }

          var startPan = animation.startPan;
          var endPan = properties.pan;
          var pan = self._private.pan;
          var animatingPan = endPan != null && isCore;
          if( animatingPan ){
            if( valid( startPan.x, endPan.x ) ){
              pan.x = ease( startPan.x, endPan.x, percent );
            }

            if( valid( startPan.y, endPan.y ) ){
              pan.y = ease( startPan.y, endPan.y, percent );
            }

            self.trigger('pan');
          }

          var startZoom = animation.startZoom;
          var endZoom = properties.zoom;
          var animatingZoom = endZoom != null && isCore;
          if( animatingZoom ){
            if( valid( startZoom, endZoom ) ){
              self._private.zoom = ease( startZoom, endZoom, percent );
            }

            self.trigger('zoom');
          }

          if( animatingPan || animatingZoom ){
            self.trigger('viewport');
          }

          if( properties.css && isEles ){
            var props = properties.css;

            for( var i = 0; i < props.length; i++ ){
              var name = props[i].name;
              var prop = props[i];
              var end = prop;

              var start = animation.startStyle[ name ];
              var easedVal = ease( start, end, percent );
              
              style.overrideBypass( self, name, easedVal );
            } // for props
          } // if 

        }
        
        if( $$.is.fn(params.step) ){
          params.step.apply( self, [ now ] );
        }
        
        if( percent >= 1 ){
          animation.done = true;
        }
        
        return percent;
      }
      
      function valid(start, end){
        if( start == null || end == null ){
          return false;
        }
        
        if( $$.is.number(start) && $$.is.number(end) ){
          return true;
        } else if( (start) && (end) ){
          return true;
        }
        
        return false;
      }
      
      function ease(startProp, endProp, percent){
        if( percent < 0 ){
          percent = 0;
        } else if( percent > 1 ){
          percent = 1;
        }

        var start, end;

        if( startProp.pxValue != null || startProp.value != null ){
          start = startProp.pxValue != null ? startProp.pxValue : startProp.value;
        } else {
          start = startProp;
        }

        if( endProp.pxValue != null || endProp.value != null ){
          end = endProp.pxValue != null ? endProp.pxValue : endProp.value;
        } else {
          end = endProp;
        }

        if( $$.is.number(start) && $$.is.number(end) ){
          return start + (end - start) * percent;

        } else if( $$.is.number(start[0]) && $$.is.number(end[0]) ){ // then assume a colour
          var c1 = start;
          var c2 = end;

          var ch = function(ch1, ch2){
            var diff = ch2 - ch1;
            var min = ch1;
            return Math.round( percent * diff + min );
          };
          
          var r = ch( c1[0], c2[0] );
          var g = ch( c1[1], c2[1] );
          var b = ch( c1[2], c2[2] );
          
          return [r, g, b];
        }
        
        return undefined;
      }
      
    }
    
  });
  
})( cytoscape, typeof window === 'undefined' ? null : window );


  
    
;(function($$){ 'use strict';
  
  $$.fn.core({
    data: $$.define.data({
      field: 'data',
      bindingEvent: 'data',
      allowBinding: true,
      allowSetting: true,
      settingEvent: 'data',
      settingTriggersEvent: true,
      triggerFnName: 'trigger',
      allowGetting: true
    }),

    removeData: $$.define.removeData({
      field: 'data',
      event: 'data',
      triggerFnName: 'trigger',
      triggerEvent: true
    }),

    scratch: $$.define.data({
      field: 'scratch',
      allowBinding: false,
      allowSetting: true,
      settingTriggersEvent: false,
      allowGetting: true
    }),

    removeScratch: $$.define.removeData({
      field: 'scratch',
      triggerEvent: false
    })
  });
  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.core({
    on: $$.define.on(), // .on( events [, selector] [, data], handler)
    one: $$.define.on({ unbindSelfOnTrigger: true }),
    once: $$.define.on({ unbindAllBindersOnTrigger: true }),
    off: $$.define.off(), // .off( events [, selector] [, handler] )
    trigger: $$.define.trigger() // .trigger( events [, extraParams] )
  });

  // aliases for those folks who like old stuff:
  $$.corefn.bind = $$.corefn.on;
  $$.corefn.unbind = $$.corefn.off;

})( cytoscape );

;(function($$){ 'use strict';
  
  $$.fn.core({
    
    png: function( options ){
      var renderer = this._private.renderer;
      options = options || {};

      return renderer.png( options );      
    }
    
  });
  
})( cytoscape );
;(function($$){ 'use strict';
  
  $$.fn.core({
    
    layout: function( params ){
      var layout;

      // always use a new layout w/ init opts; slightly different backwards compatibility
      // but fixes layout reuse issues like dagre #819 
      if( params == null ){ 
        params = $$.util.extend({}, this._private.options.layout);
        params.eles = this.$();
      }

      layout = this.initLayout( params );
      layout.run();

      return this; // chaining
    },

    makeLayout: function( params ){
      return this.initLayout( params );
    },
    
    initLayout: function( options ){
      if( options == null ){
        $$.util.error('Layout options must be specified to make a layout');
        return;
      }
      
      if( options.name == null ){
        $$.util.error('A `name` must be specified to make a layout');
        return;
      }
      
      var name = options.name;
      var LayoutProto = $$.extension('layout', name);
      
      if( LayoutProto == null ){
        $$.util.error('Can not apply layout: No such layout `' + name + '` found; did you include its JS file?');
        return;
      }

      options.eles = options.eles != null ? options.eles : this.$();

      if( $$.is.string( options.eles ) ){
        options.eles = this.$( options.eles );
      }
      
      var layout = new LayoutProto( $$.util.extend({}, options, {
        cy: this
      }) );

      // make sure layout has _private for use w/ std apis like .on()
      if( !$$.is.plainObject(layout._private) ){
        layout._private = {};
      }

      layout._private.cy = this;
      layout._private.listeners = [];
      
      return layout;
    }
    
  });
  
})( cytoscape );
(function($$){ 'use strict';
  
  $$.fn.core({
    notify: function( params ){
      if( this._private.batchingNotify ){
        var bEles = this._private.batchNotifyEles;
        var bTypes = this._private.batchNotifyTypes;

        if( params.collection ){ for( var i = 0; i < params.collection.length; i++ ){
          var ele = params.collection[i];

          if( !bEles.ids[ ele._private.id ] ){
            bEles.push( ele );
          }
        } }

        if( !bTypes.ids[ params.type ] ){
          bTypes.push( params.type );
        }

        return; // notifications are disabled during batching
      }

      if( !this._private.notificationsEnabled ){ return; } // exit on disabled

      var renderer = this.renderer();
      
      renderer.notify(params);
    },
    
    notifications: function( bool ){
      var p = this._private;
      
      if( bool === undefined ){
        return p.notificationsEnabled;
      } else {
        p.notificationsEnabled = bool ? true : false;
      }
    },
    
    noNotifications: function( callback ){
      this.notifications(false);
      callback();
      this.notifications(true);
    },

    startBatch: function(){
      var _p = this._private;

      _p.batchingStyle = _p.batchingNotify = true;
      _p.batchStyleEles = [];
      _p.batchNotifyEles = [];
      _p.batchNotifyTypes = [];

      _p.batchStyleEles.ids = {};
      _p.batchNotifyEles.ids = {};
      _p.batchNotifyTypes.ids = {};

      return this;
    },

    endBatch: function(){
      var _p = this._private;

      // update style for dirty eles
      _p.batchingStyle = false;
      new $$.Collection(this, _p.batchStyleEles).updateStyle();

      // notify the renderer of queued eles and event types
      _p.batchingNotify = false;
      this.notify({
        type: _p.batchNotifyTypes,
        collection: _p.batchNotifyEles
      });

      return this;
    },

    batch: function( callback ){
      this.startBatch();
      callback();
      this.endBatch();

      return this;
    },

    // for backwards compatibility
    batchData: function( map ){
      var cy = this;

      return this.batch(function(){
        for( var id in map ){
          var data = map[id];
          var ele = cy.getElementById( id );
          
          ele.data( data );
        }
      });
    }
  });
  
})( cytoscape );

;(function($$){ 'use strict';
  
  $$.fn.core({
    
    renderTo: function( context, zoom, pan, pxRatio ){
      var r = this._private.renderer;

      r.renderTo( context, zoom, pan, pxRatio );
      return this;
    },

    renderer: function(){
      return this._private.renderer;
    },

    forceRender: function(){
      this.notify({
        type: 'draw'
      });

      return this;
    },

    resize: function(){
      this.notify({
        type: 'resize'
      });

      this.trigger('resize');

      return this;
    },
    
    initRenderer: function( options ){
      var cy = this;

      var RendererProto = $$.extension('renderer', options.name);
      if( RendererProto == null ){
        $$.util.error('Can not initialise: No such renderer `%s` found; did you include its JS file?', options.name);
        return;
      }
      
      this._private.renderer = new RendererProto(
        $$.util.extend({}, options, {
          cy: cy,
          style: cy._private.style
        })
      );
       
    }
    
  });  
  
})( cytoscape );
;(function($$){ 'use strict';
  
  $$.fn.core({

    // get a collection
    // - empty collection on no args
    // - collection of elements in the graph on selector arg
    // - guarantee a returned collection when elements or collection specified
    collection: function( eles ){

      if( $$.is.string( eles ) ){
        return this.$( eles );

      } else if( $$.is.elementOrCollection( eles ) ){
        return eles.collection();

      } else if( $$.is.array( eles ) ){
        return new $$.Collection( this, eles );
      }

      return new $$.Collection( this );
    },
    
    nodes: function( selector ){
      var nodes = this.$(function(){
        return this.isNode();
      });

      if( selector ){
        return nodes.filter( selector );
      } 

      return nodes;
    },
    
    edges: function( selector ){
      var edges = this.$(function(){
        return this.isEdge();
      });

      if( selector ){
        return edges.filter( selector );
      }

      return edges;
    },
      
    // search the graph like jQuery
    $: function( selector ){
      var eles = new $$.Collection( this, this._private.elements );

      if( selector ){
        return eles.filter( selector );
      }

      return eles;
    }
    
  });  

  // aliases
  $$.corefn.elements = $$.corefn.filter = $$.corefn.$;  
  
})( cytoscape );

;(function($$){ 'use strict';
  
  $$.fn.core({
    
    style: function( newStyle ){
      if( newStyle ){
        var s = this.setStyle( newStyle );

        s.update();
      }

      return this._private.style;
    },

    setStyle: function( style ){
      var _p = this._private;

      if( $$.is.stylesheet(style) ){
        _p.style = style.generateStyle(this);
      
      } else if( $$.is.array(style) ) {
        _p.style = $$.style.fromJson(this, style);
      
      } else if( $$.is.string(style) ){
        _p.style = $$.style.fromString(this, style);
      
      } else {
        _p.style = new $$.Style( this );
      }

      return _p.style;
    }
  });
  
})( cytoscape );


;(function($$){ 'use strict';
  
  $$.fn.core({

    autolock: function(bool){
      if( bool !== undefined ){
        this._private.autolock = bool ? true : false;
      } else {
        return this._private.autolock;
      }
      
      return this; // chaining
    },

    autoungrabify: function(bool){
      if( bool !== undefined ){
        this._private.autoungrabify = bool ? true : false;
      } else {
        return this._private.autoungrabify;
      }
      
      return this; // chaining
    },

    autounselectify: function(bool){
      if( bool !== undefined ){
        this._private.autounselectify = bool ? true : false;
      } else {
        return this._private.autounselectify;
      }
      
      return this; // chaining
    },

    panningEnabled: function( bool ){
      if( bool !== undefined ){
        this._private.panningEnabled = bool ? true : false;
      } else {
        return this._private.panningEnabled;
      }
      
      return this; // chaining
    },

    userPanningEnabled: function( bool ){
      if( bool !== undefined ){
        this._private.userPanningEnabled = bool ? true : false;
      } else {
        return this._private.userPanningEnabled;
      }
      
      return this; // chaining
    },
    
    zoomingEnabled: function( bool ){
      if( bool !== undefined ){
        this._private.zoomingEnabled = bool ? true : false;
      } else {
        return this._private.zoomingEnabled;
      }
      
      return this; // chaining
    },

    userZoomingEnabled: function( bool ){
      if( bool !== undefined ){
        this._private.userZoomingEnabled = bool ? true : false;
      } else {
        return this._private.userZoomingEnabled;
      }
      
      return this; // chaining
    },

    boxSelectionEnabled: function( bool ){
      if( bool !== undefined ){
        this._private.boxSelectionEnabled = bool ? true : false;
      } else {
        return this._private.boxSelectionEnabled;
      }
      
      return this; // chaining
    },
    
    pan: function(){
      var args = arguments;
      var pan = this._private.pan;
      var dim, val, dims, x, y;

      switch( args.length ){
      case 0: // .pan()
        return pan;

      case 1: 

        if( $$.is.string( args[0] ) ){ // .pan('x')
          dim = args[0];
          return pan[ dim ];

        } else if( $$.is.plainObject( args[0] ) ) { // .pan({ x: 0, y: 100 })
          if( !this._private.panningEnabled ){
            return this;
          }

          dims = args[0];
          x = dims.x;
          y = dims.y;

          if( $$.is.number(x) ){
            pan.x = x;
          }

          if( $$.is.number(y) ){
            pan.y = y;
          }

          this.trigger('pan viewport');
        }
        break;

      case 2: // .pan('x', 100)
        if( !this._private.panningEnabled ){
          return this;
        }

        dim = args[0];
        val = args[1];

        if( (dim === 'x' || dim === 'y') && $$.is.number(val) ){
          pan[dim] = val;
        }

        this.trigger('pan viewport');
        break;

      default:
        break; // invalid
      }

      this.notify({ // notify the renderer that the viewport changed
        type: 'viewport'
      });

      return this; // chaining
    },
    
    panBy: function(params){
      var args = arguments;
      var pan = this._private.pan;
      var dim, val, dims, x, y;

      if( !this._private.panningEnabled ){
        return this;
      }

      switch( args.length ){
      case 1: 

        if( $$.is.plainObject( args[0] ) ) { // .panBy({ x: 0, y: 100 })
          dims = args[0];
          x = dims.x;
          y = dims.y;

          if( $$.is.number(x) ){
            pan.x += x;
          }

          if( $$.is.number(y) ){
            pan.y += y;
          }

          this.trigger('pan viewport');
        }
        break;

      case 2: // .panBy('x', 100)
        dim = args[0];
        val = args[1];

        if( (dim === 'x' || dim === 'y') && $$.is.number(val) ){
          pan[dim] += val;
        }

        this.trigger('pan viewport');
        break;

      default:
        break; // invalid
      }

      this.notify({ // notify the renderer that the viewport changed
        type: 'viewport'
      });

      return this; // chaining
    },
    
    fit: function( elements, padding ){
      var viewportState = this.getFitViewport( elements, padding );

      if( viewportState ){
        var _p = this._private;
        _p.zoom = viewportState.zoom;
        _p.pan = viewportState.pan;

        this.trigger('pan zoom viewport');

        this.notify({ // notify the renderer that the viewport changed
          type: 'viewport'
        });
      }

      return this; // chaining
    },

    getFitViewport: function( elements, padding ){
      if( $$.is.number(elements) && padding === undefined ){ // elements is optional
        padding = elements;
        elements = undefined;
      }

      if( !this._private.panningEnabled || !this._private.zoomingEnabled ){
        return;
      }

      var bb;

      if( $$.is.string(elements) ){
        var sel = elements;
        elements = this.$( sel );

      } else if( $$.is.boundingBox(elements) ){ // assume bb
        var bbe = elements;
        bb = {
          x1: bbe.x1,
          y1: bbe.y1,
          x2: bbe.x2,
          y2: bbe.y2
        };

        bb.w = bb.x2 - bb.x1;
        bb.h = bb.y2 - bb.y1;

      } else if( !$$.is.elementOrCollection(elements) ){
        elements = this.elements();
      }

      bb = bb || elements.boundingBox();

      var w = this.width();
      var h = this.height();
      var zoom;
      padding = $$.is.number(padding) ? padding : 0;

      if( !isNaN(w) && !isNaN(h) && w > 0 && h > 0 && !isNaN(bb.w) && !isNaN(bb.h) &&  bb.w > 0 && bb.h > 0 ){
        zoom = Math.min( (w - 2*padding)/bb.w, (h - 2*padding)/bb.h );

        // crop zoom
        zoom = zoom > this._private.maxZoom ? this._private.maxZoom : zoom;
        zoom = zoom < this._private.minZoom ? this._private.minZoom : zoom;

        var pan = { // now pan to middle
          x: (w - zoom*( bb.x1 + bb.x2 ))/2,
          y: (h - zoom*( bb.y1 + bb.y2 ))/2
        };

        return {
          zoom: zoom, 
          pan: pan
        };
      }

      return;
    },
    
    minZoom: function( zoom ){
      if( zoom === undefined ){
        return this._private.minZoom;
      } else if( $$.is.number(zoom) ){
        this._private.minZoom = zoom;
      }

      return this;
    },

    maxZoom: function( zoom ){
      if( zoom === undefined ){
        return this._private.maxZoom;
      } else if( $$.is.number(zoom) ){
        this._private.maxZoom = zoom;
      }

      return this;
    },

    zoom: function( params ){
      var pos; // in rendered px
      var zoom;

      if( params === undefined ){ // then get the zoom
        return this._private.zoom;

      } else if( $$.is.number(params) ){ // then set the zoom
        zoom = params;

      } else if( $$.is.plainObject(params) ){ // then zoom about a point
        zoom = params.level;

        if( params.position ){
          var p = params.position;
          var pan = this._private.pan;
          var z = this._private.zoom;

          pos = { // convert to rendered px
            x: p.x * z + pan.x,
            y: p.y * z + pan.y
          };
        } else if( params.renderedPosition ){
          pos = params.renderedPosition;
        }

        if( pos && !this._private.panningEnabled ){
          return this; // panning disabled
        }
      }

      if( !this._private.zoomingEnabled ){
        return this; // zooming disabled
      }

      if( !$$.is.number(zoom) || ( pos && (!$$.is.number(pos.x) || !$$.is.number(pos.y)) ) ){
        return this; // can't zoom with invalid params
      }

      // crop zoom
      zoom = zoom > this._private.maxZoom ? this._private.maxZoom : zoom;
      zoom = zoom < this._private.minZoom ? this._private.minZoom : zoom;

      if( pos ){ // set zoom about position
        var pan1 = this._private.pan;
        var zoom1 = this._private.zoom;
        var zoom2 = zoom;
        
        var pan2 = {
          x: -zoom2/zoom1 * (pos.x - pan1.x) + pos.x,
          y: -zoom2/zoom1 * (pos.y - pan1.y) + pos.y
        };

        this._private.zoom = zoom;
        this._private.pan = pan2;

        var posChanged = pan1.x !== pan2.x || pan1.y !== pan2.y;
        this.trigger(' zoom ' + (posChanged ? ' pan ' : '') + ' viewport ' );
      
      } else { // just set the zoom
        this._private.zoom = zoom;
        this.trigger('zoom viewport');
      }

      this.notify({ // notify the renderer that the viewport changed
        type: 'viewport'
      });

      return this; // chaining
    },

    viewport: function( opts ){ 
      var _p = this._private;
      var zoomDefd = true;
      var panDefd = true;
      var events = []; // to trigger
      var zoomFailed = false;
      var panFailed = false;

      if( !opts ){ return this; }
      if( !$$.is.number(opts.zoom) ){ zoomDefd = false; }
      if( !$$.is.plainObject(opts.pan) ){ panDefd = false; }
      if( !zoomDefd && !panDefd ){ return this; }

      if( zoomDefd ){
        var z = opts.zoom;

        if( z < _p.minZoom || z > _p.maxZoom || !_p.zoomingEnabled ){
          zoomFailed = true;

        } else {
          _p.zoom = z;

          events.push('zoom');
        }
      }

      if( panDefd && (!zoomFailed || !opts.cancelOnFailedZoom) && _p.panningEnabled ){
        var p = opts.pan;

        if( $$.is.number(p.x) ){
          _p.pan.x = p.x;
          panFailed = false;
        }

        if( $$.is.number(p.y) ){
          _p.pan.y = p.y;
          panFailed = false;
        }

        if( !panFailed ){
          events.push('pan');
        }
      }

      if( events.length > 0 ){
        events.push('viewport');
        this.trigger( events.join(' ') );

        this.notify({
          type: 'viewport'
        });
      }

      return this; // chaining
    },
    
    center: function( elements ){
      var pan = this.getCenterPan( elements );

      if( pan ){
        this._private.pan = pan;

        this.trigger('pan viewport');

        this.notify({ // notify the renderer that the viewport changed
          type: 'viewport'
        });
      }

      return this; // chaining
    },

    getCenterPan: function( elements, zoom ){
      if( !this._private.panningEnabled ){
        return;
      }

      if( $$.is.string(elements) ){
        var selector = elements;
        elements = this.elements( selector );
      } else if( !$$.is.elementOrCollection(elements) ){
        elements = this.elements();
      }

      var bb = elements.boundingBox();
      var w = this.width();
      var h = this.height();
      zoom = zoom === undefined ? this._private.zoom : zoom;

      var pan = { // middle
        x: (w - zoom*( bb.x1 + bb.x2 ))/2,
        y: (h - zoom*( bb.y1 + bb.y2 ))/2
      };
      
      return pan;
    },
    
    reset: function(){
      if( !this._private.panningEnabled || !this._private.zoomingEnabled ){
        return this;
      }

      this.viewport({
        pan: { x: 0, y: 0 },
        zoom: 1
      });
      
      return this; // chaining
    },

    width: function(){
      var container = this._private.container;

      if( container ){
        return container.clientWidth;
      }

      return 1; // fallback if no container (not 0 b/c can be used for dividing etc)
    },

    height: function(){
      var container = this._private.container;

      if( container ){
        return container.clientHeight;
      }

      return 1; // fallback if no container (not 0 b/c can be used for dividing etc)
    },

    extent: function(){
      var pan = this._private.pan;
      var zoom = this._private.zoom;
      var rb = this.renderedExtent();

      var b = {
        x1: ( rb.x1 - pan.x )/zoom,
        x2: ( rb.x2 - pan.x )/zoom,
        y1: ( rb.y1 - pan.y )/zoom,
        y2: ( rb.y2 - pan.y )/zoom,
      };

      b.w = b.x2 - b.x1;
      b.h = b.y2 - b.y1;

      return b;
    },

    renderedExtent: function(){
      var width = this.width();
      var height = this.height();

      return {
        x1: 0,
        y1: 0,
        x2: width,
        y2: height,
        w: width,
        h: height
      };
    }
  });

  // aliases
  $$.corefn.centre = $$.corefn.center;

  // backwards compatibility
  $$.corefn.autolockNodes = $$.corefn.autolock;
  $$.corefn.autoungrabifyNodes = $$.corefn.autoungrabify;

})( cytoscape );

;(function($$){ 'use strict';
  
  // Use this interface to define functions for collections/elements.
  // This interface is good, because it forces you to think in terms
  // of the collections case (more than 1 element), so we don't need
  // notification blocking nonsense everywhere.
  //
  // Other collection-*.js files depend on this being defined first.
  // It's a trade off: It simplifies the code for Collection and 
  // Element integration so much that it's worth it to create the
  // JS dependency.
  //
  // Having this integration guarantees that we can call any
  // collection function on an element and vice versa.

  // e.g. $$.fn.collection({ someFunc: function(){ /* ... */ } })
  $$.fn.collection = $$.fn.eles = function( fnMap, options ){
    for( var name in fnMap ){
      var fn = fnMap[name];

      $$.Collection.prototype[ name ] = fn;
    }
  };
  
  // factory for generating edge ids when no id is specified for a new element
  var idFactory = {
    prefix: {
      nodes: 'n',
      edges: 'e'
    },
    id: {
      nodes: 0,
      edges: 0
    },
    generate: function(cy, element, tryThisId){
      var json = $$.is.element( element ) ? element._private : element;
      var group = json.group;
      var id = tryThisId != null ? tryThisId : this.prefix[group] + this.id[group];
      
      if( cy.getElementById(id).empty() ){
        this.id[group]++; // we've used the current id, so move it up
      } else { // otherwise keep trying successive unused ids
        while( !cy.getElementById(id).empty() ){
          id = this.prefix[group] + ( ++this.id[group] );
        }
      }
      
      return id;
    }
  };
  
  // Element
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  // represents a node or an edge
  $$.Element = function(cy, params, restore){
    if( !(this instanceof $$.Element) ){
      return new $$.Element(cy, params, restore);
    }

    var self = this;
    restore = (restore === undefined || restore ? true : false);
    
    if( cy === undefined || params === undefined || !$$.is.core(cy) ){
      $$.util.error('An element must have a core reference and parameters set');
      return;
    }
    
    // validate group
    if( params.group !== 'nodes' && params.group !== 'edges' ){
      $$.util.error('An element must be of type `nodes` or `edges`; you specified `' + params.group + '`');
      return;
    }
    
    // make the element array-like, just like a collection
    this.length = 1;
    this[0] = this;
    
    // NOTE: when something is added here, add also to ele.json()
    this._private = {
      cy: cy,
      single: true, // indicates this is an element
      data: params.data || {}, // data object
      layoutData: {}, // place for layouts to put calculated stats etc for mappers
      position: params.position || {}, // (x, y) position pair
      autoWidth: undefined, // width and height of nodes calculated by the renderer when set to special 'auto' value
      autoHeight: undefined, 
      listeners: [], // array of bound listeners
      group: params.group, // string; 'nodes' or 'edges'
      style: {}, // properties as set by the style
      rstyle: {}, // properties for style sent from the renderer to the core
      styleCxts: [], // applied style contexts from the styler
      removed: true, // whether it's inside the vis; true if removed (set true here since we call restore)
      selected: params.selected ? true : false, // whether it's selected
      selectable: params.selectable === undefined ? true : ( params.selectable ? true : false ), // whether it's selectable
      locked: params.locked ? true : false, // whether the element is locked (cannot be moved)
      grabbed: false, // whether the element is grabbed by the mouse; renderer sets this privately
      grabbable: params.grabbable === undefined ? true : ( params.grabbable ? true : false ), // whether the element can be grabbed
      active: false, // whether the element is active from user interaction
      classes: {}, // map ( className => true )
      animation: { // object for currently-running animations
        current: [],
        queue: []
      },
      rscratch: {}, // object in which the renderer can store information
      scratch: {}, // scratch objects
      edges: [], // array of connected edges
      children: [] // array of children
    };
    
    // renderedPosition overrides if specified
    if( params.renderedPosition ){
      var rpos = params.renderedPosition;
      var pan = cy.pan();
      var zoom = cy.zoom();

      this._private.position = {
        x: (rpos.x - pan.x)/zoom,
        y: (rpos.y - pan.y)/zoom
      };
    }
    
    if( $$.is.string(params.classes) ){
      var classes = params.classes.split(/\s+/);
      for( var i = 0, l = classes.length; i < l; i++ ){
        var cls = classes[i];
        if( !cls || cls === '' ){ continue; }

        self._private.classes[cls] = true;
      }
    }

    if( params.css ){
      cy.style().applyBypass( this, params.css );
    }
    
    if( restore === undefined || restore ){
      this.restore();
    }
    
  };

  
  // Collection
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  // represents a set of nodes, edges, or both together
  $$.Collection = function(cy, elements, options){
    if( !(this instanceof $$.Collection) ){
      return new $$.Collection(cy, elements);
    }

    if( cy === undefined || !$$.is.core(cy) ){
      $$.util.error('A collection must have a reference to the core');
      return;
    }
    
    var ids = {};
    var indexes = {};
    var createdElements = false;
    
    if( !elements ){
      elements = [];
    } else if( elements.length > 0 && $$.is.plainObject( elements[0] ) && !$$.is.element( elements[0] ) ){
      createdElements = true;

      // make elements from json and restore all at once later
      var eles = [];
      var elesIds = {};

      for( var i = 0, l = elements.length; i < l; i++ ){
        var json = elements[i];

        if( json.data == null ){
          json.data = {};
        }
        
        var data = json.data;

        // make sure newly created elements have valid ids
        if( data.id == null ){
          data.id = idFactory.generate( cy, json );
        } else if( cy.getElementById( data.id ).length !== 0 || elesIds[ data.id ] ){
          continue; // can't create element if prior id already exists
        }

        var ele = new $$.Element( cy, json, false );
        eles.push( ele );
        elesIds[ data.id ] = true;
      }

      elements = eles;
    }
    
    this.length = 0;

    for( var i = 0, l = elements.length; i < l; i++ ){
      var element = elements[i];
      if( !element ){  continue; }
      
      var id = element._private.data.id;
      
      if( !options || (options.unique && !ids[ id ] ) ){
        ids[ id ] = element;
        indexes[ id ] = this.length;

        this[ this.length ] = element;
        this.length++;
      }
    }
    
    this._private = {
      cy: cy,
      ids: ids,
      indexes: indexes
    };

    // restore the elements if we created them from json
    if( createdElements ){
      this.restore();
    }
  };
  
  
  // Functions
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  // keep the prototypes in sync (an element has the same functions as a collection)
  // and use $$.elefn and $$.elesfn as shorthands to the prototypes
  $$.elefn = $$.elesfn = $$.Element.prototype = $$.Collection.prototype;

  $$.elesfn.cy = function(){
    return this._private.cy;
  };
  
  $$.elesfn.element = function(){
    return this[0];
  };
  
  $$.elesfn.collection = function(){
    if( $$.is.collection(this) ){
      return this;
    } else { // an element
      return new $$.Collection( this._private.cy, [this] );
    }
  };

  $$.elesfn.unique = function(){
    return new $$.Collection( this._private.cy, this, { unique: true } );
  };

  $$.elesfn.getElementById = function( id ){
    var cy = this._private.cy;
    var ele = this._private.ids[ id ];

    return ele ? ele : $$.Collection(cy); // get ele or empty collection
  };

  $$.elesfn.json = function(){
    var ele = this.element();
    if( ele == null ){ return undefined; }

    var p = ele._private;
    
    var json = $$.util.copy({
      data: p.data,
      position: p.position,
      group: p.group,
      bypass: p.bypass,
      removed: p.removed,
      selected: p.selected,
      selectable: p.selectable,
      locked: p.locked,
      grabbed: p.grabbed,
      grabbable: p.grabbable,
      classes: ''
    });
    
    var classes = [];
    for( var cls in p.classes ){
      if( p.classes[cls] ){
        classes.push(cls);
      }
    }
    
    for( var i = 0; i < classes.length; i++ ){
      var cls = classes[i];
      json.classes += cls + ( i < classes.length - 1 ? ' ' : '' );
    }
    
    return json;
  };

  $$.elesfn.jsons = function(){
    var jsons = [];

    for( var i = 0; i < this.length; i++ ){
      var ele = this[i];
      var json = ele.json();

      jsons.push( json );
    }

    return jsons;
  };

  $$.elesfn.clone = function(){
    var cy = this.cy();
    var elesArr = [];

    for( var i = 0; i < this.length; i++ ){
      var ele = this[i];
      var json = ele.json();
      var clone = new $$.Element(cy, json, false); // NB no restore

      elesArr.push( clone );
    }

    return new $$.Collection( cy, elesArr );
  };

  $$.elesfn.restore = function( notifyRenderer ){
    var self = this;
    var restored = [];
    var cy = self.cy();
    
    if( notifyRenderer === undefined ){
      notifyRenderer = true;
    }

    // create arrays of nodes and edges, since we need to
    // restore the nodes first
    var elements = [];
    var nodes = [], edges = [];
    var numNodes = 0;
    var numEdges = 0;
    for( var i = 0, l = self.length; i < l; i++ ){
      var ele = self[i];
      
      // keep nodes first in the array and edges after
      if( ele.isNode() ){ // put to front of array if node
        nodes.push( ele );
        numNodes++;
      } else { // put to end of array if edge
        edges.push( ele );
        numEdges++;
      }
    }

    elements = nodes.concat( edges );

    // now, restore each element
    for( var i = 0, l = elements.length; i < l; i++ ){
      var ele = elements[i];

      if( !ele.removed() ){
        // don't need to do anything
        continue;
      }
      
      var _private = ele._private;
      var data = _private.data;
      
      // set id and validate
      if( data.id === undefined ){
        data.id = idFactory.generate( cy, ele );
      } else if( $$.is.emptyString(data.id) || !$$.is.string(data.id) ){
        $$.util.error('Can not create element with invalid string ID `' + data.id + '`');
        
        // can't create element if it has empty string as id or non-string id
        continue;
      } else if( cy.getElementById( data.id ).length !== 0 ){
        $$.util.error('Can not create second element with ID `' + data.id + '`');
        
        // can't create element if one already has that id
        continue;
      }

      var id = data.id; // id is finalised, now let's keep a ref
      
      if( ele.isEdge() ){ // extra checks for edges
        
        var edge = ele;
        var fields = ['source', 'target'];
        var fieldsLength = fields.length;
        var badSourceOrTarget = false;
        for(var j = 0; j < fieldsLength; j++){
          
          var field = fields[j];
          var val = data[field];
          
          if( val == null || val === '' ){
            // can't create if source or target is not defined properly
            $$.util.error('Can not create edge `' + id + '` with unspecified ' + field);
            badSourceOrTarget = true;
          } else if( cy.getElementById(val).empty() ){ 
            // can't create edge if one of its nodes doesn't exist
            $$.util.error('Can not create edge `' + id + '` with nonexistant ' + field + ' `' + val + '`');
            badSourceOrTarget = true;
          }
        }

        if( badSourceOrTarget ){ continue; } // can't create this
        
        var src = cy.getElementById( data.source );
        var tgt = cy.getElementById( data.target );

        src._private.edges.push( edge );
        tgt._private.edges.push( edge );

        edge._private.source = src;
        edge._private.target = tgt;

      } // if is edge
       
      // create mock ids map for element so it can be used like collections
      _private.ids = {};
      _private.ids[ id ] = ele;

      _private.removed = false;
      cy.addToPool( ele );
      
      restored.push( ele );
    } // for each element

    // do compound node sanity checks
    for( var i = 0; i < numNodes; i++ ){ // each node 
      var node = elements[i];
      var data = node._private.data;

      var parentId = node._private.data.parent;
      var specifiedParent = parentId != null;

      if( specifiedParent ){
        var parent = cy.getElementById( parentId );

        if( parent.empty() ){
          // non-existant parent; just remove it
          data.parent = undefined;
        } else {
          var selfAsParent = false;
          var ancestor = parent;
          while( !ancestor.empty() ){
            if( node.same(ancestor) ){
              // mark self as parent and remove from data
              selfAsParent = true;
              data.parent = undefined; // remove parent reference

              // exit or we loop forever
              break;
            }

            ancestor = ancestor.parent();
          }

          if( !selfAsParent ){
            // connect with children
            parent[0]._private.children.push( node );
            node._private.parent = parent[0];

            // let the core know we have a compound graph
            cy._private.hasCompoundNodes = true;
          }
        } // else
      } // if specified parent
    } // for each node
    
    restored = new $$.Collection( cy, restored );
    if( restored.length > 0 ){

      var toUpdateStyle = restored.add( restored.connectedNodes() ).add( restored.parent() );
      toUpdateStyle.updateStyle( notifyRenderer );

      if( notifyRenderer ){
        restored.rtrigger('add');
      } else {
        restored.trigger('add');
      }
    }
    
    return self; // chainability
  };
  
  $$.elesfn.removed = function(){
    var ele = this[0];
    return ele && ele._private.removed;
  };

  $$.elesfn.inside = function(){
    var ele = this[0];
    return ele && !ele._private.removed;
  };

  $$.elesfn.remove = function( notifyRenderer ){
    var self = this;
    var removed = [];
    var elesToRemove = [];
    var elesToRemoveIds = {};
    var cy = self._private.cy;
    
    if( notifyRenderer === undefined ){
      notifyRenderer = true;
    }
    
    // add connected edges
    function addConnectedEdges(node){
      var edges = node._private.edges; 
      for( var i = 0; i < edges.length; i++ ){
        add( edges[i] );
      }
    }
    

    // add descendant nodes
    function addChildren(node){
      var children = node._private.children;
      
      for( var i = 0; i < children.length; i++ ){
        add( children[i] );
      }
    }

    function add( ele ){
      var alreadyAdded =  elesToRemoveIds[ ele.id() ];
      if( alreadyAdded ){
        return;
      } else {
        elesToRemoveIds[ ele.id() ] = true;
      }

      if( ele.isNode() ){
        elesToRemove.push( ele ); // nodes are removed last

        addConnectedEdges( ele );
        addChildren( ele );
      } else {
        elesToRemove.unshift( ele ); // edges are removed first
      }
    }

    // make the list of elements to remove
    // (may be removing more than specified due to connected edges etc)

    for( var i = 0, l = self.length; i < l; i++ ){
      var ele = self[i];

      add( ele );
    }
    
    function removeEdgeRef(node, edge){
      var connectedEdges = node._private.edges;
      for( var j = 0; j < connectedEdges.length; j++ ){
        var connectedEdge = connectedEdges[j];
        
        if( edge === connectedEdge ){
          connectedEdges.splice( j, 1 );
          break;
        }
      }
    }

    function removeChildRef(parent, ele){
      ele = ele[0];
      parent = parent[0];
      var children = parent._private.children;

      for( var j = 0; j < children.length; j++ ){
        if( children[j][0] === ele[0] ){
          children.splice(j, 1);
          break;
        }
      }
    }

    for( var i = 0; i < elesToRemove.length; i++ ){
      var ele = elesToRemove[i];

      // mark as removed
      ele._private.removed = true;

      // remove from core pool
      cy.removeFromPool( ele );

      // add to list of removed elements
      removed.push( ele );

      if( ele.isEdge() ){ // remove references to this edge in its connected nodes
        var src = ele.source()[0];
        var tgt = ele.target()[0];

        removeEdgeRef( src, ele );
        removeEdgeRef( tgt, ele );

      } else { // remove reference to parent 
        var parent = ele.parent();

        if( parent.length !== 0 ){
          removeChildRef(parent, ele);
        }
      }
    }

    // check to see if we have a compound graph or not
    var elesStillInside = cy._private.elements;
    cy._private.hasCompoundNodes = false;
    for( var i = 0; i < elesStillInside.length; i++ ){
      var ele = elesStillInside[i];

      if( ele.isParent() ){
        cy._private.hasCompoundNodes = true;
        break;
      }
    }

    var removedElements = new $$.Collection( this.cy(), removed );
    if( removedElements.size() > 0 ){
      // must manually notify since trigger won't do this automatically once removed
      
      if( notifyRenderer ){
        this.cy().notify({
          type: 'remove',
          collection: removedElements
        });
      }
      
      removedElements.trigger('remove');
    }

    // check for empty remaining parent nodes
    var checkedParentId = {};
    for( var i = 0; i < elesToRemove.length; i++ ){
      var ele = elesToRemove[i];
      var isNode = ele._private.group === 'nodes';
      var parentId = ele._private.data.parent;

      if( isNode && parentId !== undefined && !checkedParentId[ parentId ] ){
        checkedParentId[ parentId ] = true;
        var parent = cy.getElementById( parentId );

        if( parent && parent.length !== 0 && !parent._private.removed && parent.children().length === 0 ){
          parent.updateStyle();
        }
      }
    }

    return this;
  };

  $$.elesfn.move = function( struct ){
    var cy = this._private.cy;

    if( struct.source !== undefined || struct.target !== undefined ){
      var srcId = struct.source;
      var tgtId = struct.target;
      var srcExists = cy.getElementById( srcId ).length > 0;
      var tgtExists = cy.getElementById( tgtId ).length > 0;

      if( srcExists || tgtExists ){
        var jsons = this.jsons();

        this.remove();

        for( var i = 0; i < jsons.length; i++ ){
          var json = jsons[i];

          if( json.group === 'edges' ){
            if( srcExists ){ json.data.source = srcId; }
            if( tgtExists ){ json.data.target = tgtId; }
          }
        }

        return cy.add( jsons );
      }
 
    } else if( struct.parent !== undefined ){ // move node to new parent
      var parentId = struct.parent;
      var parentExists = parentId === null || cy.getElementById( parentId ).length > 0;
    
      if( parentExists ){
        var jsons = this.jsons();
        var descs = this.descendants();
        var descsEtc = descs.merge( descs.add(this).connectedEdges() );

        this.remove(); // NB: also removes descendants and their connected edges

        for( var i = 0; i < this.length; i++ ){
          var json = jsons[i];

          if( json.group === 'nodes' ){
            json.data.parent = parentId === null ? undefined : parentId;
          }
        }
      }

      return cy.add( jsons ).merge( descsEtc.restore() );
    }

    return this; // if nothing done
  };
  
})( cytoscape );


;(function($$){ 'use strict';

  // search, spanning trees, etc
  $$.fn.eles({

    // std functional ele first callback style
    stdBreadthFirstSearch: function( options ){
      options = $$.util.extend( {}, options, {
        std: true
      } );

      return this.breadthFirstSearch( options );
    },

    // do a breadth first search from the nodes in the collection
    // from pseudocode on wikipedia
    breadthFirstSearch: function( roots, fn, directed ){
      var options;
      var std;
      var thisArg;
      if( $$.is.plainObject(roots) && !$$.is.elementOrCollection(roots) ){
        options = roots;
        roots = options.roots;
        fn = options.visit;
        directed = options.directed;
        std = options.std;
        thisArg = options.thisArg;
      }

      directed = arguments.length === 2 && !$$.is.fn(fn) ? fn : directed;
      fn = $$.is.fn(fn) ? fn : function(){};
      
      var cy = this._private.cy;
      var v = $$.is.string(roots) ? this.filter(roots) : roots;
      var Q = [];
      var connectedNodes = [];
      var connectedBy = {};
      var id2depth = {};
      var V = {};
      var j = 0;
      var found;
      var nodes = this.nodes();
      var edges = this.edges();

      // enqueue v
      for( var i = 0; i < v.length; i++ ){
        if( v[i].isNode() ){
          Q.unshift( v[i] );
          V[ v[i].id() ] = true; 

          connectedNodes.push( v[i] );
          id2depth[ v[i].id() ] = 0;
        }
      }

      while( Q.length !== 0 ){
        var v = Q.shift();
        var depth = id2depth[ v.id() ];
        var prevEdge = connectedBy[ v.id() ];
        var prevNode = prevEdge == null ? undefined : prevEdge.connectedNodes().not( v )[0];
        var ret;

        if( std ){
          ret = fn.call(thisArg, v, prevEdge, prevNode, j++, depth);
        } else {
          ret = fn.call(v, j++, depth, v, prevEdge, prevNode);
        }

        if( ret === true ){
          found = v;
          break;
        }

        if( ret === false ){
          break;
        }

        var vwEdges = v.connectedEdges(directed ? function(){ return this.data('source') === v.id(); } : undefined).intersect( edges );
        for( var i = 0; i < vwEdges.length; i++ ){
          var e = vwEdges[i];
          var w = e.connectedNodes(function(){ return this.id() !== v.id(); }).intersect( nodes );

          if( w.length !== 0 && !V[ w.id() ] ){
            w = w[0];

            Q.push( w );
            V[ w.id() ] = true;

            id2depth[ w.id() ] = id2depth[ v.id() ] + 1;

            connectedNodes.push( w );
            connectedBy[ w.id() ] = e;
          }
        }
        
      }

      var connectedEles = [];

      for( var i = 0; i < connectedNodes.length; i++ ){
        var node = connectedNodes[i];
        var edge = connectedBy[ node.id() ];

        if( edge ){
          connectedEles.push( edge );
        }

        connectedEles.push( node );
      }

      return {
        path: new $$.Collection( cy, connectedEles, { unique: true } ),
        found: new $$.Collection( cy, found, { unique: true } )
      };
    },

    // std functional ele first callback style
    stdDepthFirstSearch: function( options ){
      options = $$.util.extend( {}, options, {
        std: true
      } );

      return this.depthFirstSearch( options );
    },

    // do a depth first search on the nodes in the collection
    // from pseudocode on wikipedia (iterative impl)
    depthFirstSearch: function( roots, fn, directed ){
      var options;
      var std;
      var thisArg;
      if( $$.is.plainObject(roots) && !$$.is.elementOrCollection(roots) ){
        options = roots;
        roots = options.roots;
        fn = options.visit;
        directed = options.directed;
        std = options.std;
        thisArg = options.thisArg;
      }
      
      directed = arguments.length === 2 && !$$.is.fn(fn) ? fn : directed;
      fn = $$.is.fn(fn) ? fn : function(){};
      var cy = this._private.cy;
      var v = $$.is.string(roots) ? this.filter(roots) : roots;
      var S = [];
      var connectedNodes = [];
      var connectedBy = {};
      var id2depth = {};
      var discovered = {};
      var j = 0;
      var found;
      var edges = this.edges();
      var nodes = this.nodes();

      // push v
      for( var i = 0; i < v.length; i++ ){
        if( v[i].isNode() ){
          S.push( v[i] );

          connectedNodes.push( v[i] );
          id2depth[ v[i].id() ] = 0;
        }
      }

      while( S.length !== 0 ){
        var v = S.pop();

        if( !discovered[ v.id() ] ){
          discovered[ v.id() ] = true;

          var depth = id2depth[ v.id() ];
          var prevEdge = connectedBy[ v.id() ];
          var prevNode = prevEdge == null ? undefined : prevEdge.connectedNodes().not( v )[0];
          var ret;

          if( std ){
            ret = fn.call(thisArg, v, prevEdge, prevNode, j++, depth);
          } else {
            ret = fn.call(v, j++, depth, v, prevEdge, prevNode);
          }

          if( ret === true ){
            found = v;
            break;
          }

          if( ret === false ){
            break;
          }

          var vwEdges = v.connectedEdges(directed ? function(){ return this.data('source') === v.id(); } : undefined).intersect( edges );
          
          for( var i = 0; i < vwEdges.length; i++ ){
            var e = vwEdges[i];
            var w = e.connectedNodes(function(){ return this.id() !== v.id(); }).intersect( nodes );

            if( w.length !== 0 && !discovered[ w.id() ] ){
              w = w[0];

              S.push( w );

              id2depth[ w.id() ] = id2depth[ v.id() ] + 1;

              connectedNodes.push( w );
              connectedBy[ w.id() ] = e;
            }
          }
        }
      }

      var connectedEles = [];

      for( var i = 0; i < connectedNodes.length; i++ ){
        var node = connectedNodes[i];
        var edge = connectedBy[ node.id() ];

        if( edge ){
          connectedEles.push( edge );
        }

        connectedEles.push( node );
      }

      return {
        path: new $$.Collection( cy, connectedEles, { unique: true } ),
        found: new $$.Collection( cy, found, { unique: true } )
      };
    },

    // kruskal's algorithm (finds min spanning tree, assuming undirected graph)
    // implemented from pseudocode from wikipedia
    kruskal: function( weightFn ){
      weightFn = $$.is.fn(weightFn) ? weightFn : function(){ return 1; }; // if not specified, assume each edge has equal weight (1)

      function findSet(ele){
        for( var i = 0; i < forest.length; i++ ){
          var eles = forest[i];

          if( eles.anySame(ele) ){
            return {
              eles: eles,
              index: i
            };
          }
        }
      }

      var A = new $$.Collection(this._private.cy, []);
      var forest = [];
      var nodes = this.nodes();

      for( var i = 0; i < nodes.length; i++ ){
        forest.push( nodes[i].collection() );
      }

      var edges = this.edges();
      var S = edges.toArray().sort(function(a, b){
        var weightA = weightFn.call(a, a);
        var weightB = weightFn.call(b, b);

        return weightA - weightB;
      });

      for(var i = 0; i < S.length; i++){
        var edge = S[i];
        var u = edge.source()[0];
        var v = edge.target()[0];
        var setU = findSet(u);
        var setV = findSet(v);

        if( setU.index !== setV.index ){
          A = A.add( edge );

          // combine forests for u and v
          forest[ setU.index ] = setU.eles.add( setV.eles );
          forest.splice( setV.index, 1 );
        }
      }

      return nodes.add( A );

    },

    dijkstra: function( root, weightFn, directed ){
      var options;
      if( $$.is.plainObject(root) && !$$.is.elementOrCollection(root) ){
        options = root;
        root = options.root;
        weightFn = options.weight;
        directed = options.directed;
      }

      var cy = this._private.cy;
      directed = !$$.is.fn(weightFn) ? weightFn : directed;
      weightFn = $$.is.fn(weightFn) ? weightFn : function(){ return 1; }; // if not specified, assume each edge has equal weight (1)

      var source = $$.is.string(root) ? this.filter(root).eq(0) : root.eq(0);
      var dist = {};
      var prev = {};
      var knownDist = {};

      var edges = this.edges().filter(function(){ return !this.isLoop(); });
      var nodes = this.nodes();
      var Q = [];

      for( var i = 0; i < nodes.length; i++ ){
        dist[ nodes[i].id() ] = nodes[i].same( source ) ? 0 : Infinity;
        Q.push( nodes[i] );
      }

      var valueFn = function(node) {
        return dist[ node.id() ];
      };
      
      Q = new $$.Collection(cy, Q);
    
      var heap = $$.Minheap(cy, Q, valueFn);
    
      var distBetween = function(u, v){
        var uvs = ( directed ? u.edgesTo(v) : u.edgesWith(v) ).intersect(edges);
        var smallestDistance = Infinity;
        var smallestEdge;

        for( var i = 0; i < uvs.length; i++ ){
          var edge = uvs[i];
          var weight = weightFn.apply( edge, [edge] );

          if( weight < smallestDistance || !smallestEdge ){
            smallestDistance = weight;
            smallestEdge = edge;
          }
        }

        return {
          edge: smallestEdge,
          dist: smallestDistance
        };
      };

      while(heap.size() > 0){
        var smallestEl = heap.pop(),
        smalletsDist = smallestEl.value,
        uid = smallestEl.id,
        u = cy.getElementById(uid);
    
        knownDist[uid] = smalletsDist;
      
        if( smalletsDist === Math.Infinite ){
          break;
        }

        var neighbors = u.neighborhood().intersect(nodes);
        for( var i = 0; i < neighbors.length; i++ ){
          var v = neighbors[i];
          var vid = v.id();
          var vDist = distBetween(u, v);

          var alt = smalletsDist + vDist.dist;

          if( alt < heap.getValueById(vid) ){
            heap.edit(vid, alt);
            prev[ vid ] = {
              node: u,
              edge: vDist.edge
            };
          }
        } // for 
      } // while

      return {
        distanceTo: function(node){
          var target = $$.is.string(node) ? nodes.filter(node).eq(0) : node.eq(0);

          return knownDist[ target.id() ];
        },

        pathTo: function(node){
          var target = $$.is.string(node) ? nodes.filter(node).eq(0) : node.eq(0);
          var S = [];
          var u = target;

          if( target.length > 0 ){
            S.unshift( target );

            while( prev[ u.id() ] ){
              var p = prev[ u.id() ];

              S.unshift( p.edge );
              S.unshift( p.node );

              u = p.node;
            }
          }

          return new $$.Collection( cy, S );
        }
      };
    }  
  });

  // nice, short mathemathical alias
  $$.elesfn.bfs = $$.elesfn.breadthFirstSearch;
  $$.elesfn.dfs = $$.elesfn.depthFirstSearch;
  $$.elesfn.stdBfs = $$.elesfn.stdBreadthFirstSearch;
  $$.elesfn.stdDfs = $$.elesfn.stdDepthFirstSearch;
  
})( cytoscape );
;(function($$) { 
  'use strict';

  // Additional graph analysis algorithms
  $$.fn.eles({

    // Implemented from pseudocode from wikipedia

    // options => options object
    //   root // starting node (either element or selector string)
    //   weight: function( edge ){} // specifies weight to use for `edge`/`this`. If not present, it will be asumed a weight of 1 for all edges
    //   heuristic: function( node ){} // specifies heuristic value for `node`/`this`
    //   directed // default false
    //   goal // target node (either element or selector string). Mandatory.

    // retObj => returned object by function
    //   found : true/false // whether a path from root to goal has been found
    //   distance // Distance for the shortest path from root to goal
    //   path // Array of ids of nodes in shortest path
    aStar: function(options) {
      options = options || {};

      var logDebug = function() {
        if (debug) {
          console.log.apply(console, arguments);
        }
      };

      // Reconstructs the path from Start to End, acumulating the result in pathAcum
      var reconstructPath = function(start, end, cameFromMap, pathAcum) {
        // Base case
        if (start == end) {
          pathAcum.push( cy.getElementById(end) );
          return pathAcum;
        }
        
        if (end in cameFromMap) {
          // We know which node is before the last one
          var previous = cameFromMap[end];
          var previousEdge = cameFromEdge[end];

          pathAcum.push( cy.getElementById(end) );
          pathAcum.push( cy.getElementById(previousEdge) );


          return reconstructPath(start, 
                       previous, 
                       cameFromMap, 
                       pathAcum);
        }

        // We should not reach here!
        return undefined;       
      };

      // Returns the index of the element in openSet which has minimum fScore
      var findMin = function(openSet, fScore) {
        if (openSet.length === 0) {
          // Should never be the case
          return undefined;
        }
        var minPos = 0;
        var tempScore = fScore[openSet[0]];
        for (var i = 1; i < openSet.length; i++) {
          var s = fScore[openSet[i]];
          if (s < tempScore) {
            tempScore = s;
            minPos = i;
          }
        }
        return minPos;
      };

      // Parse options
      // debug - optional
      if (options.debug != null) {
        var debug = options.debug;
      } else {
        var debug = false;
      }

      logDebug("Starting aStar..."); 
      var cy = this._private.cy;

      // root - mandatory!
      if (options != null && options.root != null) {        
        var source = $$.is.string(options.root) ? 
          // use it as a selector, e.g. "#rootID
          this.filter(options.root)[0] : 
          options.root[0];
        logDebug("Source node: %s", source.id()); 
      } else {
        return undefined;
      }
      
      // goal - mandatory!
      if (options.goal != null) {       
        var target = $$.is.string(options.goal) ? 
          // use it as a selector, e.g. "#goalID
          this.filter(options.goal)[0] : 
          options.goal[0];
        logDebug("Target node: %s", target.id()); 
      } else {
        return undefined;
      }

      // Heuristic function - optional
      if (options.heuristic != null && $$.is.fn(options.heuristic)) {       
        var heuristic = options.heuristic;
      } else {
        var heuristic = function(){ return 0; }; // use constant if unspecified
        // $$.util.error("Missing required parameter (heuristic)! Aborting.");
        // return;
      }

      // Weight function - optional
      if (options.weight != null && $$.is.fn(options.weight)) {       
        var weightFn = options.weight;
      } else {
        // If not specified, assume each edge has equal weight (1)
        var weightFn = function(e) {return 1;};
      }

      // directed - optional
      if (options.directed != null) {       
        var directed = options.directed;
      } else {
        var directed = false;
      }

      var closedSet = [];
      var openSet = [source.id()];
      var cameFrom = {};
      var cameFromEdge = {};
      var gScore = {};
      var fScore = {};

      gScore[source.id()] = 0;
      fScore[source.id()] = heuristic(source);
      
      var edges = this.edges().not(':loop');
      var nodes = this.nodes();

      // Counter
      var steps = 0;

      // Main loop 
      while (openSet.length > 0) {
        var minPos = findMin(openSet, fScore);
        var cMin = this.filter("#" + openSet[minPos])[0];
        steps++;

        logDebug("\nStep: %s", steps);
        logDebug("Processing node: %s, fScore = %s", cMin.id(), fScore[cMin.id()]);
        
        // If we've found our goal, then we are done
        if (cMin.id() == target.id()) {
          logDebug("Found goal node!");
          var rPath = reconstructPath(source.id(), target.id(), cameFrom, []);
          rPath.reverse();
          logDebug("Path: %s", rPath);
          return {
            found : true,
            distance : gScore[cMin.id()],
            path : new $$.Collection(cy, rPath),
            steps : steps
          };          
        }
        
        // Add cMin to processed nodes
        closedSet.push(cMin.id());
        // Remove cMin from boundary nodes
        openSet.splice(minPos, 1);
        logDebug("Added node to closedSet, removed from openSet.");
        logDebug("Processing neighbors...");

        // Update scores for neighbors of cMin
        // Take into account if graph is directed or not
        var vwEdges = cMin.connectedEdges(directed ? '[source = "' + cMin.id() + '"]' 
                         : undefined).intersect(edges);         
        for (var i = 0; i < vwEdges.length; i++) {
          var e = vwEdges[i];
          var w = e.connectedNodes('[id != "' + cMin.id() + '"]').intersect(nodes);

          logDebug("   processing neighbor: %s", w.id());
          // if node is in closedSet, ignore it
          if (closedSet.indexOf(w.id()) != -1) {
            logDebug("   already in closedSet, ignoring it.");
            continue;
          }
          
          // New tentative score for node w
          var tempScore = gScore[cMin.id()] + weightFn.apply(e, [e]);
          logDebug("   tentative gScore: %d", tempScore);

          // Update gScore for node w if:
          //   w not present in openSet
          // OR
          //   tentative gScore is less than previous value

          // w not in openSet
          if (openSet.indexOf(w.id()) == -1) {
            gScore[w.id()] = tempScore;
            fScore[w.id()] = tempScore + heuristic(w);
            openSet.push(w.id()); // Add node to openSet
            cameFrom[w.id()] = cMin.id();
            cameFromEdge[w.id()] = e.id();
            logDebug("   not in openSet, adding it. ");
            logDebug("   fScore(%s) = %s", w.id(), tempScore);
            continue;
          }
          // w already in openSet, but with greater gScore
          if (tempScore < gScore[w.id()]) {
            gScore[w.id()] = tempScore;
            fScore[w.id()] = tempScore + heuristic(w);
            cameFrom[w.id()] = cMin.id();
            logDebug("   better score, replacing gScore. ");
            logDebug("   fScore(%s) = %s", w.id(), tempScore);
          }

        } // End of neighbors update

      } // End of main loop

      // If we've reached here, then we've not reached our goal
      logDebug("Reached end of computation without finding our goal");
      return {
        found : false,
        distance : undefined,
        path : undefined,
        steps : steps
      };
    }, // aStar()


    // Implemented from pseudocode from wikipedia
    // options => options object
    //   weight: function( edge ){} // specifies weight to use for `edge`/`this`. If not present, it will be asumed a weight of 1 for all edges
    //   directed // default false
    // retObj => returned object by function
    //   pathTo : function(fromId, toId) // Returns the shortest path from node with ID "fromID" to node with ID "toId", as an array of node IDs
    //   distanceTo: function(fromId, toId) // Returns the distance of the shortest path from node with ID "fromID" to node with ID "toId"
    floydWarshall: function(options) {
      options = options || {};

      var logDebug = function() {
        if (debug) {
          console.log.apply(console, arguments);
        }
      };

      // Parse options
      // debug - optional
      if (options.debug != null) {
        var debug = options.debug;
      } else {
        var debug = false;
      }
      logDebug("Starting floydWarshall..."); 

      var cy = this._private.cy;

      // Weight function - optional
      if (options.weight != null && $$.is.fn(options.weight)) {       
        var weightFn = options.weight;
      } else {
        // If not specified, assume each edge has equal weight (1)
        var weightFn = function(e) {return 1;};
      }

      // directed - optional
      if (options.directed != null) {       
        var directed = options.directed;
      } else {
        var directed = false;
      }

      var edges = this.edges().not(':loop');
      var nodes = this.nodes();
      var numNodes = nodes.length;

      // mapping: node id -> position in nodes array
      var id2position = {};
      for (var i = 0; i < numNodes; i++) {
        id2position[nodes[i].id()] = i;
      }     

      // Initialize distance matrix
      var dist = [];
      for (var i = 0; i < numNodes; i++) {
        var newRow = new Array(numNodes);
        for (var j = 0; j < numNodes; j++) {
          if (i == j) {
            newRow[j] = 0;
          } else {
            newRow[j] = Infinity;
          }
        }
        dist.push(newRow);
      }           

      // Initialize matrix used for path reconstruction
      // Initialize distance matrix
      var next = [];
      var edgeNext = [];

      var initMatrix = function(next){
        for (var i = 0; i < numNodes; i++) {
          var newRow = new Array(numNodes);
          for (var j = 0; j < numNodes; j++) {
            newRow[j] = undefined;
          }
          next.push(newRow);
        }
      };

      initMatrix(next);
      initMatrix(edgeNext);
      
      // Process edges
      for (var i = 0; i < edges.length ; i++) {     
        var sourceIndex = id2position[edges[i].source().id()];
        var targetIndex = id2position[edges[i].target().id()];    
        var weight = weightFn.apply(edges[i], [edges[i]]);
        
        // Check if already process another edge between same 2 nodes
        if (dist[sourceIndex][targetIndex] > weight) {
          dist[sourceIndex][targetIndex] = weight;
          next[sourceIndex][targetIndex] = targetIndex;
          edgeNext[sourceIndex][targetIndex] = edges[i];
        }
      }

      // If undirected graph, process 'reversed' edges
      if (!directed) {
        for (var i = 0; i < edges.length ; i++) {     
          var sourceIndex = id2position[edges[i].target().id()];    
          var targetIndex = id2position[edges[i].source().id()];
          var weight = weightFn.apply(edges[i], [edges[i]]);
          
          // Check if already process another edge between same 2 nodes
          if (dist[sourceIndex][targetIndex] > weight) {
            dist[sourceIndex][targetIndex] = weight;
            next[sourceIndex][targetIndex] = targetIndex;
            edgeNext[sourceIndex][targetIndex] = edges[i];
          }
        }
      }

      // Main loop
      for (var k = 0; k < numNodes; k++) {
        for (var i = 0; i < numNodes; i++) {
          for (var j = 0; j < numNodes; j++) {            
            if (dist[i][k] + dist[k][j] < dist[i][j]) {
              dist[i][j] = dist[i][k] + dist[k][j];
              next[i][j] = next[i][k];
            }
          }
        }
      }

      // Build result object       
      var position2id = [];
      for (var i = 0; i < numNodes; i++) {
        position2id.push(nodes[i].id());
      }

      var res = {
        distance: function(from, to) {
          if ($$.is.string(from)) {
            // from is a selector string
            var fromId = (cy.filter(from)[0]).id();
          } else {
            // from is a node
            var fromId = from.id();
          }

          if ($$.is.string(to)) {
            // to is a selector string
            var toId = (cy.filter(to)[0]).id();
          } else {
            // to is a node
            var toId = to.id();
          }

          return dist[id2position[fromId]][id2position[toId]];
        },

        path: function(from, to) {
          var reconstructPathAux = function(from, to, next, position2id, edgeNext) {
            if (from === to) {
              return cy.getElementById( position2id[from] );
            }
            if (next[from][to] === undefined) {
              return undefined;
            }

            var path = [ cy.getElementById(position2id[from]) ];
            var prev = from;
            while (from !== to) {
              prev = from;
              from = next[from][to];

              var edge = edgeNext[prev][from];
              path.push( edge );

              path.push( cy.getElementById(position2id[from]) );
            }
            return path;
          };

          if ($$.is.string(from)) {
            // from is a selector string
            var fromId = (cy.filter(from)[0]).id();
          } else {
            // from is a node
            var fromId = from.id();
          }

          if ($$.is.string(to)) {
            // to is a selector string
            var toId = (cy.filter(to)[0]).id();
          } else {
            // to is a node
            var toId = to.id();
          }
          
          var pathArr = reconstructPathAux(id2position[fromId], 
                        id2position[toId], 
                        next,
                        position2id,
                        edgeNext);

          return new $$.Collection( cy, pathArr );
        },
      };

      return res;

    }, // floydWarshall


    // Implemented from pseudocode from wikipedia
    // options => options object
    //   root: starting node (either element or selector string)
    //   weight: function( edge ){} // specifies weight to use for `edge`/`this`. If not present, it will be asumed a weight of 1 for all edges
    //   directed // default false
    // retObj => returned object by function
    //   pathTo : function(toId) // Returns the shortest path from root node to node with ID "toId", as an array of node IDs
    //   distanceTo: function(toId) // Returns the distance of the shortest path from root node to node with ID "toId"
    //   hasNegativeWeightCycle: true/false (if true, pathTo and distanceTo will be undefined)
    bellmanFord: function(options) {
      options = options || {};

      var logDebug = function() {
        if (debug) {
          console.log.apply(console, arguments);
        }
      };

      // Parse options
      // debug - optional
      if (options.debug != null) {
        var debug = options.debug;
      } else {
        var debug = false;
      }
      logDebug("Starting bellmanFord..."); 

      // Weight function - optional
      if (options.weight != null && $$.is.fn(options.weight)) {       
        var weightFn = options.weight;
      } else {
        // If not specified, assume each edge has equal weight (1)
        var weightFn = function(e) {return 1;};
      }

      // directed - optional
      if (options.directed != null) {       
        var directed = options.directed;
      } else {
        var directed = false;
      }

      // root - mandatory!
      if (options.root != null) {       
        if ($$.is.string(options.root)) {
          // use it as a selector, e.g. "#rootID
          var source = this.filter(options.root)[0];
        } else {
          var source = options.root[0];
        }
        logDebug("Source node: %s", source.id()); 
      } else {
        $$.util.error("options.root required");
        return undefined;
      }

      var cy = this._private.cy;
      var edges = this.edges().not(':loop');
      var nodes = this.nodes();
      var numNodes = nodes.length;

      // mapping: node id -> position in nodes array
      var id2position = {};
      for (var i = 0; i < numNodes; i++) {
        id2position[nodes[i].id()] = i;
      }     

      // Initializations
      var cost = [];
      var predecessor = [];
      var predEdge = [];
      
      for (var i = 0; i < numNodes; i++) {
        if (nodes[i].id() === source.id()) {
          cost[i] = 0;
        } else {
          cost[i] = Infinity;
        } 
        predecessor[i] = undefined;
      }
      
      // Edges relaxation      
      var flag = false;
      for (var i = 1; i < numNodes; i++) {
        flag = false;
        for (var e = 0; e < edges.length; e++) {
          var sourceIndex = id2position[edges[e].source().id()];
          var targetIndex = id2position[edges[e].target().id()];    
          var weight = weightFn.apply(edges[e], [edges[e]]);
          
          var temp = cost[sourceIndex] + weight;
          if (temp < cost[targetIndex]) {
            cost[targetIndex] = temp;
            predecessor[targetIndex] = sourceIndex;
            predEdge[targetIndex] = edges[e];
            flag = true;
          }

          // If undirected graph, we need to take into account the 'reverse' edge
          if (!directed) {
            var temp = cost[targetIndex] + weight;
            if (temp < cost[sourceIndex]) {
              cost[sourceIndex] = temp;
              predecessor[sourceIndex] = targetIndex;
              predEdge[sourceIndex] = edges[e];
              flag = true;
            }
          }
        }

        if (!flag) {
          break;
        }
      }      
            
      if (flag) {
        // Check for negative weight cycles
        for (var e = 0; e < edges.length; e++) {
          var sourceIndex = id2position[edges[e].source().id()];
          var targetIndex = id2position[edges[e].target().id()];    
          var weight = weightFn.apply(edges[e], [edges[e]]);
          
          if (cost[sourceIndex] + weight < cost[targetIndex]) {
            $$.util.error("Error: graph contains a negative weigth cycle!"); 
            return { pathTo: undefined,
                 distanceTo: undefined,
                 hasNegativeWeightCycle: true};
          }
        }     
      }

      // Build result object       
      var position2id = [];
      for (var i = 0; i < numNodes; i++) {
        position2id.push(nodes[i].id());
      }
      
      
      var res = {       
        distanceTo : function(to) {
          if ($$.is.string(to)) {
            // to is a selector string
            var toId = (cy.filter(to)[0]).id();
          } else {
            // to is a node
            var toId = to.id();
          }

          return cost[id2position[toId]];
        }, 

        pathTo : function(to) {

          var reconstructPathAux = function(predecessor, fromPos, toPos, position2id, acumPath, predEdge) {
            for(;;){
              // Add toId to path
              acumPath.push( cy.getElementById(position2id[toPos]) );
              acumPath.push( predEdge[toPos] );

              if (fromPos === toPos) {
                // reached starting node
                return acumPath;
              }

              // If no path exists, discart acumulated path and return undefined
              var predPos = predecessor[toPos];
              if (typeof predPos === "undefined") {
                return undefined;
              }

              toPos = predPos;
            }

          };

          if ($$.is.string(to)) {
            // to is a selector string
            var toId = (cy.filter(to)[0]).id();
          } else {
            // to is a node
            var toId = to.id();
          }
          var path = [];

          // This returns a reversed path 
          var res =  reconstructPathAux(predecessor, 
                        id2position[source.id()],
                        id2position[toId], 
                        position2id, 
                        path,
                        predEdge);

          // Get it in the correct order and return it
          if (res != null) {
            res.reverse();
          }

          return new $$.Collection(cy, res);                       
        }, 

        hasNegativeWeightCycle: false
      };

      return res;

    }, // bellmanFord


    // Computes the minimum cut of an undirected graph
    // Returns the correct answer with high probability
    // options => options object
    // 
    // retObj => returned object by function
    //   cut : list of IDs of edges in the cut,
    //   partition1: list of IDs of nodes in one partition
    //   partition2: list of IDs of nodes in the other partition
    kargerStein: function(options) {
      options = options || {};
      
      var logDebug = function() {
        if (debug) {
          console.log.apply(console, arguments);
        }
      };

      // Function which colapses 2 (meta) nodes into one
      // Updates the remaining edge lists
      // Receives as a paramater the edge which causes the collapse
      var colapse = function(edgeIndex, nodeMap, remainingEdges) {
        var edgeInfo = remainingEdges[edgeIndex];
        var sourceIn = edgeInfo[1];
        var targetIn = edgeInfo[2];
        var partition1 = nodeMap[sourceIn];
        var partition2 = nodeMap[targetIn];

        // Delete all edges between partition1 and partition2
        var newEdges = remainingEdges.filter(function(edge) {
          if (nodeMap[edge[1]] === partition1 && nodeMap[edge[2]] === partition2) {
            return false;
          }
          if (nodeMap[edge[1]] === partition2 && nodeMap[edge[2]] === partition1) {
            return false;
          }
          return true;
        });
        
        // All edges pointing to partition2 should now point to partition1
        for (var i = 0; i < newEdges.length; i++) {
          var edge = newEdges[i];
          if (edge[1] === partition2) { // Check source
            newEdges[i] = edge.slice(0);
            newEdges[i][1] = partition1;
          } else if (edge[2] === partition2) { // Check target
            newEdges[i] = edge.slice(0);
            newEdges[i][2] = partition1;
          }
        } 
        
        // Move all nodes from partition2 to partition1
        for (var i = 0; i < nodeMap.length; i++) {
          if (nodeMap[i] === partition2) {
            nodeMap[i] = partition1;
          }
        }
        
        return newEdges;
      };


      // Contracts a graph until we reach a certain number of meta nodes
      var contractUntil = function(metaNodeMap, 
                     remainingEdges,
                     size, 
                     sizeLimit) {
        // Stop condition
        if (size <= sizeLimit) {
          return remainingEdges;
        }
        
        // Choose an edge randomly
        var edgeIndex = Math.floor((Math.random() * remainingEdges.length));

        // Colapse graph based on edge
        var newEdges = colapse(edgeIndex, metaNodeMap, remainingEdges);
        
        return contractUntil(metaNodeMap, 
                   newEdges, 
                   size - 1, 
                   sizeLimit);        
      };


      // Parse options
      // debug - optional
      if (options != null && options.debug != null) {
        var debug = options.debug;
      } else {
        var debug = false;
      }
      logDebug("Starting kargerStein..."); 

      var cy = this._private.cy;
      var edges = this.edges().not(':loop');
      var nodes = this.nodes();
      var numNodes = nodes.length;
      var numEdges = edges.length;
      var numIter = Math.ceil(Math.pow(Math.log(numNodes) / Math.LN2, 2));
      var stopSize = Math.floor(numNodes / Math.sqrt(2));

      if (numNodes < 2) {
        $$.util.error("At least 2 nodes are required for KargerSteing algorithm!"); 
        return undefined;
      }

      // Create numerical identifiers for each node
      // mapping: node id -> position in nodes array
      // for reverse mapping, simply use nodes array
      var id2position = {};
      for (var i = 0; i < numNodes; i++) {
        id2position[nodes[i].id()] = i;
      }

      // Now store edge destination as indexes
      // Format for each edge (edge index, source node index, target node index)
      var edgeIndexes = [];
      for (var i = 0; i < numEdges; i++) {
        var e = edges[i];
        edgeIndexes.push([i, id2position[e.source().id()], id2position[e.target().id()]]);
      }

      // We will store the best cut found here
      var minCutSize = Infinity;
      var minCut;     

      // Initial meta node partition
      var originalMetaNode = [];
      for (var i = 0; i < numNodes; i++) {
        originalMetaNode.push(i);
      }

      // Main loop
      for (var iter = 0; iter <= numIter; iter++) {
        // Create new meta node partition
        var metaNodeMap = originalMetaNode.slice(0);

        // Contract until stop point (stopSize nodes)
        var edgesState = contractUntil(metaNodeMap, edgeIndexes, numNodes, stopSize);
        
        // Create a copy of the colapsed nodes state
        var metaNodeMap2 = metaNodeMap.slice(0);

        // Run 2 iterations starting in the stop state
        var res1 = contractUntil(metaNodeMap, edgesState, stopSize, 2);
        var res2 = contractUntil(metaNodeMap2, edgesState, stopSize, 2);

        // Is any of the 2 results the best cut so far?
        if (res1.length <= res2.length && res1.length < minCutSize) {
          minCutSize = res1.length;
          minCut = [res1, metaNodeMap];
        } else if (res2.length <= res1.length && res2.length < minCutSize) {
          minCutSize = res2.length;
          minCut = [res2, metaNodeMap2];
        }
      } // end of main loop

      
      // Construct result
      var resEdges = (minCut[0]).map(function(e){ return edges[e[0]]; });
      var partition1 = [];
      var partition2 = [];

      // traverse metaNodeMap for best cut
      var witnessNodePartition = minCut[1][0];
      for (var i = 0; i < minCut[1].length; i++) { 
        var partitionId = minCut[1][i]; 
        if (partitionId === witnessNodePartition) {
          partition1.push(nodes[i]);
        } else {
          partition2.push(nodes[i]);
        }       
      }
      
      var ret = {
        cut: new $$.Collection(cy, resEdges),
        partition1: new $$.Collection(cy, partition1),
        partition2: new $$.Collection(cy, partition2)
      };
      
      return ret;
    },


    // 
    // options => options object
    //   dampingFactor: optional
    //   precision: optional
    //   iterations : optional
    // retObj => returned object by function
    //  rank : function that returns the pageRank of a given node (object or selector string)
    pageRank: function(options) {
      options = options || {};
      
      var normalizeVector = function(vector) {
        var length = vector.length;

        // First, get sum of all elements
        var total = 0; 
        for (var i = 0; i < length; i++) {
          total += vector[i];
        }

        // Now, divide each by the sum of all elements
        for (var i = 0; i < length; i++) {
          vector[i] = vector[i] / total;
        }
      };
      
      var logDebug = function() {
        if (debug) {
          console.log.apply(console, arguments);
        }
      };
      
      // Parse options
      // debug - optional
      if (options != null && 
        options.debug != null) {
        var debug = options.debug;
      } else {
        var debug = false;
      }
      logDebug("Starting pageRank..."); 

      // dampingFactor - optional
      if (options != null && 
        options.dampingfactor != null) {
        var dampingFactor = options.dampingFactor;
      } else {
        var dampingFactor = 0.8; // Default damping factor
      }

      // desired precision - optional
      if (options != null && 
        options.precision != null) {
        var epsilon = options.precision;
      } else {
        var epsilon = 0.000001; // Default precision
      }

      // Max number of iterations - optional
      if (options != null && 
        options.iterations != null) {
        var numIter = options.iterations;
      } else {
        var numIter = 200; // Default number of iterations
      }

      // Weight function - optional
      if (options != null && 
        options.weight != null && 
        $$.is.fn(options.weight)) {       
        var weightFn = options.weight;
      } else {
        // If not specified, assume each edge has equal weight (1)
        var weightFn = function(e) {return 1;}; 
      }

      var cy = this._private.cy;
      var edges = this.edges().not(':loop');
      var nodes = this.nodes();
      var numNodes = nodes.length;
      var numEdges = edges.length;

      // Create numerical identifiers for each node
      // mapping: node id -> position in nodes array
      // for reverse mapping, simply use nodes array
      var id2position = {};
      for (var i = 0; i < numNodes; i++) {
        id2position[nodes[i].id()] = i;
      }

      // Construct transposed adjacency matrix
      // First lets have a zeroed matrix of the right size
      // We'll also keep track of the sum of each column
      var matrix = [];
      var columnSum = [];
      var additionalProb = (1 - dampingFactor) / numNodes;

      // Create null matric
      for (var i = 0; i < numNodes; i++) { 
        var newRow = [];
        for (var j = 0; j < numNodes; j++) {
          newRow.push(0.0);
        }
        matrix.push(newRow);
        columnSum.push(0.0);
      }

      // Now, process edges
      for (var i = 0; i < numEdges; i++) {
        var edge = edges[i];
        var s = id2position[edge.source().id()];
        var t = id2position[edge.target().id()];
        var w = weightFn.apply(edge, [edge]);
        
        // Update matrix
        matrix[t][s] += w;

        // Update column sum
        columnSum[s] += w; 
      }

      // Add additional probability based on damping factor
      // Also, take into account columns that have sum = 0
      var p = 1.0 / numNodes + additionalProb; // Shorthand
      // Traverse matrix, column by column
      for (var j = 0; j < numNodes; j++) { 
        if (columnSum[j] === 0) {
          // No 'links' out from node jth, assume equal probability for each possible node
          for (var i = 0; i < numNodes; i++) {
            matrix[i][j] = p;
          }
        } else {
          // Node jth has outgoing link, compute normalized probabilities
          for (var i = 0; i < numNodes; i++) {
            matrix[i][j] = matrix[i][j] / columnSum[j] + additionalProb;
          }         
        }
      }

      // Compute dominant eigenvector using power method
      var eigenvector = [];
      var nullVector = [];
      var previous;

      // Start with a vector of all 1's
      // Also, initialize a null vector which will be used as shorthand
      for (var i = 0; i < numNodes; i++) {
        eigenvector.push(1.0);
        nullVector.push(0.0);
      }
            
      for (var iter = 0; iter < numIter; iter++) {
        // New array with all 0's
        var temp = nullVector.slice(0);
        
        // Multiply matrix with previous result
        for (var i = 0; i < numNodes; i++) {
          for (var j = 0; j < numNodes; j++) {        
            temp[i] += matrix[i][j] * eigenvector[j];
          }
        }

        normalizeVector(temp);
        previous = eigenvector;
        eigenvector = temp;

        var diff = 0;
        // Compute difference (squared module) of both vectors
        for (var i = 0; i < numNodes; i++) {
          diff += Math.pow(previous[i] - eigenvector[i], 2);
        }
        
        // If difference is less than the desired threshold, stop iterating
        if (diff < epsilon) {
          logDebug("Stoped at iteration %s", iter);
          break;
        }
      }
            
      logDebug("Result:\n" + eigenvector);

      // Construct result
      var res = {
        rank : function(node) {
          if ($$.is.string(node)) {
            // is a selector string
            var nodeId = (cy.filter(node)[0]).id();
          } else {
            // is a node object
            var nodeId = node.id();
          }
          return eigenvector[id2position[nodeId]];
        }
      };


      return res;
    } // pageRank

  }); // $$.fn.eles


}) (cytoscape);
;(function( $$ ){ 'use strict';

  $$.fn.eles({
    animated: $$.define.animated(),
    clearQueue: $$.define.clearQueue(),
    delay: $$.define.delay(),
    animate: $$.define.animate(),
    stop: $$.define.stop()
  });
  
})( cytoscape );  

;(function( $$ ){ 'use strict';
  
  $$.fn.eles({
    classes: function(opts){
      var eles = this;
      var changed = [];
      var fn;

      if( $$.is.fn(opts) ){
        fn = opts;

      } else if( !$$.is.plainObject(opts) ){
        return this; // needs opts or fn
      } 

      for(var i = 0; i < eles.length; i++){
        var ele = eles[i];
        var eleChanged = false;

        opts = fn ? fn.apply(ele, [i, ele]) : opts;

        // add classes
        if( opts.add ){ for( var j = 0; j < opts.add.length; j++ ){
          var cls = opts.add[j];
          var hasClass = ele._private.classes[cls];

          ele._private.classes[cls] = true;

          if( !hasClass && !eleChanged ){
            changed.push( ele );
            eleChanged = true;
          }
        } }

        // remove classes
        if( opts.remove ){ for( var j = 0; j < opts.remove.length; j++ ){
          var cls = opts.remove[j];
          var hasClass = ele._private.classes[cls];

          ele._private.classes[cls] = false;

          if( hasClass && !eleChanged ){
            changed.push( ele );
            eleChanged = true;
          }
        } }

        // toggle classes
        if( opts.toggle ){ for( var j = 0; j < opts.toggle.length; j++ ){
          var cls = opts.toggle[j];
          var hasClass = ele._private.classes[cls];

          ele._private.classes[cls] = !hasClass;

          if( !eleChanged ){
            changed.push( ele );
            eleChanged = true;
          }
        } }
      }

      if( changed.length > 0 ){
        new $$.Collection( this.cy(), changed )
          .updateStyle()
          .trigger('class')
        ;
      }

      return this;
    },

    addClass: function(classes){
      classes = classes.split(/\s+/);
      var self = this;
      var changed = [];
      
      for( var i = 0; i < classes.length; i++ ){
        var cls = classes[i];
        if( $$.is.emptyString(cls) ){ continue; }
        
        for( var j = 0; j < self.length; j++ ){
          var ele = self[j];
          var hasClass = ele._private.classes[cls];
          ele._private.classes[cls] = true;

          if( !hasClass ){ // if didn't already have, add to list of changed
            changed.push( ele );
          }
        }
      }
      
      // trigger update style on those eles that had class changes
      if( changed.length > 0 ){
        new $$.Collection(this._private.cy, changed)
          .updateStyle()
          .trigger('class')
        ;
      }

      return self;
    },

    hasClass: function(className){
      var ele = this[0];
      return ( ele != null && ele._private.classes[className] ) ? true : false;
    },

    toggleClass: function(classesStr, toggle){
      var classes = classesStr.split(/\s+/);
      var self = this;
      var changed = []; // eles who had classes changed
      
      for( var i = 0, il = self.length; i < il; i++ ){
        var ele = self[i];

        for( var j = 0; j < classes.length; j++ ){
          var cls = classes[j];

          if( $$.is.emptyString(cls) ){ continue; }
          
          var hasClass = ele._private.classes[cls];
          var shouldAdd = toggle || (toggle === undefined && !hasClass);

          if( shouldAdd ){
            ele._private.classes[cls] = true;

            if( !hasClass ){ changed.push(ele); }
          } else { // then remove
            ele._private.classes[cls] = false;

            if( hasClass ){ changed.push(ele); }
          }

        } // for j classes
      } // for i eles
      
      // trigger update style on those eles that had class changes
      if( changed.length > 0 ){
        new $$.Collection(this._private.cy, changed)
          .updateStyle()
          .trigger('class')
        ;
      }

      return self;
    },

    removeClass: function(classes){
      classes = classes.split(/\s+/);
      var self = this;
      var changed = [];

      for( var i = 0; i < self.length; i++ ){
        var ele = self[i];

        for( var j = 0; j < classes.length; j++ ){
          var cls = classes[j];
          if( !cls || cls === '' ){ continue; }

          var hasClass = ele._private.classes[cls];
          ele._private.classes[cls] = undefined;

          if( hasClass ){ // then we changed its set of classes
            changed.push( ele );
          }
        }
      }
      
      // trigger update style on those eles that had class changes
      if( changed.length > 0 ){
        new $$.Collection(self._private.cy, changed).updateStyle();
      }

      self.trigger('class');
      return self;
    },

    flashClass: function(classes, duration){
      var self = this;

      if( duration == null ){
        duration = 250;
      } else if( duration === 0 ){
        return self; // nothing to do really
      }

      self.addClass( classes );
      setTimeout(function(){
        self.removeClass( classes );
      }, duration);

      return self;
    }
  });
  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.eles({
    allAre: function( selector ){
      return this.filter(selector).length === this.length;
    },

    is: function( selector ){
      return this.filter(selector).length > 0;
    },

    some: function( fn, thisArg ){
      for( var i = 0; i < this.length; i++ ){
        var ret = fn.apply( thisArg, [ this[i], i, this ] );

        if( ret ){
          return true;
        }
      }

      return false;
    },

    every: function( fn, thisArg ){
      for( var i = 0; i < this.length; i++ ){
        var ret = fn.apply( thisArg, [ this[i], i, this ] );

        if( !ret ){
          return false;
        }
      }

      return true;
    },

    same: function( collection ){
      collection = this.cy().collection( collection );

      // cheap extra check
      if( this.length !== collection.length ){
        return false;
      }

      return this.intersect( collection ).length === this.length;
    },

    anySame: function( collection ){
      collection = this.cy().collection( collection );

      return this.intersect( collection ).length > 0;
    },

    allAreNeighbors: function( collection ){
      collection = this.cy().collection( collection );

      return this.neighborhood().intersect( collection ).length === collection.length;
    }
  });
  
})( cytoscape );

;(function($$){ 'use strict';

  // Compound functions
  /////////////////////

  $$.fn.eles({
    parent: function( selector ){
      var parents = [];
      var cy = this._private.cy;

      for( var i = 0; i < this.length; i++ ){
        var ele = this[i];
        var parent = cy.getElementById( ele._private.data.parent );

        if( parent.size() > 0 ){
          parents.push( parent );
        }
      }
      
      return new $$.Collection( cy, parents, { unique: true } ).filter( selector );
    },

    parents: function( selector ){
      var parents = [];

      var eles = this.parent();
      while( eles.nonempty() ){
        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];
          parents.push( ele );
        }

        eles = eles.parent();
      }

      return new $$.Collection( this.cy(), parents, { unique: true } ).filter( selector );
    },

    commonAncestors: function( selector ){
      var ancestors;

      for( var i = 0; i < this.length; i++ ){
        var ele = this[i];
        var parents = ele.parents();
        
        ancestors = ancestors || parents;

        ancestors = ancestors.intersect( parents ); // current list must be common with current ele parents set
      }

      return ancestors.filter( selector );
    },

    orphans: function( selector ){
      return this.stdFilter(function( ele ){
        return ele.isNode() && ele.parent().empty();
      }).filter( selector );
    },

    nonorphans: function( selector ){
      return this.stdFilter(function( ele ){
        return ele.isNode() && ele.parent().nonempty();
      }).filter( selector );
    },

    children: function( selector ){
      var children = [];

      for( var i = 0; i < this.length; i++ ){
        var ele = this[i];
        children = children.concat( ele._private.children );
      }

      return new $$.Collection( this.cy(), children, { unique: true } ).filter( selector );
    },

    siblings: function( selector ){
      return this.parent().children().not( this ).filter( selector );
    },

    isParent: function(){
      var ele = this[0];

      if( ele ){
        return ele._private.children.length !== 0;
      }
    },

    isChild: function(){
      var ele = this[0];

      if( ele ){
        return ele._private.data.parent !== undefined && ele.parent().length !== 0;
      }
    },

    descendants: function( selector ){
      var elements = [];

      function add( eles ){
        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];

          elements.push( ele );

          if( ele.children().nonempty() ){
            add( ele.children() );
          }
        }
      }

      add( this.children() );

      return new $$.Collection( this.cy(), elements, { unique: true } ).filter( selector );
    }
  });

  // aliases
  $$.elesfn.ancestors = $$.elesfn.parents;
  
})( cytoscape );
;(function($$){ 'use strict';
  
  var borderWidthMultiplier = 2 * 0.5;
  var borderWidthAdjustment = 0;

  $$.fn.eles({

    data: $$.define.data({
      field: 'data',
      bindingEvent: 'data',
      allowBinding: true,
      allowSetting: true,
      settingEvent: 'data',
      settingTriggersEvent: true,
      triggerFnName: 'trigger',
      allowGetting: true,
      immutableKeys: {
        'id': true,
        'source': true,
        'target': true,
        'parent': true
      },
      updateStyle: true
    }),

    removeData: $$.define.removeData({
      field: 'data',
      event: 'data',
      triggerFnName: 'trigger',
      triggerEvent: true,
      immutableKeys: {
        'id': true,
        'source': true,
        'target': true,
        'parent': true
      },
      updateStyle: true
    }),

    scratch: $$.define.data({
      field: 'scratch',
      allowBinding: false,
      allowSetting: true,
      settingTriggersEvent: false,
      allowGetting: true
    }),

    removeScratch: $$.define.removeData({
      field: 'scratch',
      triggerEvent: false
    }),

    rscratch: $$.define.data({
      field: 'rscratch',
      allowBinding: false,
      allowSetting: true,
      settingTriggersEvent: false,
      allowGetting: true
    }),

    removeRscratch: $$.define.removeData({
      field: 'rscratch',
      triggerEvent: false
    }),

    id: function(){
      var ele = this[0];

      if( ele ){
        return ele._private.data.id;
      }
    },

    position: $$.define.data({
      field: 'position',
      bindingEvent: 'position',
      allowBinding: true,
      allowSetting: true,
      settingEvent: 'position',
      settingTriggersEvent: true,
      triggerFnName: 'rtrigger',
      allowGetting: true,
      validKeys: ['x', 'y'],
      onSet: function( eles ){
        var updatedEles = eles.updateCompoundBounds();
        updatedEles.rtrigger('position');
      },
      canSet: function( ele ){
        return !ele.locked();
      }
    }),

    // position but no notification to renderer
    silentPosition: $$.define.data({
      field: 'position',
      bindingEvent: 'position',
      allowBinding: false,
      allowSetting: true,
      settingEvent: 'position',
      settingTriggersEvent: false,
      triggerFnName: 'trigger',
      allowGetting: true,
      validKeys: ['x', 'y'],
      onSet: function( eles ){
        eles.updateCompoundBounds();
      },
      canSet: function( ele ){
        return !ele.locked();
      }
    }),

    positions: function( pos, silent ){
      if( $$.is.plainObject(pos) ){
        this.position(pos);
        
      } else if( $$.is.fn(pos) ){
        var fn = pos;
        
        for( var i = 0; i < this.length; i++ ){
          var ele = this[i];

          var pos = fn.apply(ele, [i, ele]);

          if( pos && !ele.locked() ){
            var elePos = ele._private.position;
            elePos.x = pos.x;
            elePos.y = pos.y;
          }
        }

        var updatedEles = this.updateCompoundBounds();
        var toTrigger = updatedEles.length > 0 ? this.add( updatedEles ) : this;

        if( silent ){
          toTrigger.trigger('position');
        } else {
          toTrigger.rtrigger('position');
        }
      }

      return this; // chaining
    },

    silentPositions: function( pos ){
      return this.positions( pos, true );
    },

    updateCompoundBounds: function(){
      var cy = this.cy();

      if( !cy.styleEnabled() || !cy.hasCompoundNodes() ){ return cy.collection(); } // save cycles for non compound graphs or when style disabled

      var updated = [];

      function update( parent ){
        var children = parent.children();
        var style = parent._private.style;
        var bb = children.boundingBox({ includeLabels: false, includeEdges: false });
        var padding = {
          top: style['padding-top'].pxValue,
          bottom: style['padding-bottom'].pxValue,
          left: style['padding-left'].pxValue,
          right: style['padding-right'].pxValue
        };
        var pos = parent._private.position;
        var didUpdate = false;

        if( style['width'].value === 'auto' ){
          parent._private.autoWidth = bb.w + padding.left + padding.right;
          pos.x = (bb.x1 + bb.x2 - padding.left + padding.right)/2;
          didUpdate = true;
        }

        if( style['height'].value === 'auto' ){
          parent._private.autoHeight = bb.h + padding.top + padding.bottom;
          pos.y = (bb.y1 + bb.y2 - padding.top + padding.bottom)/2;
          didUpdate = true;
        }

        if( didUpdate ){
          updated.push( parent );
        }
      }

      // go up, level by level
      var eles = this.parent();
      while( eles.nonempty() ){

        // update each parent node in this level
        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];

          update( ele );
        }

        // next level
        eles = eles.parent();
      }

      // return changed
      return new $$.Collection( cy, updated );
    },

    // get/set the rendered (i.e. on screen) positon of the element
    renderedPosition: function( dim, val ){
      var ele = this[0];
      var cy = this.cy();
      var zoom = cy.zoom();
      var pan = cy.pan();
      var rpos = $$.is.plainObject( dim ) ? dim : undefined;
      var setting = rpos !== undefined || ( val !== undefined && $$.is.string(dim) );

      if( ele && ele.isNode() ){ // must have an element and must be a node to return position
        if( setting ){
          for( var i = 0; i < this.length; i++ ){
            var ele = this[i];

            if( val !== undefined ){ // set one dimension
              ele._private.position[dim] = ( val - pan[dim] )/zoom;
            } else if( rpos !== undefined ){ // set whole position
              ele._private.position = {
                x: ( rpos.x - pan.x ) /zoom,
                y: ( rpos.y - pan.y ) /zoom
              };
            }
          }

          this.rtrigger('position');
        } else { // getting
          var pos = ele._private.position;
          rpos = {
            x: pos.x * zoom + pan.x,
            y: pos.y * zoom + pan.y
          };

          if( dim === undefined ){ // then return the whole rendered position
            return rpos;
          } else { // then return the specified dimension
            return rpos[ dim ];
          }
        }
      } else if( !setting ){
        return undefined; // for empty collection case
      }

      return this; // chaining
    },

    // get/set the position relative to the parent
    parentPosition: function( dim, val ){
      var ele = this[0];
      var cy = this.cy();
      var ppos = $$.is.plainObject( dim ) ? dim : undefined;
      var setting = ppos !== undefined || ( val !== undefined && $$.is.string(dim) );
      var hasCompoundNodes = cy.hasCompoundNodes();

      if( ele && ele.isNode() ){ // must have an element and must be a node to return position
        if( setting ){
          for( var i = 0; i < this.length; i++ ){
            var ele = this[i];
            var parent = hasCompoundNodes ? ele.parent() : null;
            var hasParent = parent && parent.length > 0;
            var relativeToParent = hasParent;

            if( hasParent ){
              parent = parent[0];
            }

            var origin = relativeToParent ? parent._private.position : { x: 0, y: 0 };

            if( val !== undefined ){ // set one dimension
              ele._private.position[dim] = val + origin[dim];
            } else if( ppos !== undefined ){ // set whole position
              ele._private.position = {
                x: ppos.x + origin.x,
                y: ppos.y + origin.y,
              };
            }
          }

          this.rtrigger('position');

        } else { // getting
          var pos = ele._private.position;
          var parent = hasCompoundNodes ? ele.parent() : null;
          var hasParent = parent && parent.length > 0;
          var relativeToParent = hasParent;

          if( hasParent ){
            parent = parent[0];
          }

          var origin = relativeToParent ? parent._private.position : { x: 0, y: 0 };

          ppos = {
            x: pos.x - origin.x,
            y: pos.y - origin.y
          };

          if( dim === undefined ){ // then return the whole rendered position
            return ppos;
          } else { // then return the specified dimension
            return ppos[ dim ];
          }
        }
      } else if( !setting ){
        return undefined; // for empty collection case
      }

      return this; // chaining
    },

    // convenience function to get a numerical value for the width of the node/edge
    width: function(){
      var ele = this[0];
      var cy = ele._private.cy;
      var styleEnabled = cy._private.styleEnabled;

      if( ele ){
        if( styleEnabled ){
          var w = ele._private.style.width;
          return w.strValue === 'auto' ? ele._private.autoWidth : w.pxValue;
        } else {
          return 1;
        }
      }
    },

    outerWidth: function(){
      var ele = this[0];
      var cy = ele._private.cy;
      var styleEnabled = cy._private.styleEnabled;

      if( ele ){
        if( styleEnabled ){
          var style = ele._private.style;
          var width = style.width.strValue === 'auto' ? ele._private.autoWidth : style.width.pxValue;
          var border = style['border-width'] ? style['border-width'].pxValue * borderWidthMultiplier + borderWidthAdjustment : 0;

          return width + border;
        } else {
          return 1;
        }
      }
    },

    renderedWidth: function(){
      var ele = this[0];

      if( ele ){
        var width = ele.width();
        return width * this.cy().zoom();
      }
    },

    renderedOuterWidth: function(){
      var ele = this[0];

      if( ele ){
        var owidth = ele.outerWidth();
        return owidth * this.cy().zoom();
      }
    },

    // convenience function to get a numerical value for the height of the node
    height: function(){ 
      var ele = this[0];
      var cy = ele._private.cy;
      var styleEnabled = cy._private.styleEnabled;

      if( ele && ele._private.group === 'nodes' ){
        if( styleEnabled ){
          var h = ele._private.style.height;
          return h.strValue === 'auto' ? ele._private.autoHeight : h.pxValue;
        } else {
          return 1;
        }
      }
    },

    outerHeight: function(){
      var ele = this[0];
      var cy = ele._private.cy;
      var styleEnabled = cy._private.styleEnabled;

      if( ele && ele._private.group === 'nodes' ){
        if( styleEnabled ){
          var style = ele._private.style;
          var height = style.height.strValue === 'auto' ? ele._private.autoHeight : style.height.pxValue;
          var border = style['border-width'] ? style['border-width'].pxValue * borderWidthMultiplier + borderWidthAdjustment : 0;
        } else {
          return 1;
        }

        return height + border;
      }
    },

    renderedHeight: function(){
      var ele = this[0];

      if( ele && ele._private.group === 'nodes' ){
        var height = ele.height();
        return height * this.cy().zoom();
      }
    },

    renderedOuterHeight: function(){
      var ele = this[0];

      if( ele && ele._private.group === 'nodes' ){
        var oheight = ele.outerHeight();
        return oheight * this.cy().zoom();
      }
    },

    renderedBoundingBox: function( options ){
      var bb = this.boundingBox( options );
      var cy = this.cy();
      var zoom = cy.zoom();
      var pan = cy.pan();

      var x1 = bb.x1 * zoom + pan.x;
      var x2 = bb.x2 * zoom + pan.x;
      var y1 = bb.y1 * zoom + pan.y;
      var y2 = bb.y2 * zoom + pan.y;

      return {
        x1: x1,
        x2: x2,
        y1: y1,
        y2: y2,
        w: x2 - x1,
        h: y2 - y1
      };
    },

    // get the bounding box of the elements (in raw model position)
    boundingBox: function( options ){
      var eles = this;
      var cy = eles._private.cy;
      var cy_p = cy._private;
      var styleEnabled = cy_p.styleEnabled;

      options = options || {};

      var includeNodes = options.includeNodes === undefined ? true : options.includeNodes;
      var includeEdges = options.includeEdges === undefined ? true : options.includeEdges;
      var includeLabels = options.includeLabels === undefined ? true : options.includeLabels;

      // recalculate projections etc
      if( styleEnabled ){
        cy_p.renderer.recalculateRenderedStyle( this );
      }

      var x1 = Infinity;
      var x2 = -Infinity;
      var y1 = Infinity;
      var y2 = -Infinity;

      // find bounds of elements
      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var _p = ele._private;
        var display = styleEnabled ? _p.style['display'].value : 'element';
        var isNode = _p.group === 'nodes';
        var ex1, ex2, ey1, ey2, x, y;
        var includedEle = false;

        if( display === 'none' ){ continue; } // then ele doesn't take up space      

        if( isNode && includeNodes ){
          includedEle = true;

          var pos = _p.position;
          x = pos.x;
          y = pos.y;
          var w = ele.outerWidth();
          var halfW = w/2;
          var h = ele.outerHeight();
          var halfH = h/2;

          // handle node dimensions
          /////////////////////////

          ex1 = x - halfW;
          ex2 = x + halfW;
          ey1 = y - halfH;
          ey2 = y + halfH;

          x1 = ex1 < x1 ? ex1 : x1;
          x2 = ex2 > x2 ? ex2 : x2;
          y1 = ey1 < y1 ? ey1 : y1;
          y2 = ey2 > y2 ? ey2 : y2;

        } else if( ele.isEdge() && includeEdges ){ 
          includedEle = true;

          var n1pos = ele._private.source._private.position;
          var n2pos = ele._private.target._private.position;

          // handle edge dimensions (rough box estimate)
          //////////////////////////////////////////////

          var rstyle = ele._private.rstyle || {};

          ex1 = n1pos.x;
          ex2 = n2pos.x;
          ey1 = n1pos.y;
          ey2 = n2pos.y;

          if( ex1 > ex2 ){
            var temp = ex1;
            ex1 = ex2;
            ex2 = temp;
          }

          if( ey1 > ey2 ){
            var temp = ey1;
            ey1 = ey2;
            ey2 = temp;
          }

          x1 = ex1 < x1 ? ex1 : x1;
          x2 = ex2 > x2 ? ex2 : x2;
          y1 = ey1 < y1 ? ey1 : y1;
          y2 = ey2 > y2 ? ey2 : y2;

          // handle points along edge (sanity check)
          //////////////////////////////////////////

          if( styleEnabled ){
            var bpts = rstyle.bezierPts || [];

            var w = ele._private.style['width'].pxValue;
            var wHalf = w/2;

            for( var j = 0; j < bpts.length; j++ ){
              var bpt = bpts[j];

              ex1 = bpt.x - wHalf;
              ex2 = bpt.x + wHalf;
              ey1 = bpt.y - wHalf;
              ey2 = bpt.y + wHalf;

              x1 = ex1 < x1 ? ex1 : x1;
              x2 = ex2 > x2 ? ex2 : x2;
              y1 = ey1 < y1 ? ey1 : y1;
              y2 = ey2 > y2 ? ey2 : y2;
            }
          }

        } // edges

        // handle label dimensions
        //////////////////////////

        if( styleEnabled ){

          var style = ele._private.style;
          var rstyle = ele._private.rstyle;
          var label = style['content'].strValue;
          var fontSize = style['font-size'];
          var halign = style['text-halign'];
          var valign = style['text-valign'];
          var labelWidth = rstyle.labelWidth;
          var labelHeight = rstyle.labelHeight;
          var labelX = rstyle.labelX;
          var labelY = rstyle.labelY;

          if( includedEle && includeLabels && label && fontSize && labelHeight != null && labelWidth != null && labelX != null && labelY != null && halign && valign ){
            var lh = labelHeight;
            var lw = labelWidth;
            var lx1, lx2, ly1, ly2;

            if( ele.isEdge() ){
              lx1 = labelX - lw/2;
              lx2 = labelX + lw/2;
              ly1 = labelY - lh/2;
              ly2 = labelY + lh/2;
            } else {
              switch( halign.value ){
                case 'left':
                  lx1 = labelX - lw;
                  lx2 = labelX;
                  break;

                case 'center':
                  lx1 = labelX - lw/2;
                  lx2 = labelX + lw/2;
                  break;

                case 'right':
                  lx1 = labelX;
                  lx2 = labelX + lw;
                  break;
              }

              switch( valign.value ){
                case 'top':
                  ly1 = labelY - lh;
                  ly2 = labelY;
                  break;

                case 'center':
                  ly1 = labelY - lh/2;
                  ly2 = labelY + lh/2;
                  break;

                case 'bottom':
                  ly1 = labelY;
                  ly2 = labelY + lh;
                  break;
              }
            }

            x1 = lx1 < x1 ? lx1 : x1;
            x2 = lx2 > x2 ? lx2 : x2;
            y1 = ly1 < y1 ? ly1 : y1;
            y2 = ly2 > y2 ? ly2 : y2;
          }
        } // style enabled
      } // for

      return {
        x1: x1,
        x2: x2,
        y1: y1,
        y2: y2,
        w: x2 - x1,
        h: y2 - y1
      };
    }
  }); 

  // in case some users want to be explicit
  $$.elesfn.modelPosition = $$.elesfn.position;
  $$.elesfn.modelPositions = $$.elesfn.positions;
  
})( cytoscape );

;(function( $$ ){ 'use strict';
  
  // Regular degree functions (works on single element)
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  function defineDegreeFunction(callback){
    return function( includeLoops ){
      var self = this;

      if( includeLoops === undefined ){
        includeLoops = true;
      }
      
      if( self.length === 0 ){ return; }

      if( self.isNode() && !self.removed() ){
        var degree = 0;
        var node = self[0];
        var connectedEdges = node._private.edges;

        for( var i = 0; i < connectedEdges.length; i++ ){
          var edge = connectedEdges[i];

          if( !includeLoops && edge.isLoop() ){
            continue;
          }

          degree += callback( node, edge );
        }
        
        return degree;
      } else {
        return;
      }
    };
  }
  
  $$.fn.eles({
    degree: defineDegreeFunction(function(node, edge){
      if( edge.source().same( edge.target() ) ){
        return 2;
      } else {
        return 1;
      }
    }),

    indegree: defineDegreeFunction(function(node, edge){
      if( edge.target().same(node) ){
        return 1;
      } else {
        return 0;
      }
    }),

    outdegree: defineDegreeFunction(function(node, edge){
      if( edge.source().same(node) ){
        return 1;
      } else {
        return 0;
      }
    })
  });
  
  
  // Collection degree stats
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  function defineDegreeBoundsFunction(degreeFn, callback){
    return function( includeLoops ){
      var ret;
      var nodes = this.nodes();

      for( var i = 0; i < nodes.length; i++ ){
        var ele = nodes[i];
        var degree = ele[degreeFn]( includeLoops );
        if( degree !== undefined && (ret === undefined || callback(degree, ret)) ){
          ret = degree;
        }
      }
      
      return ret;
    };
  }
  
  $$.fn.eles({
    minDegree: defineDegreeBoundsFunction('degree', function(degree, min){
      return degree < min;
    }),

    maxDegree: defineDegreeBoundsFunction('degree', function(degree, max){
      return degree > max;
    }),

    minIndegree: defineDegreeBoundsFunction('indegree', function(degree, min){
      return degree < min;
    }),

    maxIndegree: defineDegreeBoundsFunction('indegree', function(degree, max){
      return degree > max;
    }),

    minOutdegree: defineDegreeBoundsFunction('outdegree', function(degree, min){
      return degree < min;
    }),

    maxOutdegree: defineDegreeBoundsFunction('outdegree', function(degree, max){
      return degree > max;
    })
  });
  
  $$.fn.eles({
    totalDegree: function( includeLoops ){
      var total = 0;
      var nodes = this.nodes();

      for( var i = 0; i < nodes.length; i++ ){
        total += nodes[i].degree( includeLoops );
      }

      return total;
    }
  });
  
})( cytoscape );

  
;(function($$){ 'use strict';
  
  // Functions for binding & triggering events
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  $$.fn.eles({
    on: $$.define.on(), // .on( events [, selector] [, data], handler)
    one: $$.define.on({ unbindSelfOnTrigger: true }),
    once: $$.define.on({ unbindAllBindersOnTrigger: true }),
    off: $$.define.off(), // .off( events [, selector] [, handler] )
    trigger: $$.define.trigger(), // .trigger( events [, extraParams] )

    rtrigger: function(event, extraParams){ // for internal use only
      if( this.length === 0 ){ return; } // empty collections don't need to notify anything

      // notify renderer
      this.cy().notify({
        type: event,
        collection: this
      });
      
      this.trigger(event, extraParams);
      return this;
    }
  });

  // aliases for those folks who like old stuff:
  $$.elesfn.bind = $$.elesfn.on;
  $$.elesfn.unbind = $$.elesfn.off;
  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.eles({
    nodes: function( selector ){
      return this.filter(function(i, element){
        return element.isNode();
      }).filter(selector);
    },

    edges: function( selector ){
      return this.filter(function(i, element){
        return element.isEdge();
      }).filter(selector);
    },

    filter: function( filter ){
      var cy = this._private.cy;
      
      if( $$.is.fn(filter) ){
        var elements = [];

        for( var i = 0; i < this.length; i++ ){
          var ele = this[i];

          if( filter.apply(ele, [i, ele]) ){
            elements.push(ele);
          }
        }
        
        return new $$.Collection(cy, elements);
      
      } else if( $$.is.string(filter) || $$.is.elementOrCollection(filter) ){
        return new $$.Selector(filter).filter(this);
      
      } else if( filter === undefined ){
        return this;
      }

      return new $$.Collection( cy ); // if not handled by above, give 'em an empty collection
    },

    not: function( toRemove ){
      var cy = this._private.cy;

      if( !toRemove ){
        return this;
      } else {
      
        if( $$.is.string( toRemove ) ){
          toRemove = this.filter( toRemove );
        }
        
        var elements = [];
        
        for( var i = 0; i < this.length; i++ ){
          var element = this[i];

          var remove = toRemove._private.ids[ element.id() ];
          if( !remove ){
            elements.push( element );
          }
        }
        
        return new $$.Collection( cy, elements );
      }
      
    },

    intersect: function( other ){
      var cy = this._private.cy;
      
      // if a selector is specified, then filter by it instead
      if( $$.is.string(other) ){
        var selector = other;
        return this.filter( selector );
      }
      
      var elements = [];
      var col1 = this;
      var col2 = other;
      var col1Smaller = this.length < other.length;
      // var ids1 = col1Smaller ? col1._private.ids : col2._private.ids;
      var ids2 = col1Smaller ? col2._private.ids : col1._private.ids;
      var col = col1Smaller ? col1 : col2;
      
      for( var i = 0; i < col.length; i++ ){
        var id = col[i]._private.data.id;
        var ele = ids2[ id ];

        if( ele ){
          elements.push( ele );
        }
      }
      
      return new $$.Collection( cy, elements );
    },

    add: function( toAdd ){
      var cy = this._private.cy;    
      
      if( !toAdd ){
        return this;
      }
      
      if( $$.is.string(toAdd) ){
        var selector = toAdd;
        toAdd = cy.elements(selector);
      }
      
      var elements = [];

      for( var i = 0; i < this.length; i++ ){
        elements.push( this[i] );
      }

      for( var i = 0; i < toAdd.length; i++ ){

        var add = !this._private.ids[ toAdd[i].id() ];
        if( add ){
          elements.push( toAdd[i] );
        }
      }
      
      return new $$.Collection(cy, elements);
    },

    // in place merge on calling collection
    merge: function( toAdd ){
      var _p = this._private;
      var cy = _p.cy;    
      
      if( !toAdd ){
        return this;
      }
      
      if( $$.is.string(toAdd) ){
        var selector = toAdd;
        toAdd = cy.elements(selector);
      }

      for( var i = 0; i < toAdd.length; i++ ){
        var toAddEle = toAdd[i];
        var id = toAddEle.id();
        var add = !_p.ids[ id ];

        if( add ){
          var index = this.length++;

          this[ index ] = toAddEle;
          _p.ids[ id ] = toAddEle;
          _p.indexes[ id ] = index;
        }
      }
      
      return this; // chaining
    },

    // remove single ele in place in calling collection
    unmergeOne: function( ele ){
      ele = ele[0];

      var _p = this._private;
      var id = ele.id();
      var i = _p.indexes[ id ];

      if( i == null ){
        return this; // no need to remove
      }

      // remove ele
      this[i] = undefined;
      _p.ids[ id ] = undefined;
      _p.indexes[ id ] = undefined;

      var unmergedLastEle = i === this.length - 1;

      // replace empty spot with last ele in collection
      if( this.length > 1 && !unmergedLastEle ){
        var lastEleI = this.length - 1;
        var lastEle = this[ lastEleI ];

        this[ lastEleI ] = undefined;
        this[i] = lastEle;
        _p.indexes[ lastEle.id() ] = i;
      }

      // the collection is now 1 ele smaller
      this.length--;

      return this;
    },

    // remove eles in place on calling collection
    unmerge: function( toRemove ){
      var cy = this._private.cy;    
      
      if( !toRemove ){
        return this;
      }

      if( $$.is.string(toRemove) ){
        var selector = toRemove;
        toRemove = cy.elements(selector);
      }

      for( var i = 0; i < toRemove.length; i++ ){
        this.unmergeOne( toRemove[i] );
      }
      
      return this; // chaining
    },

    map: function( mapFn, thisArg ){
      var arr = [];
      var eles = this;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var ret = mapFn.apply( thisArg, [ele, i, eles] );

        arr.push( ret );
      }

      return arr;
    },

    stdFilter: function( fn, thisArg ){
      var filterEles = [];
      var eles = this;
      var cy = this._private.cy;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var include = fn.apply( thisArg, [ele, i, eles] );

        if( include ){
          filterEles.push( ele );
        }
      }

      return new $$.Collection( cy, filterEles );
    },

    max: function( valFn, thisArg ){
      var max = -Infinity;
      var maxEle;
      var eles = this;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var val = valFn.apply( thisArg, [ ele, i, eles ] );

        if( val > max ){
          max = val;
          maxEle = ele;
        }
      }

      return {
        value: max,
        ele: maxEle
      };
    },

    min: function( valFn, thisArg ){
      var min = Infinity;
      var minEle;
      var eles = this;

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var val = valFn.apply( thisArg, [ ele, i, eles ] );

        if( val < min ){
          min = val;
          minEle = ele;
        }
      }

      return {
        value: min,
        ele: minEle
      };
    }
  });
  
})( cytoscape );
;(function($$){ 'use strict';

  $$.fn.eles({
    isNode: function(){
      return this.group() === 'nodes';
    },

    isEdge: function(){
      return this.group() === 'edges';
    },

    isLoop: function(){
      return this.isEdge() && this.source().id() === this.target().id();
    },

    isSimple: function(){
      return this.isEdge() && this.source().id() !== this.target().id();
    },

    group: function(){
      var ele = this[0];

      if( ele ){
        return ele._private.group;
      }
    }
  });

  
})( cytoscape );

;(function($$){ 'use strict';
  
  // Functions for iterating over collections
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  $$.fn.eles({
    each: function(fn){
      if( $$.is.fn(fn) ){
        for(var i = 0; i < this.length; i++){
          var ele = this[i];
          var ret = fn.apply( ele, [ i, ele ] );

          if( ret === false ){ break; } // exit each early on return false
        }
      }
      return this;
    },

    forEach: function(fn, thisArg){
      if( $$.is.fn(fn) ){

        for(var i = 0; i < this.length; i++){
          var ele = this[i];
          var ret = fn.apply( thisArg, [ ele, i, this ] );

          if( ret === false ){ break; } // exit each early on return false
        }
      }

      return this;
    },

    toArray: function(){
      var array = [];
      
      for(var i = 0; i < this.length; i++){
        array.push( this[i] );
      }
      
      return array;
    },

    slice: function(start, end){
      var array = [];
      var thisSize = this.length;
      
      if( end == null ){
        end = thisSize;
      }

      if( start == null ){
        start = 0;
      }
      
      if( start < 0 ){
        start = thisSize + start;
      }

      if( end < 0 ){
        end = thisSize + end;
      }
      
      for(var i = start; i >= 0 && i < end && i < thisSize; i++){
        array.push( this[i] );
      }
      
      return new $$.Collection(this.cy(), array);
    },

    size: function(){
      return this.length;
    },

    eq: function(i){
      return this[i] || new $$.Collection( this.cy() );
    },

    first: function(){
      return this[0] || new $$.Collection( this.cy() );
    },

    last: function(){
      return this[ this.length - 1 ] || new $$.Collection( this.cy() );
    },

    empty: function(){
      return this.length === 0;
    },

    nonempty: function(){
      return !this.empty();
    },

    sort: function( sortFn ){
      if( !$$.is.fn( sortFn ) ){
        return this;
      }

      var cy = this.cy();      
      var sorted = this.toArray().sort( sortFn );

      return new $$.Collection(cy, sorted);
    },

    sortByZIndex: function(){
      return this.sort( $$.Collection.zIndexSort );
    },

    zDepth: function(){
      var ele = this[0];
      if( !ele ){ return undefined; }

      var _p = ele._private;
      var group = _p.group;

      if( group === 'nodes' ){
        return _p.data.parent ? ele.parents().size() : 0;
      } else {
        var src = _p.source;
        var tgt = _p.target;
        var srcDepth = src._private.data.parent ? src.parents().size() : 0;
        var tgtDepth = tgt._private.data.parent ? tgt.parents().size() : 0;

        return Math.max( srcDepth - 1, tgtDepth - 1, 0 ) + 0.5; // depth of deepest parent and just a bit above
      }
    }
  });

  $$.Collection.zIndexSort = function(a, b){
    var cy = a.cy();
    var a_p = a._private;
    var b_p = b._private;
    var zDiff = a_p.style['z-index'].value - b_p.style['z-index'].value;
    var depthA = 0;
    var depthB = 0;
    var hasCompoundNodes = cy.hasCompoundNodes();
    var aIsNode = a_p.group === 'nodes';
    var aIsEdge = a_p.group === 'edges';
    var bIsNode = b_p.group === 'nodes';
    var bIsEdge = b_p.group === 'edges';

    // no need to calculate element depth if there is no compound node
    if( hasCompoundNodes ){
      depthA = a.zDepth();
      depthB = b.zDepth();
    }

    var depthDiff = depthA - depthB;
    var sameDepth = depthDiff === 0;

    if( sameDepth ){
      
      if( aIsNode && bIsEdge ){
        return 1; // 'a' is a node, it should be drawn later       
      
      } else if( aIsEdge && bIsNode ){
        return -1; // 'a' is an edge, it should be drawn first

      } else { // both nodes or both edges
        if( zDiff === 0 ){ // same z-index => compare indices in the core (order added to graph w/ last on top)
          return a_p.index - b_p.index;
        } else {
          return zDiff;
        }
      }
    
    // elements on different level
    } else {
      return depthDiff; // deeper element should be drawn later
    }

  };
  
})( cytoscape );

;(function($$){ 'use strict';
  
  // Functions for layouts on nodes
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  $$.fn.eles({

    // using standard layout options, apply position function (w/ or w/o animation)
    layoutPositions: function( layout, options, fn ){
      var nodes = this.nodes();
      var cy = this.cy();

      layout.trigger({ type: 'layoutstart', layout: layout });

      if( options.animate ){
        for( var i = 0; i < nodes.length; i++ ){
          var node = nodes[i];
          var lastNode = i === nodes.length - 1;

          var newPos = fn.call( node, i, node );
          var pos = node.position();

          if( !$$.is.number(pos.x) || !$$.is.number(pos.y) ){
            node.silentPosition({ x: 0, y: 0 });
          }

          node.animate({
            position: newPos
          }, {
            duration: options.animationDuration,
            step: !lastNode ? undefined : function(){
              if( options.fit ){
                cy.fit( options.padding );
              } 
            },
            complete: !lastNode ? undefined : function(){
              if( options.zoom != null ){
                cy.zoom( options.zoom );
              }

              if( options.pan ){
                cy.pan( options.pan );
              } 

              if( options.fit ){
                cy.fit( options.padding );
              } 
              
              layout.one('layoutstop', options.stop);
              layout.trigger({ type: 'layoutstop', layout: layout });
            }
          });
        }

        layout.one('layoutready', options.ready);
        layout.trigger({ type: 'layoutready', layout: layout });
      } else {
        nodes.positions( fn );

        if( options.fit ){
          cy.fit( options.padding );
        }

        if( options.zoom != null ){
          cy.zoom( options.zoom );
        }

        if( options.pan ){
          cy.pan( options.pan );
        } 

        layout.one('layoutready', options.ready);
        layout.trigger({ type: 'layoutready', layout: layout });
        
        layout.one('layoutstop', options.stop);
        layout.trigger({ type: 'layoutstop', layout: layout });
      }

      return this; // chaining
    },

    layout: function( options ){
      var cy = this.cy();

      cy.layout( $$.util.extend({}, options, {
        eles: this
      }) );

      return this;
    },

    makeLayout: function( options ){
      var cy = this.cy();

      return cy.makeLayout( $$.util.extend({}, options, {
        eles: this
      }) );
    }

  });
  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.eles({

    // fully updates (recalculates) the style for the elements
    updateStyle: function( notifyRenderer ){
      var cy = this._private.cy;

      if( !cy.styleEnabled() ){ return this; }

      if( cy._private.batchingStyle ){
        var bEles = cy._private.batchStyleEles;

        for( var i = 0; i < this.length; i++ ){
          var ele = this[i];

          if( !bEles.ids[ ele._private.id ] ){
            bEles.push( ele );
          }
        }

        return this; // chaining and exit early when batching
      }

      var style = cy.style();
      notifyRenderer = notifyRenderer || notifyRenderer === undefined ? true : false;

      style.apply( this );

      var updatedCompounds = this.updateCompoundBounds();
      var toNotify = updatedCompounds.length > 0 ? this.add( updatedCompounds ) : this;

      if( notifyRenderer ){
        toNotify.rtrigger('style'); // let renderer know we changed style
      } else {
        toNotify.trigger('style'); // just fire the event
      }
      return this; // chaining
    },

    // just update the mappers in the elements' styles; cheaper than eles.updateStyle()
    updateMappers: function( notifyRenderer ){
      var cy = this._private.cy;
      var style = cy.style();
      notifyRenderer = notifyRenderer || notifyRenderer === undefined ? true : false;

      if( !cy.styleEnabled() ){ return this; }

      style.updateMappers( this );

      var updatedCompounds = this.updateCompoundBounds();
      var toNotify = updatedCompounds.length > 0 ? this.add( updatedCompounds ) : this;

      if( notifyRenderer ){
        toNotify.rtrigger('style'); // let renderer know we changed style
      } else {
        toNotify.trigger('style'); // just fire the event
      }
      return this; // chaining
    },

    // get the specified css property as a rendered value (i.e. on-screen value)
    // or get the whole rendered style if no property specified (NB doesn't allow setting)
    renderedCss: function( property ){
      var cy = this.cy();
      if( !cy.styleEnabled() ){ return this; }

      var ele = this[0];

      if( ele ){
        var renstyle = ele.cy().style().getRenderedStyle( ele );

        if( property === undefined ){
          return renstyle;
        } else {
          return renstyle[ property ];
        }
      }
    },

    // read the calculated css style of the element or override the style (via a bypass)
    css: function( name, value ){
      var cy = this.cy();
      
      if( !cy.styleEnabled() ){ return this; }

      var updateTransitions = false;
      var style = cy.style();

      if( $$.is.plainObject(name) ){ // then extend the bypass
        var props = name;
        style.applyBypass( this, props, updateTransitions );

        var updatedCompounds = this.updateCompoundBounds();
        var toNotify = updatedCompounds.length > 0 ? this.add( updatedCompounds ) : this;
        toNotify.rtrigger('style'); // let the renderer know we've updated style

      } else if( $$.is.string(name) ){
  
        if( value === undefined ){ // then get the property from the style
          var ele = this[0];

          if( ele ){
            return ele._private.style[ name ].strValue;
          } else { // empty collection => can't get any value
            return;
          }

        } else { // then set the bypass with the property value
          style.applyBypass( this, name, value, updateTransitions );

          var updatedCompounds = this.updateCompoundBounds();
          var toNotify = updatedCompounds.length > 0 ? this.add( updatedCompounds ) : this;
          toNotify.rtrigger('style'); // let the renderer know we've updated style
        }

      } else if( name === undefined ){
        var ele = this[0];

        if( ele ){
          return style.getRawStyle( ele );
        } else { // empty collection => can't get any value
          return;
        }
      }

      return this; // chaining
    },

    removeCss: function( names ){
      var cy = this.cy();
      
      if( !cy.styleEnabled() ){ return this; }

      var updateTransitions = false;
      var style = cy.style();
      var eles = this;

      if( names === undefined ){
        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];

          style.removeAllBypasses( ele, updateTransitions );
        }
      } else {
        names = names.split(/\s+/);

        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];

          style.removeBypasses( ele, names, updateTransitions );
        }
      }

      var updatedCompounds = this.updateCompoundBounds();
      var toNotify = updatedCompounds.length > 0 ? this.add( updatedCompounds ) : this;
      toNotify.rtrigger('style'); // let the renderer know we've updated style

      return this; // chaining
    },

    show: function(){
      this.css('display', 'element');
      return this; // chaining
    },

    hide: function(){
      this.css('display', 'none');
      return this; // chaining
    },

    visible: function(){
      var cy = this.cy();
      if( !cy.styleEnabled() ){ return true; }

      var ele = this[0];
      var hasCompoundNodes = cy.hasCompoundNodes();

      if( ele ){
        var style = ele._private.style;

        if(
          style['visibility'].value !== 'visible'
          || style['display'].value !== 'element'
        ){
          return false;
        }
        
        if( ele._private.group === 'nodes' ){
          if( !hasCompoundNodes ){ return true; }

          var parents = ele._private.data.parent ? ele.parents() : null;

          if( parents ){
            for( var i = 0; i < parents.length; i++ ){
              var parent = parents[i];
              var pStyle = parent._private.style;
              var pVis = pStyle['visibility'].value;
              var pDis = pStyle['display'].value;

              if( pVis !== 'visible' || pDis !== 'element' ){
                return false;
              }
            }
          }

          return true;
        } else {
          var src = ele._private.source;
          var tgt = ele._private.target;

          return src.visible() && tgt.visible();
        }

      }
    },

    hidden: function(){
      var ele = this[0];

      if( ele ){
        return !ele.visible();
      }
    },

    effectiveOpacity: function(){
      var cy = this.cy();
      if( !cy.styleEnabled() ){ return 1; }

      var hasCompoundNodes = cy.hasCompoundNodes();
      var ele = this[0];

      if( ele ){
        var _p = ele._private;
        var parentOpacity = _p.style.opacity.value;

        if( !hasCompoundNodes ){ return parentOpacity; }

        var parents = !_p.data.parent ? null : ele.parents();
        
        if( parents ){
          for( var i = 0; i < parents.length; i++ ){
            var parent = parents[i];
            var opacity = parent._private.style.opacity.value;

            parentOpacity = opacity * parentOpacity;
          }
        }

        return parentOpacity;
      }
    },

    transparent: function(){
      var ele = this[0];
      var hasCompoundNodes = ele.cy().hasCompoundNodes();

      if( ele ){
        if( !hasCompoundNodes ){
          return ele._private.style.opacity.value === 0;
        } else {
          return ele.effectiveOpacity() === 0;
        }
      }
    },

    isFullAutoParent: function(){
      var cy = this.cy();
      if( !cy.styleEnabled() ){ return false; }

      var ele = this[0];

      if( ele ){
        var autoW = ele._private.style['width'].value === 'auto';
        var autoH = ele._private.style['height'].value === 'auto';

        return ele.isParent() && autoW && autoH;
      }
    }

  });


  $$.elesfn.style = $$.elesfn.css;
  $$.elesfn.renderedStyle = $$.elesfn.renderedCss;
  $$.elesfn.removeStyle = $$.elesfn.removeCss;
  
})( cytoscape );
;(function($$){ 'use strict';
  
  // Collection functions that toggle a boolean value
  ////////////////////////////////////////////////////////////////////////////////////////////////////
  
  
  function defineSwitchFunction(params){
    return function(){
      var args = arguments;
      var changedEles = [];
      
      // e.g. cy.nodes().select( data, handler )
      if( args.length === 2 ){
        var data = args[0];
        var handler = args[1];
        this.bind( params.event, data, handler );
      } 
      
      // e.g. cy.nodes().select( handler )
      else if( args.length === 1 ){
        var handler = args[0];
        this.bind( params.event, handler );
      }
      
      // e.g. cy.nodes().select()
      else if( args.length === 0 ){
        for( var i = 0; i < this.length; i++ ){
          var ele = this[i];
          var able = !params.ableField || ele._private[params.ableField];
          var changed = ele._private[params.field] != params.value;

          if( params.overrideAble ){
            var overrideAble = params.overrideAble(ele);

            if( overrideAble !== undefined ){
              able = overrideAble;

              if( !overrideAble ){ return this; } // to save cycles assume not able for all on override
            }
          }

          if( able ){
            ele._private[params.field] = params.value;

            if( changed ){
              changedEles.push( ele );
            }
          }
        }

        var changedColl = $$.Collection( this.cy(), changedEles );
        changedColl.updateStyle(); // change of state => possible change of style
        changedColl.trigger( params.event );
      }

      return this;
    };
  }
  
  function defineSwitchSet( params ){
    $$.elesfn[ params.field ] = function(){
      var ele = this[0];

      if( ele ){
        if( params.overrideField ){
          var val = params.overrideField(ele);

          if( val !== undefined ){
            return val;
          }
        }

        return ele._private[ params.field ];
      }
    };
    
    $$.elesfn[ params.on ] = defineSwitchFunction({
      event: params.on,
      field: params.field,
      ableField: params.ableField,
      overrideAble: params.overrideAble,
      value: true
    });

    $$.elesfn[ params.off ] = defineSwitchFunction({
      event: params.off,
      field: params.field,
      ableField: params.ableField,
      overrideAble: params.overrideAble,
      value: false
    });
  }
  
  defineSwitchSet({
    field: 'locked',
    overrideField: function(ele){
      return ele.cy().autolock() ? true : undefined;
    },
    on: 'lock',
    off: 'unlock'
  });
  
  defineSwitchSet({
    field: 'grabbable',
    overrideField: function(ele){
      return ele.cy().autoungrabify() ? false : undefined;
    },
    on: 'grabify',
    off: 'ungrabify'
  });
  
  defineSwitchSet({
    field: 'selected',
    ableField: 'selectable',
    overrideAble: function(ele){
      return ele.cy().autounselectify() ? false : undefined;
    },
    on: 'select',
    off: 'unselect'
  });
  
  defineSwitchSet({
    field: 'selectable',
    overrideField: function(ele){
      return ele.cy().autounselectify() ? false : undefined;
    },
    on: 'selectify',
    off: 'unselectify'
  });
  
  $$.elesfn.grabbed = function(){
    var ele = this[0];
    if( ele ){
      return ele._private.grabbed;
    }
  };

  defineSwitchSet({
    field: 'active',
    on: 'activate',
    off: 'unactivate'
  });

  $$.elesfn.inactive = function(){
    var ele = this[0];
    if( ele ){
      return !ele._private.active;
    }
  };
  
})( cytoscape );

;(function($$){ 'use strict';

  // DAG functions
  //////////////////////////

  $$.fn.eles({
    // get the root nodes in the DAG
    roots: function( selector ){
      var eles = this;
      var roots = [];

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        if( !ele.isNode() ){
          continue;
        }

        var hasEdgesPointingIn = ele.connectedEdges(function(){
          return this.data('target') === ele.id() && this.data('source') !== ele.id();
        }).length > 0;

        if( !hasEdgesPointingIn ){
          roots.push( ele );
        }
      }

      return new $$.Collection( this._private.cy, roots, { unique: true } ).filter( selector );
    },

    // get the leaf nodes in the DAG
    leaves: function( selector ){
      var eles = this;
      var leaves = [];

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        if( !ele.isNode() ){
          continue;
        }

        var hasEdgesPointingOut = ele.connectedEdges(function(){
          return this.data('source') === ele.id() && this.data('target') !== ele.id();
        }).length > 0;

        if( !hasEdgesPointingOut ){
          leaves.push( ele );
        }
      }

      return new $$.Collection( this._private.cy, leaves, { unique: true } ).filter( selector );
    },

    // normally called children in graph theory
    // these nodes =edges=> outgoing nodes
    outgoers: function( selector ){
      var eles = this;
      var oEles = [];

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var eleId = ele.id();

        if( !ele.isNode() ){ continue; }

        var edges = ele._private.edges;
        for( var j = 0; j < edges.length; j++ ){
          var edge = edges[j];
          var srcId = edge._private.data.source;
          var tgtId = edge._private.data.target;

          if( srcId === eleId && tgtId !== eleId ){
            oEles.push( edge );
            oEles.push( edge.target()[0] );
          }
        }
      }

      return new $$.Collection( this._private.cy, oEles, { unique: true } ).filter( selector );
    },

    // aka DAG descendants
    successors: function( selector ){
      var eles = this;
      var sEles = [];
      var sElesIds = {};

      for(;;){
        var outgoers = eles.outgoers();

        if( outgoers.length === 0 ){ break; } // done if no outgoers left

        var newOutgoers = false;
        for( var i = 0; i < outgoers.length; i++ ){
          var outgoer = outgoers[i];
          var outgoerId = outgoer.id();

          if( !sElesIds[ outgoerId ] ){
            sElesIds[ outgoerId ] = true;
            sEles.push( outgoer );
            newOutgoers = true;
          }
        }

        if( !newOutgoers ){ break; } // done if touched all outgoers already

        eles = outgoers;
      }

      return new $$.Collection( this._private.cy, sEles, { unique: true } ).filter( selector );
    },

    // normally called parents in graph theory
    // these nodes <=edges= incoming nodes
    incomers: function( selector ){
      var eles = this;
      var oEles = [];

      for( var i = 0; i < eles.length; i++ ){
        var ele = eles[i];
        var eleId = ele.id();

        if( !ele.isNode() ){ continue; }

        var edges = ele._private.edges;
        for( var j = 0; j < edges.length; j++ ){
          var edge = edges[j];
          var srcId = edge._private.data.source;
          var tgtId = edge._private.data.target;

          if( tgtId === eleId && srcId !== eleId ){
            oEles.push( edge );
            oEles.push( edge.source()[0] );
          }
        }
      }

      return new $$.Collection( this._private.cy, oEles, { unique: true } ).filter( selector );
    },

    // aka DAG ancestors
    predecessors: function( selector ){
      var eles = this;
      var pEles = [];
      var pElesIds = {};

      for(;;){
        var incomers = eles.incomers();

        if( incomers.length === 0 ){ break; } // done if no incomers left

        var newIncomers = false;
        for( var i = 0; i < incomers.length; i++ ){
          var incomer = incomers[i];
          var incomerId = incomer.id();

          if( !pElesIds[ incomerId ] ){
            pElesIds[ incomerId ] = true;
            pEles.push( incomer );
            newIncomers = true;
          }
        }

        if( !newIncomers ){ break; } // done if touched all incomers already

        eles = incomers;
      }

      return new $$.Collection( this._private.cy, pEles, { unique: true } ).filter( selector );
    }
  });


  // Neighbourhood functions
  //////////////////////////

  $$.fn.eles({
    neighborhood: function(selector){
      var elements = [];
      var cy = this._private.cy;
      var nodes = this.nodes();

      for( var i = 0; i < nodes.length; i++ ){ // for all nodes
        var node = nodes[i];
        var connectedEdges = node.connectedEdges();

        // for each connected edge, add the edge and the other node
        for( var j = 0; j < connectedEdges.length; j++ ){
          var edge = connectedEdges[j];
          var otherNode = edge.connectedNodes().not(node);

          // need check in case of loop
          if( otherNode.length > 0 ){
            elements.push( otherNode[0] ); // add node 1 hop away
          }
          
          // add connected edge
          elements.push( edge[0] );
        }

      }
      
      return ( new $$.Collection( cy, elements, { unique: true } ) ).filter( selector );
    },

    closedNeighborhood: function(selector){
      return this.neighborhood().add( this ).filter( selector );
    },

    openNeighborhood: function(selector){
      return this.neighborhood( selector );
    }
  });  


  // Edge functions
  /////////////////

  $$.fn.eles({
    source: function( selector ){
      var ele = this[0];
      var src;

      if( ele ){
        src = ele._private.source;
      }

      return src && selector ? src.filter( selector ) : src;
    },

    target: function( selector ){
      var ele = this[0];
      var tgt;

      if( ele ){
        tgt = ele._private.target;
      }

      return tgt && selector ? tgt.filter( selector ) : tgt;
    },

    sources: defineSourceFunction({
      attr: 'source'
    }),

    targets: defineSourceFunction({
      attr: 'target'
    })
  });
  
  function defineSourceFunction( params ){
    return function( selector ){
      var sources = [];
      var cy = this._private.cy;

      for( var i = 0; i < this.length; i++ ){
        var ele = this[i];
        var src = ele._private[ params.attr ];

        if( src ){
          sources.push( src );
        }
      }
      
      return new $$.Collection( cy, sources, { unique: true } ).filter( selector );
    };
  }

  $$.fn.eles({
    edgesWith: defineEdgesWithFunction(),

    edgesTo: defineEdgesWithFunction({
      thisIs: 'source'
    })
  });
  
  function defineEdgesWithFunction( params ){
    
    return function(otherNodes){
      var elements = [];
      var cy = this._private.cy;
      var p = params || {};

      // get elements if a selector is specified
      if( $$.is.string(otherNodes) ){
        otherNodes = cy.$( otherNodes );
      }
      
      var edges = otherNodes.connectedEdges();
      var thisIds = this._private.ids;
      
      for( var i = 0; i < edges.length; i++ ){
        var edge = edges[i];
        var foundId;
        var edgeData = edge._private.data;

        if( p.thisIs ){
          var idToFind = edgeData[ p.thisIs ];
          foundId = thisIds[ idToFind ];
        } else {
          foundId = thisIds[ edgeData.source ] || thisIds[ edgeData.target ];
        }
        
        if( foundId ){
          elements.push( edge );
        }
      }
      
      return new $$.Collection( cy, elements, { unique: true } );
    };
  }
  
  $$.fn.eles({
    connectedEdges: function( selector ){
      var retEles = [];
      var cy = this._private.cy;
      
      var eles = this;
      for( var i = 0; i < eles.length; i++ ){
        var node = eles[i];
        if( !node.isNode() ){ continue; }

        var edges = node._private.edges;

        for( var j = 0; j < edges.length; j++ ){
          var edge = edges[j];          
          retEles.push( edge );
        }
      }
      
      return new $$.Collection( cy, retEles, { unique: true } ).filter( selector );
    },

    connectedNodes: function( selector ){
      var retEles = [];
      var cy = this._private.cy;

      var eles = this;
      for( var i = 0; i < eles.length; i++ ){
        var edge = eles[i];
        if( !edge.isEdge() ){ continue; }

        retEles.push( edge.source()[0] );
        retEles.push( edge.target()[0] );
      }

      return new $$.Collection( cy, retEles, { unique: true } ).filter( selector );
    },

    parallelEdges: defineParallelEdgesFunction(),

    codirectedEdges: defineParallelEdgesFunction({
      codirected: true
    })
  });
  
  function defineParallelEdgesFunction(params){
    var defaults = {
      codirected: false
    };
    params = $$.util.extend({}, defaults, params);
    
    return function( selector ){
      var cy = this._private.cy;
      var elements = [];
      var edges = this.edges();
      var p = params;

      // look at all the edges in the collection
      for( var i = 0; i < edges.length; i++ ){
        var edge1 = edges[i];
        var src1 = edge1.source()[0];
        var srcid1 = src1.id();
        var tgt1 = edge1.target()[0];
        var tgtid1 = tgt1.id();
        var srcEdges1 = src1._private.edges;

        // look at edges connected to the src node of this edge
        for( var j = 0; j < srcEdges1.length; j++ ){
          var edge2 = srcEdges1[j];
          var edge2data = edge2._private.data;
          var tgtid2 = edge2data.target;
          var srcid2 = edge2data.source;

          var codirected = tgtid2 === tgtid1 && srcid2 === srcid1;
          var oppdirected = srcid1 === tgtid2 && tgtid1 === srcid2;
          
          if( (p.codirected && codirected) || (!p.codirected && (codirected || oppdirected)) ){
            elements.push( edge2 );
          }
        }
      }
      
      return new $$.Collection( cy, elements, { unique: true } ).filter( selector );
    };
  
  }

  
})( cytoscape );

;(function($$){ 'use strict';

  $$.fn.eles({

    fit: function(){},
    center: function(){}

  });
  
})( cytoscape );
;(function ($$) {
  "use strict";

  /*  Min and Max heap predefaults */
  
  $$.Minheap = function (cy, eles, valueFn) {
    return new $$.Heap(cy, eles, $$.Heap.minHeapComparator, valueFn);
  };

  $$.Maxheap = function (cy, eles, valueFn) {
    return new $$.Heap(cy, eles, $$.Heap.maxHeapComparator, valueFn);
  };
  
  $$.Heap = function (cy, eles, comparator, valueFn) {
    if (typeof comparator === "undefined" || typeof eles === "undefined") {
      return;
    }
    
    if (typeof valueFn === "undefined") {
      valueFn = $$.Heap.idFn;
    }

    var sourceHeap = [],
      pointers = {},
      elements = [],
      i = 0,
      id,
      heap,
      elesLen;

    eles = this.getArgumentAsCollection(eles, cy);
    elesLen = eles.length;

    for (i = 0; i < elesLen; i += 1) {
      sourceHeap.push(valueFn.call(cy, eles[i], i, eles));

      id = eles[i].id();
      
      if (pointers.hasOwnProperty(id)) {
        throw "ERROR: Multiple items with the same id found: " + id;
      }
      
      pointers[id] = i;
      elements.push(id);
    }

    this._private = {
      cy: cy,
      heap: sourceHeap,
      pointers: pointers,
      elements: elements,
      comparator: comparator,
      extractor: valueFn,
      length: elesLen
    };

    for (i = Math.floor(elesLen / 2); i >= 0; i -= 1) {
      heap = this.heapify(i);
    }

    return heap;
  };

  /* static methods */
  $$.Heap.idFn = function (node) {
    return node.id();
  };

  $$.Heap.minHeapComparator = function (a, b) {
    return a >= b;
  };

  $$.Heap.maxHeapComparator = function (a, b) {
    return a <= b;
  };

  $$.fn.heap = function( fnMap, options ){
    for( var name in fnMap ){
      var fn = fnMap[name];
      $$.Heap.prototype[ name ] = fn;
    }
  };

  $$.heapfn = $$.Heap.prototype; // short alias

  /* object methods */
  $$.heapfn.size = function () {
    return this._private.length;
  };

  $$.heapfn.getArgumentAsCollection = function (eles, cy) {
    var result;
    if(typeof cy === "undefined") {
      cy = this._private.cy;
    }

    if ($$.is.elementOrCollection(eles)) {
      result = eles;

    } else {
      var resultArray = [],
        sourceEles = [].concat.apply([], [eles]);

      for (var i = 0; i < sourceEles.length; i++) {
        var id = sourceEles[i],
          ele = cy.getElementById(id);

        if(ele.length > 0) {
          resultArray.push(ele);
        }
      }

      result = new $$.Collection(cy, resultArray);
    }

    return result;
  };

  $$.heapfn.isHeap = function () {
    var array = this._private.heap,
      arrlen = array.length,
      i,
      left,
      right,
      lCheck,
      rCheck,
      comparator = this._private.comparator;

    for (i = 0; i < arrlen; i += 1) {
      left = 2 * i + 1;
      right = left + 1;
      lCheck = left < arrlen ? comparator(array[left], array[i]) : true;
      rCheck = right < arrlen ? comparator(array[right], array[i]) : true;

      if (!lCheck || !rCheck) {
        return false;
      }
    }

    return true;
  };

  $$.heapfn.heapSwap = function (i, j) {
    var heap = this._private.heap,
      pointers = this._private.pointers,
      elements = this._private.elements,
      swapValue = heap[i],
      swapElems = elements[i],
      idI = elements[i],
      idJ = elements[j];

    heap[i] = heap[j];
    elements[i] = elements[j];

    pointers[idI] = j;
    pointers[idJ] = i;

    heap[j] = swapValue;
    elements[j] = swapElems;
  };

  $$.heapfn.heapify = function (i, rootToLeaf) {
    var treeLen = 0,
      condHeap = false,
      array,
      current,
      left,
      right,
      best,
      comparator,
      parent;
    
    if (typeof rootToLeaf === "undefined") {
      rootToLeaf = true;
    }

    array = this._private.heap;
    treeLen = array.length;
    comparator = this._private.comparator;
    current = i;

    while (!condHeap) {

      if (rootToLeaf) {
        left = 2 * current + 1;
        right = left + 1;
        best = current;
        
        if (left < treeLen && !comparator(array[left], array[best])) {
          best = left;
        }
        
        if (right < treeLen && !comparator(array[right], array[best])) {
          best = right;
        }
        
        condHeap = best === current;
        
        if (!condHeap) {
          this.heapSwap(best, current);
          current = best;
        }

      } else {
        parent = Math.floor((current - 1) / 2);
        best = current;
        condHeap = parent < 0 || comparator(array[best], array[parent]);

        if (!condHeap) {
          this.heapSwap(best, parent);
          current = parent;
        }
      }

    } // while
  };

  /* collectionOrElement */
  $$.heapfn.insert = function (eles) {
    var elements = this.getArgumentAsCollection(eles),
      elsize = elements.length,
      element,
      elindex,
      elvalue,
      elid,
      i;

    for (i = 0; i < elsize; i += 1) {
      element = elements[i];
      elindex = this._private.heap.length;
      elvalue = this._private.extractor(element);
      elid = element.id();

      if (this._private.pointers.hasOwnProperty(elid)) {
        throw "ERROR: Multiple items with the same id found: " + elid;
      }

      this._private.heap.push(elvalue);
      this._private.elements.push(elid);
      this._private.pointers[elid] = elindex;
      this.heapify(elindex, false);
    }

    this._private.length = this._private.heap.length;
  };

  $$.heapfn.getValueById = function (elementId) {
    if (this._private.pointers.hasOwnProperty(elementId)) {
      var elementIndex = this._private.pointers[elementId];

      return this._private.heap[elementIndex];
    }
  };
  
  $$.heapfn.contains = function (eles) {
    var elements = this.getArgumentAsCollection(eles);

    for (var i = 0; i < elements.length; i += 1) {
      var elementId = elements[i].id();

      if(!this._private.pointers.hasOwnProperty(elementId)) {
        return false;
      }
    }

    return true;
  };
  
  $$.heapfn.top = function () {
    if (this._private.length > 0) {

      return {
        value: this._private.heap[0],
        id: this._private.elements[0]
      };

    }
  };

  $$.heapfn.pop = function () {
    if (this._private.length > 0) {
      var top = this.top(),
        lastIndex = this._private.length - 1,
        removeCandidate,
        removeValue,
        remId;

      this.heapSwap(0, lastIndex);

      removeCandidate = this._private.elements[lastIndex];
      removeValue = this._private.heap[lastIndex];
      remId = removeCandidate;

      this._private.heap.pop();
      this._private.elements.pop();
      this._private.length = this._private.heap.length;
      this._private.pointers[remId] = undefined;

      this.heapify(0);
      return top;
    }
  };

  $$.heapfn.findDirectionHeapify = function (index) {
    var parent = Math.floor((index - 1) / 2),
      array = this._private.heap,
      condHeap = parent < 0 || this._private.comparator(array[index], array[parent]);

    this.heapify(index, condHeap);
  };

  /* edit is a new value or function */
  // only values in heap are updated. elements themselves are not!
  $$.heapfn.edit = function (eles, edit) {
    var elements = this.getArgumentAsCollection(eles);
    
    for (var i = 0; i < elements.length; i += 1) {
      var elementId = elements[i].id(),
        elementIndex = this._private.pointers[elementId],
        elementValue = this._private.heap[elementIndex];
      
      if ($$.is.number(edit)) {
        this._private.heap[elementIndex] = edit;
        
      } else if ($$.is.fn(edit)) {
        this._private.heap[elementIndex] = edit.call(this._private.cy, elementValue, elementIndex);
      }

      this.findDirectionHeapify(elementIndex);
    }
  };

  $$.heapfn.delete = function (eles) {
    var elements = this.getArgumentAsCollection(eles);
    
    for (var i = 0; i < elements.length; i += 1) {
      var elementId = elements[i].id(),
        elementIndex = this._private.pointers[elementId],
        lastIndex = this._private.length - 1,
        removeCandidate,
        removeValue,
        remId;

      if (elementIndex !== lastIndex) {
        this.heapSwap(elementIndex, lastIndex);
      }

      removeCandidate = this._private.elements[lastIndex];
      removeValue = this._private.heap[lastIndex];
      remId = removeCandidate;

      this._private.heap.pop();
      this._private.elements.pop();
      this._private.length = this._private.heap.length;
      this._private.pointers[remId] = undefined;

      this.findDirectionHeapify(elementIndex);
    }

    return removeValue;
  };

})(cytoscape);
/*
  The canvas renderer was written by Yue Dong.

  Modifications tracked on Github.
*/

(function($$) { 'use strict';

  function CanvasRenderer(options) {
    
    CanvasRenderer.CANVAS_LAYERS = 5;
    CanvasRenderer.SELECT_BOX = 0;
    CanvasRenderer.DRAG = 2;
    CanvasRenderer.NODE = 4;
    CanvasRenderer.TEXTURE_BUFFER = 0;
    CanvasRenderer.BUFFER_COUNT = 2;

    this.options = options;

    this.data = {
        
      select: [undefined, undefined, undefined, undefined, 0], // Coordinates for selection box, plus enabled flag 
      renderer: this, cy: options.cy, container: options.cy.container(),
      
      canvases: new Array(CanvasRenderer.CANVAS_LAYERS),
      contexts: new Array(CanvasRenderer.CANVAS_LAYERS),
      canvasNeedsRedraw: new Array(CanvasRenderer.CANVAS_LAYERS),
      
      bufferCanvases: new Array(CanvasRenderer.BUFFER_COUNT),
      bufferContexts: new Array(CanvasRenderer.CANVAS_LAYERS)

    };
    
    //--Pointer-related data
    this.hoverData = {down: null, last: null, 
        downTime: null, triggerMode: null, 
        dragging: false, 
        initialPan: [null, null], capture: false};
    
    this.timeoutData = {panTimeout: null};
    
    this.dragData = {possibleDragElements: []};
    
    this.touchData = {start: null, capture: false,
        // These 3 fields related to tap, taphold events
        startPosition: [null, null, null, null, null, null],
        singleTouchStartTime: null,
        singleTouchMoved: true,
        
        
        now: [null, null, null, null, null, null], 
        earlier: [null, null, null, null, null, null] };
    //--
    
    //--Wheel-related data 
    this.zoomData = {freeToZoom: false, lastPointerX: null};
    //--
    
    this.redraws = 0;
    this.showFps = options.showFps;

    this.bindings = [];
    
    this.data.canvasContainer = document.createElement('div');
    var containerStyle = this.data.canvasContainer.style;
    containerStyle.position = 'absolute';
    containerStyle.zIndex = '0';
    containerStyle.overflow = 'hidden';

    this.data.container.appendChild( this.data.canvasContainer );

    for (var i = 0; i < CanvasRenderer.CANVAS_LAYERS; i++) {
      this.data.canvases[i] = document.createElement('canvas');
      this.data.contexts[i] = this.data.canvases[i].getContext('2d');
      this.data.canvases[i].style.position = 'absolute';
      this.data.canvases[i].setAttribute('data-id', 'layer' + i);
      this.data.canvases[i].style.zIndex = String(CanvasRenderer.CANVAS_LAYERS - i);
      this.data.canvasContainer.appendChild(this.data.canvases[i]);
      
      this.data.canvasNeedsRedraw[i] = false;
    }
    this.data.topCanvas = this.data.canvases[0];

    this.data.canvases[CanvasRenderer.NODE].setAttribute('data-id', 'layer' + CanvasRenderer.NODE + '-node');
    this.data.canvases[CanvasRenderer.SELECT_BOX].setAttribute('data-id', 'layer' + CanvasRenderer.SELECT_BOX + '-selectbox');
    this.data.canvases[CanvasRenderer.DRAG].setAttribute('data-id', 'layer' + CanvasRenderer.DRAG + '-drag');
    
    for (var i = 0; i < CanvasRenderer.BUFFER_COUNT; i++) {
      this.data.bufferCanvases[i] = document.createElement('canvas');
      this.data.bufferContexts[i] = this.data.bufferCanvases[i].getContext('2d');
      this.data.bufferCanvases[i].style.position = 'absolute';
      this.data.bufferCanvases[i].setAttribute('data-id', 'buffer' + i);
      this.data.bufferCanvases[i].style.zIndex = String(-i - 1);
      this.data.bufferCanvases[i].style.visibility = 'hidden';
      //this.data.canvasContainer.appendChild(this.data.bufferCanvases[i]);
    }

    this.hideEdgesOnViewport = options.hideEdgesOnViewport;
    this.hideLabelsOnViewport = options.hideLabelsOnViewport;
    this.textureOnViewport = options.textureOnViewport;
    this.wheelSensitivity = options.wheelSensitivity;
    this.motionBlurEnabled = options.motionBlur === undefined ? true : options.motionBlur; // on by default
    this.forcedPixelRatio = options.pixelRatio;
    this.motionBlur = true; // for initial kick off
    this.tapThreshold = options.tapThreshold;
    this.tapThreshold2 = options.tapThreshold * options.tapThreshold;
    this.tapholdDuration = 500;

    this.load();
  }

  CanvasRenderer.panOrBoxSelectDelay = 400;
  CanvasRenderer.isTouch = $$.is.touch();

  // whether to use Path2D caching for drawing
  var pathsImpld = typeof Path2D !== 'undefined';
  CanvasRenderer.usePaths = function(){
    return pathsImpld;
  };

  CanvasRenderer.prototype.notify = function(params) {
    var types;

    if( $$.is.array( params.type ) ){
      types = params.type;

    } else {
      types = [ params.type ];
    }

    for( var i = 0; i < types.length; i++ ){
      var type = types[i];

      switch( type ){
        case 'destroy':
          this.destroy();
          return;

        case 'add':
        case 'remove':
        case 'load':
          this.updateNodesCache();
          this.updateEdgesCache();
          break;

        case 'viewport':
          this.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
          break;

        case 'style':
          this.updateCachedZSortedEles();
          break;
      }

      if( type === 'load' || type === 'resize' ){
        this.invalidateContainerClientCoordsCache();
        this.matchCanvasSize(this.data.container);
      }
    } // for
    
    this.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
    this.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

    this.redraw();
  };

  CanvasRenderer.prototype.destroy = function(){
    this.destroyed = true;

    for( var i = 0; i < this.bindings.length; i++ ){
      var binding = this.bindings[i];
      var b = binding;

      b.target.removeEventListener(b.event, b.handler, b.useCapture);
    }

    if( this.removeObserver ){
      this.removeObserver.disconnect();
    }

    if( this.labelCalcDiv ){
      document.body.removeChild(this.labelCalcDiv);
    }
  };

  

  // copy the math functions into the renderer prototype
  // unfortunately these functions are used interspersed t/o the code
  // and this makes sure things work just in case a ref was missed in refactoring
  // TODO remove this eventually
  for( var fnName in $$.math ){
    CanvasRenderer.prototype[ fnName ] = $$.math[ fnName ];
  }
  
  
  $$('renderer', 'canvas', CanvasRenderer);
  
})( cytoscape );

;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');
  var rendFunc = CanvasRenderer.prototype;
  var arrowShapes = CanvasRenderer.arrowShapes = {};

  CanvasRenderer.arrowShapeHeight = 0.3;

  // Contract for arrow shapes:
  // 0, 0 is arrow tip
  // (0, 1) is direction towards node
  // (1, 0) is right
  //
  // functional api:
  // collide: check x, y in shape
  // roughCollide: called before collide, no false negatives
  // draw: draw
  // spacing: dist(arrowTip, nodeBoundary)
  // gap: dist(edgeTip, nodeBoundary), edgeTip may != arrowTip

  var bbCollide = function(x, y, centerX, centerY, width, height, direction, padding){
    var x1 = centerX - width/2;
    var x2 = centerX + width/2;
    var y1 = centerY - height/2;
    var y2 = centerY + height/2;

    return (x1 <= x && x <= x2) && (y1 <= y && y <= y2);
  };

  var transform = function(x, y, size, angle, translation){
    angle = -angle; // b/c of notation used in arrow draw fn

    var xRotated = x * Math.cos(angle) - y * Math.sin(angle);
    var yRotated = x * Math.sin(angle) + y * Math.cos(angle);
    
    var xScaled = xRotated * size;
    var yScaled = yRotated * size;

    var xTranslated = xScaled + translation.x;
    var yTranslated = yScaled + translation.y;
    
    return {
      x: xTranslated,
      y: yTranslated
    };
  };

  arrowShapes['arrow'] = {
    _points: [
      -0.15, -0.3,
      0, 0,
      0.15, -0.3
    ],
    
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = arrowShapes['arrow']._points;
      
//      console.log("collide(): " + direction);
      
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var points = arrowShapes['arrow']._points;
    
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        context.lineTo(pt.x, pt.y);
      }

    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };

  arrowShapes['triangle'] = arrowShapes['arrow'];
  
  arrowShapes['triangle-backcurve'] = {
    _ctrlPt: [ 0, -0.15 ],

    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = arrowShapes['triangle']._points;
      
//      console.log("collide(): " + direction);
      
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var points = arrowShapes['triangle']._points;
      var firstPt;
    
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        if( i === 0 ){
          firstPt = pt;
        }

        context.lineTo(pt.x, pt.y);
      }

      var ctrlPt = this._ctrlPt;
      var ctrlPtTrans = transform( ctrlPt[0], ctrlPt[1], size, angle, translation );

      context.quadraticCurveTo( ctrlPtTrans.x, ctrlPtTrans.y, firstPt.x, firstPt.y );
    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };
  

  arrowShapes['triangle-tee'] = {
    _points: [
      -0.15, -0.3,
      0, 0,
      0.15, -0.3,
      -0.15, -0.3
    ],

    _pointsTee: [
      -0.15, -0.4,
      -0.15, -0.5,
      0.15, -0.5,
      0.15, -0.4
    ],
    
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var triPts = arrowShapes['triangle-tee']._points;
      var teePts = arrowShapes['triangle-tee']._pointsTee;
      
      var inside = $$.math.pointInsidePolygon(x, y, teePts, centerX, centerY, width, height, direction, padding) 
        || $$.math.pointInsidePolygon(x, y, triPts, centerX, centerY, width, height, direction, padding);

      return inside;
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var triPts = arrowShapes['triangle-tee']._points;
      for (var i = 0; i < triPts.length / 2; i++){
        var pt = transform( triPts[ i * 2 ],  triPts[ i * 2 + 1 ], size, angle, translation );
        
        context.lineTo( pt.x, pt.y );
      }

      var teePts = arrowShapes['triangle-tee']._pointsTee;
      var firstTeePt = transform( teePts[0], teePts[1], size, angle, translation );
      context.moveTo( firstTeePt.x, firstTeePt.y );

      for (var i = 0; i < teePts.length / 2; i++){
        var pt = transform( teePts[ i * 2 ],  teePts[ i * 2 + 1 ], size, angle, translation );
        
        context.lineTo( pt.x, pt.y );
      }
    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };

  arrowShapes['half-triangle-overshot'] = {
    _points: [
      0, -0.25,
      -0.5, -0.25,
      0.5, 0.25
    ],
    
    leavePathOpen: true,
    matchEdgeWidth: true,

    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = this._points;
      
//      console.log("collide(): " + direction);
      
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var points = this._points;
    
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        context.lineTo(pt.x, pt.y);
      }
    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };

  arrowShapes['none'] = {
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      return false;
    },
    
    roughCollide: function(x, y, centerX, centerY, width, height, direction, padding) {
      return false;
    },
    
    draw: function(context) {
    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return 0;
    }
  };
  
  arrowShapes['circle'] = {
    _baseRadius: 0.15,
    
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      // Transform x, y to get non-rotated ellipse
      
      if (width != height) {                  
        var aspectRatio = (height + padding) / (width + padding);
        y /= aspectRatio;
        centerY /= aspectRatio;
        
        return (Math.pow(centerX - x, 2) 
          + Math.pow(centerY - y, 2) <= Math.pow((width + padding)
            * arrowShapes['circle']._baseRadius, 2));
      } else {
        return (Math.pow(centerX - x, 2) 
          + Math.pow(centerY - y, 2) <= Math.pow((width + padding)
            * arrowShapes['circle']._baseRadius, 2));
      }
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      context.arc(translation.x, translation.y, arrowShapes['circle']._baseRadius * size, 0, Math.PI * 2, false);
    },
    
    spacing: function(edge) {
      return rendFunc.getArrowWidth(edge._private.style['width'].pxValue)
        * arrowShapes['circle']._baseRadius;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };
  
  arrowShapes['inhibitor'] = {
    _points: [
      -0.25, 0,
      -0.25, -0.1,
      0.25, -0.1,
      0.25, 0
    ],
    
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = arrowShapes['inhibitor']._points;
      
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var points = arrowShapes['inhibitor']._points;
      
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        context.lineTo(pt.x, pt.y);
      }
    },
    
    spacing: function(edge) {
      return 1;
    },
    
    gap: function(edge) {
      return 1;
    }
  };

  arrowShapes['tee'] = arrowShapes['inhibitor'];

  arrowShapes['square'] = {
    _points: [
      -0.15, 0.00,
      0.15, 0.00,
      0.15, -0.3,
      -0.15, -0.3
    ],
    
    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = arrowShapes['square']._points;
      
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },
    
    roughCollide: bbCollide,
    
    draw: function(context, size, angle, translation) {
      var points = arrowShapes['square']._points;
    
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        context.lineTo(pt.x, pt.y);
      }
    },
    
    spacing: function(edge) {
      return 0;
    },

    gap: function(edge) {
      return edge._private.style['width'].pxValue * 2;
    }
  };

  arrowShapes['diamond'] = {
    _points: [
      -0.15, -0.15,
      0, -0.3,
      0.15, -0.15,
      0, 0
    ],

    collide: function(x, y, centerX, centerY, width, height, direction, padding) {
      var points = arrowShapes['diamond']._points;
          
      return $$.math.pointInsidePolygon(
        x, y, points, centerX, centerY, width, height, direction, padding);
    },

    roughCollide: bbCollide,

    draw: function(context, size, angle, translation) {
      var points = arrowShapes['diamond']._points;
    
      for (var i = 0; i < points.length / 2; i++) {
        var pt = transform( points[i * 2], points[i * 2 + 1], size, angle, translation );

        context.lineTo(pt.x, pt.y);
      }
    },
    
    spacing: function(edge) {
      return 0;
    },
    
    gap: function(edge) {
      return edge._private.style['width'].pxValue;
    }
  };

})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  CanvasRenderer.prototype.getCachedNodes = function() {
    var data = this.data; var cy = this.data.cy;
    
    if (data.cache == null) {
      data.cache = {};
    }
    
    if (data.cache.cachedNodes == null) {
      data.cache.cachedNodes = cy.nodes();
    }
    
    return data.cache.cachedNodes;
  };
  
  CanvasRenderer.prototype.updateNodesCache = function() {
    var data = this.data; var cy = this.data.cy;
    
    if (data.cache == null) {
      data.cache = {};
    }
    
    data.cache.cachedNodes = cy.nodes();
  };
  
  CanvasRenderer.prototype.getCachedEdges = function() {
    var data = this.data; var cy = this.data.cy;
    
    if (data.cache == null) {
      data.cache = {};
    }
    
    if (data.cache.cachedEdges == null) {
      data.cache.cachedEdges = cy.edges();
    }
    
    return data.cache.cachedEdges;
  };
  
  CanvasRenderer.prototype.updateEdgesCache = function() {
    var data = this.data; var cy = this.data.cy;
    
    if (data.cache == null) {
      data.cache = {};
    }
    
    data.cache.cachedEdges = cy.edges();
  };

})( cytoscape );

;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  // Project mouse
  CanvasRenderer.prototype.projectIntoViewport = function(clientX, clientY) {
    var offsets = this.findContainerClientCoords();
    var offsetLeft = offsets[0];
    var offsetTop = offsets[1];
    
    var x = clientX - offsetLeft; 
    var y = clientY - offsetTop;
    
    x -= this.data.cy.pan().x; y -= this.data.cy.pan().y; x /= this.data.cy.zoom(); y /= this.data.cy.zoom();
    return [x, y];
  };

  CanvasRenderer.prototype.findContainerClientCoords = function() {
    var container = this.data.container;

    var bb = this.containerBB = this.containerBB || container.getBoundingClientRect();

    return [bb.left, bb.top, bb.right - bb.left, bb.bottom - bb.top];
  };

  CanvasRenderer.prototype.invalidateContainerClientCoordsCache = function(){
    this.containerBB = null;
  };

  // Find nearest element
  CanvasRenderer.prototype.findNearestElement = function(x, y, visibleElementsOnly){
    var self = this;
    var eles = this.getCachedZSortedEles();
    var near = [];
    var isTouch = CanvasRenderer.isTouch;
    var zoom = this.data.cy.zoom();
    var hasCompounds = this.data.cy.hasCompoundNodes();
    var edgeThreshold = (isTouch ? 256 : 32) / zoom;
    var nodeThreshold = (isTouch ? 16 : 0) /  zoom;

    function checkNode(node){
      var width = node.outerWidth();
      var height = node.outerHeight();
      var hw = width/2;
      var hh = height/2;
      var pos = node._private.position;

      if(
        pos.x - hw <= x && x <= pos.x + hw // bb check x
          &&
        pos.y - hh <= y && y <= pos.y + hh // bb check y
      ){
        var visible = !visibleElementsOnly || ( node.visible() && !node.transparent() );

        // exit early if invisible edge and must be visible
        if( visibleElementsOnly && !visible ){
          return;
        }

        var shape = CanvasRenderer.nodeShapes[ self.getNodeShape(node) ];
        var borderWO = node._private.style['border-width'].pxValue / 2;

        if(
          shape.checkPoint(x, y, borderWO, width + nodeThreshold, height + nodeThreshold, pos.x, pos.y)
        ){
            near.push( node );
        }

      }
    }

    function checkEdge(edge){
      var rs = edge._private.rscratch;
      var style = edge._private.style;
      var width = style['width'].pxValue;
      var widthSq = width * width;
      var width2 = width * 2;
      var src = edge._private.source;
      var tgt = edge._private.target;
      var inEdgeBB = false;

      // exit early if invisible edge and must be visible
      var passedVisibilityCheck;
      var passesVisibilityCheck = function(){
        if( passedVisibilityCheck !== undefined ){
          return passedVisibilityCheck;
        }

        if( !visibleElementsOnly ){
          passedVisibilityCheck = true;
          return true;
        }

        var visible = edge.visible() && !edge.transparent();
        if( visible ){
          passedVisibilityCheck = true;
          return true;
        }

        passedVisibilityCheck = false;
        return false;
      };

      if (rs.edgeType === 'self') {
        if(
            (
              (inEdgeBB = $$.math.inBezierVicinity(x, y, rs.startX, rs.startY, rs.cp2ax, rs.cp2ay, rs.selfEdgeMidX, rs.selfEdgeMidY, widthSq))
                && passesVisibilityCheck() &&
              ( widthSq + edgeThreshold > $$.math.sqDistanceToQuadraticBezier(x, y, rs.startX, rs.startY, rs.cp2ax, rs.cp2ay, rs.selfEdgeMidX, rs.selfEdgeMidY) )
            )
              ||
            (
              (inEdgeBB = $$.math.inBezierVicinity(x, y, rs.selfEdgeMidX, rs.selfEdgeMidY, rs.cp2cx, rs.cp2cy, rs.endX, rs.endY, widthSq))
                && passesVisibilityCheck() &&
              ( widthSq + edgeThreshold > $$.math.sqDistanceToQuadraticBezier(x, y, rs.selfEdgeMidX, rs.selfEdgeMidY, rs.cp2cx, rs.cp2cy, rs.endX, rs.endY) )
            )
        ){
          near.push( edge );
        }
      
      } else if (rs.edgeType === 'haystack') {
        var radius = style['haystack-radius'].value;
        var halfRadius = radius/2; // b/c have to half width/height

        var tgtPos = tgt._private.position;
        var tgtW = tgt.width();
        var tgtH = tgt.height();
        var srcPos = src._private.position;
        var srcW = src.width();
        var srcH = src.height();

        var startX = srcPos.x + rs.source.x * srcW * halfRadius;
        var startY = srcPos.y + rs.source.y * srcH * halfRadius;
        var endX = tgtPos.x + rs.target.x * tgtW * halfRadius;
        var endY = tgtPos.y + rs.target.y * tgtH * halfRadius;

        if( 
          (inEdgeBB = $$.math.inLineVicinity(x, y, startX, startY, endX, endY, width2))
            && passesVisibilityCheck() &&
          widthSq + edgeThreshold > $$.math.sqDistanceToFiniteLine( x, y, startX, startY, endX, endY )
        ){
          near.push( edge );
        }
      
      } else if (rs.edgeType === 'straight') {
        if(
          (inEdgeBB = $$.math.inLineVicinity(x, y, rs.startX, rs.startY, rs.endX, rs.endY, width2))
            && passesVisibilityCheck() &&
          widthSq + edgeThreshold > $$.math.sqDistanceToFiniteLine(x, y, rs.startX, rs.startY, rs.endX, rs.endY)
        ){
          near.push( edge );
        }
      
      } else if (rs.edgeType === 'bezier') {
        if(
          (inEdgeBB = $$.math.inBezierVicinity(x, y, rs.startX, rs.startY, rs.cp2x, rs.cp2y, rs.endX, rs.endY, widthSq))
            && passesVisibilityCheck() &&
          (widthSq + edgeThreshold > $$.math.sqDistanceToQuadraticBezier(x, y, rs.startX, rs.startY, rs.cp2x, rs.cp2y, rs.endX, rs.endY))
        ){
          near.push( edge );
        }
      }
      
      if( inEdgeBB && passesVisibilityCheck() && near.length === 0 || near[near.length - 1] !== edge ){
        var srcShape = CanvasRenderer.arrowShapes[ style['source-arrow-shape'].value ];
        var tgtShape = CanvasRenderer.arrowShapes[ style['target-arrow-shape'].value ];

        var src = src || edge._private.source;
        var tgt = tgt || edge._private.target;

        var tgtPos = tgt._private.position;
        var srcPos = src._private.position;

        var srcArW = self.getArrowWidth( style['width'].pxValue );
        var srcArH = self.getArrowHeight( style['width'].pxValue );

        var tgtArW = srcArW;
        var tgtArH = srcArH;

        if(
          (
            srcShape.roughCollide(x, y, rs.arrowStartX, rs.arrowStartY, srcArW, srcArH, [rs.arrowStartX - srcPos.x, rs.arrowStartY - srcPos.y], 0)
              && 
            srcShape.collide(x, y, rs.arrowStartX, rs.arrowStartY, srcArW, srcArH, [rs.arrowStartX - srcPos.x, rs.arrowStartY - srcPos.y], 0)
          )
            ||
          (
            tgtShape.roughCollide(x, y, rs.arrowEndX, rs.arrowEndY, tgtArW, tgtArH, [rs.arrowEndX - tgtPos.x, rs.arrowEndY - tgtPos.y], 0)
              &&
            tgtShape.collide(x, y, rs.arrowEndX, rs.arrowEndY, tgtArW, tgtArH, [rs.arrowEndX - tgtPos.x, rs.arrowEndY - tgtPos.y], 0)
          )
        ){
          near.push( edge );
        }
      }

      // for compound graphs, hitting edge may actually want a connected node instead (b/c edge may have greater z-index precedence)
      if( hasCompounds &&  near.length > 0 && near[ near.length - 1 ] === edge ){
        checkNode( src );
        checkNode( tgt );
      }
    }

    for( var i = eles.length - 1; i >= 0; i-- ){ // reverse order for precedence
      var ele = eles[i];

      if( near.length > 0 ){ break; } // since we check in z-order, first found is top and best result => exit early

      if( ele._private.group === 'nodes' ){ 
        checkNode( eles[i] );

      } else  { // then edge
        checkEdge( eles[i] );
      }

    }
  
    
    if( near.length > 0 ){
      return near[ near.length - 1 ];
    } else {
      return null;
    }
  }; 

  // 'Give me everything from this box'
  CanvasRenderer.prototype.getAllInBox = function(x1, y1, x2, y2) {
    var nodes = this.getCachedNodes();
    var edges = this.getCachedEdges();
    var box = [];
    
    var x1c = Math.min(x1, x2);
    var x2c = Math.max(x1, x2);
    var y1c = Math.min(y1, y2);
    var y2c = Math.max(y1, y2); 

    x1 = x1c; 
    x2 = x2c; 
    y1 = y1c; 
    y2 = y2c; 

    var heur;
    
    for ( var i = 0; i < nodes.length; i++ ){
      var pos = nodes[i]._private.position;
      var nShape = this.getNodeShape(nodes[i]);
      var w = this.getNodeWidth(nodes[i]);
      var h = this.getNodeHeight(nodes[i]);
      var border = nodes[i]._private.style['border-width'].pxValue / 2;
      var shapeObj = CanvasRenderer.nodeShapes[ nShape ];

      if ( shapeObj.intersectBox(x1, y1, x2, y2, w, h, pos.x, pos.y, border) ){
        box.push(nodes[i]);
      }
    }
    
    for ( var i = 0; i < edges.length; i++ ){
      var rs = edges[i]._private.rscratch;

      if (edges[i]._private.rscratch.edgeType == 'self') {
        if ((heur = $$.math.boxInBezierVicinity(x1, y1, x2, y2,
            rs.startX, rs.startY,
            rs.cp2ax, rs.cp2ay,
            rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))
              &&
            (heur == 2 || (heur == 1 && $$.math.checkBezierInBox(x1, y1, x2, y2,
              rs.startX, rs.startY,
              rs.cp2ax, rs.cp2ay,
              rs.endX, rs.endY, edges[i]._private.style['width'].pxValue)))
                ||
          (heur = $$.math.boxInBezierVicinity(x1, y1, x2, y2,
            rs.startX, rs.startY,
            rs.cp2cx, rs.cp2cy,
            rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))
              &&
            (heur == 2 || (heur == 1 && $$.math.checkBezierInBox(x1, y1, x2, y2,
              rs.startX, rs.startY,
              rs.cp2cx, rs.cp2cy,
              rs.endX, rs.endY, edges[i]._private.style['width'].pxValue)))
          )
        { box.push(edges[i]); }
      }
      
      if (rs.edgeType == 'bezier' &&
        (heur = $$.math.boxInBezierVicinity(x1, y1, x2, y2,
            rs.startX, rs.startY,
            rs.cp2x, rs.cp2y,
            rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))
              &&
            (heur == 2 || (heur == 1 && $$.math.checkBezierInBox(x1, y1, x2, y2,
              rs.startX, rs.startY,
              rs.cp2x, rs.cp2y,
              rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))))
        { box.push(edges[i]); }
    
      if (rs.edgeType == 'straight' &&
        (heur = $$.math.boxInBezierVicinity(x1, y1, x2, y2,
            rs.startX, rs.startY,
            rs.startX * 0.5 + rs.endX * 0.5, 
            rs.startY * 0.5 + rs.endY * 0.5, 
            rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))
              && /* console.log('test', heur) == undefined && */
            (heur == 2 || (heur == 1 && $$.math.checkStraightEdgeInBox(x1, y1, x2, y2,
              rs.startX, rs.startY,
              rs.endX, rs.endY, edges[i]._private.style['width'].pxValue))))
        { box.push(edges[i]); }


      if (rs.edgeType == 'haystack'){
        var tgt = edges[i].target()[0];
        var tgtPos = tgt.position();
        var src = edges[i].source()[0];
        var srcPos = src.position();

        var startX = srcPos.x + rs.source.x;
        var startY = srcPos.y + rs.source.y;
        var endX = tgtPos.x + rs.target.x;
        var endY = tgtPos.y + rs.target.y;

        var startInBox = (x1 <= startX && startX <= x2) && (y1 <= startY && startY <= y2);
        var endInBox = (x1 <= endX && endX <= x2) && (y1 <= endY && endY <= y2);

        if( startInBox && endInBox ){
          box.push( edges[i] );
        }
      }
      
    }
    
    return box;
  };


  /**
   * Returns the width of the given node. If the width is set to auto,
   * returns the value of the autoWidth field.
   *
   * @param node          a node
   * @return {number}     width of the node
   */
  CanvasRenderer.prototype.getNodeWidth = function(node)
  {
    return node.width();
  };

  /**
   * Returns the height of the given node. If the height is set to auto,
   * returns the value of the autoHeight field.
   *
   * @param node          a node
   * @return {number}     width of the node
   */
  CanvasRenderer.prototype.getNodeHeight = function(node)
  {
    return node.height();
  };

  /**
   * Returns the shape of the given node. If the height or width of the given node
   * is set to auto, the node is considered to be a compound.
   *
   * @param node          a node
   * @return {String}     shape of the node
   */
  CanvasRenderer.prototype.getNodeShape = function(node)
  {
    // TODO only allow rectangle for a compound node?
//    if (node._private.style['width'].value == 'auto' ||
//        node._private.style['height'].value == 'auto')
//    {
//      return 'rectangle';
//    }

    var shape = node._private.style['shape'].value;

    if( node.isParent() ){
      if( shape === 'rectangle' || shape === 'roundrectangle' ){
        return shape;
      } else {
        return 'rectangle';
      }
    }

    return shape;
  };


  CanvasRenderer.prototype.getNodePadding = function(node)
  {
    var left = node._private.style['padding-left'].pxValue;
    var right = node._private.style['padding-right'].pxValue;
    var top = node._private.style['padding-top'].pxValue;
    var bottom = node._private.style['padding-bottom'].pxValue;

    if (isNaN(left))
    {
      left = 0;
    }

    if (isNaN(right))
    {
      right = 0;
    }

    if (isNaN(top))
    {
      top = 0;
    }

    if (isNaN(bottom))
    {
      bottom = 0;
    }

    return {left : left,
      right : right,
      top : top,
      bottom : bottom};
  };

  CanvasRenderer.prototype.zOrderSort = $$.Collection.zIndexSort;

  CanvasRenderer.prototype.updateCachedZSortedEles = function(){
    this.getCachedZSortedEles( true );
  };

  CanvasRenderer.prototype.getCachedZSortedEles = function( forceRecalc ){
    var lastNodes = this.lastZOrderCachedNodes;
    var lastEdges = this.lastZOrderCachedEdges;
    var nodes = this.getCachedNodes();
    var edges = this.getCachedEdges();
    var eles = [];

    if( forceRecalc || !lastNodes || !lastEdges || lastNodes !== nodes || lastEdges !== edges ){ 
      //console.time('cachezorder')
      
      for( var i = 0; i < nodes.length; i++ ){
        if( nodes[i].visible() && !nodes[i].transparent() ){
          eles.push( nodes[i] );
        }
      }

      for( var i = 0; i < edges.length; i++ ){
        if( edges[i].visible() && !edges[i].transparent() ){
          eles.push( edges[i] );
        }
      }

      eles.sort( this.zOrderSort );
      this.cachedZSortedEles = eles;
      //console.log('make cache')

      //console.timeEnd('cachezorder')
    } else {
      eles = this.cachedZSortedEles;
      //console.log('read cache')
    }

    this.lastZOrderCachedNodes = nodes;
    this.lastZOrderCachedEdges = edges;

    return eles;
  };

  CanvasRenderer.prototype.projectBezier = function(edge){
    var qbezierAt = $$.math.qbezierAt;
    var rs = edge._private.rscratch;
    var bpts = edge._private.rstyle.bezierPts = [];

    function pushBezierPts(pts){
      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.05 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.05 )
      });

      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.25 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.25 )
      });

      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.4 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.4 )
      });

      var mid = {
        x: qbezierAt( pts[0], pts[2], pts[4], 0.5 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.5 )
      };

      bpts.push( mid );

      if( rs.edgeType === 'self' ){
        rs.midX = rs.selfEdgeMidX;
        rs.midY = rs.selfEdgeMidY;
      } else {
        rs.midX = mid.x;
        rs.midY = mid.y;
      }

      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.6 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.6 )
      });

      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.75 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.75 )
      });

      bpts.push({
        x: qbezierAt( pts[0], pts[2], pts[4], 0.95 ),
        y: qbezierAt( pts[1], pts[3], pts[5], 0.95 )
      });
    }

    if( rs.edgeType === 'self' ){
      pushBezierPts( [rs.startX, rs.startY, rs.cp2ax, rs.cp2ay, rs.selfEdgeMidX, rs.selfEdgeMidY] );
      pushBezierPts( [rs.selfEdgeMidX, rs.selfEdgeMidY, rs.cp2cx, rs.cp2cy, rs.endX, rs.endY] );
    } else if( rs.edgeType === 'bezier' ){
      pushBezierPts( [rs.startX, rs.startY, rs.cp2x, rs.cp2y, rs.endX, rs.endY] );
    }
  };

  CanvasRenderer.prototype.recalculateNodeLabelProjection = function( node ){
    var content = node._private.style['content'].strValue;
    if( !content || content.match(/^\s+$/) ){ return; }

    var textX, textY;
    var nodeWidth = node.outerWidth();
    var nodeHeight = node.outerHeight();
    var nodePos = node._private.position;
    var textHalign = node._private.style['text-halign'].strValue;
    var textValign = node._private.style['text-valign'].strValue;
    var rs = node._private.rscratch;
    var rstyle = node._private.rstyle;

    switch( textHalign ){
      case 'left':
        textX = nodePos.x - nodeWidth / 2;
        break;

      case 'right':
        textX = nodePos.x + nodeWidth / 2;
        break;

      default: // e.g. center
        textX = nodePos.x;
    }

    switch( textValign ){
      case 'top':
        textY = nodePos.y - nodeHeight / 2;
        break;

      case 'bottom':
        textY = nodePos.y + nodeHeight / 2;
        break;

      default: // e.g. middle
        textY = nodePos.y;
    }
  
    rs.labelX = textX;
    rs.labelY = textY;
    rstyle.labelX = textX;
    rstyle.labelY = textY;

    this.applyLabelDimensions( node );
  };

  CanvasRenderer.prototype.recalculateEdgeLabelProjection = function( edge ){
    var content = edge._private.style['content'].strValue;
    if( !content || content.match(/^\s+$/) ){ return; }

    var textX, textY;  
    var edgeCenterX, edgeCenterY;
    var rs = edge._private.rscratch;
    var rstyle = edge._private.rstyle;
    
    if (rs.edgeType == 'self') {
      edgeCenterX = rs.selfEdgeMidX;
      edgeCenterY = rs.selfEdgeMidY;
    } else if (rs.edgeType == 'straight') {
      edgeCenterX = (rs.startX + rs.endX) / 2;
      edgeCenterY = (rs.startY + rs.endY) / 2;
    } else if (rs.edgeType == 'bezier') {
      edgeCenterX = $$.math.qbezierAt( rs.startX, rs.cp2x, rs.endX, 0.5 );
      edgeCenterY = $$.math.qbezierAt( rs.startY, rs.cp2y, rs.endY, 0.5 );
    } else if (rs.edgeType == 'haystack') {
      var srcPos = edge._private.source._private.position;
      var tgtPos = edge._private.target._private.position;

      edgeCenterX = (srcPos.x + rs.source.x + tgtPos.x + rs.target.x)/2;
      edgeCenterY = (srcPos.y + rs.source.y + tgtPos.y + rs.target.y)/2;
    }
    
    textX = edgeCenterX;
    textY = edgeCenterY;

    // add center point to style so bounding box calculations can use it
    rs.labelX = textX;
    rs.labelY = textY;
    rstyle.labelX = textX;
    rstyle.labelY = textY;

    this.applyLabelDimensions( edge );
  };

  CanvasRenderer.prototype.applyLabelDimensions = function( ele ){
    var rs = ele._private.rscratch;
    var rstyle = ele._private.rstyle;

    var text = this.getLabelText( ele );
    var labelDims = this.calculateLabelDimensions( ele, text );
 
    rstyle.labelWidth = labelDims.width;
    rs.labelWidth = labelDims.width;
 
    rstyle.labelHeight = labelDims.height;
    rs.labelHeight = labelDims.height;
  };

  CanvasRenderer.prototype.getLabelText = function( ele ){
    var style = ele._private.style;
    var text = ele._private.style['content'].strValue;
    var textTransform = style['text-transform'].value;
    
    if (textTransform == 'none') {
    } else if (textTransform == 'uppercase') {
      text = text.toUpperCase();
    } else if (textTransform == 'lowercase') {
      text = text.toLowerCase();
    }

    return text;
  };

  CanvasRenderer.prototype.calculateLabelDimensions = function( ele, text ){
    var r = this;
    var style = ele._private.style;
    var fStyle = style['font-style'].strValue;
    var size = style['font-size'].pxValue + 'px';
    var family = style['font-family'].strValue;
    // var variant = style['font-variant'].strValue;
    var weight = style['font-weight'].strValue;

    var cacheKey = ele._private.labelKey;
    var cache = r.labelDimCache || (r.labelDimCache = {});

    if( cache[cacheKey] ){
      return cache[cacheKey];
    }

    var div = this.labelCalcDiv;

    if( !div ){
      div = this.labelCalcDiv = document.createElement('div');
      document.body.appendChild( div );
    }

    var ds = div.style;

    // from ele style
    ds.fontFamily = family;
    ds.fontStyle = fStyle;
    ds.fontSize = size;
    // ds.fontVariant = variant;
    ds.fontWeight = weight;

    // forced style
    ds.position = 'absolute';
    ds.left = '-9999px';
    ds.top = '-9999px';
    ds.zIndex = '-1';
    ds.visibility = 'hidden';
    ds.pointerEvents = 'none';
    ds.padding = '0';
    ds.lineHeight = '1';

    // put label content in div
    div.textContent = text;

    cache[cacheKey] = {
      width: div.clientWidth,
      height: div.clientHeight
    };

    return cache[cacheKey];
  };  

  CanvasRenderer.prototype.recalculateRenderedStyle = function( eles ){
    var edges = [];
    var nodes = [];
    var handledEdge = {};

    for( var i = 0; i < eles.length; i++ ){
      var ele = eles[i];
      var _p = ele._private;
      var rs = _p.rscratch;
      var rstyle = _p.rstyle;
      var id = _p.data.id;
      var bbStyleSame = rs.boundingBoxKey != null && _p.boundingBoxKey === rs.boundingBoxKey;
      var labelStyleSame = rs.labelKey != null && _p.labelKey === rs.labelKey;
      var styleSame = bbStyleSame && labelStyleSame;

      if( ele._private.group === 'nodes' ){
        var pos = _p.position;
        var posSame = rstyle.nodeX != null && rstyle.nodeY != null && pos.x === rstyle.nodeX && pos.y === rstyle.nodeY;

        if( !posSame || !styleSame ){
          nodes.push( ele );
        }

        rstyle.nodeX = pos.x;
        rstyle.nodeY = pos.y;
      } else { // edges

        var srcPos = ele._private.source._private.position;
        var tgtPos = ele._private.target._private.position;
        var srcSame = rstyle.srcX != null && rstyle.srcY != null && srcPos.x === rstyle.srcX && srcPos.y === rstyle.srcY;
        var tgtSame = rstyle.tgtX != null && rstyle.tgtY != null && tgtPos.x === rstyle.tgtX && tgtPos.y === rstyle.tgtY;
        var positionsSame = srcSame && tgtSame;

        if( !positionsSame || !styleSame ){
          var curveType = _p.style['curve-style'].value;

          if( curveType === 'bezier' ){
            if( !handledEdge[ id ] ){
              edges.push( ele );
              handledEdge[ id ] = true;

              var parallelEdges = ele.parallelEdges();
              for( var i = 0; i < parallelEdges.length; i++ ){
                var pEdge = parallelEdges[i];
                var pId = pEdge._private.data.id;

                if( !handledEdge[ pId ] ){
                  edges.push( pEdge );
                  handledEdge[ pId ] = true;
                }
                
              }
            }
          } else {
            edges.push( ele );
          }
        } // if positions diff

        // update rstyle positions
        rstyle.srcX = srcPos.x;
        rstyle.srcY = srcPos.y;
        rstyle.tgtX = tgtPos.x;
        rstyle.tgtY = tgtPos.y;

      } // if edges

      rs.boundingBoxKey = _p.boundingBoxKey;
      rs.labelKey = _p.labelKey;
    }

    this.recalculateEdgeProjections( edges );
    this.recalculateLabelProjections( nodes, edges );
  };

  CanvasRenderer.prototype.recalculateLabelProjections = function( nodes, edges ){
    for( var i = 0; i < nodes.length; i++ ){
      this.recalculateNodeLabelProjection( nodes[i] );
    }

    for( var i = 0; i < edges.length; i++ ){
      this.recalculateEdgeLabelProjection( edges[i] );
    }
  };

  CanvasRenderer.prototype.recalculateEdgeProjections = function( edges ){
    this.findEdgeControlPoints( edges );
  };


  // Find edge control points
  CanvasRenderer.prototype.findEdgeControlPoints = function(edges) {
    if( !edges || edges.length === 0 ){ return; }

    var hashTable = {};
    var pairIds = [];
    var haystackEdges = [];

    // create a table of edge (src, tgt) => list of edges between them
    var pairId;
    for (var i = 0; i < edges.length; i++){
      var edge = edges[i];
      var style = edge._private.style;
      var edgeIsUnbundled = style['curve-style'].value === 'unbundled-bezier';

      // ignore edges who are not to be displayed
      // they shouldn't take up space
      if( style.display.value === 'none' ){
        continue;
      }

      if( style['curve-style'].value === 'haystack' ){
        haystackEdges.push( edge );
        continue;
      }

      var srcId = edge._private.data.source;
      var tgtId = edge._private.data.target;

      pairId = srcId > tgtId ?
        tgtId + '-' + srcId :
        srcId + '-' + tgtId ;

      if( edgeIsUnbundled ){
        pairId = 'unbundled' + edge._private.data.id;
      }

      if (hashTable[pairId] == null) {
        hashTable[pairId] = [];
        pairIds.push( pairId );
      }
      
      hashTable[pairId].push( edge );

      if( edgeIsUnbundled ){
        hashTable[pairId].hasUnbundled = true;
      }
    }

    var src, tgt, srcPos, tgtPos, srcW, srcH, tgtW, tgtH, srcShape, tgtShape, srcBorder, tgtBorder;
    var vectorNormInverse;
    var badBezier;
    
    // for each pair (src, tgt), create the ctrl pts
    // Nested for loop is OK; total number of iterations for both loops = edgeCount  
    for (var p = 0; p < pairIds.length; p++) {
      pairId = pairIds[p];
      var pairEdges = hashTable[pairId];
    
      // for each pair id, the edges should be sorted by index
      pairEdges.sort(function(edge1, edge2){
        return edge1._private.index - edge2._private.index;
      });

      src = pairEdges[0]._private.source;
      tgt = pairEdges[0]._private.target;

      // make sure src/tgt distinction is consistent
      // (src/tgt in this case are just for ctrlpts and don't actually have to be true src/tgt)
      if( src._private.data.id > tgt._private.data.id ){
        var temp = src;
        src = tgt;
        tgt = temp;
      }

      srcPos = src._private.position;
      tgtPos = tgt._private.position;

      srcW = this.getNodeWidth(src);
      srcH = this.getNodeHeight(src);

      tgtW = this.getNodeWidth(tgt);
      tgtH = this.getNodeHeight(tgt);

      srcShape = CanvasRenderer.nodeShapes[ this.getNodeShape(src) ];
      tgtShape = CanvasRenderer.nodeShapes[ this.getNodeShape(tgt) ];

      srcBorder = src._private.style['border-width'].pxValue;
      tgtBorder = tgt._private.style['border-width'].pxValue;

      badBezier = false;
      

      if( (pairEdges.length > 1 && src !== tgt) || pairEdges.hasUnbundled ){

        // pt outside src shape to calc distance/displacement from src to tgt
        var srcOutside = srcShape.intersectLine(
          srcPos.x,
          srcPos.y,
          srcW,
          srcH,
          tgtPos.x,
          tgtPos.y,
          srcBorder / 2
        );

        // pt outside tgt shape to calc distance/displacement from src to tgt
        var tgtOutside = tgtShape.intersectLine(
          tgtPos.x,
          tgtPos.y,
          tgtW,
          tgtH,
          srcPos.x,
          srcPos.y,
          tgtBorder / 2
        );

        var midptSrcPts = {
          x1: srcOutside[0],
          x2: tgtOutside[0],
          y1: srcOutside[1],
          y2: tgtOutside[1]
        };

        var dy = ( tgtOutside[1] - srcOutside[1] );
        var dx = ( tgtOutside[0] - srcOutside[0] );
        var l = Math.sqrt( dx*dx + dy*dy );

        var vector = {
          x: dx,
          y: dy
        };
        
        var vectorNorm = {
          x: vector.x/l,
          y: vector.y/l
        };
        vectorNormInverse = {
          x: -vectorNorm.y,
          y: vectorNorm.x
        };

        // if src intersection is inside tgt or tgt intersection is inside src, then no ctrl pts to draw
        if( 
          tgtShape.checkPoint( srcOutside[0], srcOutside[1], tgtBorder/2, tgtW, tgtH, tgtPos.x, tgtPos.y )  ||
          srcShape.checkPoint( tgtOutside[0], tgtOutside[1], srcBorder/2, srcW, srcH, srcPos.x, srcPos.y ) 
        ){
          vectorNormInverse = {};
          badBezier = true;
        }
        
      }
      
      var edge;
      var rs;
      
      for (var i = 0; i < pairEdges.length; i++) {
        edge = pairEdges[i];
        rs = edge._private.rscratch;
        
        var edgeIndex1 = rs.lastEdgeIndex;
        var edgeIndex2 = i;

        var numEdges1 = rs.lastNumEdges;
        var numEdges2 = pairEdges.length;

        var eStyle = edge._private.style;
        var stepSize = eStyle['control-point-step-size'].pxValue;
        var stepDist = eStyle['control-point-distance'] !== undefined ? eStyle['control-point-distance'].pxValue : undefined;
        var stepWeight = eStyle['control-point-weight'].value;
        var edgeIsUnbundled = eStyle['curve-style'].value === 'unbundled-bezier';

        var srcX1 = rs.lastSrcCtlPtX;
        var srcX2 = srcPos.x;
        var srcY1 = rs.lastSrcCtlPtY;
        var srcY2 = srcPos.y;
        var srcW1 = rs.lastSrcCtlPtW;
        var srcW2 = src.outerWidth();
        var srcH1 = rs.lastSrcCtlPtH;
        var srcH2 = src.outerHeight();

        var tgtX1 = rs.lastTgtCtlPtX;
        var tgtX2 = tgtPos.x;
        var tgtY1 = rs.lastTgtCtlPtY;
        var tgtY2 = tgtPos.y;
        var tgtW1 = rs.lastTgtCtlPtW;
        var tgtW2 = tgt.outerWidth();
        var tgtH1 = rs.lastTgtCtlPtH;
        var tgtH2 = tgt.outerHeight();

        var width1 = rs.lastW;
        var width2 = eStyle['control-point-step-size'].pxValue;

        if( badBezier ){
          rs.badBezier = true;
        } else {
          rs.badBezier = false;
        }

        if( srcX1 === srcX2 && srcY1 === srcY2 && srcW1 === srcW2 && srcH1 === srcH2
        &&  tgtX1 === tgtX2 && tgtY1 === tgtY2 && tgtW1 === tgtW2 && tgtH1 === tgtH2
        &&  width1 === width2
        &&  ((edgeIndex1 === edgeIndex2 && numEdges1 === numEdges2) || edgeIsUnbundled) ){
          // console.log('edge ctrl pt cache HIT')
          continue; // then the control points haven't changed and we can skip calculating them
        } else {
          rs.lastSrcCtlPtX = srcX2;
          rs.lastSrcCtlPtY = srcY2;
          rs.lastSrcCtlPtW = srcW2;
          rs.lastSrcCtlPtH = srcH2;
          rs.lastTgtCtlPtX = tgtX2;
          rs.lastTgtCtlPtY = tgtY2;
          rs.lastTgtCtlPtW = tgtW2;
          rs.lastTgtCtlPtH = tgtH2;
          rs.lastEdgeIndex = edgeIndex2;
          rs.lastNumEdges = numEdges2;
          rs.lastWidth = width2;
          // console.log('edge ctrl pt cache MISS')
        }

        // Self-edge
        if ( src === tgt ) {
            
          rs.edgeType = 'self';
          
          var j = i;
          var loopDist = stepSize;

          if( edgeIsUnbundled ){
            j = 0;
            loopDist = stepDist;
          }

          // New -- fix for large nodes
          rs.cp2ax = srcPos.x;
          rs.cp2ay = srcPos.y - (1 + Math.pow(srcH, 1.12) / 100) * loopDist * (j / 3 + 1);
          
          rs.cp2cx = src._private.position.x - (1 + Math.pow(srcW, 1.12) / 100) * loopDist * (j / 3 + 1);
          rs.cp2cy = srcPos.y;
          
          rs.selfEdgeMidX = (rs.cp2ax + rs.cp2cx) / 2.0;
          rs.selfEdgeMidY = (rs.cp2ay + rs.cp2cy) / 2.0;
          
        // Straight edge
        } else if (pairEdges.length % 2 === 1
          && i === Math.floor(pairEdges.length / 2)
          && !edgeIsUnbundled ) {
          
          rs.edgeType = 'straight';
          
        // Bezier edge
        } else {
          var normStepDist = (0.5 - pairEdges.length / 2 + i) * stepSize;
          var manStepDist;
          var sign = $$.math.signum( normStepDist );

          if( edgeIsUnbundled ){
            manStepDist = stepDist;
          } else {
            manStepDist = stepDist !== undefined ? sign * stepDist : undefined; 
          }

          var distanceFromMidpoint = manStepDist !== undefined ? manStepDist : normStepDist;
          
          var w1 = (1 - stepWeight);
          var w2 = stepWeight;

          var swappedDirection = edge._private.source !== src;
          if( swappedDirection ){
            w1 = stepWeight;
            w2 = (1 - stepWeight);
          }

          var adjustedMidpt = {
            x: midptSrcPts.x1 * w1 + midptSrcPts.x2 * w2,
            y: midptSrcPts.y1 * w1 + midptSrcPts.y2 * w2
          };

          rs.edgeType = 'bezier';
          
          rs.cp2x = adjustedMidpt.x + vectorNormInverse.x * distanceFromMidpoint;
          rs.cp2y = adjustedMidpt.y + vectorNormInverse.y * distanceFromMidpoint;
          
          // console.log(edge, midPointX, displacementX, distanceFromMidpoint);
        }

        // find endpts for edge
        this.findEndpoints( edge );

        var badStart = !$$.is.number( rs.startX ) || !$$.is.number( rs.startY );
        var badAStart = !$$.is.number( rs.arrowStartX ) || !$$.is.number( rs.arrowStartY );
        var badEnd = !$$.is.number( rs.endX ) || !$$.is.number( rs.endY );
        var badAEnd = !$$.is.number( rs.arrowEndX ) || !$$.is.number( rs.arrowEndY );

        var minCpADistFactor = 3;
        var arrowW = this.getArrowWidth( edge._private.style['width'].pxValue ) * CanvasRenderer.arrowShapeHeight;
        var minCpADist = minCpADistFactor * arrowW;
        var startACpDist = $$.math.distance( { x: rs.cp2x, y: rs.cp2y }, { x: rs.startX, y: rs.startY } );
        var closeStartACp = startACpDist < minCpADist;
        var endACpDist = $$.math.distance( { x: rs.cp2x, y: rs.cp2y }, { x: rs.endX, y: rs.endY } );
        var closeEndACp = endACpDist < minCpADist;

        if( rs.edgeType === 'bezier' ){
          var overlapping = false;

          if( badStart || badAStart || closeStartACp ){
            overlapping = true;

            // project control point along line from src centre to outside the src shape
            // (otherwise intersection will yield nothing)
            var cpD = { // delta
              x: rs.cp2x - srcPos.x,
              y: rs.cp2y - srcPos.y
            };
            var cpL = Math.sqrt( cpD.x*cpD.x + cpD.y*cpD.y ); // length of line
            var cpM = { // normalised delta
              x: cpD.x / cpL,
              y: cpD.y / cpL
            };
            var radius = Math.max(srcW, srcH);
            var cpProj = { // *2 radius guarantees outside shape
              x: rs.cp2x + cpM.x * 2 * radius,
              y: rs.cp2y + cpM.y * 2 * radius
            };

            var srcCtrlPtIntn = srcShape.intersectLine(
              srcPos.x,
              srcPos.y,
              srcW,
              srcH,
              cpProj.x,
              cpProj.y,
              srcBorder / 2
            );

            if( closeStartACp ){
              rs.cp2x = rs.cp2x + cpM.x * (minCpADist - startACpDist); 
              rs.cp2y = rs.cp2y + cpM.y * (minCpADist - startACpDist);
            } else {
              rs.cp2x = srcCtrlPtIntn[0] + cpM.x * minCpADist; 
              rs.cp2y = srcCtrlPtIntn[1] + cpM.y * minCpADist;
            }
          }

          if( badEnd || badAEnd || closeEndACp ){
            overlapping = true;

            // project control point along line from tgt centre to outside the tgt shape
            // (otherwise intersection will yield nothing)
            var cpD = { // delta
              x: rs.cp2x - tgtPos.x,
              y: rs.cp2y - tgtPos.y
            };
            var cpL = Math.sqrt( cpD.x*cpD.x + cpD.y*cpD.y ); // length of line
            var cpM = { // normalised delta
              x: cpD.x / cpL,
              y: cpD.y / cpL
            };
            var radius = Math.max(srcW, srcH);
            var cpProj = { // *2 radius guarantees outside shape
              x: rs.cp2x + cpM.x * 2 * radius,
              y: rs.cp2y + cpM.y * 2 * radius
            };

            var tgtCtrlPtIntn = tgtShape.intersectLine(
              tgtPos.x,
              tgtPos.y,
              tgtW,
              tgtH,
              cpProj.x,
              cpProj.y,
              tgtBorder / 2
            );

            if( closeEndACp ){
              rs.cp2x = rs.cp2x + cpM.x * (minCpADist - endACpDist); 
              rs.cp2y = rs.cp2y + cpM.y * (minCpADist - endACpDist);
            } else {
              rs.cp2x = tgtCtrlPtIntn[0] + cpM.x * minCpADist; 
              rs.cp2y = tgtCtrlPtIntn[1] + cpM.y * minCpADist;
            }
            
          }

          if( overlapping ){
            // recalc endpts
            this.findEndpoints( edge );
          }
        } else if( rs.edgeType === 'straight' ){
          rs.midX = ( srcX2 + tgtX2 )/2;
          rs.midY = ( srcY2 + tgtY2 )/2;
        }

        // project the edge into rstyle
        this.projectBezier( edge );

      }
    }
      
    for( var i = 0; i < haystackEdges.length; i++ ){
      var edge = haystackEdges[i];
      var rscratch = edge._private.rscratch;

      if( !rscratch.haystack ){
        var angle = Math.random() * 2 * Math.PI;

        rscratch.source = {
          x: Math.cos(angle),
          y: Math.sin(angle)
        };

        var angle = Math.random() * 2 * Math.PI;

        rscratch.target = {
          x: Math.cos(angle),
          y: Math.sin(angle)
        };
      }  

      // always override as haystack in case set to different type previously
      rscratch.edgeType = 'haystack';
      rscratch.haystack = true;
    }

    return hashTable;
  };

  CanvasRenderer.prototype.findEndpoints = function(edge) {
    var intersect;

    var source = edge.source()[0];
    var target = edge.target()[0];
    
    var tgtArShape = edge._private.style['target-arrow-shape'].value;
    var srcArShape = edge._private.style['source-arrow-shape'].value;

    var tgtBorderW = target._private.style['border-width'].pxValue;
    var srcBorderW = source._private.style['border-width'].pxValue;

    var rs = edge._private.rscratch;
    
    if (edge._private.rscratch.edgeType == 'self') {
      
      var cp = [rs.cp2cx, rs.cp2cy];
      
      intersect = CanvasRenderer.nodeShapes[this.getNodeShape(target)].intersectLine(
        target._private.position.x,
        target._private.position.y,
        this.getNodeWidth(target),
        this.getNodeHeight(target),
        cp[0],
        cp[1], 
        tgtBorderW / 2
      );
      
      var arrowEnd = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[tgtArShape].spacing(edge));
      var edgeEnd = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[tgtArShape].gap(edge));
      
      rs.endX = edgeEnd[0];
      rs.endY = edgeEnd[1];
      
      rs.arrowEndX = arrowEnd[0];
      rs.arrowEndY = arrowEnd[1];
      
      var cp = [rs.cp2ax, rs.cp2ay];

      intersect = CanvasRenderer.nodeShapes[this.getNodeShape(source)].intersectLine(
        source._private.position.x,
        source._private.position.y,
        this.getNodeWidth(source),
        this.getNodeHeight(source),
        cp[0], //halfPointX,
        cp[1], //halfPointY
        srcBorderW / 2
      );
      
      var arrowStart = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[srcArShape].spacing(edge));
      var edgeStart = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[srcArShape].gap(edge));
      
      rs.startX = edgeStart[0];
      rs.startY = edgeStart[1];


      rs.arrowStartX = arrowStart[0];
      rs.arrowStartY = arrowStart[1];
      
    } else if (rs.edgeType == 'straight') {
    
      intersect = CanvasRenderer.nodeShapes[this.getNodeShape(target)].intersectLine(
        target._private.position.x,
        target._private.position.y,
        this.getNodeWidth(target),
        this.getNodeHeight(target),
        source.position().x,
        source.position().y,
        tgtBorderW / 2);
        
      if (intersect.length === 0) {
        rs.noArrowPlacement = true;
  //      return;
      } else {
        rs.noArrowPlacement = false;
      }
      
      var arrowEnd = $$.math.shortenIntersection(intersect,
        [source.position().x, source.position().y],
        CanvasRenderer.arrowShapes[tgtArShape].spacing(edge));
      var edgeEnd = $$.math.shortenIntersection(intersect,
        [source.position().x, source.position().y],
        CanvasRenderer.arrowShapes[tgtArShape].gap(edge));

      rs.endX = edgeEnd[0];
      rs.endY = edgeEnd[1];
      
      rs.arrowEndX = arrowEnd[0];
      rs.arrowEndY = arrowEnd[1];
    
      intersect = CanvasRenderer.nodeShapes[this.getNodeShape(source)].intersectLine(
        source._private.position.x,
        source._private.position.y,
        this.getNodeWidth(source),
        this.getNodeHeight(source),
        target.position().x,
        target.position().y,
        srcBorderW / 2);
      
      if (intersect.length === 0) {
        rs.noArrowPlacement = true;
  //      return;
      } else {
        rs.noArrowPlacement = false;
      }
      
      /*
      console.log("1: "
        + CanvasRenderer.arrowShapes[srcArShape],
          srcArShape);
      */
      var arrowStart = $$.math.shortenIntersection(intersect,
        [target.position().x, target.position().y],
        CanvasRenderer.arrowShapes[srcArShape].spacing(edge));
      var edgeStart = $$.math.shortenIntersection(intersect,
        [target.position().x, target.position().y],
        CanvasRenderer.arrowShapes[srcArShape].gap(edge));

      rs.startX = edgeStart[0];
      rs.startY = edgeStart[1];
      
      rs.arrowStartX = arrowStart[0];
      rs.arrowStartY = arrowStart[1];
            
    } else if (rs.edgeType == 'bezier') {
      // if( window.badArrow) debugger;
      var cp = [rs.cp2x, rs.cp2y];
      
      intersect = CanvasRenderer.nodeShapes[
        this.getNodeShape(target)].intersectLine(
        target._private.position.x,
        target._private.position.y,
        this.getNodeWidth(target),
        this.getNodeHeight(target),
        cp[0], //halfPointX,
        cp[1], //halfPointY
        tgtBorderW / 2
      );
      
      /*
      console.log("2: "
        + CanvasRenderer.arrowShapes[srcArShape],
          srcArShape);
      */
      var arrowEnd = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[tgtArShape].spacing(edge));
      var edgeEnd = $$.math.shortenIntersection(intersect, cp,
        CanvasRenderer.arrowShapes[tgtArShape].gap(edge));
      
      rs.endX = edgeEnd[0];
      rs.endY = edgeEnd[1];
      
      rs.arrowEndX = arrowEnd[0];
      rs.arrowEndY = arrowEnd[1];
      
      intersect = CanvasRenderer.nodeShapes[
        this.getNodeShape(source)].intersectLine(
        source._private.position.x,
        source._private.position.y,
        this.getNodeWidth(source),
        this.getNodeHeight(source),
        cp[0], //halfPointX,
        cp[1], //halfPointY
        srcBorderW / 2
      );
      
      var arrowStart = $$.math.shortenIntersection(
        intersect, 
        cp,
        CanvasRenderer.arrowShapes[srcArShape].spacing(edge)
      );
      var edgeStart = $$.math.shortenIntersection(
        intersect, 
        cp,
        CanvasRenderer.arrowShapes[srcArShape].gap(edge)
      );
    
      rs.startX = edgeStart[0];
      rs.startY = edgeStart[1];
      
      rs.arrowStartX = arrowStart[0];
      rs.arrowStartY = arrowStart[1];
      
      // if( isNaN(rs.startX) || isNaN(rs.startY) ){
      //   debugger;
      // }

    } else if (rs.isArcEdge) {
      return;
    }
  };

  // Find adjacent edges
  CanvasRenderer.prototype.findEdges = function(nodeSet) {
    
    var edges = this.getCachedEdges();
    
    var hashTable = {};
    var adjacentEdges = [];
    
    for (var i = 0; i < nodeSet.length; i++) {
      hashTable[nodeSet[i]._private.data.id] = nodeSet[i];
    }
    
    for (var i = 0; i < edges.length; i++) {
      if (hashTable[edges[i]._private.data.source]
        || hashTable[edges[i]._private.data.target]) {
        
        adjacentEdges.push(edges[i]);
      }
    }
    
    return adjacentEdges;
  };

  CanvasRenderer.prototype.getArrowWidth = CanvasRenderer.prototype.getArrowHeight = function(edgeWidth) {
    var cache = this.arrowWidthCache = this.arrowWidthCache || {};

    var cachedVal = cache[edgeWidth];
    if( cachedVal ){
      return cachedVal;
    }

    cachedVal =  Math.max(Math.pow(edgeWidth * 13.37, 0.9), 29);
    cache[edgeWidth] = cachedVal;

    return cachedVal;
  };


})( cytoscape );

;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

// Draw edge
  CanvasRenderer.prototype.drawEdge = function(context, edge, drawOverlayInstead) {
    var rs = edge._private.rscratch;
    var usePaths = CanvasRenderer.usePaths();

    // if bezier ctrl pts can not be calculated, then die
    if( rs.badBezier || ( (rs.edgeType === 'bezier' || rs.edgeType === 'straight') && isNaN(rs.startX)) ){ // extra isNaN() for safari 7.1 b/c it mangles ctrlpt calcs
      return;
    }

    var style = edge._private.style;
    
    // Edge line width
    if (style['width'].pxValue <= 0) {
      return;
    }

    var overlayPadding = style['overlay-padding'].pxValue;
    var overlayOpacity = style['overlay-opacity'].value;
    var overlayColor = style['overlay-color'].value;

    // Edge color & opacity
    if( drawOverlayInstead ){

      if( overlayOpacity === 0 ){ // exit early if no overlay
        return;
      }

      this.strokeStyle(context, overlayColor[0], overlayColor[1], overlayColor[2], overlayOpacity);
      context.lineCap = 'round';

      if( edge._private.rscratch.edgeType == 'self' && !usePaths ){
        context.lineCap = 'butt';
      }

    } else {
      var lineColor = style['line-color'].value;

      this.strokeStyle(context, lineColor[0], lineColor[1], lineColor[2], style.opacity.value);
      
      context.lineCap = 'butt'; 
    }
    
    var startNode, endNode, source, target;
    source = startNode = edge._private.source;
    target = endNode = edge._private.target;

    var targetPos = target._private.position;
    var targetW = target.width();
    var targetH = target.height();
    var sourcePos = source._private.position;
    var sourceW = source.width();
    var sourceH = source.height();


    var edgeWidth = style['width'].pxValue + (drawOverlayInstead ? 2 * overlayPadding : 0);
    var lineStyle = drawOverlayInstead ? 'solid' : style['line-style'].value;
    context.lineWidth = edgeWidth;
    
    if( rs.edgeType !== 'haystack' ){
      //this.findEndpoints(edge);
    }
    
    if( rs.edgeType === 'haystack' ){
      var radius = style['haystack-radius'].value;
      var halfRadius = radius/2; // b/c have to half width/height

      this.drawStyledEdge(
        edge, 
        context, 
        rs.haystackPts = [
          rs.source.x * sourceW * halfRadius + sourcePos.x,
          rs.source.y * sourceH * halfRadius + sourcePos.y,
          rs.target.x * targetW * halfRadius + targetPos.x,
          rs.target.y * targetH * halfRadius + targetPos.y
        ],
        lineStyle,
        edgeWidth
      );
    } else if (rs.edgeType === 'self') {
      
      var details = edge._private.rscratch;
      var points = [details.startX, details.startY, details.cp2ax,
        details.cp2ay, details.selfEdgeMidX, details.selfEdgeMidY,
        details.selfEdgeMidX, details.selfEdgeMidY,
        details.cp2cx, details.cp2cy, details.endX, details.endY];

      var details = edge._private.rscratch;
      this.drawStyledEdge(edge, context, points, lineStyle, edgeWidth);
      
    } else if (rs.edgeType === 'straight') {
      
      var nodeDirectionX = endNode._private.position.x - startNode._private.position.x;
      var nodeDirectionY = endNode._private.position.y - startNode._private.position.y;
      
      var edgeDirectionX = rs.endX - rs.startX;
      var edgeDirectionY = rs.endY - rs.startY;
      
      if (nodeDirectionX * edgeDirectionX
        + nodeDirectionY * edgeDirectionY < 0) {
        
        rs.straightEdgeTooShort = true;  
      } else {
        
        var details = rs;
        this.drawStyledEdge(edge, context, [details.startX, details.startY,
                                      details.endX, details.endY],
                                      lineStyle,
                                      edgeWidth);
        
        rs.straightEdgeTooShort = false;  
      }  
    } else {
      
      var details = rs;
      
      this.drawStyledEdge(edge, context, [details.startX, details.startY,
        details.cp2x, details.cp2y, details.endX, details.endY],
        lineStyle,
        edgeWidth);
      
    }
    
    if( rs.edgeType === 'haystack' ){
      this.drawArrowheads(context, edge, drawOverlayInstead);
    } else if ( rs.noArrowPlacement !== true && rs.startX !== undefined ){
      this.drawArrowheads(context, edge, drawOverlayInstead);
    }

  };
  
  
  CanvasRenderer.prototype.drawStyledEdge = function(
      edge, context, pts, type, width) {

    // 3 points given -> assume Bezier
    // 2 -> assume straight
    
    var rs = edge._private.rscratch;
    var canvasCxt = context;
    var path;
    var pathCacheHit = false;
    var usePaths = CanvasRenderer.usePaths();


    if( usePaths ){

      var pathCacheKey = pts;
      var keyLengthMatches = rs.pathCacheKey && pathCacheKey.length === rs.pathCacheKey.length;
      var keyMatches = keyLengthMatches;

      for( var i = 0; keyMatches && i < pathCacheKey.length; i++ ){
        if( rs.pathCacheKey[i] !== pathCacheKey[i] ){
          keyMatches = false;
        }
      }

      if( keyMatches ){
        path = context = rs.pathCache;
        pathCacheHit = true;
      } else {
        path = context = new Path2D();
        rs.pathCacheKey = pathCacheKey;
        rs.pathCache = path;
      }

    }

    if( canvasCxt.setLineDash ){ // for very outofdate browsers
      switch( type ){
        case 'dotted':
          canvasCxt.setLineDash([ 1, 1 ]);
          break;

        case 'dashed':
          canvasCxt.setLineDash([ 6, 3 ]);
          break;

        case 'solid':
          canvasCxt.setLineDash([ ]);
          break;
      }
    }

    if( !pathCacheHit ){
      if( context.beginPath ){ context.beginPath(); }
      context.moveTo(pts[0], pts[1]);
      
      if (pts.length === 3 * 2) { // bezier
        context.quadraticCurveTo(pts[2], pts[3], pts[4], pts[5]);
      } else if( pts.length === 3 * 2 * 2 ){ // double bezier loop
        context.quadraticCurveTo(pts[2], pts[3], pts[4], pts[5]);
        context.quadraticCurveTo(pts[8], pts[9], pts[10], pts[11]);
      } else { // line
        context.lineTo(pts[2], pts[3]);
      }
    }

    context = canvasCxt;
    if( usePaths ){
      context.stroke( path );
    } else {
      context.stroke();
    }
  
    // reset any line dashes
    if( context.setLineDash ){ // for very outofdate browsers
      context.setLineDash([ ]);
    }

  };

  CanvasRenderer.prototype.drawArrowheads = function(context, edge, drawOverlayInstead) {
    if( drawOverlayInstead ){ return; } // don't do anything for overlays 

    var rs = edge._private.rscratch;
    var self = this;
    var isHaystack = rs.edgeType === 'haystack';

    // Displacement gives direction for arrowhead orientation
    var dispX, dispY;
    var startX, startY, endX, endY;

    var srcPos = edge.source().position();
    var tgtPos = edge.target().position();

    if( isHaystack ){
      startX = rs.haystackPts[0];
      startY = rs.haystackPts[1];
      endX = rs.haystackPts[2];
      endY = rs.haystackPts[3];
    } else {
      startX = rs.arrowStartX;
      startY = rs.arrowStartY;
      endX = rs.arrowEndX;
      endY = rs.arrowEndY;
    }

    var style = edge._private.style;
    
    function drawArrowhead( prefix, x, y, dispX, dispY ){
      var arrowShape = style[prefix + '-arrow-shape'].value;

      if( arrowShape === 'none' ){
        return;
      }

      var gco = context.globalCompositeOperation;

      context.globalCompositeOperation = 'destination-out';
      
      self.fillStyle(context, 255, 255, 255, 1);


      var arrowClearFill = style[prefix + '-arrow-fill'].value === 'hollow' ? 'both' : 'filled';
      var arrowFill = style[prefix + '-arrow-fill'].value;

      if( arrowShape === 'half-triangle-overshot' ){
        arrowFill = 'hollow';
        arrowClearFill = 'hollow';
      }

      self.drawArrowShape( edge, prefix, context, 
        arrowClearFill, style['width'].pxValue, style[prefix + '-arrow-shape'].value, 
        x, y, dispX, dispY
      );

      context.globalCompositeOperation = gco;

      var color = style[prefix + '-arrow-color'].value;
      self.fillStyle(context, color[0], color[1], color[2], style.opacity.value);

      self.drawArrowShape( edge, prefix, context, 
        arrowFill, style['width'].pxValue, style[prefix + '-arrow-shape'].value, 
        x, y, dispX, dispY
      );
    }

    dispX = startX - srcPos.x;
    dispY = startY - srcPos.y;

    if( !isHaystack && !isNaN(startX) && !isNaN(startY) && !isNaN(dispX) && !isNaN(dispY) ){
      drawArrowhead( 'source', startX, startY, dispX, dispY );

    } else {
      // window.badArrow = true;
      // debugger;
    }
    
    var midX = rs.midX;
    var midY = rs.midY;

    if( isHaystack ){
      midX = ( startX + endX )/2;
      midY = ( startY + endY )/2;
    }

    dispX = startX - endX;
    dispY = startY - endY;

    if( rs.edgeType === 'self' ){
      dispX = 1;
      dispY = -1;
    }

    if( !isNaN(midX) && !isNaN(midY) ){
      drawArrowhead( 'mid-target', midX, midY, dispX, dispY );
    }

    dispX *= -1;
    dispY *= -1;

    if( !isNaN(midX) && !isNaN(midY) ){
      drawArrowhead( 'mid-source', midX, midY, dispX, dispY );
    }
    
    dispX = endX - tgtPos.x;
    dispY = endY - tgtPos.y;
    
    if( !isHaystack && !isNaN(endX) && !isNaN(endY) && !isNaN(dispX) && !isNaN(dispY) ){
      drawArrowhead( 'target', endX, endY, dispX, dispY );
    }
  };
  
  // Draw arrowshape
  CanvasRenderer.prototype.drawArrowShape = function(edge, arrowType, context, fill, edgeWidth, shape, x, y, dispX, dispY) {
    var usePaths = CanvasRenderer.usePaths();
    var rs = edge._private.rscratch;
    var pathCacheHit = false;
    var path;
    var canvasContext = context;
    var translation = { x: x, y: y };

    // Negative of the angle
    var angle = Math.asin(dispY / (Math.sqrt(dispX * dispX + dispY * dispY)));
  
    if (dispX < 0) {
      angle = angle + Math.PI / 2;
    } else {
      angle = - (Math.PI / 2 + angle);
    }
    
    var size = this.getArrowWidth( edgeWidth );
    var shapeImpl = CanvasRenderer.arrowShapes[shape];

    // context.translate(x, y);

    if( usePaths ){
      var pathCacheKey = size + '$' + shape + '$' + angle + '$' + x + '$' + y;
      rs.arrowPathCacheKey = rs.arrowPathCacheKey || {};
      rs.arrowPathCache = rs.arrowPathCache || {};

      var alreadyCached = rs.arrowPathCacheKey[arrowType] === pathCacheKey;
      if( alreadyCached ){
        path = context = rs.arrowPathCache[arrowType];
        pathCacheHit = true;
      } else {
        path = context = new Path2D();
        rs.arrowPathCacheKey[arrowType] = pathCacheKey;
        rs.arrowPathCache[arrowType] = path;
      }
    }

    if( context.beginPath ){ context.beginPath(); }

    if( !pathCacheHit ){
      shapeImpl.draw(context, size, angle, translation);
    }
    
    if( !shapeImpl.leavePathOpen && context.closePath ){
      context.closePath();
    }

    context = canvasContext;

    if( fill === 'filled' || fill === 'both' ){
      if( usePaths ){
        context.fill( path );
      } else {
        context.fill();
      }
    }

    if( fill === 'hollow' || fill === 'both' ){
      context.lineWidth = ( shapeImpl.matchEdgeWidth ? edgeWidth : 1 );
      context.lineJoin = 'miter';

      if( usePaths ){
        context.stroke( path );
      } else {
        context.stroke();
      }
      
    }

    // context.translate(-x, -y);
  };

})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  CanvasRenderer.prototype.getCachedImage = function(url, onLoad) {
    var r = this;
    var imageCache = r.imageCache = r.imageCache || {};

    if( imageCache[url] && imageCache[url].image ){
      return imageCache[url].image;
    }
    
    var cache = imageCache[url] = imageCache[url] || {};

    var image = cache.image = new Image();
    image.addEventListener('load', onLoad);
    image.src = url;
    
    return image;
  };
    
  CanvasRenderer.prototype.drawInscribedImage = function(context, img, node) {
    var r = this;
    var nodeX = node._private.position.x;
    var nodeY = node._private.position.y;
    var style = node._private.style;
    var fit = style['background-fit'].value;
    var xPos = style['background-position-x'];
    var yPos = style['background-position-y'];
    var repeat = style['background-repeat'].value;
    var nodeW = node.width();
    var nodeH = node.height();
    var rs = node._private.rscratch;
    var clip = style['background-clip'].value;
    var shouldClip = clip === 'node';
    var imgOpacity = style['background-image-opacity'].value;
    
    var w = img.width;
    var h = img.height;

    if( w === 0 || h === 0 ){
      return; // no point in drawing empty image (and chrome is broken in this case)
    }

    if( fit === 'contain' ){
      var scale = Math.min( nodeW/w, nodeH/h );

      w *= scale;
      h *= scale;

    } else if( fit === 'cover' ){
      var scale = Math.max( nodeW/w, nodeH/h );

      w *= scale;
      h *= scale;
    }

    var x = (nodeX - nodeW/2); // left
    if( xPos.units === '%' ){
      x += (nodeW - w) * xPos.value/100;
    } else {
      x += xPos.pxValue;
    }

    var y = (nodeY - nodeH/2); // top
    if( yPos.units === '%' ){
      y += (nodeH - h) * yPos.value/100;
    } else {
      y += yPos.pxValue;
    }

    if( rs.pathCache ){
      x -= nodeX;
      y -= nodeY;

      nodeX = 0;
      nodeY = 0;
    }

    var gAlpha = context.globalAlpha;

    context.globalAlpha = imgOpacity;

    if( repeat === 'no-repeat' ){

      if( shouldClip ){
        context.save();

        if( rs.pathCache ){
          context.clip( rs.pathCache );
        } else {
          CanvasRenderer.nodeShapes[r.getNodeShape(node)].drawPath(
            context,
            nodeX, nodeY, 
            nodeW, nodeH);

          context.clip();
        }
      }

      context.drawImage( img, 0, 0, img.width, img.height, x, y, w, h );

      if( shouldClip ){
        context.restore();
      }
    } else {
      var pattern = context.createPattern( img, repeat );
      context.fillStyle = pattern;

      CanvasRenderer.nodeShapes[r.getNodeShape(node)].drawPath(
          context,
          nodeX, nodeY, 
          nodeW, nodeH);

        context.translate(x, y);
        context.fill();
        context.translate(-x, -y);
    }

    context.globalAlpha = gAlpha;
    
  };

  
})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  // Draw edge text
  CanvasRenderer.prototype.drawEdgeText = function(context, edge) {
    var text = edge._private.style['content'].strValue;

    if( !text || text.match(/^\s+$/) ){
      return;
    }

    if( this.hideEdgesOnViewport && (this.dragData.didDrag || this.pinching || this.hoverData.dragging || this.data.wheel || this.swipePanning) ){ return; } // save cycles on pinching

    var computedSize = edge._private.style['font-size'].pxValue * edge.cy().zoom();
    var minSize = edge._private.style['min-zoomed-font-size'].pxValue;

    if( computedSize < minSize ){
      return;
    }
  
    // Calculate text draw position
    
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    
    // this.recalculateEdgeLabelProjection( edge );
    
    var rs = edge._private.rscratch;
    this.drawText(context, edge, rs.labelX, rs.labelY);
  };

  // Draw node text
  CanvasRenderer.prototype.drawNodeText = function(context, node) {
    var text = node._private.style['content'].strValue;

    if ( !text || text.match(/^\s+$/) ) {
      return;
    }

    var computedSize = node._private.style['font-size'].pxValue * node.cy().zoom();
    var minSize = node._private.style['min-zoomed-font-size'].pxValue;

    if( computedSize < minSize ){
      return;
    }
      
    // this.recalculateNodeLabelProjection( node );

    var textHalign = node._private.style['text-halign'].strValue;
    var textValign = node._private.style['text-valign'].strValue;
    var rs = node._private.rscratch;

    switch( textHalign ){
      case 'left':
        context.textAlign = 'right';
        break;

      case 'right':
        context.textAlign = 'left';
        break;

      default: // e.g. center
        context.textAlign = 'center';
    }

    switch( textValign ){
      case 'top':
        context.textBaseline = 'bottom';
        break;

      case 'bottom':
        context.textBaseline = 'top';
        break;

      default: // e.g. center
        context.textBaseline = 'middle';
    }

    this.drawText(context, node, rs.labelX, rs.labelY);
  };
  
  CanvasRenderer.prototype.getFontCache = function(context){
    var cache;

    this.fontCaches = this.fontCaches || [];

    for( var i = 0; i < this.fontCaches.length; i++ ){
      cache = this.fontCaches[i];

      if( cache.context === context ){
        return cache;
      }
    }

    cache = {
      context: context
    };
    this.fontCaches.push(cache);

    return cache;
  };

  // set up canvas context with font
  // returns transformed text string
  CanvasRenderer.prototype.setupTextStyle = function( context, element ){
    // Font style
    var parentOpacity = element.effectiveOpacity();
    var style = element._private.style;
    var labelStyle = style['font-style'].strValue;
    var labelSize = style['font-size'].pxValue + 'px';
    var labelFamily = style['font-family'].strValue;
    var labelWeight = style['font-weight'].strValue;
    var opacity = style['text-opacity'].value * style['opacity'].value * parentOpacity;
    var outlineOpacity = style['text-outline-opacity'].value * opacity;
    var color = style['color'].value;
    var outlineColor = style['text-outline-color'].value;

    var fontCacheKey = element._private.fontKey;
    var cache = this.getFontCache(context);

    if( cache.key !== fontCacheKey ){
      context.font = labelStyle + ' ' + labelWeight + ' ' + labelSize + ' ' + labelFamily;

      cache.key = fontCacheKey;
    }

    var text = String(style['content'].value);
    var textTransform = style['text-transform'].value;
    
    if (textTransform == 'none') {
    } else if (textTransform == 'uppercase') {
      text = text.toUpperCase();
    } else if (textTransform == 'lowercase') {
      text = text.toLowerCase();
    }
    
    // Calculate text draw position based on text alignment
    
    // so text outlines aren't jagged
    context.lineJoin = 'round';

    this.fillStyle(context, color[0], color[1], color[2], opacity);
    
    this.strokeStyle(context, outlineColor[0], outlineColor[1], outlineColor[2], outlineOpacity);

    return text;
  };

  // Draw text
  CanvasRenderer.prototype.drawText = function(context, element, textX, textY) {
    var style = element._private.style;
    var parentOpacity = element.effectiveOpacity();
    if( parentOpacity === 0 ){ return; }

    var text = this.setupTextStyle( context, element );
    
    if ( text != null && !isNaN(textX) && !isNaN(textY) ) {
     
      var lineWidth = 2  * style['text-outline-width'].value; // *2 b/c the stroke is drawn centred on the middle
      if (lineWidth > 0) {
        context.lineWidth = lineWidth;
        context.strokeText(text, textX, textY);
      }

      context.fillText(text, textX, textY);
    }
  };

  
})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  // Draw node
  CanvasRenderer.prototype.drawNode = function(context, node, drawOverlayInstead) {

    var r = this;
    var nodeWidth, nodeHeight;
    var style = node._private.style;
    var rs = node._private.rscratch;
    
    var usePaths = CanvasRenderer.usePaths();
    var canvasContext = context;
    var path;
    var pathCacheHit = false;

    var overlayPadding = style['overlay-padding'].pxValue;
    var overlayOpacity = style['overlay-opacity'].value;
    var overlayColor = style['overlay-color'].value;

    if( drawOverlayInstead && overlayOpacity === 0 ){ // exit early if drawing overlay but none to draw
      return;
    }

    var parentOpacity = node.effectiveOpacity();
    if( parentOpacity === 0 ){ return; }

    nodeWidth = this.getNodeWidth(node);
    nodeHeight = this.getNodeHeight(node);
    
    context.lineWidth = style['border-width'].pxValue;

    if( drawOverlayInstead === undefined || !drawOverlayInstead ){

      // Node color & opacity

      var bgColor = style['background-color'].value;
      var borderColor = style['border-color'].value;
      var borderStyle = style['border-style'].value;

      this.fillStyle(context, bgColor[0], bgColor[1], bgColor[2], style['background-opacity'].value * style['opacity'].value * parentOpacity);
      
      this.strokeStyle(context, borderColor[0], borderColor[1], borderColor[2], style['border-opacity'].value * style['opacity'].value * parentOpacity);

      context.lineJoin = 'miter'; // so borders are square with the node shape

      if( context.setLineDash ){ // for very outofdate browsers
        switch( borderStyle ){
          case 'dotted':
            context.setLineDash([ 1, 1 ]);
            break;

          case 'dashed':
            context.setLineDash([ 4, 2 ]);
            break;

          case 'solid':
          case 'double':
            context.setLineDash([ ]);
            break;
        }
      }

      //var image = this.getCachedImage('url');
      
      var url = style['background-image'].value[2] ||
        style['background-image'].value[1];
      
      var styleShape = style['shape'].strValue;

      var pos = node._private.position;

      if( usePaths ){
        var pathCacheKey = styleShape + '$' + nodeWidth +'$' + nodeHeight;

        context.translate( pos.x, pos.y );

        if( rs.pathCacheKey === pathCacheKey ){
          path = context = rs.pathCache;
          pathCacheHit = true;
        } else {
          path = context = new Path2D();
          rs.pathCacheKey = pathCacheKey;
          rs.pathCache = path;
        }
      }

      if( !pathCacheHit ){

        var npos = pos;

        if( usePaths ){
          npos = {
            x: 0,
            y: 0
          };
        }

        CanvasRenderer.nodeShapes[this.getNodeShape(node)].drawPath(
              context,
              npos.x,
              npos.y,
              nodeWidth,
              nodeHeight);
      }

      context = canvasContext;

      if( usePaths ){
        context.fill( path );
      } else {
        context.fill();
      }

      if (url !== undefined) {
        
        // get image, and if not loaded then ask to redraw when later loaded
        var image = this.getCachedImage(url, function(){
          r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
          r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;
          
          r.redraw();
        });
        
        if( image.complete ){
          this.drawInscribedImage(context, image, node);
        }
        
      } 
      
      var darkness = style['background-blacken'].value;
      var borderWidth = style['border-width'].pxValue;

      if( this.hasPie(node) ){
        this.drawPie(context, node);

        // redraw path for blacken and border
        if( darkness !== 0 || borderWidth !== 0 ){

          if( !usePaths ){
            CanvasRenderer.nodeShapes[this.getNodeShape(node)].drawPath(
                context,
                pos.x,
                pos.y,
                nodeWidth,
                nodeHeight);
          }
        }
      }

      if( darkness > 0 ){
        this.fillStyle(context, 0, 0, 0, darkness);

        if( usePaths ){
          context.fill( path );
        } else {
          context.fill();
        }
        
      } else if( darkness < 0 ){
        this.fillStyle(context, 255, 255, 255, -darkness);
        
        if( usePaths ){
          context.fill( path );
        } else {
          context.fill();
        }
      }

      // Border width, draw border
      if (borderWidth > 0) {

        if( usePaths ){
          context.stroke( path );
        } else {
          context.stroke();
        }

        if( borderStyle === 'double' ){
          context.lineWidth = style['border-width'].pxValue/3;

          var gco = context.globalCompositeOperation;
          context.globalCompositeOperation = 'destination-out';

          if( usePaths ){
            context.stroke( path );
          } else {
            context.stroke();
          }

          context.globalCompositeOperation = gco;
        }

      }

      if( usePaths ){
        context.translate( -pos.x, -pos.y );
      }

      // reset in case we changed the border style
      if( context.setLineDash ){ // for very outofdate browsers
        context.setLineDash([ ]);
      }

    // draw the overlay
    } else {

      if( overlayOpacity > 0 ){
        this.fillStyle(context, overlayColor[0], overlayColor[1], overlayColor[2], overlayOpacity);

        CanvasRenderer.nodeShapes['roundrectangle'].drawPath(
          context,
          node._private.position.x,
          node._private.position.y,
          nodeWidth + overlayPadding * 2,
          nodeHeight + overlayPadding * 2
        );

        context.fill();
      }
    }

  };

  // does the node have at least one pie piece?
  CanvasRenderer.prototype.hasPie = function(node){
    node = node[0]; // ensure ele ref
    
    return node._private.hasPie;
  };

  CanvasRenderer.prototype.drawPie = function(context, node){
    node = node[0]; // ensure ele ref

    var pieSize = node._private.style['pie-size'];
    var nodeW = this.getNodeWidth( node );
    var nodeH = this.getNodeHeight( node );
    var x = node._private.position.x;
    var y = node._private.position.y;
    var radius = Math.min( nodeW, nodeH ) / 2; // must fit in node
    var lastPercent = 0; // what % to continue drawing pie slices from on [0, 1]
    var usePaths = CanvasRenderer.usePaths();

    if( usePaths ){
      x = 0;
      y = 0;
    }

    if( pieSize.units === '%' ){
      radius = radius * pieSize.value / 100;
    } else if( pieSize.pxValue !== undefined ){
      radius = pieSize.pxValue / 2;
    }

    for( var i = 1; i <= $$.style.pieBackgroundN; i++ ){ // 1..N
      var size = node._private.style['pie-' + i + '-background-size'].value;
      var color = node._private.style['pie-' + i + '-background-color'].value;
      var opacity = node._private.style['pie-' + i + '-background-opacity'].value;
      var percent = size / 100; // map integer range [0, 100] to [0, 1]
      var angleStart = 1.5 * Math.PI + 2 * Math.PI * lastPercent; // start at 12 o'clock and go clockwise
      var angleDelta = 2 * Math.PI * percent;
      var angleEnd = angleStart + angleDelta;

      // ignore if
      // - zero size
      // - we're already beyond the full circle
      // - adding the current slice would go beyond the full circle
      if( size === 0 || lastPercent >= 1 || lastPercent + percent > 1 ){
        continue;
      }

      context.beginPath();
      context.moveTo(x, y);
      context.arc( x, y, radius, angleStart, angleEnd );
      context.closePath();

      this.fillStyle(context, color[0], color[1], color[2], opacity);

      context.fill();

      lastPercent += percent;
    }

  };

  
})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  // var isFirefox = typeof InstallTrigger !== 'undefined';

  CanvasRenderer.prototype.getPixelRatio = function(){ 
    var context = this.data.contexts[0];

    if( this.forcedPixelRatio != null ){
      return this.forcedPixelRatio;
    }

    var backingStore = context.backingStorePixelRatio ||
      context.webkitBackingStorePixelRatio ||
      context.mozBackingStorePixelRatio ||
      context.msBackingStorePixelRatio ||
      context.oBackingStorePixelRatio ||
      context.backingStorePixelRatio || 1;

    //console.log(window.devicePixelRatio, backingStore);

    // if( isFirefox ){ // because ff can't scale canvas properly
    //   return 1;
    // }

    return (window.devicePixelRatio || 1) / backingStore;
  };

  CanvasRenderer.prototype.paintCache = function(context){
    var caches = this.paintCaches = this.paintCaches || [];
    var needToCreateCache = true;
    var cache;

    for(var i = 0; i < caches.length; i++ ){
      cache = caches[i];

      if( cache.context === context ){
        needToCreateCache = false;
        break;
      }
    }

    if( needToCreateCache ){
      cache = {
        context: context
      };
      caches.push( cache );
    }

    return cache;
  };

  CanvasRenderer.prototype.fillStyle = function(context, r, g, b, a){
    context.fillStyle = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
    
    // turn off for now, seems context does its own caching

    // var cache = this.paintCache(context);

    // var fillStyle = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';

    // if( cache.fillStyle !== fillStyle ){
    //   context.fillStyle = cache.fillStyle = fillStyle;
    // }
  };

  CanvasRenderer.prototype.strokeStyle = function(context, r, g, b, a){
    context.strokeStyle = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
    
    // turn off for now, seems context does its own caching

    // var cache = this.paintCache(context);

    // var strokeStyle = 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';

    // if( cache.strokeStyle !== strokeStyle ){
    //   context.strokeStyle = cache.strokeStyle = strokeStyle;
    // }
  };

  // Resize canvas
  CanvasRenderer.prototype.matchCanvasSize = function(container) {
    var data = this.data;
    var width = container.clientWidth;
    var height = container.clientHeight;
    var pixelRatio = this.getPixelRatio();
    var canvasWidth = width * pixelRatio;
    var canvasHeight = height * pixelRatio;
    var canvas;

    if( canvasWidth === this.canvasWidth && canvasHeight === this.canvasHeight ){
      return; // save cycles if same
    }

    this.fontCaches = null; // resizing resets the style

    var canvasContainer = data.canvasContainer;
    canvasContainer.style.width = width + 'px';
    canvasContainer.style.height = height + 'px';

    for (var i = 0; i < CanvasRenderer.CANVAS_LAYERS; i++) {

      canvas = data.canvases[i];
      
      if (canvas.width !== canvasWidth || canvas.height !== canvasHeight) {
        
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;

        canvas.style.width = width + 'px';
        canvas.style.height = height + 'px';
      }
    }
    
    for (var i = 0; i < CanvasRenderer.BUFFER_COUNT; i++) {
      
      canvas = data.bufferCanvases[i];
      
      if (canvas.width !== canvasWidth || canvas.height !== canvasHeight) {
        
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;

        canvas.style.width = width + 'px';
        canvas.style.height = height + 'px';
      }
    }

    this.textureMult = 1;
    if( pixelRatio <= 1 ){
      canvas = data.bufferCanvases[ CanvasRenderer.TEXTURE_BUFFER ];

      this.textureMult = 2;
      canvas.width = canvasWidth * this.textureMult;
      canvas.height = canvasHeight * this.textureMult;
    }

    this.canvasWidth = canvasWidth;
    this.canvasHeight = canvasHeight;

  };

  CanvasRenderer.prototype.renderTo = function( cxt, zoom, pan, pxRatio ){
    this.redraw({
      forcedContext: cxt,
      forcedZoom: zoom,
      forcedPan: pan,
      drawAllLayers: true,
      forcedPxRatio: pxRatio
    });
  };

  CanvasRenderer.prototype.timeToRender = function(){
    return this.redrawTotalTime / this.redrawCount;
  };

  CanvasRenderer.minRedrawLimit = 1000/60; // people can't see much better than 60fps
  CanvasRenderer.maxRedrawLimit = 1000;  // don't cap max b/c it's more important to be responsive than smooth
  CanvasRenderer.motionBlurDelay = 100;

  // Redraw frame
  CanvasRenderer.prototype.redraw = function( options ) {
    options = options || {};

    // console.log('redraw');

    var forcedContext = options.forcedContext;
    var drawAllLayers = options.drawAllLayers;
    var drawOnlyNodeLayer = options.drawOnlyNodeLayer;
    var forcedZoom = options.forcedZoom;
    var forcedPan = options.forcedPan;
    var r = this;
    var pixelRatio = options.forcedPxRatio === undefined ? this.getPixelRatio() : options.forcedPxRatio;
    var cy = r.data.cy; var data = r.data; 
    var needDraw = data.canvasNeedsRedraw;
    var motionBlur = options.motionBlur !== undefined ? options.motionBlur : r.motionBlur;
    motionBlur = motionBlur && !forcedContext && r.motionBlurEnabled;

    if( motionBlur && r.motionBlurTimeout ){
      clearTimeout( r.motionBlurTimeout );
    }

    if( !forcedContext && this.redrawTimeout ){
      clearTimeout( this.redrawTimeout );
    }
    this.redrawTimeout = null;

    if( this.averageRedrawTime === undefined ){ this.averageRedrawTime = 0; }

    var minRedrawLimit = CanvasRenderer.minRedrawLimit; 
    var maxRedrawLimit = CanvasRenderer.maxRedrawLimit;

    var redrawLimit = this.averageRedrawTime; // estimate the ideal redraw limit based on how fast we can draw
    redrawLimit = minRedrawLimit > redrawLimit ? minRedrawLimit : redrawLimit;
    redrawLimit = redrawLimit < maxRedrawLimit ? redrawLimit : maxRedrawLimit;

    //console.log('--\nideal: %i; effective: %i', this.averageRedrawTime, redrawLimit);

    if( this.lastDrawTime === undefined ){ this.lastDrawTime = 0; }

    var nowTime = +new Date();
    var timeElapsed = nowTime - this.lastDrawTime;
    var callAfterLimit = timeElapsed >= redrawLimit;

    if( !forcedContext ){
      if( !callAfterLimit || this.currentlyDrawing ){
        // console.log('-- skip');

        // we have new things to draw but we're busy, so try again when possibly free
        this.redrawTimeout = setTimeout(function(){
          r.redraw();
        }, redrawLimit);
        return;
      }

      this.lastDrawTime = nowTime;
      this.currentlyDrawing = true;
    }


    var startTime = +new Date();

    //console.log('-- redraw --')


    function drawToContext(){ 
      // startTime = +new Date();
      // console.profile('draw' + startTime)
      var edges = r.getCachedEdges();
      var coreStyle = cy.style()._private.coreStyle;
      
      var zoom = cy.zoom();
      var effectiveZoom = forcedZoom !== undefined ? forcedZoom : zoom;
      var pan = cy.pan();
      var effectivePan = {
        x: pan.x,
        y: pan.y
      };

      if( forcedPan ){
        effectivePan = forcedPan;
      }

      // apply pixel ratio

      effectiveZoom *= pixelRatio;
      effectivePan.x *= pixelRatio;
      effectivePan.y *= pixelRatio;
      
      var eles = {
        drag: {
          nodes: [],
          edges: [],
          eles: []
        },
        nondrag: {
          nodes: [],
          edges: [],
          eles: []
        }
      };

      function setContextTransform(context, clear){
        context.setTransform(1, 0, 0, 1, 0, 0);

        if( clear === 'motionBlur' ){
          var gco = context.globalCompositeOperation;

          context.globalCompositeOperation = 'destination-out';
          r.fillStyle( context, 255, 255, 255, 0.666 );
          context.fillRect(0, 0, r.canvasWidth, r.canvasHeight);

          context.globalCompositeOperation = gco;
        } else if( !forcedContext && (clear === undefined || clear) ){
          context.clearRect(0, 0, r.canvasWidth, r.canvasHeight);
        }
        
        if( !drawAllLayers ){
          context.translate(effectivePan.x, effectivePan.y);
          context.scale(effectiveZoom, effectiveZoom);
        }
        if( forcedPan ){
          context.translate(forcedPan.x, forcedPan.y);
        } 
        if( forcedZoom ){
          context.scale(forcedZoom, forcedZoom);
        }
      }

      var textureDraw = r.textureOnViewport && !forcedContext && (r.pinching || r.hoverData.dragging || r.swipePanning || r.data.wheelZooming);

      if( textureDraw ){

        var bb;

        if( !r.textureCache ){
          r.textureCache = {};

          bb = r.textureCache.bb = cy.elements().boundingBox();

          r.textureCache.texture = r.data.bufferCanvases[ CanvasRenderer.TEXTURE_BUFFER ];

          var cxt = r.data.bufferContexts[ CanvasRenderer.TEXTURE_BUFFER ];

          cxt.setTransform(1, 0, 0, 1, 0, 0);
          cxt.clearRect(0, 0, r.canvasWidth * r.textureMult, r.canvasHeight * r.textureMult);
          
          r.redraw({
            forcedContext: cxt,
            drawOnlyNodeLayer: true,
            forcedPxRatio: pixelRatio * r.textureMult
          });

          var vp = r.textureCache.viewport = {
            zoom: cy.zoom(),
            pan: cy.pan(),
            width: r.canvasWidth,
            height: r.canvasHeight
          };

          vp.mpan = {
            x: (0 - vp.pan.x)/vp.zoom,
            y: (0 - vp.pan.y)/vp.zoom
          };
        }

        needDraw[CanvasRenderer.DRAG] = false;
        needDraw[CanvasRenderer.NODE] = false;

        var context = data.contexts[CanvasRenderer.NODE];

        var texture = r.textureCache.texture;
        var vp = r.textureCache.viewport;
        bb = r.textureCache.bb;

        context.setTransform(1, 0, 0, 1, 0, 0);
        context.clearRect(0, 0, vp.width, vp.height);

        var outsideBgColor = coreStyle['outside-texture-bg-color'].value;
        var outsideBgOpacity = coreStyle['outside-texture-bg-opacity'].value;
        r.fillStyle( context, outsideBgColor[0], outsideBgColor[1], outsideBgColor[2], outsideBgOpacity );
        context.fillRect( 0, 0, vp.width, vp.height );

        var zoom = cy.zoom();
        
        setContextTransform( context, false );

        context.clearRect( vp.mpan.x, vp.mpan.y, vp.width/vp.zoom/pixelRatio, vp.height/vp.zoom/pixelRatio );
        context.drawImage( texture, vp.mpan.x, vp.mpan.y, vp.width/vp.zoom/pixelRatio, vp.height/vp.zoom/pixelRatio );

      } else if( r.textureOnViewport && !forcedContext ){ // clear the cache since we don't need it
        r.textureCache = null;
      }

      var vpManip = (r.pinching || r.hoverData.dragging || r.swipePanning || r.data.wheelZooming || r.hoverData.draggingEles);
      var hideEdges = r.hideEdgesOnViewport && vpManip;
      var hideLabels = r.hideLabelsOnViewport && vpManip;

      if (needDraw[CanvasRenderer.DRAG] || needDraw[CanvasRenderer.NODE] || drawAllLayers || drawOnlyNodeLayer) {
        //NB : VERY EXPENSIVE

        if( hideEdges ){ 
        } else {
          r.findEdgeControlPoints(edges);
        }

        var zEles = r.getCachedZSortedEles();
        var extent = cy.extent();

        for (var i = 0; i < zEles.length; i++) {
          var ele = zEles[i];
          var list;
          var bb = forcedContext ? null : ele.boundingBox();
          var insideExtent = forcedContext ? true : $$.math.boundingBoxesIntersect( extent, bb );

          if( !insideExtent ){ continue; } // no need to render

          if ( ele._private.rscratch.inDragLayer ) {
            list = eles.drag;
          } else {
            list = eles.nondrag;
          }

          list.eles.push( ele );
        }

      }
      
      
      function drawElements( list, context ){
        var eles = list.eles;

        for( var i = 0; i < eles.length; i++ ){
          var ele = eles[i];

          if( ele.isNode() ){
            r.drawNode(context, ele);

            if( !hideLabels ){
              r.drawNodeText(context, ele);
            }

            r.drawNode(context, ele, true);
          } else if( !hideEdges ) {
            r.drawEdge(context, ele);

            if( !hideLabels ){
              r.drawEdgeText(context, ele);
            }

            r.drawEdge(context, ele, true);
          }
          
          
        }

      }

      var nodeLayerNeedsMotionClear = needDraw[CanvasRenderer.DRAG] && !needDraw[CanvasRenderer.NODE] && motionBlur && !r.clearedNodeLayerForMotionBlur;
      if( nodeLayerNeedsMotionClear ){ r.clearedNodeLayerForMotionBlur = true; }

      if( needDraw[CanvasRenderer.NODE] || drawAllLayers || drawOnlyNodeLayer || nodeLayerNeedsMotionClear ){
        // console.log('redrawing node layer');
        
        var context = forcedContext || data.contexts[CanvasRenderer.NODE];

        setContextTransform( context, motionBlur && !nodeLayerNeedsMotionClear ? 'motionBlur' : undefined );
        drawElements(eles.nondrag, context);
        
        if( !drawAllLayers ){
          needDraw[CanvasRenderer.NODE] = false; 
        }
      }
      
      if ( !drawOnlyNodeLayer && (needDraw[CanvasRenderer.DRAG] || drawAllLayers) ) {
        
        var context = forcedContext || data.contexts[CanvasRenderer.DRAG];
        
        setContextTransform( context, motionBlur ? 'motionBlur' : undefined );
        drawElements(eles.drag, context);
        
        if( !drawAllLayers ){
          needDraw[CanvasRenderer.DRAG] = false;
        }
      }
      
      if( r.showFps || (!drawOnlyNodeLayer && (needDraw[CanvasRenderer.SELECT_BOX] && !drawAllLayers)) ) {
        // console.log('redrawing selection box');
        
        var context = forcedContext || data.contexts[CanvasRenderer.SELECT_BOX];

        setContextTransform( context );

        if( data.select[4] == 1 && r.hoverData.selecting ){
          var zoom = data.cy.zoom();
          var borderWidth = coreStyle['selection-box-border-width'].value / zoom;
          
          context.lineWidth = borderWidth;
          context.fillStyle = "rgba(" 
            + coreStyle['selection-box-color'].value[0] + ","
            + coreStyle['selection-box-color'].value[1] + ","
            + coreStyle['selection-box-color'].value[2] + ","
            + coreStyle['selection-box-opacity'].value + ")";
          
          context.fillRect(
            data.select[0],
            data.select[1],
            data.select[2] - data.select[0],
            data.select[3] - data.select[1]);
          
          if (borderWidth > 0) {
            context.strokeStyle = "rgba(" 
              + coreStyle['selection-box-border-color'].value[0] + ","
              + coreStyle['selection-box-border-color'].value[1] + ","
              + coreStyle['selection-box-border-color'].value[2] + ","
              + coreStyle['selection-box-opacity'].value + ")";
            
            context.strokeRect(
              data.select[0],
              data.select[1],
              data.select[2] - data.select[0],
              data.select[3] - data.select[1]);
          }
        }

        if( data.bgActivePosistion && !r.hoverData.selecting ){
          var zoom = data.cy.zoom();
          var pos = data.bgActivePosistion;

          context.fillStyle = "rgba(" 
            + coreStyle['active-bg-color'].value[0] + ","
            + coreStyle['active-bg-color'].value[1] + ","
            + coreStyle['active-bg-color'].value[2] + ","
            + coreStyle['active-bg-opacity'].value + ")";

          context.beginPath();
          context.arc(pos.x, pos.y, coreStyle['active-bg-size'].pxValue / zoom, 0, 2 * Math.PI); 
          context.fill();
        }
        
        var timeToRender = r.averageRedrawTime;
        if( r.showFps && timeToRender ){
          timeToRender = Math.round( timeToRender );
          var fps = Math.round(1000/timeToRender);

          context.setTransform(1, 0, 0, 1, 0, 0);

          //context.font = '20px helvetica';
          context.fillStyle = 'rgba(255, 0, 0, 0.75)';
          context.strokeStyle = 'rgba(255, 0, 0, 0.75)';
          context.lineWidth = 1;
          context.fillText( '1 frame = ' + timeToRender + ' ms = ' + fps + ' fps', 0, 20);

          var maxFps = 60;
          context.strokeRect(0, 30, 250, 20);
          context.fillRect(0, 30, 250 * Math.min(fps/maxFps, 1), 20);
        }

        if( !drawAllLayers ){
          needDraw[CanvasRenderer.SELECT_BOX] = false; 
        }
      }


      var endTime = +new Date();

      if( r.averageRedrawTime === undefined ){
        r.averageRedrawTime = endTime - startTime;
      }

      if( r.redrawCount === undefined ){
        r.redrawCount = 0;
      }

      r.redrawCount++;

      if( r.redrawTotalTime === undefined ){
        r.redrawTotalTime = 0;
      }

      r.redrawTotalTime += endTime - startTime;
      r.lastRedrawTime = endTime - startTime;

      // use a weighted average with a bias from the previous average so we don't spike so easily
      r.averageRedrawTime = r.averageRedrawTime/2 + (endTime - startTime)/2;
      //console.log('actual: %i, average: %i', endTime - startTime, this.averageRedrawTime);

      r.currentlyDrawing = false;

      // console.profileEnd('draw' + startTime)

      if( r.clearingMotionBlur ){
        r.clearingMotionBlur = false;
        r.motionBlurCleared = true;
        r.motionBlur = true;
      }

      if( motionBlur ){ 
        r.motionBlurTimeout = setTimeout(function(){
          r.motionBlurTimeout = null;
          // console.log('motion blur clear');

          r.clearedNodeLayerForMotionBlur = false;
          r.motionBlur = false;
          r.clearingMotionBlur = true;

          needDraw[CanvasRenderer.NODE] = true; 
          needDraw[CanvasRenderer.DRAG] = true; 

          r.redraw();
        }, CanvasRenderer.motionBlurDelay);
      }
    } // draw to context

    if( !forcedContext ){
      $$.util.requestAnimationFrame(drawToContext); // makes direct renders to screen a bit more responsive
    } else {
      drawToContext();
    }

    if( !forcedContext && !r.initrender ){
      r.initrender = true;
      cy.trigger('initrender');
    }
    
  };

})( cytoscape );

;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  // @O Polygon drawing
  CanvasRenderer.prototype.drawPolygonPath = function(
    context, x, y, width, height, points) {

    var halfW = width / 2;
    var halfH = height / 2;

    if( context.beginPath ){ context.beginPath(); }

    context.moveTo( x + halfW * points[0], y + halfH * points[1] );

    for (var i = 1; i < points.length / 2; i++) {
      context.lineTo( x + halfW * points[i * 2], y + halfH * points[i * 2 + 1] );
    }
    
    context.closePath();
  };
  
  CanvasRenderer.prototype.drawPolygon = function(
    context, x, y, width, height, points) {

    // Draw path
    this.drawPolygonPath(context, x, y, width, height, points);
    
    // Fill path
    context.fill();
  };
  
  // Round rectangle drawing
  CanvasRenderer.prototype.drawRoundRectanglePath = function(
    context, x, y, width, height, radius) {
    
    var halfWidth = width / 2;
    var halfHeight = height / 2;
    var cornerRadius = $$.math.getRoundRectangleRadius(width, height);
    
    if( context.beginPath ){ context.beginPath(); }
    
    // Start at top middle
    context.moveTo(x, y - halfHeight);
    // Arc from middle top to right side
    context.arcTo(x + halfWidth, y - halfHeight, x + halfWidth, y, cornerRadius);
    // Arc from right side to bottom
    context.arcTo(x + halfWidth, y + halfHeight, x, y + halfHeight, cornerRadius);
    // Arc from bottom to left side
    context.arcTo(x - halfWidth, y + halfHeight, x - halfWidth, y, cornerRadius);
    // Arc from left side to topBorder
    context.arcTo(x - halfWidth, y - halfHeight, x, y - halfHeight, cornerRadius);
    // Join line
    context.lineTo(x, y - halfHeight);
    
    
    context.closePath();
  };
  
  CanvasRenderer.prototype.drawRoundRectangle = function(
    context, x, y, width, height, radius) {
    
    this.drawRoundRectanglePath(context, x, y, width, height, radius);
    
    context.fill();
  };


})( cytoscape );

;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  CanvasRenderer.prototype.createBuffer = function(w, h) {
    var buffer = document.createElement('canvas');
    buffer.width = w;
    buffer.height = h;
    
    return [buffer, buffer.getContext('2d')];
  };

  CanvasRenderer.prototype.bufferCanvasImage = function( options ){
    var data = this.data;
    var cy = data.cy;
    var bb = cy.elements().boundingBox();
    var width = options.full ? Math.ceil(bb.w) : this.data.container.clientWidth;
    var height = options.full ? Math.ceil(bb.h) : this.data.container.clientHeight;
    var scale = 1;

    if( options.scale !== undefined ){
      width *= options.scale;
      height *= options.scale;

      scale = options.scale;
    }

    var buffCanvas = document.createElement('canvas');

    buffCanvas.width = width;
    buffCanvas.height = height;

    buffCanvas.style.width = width + 'px';
    buffCanvas.style.height = height + 'px';

    var buffCxt = buffCanvas.getContext('2d');

    // Rasterize the layers, but only if container has nonzero size
    if (width > 0 && height > 0) {

      buffCxt.clearRect( 0, 0, width, height );

      if( options.bg ){
        buffCxt.fillStyle = options.bg;
        buffCxt.rect( 0, 0, width, height );
        buffCxt.fill();
      }

      buffCxt.globalCompositeOperation = 'source-over';

      if( options.full ){ // draw the full bounds of the graph
        this.redraw({
          forcedContext: buffCxt,
          drawAllLayers: true,
          forcedZoom: scale,
          forcedPan: { x: -bb.x1*scale, y: -bb.y1*scale },
          forcedPxRatio: 1
        });
      } else { // draw the current view
        var cyPan = cy.pan();
        var pan = {
          x: cyPan.x * scale,
          y: cyPan.y * scale
        };
        var zoom = cy.zoom() * scale;

        this.redraw({
          forcedContext: buffCxt,
          drawAllLayers: true,
          forcedZoom: zoom,
          forcedPan: pan,
          forcedPxRatio: 1
        });
      }
    }

    return buffCanvas;
  }; 

  CanvasRenderer.prototype.png = function( options ){
    return this.bufferCanvasImage( options ).toDataURL('image/png');
  };

})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');

  CanvasRenderer.prototype.registerBinding = function(target, event, handler, useCapture){
    this.bindings.push({
      target: target,
      event: event,
      handler: handler,
      useCapture: useCapture
    });

    target.addEventListener(event, handler, useCapture);
  };

  CanvasRenderer.prototype.nodeIsDraggable = function(node) {
    if (node._private.style['opacity'].value !== 0
      && node._private.style['visibility'].value == 'visible'
      && node._private.style['display'].value == 'element'
      && !node.locked()
      && node.grabbable() ) {

      return true;
    }
    
    return false;
  };

  CanvasRenderer.prototype.load = function() {
    var r = this;

    var getDragListIds = function(opts){
      var listHasId;

      if( opts.addToList && r.data.cy.hasCompoundNodes() ){ // only needed for compound graphs
        if( !opts.addToList.hasId ){ // build ids lookup if doesn't already exist
          opts.addToList.hasId = {};

          for( var i = 0; i < opts.addToList.length; i++ ){
            var ele = opts.addToList[i];

            opts.addToList.hasId[ ele.id() ] = true;
          }
        }

        listHasId = opts.addToList.hasId;
      }

      return listHasId || {};
    };

    // helper function to determine which child nodes and inner edges
    // of a compound node to be dragged as well as the grabbed and selected nodes
    var addDescendantsToDrag = function(node, opts){
      if( !node._private.cy.hasCompoundNodes() ){
        return;
      }

      var listHasId = getDragListIds( opts );

      var innerNodes = node.descendants();

      // TODO do not drag hidden children & children of hidden children?
      for( var i = 0; i < innerNodes.size(); i++ ){
        var iNode = innerNodes[i];
        var _p = iNode._private;

        if( opts.inDragLayer ){
          _p.rscratch.inDragLayer = true;
        }

        if( opts.addToList && !listHasId[ iNode.id() ] ){
          opts.addToList.push( iNode );
          listHasId[ iNode.id() ] = true;

          _p.grabbed = true; 
        }

        var edges = _p.edges;
        for( var j = 0; opts.inDragLayer && j < edges.length; j++ ){
          edges[j]._private.rscratch.inDragLayer = true;
        }
      }
    };

    // adds the given nodes, and its edges to the drag layer
    var addNodeToDrag = function(node, opts){

      var _p = node._private;
      var listHasId = getDragListIds( opts );

      if( opts.inDragLayer ){
        _p.rscratch.inDragLayer = true;
      }

      if( opts.addToList && !listHasId[ node.id() ] ){
        opts.addToList.push( node );
        listHasId[ node.id() ] = true;

        _p.grabbed = true; 
      }

      var edges = _p.edges;
      for( var i = 0; opts.inDragLayer && i < edges.length; i++ ){
        edges[i]._private.rscratch.inDragLayer = true;
      }

      addDescendantsToDrag( node, opts ); // always add to drag

      // also add nodes and edges related to the topmost ancestor
      updateAncestorsInDragLayer( node, {
        inDragLayer: true
      } );
    };

    // helper function to determine which ancestor nodes and edges should go
    // to the drag layer (or should be removed from drag layer).
    var updateAncestorsInDragLayer = function(node, opts) {
      // find top-level parent
      var parent = node;

      if( !node._private.cy.hasCompoundNodes() ){
        return;
      }

      while( parent.parent().nonempty() ){
        parent = parent.parent()[0];
      }

      // no parent node: no nodes to add to the drag layer
      if( parent == node ){
        return;
      }

      var nodes = parent
        .descendants()
        .add( parent )
        .not( node )
        .not( node.descendants() )
      ;

      var edges = nodes.connectedEdges();

      var listHasId = getDragListIds( opts );

      for( var i = 0; i < nodes.size(); i++ ){
        if( opts.inDragLayer !== undefined ){
          nodes[i]._private.rscratch.inDragLayer = opts.inDragLayer;
        }

        if( opts.addToList && !listHasId[ nodes[i].id() ] ){
          opts.addToList.push( nodes[i] );
          listHasId[ nodes[i].id() ] = true;

          nodes[i]._private.grabbed = true;
        }
      }

      for( var j = 0; opts.inDragLayer !== undefined && j < edges.length; j++ ) {
        edges[j]._private.rscratch.inDragLayer = opts.inDragLayer;
      }
    };

    if( typeof MutationObserver !== 'undefined' ){
      r.removeObserver = new MutationObserver(function( mutns ){
        for( var i = 0; i < mutns.length; i++ ){
          var mutn = mutns[i];
          var rNodes = mutn.removedNodes;

          if( rNodes ){ for( var j = 0; j < rNodes.length; j++ ){
            var rNode = rNodes[j];

            if( rNode === r.data.container ){
              r.destroy();
              break;
            }
          } }
        }
      });

      r.removeObserver.observe( r.data.container.parentNode, { childList: true } );
    } else {
      r.registerBinding(r.data.container, 'DOMNodeRemoved', function(e){
        r.destroy();
      });
    }



    // auto resize
    r.registerBinding(window, 'resize', $$.util.debounce( function(e) {
      r.invalidateContainerClientCoordsCache();

      r.matchCanvasSize(r.data.container);
      r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
      r.redraw();
    }, 100 ) );

    var invalCtnrBBOnScroll = function(domEle){
      r.registerBinding(domEle, 'scroll', function(e){
        r.invalidateContainerClientCoordsCache();
      } );
    };

    var bbCtnr = r.data.cy.container();

    for( ;; ){
      
      invalCtnrBBOnScroll( bbCtnr );

      if( bbCtnr.parentNode ){
        bbCtnr = bbCtnr.parentNode;
      } else {
        break;
      }
      
    }

    // stop right click menu from appearing on cy
    r.registerBinding(r.data.container, 'contextmenu', function(e){
      e.preventDefault();
    });

    var inBoxSelection = function(){
      return r.data.select[4] !== 0;
    };

    // Primary key
    r.registerBinding(r.data.container, 'mousedown', function(e) { 
      e.preventDefault();
      r.hoverData.capture = true;
      r.hoverData.which = e.which;
      
      var cy = r.data.cy; 
      var pos = r.projectIntoViewport(e.clientX, e.clientY);
      var select = r.data.select;
      var near = r.findNearestElement(pos[0], pos[1], true);
      var draggedElements = r.dragData.possibleDragElements;

      r.hoverData.mdownPos = pos;

      var checkForTaphold = function(){
        r.hoverData.tapholdCancelled = false;

        clearTimeout( r.hoverData.tapholdTimeout );

        r.hoverData.tapholdTimeout = setTimeout(function(){

          if( r.hoverData.tapholdCancelled ){
            return;
          } else {
            var ele = r.hoverData.down;

            if( ele ){
              ele.trigger( new $$.Event(e, {
                type: 'taphold',
                cyPosition: { x: pos[0], y: pos[1] }
              }) );
            } else {
              cy.trigger( new $$.Event(e, {
                type: 'taphold',
                cyPosition: { x: pos[0], y: pos[1] }
              }) );
            }
          }

        }, r.tapholdDuration);
      };

      // Right click button
      if( e.which == 3 ){

        r.hoverData.cxtStarted = true;

        var cxtEvt = new $$.Event(e, {
          type: 'cxttapstart', 
          cyPosition: { x: pos[0], y: pos[1] } 
        });

        if( near ){
          near.activate();
          near.trigger( cxtEvt );

          r.hoverData.down = near;
        } else {
          cy.trigger( cxtEvt );
        }

        r.hoverData.downTime = (new Date()).getTime();
        r.hoverData.cxtDragged = false;

      // Primary button
      } else if (e.which == 1) {
        
        if( near ){
          near.activate();
        }

        // Element dragging
        {
          // If something is under the cursor and it is draggable, prepare to grab it
          if (near != null) {

            if( r.nodeIsDraggable(near) ){

              var grabEvent = new $$.Event(e, {
                type: 'grab',
                cyPosition: { x: pos[0], y: pos[1] }
              });

              if ( near.isNode() && !near.selected() ){

                draggedElements = r.dragData.possibleDragElements = [];
                addNodeToDrag( near, { addToList: draggedElements } );

                near.trigger(grabEvent);

              } else if ( near.isNode() && near.selected() ){
                draggedElements = r.dragData.possibleDragElements = [  ];

                var selectedNodes = cy.$(function(){ return this.isNode() && this.selected(); });

                for( var i = 0; i < selectedNodes.length; i++ ){

                  // Only add this selected node to drag if it is draggable, eg. has nonzero opacity
                  if( r.nodeIsDraggable( selectedNodes[i] ) ){
                    addNodeToDrag( selectedNodes[i], { addToList: draggedElements } );
                  }
                }

                near.trigger( grabEvent );
              }

              r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
              r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

            }
            
            near
              .trigger(new $$.Event(e, {
                type: 'mousedown',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapstart',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmousedown',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
            ;
            
          } else if (near == null) {
            cy
              .trigger(new $$.Event(e, {
                type: 'mousedown',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapstart',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmousedown',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
            ;
          }
          
          r.hoverData.down = near;
          r.hoverData.downTime = (new Date()).getTime();

        }
      
        // Selection box
        if ( near == null || near.isEdge() ) {
          select[4] = 1;
          var timeUntilActive = Math.max( 0, CanvasRenderer.panOrBoxSelectDelay - (+new Date() - r.hoverData.downTime) );

          clearTimeout( r.bgActiveTimeout );

          if( cy.boxSelectionEnabled() || ( near && near.isEdge() ) ){
            r.bgActiveTimeout = setTimeout(function(){
              if( near ){
                near.unactivate();
              }

              r.data.bgActivePosistion = {
                x: pos[0],
                y: pos[1]
              };

              checkForTaphold();

              r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
      
              r.redraw();
            }, timeUntilActive);
          } else {
            r.data.bgActivePosistion = {
              x: pos[0],
              y: pos[1]
            };

            checkForTaphold();

            r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
    
            r.redraw();
          }
          
        }
      
      } 
      
      // Initialize selection box coordinates
      select[0] = select[2] = pos[0];
      select[1] = select[3] = pos[1];
      
    }, false);
    
    r.registerBinding(window, 'mousemove', $$.util.throttle( function(e) {
      var preventDefault = false;
      var capture = r.hoverData.capture;

      // save cycles if mouse events aren't to be captured
      if ( !capture ){
        var containerPageCoords = r.findContainerClientCoords();

        if (e.clientX > containerPageCoords[0] && e.clientX < containerPageCoords[0] + r.canvasWidth
          && e.clientY > containerPageCoords[1] && e.clientY < containerPageCoords[1] + r.canvasHeight
        ) {
          // inside container bounds so OK
        } else {
          return;
        }

        var cyContainer = r.data.container;
        var target = e.target;
        var tParent = target.parentNode;
        var containerIsTarget = false;

        while( tParent ){
          if( tParent === cyContainer ){
            containerIsTarget = true;
            break;
          }

          tParent = tParent.parentNode;
        }

        if( !containerIsTarget ){ return; } // if target is outisde cy container, then this event is not for us
      }

      var cy = r.data.cy;
      var zoom = cy.zoom();
      var pan = cy.pan();
      var pos = r.projectIntoViewport(e.clientX, e.clientY);
      var select = r.data.select;
      
      var near = null;
      if( !r.hoverData.draggingEles ){
        near = r.findNearestElement(pos[0], pos[1], true);
      }
      var last = r.hoverData.last;
      var down = r.hoverData.down;
      
      var disp = [pos[0] - select[2], pos[1] - select[3]];

      var draggedElements = r.dragData.possibleDragElements;

      var dx = select[2] - select[0];
      var dx2 = dx * dx;
      var dy = select[3] - select[1];
      var dy2 = dy * dy;
      var dist2 = dx2 + dy2;
      var rdist2 = dist2 * zoom * zoom;

      r.hoverData.tapholdCancelled = true;

      var updateDragDelta = function(){
        var dragDelta = r.hoverData.dragDelta = r.hoverData.dragDelta || [];

        if( dragDelta.length === 0 ){
          dragDelta.push(0);
          dragDelta.push(0);
        } else {
          dragDelta[0] += disp[0];
          dragDelta[1] += disp[1];
        }
      };
      

      preventDefault = true;

      // Mousemove event
      {
        if (near != null) {
          near
            .trigger(new $$.Event(e, {
              type: 'mousemove',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'vmousemove',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'tapdrag',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
          ;
          
        } else if (near == null) {
          cy
            .trigger(new $$.Event(e, {
              type: 'mousemove',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'vmousemove',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'tapdrag',
              cyPosition: { x: pos[0], y: pos[1] }
            }))
          ;
        }

      }

      // trigger context drag if rmouse down
      if( r.hoverData.which === 3 ){
        var cxtEvt = new $$.Event(e, {
          type: 'cxtdrag',
          cyPosition: { x: pos[0], y: pos[1] }
        });

        if( down ){
          down.trigger( cxtEvt );
        } else {
          cy.trigger( cxtEvt );
        }

        r.hoverData.cxtDragged = true;

        if( !r.hoverData.cxtOver || near !== r.hoverData.cxtOver ){

          if( r.hoverData.cxtOver ){
            r.hoverData.cxtOver.trigger( new $$.Event(e, {
              type: 'cxtdragout',
              cyPosition: { x: pos[0], y: pos[1] }
            }) );

            // console.log('cxtdragout ' + r.hoverData.cxtOver.id());
          }

          r.hoverData.cxtOver = near;

          if( near ){
            near.trigger( new $$.Event(e, {
              type: 'cxtdragover',
              cyPosition: { x: pos[0], y: pos[1] }
            }) );

            // console.log('cxtdragover ' + near.id());
          }

        }

      // Check if we are drag panning the entire graph
      } else if (r.hoverData.dragging) {
        preventDefault = true;

        if( cy.panningEnabled() && cy.userPanningEnabled() ){
          var deltaP;

          if( r.hoverData.justStartedPan ){
            var mdPos = r.hoverData.mdownPos;

            deltaP = {
              x: ( pos[0] - mdPos[0] ) * zoom,
              y: ( pos[1] - mdPos[1] ) * zoom
            };

            r.hoverData.justStartedPan = false;

          } else {
            deltaP = {
              x: disp[0] * zoom,
              y: disp[1] * zoom
            };

          }

          cy.panBy( deltaP );
          
        }
        
        // Needs reproject due to pan changing viewport
        pos = r.projectIntoViewport(e.clientX, e.clientY);

      // Checks primary button down & out of time & mouse not moved much
      } else if(
          select[4] == 1 && (down == null || down.isEdge())
          && ( !cy.boxSelectionEnabled() || (+new Date() - r.hoverData.downTime >= CanvasRenderer.panOrBoxSelectDelay) )
          //&& (Math.abs(select[3] - select[1]) + Math.abs(select[2] - select[0]) < 4)
          && !r.hoverData.selecting
          && rdist2 >= r.tapThreshold2
          && cy.panningEnabled() && cy.userPanningEnabled()
      ){
        r.hoverData.dragging = true;
        r.hoverData.selecting = false;
        r.hoverData.justStartedPan = true;
        select[4] = 0;

      } else {
        // deactivate bg on box selection
        if (cy.boxSelectionEnabled() && Math.pow(select[2] - select[0], 2) + Math.pow(select[3] - select[1], 2) > 7 && select[4]){
          clearTimeout( r.bgActiveTimeout );
          r.data.bgActivePosistion = undefined;
          r.hoverData.selecting = true;

          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
          r.redraw();
        }
        
        if( down && down.isEdge() && down.active() ){ down.unactivate(); }

        if (near != last) {
          
          if (last) {
            last.trigger( new $$.Event(e, {
              type: 'mouseout',
              cyPosition: { x: pos[0], y: pos[1] }
            }) ); 

            last.trigger( new $$.Event(e, {
              type: 'tapdragout',
              cyPosition: { x: pos[0], y: pos[1] }
            }) ); 
          }
          
          if (near) {
            near.trigger( new $$.Event(e, {
              type: 'mouseover',
              cyPosition: { x: pos[0], y: pos[1] }
            }) ); 

            near.trigger( new $$.Event(e, {
              type: 'tapdragover',
              cyPosition: { x: pos[0], y: pos[1] }
            }) ); 
          }
          
          r.hoverData.last = near;
        }

        if( down && down.isNode() && r.nodeIsDraggable(down) ){

          if( rdist2 >= r.tapThreshold2 ){ // then drag

            var justStartedDrag = !r.dragData.didDrag;

            if( justStartedDrag ) {
              r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
            }

            r.dragData.didDrag = true; // indicate that we actually did drag the node

            var toTrigger = [];

            for( var i = 0; i < draggedElements.length; i++ ){
              var dEle = draggedElements[i];

              // now, add the elements to the drag layer if not done already
              if( !r.hoverData.draggingEles ){ 
                addNodeToDrag( dEle, { inDragLayer: true } );
              }

              // Locked nodes not draggable, as well as non-visible nodes
              if( dEle.isNode() && r.nodeIsDraggable(dEle) && dEle.grabbed() ){
                var dPos = dEle._private.position;

                toTrigger.push( dEle );
                
                if( $$.is.number(disp[0]) && $$.is.number(disp[1]) ){
                  dPos.x += disp[0];
                  dPos.y += disp[1];

                  if( justStartedDrag ){
                    var dragDelta = r.hoverData.dragDelta;

                    if( $$.is.number(dragDelta[0]) && $$.is.number(dragDelta[1]) ){
                      dPos.x += dragDelta[0];
                      dPos.y += dragDelta[1];
                    }
                  }
                }

              }
            }

            r.hoverData.draggingEles = true;
            
            var tcol = (new $$.Collection(cy, toTrigger));

            tcol.updateCompoundBounds();
            tcol.trigger('position drag');
            
            r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;
            r.redraw();

          } else { // otherwise save drag delta for when we actually start dragging so the relative grab pos is constant
            updateDragDelta();
          }
        }

        // prevent the dragging from triggering text selection on the page
        preventDefault = true;
      }
      
      select[2] = pos[0]; select[3] = pos[1];
      
      if( preventDefault ){ 
        if(e.stopPropagation) e.stopPropagation();
          if(e.preventDefault) e.preventDefault();
          return false;
        }
    }, 1000/30, { trailing: true }), false);
    
    r.registerBinding(window, 'mouseup', function(e) {
      // console.log('--\nmouseup', e)

      var capture = r.hoverData.capture;
      if (!capture) { return; }
      r.hoverData.capture = false;
    
      var cy = r.data.cy; var pos = r.projectIntoViewport(e.clientX, e.clientY); var select = r.data.select;
      var near = r.findNearestElement(pos[0], pos[1], true); 
      var draggedElements = r.dragData.possibleDragElements; var down = r.hoverData.down;
      var shiftDown = e.shiftKey;
      
      if( r.data.bgActivePosistion ){
        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
        r.redraw();
      }

      r.data.bgActivePosistion = undefined; // not active bg now
      clearTimeout( r.bgActiveTimeout );

      r.hoverData.cxtStarted = false;
      r.hoverData.draggingEles = false;
      r.hoverData.selecting = false;

      if( down ){
        down.unactivate();
      }

      if( r.hoverData.which === 3 ){
        var cxtEvt = new $$.Event(e, {
          type: 'cxttapend',
          cyPosition: { x: pos[0], y: pos[1] }
        });

        if( down ){
          down.trigger( cxtEvt );
        } else {
          cy.trigger( cxtEvt );
        }

        if( !r.hoverData.cxtDragged ){
          var cxtTap = new $$.Event(e, {
            type: 'cxttap',
            cyPosition: { x: pos[0], y: pos[1] }
          });

          if( down ){
            down.trigger( cxtTap );
          } else {
            cy.trigger( cxtTap );
          }
        }

        r.hoverData.cxtDragged = false;
        r.hoverData.which = null;

      // if not right mouse
      } else {

        // Deselect all elements if nothing is currently under the mouse cursor and we aren't dragging something
        if ( (down == null) // not mousedown on node
          && !r.dragData.didDrag // didn't move the node around
          && !(Math.pow(select[2] - select[0], 2) + Math.pow(select[3] - select[1], 2) > 7 && select[4]) // not box selection
          && !r.hoverData.dragging // not panning
        ) {

          cy.$(function(){
            return this.selected();
          }).unselect();
          
          if (draggedElements.length > 0) {
            r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
          }
          
          r.dragData.possibleDragElements = draggedElements = [];
        }
      
        
        // Mouseup event
        {
          // console.log('trigger mouseup et al');

          if (near != null) {
            near
              .trigger(new $$.Event(e, {
                type: 'mouseup',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapend',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmouseup',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
            ;
          } else if (near == null) {
            cy
              .trigger(new $$.Event(e, {
                type: 'mouseup',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapend',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmouseup',
                cyPosition: { x: pos[0], y: pos[1] }
              }))
            ;
          }
        }
        
        // Click event
        {
          // console.log('trigger click et al');

          if (Math.pow(select[2] - select[0], 2) + Math.pow(select[3] - select[1], 2) === 0) {
            if (near != null) {
              near
                .trigger( new $$.Event(e, {
                  type: 'click',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
                .trigger( new $$.Event(e, {
                  type: 'tap',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
                .trigger( new $$.Event(e, {
                  type: 'vclick',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
              ;
            } else if (near == null) {
              cy
                .trigger( new $$.Event(e, {
                  type: 'click',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
                .trigger( new $$.Event(e, {
                  type: 'tap',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
                .trigger( new $$.Event(e, {
                  type: 'vclick',
                  cyPosition: { x: pos[0], y: pos[1] }
                }) )
              ;
            }
          }
        }

        // Single selection
        if (near == down && !r.dragData.didDrag) {
          if (near != null && near._private.selectable) {
            
            // console.log('single selection')

            if( r.hoverData.dragging ){
              // if panning, don't change selection state
            } else if( cy.selectionType() === 'additive' || shiftDown ){
              if( near.selected() ){
                near.unselect();
              } else {
                near.select();
              }
            } else {
              if( !shiftDown ){
                cy.$(':selected').not( near ).unselect();
                near.select();
              }               
            }
            
            r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
            
          }
      
        } 
        
        if ( cy.boxSelectionEnabled() &&  Math.pow(select[2] - select[0], 2) + Math.pow(select[3] - select[1], 2) > 7 && select[4] ) {         
          var newlySelected = [];
          var box = r.getAllInBox( select[0], select[1], select[2], select[3] );

          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

          if( box.length > 0 ) { 
            r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
          }

          for( var i = 0; i < box.length; i++ ){ 
            if( box[i]._private.selectable ){
              newlySelected.push( box[i] );
            }
          }

          var newlySelCol = new $$.Collection( cy, newlySelected );

          if( cy.selectionType() === 'additive' ){
            newlySelCol.select();
          } else {
            if( !shiftDown ){
              cy.$(':selected').not( newlySelCol ).unselect();
            }

            newlySelCol.select();
          }

          // always need redraw in case eles unselectable
          r.redraw();
          
        }
        
        // Cancel drag pan
        if( r.hoverData.dragging ){
          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
          r.redraw();
        }

        r.hoverData.dragging = false;
        
        if (!select[4]) {
          // console.log('free at end', draggedElements)

          r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true; 
          r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
          
          for (var i=0; i < draggedElements.length; i++) {
            
            if(draggedElements[i]._private.group === 'nodes') { 
              draggedElements[i]._private.rscratch.inDragLayer = false;
              draggedElements[i]._private.grabbed = false;
              
              var sEdges = draggedElements[i]._private.edges;
              for( var j = 0; j < sEdges.length; j++ ){ sEdges[j]._private.rscratch.inDragLayer = false; }

              // for compound nodes, also remove related nodes and edges from the drag layer
              updateAncestorsInDragLayer(draggedElements[i], { inDragLayer: false });
              
            } else if( draggedElements[i]._private.group === 'edges' ){
              draggedElements[i]._private.rscratch.inDragLayer = false;
            }
            
          }

          if( down ){ down.trigger('free'); }

  //        draggedElements = r.dragData.possibleDragElements = [];
          
        }
      
      } // else not right mouse

      select[4] = 0; r.hoverData.down = null;
      
      //r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true; 
      
//      console.log('mu', pos[0], pos[1]);
//      console.log('ss', select);
      
      r.dragData.didDrag = false;
      r.hoverData.dragDelta = [];
      
    }, false);

    var wheelHandler = function(e) { 
      if( r.scrollingPage ){ return; } // while scrolling, ignore wheel-to-zoom

      var cy = r.data.cy;
      var pos = r.projectIntoViewport(e.clientX, e.clientY);
      var rpos = [pos[0] * cy.zoom() + cy.pan().x,
                    pos[1] * cy.zoom() + cy.pan().y];
      
      if( r.hoverData.draggingEles || r.hoverData.dragging || r.hoverData.cxtStarted || inBoxSelection() ){ // if pan dragging or cxt dragging, wheel movements make no zoom
        e.preventDefault();
        return;
      }

      if( cy.panningEnabled() && cy.userPanningEnabled() && cy.zoomingEnabled() && cy.userZoomingEnabled() ){
        e.preventDefault();
        
        r.data.wheelZooming = true;
        clearTimeout( r.data.wheelTimeout );
        r.data.wheelTimeout = setTimeout(function(){
          r.data.wheelZooming = false;

          r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
          r.redraw();
        }, 150);

        var diff = e.deltaY / -250 || e.wheelDeltaY / 1000 || e.wheelDelta / 1000;
        diff = diff * r.wheelSensitivity;

        var needsWheelFix = e.deltaMode === 1;
        if( needsWheelFix ){ // fixes slow wheel events on ff/linux and ff/windows
          diff *= 33;
        }

        cy.zoom({
          level: cy.zoom() * Math.pow(10, diff),
          renderedPosition: { x: rpos[0], y: rpos[1] }
        });
      }

    };
    
    // Functions to help with whether mouse wheel should trigger zooming
    // --
    r.registerBinding(r.data.container, 'wheel', wheelHandler, true);

    // disable nonstandard wheel events
    // r.registerBinding(r.data.container, 'mousewheel', wheelHandler, true);
    // r.registerBinding(r.data.container, 'DOMMouseScroll', wheelHandler, true);
    // r.registerBinding(r.data.container, 'MozMousePixelScroll', wheelHandler, true); // older firefox

    r.registerBinding(window, 'scroll', function(e){
      r.scrollingPage = true;

      clearTimeout( r.scrollingPageTimeout );
      r.scrollingPageTimeout = setTimeout(function(){
        r.scrollingPage = false;
      }, 250);
    }, true);
    
    // Functions to help with handling mouseout/mouseover on the Cytoscape container
          // Handle mouseout on Cytoscape container
    r.registerBinding(r.data.container, 'mouseout', function(e) { 
      var pos = r.projectIntoViewport(e.clientX, e.clientY);

      r.data.cy.trigger(new $$.Event(e, {
        type: 'mouseout',
        cyPosition: { x: pos[0], y: pos[1] }
      }));
    }, false);
    
    r.registerBinding(r.data.container, 'mouseover', function(e) { 
      var pos = r.projectIntoViewport(e.clientX, e.clientY);

      r.data.cy.trigger(new $$.Event(e, {
        type: 'mouseover',
        cyPosition: { x: pos[0], y: pos[1] }
      }));
    }, false);
    
    var f1x1, f1y1, f2x1, f2y1; // starting points for pinch-to-zoom
    var distance1, distance1Sq; // initial distance between finger 1 and finger 2 for pinch-to-zoom
    var center1, modelCenter1; // center point on start pinch to zoom
    var offsetLeft, offsetTop;
    var containerWidth, containerHeight;
    var twoFingersStartInside;

    var distance = function(x1, y1, x2, y2){
      return Math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) );
    };

    var distanceSq = function(x1, y1, x2, y2){
      return (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
    };

    r.registerBinding(r.data.container, 'touchstart', function(e) {

      clearTimeout( this.threeFingerSelectTimeout );

      if( e.target !== r.data.link ){
        e.preventDefault();
      }
    
      r.touchData.capture = true;
      r.data.bgActivePosistion = undefined;

      var cy = r.data.cy; 
      var nodes = r.getCachedNodes();
      var edges = r.getCachedEdges();
      var now = r.touchData.now;
      var earlier = r.touchData.earlier;
      
      if (e.touches[0]) { var pos = r.projectIntoViewport(e.touches[0].clientX, e.touches[0].clientY); now[0] = pos[0]; now[1] = pos[1]; }
      if (e.touches[1]) { var pos = r.projectIntoViewport(e.touches[1].clientX, e.touches[1].clientY); now[2] = pos[0]; now[3] = pos[1]; }
      if (e.touches[2]) { var pos = r.projectIntoViewport(e.touches[2].clientX, e.touches[2].clientY); now[4] = pos[0]; now[5] = pos[1]; }
    

      // record starting points for pinch-to-zoom
      if( e.touches[1] ){

        // anything in the set of dragged eles should be released
        var release = function( eles ){
          for( var i = 0; i < eles.length; i++ ){
            eles[i]._private.grabbed = false;
            eles[i]._private.rscratch.inDragLayer = false;
            if( eles[i].active() ){ eles[i].unactivate(); }
          }
        };
        release(nodes);
        release(edges);

        var offsets = r.findContainerClientCoords();
        offsetLeft = offsets[0];
        offsetTop = offsets[1];
        containerWidth = offsets[2];
        containerHeight = offsets[3];

        f1x1 = e.touches[0].clientX - offsetLeft;
        f1y1 = e.touches[0].clientY - offsetTop;
        
        f2x1 = e.touches[1].clientX - offsetLeft;
        f2y1 = e.touches[1].clientY - offsetTop;

        twoFingersStartInside = 
             0 <= f1x1 && f1x1 <= containerWidth
          && 0 <= f2x1 && f2x1 <= containerWidth
          && 0 <= f1y1 && f1y1 <= containerHeight
          && 0 <= f2y1 && f2y1 <= containerHeight
        ;

        var pan = cy.pan();
        var zoom = cy.zoom();

        distance1 = distance( f1x1, f1y1, f2x1, f2y1 );
        distance1Sq = distanceSq( f1x1, f1y1, f2x1, f2y1 );
        center1 = [ (f1x1 + f2x1)/2, (f1y1 + f2y1)/2 ];
        modelCenter1 = [ 
          (center1[0] - pan.x) / zoom,
          (center1[1] - pan.y) / zoom
        ];

        // consider context tap
        var cxtDistThreshold = 200;
        var cxtDistThresholdSq = cxtDistThreshold * cxtDistThreshold;
        if( distance1Sq < cxtDistThresholdSq && !e.touches[2] ){

          var near1 = r.findNearestElement(now[0], now[1], true);
          var near2 = r.findNearestElement(now[2], now[3], true);

          //console.log(distance1)

          if( near1 && near1.isNode() ){
            near1.activate().trigger( new $$.Event(e, {
              type: 'cxttapstart',
              cyPosition: { x: now[0], y: now[1] }
            }) );
            r.touchData.start = near1;
          
          } else if( near2 && near2.isNode() ){
            near2.activate().trigger( new $$.Event(e, {
              type: 'cxttapstart',
              cyPosition: { x: now[0], y: now[1] }
            }) );
            r.touchData.start = near2;
          
          } else {
            cy.trigger( new $$.Event(e, {
              type: 'cxttapstart',
              cyPosition: { x: now[0], y: now[1] }
            }) );
            r.touchData.start = null;
          } 

          if( r.touchData.start ){ r.touchData.start._private.grabbed = false; }
          r.touchData.cxt = true;
          r.touchData.cxtDragged = false;
          r.data.bgActivePosistion = undefined;

          //console.log('cxttapstart')

          r.redraw();
          return;
          
        }

        // console.log(center1);
        // console.log('touchstart ptz');
        // console.log(offsetLeft, offsetTop);
        // console.log(f1x1, f1y1);
        // console.log(f2x1, f2y1);
        // console.log(distance1);
        // console.log(center1);
      }

      // console.log('another tapstart')
      
      
      if (e.touches[2]) {
      
      } else if (e.touches[1]) {
        
      } else if (e.touches[0]) {
        var near = r.findNearestElement(now[0], now[1], true);

        if (near != null) {
          near.activate();

          r.touchData.start = near;
          
          if( near.isNode() && r.nodeIsDraggable(near) ){

            var draggedEles = r.dragData.touchDragEles = [];
            
            r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
            r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

            if( near.selected() ){
              // reset drag elements, since near will be added again

              var selectedNodes = cy.$(function(){
                return this.isNode() && this.selected();
              });

              for( var k = 0; k < selectedNodes.length; k++ ){
                var selectedNode = selectedNodes[k];

                if( r.nodeIsDraggable(selectedNode) ){
                  addNodeToDrag( selectedNode, { addToList: draggedEles } );
                }
              }
            } else {
              addNodeToDrag( near, { addToList: draggedEles } );
            }

            near.trigger( new $$.Event(e, {
              type: 'grab',
              cyPosition: { x: now[0], y: now[1] }
            }) );
          }
          
          near
            .trigger(new $$.Event(e, {
              type: 'touchstart',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'tapstart',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'vmousdown',
              cyPosition: { x: now[0], y: now[1] }
            }))
          ;
        } if (near == null) {
          cy
            .trigger(new $$.Event(e, {
              type: 'touchstart',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'tapstart',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'vmousedown',
              cyPosition: { x: now[0], y: now[1] }
            }))
          ;

          r.data.bgActivePosistion = {
            x: pos[0],
            y: pos[1]
          };

          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
          r.redraw();
        }
        
        
        // Tap, taphold
        // -----
        
        for (var i=0; i<now.length; i++) {
          earlier[i] = now[i];
          r.touchData.startPosition[i] = now[i];
        }
        
        r.touchData.singleTouchMoved = false;
        r.touchData.singleTouchStartTime = +new Date();
        
        clearTimeout( r.touchData.tapholdTimeout );
        r.touchData.tapholdTimeout = setTimeout(function() {
          if(
              r.touchData.singleTouchMoved === false
              && !r.pinching // if pinching, then taphold unselect shouldn't take effect

              // This time double constraint prevents multiple quick taps
              // followed by a taphold triggering multiple taphold events
              //&& Date.now() - r.touchData.singleTouchStartTime > 250
          ){
            if (r.touchData.start) {
              r.touchData.start.trigger( new $$.Event(e, {
                type: 'taphold',
                cyPosition: { x: now[0], y: now[1] }
              }) );
            } else {
              r.data.cy.trigger( new $$.Event(e, {
                type: 'taphold',
                cyPosition: { x: now[0], y: now[1] }
              }) );

              cy.$(':selected').unselect();
            }

//            console.log('taphold');
          }
        }, r.tapholdDuration);
      }
      
      //r.redraw();
      
    }, false);
    
// console.log = function(m){ $('#console').append('<div>'+m+'</div>'); };

    r.registerBinding(window, 'touchmove', $$.util.throttle(function(e) {
    
      var select = r.data.select;
      var capture = r.touchData.capture; //if (!capture) { return; }; 
      if( capture ){ e.preventDefault(); }
    
      var cy = r.data.cy; 
      var now = r.touchData.now; var earlier = r.touchData.earlier;
      var zoom = cy.zoom();
      
      if (e.touches[0]) { var pos = r.projectIntoViewport(e.touches[0].clientX, e.touches[0].clientY); now[0] = pos[0]; now[1] = pos[1]; }
      if (e.touches[1]) { var pos = r.projectIntoViewport(e.touches[1].clientX, e.touches[1].clientY); now[2] = pos[0]; now[3] = pos[1]; }
      if (e.touches[2]) { var pos = r.projectIntoViewport(e.touches[2].clientX, e.touches[2].clientY); now[4] = pos[0]; now[5] = pos[1]; }
      var disp = []; for (var j=0;j<now.length;j++) { disp[j] = now[j] - earlier[j]; }
      
      var startPos = r.touchData.startPosition;

      var dx = now[0] - startPos[0];
      var dx2 = dx * dx;
      var dy = now[1] - startPos[1];
      var dy2 = dy * dy;
      var dist2 = dx2 + dy2;
      var rdist2 = dist2 * zoom * zoom;

      if( capture && r.touchData.cxt ){
        var f1x2 = e.touches[0].clientX - offsetLeft, f1y2 = e.touches[0].clientY - offsetTop;
        var f2x2 = e.touches[1].clientX - offsetLeft, f2y2 = e.touches[1].clientY - offsetTop;
        // var distance2 = distance( f1x2, f1y2, f2x2, f2y2 );
        var distance2Sq = distanceSq( f1x2, f1y2, f2x2, f2y2 );
        var factorSq = distance2Sq / distance1Sq;

        var distThreshold = 150;
        var distThresholdSq = distThreshold * distThreshold;
        var factorThreshold = 1.5;
        var factorThresholdSq = factorThreshold * factorThreshold;

        //console.log(factor, distance2)

        // cancel ctx gestures if the distance b/t the fingers increases
        if( factorSq >= factorThresholdSq || distance2Sq >= distThresholdSq ){
          r.touchData.cxt = false;
          if( r.touchData.start ){ r.touchData.start.unactivate(); r.touchData.start = null; }
          r.data.bgActivePosistion = undefined;
          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

          var cxtEvt = new $$.Event(e, {
            type: 'cxttapend',
            cyPosition: { x: now[0], y: now[1] }
          });
          if( r.touchData.start ){
            r.touchData.start.trigger( cxtEvt );
          } else {
            cy.trigger( cxtEvt );
          }
        }

      }  

      if( capture && r.touchData.cxt ){ 
        var cxtEvt = new $$.Event(e, {
          type: 'cxtdrag',
          cyPosition: { x: now[0], y: now[1] }
        });
        r.data.bgActivePosistion = undefined;
        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

        if( r.touchData.start ){
          r.touchData.start.trigger( cxtEvt );
        } else {
          cy.trigger( cxtEvt );
        }

        if( r.touchData.start ){ r.touchData.start._private.grabbed = false; }
        r.touchData.cxtDragged = true;

        //console.log('cxtdrag')

        var near = r.findNearestElement(now[0], now[1], true);

        if( !r.touchData.cxtOver || near !== r.touchData.cxtOver ){

          if( r.touchData.cxtOver ){
            r.touchData.cxtOver.trigger( new $$.Event(e, {
              type: 'cxtdragout',
              cyPosition: { x: now[0], y: now[1] }
            }) );

            // console.log('cxtdragout');
          }

          r.touchData.cxtOver = near;

          if( near ){
            near.trigger( new $$.Event(e, {
              type: 'cxtdragover',
              cyPosition: { x: now[0], y: now[1] }
            }) );

            // console.log('cxtdragover');
          }

        }

      } else if( capture && e.touches[2] && cy.boxSelectionEnabled() ){ 
        r.data.bgActivePosistion = undefined;
        clearTimeout( this.threeFingerSelectTimeout );
        this.lastThreeTouch = +new Date();

        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

        if( !select || select.length === 0 || select[0] === undefined ){
          select[0] = (now[0] + now[2] + now[4])/3;
          select[1] = (now[1] + now[3] + now[5])/3;
          select[2] = (now[0] + now[2] + now[4])/3 + 1;
          select[3] = (now[1] + now[3] + now[5])/3 + 1;
        } else {
          select[2] = (now[0] + now[2] + now[4])/3;
          select[3] = (now[1] + now[3] + now[5])/3;
        }

        select[4] = 1;

        r.redraw();

      } else if ( capture && e.touches[1] && cy.zoomingEnabled() && cy.panningEnabled() && cy.userZoomingEnabled() && cy.userPanningEnabled() ) { // two fingers => pinch to zoom
        r.data.bgActivePosistion = undefined;
        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

        var draggedEles = r.dragData.touchDragEles;
        if( draggedEles ){ 
          r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

          for( var i = 0; i < draggedEles.length; i++ ){
            draggedEles[i]._private.grabbed = false;
            draggedEles[i]._private.rscratch.inDragLayer = false;
          }
        }

        // console.log('touchmove ptz');

        // (x2, y2) for fingers 1 and 2
        var f1x2 = e.touches[0].clientX - offsetLeft, f1y2 = e.touches[0].clientY - offsetTop;
        var f2x2 = e.touches[1].clientX - offsetLeft, f2y2 = e.touches[1].clientY - offsetTop;

        // console.log( f1x2, f1y2 )
        // console.log( f2x2, f2y2 )

        var distance2 = distance( f1x2, f1y2, f2x2, f2y2 );
        // var distance2Sq = distanceSq( f1x2, f1y2, f2x2, f2y2 );
        // var factor = Math.sqrt( distance2Sq ) / Math.sqrt( distance1Sq );
        var factor = distance2 / distance1;

        // console.log(distance2)
        // console.log(factor)

        if( factor != 1 && twoFingersStartInside){

          // console.log(factor)
          // console.log(distance2 + ' / ' + distance1);
          // console.log('--');

          // delta finger1
          var df1x = f1x2 - f1x1;
          var df1y = f1y2 - f1y1;

          // delta finger 2
          var df2x = f2x2 - f2x1;
          var df2y = f2y2 - f2y1;

          // translation is the normalised vector of the two fingers movement
          // i.e. so pinching cancels out and moving together pans
          var tx = (df1x + df2x)/2;
          var ty = (df1y + df2y)/2;

          // adjust factor by the speed multiplier
          // var speed = 1.5;
          // if( factor > 1 ){
          //   factor = (factor - 1) * speed + 1;
          // } else {
          //   factor = 1 - (1 - factor) * speed;
          // }

          // now calculate the zoom
          var zoom1 = cy.zoom();
          var zoom2 = zoom1 * factor;
          var pan1 = cy.pan();

          // the model center point converted to the current rendered pos
          var ctrx = modelCenter1[0] * zoom1 + pan1.x;
          var ctry = modelCenter1[1] * zoom1 + pan1.y;

          var pan2 = {
            x: -zoom2/zoom1 * (ctrx - pan1.x - tx) + ctrx,
            y: -zoom2/zoom1 * (ctry - pan1.y - ty) + ctry
          };

          // console.log(pan2);
          // console.log(zoom2);

          // remove dragged eles
          if( r.touchData.start ){
            var draggedEles = r.dragData.touchDragEles;

            if( draggedEles ){ for( var i = 0; i < draggedEles.length; i++ ){
              draggedEles[i]._private.grabbed = false;
              draggedEles[i]._private.rscratch.inDragLayer = false;
            } }

            r.touchData.start._private.active = false;
            r.touchData.start._private.grabbed = false;
            r.touchData.start._private.rscratch.inDragLayer = false;

            r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

            r.touchData.start
              .trigger('free')
              .trigger('unactivate')
            ;
          }

          cy.viewport({
            zoom: zoom2,
            pan: pan2,
            cancelOnFailedZoom: true
          });

          distance1 = distance2;  
          f1x1 = f1x2;
          f1y1 = f1y2;
          f2x1 = f2x2;
          f2y1 = f2y2;

          r.pinching = true;
        }
        
        // Re-project
        if (e.touches[0]) { var pos = r.projectIntoViewport(e.touches[0].clientX, e.touches[0].clientY); now[0] = pos[0]; now[1] = pos[1]; }
        if (e.touches[1]) { var pos = r.projectIntoViewport(e.touches[1].clientX, e.touches[1].clientY); now[2] = pos[0]; now[3] = pos[1]; }
        if (e.touches[2]) { var pos = r.projectIntoViewport(e.touches[2].clientX, e.touches[2].clientY); now[4] = pos[0]; now[5] = pos[1]; }

      } else if (e.touches[0]) {
        var start = r.touchData.start;
        var last = r.touchData.last;
        var near = near || r.findNearestElement(now[0], now[1], true);

        if( start != null && start._private.group == 'nodes' && r.nodeIsDraggable(start) ){

          if( rdist2 >= r.tapThreshold2 ){ // then dragging can happen
            var draggedEles = r.dragData.touchDragEles;

            for( var k = 0; k < draggedEles.length; k++ ){
              var draggedEle = draggedEles[k];

              if( r.nodeIsDraggable(draggedEle) && draggedEle.isNode() && draggedEle.grabbed() ){
                r.dragData.didDrag = true;
                var dPos = draggedEle._private.position;
                var justStartedDrag = !r.hoverData.draggingEles;

                if( $$.is.number(disp[0]) && $$.is.number(disp[1]) ){
                  dPos.x += disp[0];
                  dPos.y += disp[1];
                }

                if( justStartedDrag ){
                  addNodeToDrag( draggedEle, { inDragLayer: true } );

                  var dragDelta = r.touchData.dragDelta;

                  if( $$.is.number(dragDelta[0]) && $$.is.number(dragDelta[1]) ){
                    dPos.x += dragDelta[0];
                    dPos.y += dragDelta[1];
                  }

                }
              }
            }

            var tcol = new $$.Collection(cy, draggedEle);
            
            tcol.updateCompoundBounds();
            tcol.trigger('position drag');

            r.hoverData.draggingEles = true;
            
            r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true;

            if( 
                 r.touchData.startPosition[0] == earlier[0]
              && r.touchData.startPosition[1] == earlier[1]
            ){
              
              r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true;
            }
            
            r.redraw();
          } else { // otherise keep track of drag delta for later
            var dragDelta = r.touchData.dragDelta = r.touchData.dragDelta || [];

            if( dragDelta.length === 0 ){
              dragDelta.push(0);
              dragDelta.push(0);
            } else {
              dragDelta[0] += disp[0];
              dragDelta[1] += disp[1];
            }
          }
        }
        
        // Touchmove event
        {

          if (start != null) {
            start.trigger( new $$.Event(e, {
              type: 'touchmove',
              cyPosition: { x: now[0], y: now[1] }
            }) ); 

            start.trigger( new $$.Event(e, {
              type: 'tapdrag',
              cyPosition: { x: now[0], y: now[1] }
            }) ); 

            start.trigger( new $$.Event(e, {
              type: 'vmousemove',
              cyPosition: { x: now[0], y: now[1] }
            }) ); 
          }
          
          if (start == null) { 

            if (near != null) { 
              near.trigger( new $$.Event(e, {
                type: 'touchmove',
                cyPosition: { x: now[0], y: now[1] }
              }) ); 

              near.trigger( new $$.Event(e, {
                type: 'tapdrag',
                cyPosition: { x: now[0], y: now[1] }
              }) );

              near.trigger( new $$.Event(e, {
                type: 'vmousemove',
                cyPosition: { x: now[0], y: now[1] }
              }) );
            }

            if (near == null) { 
              cy.trigger( new $$.Event(e, {
                type: 'touchmove',
                cyPosition: { x: now[0], y: now[1] }
              }) ); 

              cy.trigger( new $$.Event(e, {
                type: 'tapdrag',
                cyPosition: { x: now[0], y: now[1] }
              }) ); 

              cy.trigger( new $$.Event(e, {
                type: 'vmousemove',
                cyPosition: { x: now[0], y: now[1] }
              }) ); 
            }
          }

          if (near != last) {
            if (last) { last.trigger(new $$.Event(e, { type: 'tapdragout', cyPosition: { x: now[0], y: now[1] } })); }
            if (near) { near.trigger(new $$.Event(e, { type: 'tapdragover', cyPosition: { x: now[0], y: now[1] } })); }
          }

          r.touchData.last = near;
        }
        
        // Check to cancel taphold
        for (var i=0;i<now.length;i++) {
          if (now[i] 
            && r.touchData.startPosition[i]
            && Math.abs(now[i] - r.touchData.startPosition[i]) > 4) {
            
            r.touchData.singleTouchMoved = true;
          }
        }
        
        if(
            capture
            && ( start == null || start.isEdge() )
            && cy.panningEnabled() && cy.userPanningEnabled()
        ){

          if( r.swipePanning ){
            cy.panBy({
              x: disp[0] * zoom,
              y: disp[1] * zoom
            });

          } else if( rdist2 >= r.tapThreshold2 ){
            r.swipePanning = true;

            cy.panBy({
              x: dx * zoom,
              y: dy * zoom
            });
          }

          if( start ){
            start.unactivate();

            if( !r.data.bgActivePosistion ){
              r.data.bgActivePosistion = {
                x: now[0],
                y: now[1]
              };
            }

            r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

            r.touchData.start = null;
          }
          
          // Re-project
          var pos = r.projectIntoViewport(e.touches[0].clientX, e.touches[0].clientY);
          now[0] = pos[0]; now[1] = pos[1];
        }
      }

      for (var j=0; j<now.length; j++) { earlier[j] = now[j]; }
      //r.redraw();
      
    }, 1000/30, { trailing: true }), false);
    
    r.registerBinding(window, 'touchcancel', function(e) {
      var start = r.touchData.start;

      r.touchData.capture = false;

      if( start ){
        start.unactivate();
      }
    });

    r.registerBinding(window, 'touchend', function(e) {
      var start = r.touchData.start;

      var capture = r.touchData.capture; 

      if( capture ){
        r.touchData.capture = false;
      } else {
        return;
      }
      
      e.preventDefault();
      var select = r.data.select;

      r.swipePanning = false;
      r.hoverData.draggingEles = false;
      
      var cy = r.data.cy; 
      var zoom = cy.zoom();
      var now = r.touchData.now;
      var earlier = r.touchData.earlier;

      if (e.touches[0]) { var pos = r.projectIntoViewport(e.touches[0].clientX, e.touches[0].clientY); now[0] = pos[0]; now[1] = pos[1]; }
      if (e.touches[1]) { var pos = r.projectIntoViewport(e.touches[1].clientX, e.touches[1].clientY); now[2] = pos[0]; now[3] = pos[1]; }
      if (e.touches[2]) { var pos = r.projectIntoViewport(e.touches[2].clientX, e.touches[2].clientY); now[4] = pos[0]; now[5] = pos[1]; }
      
      if( start ){
        start.unactivate();
      }

      var ctxTapend;
      if( r.touchData.cxt ){
        ctxTapend = new $$.Event(e, {
          type: 'cxttapend',
          cyPosition: { x: now[0], y: now[1] }
        });

        if( start ){
          start.trigger( ctxTapend );
        } else {
          cy.trigger( ctxTapend );
        }

        //console.log('cxttapend')

        if( !r.touchData.cxtDragged ){
          var ctxTap = new $$.Event(e, {
            type: 'cxttap',
            cyPosition: { x: now[0], y: now[1] }
          });

          if( start ){
            start.trigger( ctxTap );
          } else {
            cy.trigger( ctxTap );
          }

          //console.log('cxttap')
        }

        if( r.touchData.start ){ r.touchData.start._private.grabbed = false; }
        r.touchData.cxt = false;
        r.touchData.start = null;

        r.redraw();
        return;
      }

      // no more box selection if we don't have three fingers
      if( !e.touches[2] && cy.boxSelectionEnabled() ){
        clearTimeout( this.threeFingerSelectTimeout );
        //this.threeFingerSelectTimeout = setTimeout(function(){
          var newlySelected = [];
          var box = r.getAllInBox( select[0], select[1], select[2], select[3] );

          select[0] = undefined;
          select[1] = undefined;
          select[2] = undefined;
          select[3] = undefined;
          select[4] = 0;

          r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

          // console.log(box);
          for( var i = 0; i< box.length; i++ ) { 
            if( box[i]._private.selectable ){
              newlySelected.push( box[i] );
            }
          }

          var newlySelCol = new $$.Collection( cy, newlySelected );

          if( cy.selectionType() === 'single' ){
            cy.$(':selected').not( newlySelCol ).unselect();
          }

          newlySelCol.select();
          
          if( newlySelCol.length > 0 ) { 
            r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
          } else {
            r.redraw();
          }

        //}, 100);
      }

      var updateStartStyle = false;

      if( start != null ){
        start._private.active = false;
        updateStartStyle = true;
        start.unactivate();
      }

      if (e.touches[2]) {
        r.data.bgActivePosistion = undefined;
        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;
      } else if (e.touches[1]) {
        
      } else if (e.touches[0]) {
      
      // Last touch released
      } else if (!e.touches[0]) {
        
        r.data.bgActivePosistion = undefined;
        r.data.canvasNeedsRedraw[CanvasRenderer.SELECT_BOX] = true;

        if (start != null ) {

          if( start._private.grabbed ){
            start._private.grabbed = false;
            start.trigger('free');
            start._private.rscratch.inDragLayer = false;
          }
          
          var sEdges = start._private.edges;
          for (var j=0;j<sEdges.length;j++) { sEdges[j]._private.rscratch.inDragLayer = false; }
          updateAncestorsInDragLayer(start, false);
          
          if( start.selected() ){
            var selectedNodes = cy.$('node:selected');

            for( var k = 0; k < selectedNodes.length; k++ ){

              var selectedNode = selectedNodes[k];
              selectedNode._private.rscratch.inDragLayer = false;
              selectedNode._private.grabbed = false;

              var sEdges = selectedNode._private.edges;
              for (var j=0; j<sEdges.length; j++) {
                sEdges[j]._private.rscratch.inDragLayer = false;
              }

              updateAncestorsInDragLayer(selectedNode, false);
            }
          }

          r.data.canvasNeedsRedraw[CanvasRenderer.DRAG] = true; 
          r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
          
          start
            .trigger(new $$.Event(e, {
              type: 'touchend',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'tapend',
              cyPosition: { x: now[0], y: now[1] }
            }))
            .trigger(new $$.Event(e, {
              type: 'vmouseup',
              cyPosition: { x: now[0], y: now[1] }
            }))
          ;
          
          start.unactivate();

          r.touchData.start = null;
          
        } else {
          var near = r.findNearestElement(now[0], now[1], true);
        
          if (near != null) { 
            near
              .trigger(new $$.Event(e, {
                type: 'touchend',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapend',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmouseup',
                cyPosition: { x: now[0], y: now[1] }
              }))
            ;
          }

          if (near == null) { 
            cy
              .trigger(new $$.Event(e, {
                type: 'touchend',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'tapend',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vmouseup',
                cyPosition: { x: now[0], y: now[1] }
              }))
            ;
          }
        }

        var dx = r.touchData.startPosition[0] - now[0];
        var dx2 = dx * dx;
        var dy = r.touchData.startPosition[1] - now[1];
        var dy2 = dy * dy;
        var dist2 = dx2 + dy2;
        var rdist2 = dist2 * zoom * zoom;
        
        // Prepare to select the currently touched node, only if it hasn't been dragged past a certain distance
        if (start != null 
            && !r.dragData.didDrag // didn't drag nodes around
            && start._private.selectable 
            && rdist2 < r.tapThreshold2
            && !r.pinching // pinch to zoom should not affect selection
        ) {

          if( cy.selectionType() === 'single' ){
            cy.$(':selected').not( start ).unselect();
            start.select();
          } else {
            if( start.selected() ){
              start.unselect();
            } else {
              start.select();
            }
          }

          updateStartStyle = true;

          
          r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
        }
        
        // Tap event, roughly same as mouse click event for touch
        if ( r.touchData.singleTouchMoved === false ) {

          if (start) {
            start
              .trigger(new $$.Event(e, {
                type: 'tap',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vclick',
                cyPosition: { x: now[0], y: now[1] }
              }))
            ;
          } else {
            cy
              .trigger(new $$.Event(e, {
                type: 'tap',
                cyPosition: { x: now[0], y: now[1] }
              }))
              .trigger(new $$.Event(e, {
                type: 'vclick',
                cyPosition: { x: now[0], y: now[1] }
              }))
            ;
          }
          
//          console.log('tap');
        }
        
        r.touchData.singleTouchMoved = true;
      }
      
      for( var j = 0; j < now.length; j++ ){ earlier[j] = now[j]; }

      r.dragData.didDrag = false; // reset for next mousedown

      if( e.touches[0] ){
        r.touchData.dragDelta = [];
      }

      if( updateStartStyle && start ){
        start.updateStyle(false);
      }

      if( e.touches.length < 2 ){
        r.pinching = false;
        r.data.canvasNeedsRedraw[CanvasRenderer.NODE] = true; 
        r.redraw();
      }

      //r.redraw();
      
    }, false);
  };

})( cytoscape );
;(function($$){ 'use strict';

  var CanvasRenderer = $$('renderer', 'canvas');
  var renderer = CanvasRenderer.prototype;
  var usePaths = CanvasRenderer.usePaths();

  // Node shape contract:
  //
  // draw: draw
  // intersectLine: report intersection from x, y, to node center
  // checkPoint: check x, y in node

  var nodeShapes = CanvasRenderer.nodeShapes = {};

  var sin0 = Math.sin(0);
  var cos0 = Math.cos(0);

  var sin = {};
  var cos = {};

  var ellipseStepSize = 0.1;

  for (var i = 0 * Math.PI; i < 2 * Math.PI; i += ellipseStepSize ) {
    sin[i] = Math.sin(i);
    cos[i] = Math.cos(i);
  }

  nodeShapes['ellipse'] = {
    draw: function(context, centerX, centerY, width, height) {
      nodeShapes['ellipse'].drawPath(context, centerX, centerY, width, height);
      context.fill();
      
//      console.log('drawing ellipse');
//      console.log(arguments);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      
      if( usePaths ){
        if( context.beginPath ){ context.beginPath(); }

        var xPos, yPos;
        var rw = width/2;
        var rh = height/2;
        for (var i = 0 * Math.PI; i < 2 * Math.PI; i += ellipseStepSize ) {
            xPos = centerX - (rw * sin[i]) * sin0 + (rw * cos[i]) * cos0;
            yPos = centerY + (rh * cos[i]) * sin0 + (rh * sin[i]) * cos0;

            if (i === 0) {
                context.moveTo(xPos, yPos);
            } else {
                context.lineTo(xPos, yPos);
            }
        }
        context.closePath();

      } else {

        if( context.beginPath ){ context.beginPath(); }
        context.translate(centerX, centerY);
        context.scale(width / 2, height / 2);
        // At origin, radius 1, 0 to 2pi
        context.arc(0, 0, 1, 0, Math.PI * 2 * 0.999, false); // *0.999 b/c chrome rendering bug on full circle
        context.closePath();

        context.scale(2/width, 2/height);
        context.translate(-centerX, -centerY);

      }
      
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      var intersect = $$.math.intersectLineEllipse(
        x, y,
        nodeX,
        nodeY,
        width / 2 + padding,
        height / 2 + padding);
      
      return intersect;
    },
    
    intersectBox: function(
      x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      return $$.math.boxIntersectEllipse(
        x1, y1, x2, y2, padding, width, height, centerX, centerY);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
//      console.log(arguments);
      
      x -= centerX;
      y -= centerY;
      
      x /= (width / 2 + padding);
      y /= (height / 2 + padding);
      
      return (Math.pow(x, 2) + Math.pow(y, 2) <= 1);
    }
  };
  
  nodeShapes['triangle'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(3, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['triangle'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['triangle'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return $$.math.polygonIntersectLine(
        x, y,
        nodeShapes['triangle'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    
      /*
      polygonIntersectLine(x, y, basePoints, centerX, centerY, 
        width, height, padding);
      */
      
      
      /*
      return renderer.polygonIntersectLine(
        node, width, height,
        x, y, nodeShapes['triangle'].points);
      */
    },
    
    intersectBox: function(
      x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      var points = nodeShapes['triangle'].points;
      
      return $$.math.boxIntersectPolygon(
        x1, y1, x2, y2,
        points, width, height, centerX, centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(
        x, y, nodeShapes['triangle'].points,
        centerX, centerY, width, height,
        [0, -1], padding);
    }
  };
  
  nodeShapes['square'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(4, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['square'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['square'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return $$.math.polygonIntersectLine(
          x, y,
          nodeShapes['square'].points,
          nodeX,
          nodeY,
          width / 2, height / 2,
          padding);
    },
    
    intersectBox: function(
      x1, y1, x2, y2,
      width, height, centerX, 
      centerY, padding) {
      
      var points = nodeShapes['square'].points;
      
      return $$.math.boxIntersectPolygon(
        x1, y1, x2, y2,
        points, width, height, centerX, 
        centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['square'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };
  
  nodeShapes['rectangle'] = nodeShapes['square'];
  
  nodeShapes['octogon'] = {};
  
  nodeShapes['roundrectangle'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(4, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawRoundRectangle(context,
        centerX, centerY,
        width, height,
        10);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawRoundRectanglePath(context,
        centerX, centerY,
        width, height,
        10);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return $$.math.roundRectangleIntersectLine(
          x, y,
          nodeX,
          nodeY,
          width, height,
          padding);
    },
    
    intersectBox: function(
      x1, y1, x2, y2,
      width, height, centerX, 
      centerY, padding) {

      return $$.math.roundRectangleIntersectBox(
        x1, y1, x2, y2, 
        width, height, centerX, centerY, padding);
    },
    
    // Looks like the width passed into this function is actually the total width / 2
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      var cornerRadius = $$.math.getRoundRectangleRadius(width, height);
      
      // Check hBox
      if ($$.math.pointInsidePolygon(x, y, nodeShapes['roundrectangle'].points,
        centerX, centerY, width, height - 2 * cornerRadius, [0, -1], padding)) {
        return true;
      }
      
      // Check vBox
      if ($$.math.pointInsidePolygon(x, y, nodeShapes['roundrectangle'].points,
        centerX, centerY, width - 2 * cornerRadius, height, [0, -1], padding)) {
        return true;
      }
      
      var checkInEllipse = function(x, y, centerX, centerY, width, height, padding) {
        x -= centerX;
        y -= centerY;
        
        x /= (width / 2 + padding);
        y /= (height / 2 + padding);
        
        return (Math.pow(x, 2) + Math.pow(y, 2) <= 1);
      };
      
      
      // Check top left quarter circle
      if (checkInEllipse(x, y,
        centerX - width / 2 + cornerRadius,
        centerY - height / 2 + cornerRadius,
        cornerRadius * 2, cornerRadius * 2, padding)) {
        
        return true;
      }
      
      /*
      if (renderer.boxIntersectEllipse(x, y, x, y, padding, 
        cornerRadius * 2, cornerRadius * 2,
        centerX - width + cornerRadius,
        centerY - height + cornerRadius)) {
        return true;
      }
      */
      
      // Check top right quarter circle
      if (checkInEllipse(x, y,
        centerX + width / 2 - cornerRadius,
        centerY - height / 2 + cornerRadius,
        cornerRadius * 2, cornerRadius * 2, padding)) {
        
        return true;
      }
      
      // Check bottom right quarter circle
      if (checkInEllipse(x, y,
        centerX + width / 2 - cornerRadius,
        centerY + height / 2 - cornerRadius,
        cornerRadius * 2, cornerRadius * 2, padding)) {
        
        return true;
      }
      
      // Check bottom left quarter circle
      if (checkInEllipse(x, y,
        centerX - width / 2 + cornerRadius,
        centerY + height / 2 - cornerRadius,
        cornerRadius * 2, cornerRadius * 2, padding)) {
        
        return true;
      }
      
      return false;
    }
  };
  
  nodeShapes['pentagon'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(5, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height, nodeShapes['pentagon'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height, nodeShapes['pentagon'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return renderer.polygonIntersectLine(
        x, y,
        nodeShapes['pentagon'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    },
    
    intersectBox: function(
      x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      var points = nodeShapes['pentagon'].points;
      
      return $$.math.boxIntersectPolygon(
        x1, y1, x2, y2,
        points, width, height, centerX, centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['pentagon'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };
  
  nodeShapes['hexagon'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(6, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['hexagon'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['hexagon'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return $$.math.polygonIntersectLine(
        x, y,
        nodeShapes['hexagon'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    },
    
    intersectBox: function(
        x1, y1, x2, y2, width, height, centerX, centerY, padding) {
        
      var points = nodeShapes['hexagon'].points;
      
      return $$.math.boxIntersectPolygon(
        x1, y1, x2, y2,
        points, width, height, centerX, centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['hexagon'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };
  
  nodeShapes['heptagon'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(7, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['heptagon'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['heptagon'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return renderer.polygonIntersectLine(
        x, y,
        nodeShapes['heptagon'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    },
    
    intersectBox: function(
        x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      var points = nodeShapes['heptagon'].points;
      
      return renderer.boxIntersectPolygon(
        x1, y1, x2, y2,
        points, width, height, centerX, centerY, [0, -1], padding);
    },

    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['heptagon'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };
  
  nodeShapes['octagon'] = {
    points: $$.math.generateUnitNgonPointsFitToSquare(8, 0),
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['octagon'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['octagon'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return renderer.polygonIntersectLine(
        x, y,
        nodeShapes['octagon'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    },
    
    intersectBox: function(
        x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      var points = nodeShapes['octagon'].points;
      
      return renderer.boxIntersectPolygon(
          x1, y1, x2, y2,
          points, width, height, centerX, centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['octagon'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };
  
  var star5Points = new Array(20);
  {
    var outerPoints = $$.math.generateUnitNgonPoints(5, 0);
    var innerPoints = $$.math.generateUnitNgonPoints(5, Math.PI / 5);
    
//    console.log(outerPoints);
//    console.log(innerPoints);
    
    // Outer radius is 1; inner radius of star is smaller
    var innerRadius = 0.5 * (3 - Math.sqrt(5));
    innerRadius *= 1.57;
    
    for (var i=0;i<innerPoints.length/2;i++) {
      innerPoints[i*2] *= innerRadius;
      innerPoints[i*2+1] *= innerRadius;
    }
    
    for (var i=0;i<20/4;i++) {
      star5Points[i*4] = outerPoints[i*2];
      star5Points[i*4+1] = outerPoints[i*2+1];
      
      star5Points[i*4+2] = innerPoints[i*2];
      star5Points[i*4+3] = innerPoints[i*2+1];
    }
    
//    console.log(star5Points);
  }

  star5Points = $$.math.fitPolygonToSquare( star5Points );
  
  nodeShapes['star5'] = nodeShapes['star'] = {
    points: star5Points,
    
    draw: function(context, centerX, centerY, width, height) {
      renderer.drawPolygon(context,
        centerX, centerY,
        width, height,
        nodeShapes['star5'].points);
    },
    
    drawPath: function(context, centerX, centerY, width, height) {
      renderer.drawPolygonPath(context,
        centerX, centerY,
        width, height,
        nodeShapes['star5'].points);
    },
    
    intersectLine: function(nodeX, nodeY, width, height, x, y, padding) {
      return renderer.polygonIntersectLine(
        x, y,
        nodeShapes['star5'].points,
        nodeX,
        nodeY,
        width / 2, height / 2,
        padding);
    },
    
    intersectBox: function(
        x1, y1, x2, y2, width, height, centerX, centerY, padding) {
      
      var points = nodeShapes['star5'].points;
      
      return renderer.boxIntersectPolygon(
          x1, y1, x2, y2,
          points, width, height, centerX, centerY, [0, -1], padding);
    },
    
    checkPoint: function(
      x, y, padding, width, height, centerX, centerY) {
      
      return $$.math.pointInsidePolygon(x, y, nodeShapes['star5'].points,
        centerX, centerY, width, height, [0, -1], padding);
    }
  };

})( cytoscape );

;(function($$){ 'use strict';
  
  var defaults = {
    animate: true, // whether to show the layout as it's running
    maxSimulationTime: 4000, // max length in ms to run the layout
    fit: true, // on every layout reposition of nodes, fit the viewport
    padding: 30, // padding around the simulation
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    ungrabifyWhileSimulating: false, // so you can't drag nodes during layout

    // callbacks on layout events
    ready: undefined, // callback on layoutready 
    stop: undefined, // callback on layoutstop

    // forces used by arbor (use arbor default on undefined)
    repulsion: undefined,
    stiffness: undefined,
    friction: undefined,
    gravity: true,
    fps: undefined,
    precision: undefined,

    // static numbers or functions that dynamically return what these
    // values should be for each element
    // e.g. nodeMass: function(n){ return n.data('weight') }
    nodeMass: undefined, 
    edgeLength: undefined,

    stepSize: 0.1, // smoothing of arbor bounding box

    // function that returns true if the system is stable to indicate
    // that the layout can be stopped
    stableEnergy: function( energy ){
      var e = energy; 
      return (e.max <= 0.5) || (e.mean <= 0.3);
    },

    // infinite layout options
    infinite: false // overrides all other options for a forces-all-the-time mode
  };
  
  function ArborLayout(options){
    this._private = {};

    this._private.options = $$.util.extend({}, defaults, options);
  }
    
  ArborLayout.prototype.run = function(){
    var layout = this;
    var options = this._private.options;

    $$.util.require('arbor', function(arbor){

      var cy = options.cy;
      var eles = options.eles;
      var nodes = eles.nodes().not(':parent');
      var edges = eles.edges();
      var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
        x1: 0, y1: 0, w: cy.width(), h: cy.height()
      } );
      var simUpdatingPos = false;

      layout.trigger({ type: 'layoutstart', layout: layout });

      // backward compatibility for old animation option
      if( options.liveUpdate !== undefined ){
        options.animate = options.liveUpdate;
      }

      // arbor doesn't work with just 1 node 
      if( cy.nodes().size() <= 1 ){
        if( options.fit ){
          cy.reset();
        }

        cy.nodes().position({
          x: Math.round( (bb.x1 + bb.x2)/2 ),
          y: Math.round( (bb.y1 + bb.y2)/2 )
        });

        layout.one('layoutready', options.ready);
        layout.trigger({ type: 'layoutready', layout: layout });

        layout.one('layoutstop', options.stop);
        layout.trigger({ type: 'layoutstop', layout: layout });

        return;
      }

      var sys = layout._private.system = arbor.ParticleSystem();

      sys.parameters({
        repulsion: options.repulsion,
        stiffness: options.stiffness, 
        friction: options.friction, 
        gravity: options.gravity, 
        fps: options.fps, 
        dt: options.dt, 
        precision: options.precision
      });

      if( options.animate && options.fit ){
        cy.fit( bb, options.padding );
      }
      
      var doneTime = 250;
      var doneTimeout;
      
      var ready = false;
      
      var lastDraw = +new Date();
      var sysRenderer = {
        init: function(system){
        },
        redraw: function(){
          var energy = sys.energy();

          // if we're stable (according to the client), we're done
          if( !options.infinite && options.stableEnergy != null && energy != null && energy.n > 0 && options.stableEnergy(energy) ){
            layout.stop();
            return;
          }

          if( !options.infinite && doneTime != Infinity ){
            clearTimeout(doneTimeout);
            doneTimeout = setTimeout(doneHandler, doneTime);
          }
          
          var movedNodes = cy.collection();
          
          sys.eachNode(function(n, point){ 
            var data = n.data;
            var node = data.element;
            
            if( node == null ){
              return;
            }

            if( !node.locked() && !node.grabbed() ){
              node.silentPosition({
                x: bb.x1 + point.x,
                y: bb.y1 + point.y
              });

              movedNodes.merge( node );
            }
          });
          

          if( options.animate && movedNodes.length > 0 ){
            simUpdatingPos = true;

            movedNodes.rtrigger('position');

            if( options.fit ){
              cy.fit( options.padding );
            }

            lastDraw = +new Date();
            simUpdatingPos = false;
          }

          
          if( !ready ){
            ready = true;
            layout.one('layoutready', options.ready);
            layout.trigger({ type: 'layoutready', layout: layout });
          }
        }
        
      };
      sys.renderer = sysRenderer;
      sys.screenSize( bb.w, bb.h );
      sys.screenPadding( options.padding, options.padding, options.padding, options.padding );
      sys.screenStep( options.stepSize );

      function calculateValueForElement(element, value){
        if( value == null ){
          return undefined;
        } else if( typeof value == typeof function(){} ){
          return value.apply(element, [element._private.data, {
            nodes: nodes.length,
            edges: edges.length,
            element: element
          }]); 
        } else {
          return value;
        }
      }

      var grabHandler;
      nodes.on('grab free position', grabHandler = function(e){
        if( simUpdatingPos ){ return; }

        var pos = this.position();
        var apos = sys.fromScreen( pos );
        if( !apos ){ return; }

        var p = arbor.Point(apos.x, apos.y);
        var padding = options.padding;

        if(
          bb.x1 + padding <= pos.x && pos.x <= bb.x2 - padding &&
          bb.y1 + padding <= pos.y && pos.y <= bb.y2 - padding
        ){
          this.scratch().arbor.p = p;
        }
        
        switch( e.type ){
        case 'grab':
          this.scratch().arbor.fixed = true;
          break;
        case 'free':
          this.scratch().arbor.fixed = false;
          //this.scratch().arbor.tempMass = 1000;
          break;
        }
      });

      var lockHandler;
      nodes.on('lock unlock', lockHandler = function(e){
        node.scratch().arbor.fixed = node.locked();
      });
            
      var removeHandler;
      eles.on('remove', removeHandler = function(e){ return; // TODO enable when layout add/remove api added
        // var ele = this;
        // var arborEle = ele.scratch().arbor;

        // if( !arborEle ){ return; }

        // if( ele.isNode() ){
        //   sys.pruneNode( arborEle );
        // } else {
        //   sys.pruneEdge( arborEle );
        // }
      });

      var addHandler;
      cy.on('add', '*', addHandler = function(){ return; // TODO enable when layout add/remove api added
        // var ele = this;

        // if( ele.isNode() ){
        //   addNode( ele );
        // } else {
        //   addEdge( ele );
        // }
      });

      var resizeHandler;
      cy.on('resize', resizeHandler = function(){
        if( options.boundingBox == null && layout._private.system != null ){
          var w = cy.width();
          var h = cy.height();

          sys.screenSize( w, h );
        }
      });

      function addNode( node ){
        if( node.isFullAutoParent() ){ return; } // they don't exist in the sim

        var id = node._private.data.id;
        var mass = calculateValueForElement(node, options.nodeMass);
        var locked = node._private.locked;
        var nPos = node.position();
        
        var pos = sys.fromScreen({
          x: nPos.x,
          y: nPos.y
        });

        node.scratch().arbor = sys.addNode(id, {
          element: node,
          mass: mass,
          fixed: locked,
          x: locked ? pos.x : undefined,
          y: locked ? pos.y : undefined
        });
      }

      function addEdge( edge ){
        var src = edge.source().id();
        var tgt = edge.target().id();
        var length = calculateValueForElement(edge, options.edgeLength);
        
        edge.scratch().arbor = sys.addEdge(src, tgt, {
          length: length
        }); 
      }

      nodes.each(function(i, node){
        addNode( node );
      });
      
      edges.each(function(i, edge){
        addEdge( edge );
      });
      
      var grabbableNodes = nodes.filter(":grabbable");
      // disable grabbing if so set
      if( options.ungrabifyWhileSimulating ){
        grabbableNodes.ungrabify();
      }
      
      var doneHandler = layout._private.doneHandler = function(){
        layout._private.doneHandler = null;

        if( !options.animate ){
          if( options.fit ){
            cy.reset();
          }

          nodes.rtrigger('position');
        }

        // unbind handlers
        nodes.off('grab free position', grabHandler);
        nodes.off('lock unlock', lockHandler);
        eles.off('remove', removeHandler);
        cy.off('add', '*', addHandler);
        cy.off('resize', resizeHandler);
        
        // enable back grabbing if so set
        if( options.ungrabifyWhileSimulating ){
          grabbableNodes.grabify();
        }

        layout.one('layoutstop', options.stop);
        layout.trigger({ type: 'layoutstop', layout: layout });
      };
      
      sys.start();
      if( !options.infinite && options.maxSimulationTime != null && options.maxSimulationTime > 0 && options.maxSimulationTime !== Infinity ){
        setTimeout(function(){
          layout.stop();
        }, options.maxSimulationTime);
      }
    
    }); // require

    return this; // chaining
  };


  ArborLayout.prototype.stop = function(){
    if( this._private.system != null ){
      this._private.system.stop();
    }

    if( this._private.doneHandler ){
      this._private.doneHandler();
    }

    return this; // chaining
  };
  
  $$('layout', 'arbor', ArborLayout);
  
  
})(cytoscape);

;(function($$){ 'use strict';
  
  var defaults = {
    fit: true, // whether to fit the viewport to the graph
    directed: false, // whether the tree is directed downwards (or edges can point in any direction if false)
    padding: 30, // padding on fit
    circle: false, // put depths in concentric circles if true, put depths top down if false
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    avoidOverlap: true, // prevents node overlap, may overflow boundingBox if not enough space
    roots: undefined, // the roots of the trees
    maximalAdjustments: 0, // how many times to try to position the nodes in a maximal way (i.e. no backtracking)
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function BreadthFirstLayout( options ){
    this.options = $$.util.extend({}, defaults, options);
  }
  
  BreadthFirstLayout.prototype.run = function(){
    var params = this.options;
    var options = params;
    
    var cy = params.cy;
    var eles = options.eles;
    var nodes = eles.nodes().not(':parent');
    var graph = eles;
    
    var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
      x1: 0, y1: 0, w: cy.width(), h: cy.height()
    } );

    var roots;
    if( $$.is.elementOrCollection(options.roots) ){
      roots = options.roots;
    } else if( $$.is.array(options.roots) ){
      var rootsArray = [];

      for( var i = 0; i < options.roots.length; i++ ){
        var id = options.roots[i];
        var ele = cy.getElementById( id );
        rootsArray.push( ele );
      }

      roots = new $$.Collection( cy, rootsArray );
    } else if( $$.is.string(options.roots) ){
      roots = cy.$( options.roots );

    } else {
      if( options.directed ){
        roots = nodes.roots();
      } else {
        var components = [];
        var unhandledNodes = nodes;

        while( unhandledNodes.length > 0 ){
          var currComp = cy.collection();

          eles.bfs({
            roots: unhandledNodes[0],
            visit: function(i, depth, node, edge, pNode){
              currComp = currComp.add( node );
            },
            directed: false
          });

          unhandledNodes = unhandledNodes.not( currComp );
          components.push( currComp );
        }

        roots = cy.collection();
        for( var i = 0; i < components.length; i++ ){
          var comp = components[i];
          var maxDegree = comp.maxDegree( false );
          var compRoots = comp.filter(function(){
            return this.degree(false) === maxDegree;
          });

          roots = roots.add( compRoots );
        }
        
      }
    }


    var depths = [];
    var foundByBfs = {};
    var id2depth = {};
    var prevNode = {};
    var prevEdge = {};
    var successors = {};

    // find the depths of the nodes
    graph.bfs({
      roots: roots,
      directed: options.directed,
      visit: function(i, depth, node, edge, pNode){
        var ele = this[0];
        var id = ele.id();

        if( !depths[depth] ){
          depths[depth] = [];
        }

        depths[depth].push( ele );
        foundByBfs[ id ] = true;
        id2depth[ id ] = depth;
        prevNode[ id ] = pNode;
        prevEdge[ id ] = edge;

        if( pNode ){
          var prevId = pNode.id();
          var succ = successors[ prevId ] = successors[ prevId ] || [];
          
          succ.push( node );
        }
      }
    });

    // check for nodes not found by bfs
    var orphanNodes = [];
    for( var i = 0; i < nodes.length; i++ ){
      var ele = nodes[i];

      if( foundByBfs[ ele.id() ] ){
        continue;
      } else {
        orphanNodes.push( ele );
      }
    }

    // assign orphan nodes a depth from their neighborhood
    var maxChecks = orphanNodes.length * 3;
    var checks = 0;
    while( orphanNodes.length !== 0 && checks < maxChecks ){
      var node = orphanNodes.shift();
      var neighbors = node.neighborhood().nodes();
      var assignedDepth = false;

      for( var i = 0; i < neighbors.length; i++ ){
        var depth = id2depth[ neighbors[i].id() ];

        if( depth !== undefined ){
          depths[depth].push( node );
          assignedDepth = true;
          break;
        }
      }

      if( !assignedDepth ){
        orphanNodes.push( node );
      }

      checks++;
    }

    // assign orphan nodes that are still left to the depth of their subgraph
    while( orphanNodes.length !== 0 ){
      var node = orphanNodes.shift();
      //var subgraph = graph.bfs( node ).path;
      var assignedDepth = false;

      // for( var i = 0; i < subgraph.length; i++ ){
      //   var depth = id2depth[ subgraph[i].id() ];

      //   if( depth !== undefined ){
      //     depths[depth].push( node );
      //     assignedDepth = true;
      //     break;
      //   }
      // }

      if( !assignedDepth ){ // worst case if the graph really isn't tree friendly, then just dump it in 0
        if( depths.length === 0 ){
          depths.push([]);
        }
        
        depths[0].push( node );
      }
    }

    // assign the nodes a depth and index
    var assignDepthsToEles = function(){
      for( var i = 0; i < depths.length; i++ ){
        var eles = depths[i];

        for( var j = 0; j < eles.length; j++ ){
          var ele = eles[j];

          ele._private.scratch.breadthfirst = {
            depth: i,
            index: j
          };
        }
      }
    };
    assignDepthsToEles();


    var intersectsDepth = function( node ){ // returns true if has edges pointing in from a higher depth
      var edges = node.connectedEdges(function(){
        return this.data('target') === node.id();
      });
      var thisInfo = node._private.scratch.breadthfirst;
      var highestDepthOfOther = 0;
      var highestOther;
      for( var i = 0; i < edges.length; i++ ){
        var edge = edges[i];
        var otherNode = edge.source()[0];
        var otherInfo = otherNode._private.scratch.breadthfirst;

        if( thisInfo.depth <= otherInfo.depth && highestDepthOfOther < otherInfo.depth ){
          highestDepthOfOther = otherInfo.depth;
          highestOther = otherNode;
        }
      }

      return highestOther;
    };

     // make maximal if so set by adjusting depths
    for( var adj = 0; adj < options.maximalAdjustments; adj++ ){

      var nDepths = depths.length;
      var elesToMove = [];
      for( var i = 0; i < nDepths; i++ ){
        var depth = depths[i];

        var nDepth = depth.length;
        for( var j = 0; j < nDepth; j++ ){
          var ele = depth[j];
          var info = ele._private.scratch.breadthfirst;
          var intEle = intersectsDepth(ele);

          if( intEle ){
            info.intEle = intEle;
            elesToMove.push( ele );
          }
        }
      }

      for( var i = 0; i < elesToMove.length; i++ ){ 
        var ele = elesToMove[i];
        var info = ele._private.scratch.breadthfirst;
        var intEle = info.intEle;
        var intInfo = intEle._private.scratch.breadthfirst;

        depths[ info.depth ].splice( info.index, 1 ); // remove from old depth & index

        // add to end of new depth
        var newDepth = intInfo.depth + 1;
        while( newDepth > depths.length - 1 ){
          depths.push([]);
        }
        depths[ newDepth ].push( ele );

        info.depth = newDepth;
        info.index = depths[newDepth].length - 1;
      }

      assignDepthsToEles();
    }

    // find min distance we need to leave between nodes
    var minDistance = 0;
    if( options.avoidOverlap ){
      for( var i = 0; i < nodes.length; i++ ){
        var w = nodes[i].outerWidth();
        var h = nodes[i].outerHeight();
        
        minDistance = Math.max(minDistance, w, h);
      }
      minDistance *= 1.75; // just to have some nice spacing
    }

    // get the weighted percent for an element based on its connectivity to other levels
    var cachedWeightedPercent = {};
    var getWeightedPercent = function( ele ){
      if( cachedWeightedPercent[ ele.id() ] ){
        return cachedWeightedPercent[ ele.id() ];
      }

      var eleDepth = ele._private.scratch.breadthfirst.depth;
      var neighbors = ele.neighborhood().nodes();
      var percent = 0;
      var samples = 0;

      for( var i = 0; i < neighbors.length; i++ ){
        var neighbor = neighbors[i];
        var index = neighbor._private.scratch.breadthfirst.index;
        var depth = neighbor._private.scratch.breadthfirst.depth;
        var nDepth = depths[depth].length;

        if( eleDepth > depth || eleDepth === 0 ){ // only get influenced by elements above
          percent += index / nDepth;
          samples++;
        }
      }

      samples = Math.max(1, samples);
      percent = percent / samples;

      if( samples === 0 ){ // so lone nodes have a "don't care" state in sorting
        percent = undefined;
      }

      cachedWeightedPercent[ ele.id() ] = percent;
      return percent;
    };


    // rearrange the indices in each depth level based on connectivity

    var sortFn = function(a, b){
      var apct = getWeightedPercent( a );
      var bpct = getWeightedPercent( b );

      return apct - bpct;
    };

    for( var times = 0; times < 3; times++ ){ // do it a few times b/c the depths are dynamic and we want a more stable result

      for( var i = 0; i < depths.length; i++ ){
        depths[i] = depths[i].sort( sortFn );
      }
      assignDepthsToEles(); // and update

    }

    var biggestDepthSize = 0;
    for( var i = 0; i < depths.length; i++ ){
      biggestDepthSize = Math.max( depths[i].length, biggestDepthSize );
    }

    var center = {
      x: bb.x1 + bb.w/2,
      y: bb.x1 + bb.h/2
    };
   
    var getPosition = function( ele, isBottomDepth ){
      var info = ele._private.scratch.breadthfirst;
      var depth = info.depth;
      var index = info.index;
      var depthSize = depths[depth].length;

      if( options.strictHierarchy ){
        depthSize = biggestDepthSize;
      }

      var distanceX = Math.max( bb.w / (depthSize + 1), minDistance );
      var distanceY = Math.max( bb.h / (depths.length + 1), minDistance );
      var radiusStepSize = Math.min( bb.w / 2 / depths.length, bb.h / 2 / depths.length );
      radiusStepSize = Math.max( radiusStepSize, minDistance );

      if( options.strictHierarchy && !options.circle ){
        
        var epos = {
          x: center.x + (index + 1 - (depthSize + 1)/2) * distanceX,
          y: (depth + 1) * distanceY
        };

        if( isBottomDepth ){
          return epos;
        }

        var succs = successors[ ele.id() ];
        if( succs ){
          epos.x = 0;

          for( var i = 0 ; i < succs.length; i++ ){
            var spos = pos[ succs[i].id() ];
            
            epos.x += spos.x;
          }

          epos.x /= succs.length;
        } else {
          //debugger;
        }

        return epos;

      } else {
        if( options.circle ){
          var radius = radiusStepSize * depth + radiusStepSize - (depths.length > 0 && depths[0].length <= 3 ? radiusStepSize/2 : 0);
          var theta = 2 * Math.PI / depths[depth].length * index;

          if( depth === 0 && depths[0].length === 1 ){
            radius = 1;
          }

          return {
            x: center.x + radius * Math.cos(theta),
            y: center.y + radius * Math.sin(theta)
          };

        } else {
          return {
            x: center.x + (index + 1 - (depthSize + 1)/2) * distanceX,
            y: (depth + 1) * distanceY
          };
        }
      }
      
    };

    // get positions in reverse depth order
    var pos = {};
    for( var i = depths.length - 1; i >=0; i-- ){
      var depth = depths[i];

      for( var j = 0; j < depth.length; j++ ){
        var node = depth[j];

        pos[ node.id() ] = getPosition( node, i === depths.length - 1 );
      }
    }

    nodes.layoutPositions(this, options, function(){
      return pos[ this.id() ];
    });
    
    return this; // chaining
  };
  
  $$('layout', 'breadthfirst', BreadthFirstLayout);
  
})( cytoscape );

;(function($$){ 'use strict';
  
  var defaults = {
    fit: true, // whether to fit the viewport to the graph
    padding: 30, // the padding on fit
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    avoidOverlap: true, // prevents node overlap, may overflow boundingBox and radius if not enough space
    radius: undefined, // the radius of the circle
    startAngle: 3/2 * Math.PI, // the position of the first node
    counterclockwise: false, // whether the layout should go counterclockwise (true) or clockwise (false)
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function CircleLayout( options ){
    this.options = $$.util.extend({}, defaults, options);
  }
  
  CircleLayout.prototype.run = function(){
    var params = this.options;
    var options = params;
    
    var cy = params.cy;
    var eles = options.eles;
      
    var nodes = eles.nodes().not(':parent');
    
    var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
      x1: 0, y1: 0, w: cy.width(), h: cy.height()
    } );

    var center = {
      x: bb.x1 + bb.w/2,
      y: bb.y1 + bb.h/2
    };
    
    var theta = options.startAngle;
    var dTheta = 2 * Math.PI / nodes.length;
    var r;

    var minDistance = 0;
    for( var i = 0; i < nodes.length; i++ ){
      var w = nodes[i].outerWidth();
      var h = nodes[i].outerHeight();
      
      minDistance = Math.max(minDistance, w, h);
    }

    if( $$.is.number(options.radius) ){
      r = options.radius;
    } else if( nodes.length <= 1 ){
      r = 0;
    } else {
      r = Math.min( bb.h, bb.w )/2 - minDistance;
    }

    // calculate the radius
    if( nodes.length > 1 && options.avoidOverlap ){ // but only if more than one node (can't overlap)
      minDistance *= 1.75; // just to have some nice spacing

      var dTheta = 2 * Math.PI / nodes.length;
      var dcos = Math.cos(dTheta) - Math.cos(0);
      var dsin = Math.sin(dTheta) - Math.sin(0);
      var rMin = Math.sqrt( minDistance * minDistance / ( dcos*dcos + dsin*dsin ) ); // s.t. no nodes overlapping
      r = Math.max( rMin, r );
    }

    var getPos = function( i, ele ){
      var rx = r * Math.cos( theta );
      var ry = r * Math.sin( theta );
      var pos = {
        x: center.x + rx,
        y: center.y + ry
      };

      theta = options.counterclockwise ? theta - dTheta : theta + dTheta;
      return pos;
    };
    
    nodes.layoutPositions( this, options, getPos );

    return this; // chaining
  };
  
  $$('layout', 'circle', CircleLayout);
  
})( cytoscape );

;(function($$){ 'use strict';

  // default layout options
  var defaults = {
    animate: true, // whether to show the layout as it's running
    refresh: 1, // number of ticks per frame; higher is faster but more jerky
    maxSimulationTime: 4000, // max length in ms to run the layout
    ungrabifyWhileSimulating: false, // so you can't drag nodes during layout
    fit: true, // on every layout reposition of nodes, fit the viewport
    padding: 30, // padding around the simulation
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }

    // layout event callbacks
    ready: function(){}, // on layoutready
    stop: function(){}, // on layoutstop

    // positioning options
    randomize: false, // use random node positions at beginning of layout
    avoidOverlap: true, // if true, prevents overlap of node bounding boxes
    handleDisconnected: true, // if true, avoids disconnected components from overlapping
    nodeSpacing: function( node ){ return 10; }, // extra spacing around nodes
    flow: undefined, // use DAG/tree flow layout if specified, e.g. { axis: 'y', minSeparation: 30 }
    alignment: undefined, // relative alignment constraints on nodes, e.g. function( node ){ return { x: 0, y: 1 } }

    // different methods of specifying edge length
    // each can be a constant numerical value or a function like `function( edge ){ return 2; }`
    edgeLength: undefined, // sets edge length directly in simulation
    edgeSymDiffLength: undefined, // symmetric diff edge length in simulation
    edgeJaccardLength: undefined, // jaccard edge length in simulation

    // iterations of cola algorithm; uses default values on undefined
    unconstrIter: undefined, // unconstrained initial layout iterations
    userConstIter: undefined, // initial layout iterations with user-specified constraints
    allConstIter: undefined, // initial layout iterations with all constraints including non-overlap

    // infinite layout options
    infinite: false // overrides all other options for a forces-all-the-time mode
  };

  // constructor
  // options : object containing layout options
  function ColaLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options); 
  }

  // runs the layout
  ColaLayout.prototype.run = function(){
    var layout = this;
    var options = this.options;

    $$.util.require('cola', function(cola){

      var cy = options.cy; // cy is automatically populated for us in the constructor
      var eles = options.eles;
      var nodes = eles.nodes();
      var edges = eles.edges();
      var ready = false;
      
      var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
        x1: 0, y1: 0, w: cy.width(), h: cy.height()
      } );

      var getOptVal = function( val, ele ){
        if( $$.is.fn(val) ){
          var fn = val;
          return fn.apply( ele, [ ele ] );
        } else {
          return val;
        }
      };

      var updateNodePositions = function(){
        var x = { min: Infinity, max: -Infinity };
        var y = { min: Infinity, max: -Infinity };

        for( var i = 0; i < nodes.length; i++ ){
          var node = nodes[i];
          var scratch = node._private.scratch.cola;

          x.min = Math.min( x.min, scratch.x );
          x.max = Math.max( x.max, scratch.x );

          y.min = Math.min( y.min, scratch.y );
          y.max = Math.max( y.max, scratch.y );
        }

        nodes.positions(function(i, node){
          var pos = node._private.position;
          var scratch = node._private.scratch.cola;

          if( !node.grabbed() ){
            pos.x = bb.x1 + scratch.x - x.min;
            pos.y = bb.y1 + scratch.y - y.min;
          }
        });

        if( !ready ){
          onReady();
          ready = true;
        }

        if( options.fit ){
          cy.fit( options.padding );
        }
      };

      var onDone = function(){
        layout.manuallyStopped = false;

        if( options.ungrabifyWhileSimulating ){
          grabbableNodes.grabify();
        }

        nodes.off('grab free position', grabHandler);
        nodes.off('lock unlock', lockHandler);

        // trigger layoutstop when the layout stops (e.g. finishes)
        layout.one('layoutstop', options.stop);
        layout.trigger({ type: 'layoutstop', layout: layout });
      };

      var onReady = function(){
        // trigger layoutready when each node has had its position set at least once
        layout.one('layoutready', options.ready);
        layout.trigger({ type: 'layoutready', layout: layout });
      };

      var ticksPerFrame = options.refresh;
      var tickSkip = 1; // frames until a tick; used to slow down sim for debugging

      if( options.refresh < 0 ){
        tickSkip = Math.abs( options.refresh );
        ticksPerFrame = 1;
      } else {
        ticksPerFrame = Math.max( 1, ticksPerFrame ); // at least 1
      }

      var adaptor = cola.adaptor({
        trigger: function( e ){ // on sim event
          switch( e.type ){
            case 'tick':
              if( options.animate ){
                updateNodePositions();
              }
              break;

            case 'end': 
              updateNodePositions();
              if( !options.infinite || layout.manuallyStopped ){ onDone(); }           
              break;
          }
        },

        kick: function( tick ){ // kick off the simulation
          var skip = 0;

          var inftick = function(){
            var ret = tick();

            if( ret && options.infinite ){ // resume layout if done
              adaptor.resume(); // resume => new kick
            }
            
            return ret; // allow regular finish b/c of new kick
          };

          var multitick = function(){ // multiple ticks in a row
            var ret;

            // skip ticks to slow down layout for debugging
            var thisSkip = skip;
            skip = (skip + 1) % tickSkip;
            if( thisSkip !== 0 ){
              return false;
            }

            for( var i = 0; i < ticksPerFrame && !ret; i++ ){
              ret = ret || inftick(); // pick up true ret vals => sim done
            }

            return ret;
          };

          if( options.animate ){
            var frame = function(){
              if( multitick() ){ return; }

              $$.util.requestAnimationFrame( frame );
            };

            $$.util.requestAnimationFrame( frame );
          } else {
            while( !inftick() ){}
          }
        },

        on: function( type, listener ){}, // dummy; not needed

        drag: function(){} // TODO
      });
      layout.adaptor = adaptor;

      // if set no grabbing during layout
      var grabbableNodes = nodes.filter(':grabbable');
      if( options.ungrabifyWhileSimulating ){
        grabbableNodes.ungrabify();
      }

      // handle node dragging
      var grabHandler;
      nodes.on('grab free position', grabHandler = function(e){
        var node = this;
        var scrCola = node._private.scratch.cola;
        var pos = node._private.position;

        if( node.grabbed() ){
          scrCola.x = pos.x - bb.x1;
          scrCola.y = pos.y - bb.y1;

          adaptor.dragstart( scrCola );
        } else if( $$.is.number(scrCola.x) && $$.is.number(scrCola.y) ){
          pos.x = scrCola.x + bb.x1;
          pos.y = scrCola.y + bb.y1;
        }

        switch( e.type ){
          case 'grab':
            adaptor.dragstart( scrCola );
            adaptor.resume();
            break;
          case 'free':
            adaptor.dragend( scrCola );
            break;
        }
        
      });

      var lockHandler;
      nodes.on('lock unlock', lockHandler = function(e){
        var node = this;
        var scrCola = node._private.scratch.cola;
      
        if( node.locked() ){
          adaptor.dragstart( scrCola );
        } else {
          adaptor.dragend( scrCola );
        }
      });

      var nonparentNodes = nodes.stdFilter(function( node ){
        return !node.isParent();
      });

      // add nodes to cola
      adaptor.nodes( nonparentNodes.map(function( node, i ){
        var padding = getOptVal( options.nodeSpacing, node );
        var pos = node.position();

        var struct = node._private.scratch.cola = {
          x: options.randomize ? Math.round( Math.random() * bb.w ) : pos.x,
          y: options.randomize ? Math.round( Math.random() * bb.h ) : pos.y,
          width: node.outerWidth() + 2*padding,
          height: node.outerHeight() + 2*padding,
          index: i
        };

        return struct;
      }) );

      if( options.alignment ){ // then set alignment constraints

        var offsetsX = [];
        var offsetsY = [];

        nonparentNodes.forEach(function( node ){
          var align = getOptVal( options.alignment, node );
          var scrCola = node._private.scratch.cola;
          var index = scrCola.index;

          if( !align ){ return; }

          if( align.x != null ){
            offsetsX.push({
              node: index,
              offset: align.x
            });
          }

          if( align.y != null ){
            offsetsY.push({
              node: index,
              offset: align.y
            });
          }
        });

        // add alignment constraints on nodes
        var constraints = [];

        if( offsetsX.length > 0 ){
          constraints.push({
            type: 'alignment',
            axis: 'x',
            offsets: offsetsX
          });
        }

        if( offsetsY.length > 0 ){
          constraints.push({
            type: 'alignment',
            axis: 'y',
            offsets: offsetsY
          });
        }
        
        adaptor.constraints( constraints );

      }

      // add compound nodes to cola
      adaptor.groups( nodes.stdFilter(function( node ){
        return node.isParent();
      }).map(function( node, i ){ // add basic group incl leaf nodes
        node._private.scratch.cola = {
          index: i,

          leaves: node.children().stdFilter(function( child ){
            return !child.isParent();
          }).map(function( child ){
            return child[0]._private.scratch.cola.index;
          })
        };

        return node;
      }).map(function( node ){ // add subgroups
        node._private.scratch.cola.groups = node.children().stdFilter(function( child ){
          return child.isParent();
        }).map(function( child ){
          return child._private.scratch.cola.index;
        });

        return node._private.scratch.cola;
      }) );

      // get the edge length setting mechanism
      var length;
      var lengthFnName;
      if( options.edgeLength != null ){
        length = options.edgeLength;
        lengthFnName = 'linkDistance';
      } else if( options.edgeSymDiffLength != null ){
        length = options.edgeSymDiffLength;
        lengthFnName = 'symmetricDiffLinkLengths';
      } else if( options.edgeJaccardLength != null ){
        length = options.edgeJaccardLength;
        lengthFnName = 'jaccardLinkLengths';
      } else {
        length = 100;
        lengthFnName = 'linkDistance';
      }

      var lengthGetter = function( link ){
        return link.calcLength;
      };

      // add the edges to cola
      adaptor.links( edges.stdFilter(function( edge ){
        return !edge.source().isParent() && !edge.target().isParent();
      }).map(function( edge, i ){
        var c = edge._private.scratch.cola = {
          source: edge.source()[0]._private.scratch.cola.index,
          target: edge.target()[0]._private.scratch.cola.index
        };

        if( length != null ){
          c.calcLength = getOptVal( length, edge );
        }

        return c;
      }) );

      adaptor.size([ bb.w, bb.h ]);

      if( length != null ){
        adaptor[ lengthFnName ]( lengthGetter );
      }

      // set the flow of cola
      if( options.flow ){
        var flow;
        var defAxis = 'y';
        var defMinSep = 50;

        if( $$.is.string(options.flow) ){
          flow = {
            axis: options.flow,
            minSeparation: defMinSep
          };
        } else if( $$.is.number(options.flow) ){
          flow = {
            axis: defAxis,
            minSeparation: options.flow
          };
        } else if( $$.is.plainObject(options.flow) ){
          flow = options.flow;

          flow.axis = flow.axis || defAxis;
          flow.minSeparation = flow.minSeparation != null ? flow.minSeparation : defMinSep;
        } else { // e.g. options.flow: true
          flow = {
            axis: defAxis,
            minSeparation: defMinSep
          };
        }

        adaptor.flowLayout( flow.axis , flow.minSeparation );
      }

      adaptor
        .avoidOverlaps( options.avoidOverlap )
        .handleDisconnected( options.handleDisconnected )
        .start( options.unconstrIter, options.userConstIter, options.allConstIter)
      ;

      layout.trigger({ type: 'layoutstart', layout: layout });

      if( !options.infinite ){
        setTimeout(function(){
          adaptor.stop();
        }, options.maxSimulationTime);
      }

    }); // require

    return this; // chaining
  };

  // called on continuous layouts to stop them before they finish
  ColaLayout.prototype.stop = function(){
    if( this.adaptor ){
      this.manuallyStopped = true;
      this.adaptor.stop();
    }

    return this; // chaining
  };

  // register the layout
  $$('layout', 'cola', ColaLayout);

})(cytoscape);
;(function($$){ 'use strict';
  
  var defaults = {
    fit: true, // whether to fit the viewport to the graph
    padding: 30, // the padding on fit
    startAngle: 3/2 * Math.PI, // the position of the first node
    counterclockwise: false, // whether the layout should go counterclockwise/anticlockwise (true) or clockwise (false)
    minNodeSpacing: 10, // min spacing between outside of nodes (used for radius adjustment)
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    avoidOverlap: true, // prevents node overlap, may overflow boundingBox if not enough space
    height: undefined, // height of layout area (overrides container height)
    width: undefined, // width of layout area (overrides container width)
    concentric: function(){ // returns numeric value for each node, placing higher nodes in levels towards the centre
      return this.degree();
    },
    levelWidth: function(nodes){ // the variation of concentric values in each level
      return nodes.maxDegree() / 4;
    },
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function ConcentricLayout( options ){
    this.options = $$.util.extend({}, defaults, options);
  }
  
  ConcentricLayout.prototype.run = function(){
    var params = this.options;
    var options = params;
    
    var cy = params.cy;
    
    var eles = options.eles;
    var nodes = eles.nodes().not(':parent');
    
    var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
      x1: 0, y1: 0, w: cy.width(), h: cy.height()
    } );

    var center = {
      x: bb.x1 + bb.w/2,
      y: bb.y1 + bb.h/2
    };
    
    var nodeValues = []; // { node, value }
    var theta = options.startAngle;
    var maxNodeSize = 0;

    for( var i = 0; i < nodes.length; i++ ){
      var node = nodes[i];
      var value;
      
      // calculate the node value
      value = options.concentric.call(node);
      nodeValues.push({
        value: value,
        node: node
      });

      // for style mapping
      node._private.layoutData.concentric = value;
    }

    // in case we used the `concentric` in style
    nodes.updateStyle();

    // calculate max size now based on potentially updated mappers
    for( var i = 0; i < nodes.length; i++ ){
      var node = nodes[i];

      maxNodeSize = Math.max( maxNodeSize, node.outerWidth(), node.outerHeight() );
    }

    // sort node values in descreasing order
    nodeValues.sort(function(a, b){
      return b.value - a.value;
    });

    var levelWidth = options.levelWidth( nodes );

    // put the values into levels
    var levels = [ [] ];
    var currentLevel = levels[0];
    for( var i = 0; i < nodeValues.length; i++ ){
      var val = nodeValues[i];

      if( currentLevel.length > 0 ){
        var diff = Math.abs( currentLevel[0].value - val.value );

        if( diff >= levelWidth ){
          currentLevel = [];
          levels.push( currentLevel );
        }
      }

      currentLevel.push( val );
    }

    // create positions from levels

    var pos = {}; // id => position
    var r = 0;
    var minDist = maxNodeSize + options.minNodeSpacing; // min dist between nodes

    if( !options.avoidOverlap ){ // then strictly constrain to bb
      var firstLvlHasMulti = levels.length > 0 && levels[0].length > 1;
      var maxR = ( Math.min(bb.w, bb.h) / 2 - minDist );
      var rStep = maxR / ( levels.length + firstLvlHasMulti ? 1 : 0 );

      minDist = Math.min( minDist, rStep );
    }

    for( var i = 0; i < levels.length; i++ ){
      var level = levels[i];
      var dTheta = 2 * Math.PI / level.length;

      // calculate the radius
      if( level.length > 1 && options.avoidOverlap ){ // but only if more than one node (can't overlap)
        var dcos = Math.cos(dTheta) - Math.cos(0);
        var dsin = Math.sin(dTheta) - Math.sin(0);
        var rMin = Math.sqrt( minDist * minDist / ( dcos*dcos + dsin*dsin ) ); // s.t. no nodes overlapping
        r = Math.max( rMin, r );
      }

      for( var j = 0; j < level.length; j++ ){
        var val = level[j];
        var theta = options.startAngle + (options.counterclockwise ? 1 : -1) * dTheta * j;

        var p = {
          x: center.x + r * Math.cos(theta),
          y: center.y + r * Math.sin(theta)
        };

        pos[ val.node.id() ] = p;
      }

      r += minDist;
      
    } 

    // position the nodes
    nodes.layoutPositions(this, options, function(){
      var id = this.id();

      return pos[id];
    });
  
    return this; // chaining
  };
  
  $$('layout', 'concentric', ConcentricLayout);
  
})( cytoscape );

/*
  The CoSE layout was written by Gerardo Huck.

  Modifications tracked on Github.
*/

;(function($$) { 'use strict';

  var DEBUG;

  /**
   * @brief :  default layout options
   */
  var defaults = {
    // Called on `layoutready`
    ready               : function() {},

    // Called on `layoutstop`
    stop                : function() {},

    // Whether to animate while running the layout
    animate             : true,

    // Number of iterations between consecutive screen positions update (0 -> only updated on the end)
    refresh             : 4,
    
    // Whether to fit the network view after when done
    fit                 : true, 

    // Padding on fit
    padding             : 30, 

    // Constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    boundingBox         : undefined,

    // Whether to randomize node positions on the beginning
    randomize           : true,
    
    // Whether to use the JS console to print debug messages
    debug               : false,

    // Node repulsion (non overlapping) multiplier
    nodeRepulsion       : 400000,
    
    // Node repulsion (overlapping) multiplier
    nodeOverlap         : 10,
    
    // Ideal edge (non nested) length
    idealEdgeLength     : 10,
    
    // Divisor to compute edge forces
    edgeElasticity      : 100,
    
    // Nesting factor (multiplier) to compute ideal edge length for nested edges
    nestingFactor       : 5, 
    
    // Gravity force (constant)
    gravity             : 250, 
    
    // Maximum number of iterations to perform
    numIter             : 100,
    
    // Initial temperature (maximum node displacement)
    initialTemp         : 200,
    
    // Cooling factor (how the temperature is reduced between consecutive iterations
    coolingFactor       : 0.95, 
    
    // Lower temperature threshold (below this point the layout will end)
    minTemp             : 1.0
  };


  /**
   * @brief       : constructor
   * @arg options : object containing layout options
   */
  function CoseLayout(options) {
    this.options = $$.util.extend({}, defaults, options); 
  }


  /**
   * @brief : runs the layout
   */
  CoseLayout.prototype.run = function() {
    var options = this.options;
    var cy      = options.cy;
    var layout  = this;

    layout.stopped = false;

    layout.trigger({ type: 'layoutstart', layout: layout });

    // Set DEBUG - Global variable
    if (true === options.debug) {
      DEBUG = true;
    } else {
      DEBUG = false;
    }

    // Get start time
    var startTime = new Date();

    // Initialize layout info
    var layoutInfo = createLayoutInfo(cy, layout, options);
    
    // Show LayoutInfo contents if debugging
    if (DEBUG) {
      printLayoutInfo(layoutInfo);
    }

    // If required, randomize node positions
    if (true === options.randomize) {
      randomizePositions(layoutInfo, cy);
    }

    updatePositions(layoutInfo, cy, options);

    var mainLoop = function(i){
      if( layout.stopped ){
        logDebug("Layout manually stopped. Stopping computation in step " + i);
        return false;
      }

      // Do one step in the phisical simulation
      step(layoutInfo, cy, options, i);
      
      // Update temperature
      layoutInfo.temperature = layoutInfo.temperature * options.coolingFactor;
      logDebug("New temperature: " + layoutInfo.temperature);

      if (layoutInfo.temperature < options.minTemp) {
        logDebug("Temperature drop below minimum threshold. Stopping computation in step " + i);
        return false;
      }

      return true;
    };

    var done = function(){
      refreshPositions(layoutInfo, cy, options);

      // Fit the graph if necessary
      if (true === options.fit) {
        cy.fit( options.padding );
      }
      
      // Get end time
      var endTime = new Date();

      console.info('Layout took ' + (endTime - startTime) + ' ms');

      // Layout has finished
      layout.one('layoutstop', options.stop);
      layout.trigger({ type: 'layoutstop', layout: layout });
    };

    if( options.animate ){
      var i = 0;
      var frame = function(){

        var f = 0;
        var loopRet;
        while( f < options.refresh && i < options.numIter ){
          var loopRet = mainLoop(i);
          if( loopRet === false ){ break; }

          f++;
          i++;
        }

        refreshPositions(layoutInfo, cy, options);
        if( options.fit ){
          cy.fit( options.padding );
        }

        if ( loopRet !== false && i + 1 < options.numIter ) {
          $$.util.requestAnimationFrame( frame );
        } else {
          done();
        }
      };

      $$.util.requestAnimationFrame( frame );
    } else {
      for (var i = 0; i < options.numIter; i++) {
        if( mainLoop(i) === false ){ break; }
      }

      done();
    }
   
    return this; // chaining
  };


  /**
   * @brief : called on continuous layouts to stop them before they finish
   */
  CoseLayout.prototype.stop = function(){
    this.stopped = true;

    return this; // chaining
  };


  /**
   * @brief     : Creates an object which is contains all the data
   *              used in the layout process
   * @arg cy    : cytoscape.js object
   * @return    : layoutInfo object initialized
   */
  var createLayoutInfo = function(cy, layout, options) {
    // Shortcut
    var edges = options.eles.edges();
    var nodes = options.eles.nodes();

    var layoutInfo   = {
      layout       : layout,
      layoutNodes  : [], 
      idToIndex    : {},
      nodeSize     : nodes.size(),
      graphSet     : [],
      indexToGraph : [], 
      layoutEdges  : [],
      edgeSize     : edges.size(),
      temperature  : options.initialTemp,
      clientWidth  : cy.width(),
      clientHeight : cy.width(),
      boundingBox  : $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
                       x1: 0, y1: 0, w: cy.width(), h: cy.height()
                     } )
    }; 
    
    // Iterate over all nodes, creating layout nodes
    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var tempNode        = {};
      tempNode.id         = nodes[i].data('id');
      tempNode.parentId   = nodes[i].data('parent');      
      tempNode.children   = [];
      tempNode.positionX  = nodes[i].position('x');
      tempNode.positionY  = nodes[i].position('y');
      tempNode.offsetX    = 0;      
      tempNode.offsetY    = 0;
      tempNode.height     = nodes[i].height();
      tempNode.width      = nodes[i].width();
      tempNode.maxX       = tempNode.positionX + tempNode.width  / 2;
      tempNode.minX       = tempNode.positionX - tempNode.width  / 2;
      tempNode.maxY       = tempNode.positionY + tempNode.height / 2;
      tempNode.minY       = tempNode.positionY - tempNode.height / 2;
      tempNode.padLeft    = nodes[i]._private.style['padding-left'].pxValue;
      tempNode.padRight   = nodes[i]._private.style['padding-right'].pxValue;
      tempNode.padTop     = nodes[i]._private.style['padding-top'].pxValue;
      tempNode.padBottom  = nodes[i]._private.style['padding-bottom'].pxValue;
      
      // Add new node
      layoutInfo.layoutNodes.push(tempNode);
      // Add entry to id-index map
      layoutInfo.idToIndex[tempNode.id] = i;
    }

    // Inline implementation of a queue, used for traversing the graph in BFS order
    var queue = [];
    var start = 0;   // Points to the start the queue
    var end   = -1;  // Points to the end of the queue

    var tempGraph = [];

    // Second pass to add child information and 
    // initialize queue for hierarchical traversal
    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      var p_id = n.parentId;
      // Check if node n has a parent node
      if (null != p_id) {
      // Add node Id to parent's list of children
      layoutInfo.layoutNodes[layoutInfo.idToIndex[p_id]].children.push(n.id);
      } else {
      // If a node doesn't have a parent, then it's in the root graph
      queue[++end] = n.id;
      tempGraph.push(n.id);    
      }
    }
    
    // Add root graph to graphSet
    layoutInfo.graphSet.push(tempGraph);

    // Traverse the graph, level by level, 
    while (start <= end) {
      // Get the node to visit and remove it from queue
      var node_id  = queue[start++];
      var node_ix  = layoutInfo.idToIndex[node_id];
      var node     = layoutInfo.layoutNodes[node_ix];
      var children = node.children;
      if (children.length > 0) {
      // Add children nodes as a new graph to graph set
      layoutInfo.graphSet.push(children);
      // Add children to que queue to be visited
      for (var i = 0; i < children.length; i++) {
        queue[++end] = children[i];
      }
      }
    }

    // Create indexToGraph map
    for (var i = 0; i < layoutInfo.graphSet.length; i++) {      
      var graph = layoutInfo.graphSet[i];
      for (var j = 0; j < graph.length; j++) {
      var index = layoutInfo.idToIndex[graph[j]];
      layoutInfo.indexToGraph[index] = i;
      }
    }
    
    // Iterate over all edges, creating Layout Edges
    for (var i = 0; i < layoutInfo.edgeSize; i++) {
      var e = edges[i];
      var tempEdge = {};      
      tempEdge.id       = e.data('id');
      tempEdge.sourceId = e.data('source');
      tempEdge.targetId = e.data('target');

      // Compute ideal length
      var idealLength = options.idealEdgeLength;

      // Check if it's an inter graph edge
      var sourceIx    = layoutInfo.idToIndex[tempEdge.sourceId];
      var targetIx    = layoutInfo.idToIndex[tempEdge.targetId];
      var sourceGraph = layoutInfo.indexToGraph[sourceIx];
      var targetGraph = layoutInfo.indexToGraph[targetIx];

      if (sourceGraph != targetGraph) {
      // Find lowest common graph ancestor
      var lca = findLCA(tempEdge.sourceId, tempEdge.targetId, layoutInfo);

      // Compute sum of node depths, relative to lca graph
      var lcaGraph = layoutInfo.graphSet[lca];
      var depth    = 0;

      // Source depth
      var tempNode = layoutInfo.layoutNodes[sourceIx];
      while (-1 === $.inArray(tempNode.id, lcaGraph)) {
        tempNode = layoutInfo.layoutNodes[layoutInfo.idToIndex[tempNode.parentId]];
        depth++;
      }

      // Target depth
      tempNode = layoutInfo.layoutNodes[targetIx];
      while (-1 === $.inArray(tempNode.id, lcaGraph)) {
        tempNode = layoutInfo.layoutNodes[layoutInfo.idToIndex[tempNode.parentId]];
        depth++;
      }

      logDebug('LCA of nodes ' + tempEdge.sourceId + ' and ' + tempEdge.targetId +  
         ". Index: " + lca + " Contents: " + lcaGraph.toString() + 
         ". Depth: " + depth);

      // Update idealLength
      idealLength *= depth * options.nestingFactor;
      }

      tempEdge.idealLength = idealLength;

      layoutInfo.layoutEdges.push(tempEdge);
    }

    // Finally, return layoutInfo object
    return layoutInfo;
  };

  
  /**
   * @brief : This function finds the index of the lowest common 
   *          graph ancestor between 2 nodes in the subtree 
   *          (from the graph hierarchy induced tree) whose
   *          root is graphIx
   *
   * @arg node1: node1's ID
   * @arg node2: node2's ID
   * @arg layoutInfo: layoutInfo object
   *
   */
  var findLCA = function(node1, node2, layoutInfo) {
    // Find their common ancester, starting from the root graph
    var res = findLCA_aux(node1, node2, 0, layoutInfo);
    if (2 > res.count) {
      // If aux function couldn't find the common ancester, 
      // then it is the root graph
      return 0;
    } else {
      return res.graph;
    }
  };


  /**
   * @brief          : Auxiliary function used for LCA computation
   * 
   * @arg node1      : node1's ID
   * @arg node2      : node2's ID
   * @arg graphIx    : subgraph index
   * @arg layoutInfo : layoutInfo object
   *
   * @return         : object of the form {count: X, graph: Y}, where:
   *                   X is the number of ancesters (max: 2) found in 
   *                   graphIx (and it's subgraphs),
   *                   Y is the graph index of the lowest graph containing 
   *                   all X nodes
   */
  var findLCA_aux = function(node1, node2, graphIx, layoutInfo) {
    var graph = layoutInfo.graphSet[graphIx];
    // If both nodes belongs to graphIx
    if (-1 < $.inArray(node1, graph) && -1 < $.inArray(node2, graph)) {
      return {count:2, graph:graphIx};
    }

    // Make recursive calls for all subgraphs
    var c = 0;
    for (var i = 0; i < graph.length; i++) {
      var nodeId   = graph[i];
      var nodeIx   = layoutInfo.idToIndex[nodeId];
      var children = layoutInfo.layoutNodes[nodeIx].children;

      // If the node has no child, skip it
      if (0 === children.length) {
      continue;
      }

      var childGraphIx = layoutInfo.indexToGraph[layoutInfo.idToIndex[children[0]]];
      var result = findLCA_aux(node1, node2, childGraphIx, layoutInfo);
      if (0 === result.count) {
      // Neither node1 nor node2 are present in this subgraph
      continue;
      } else if (1 === result.count) {
      // One of (node1, node2) is present in this subgraph
      c++;
      if (2 === c) {
        // We've already found both nodes, no need to keep searching
        break;
      }
      } else {
      // Both nodes are present in this subgraph
      return result;
      }      
    }
    
    return {count:c, graph:graphIx};
  };


  /**
   * @brief: printsLayoutInfo into js console
   *         Only used for debbuging 
   */
  var printLayoutInfo = function(layoutInfo) {
    if (!DEBUG) {
      return;
    }
    console.debug("layoutNodes:");
    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      var s = 
      "\nindex: "     + i + 
      "\nId: "        + n.id + 
      "\nChildren: "  + n.children.toString() +  
      "\nparentId: "  + n.parentId  + 
      "\npositionX: " + n.positionX + 
      "\npositionY: " + n.positionY +
      "\nOffsetX: " + n.offsetX + 
      "\nOffsetY: " + n.offsetY + 
      "\npadLeft: " + n.padLeft + 
      "\npadRight: " + n.padRight + 
      "\npadTop: " + n.padTop + 
      "\npadBottom: " + n.padBottom;

      console.debug(s);    
    }  
    
    console.debug('idToIndex');
    for (var i in layoutInfo.idToIndex) {
      console.debug("Id: " + i + "\nIndex: " + layoutInfo.idToIndex[i]);
    }

    console.debug('Graph Set');
    var set = layoutInfo.graphSet;
    for (var i = 0; i < set.length; i ++) {
      console.debug("Set : " + i + ": " + set[i].toString());
    } 

    var s = 'IndexToGraph';
    for (var i = 0; i < layoutInfo.indexToGraph.length; i ++) {
      s += "\nIndex : " + i + " Graph: "+ layoutInfo.indexToGraph[i];
    }
    console.debug(s);

    s = 'Layout Edges';
    for (var i = 0; i < layoutInfo.layoutEdges.length; i++) {
      var e = layoutInfo.layoutEdges[i];
      s += "\nEdge Index: " + i + " ID: " + e.id + 
      " SouceID: " + e.sourceId + " TargetId: " + e.targetId + 
      " Ideal Length: " + e.idealLength;
    }
    console.debug(s);

    s =  "nodeSize: " + layoutInfo.nodeSize;
    s += "\nedgeSize: " + layoutInfo.edgeSize;
    s += "\ntemperature: " + layoutInfo.temperature;
    console.debug(s);

    return;
  };


  /**
   * @brief : Randomizes the position of all nodes
   */
  var randomizePositions = function(layoutInfo, cy) {
    var width     = layoutInfo.clientWidth;
    var height    = layoutInfo.clientHeight;

    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      // No need to randomize compound nodes
      if (true || 0 === n.children.length) {
        n.positionX = Math.random() * width;
        n.positionY = Math.random() * height;
      }
    }
  };

  
  /**
   * @brief          : Updates the positions of nodes in the network
   * @arg layoutInfo : LayoutInfo object
   * @arg cy         : Cytoscape object
   * @arg options    : Layout options
   */
  var refreshPositions = function(layoutInfo, cy, options) {  
    var s = 'Refreshing positions';
    logDebug(s);

    var layout = layoutInfo.layout;
    var nodes = options.eles.nodes();
    var bb = layoutInfo.boundingBox;
    var coseBB = { x1: Infinity, x2: -Infinity, y1: Infinity, y2: -Infinity };
    
    if( options.boundingBox ){
      nodes.forEach(function( node ){
        var lnode = layoutInfo.layoutNodes[layoutInfo.idToIndex[node.data('id')]];

        coseBB.x1 = Math.min( coseBB.x1, lnode.positionX );
        coseBB.x2 = Math.max( coseBB.x2, lnode.positionX );

        coseBB.y1 = Math.min( coseBB.y1, lnode.positionY );
        coseBB.y2 = Math.max( coseBB.y2, lnode.positionY );
      });

      coseBB.w = coseBB.x2 - coseBB.x1;
      coseBB.h = coseBB.y2 - coseBB.y1;
    }

    nodes.positions(function(i, ele) {
      var lnode = layoutInfo.layoutNodes[layoutInfo.idToIndex[ele.data('id')]];
      s = "Node: " + lnode.id + ". Refreshed position: (" + 
      lnode.positionX + ", " + lnode.positionY + ").";
      logDebug(s);

      if( options.boundingBox ){ // then add extra bounding box constraint
        var pctX = (lnode.positionX - coseBB.x1) / coseBB.w;
        var pctY = (lnode.positionY - coseBB.y1) / coseBB.h;

        return {
          x: bb.x1 + pctX * bb.w,
          y: bb.y1 + pctY * bb.h
        };
      } else {
        return {
          x: lnode.positionX,
          y: lnode.positionY
        };
      }
    });

    // Trigger layoutReady only on first call
    if (true !== layoutInfo.ready) {
      s = 'Triggering layoutready';
      logDebug(s);
      layoutInfo.ready = true;
      layout.one('layoutready', options.ready);
      layout.trigger({ type: 'layoutready', layout: this });
    }
  };


  /**
   * @brief          : Performs one iteration of the physical simulation
   * @arg layoutInfo : LayoutInfo object already initialized
   * @arg cy         : Cytoscape object
   * @arg options    : Layout options
   */
  var step = function(layoutInfo, cy, options, step) {  
    var s = "\n\n###############################";
    s += "\nSTEP: " + step;
    s += "\n###############################\n";
    logDebug(s);

    // Calculate node repulsions
    calculateNodeForces(layoutInfo, cy, options);
    // Calculate edge forces
    calculateEdgeForces(layoutInfo, cy, options);
    // Calculate gravity forces
    calculateGravityForces(layoutInfo, cy, options);
    // Propagate forces from parent to child
    propagateForces(layoutInfo, cy, options);
    // Update positions based on calculated forces
    updatePositions(layoutInfo, cy, options);
  };

  
  /**
   * @brief : Computes the node repulsion forces
   */
  var calculateNodeForces = function(layoutInfo, cy, options) {
    // Go through each of the graphs in graphSet
    // Nodes only repel each other if they belong to the same graph
    var s = 'calculateNodeForces';
    logDebug(s);
    for (var i = 0; i < layoutInfo.graphSet.length; i ++) {
      var graph    = layoutInfo.graphSet[i];
      var numNodes = graph.length;

      s = "Set: " + graph.toString();
      logDebug(s);

      // Now get all the pairs of nodes 
      // Only get each pair once, (A, B) = (B, A)
      for (var j = 0; j < numNodes; j++) {
      var node1 = layoutInfo.layoutNodes[layoutInfo.idToIndex[graph[j]]];
      for (var k = j + 1; k < numNodes; k++) {
        var node2 = layoutInfo.layoutNodes[layoutInfo.idToIndex[graph[k]]];
        nodeRepulsion(node1, node2, layoutInfo, cy, options);
      } 
      }
    } 
  };


  /**
   * @brief : Compute the node repulsion forces between a pair of nodes
   */
  var nodeRepulsion = function(node1, node2, layoutInfo, cy, options) {
    var s = "Node repulsion. Node1: " + node1.id + " Node2: " + node2.id;

    // Get direction of line connecting both node centers
    var directionX = node2.positionX - node1.positionX;
    var directionY = node2.positionY - node1.positionY;
    s += "\ndirectionX: " + directionX + ", directionY: " + directionY;

    // If both centers are the same, apply a random force
    if (0 === directionX && 0 === directionY) {
      s += "\nNodes have the same position.";
      return; // TODO
    }

    var overlap = nodesOverlap(node1, node2, directionX, directionY);
    
    if (overlap > 0) {
      s += "\nNodes DO overlap.";
      s += "\nOverlap: " + overlap;
      // If nodes overlap, repulsion force is proportional 
      // to the overlap
      var force    = options.nodeOverlap * overlap;

      // Compute the module and components of the force vector
      var distance = Math.sqrt(directionX * directionX + directionY * directionY);
      s += "\nDistance: " + distance;
      var forceX   = force * directionX / distance;
      var forceY   = force * directionY / distance;

    } else {
      s += "\nNodes do NOT overlap.";
      // If there's no overlap, force is inversely proportional 
      // to squared distance

      // Get clipping points for both nodes
      var point1 = findClippingPoint(node1, directionX, directionY);
      var point2 = findClippingPoint(node2, -1 * directionX, -1 * directionY);

      // Use clipping points to compute distance
      var distanceX   = point2.x - point1.x;
      var distanceY   = point2.y - point1.y;
      var distanceSqr = distanceX * distanceX + distanceY * distanceY;
      var distance    = Math.sqrt(distanceSqr);
      s += "\nDistance: " + distance;

      // Compute the module and components of the force vector
      var force  = options.nodeRepulsion / distanceSqr;
      var forceX = force * distanceX / distance;
      var forceY = force * distanceY / distance;
    }

    // Apply force
    node1.offsetX -= forceX;
    node1.offsetY -= forceY;
    node2.offsetX += forceX;
    node2.offsetY += forceY;

    s += "\nForceX: " + forceX + " ForceY: " + forceY;
    logDebug(s);

    return;
  };


  /**
   * @brief : Finds the point in which an edge (direction dX, dY) intersects 
   *          the rectangular bounding box of it's source/target node 
   */
  var findClippingPoint = function(node, dX, dY) {

    // Shorcuts
    var X = node.positionX;
    var Y = node.positionY;
    var H = node.height;
    var W = node.width;
    var dirSlope     = dY / dX;
    var nodeSlope    = H / W;

    var s = 'Computing clipping point of node ' + node.id + 
      " . Height:  " + H + ", Width: " + W + 
      "\nDirection " + dX + ", " + dY; 
    
    // Compute intersection
    var res = {};
    do {
      // Case: Vertical direction (up)
      if (0 === dX && 0 < dY) {
        res.x = X;
        s += "\nUp direction";
        res.y = Y + H / 2;
        break;
      }

      // Case: Vertical direction (down)
      if (0 === dX && 0 > dY) {
        res.x = X;
        res.y = Y + H / 2;
        s += "\nDown direction";
        break;
      }      

      // Case: Intersects the right border
      if (0 < dX && 
      -1 * nodeSlope <= dirSlope && 
      dirSlope <= nodeSlope) {
        res.x = X + W / 2;
        res.y = Y + (W * dY / 2 / dX);
        s += "\nRightborder";
        break;
      }

      // Case: Intersects the left border
      if (0 > dX && 
      -1 * nodeSlope <= dirSlope && 
      dirSlope <= nodeSlope) {
        res.x = X - W / 2;
        res.y = Y - (W * dY / 2 / dX);
        s += "\nLeftborder";
        break;
      }

      // Case: Intersects the top border
      if (0 < dY && 
      ( dirSlope <= -1 * nodeSlope ||
        dirSlope >= nodeSlope )) {
        res.x = X + (H * dX / 2 / dY);
        res.y = Y + H / 2;
        s += "\nTop border";
        break;
      }

      // Case: Intersects the bottom border
      if (0 > dY && 
      ( dirSlope <= -1 * nodeSlope ||
        dirSlope >= nodeSlope )) {
        res.x = X - (H * dX / 2 / dY);
        res.y = Y - H / 2;
        s += "\nBottom border";
        break;
      }

    } while (false);

    s += "\nClipping point found at " + res.x + ", " + res.y;
    logDebug(s);
    return res;
  };


  /**
   * @brief  : Determines whether two nodes overlap or not
   * @return : Amount of overlapping (0 => no overlap)
   */
  var nodesOverlap = function(node1, node2, dX, dY) {

    if (dX > 0) {
      var overlapX = node1.maxX - node2.minX;
    } else {
      var overlapX = node2.maxX - node1.minX;
    }

    if (dY > 0) {
      var overlapY = node1.maxY - node2.minY;
    } else {
      var overlapY = node2.maxY - node1.minY;
    }

    if (overlapX >= 0 && overlapY >= 0) {
      return Math.sqrt(overlapX * overlapX + overlapY * overlapY);
    } else {
      return 0;
    }
  };
    
  
  /**
   * @brief : Calculates all edge forces
   */
  var calculateEdgeForces = function(layoutInfo, cy, options) {
    // Iterate over all edges
    for (var i = 0; i < layoutInfo.edgeSize; i++) {
      // Get edge, source & target nodes
      var edge     = layoutInfo.layoutEdges[i];
      var sourceIx = layoutInfo.idToIndex[edge.sourceId];
      var source   = layoutInfo.layoutNodes[sourceIx];
      var targetIx = layoutInfo.idToIndex[edge.targetId];
      var target   = layoutInfo.layoutNodes[targetIx];

      // Get direction of line connecting both node centers
      var directionX = target.positionX - source.positionX;
      var directionY = target.positionY - source.positionY;
      
      // If both centers are the same, do nothing.
      // A random force has already been applied as node repulsion
      if (0 === directionX && 0 === directionY) {
      return;
      }

      // Get clipping points for both nodes
      var point1 = findClippingPoint(source, directionX, directionY);
      var point2 = findClippingPoint(target, -1 * directionX, -1 * directionY);


      var lx = point2.x - point1.x;
      var ly = point2.y - point1.y;
      var l  = Math.sqrt(lx * lx + ly * ly);

      var force  = Math.pow(edge.idealLength - l, 2) / options.edgeElasticity; 

      if (0 !== l) {
        var forceX = force * lx / l;
        var forceY = force * ly / l;
      } else {
        var forceX = 0;
        var forceY = 0;
      }

      // Add this force to target and source nodes
      source.offsetX += forceX;
      source.offsetY += forceY;
      target.offsetX -= forceX;
      target.offsetY -= forceY;

      var s = 'Edge force between nodes ' + source.id + ' and ' + target.id;
      s += "\nDistance: " + l + " Force: (" + forceX + ", " + forceY + ")";
      logDebug(s);
    }
  };


  /**
   * @brief : Computes gravity forces for all nodes
   */
  var calculateGravityForces = function(layoutInfo, cy, options) {
    var s = 'calculateGravityForces';
    logDebug(s);
    for (var i = 0; i < layoutInfo.graphSet.length; i ++) {
      var graph    = layoutInfo.graphSet[i];
      var numNodes = graph.length;

      s = "Set: " + graph.toString();
      logDebug(s);
          
      // Compute graph center
      if (0 === i) {
        var centerX   = layoutInfo.clientHeight / 2;
        var centerY   = layoutInfo.clientWidth  / 2;    
      } else {
        // Get Parent node for this graph, and use its position as center
        var temp    = layoutInfo.layoutNodes[layoutInfo.idToIndex[graph[0]]];
        var parent  = layoutInfo.layoutNodes[layoutInfo.idToIndex[temp.parentId]];
        var centerX = parent.positionX;
        var centerY = parent.positionY;
      }
      s = "Center found at: " + centerX + ", " + centerY;
      logDebug(s);

      // Apply force to all nodes in graph
      for (var j = 0; j < numNodes; j++) {
        var node = layoutInfo.layoutNodes[layoutInfo.idToIndex[graph[j]]];
        s = "Node: " + node.id;
        var dx = centerX - node.positionX;
        var dy = centerY - node.positionY;
        var d  = Math.sqrt(dx * dx + dy * dy);
        if (d > 1.0) { // TODO: Use global variable for distance threshold
          var fx = options.gravity * dx / d;
          var fy = options.gravity * dy / d;
          node.offsetX += fx;
          node.offsetY += fy;
          s += ": Applied force: " + fx + ", " + fy;
        } else {
          s += ": skypped since it's too close to center";
        }
        logDebug(s);
      }
    }
  };


  /**
   * @brief          : This function propagates the existing offsets from 
   *                   parent nodes to its descendents.
   * @arg layoutInfo : layoutInfo Object
   * @arg cy         : cytoscape Object
   * @arg options    : Layout options
   */
  var propagateForces = function(layoutInfo, cy, options) {  
    // Inline implementation of a queue, used for traversing the graph in BFS order
    var queue = [];
    var start = 0;   // Points to the start the queue
    var end   = -1;  // Points to the end of the queue

    logDebug('propagateForces');

    // Start by visiting the nodes in the root graph
    queue.push.apply(queue, layoutInfo.graphSet[0]);
    end += layoutInfo.graphSet[0].length;

    // Traverse the graph, level by level, 
    while (start <= end) {
      // Get the node to visit and remove it from queue
      var nodeId    = queue[start++];
      var nodeIndex = layoutInfo.idToIndex[nodeId];
      var node      = layoutInfo.layoutNodes[nodeIndex];
      var children  = node.children;

      // We only need to process the node if it's compound
      if (0 < children.length) {    
      var offX = node.offsetX;
      var offY = node.offsetY;

      var s = "Propagating offset from parent node : " + node.id + 
        ". OffsetX: " + offX + ". OffsetY: " + offY;
      s += "\n Children: " + children.toString();
      logDebug(s);
      
      for (var i = 0; i < children.length; i++) {
        var childNode = layoutInfo.layoutNodes[layoutInfo.idToIndex[children[i]]];
        // Propagate offset
        childNode.offsetX += offX;
        childNode.offsetY += offY;
        // Add children to queue to be visited
        queue[++end] = children[i];
      }
      
      // Reset parent offsets
      node.offsetX = 0;
      node.offsetY = 0;
      }
      
    }
  };


  /**
   * @brief : Updates the layout model positions, based on 
   *          the accumulated forces
   */
  var updatePositions = function(layoutInfo, cy, options) {
    var s = 'Updating positions';
    logDebug(s);

    // Reset boundaries for compound nodes
    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      if (0 < n.children.length) {
        logDebug("Resetting boundaries of compound node: " + n.id);
        n.maxX = undefined;
        n.minX = undefined;
        n.maxY = undefined;
        n.minY = undefined;
      }
    }

    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      if (0 < n.children.length) {
        // No need to set compound node position
        logDebug("Skipping position update of node: " + n.id);
        continue;
      }
      s = "Node: " + n.id + " Previous position: (" + 
      n.positionX + ", " + n.positionY + ")."; 

      // Limit displacement in order to improve stability
      var tempForce = limitForce(n.offsetX, n.offsetY, layoutInfo.temperature);
      n.positionX += tempForce.x; 
      n.positionY += tempForce.y;
      n.offsetX = 0;
      n.offsetY = 0;
      n.minX    = n.positionX - n.width; 
      n.maxX    = n.positionX + n.width; 
      n.minY    = n.positionY - n.height; 
      n.maxY    = n.positionY + n.height; 
      s += " New Position: (" + n.positionX + ", " + n.positionY + ").";
      logDebug(s);

      // Update ancestry boudaries
      updateAncestryBoundaries(n, layoutInfo);
    }

    // Update size, position of compund nodes
    for (var i = 0; i < layoutInfo.nodeSize; i++) {
      var n = layoutInfo.layoutNodes[i];
      if (0 < n.children.length) {
        n.positionX = (n.maxX + n.minX) / 2;
        n.positionY = (n.maxY + n.minY) / 2;
        n.width     = n.maxX - n.minX;
        n.height    = n.maxY - n.minY;
        s = "Updating position, size of compound node " + n.id;
        s += "\nPositionX: " + n.positionX + ", PositionY: " + n.positionY;
        s += "\nWidth: " + n.width + ", Height: " + n.height;
        logDebug(s);
      }
    }  
  };


  /**
   * @brief : Limits a force (forceX, forceY) to be not 
   *          greater (in modulo) than max. 
   8          Preserves force direction. 
   */
  var limitForce = function(forceX, forceY, max) {
    var s = "Limiting force: (" + forceX + ", " + forceY + "). Max: " + max;
    var force = Math.sqrt(forceX * forceX + forceY * forceY);

    if (force > max) {
      var res = {
      x : max * forceX / force,
      y : max * forceY / force
      };      

    } else {
      var res = {
      x : forceX,
      y : forceY
      };
    }

    s += ".\nResult: (" + res.x + ", " + res.y + ")";
    logDebug(s);

    return res;
  };


  /**
   * @brief : Function used for keeping track of compound node 
   *          sizes, since they should bound all their subnodes.
   */
  var updateAncestryBoundaries = function(node, layoutInfo) {
    var s = "Propagating new position/size of node " + node.id;
    var parentId = node.parentId;
    if (null == parentId) {
      // If there's no parent, we are done
      s += ". No parent node.";
      logDebug(s);
      return;
    }

    // Get Parent Node
    var p = layoutInfo.layoutNodes[layoutInfo.idToIndex[parentId]];
    var flag = false;

    // MaxX
    if (null == p.maxX || node.maxX + p.padRight > p.maxX) {
      p.maxX = node.maxX + p.padRight;
      flag = true;
      s += "\nNew maxX for parent node " + p.id + ": " + p.maxX;
    }

    // MinX
    if (null == p.minX || node.minX - p.padLeft < p.minX) {
      p.minX = node.minX - p.padLeft;
      flag = true;
      s += "\nNew minX for parent node " + p.id + ": " + p.minX;
    }

    // MaxY
    if (null == p.maxY || node.maxY + p.padBottom > p.maxY) {
      p.maxY = node.maxY + p.padBottom;
      flag = true;
      s += "\nNew maxY for parent node " + p.id + ": " + p.maxY;
    }

    // MinY
    if (null == p.minY || node.minY - p.padTop < p.minY) {
      p.minY = node.minY - p.padTop;
      flag = true;
      s += "\nNew minY for parent node " + p.id + ": " + p.minY;
    }

    // If updated boundaries, propagate changes upward
    if (flag) {
      logDebug(s);
      return updateAncestryBoundaries(p, layoutInfo);
    } 

    s += ". No changes in boundaries/position of parent node " + p.id;  
    logDebug(s);
    return;
  };


  /**
   * @brief : Logs a debug message in JS console, if DEBUG is ON
   */
  var logDebug = function(text) {
    if (DEBUG) {
      console.debug(text);
    }
  };


  // register the layout
  $$('layout', 'cose', CoseLayout);

})(cytoscape);
;(function($$){ 'use strict';

  // default layout options
  var defaults = {
    // dagre algo options, uses default value on undefined
    nodeSep: undefined, // the separation between adjacent nodes in the same rank
    edgeSep: undefined, // the separation between adjacent edges in the same rank
    rankSep: undefined, // the separation between adjacent nodes in the same rank
    rankDir: undefined, // 'TB' for top to bottom flow, 'LR' for left to right
    minLen: function( edge ){ return 1; }, // number of ranks to keep between the source and target of the edge
    
    // general layout options
    fit: true, // whether to fit to viewport
    padding: 30, // fit padding
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    ready: function(){}, // on layoutready
    stop: function(){} // on layoutstop
  };

  // constructor
  // options : object containing layout options
  function DagreLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options); 
  }

  // runs the layout
  DagreLayout.prototype.run = function(){
    var options = this.options;
    var layout = this;

    $$.util.require('dagre', function(dagre){

      var cy = options.cy; // cy is automatically populated for us in the constructor
      var eles = options.eles;

      var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
        x1: 0, y1: 0, w: cy.width(), h: cy.height()
      } );

      var g = new dagre.Digraph();

      // add nodes to dagre
      var nodes = eles.nodes().not(':parent');
      for( var i = 0; i < nodes.length; i++ ){
        var node = nodes[i];

        g.addNode( node.id(), {
          width: node.width(),
          height: node.height()
        } );
      }

      // add edges to dagre
      var edges = eles.edges().stdFilter(function( e ){
        return !e.source().is(':parent') && !e.target().is(':parent');
      });
      for( var i = 0; i < edges.length; i++ ){
        var edge = edges[i];

        g.addEdge( edge.id(), edge.source().id(), edge.target().id(), {
          minLen: $$.is.fn(options.minLen) ? options.minLen.apply( edge, [ edge ] ) : options.minLen
        } );
      }

      var d = dagre.layout();

      if( options.nodeSep ){
        d.nodeSep( options.nodeSep );
      }

      if( options.edgeSep ){
        d.edgeSep( options.edgeSep );
      }
      
      if( options.rankSep ){
        d.rankSep( options.rankSep );
      }

      if( options.rankDir ){
        d.rankDir( options.rankDir );
      }
        
      d = d.run(g);

      d.eachNode(function(id, n) {
        cy.getElementById(id).scratch().dagre = n;
      });

      var dagreBB;

      if( options.boundingBox ){
        dagreBB = { x1: Infinity, x2: -Infinity, y1: Infinity, y2: -Infinity };
        nodes.forEach(function( node ){
          var dModel = node.scratch().dagre;

          dagreBB.x1 = Math.min( dagreBB.x1, dModel.x );
          dagreBB.x2 = Math.max( dagreBB.x2, dModel.x );

          dagreBB.y1 = Math.min( dagreBB.y1, dModel.y );
          dagreBB.y2 = Math.max( dagreBB.y2, dModel.y );
        });

        dagreBB.w = dagreBB.x2 - dagreBB.x1;
        dagreBB.h = dagreBB.y2 - dagreBB.y1;
      } else {
        dagreBB = bb;
      }

      var constrainPos = function( p ){
        if( options.boundingBox ){
          var xPct = (p.x - dagreBB.x1) / dagreBB.w;
          var yPct = (p.y - dagreBB.y1) / dagreBB.h;

          return {
            x: bb.x1 + xPct * bb.w,
            y: bb.y1 + yPct * bb.h
          };
        } else {
          return p;
        }
      };

      nodes.layoutPositions(layout, options, function(){
        var dModel = this.scratch().dagre;

        return constrainPos({
          x: dModel.x,
          y: dModel.y
        });
      });

    }); // require

    return this; // chaining
  };

  // register the layout
  $$('layout', 'dagre', DagreLayout);

})(cytoscape);
;(function($$){ 'use strict';
  
  var defaults = {
    fit: true, // whether to fit the viewport to the graph
    padding: 30, // padding used on fit
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    avoidOverlap: true, // prevents node overlap, may overflow boundingBox if not enough space
    rows: undefined, // force num of rows in the grid
    columns: undefined, // force num of cols in the grid
    position: function( node ){}, // returns { row, col } for element
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function GridLayout( options ){
    this.options = $$.util.extend({}, defaults, options);
  }
  
  GridLayout.prototype.run = function(){
    var params = this.options;
    var options = params;
    
    var cy = params.cy;
    var eles = options.eles;
    var nodes = eles.nodes().not(':parent');
    
    var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
      x1: 0, y1: 0, w: cy.width(), h: cy.height()
    } );

    if( bb.h === 0 || bb.w === 0){
      nodes.layoutPositions(this, options, function(){
        return { x: bb.x1, y: bb.y1 };
      });
      
    } else {
      
      // width/height * splits^2 = cells where splits is number of times to split width
      var cells = nodes.size();
      var splits = Math.sqrt( cells * bb.h/bb.w );
      var rows = Math.round( splits );
      var cols = Math.round( bb.w/bb.h * splits );

      var small = function(val){
        if( val == null ){
          return Math.min(rows, cols);
        } else {
          var min = Math.min(rows, cols);
          if( min == rows ){
            rows = val;
          } else {
            cols = val;
          }
        }
      };
      
      var large = function(val){
        if( val == null ){
          return Math.max(rows, cols);
        } else {
          var max = Math.max(rows, cols);
          if( max == rows ){
            rows = val;
          } else {
            cols = val;
          }
        }
      };
      
      // if rows or columns were set in options, use those values
      if( options.rows != null && options.columns != null ){
        rows = options.rows;
        cols = options.columns;
      } else if( options.rows != null && options.columns == null ){
        rows = options.rows;
        cols = Math.ceil( cells / rows );
      } else if( options.rows == null && options.columns != null ){
        cols = options.columns;
        rows = Math.ceil( cells / cols );
      }
      
      // otherwise use the automatic values and adjust accordingly
      
      // if rounding was up, see if we can reduce rows or columns
      else if( cols * rows > cells ){
        var sm = small();
        var lg = large();
        
        // reducing the small side takes away the most cells, so try it first
        if( (sm - 1) * lg >= cells ){
          small(sm - 1);
        } else if( (lg - 1) * sm >= cells ){
          large(lg - 1);
        } 
      } else {
        
        // if rounding was too low, add rows or columns
        while( cols * rows < cells ){
          var sm = small();
          var lg = large();
          
          // try to add to larger side first (adds less in multiplication)
          if( (lg + 1) * sm >= cells ){
            large(lg + 1);
          } else {
            small(sm + 1);
          }
        }
      }
      
      var cellWidth = bb.w / cols;
      var cellHeight = bb.h / rows;

      if( options.avoidOverlap ){
        for( var i = 0; i < nodes.length; i++ ){
          var node = nodes[i];
          var w = node.outerWidth();
          var h = node.outerHeight();

          cellWidth = Math.max( cellWidth, w );
          cellHeight = Math.max( cellHeight, h );
        }
      }
      
      var cellUsed = {}; // e.g. 'c-0-2' => true
      
      var used = function(row, col){
        return cellUsed['c-' + row + '-' + col] ? true : false;
      };
      
      var use = function(row, col){
        cellUsed['c-' + row + '-' + col] = true;
      };

      // to keep track of current cell position
      var row = 0;
      var col = 0;
      var moveToNextCell = function(){
        col++;
        if( col >= cols ){
          col = 0;
          row++;
        }
      };

      // get a cache of all the manual positions
      var id2manPos = {};
      for( var i = 0; i < nodes.length; i++ ){
        var node = nodes[i];
        var rcPos = options.position( node );

        if( rcPos && (rcPos.row !== undefined || rcPos.col !== undefined) ){ // must have at least row or col def'd
          var pos = {
            row: rcPos.row,
            col: rcPos.col
          };

          if( pos.col === undefined ){ // find unused col
            pos.col = 0;

            while( used(pos.row, pos.col) ){
              pos.col++;
            }
          } else if( pos.row === undefined ){ // find unused row
            pos.row = 0;

            while( used(pos.row, pos.col) ){
              pos.row++;
            }
          }

          id2manPos[ node.id() ] = pos;
          use( pos.row, pos.col );
        }
      }

      var getPos = function(i, element){
        var x, y;

        if( element.locked() || element.isFullAutoParent() ){
          return false;
        }

        // see if we have a manual position set
        var rcPos = id2manPos[ element.id() ];
        if( rcPos ){
          x = rcPos.col * cellWidth + cellWidth/2 + bb.x1;
          y = rcPos.row * cellHeight + cellHeight/2 + bb.y1;
        
        } else { // otherwise set automatically
        
          while( used(row, col) ){
            moveToNextCell();
          }

          x = col * cellWidth + cellWidth/2 + bb.x1;
          y = row * cellHeight + cellHeight/2 + bb.y1;
          use( row, col );
          
          moveToNextCell();
        }
        
        return { x: x, y: y };
        
      };

      nodes.layoutPositions( this, options, getPos );
    }

    return this; // chaining
    
  };
  
  $$('layout', 'grid', GridLayout);
  
})( cytoscape );

;(function($$){ 'use strict';

  // default layout options
  var defaults = {
    ready: function(){}, // on layoutready
    stop: function(){} // on layoutstop
  };

  // constructor
  // options : object containing layout options
  function NullLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options); 
  }

  // runs the layout
  NullLayout.prototype.run = function(){
    var options = this.options;
    var eles = options.eles; // elements to consider in the layout
    var layout = this;

    // cy is automatically populated for us in the constructor
    var cy = options.cy; // jshint ignore:line

    layout.trigger('layoutstart');

    // puts all nodes at (0, 0)
    eles.nodes().positions(function(){
      return {
        x: 0,
        y: 0
      };
    });

    // trigger layoutready when each node has had its position set at least once
    layout.one('layoutready', options.ready);
    layout.trigger('layoutready');

    // trigger layoutstop when the layout stops (e.g. finishes)
    layout.one('layoutstop', options.stop);
    layout.trigger('layoutstop');

    return this; // chaining
  };

  // called on continuous layouts to stop them before they finish
  NullLayout.prototype.stop = function(){
    return this; // chaining
  };

  // register the layout
  $$('layout', 'null', NullLayout);

})(cytoscape);
;(function($$){ 'use strict';
  
  var defaults = {
    positions: undefined, // map of (node id) => (position obj); or function(node){ return somPos; }
    zoom: undefined, // the zoom level to set (prob want fit = false if set)
    pan: undefined, // the pan level to set (prob want fit = false if set)
    fit: true, // whether to fit to viewport
    padding: 30, // padding on fit
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function PresetLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options);
  }
  
  PresetLayout.prototype.run = function(){
    var options = this.options;
    var eles = options.eles;

    var nodes = eles.nodes();
    var posIsFn = $$.is.fn( options.positions );

    function getPosition(node){
      if( options.positions == null ){
        return null;
      }

      if( posIsFn ){
        return options.positions.apply( node, [ node ] );
      }
      
      var pos = options.positions[node._private.data.id];

      if( pos == null ){
        return null;
      }
      
      return pos;
    }
    
    nodes.layoutPositions(this, options, function(i, node){
      var position = getPosition(node);
      
      if( node.locked() || position == null ){
        return false;
      }
      
      return position;
    });
        
    return this; // chaining
  };
  
  $$('layout', 'preset', PresetLayout);
  
})(cytoscape);

;(function($$){ 'use strict';
  
  var defaults = {
    fit: true, // whether to fit to viewport
    padding: 30, // fit padding
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    animate: false, // whether to transition the node positions
    animationDuration: 500, // duration of animation in ms if enabled
    ready: undefined, // callback on layoutready
    stop: undefined // callback on layoutstop
  };
  
  function RandomLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options);
  }
  
  RandomLayout.prototype.run = function(){
    var options = this.options;
    var cy = options.cy;
    var eles = options.eles;
    var nodes = eles.nodes().not(':parent');
    
    var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
      x1: 0, y1: 0, w: cy.width(), h: cy.height()
    } );

    var getPos = function( i, node ){
      return {
        x: bb.x1 + Math.round( Math.random() * bb.w ),
        y: bb.y1 + Math.round( Math.random() * bb.h )
      };
    };

    nodes.layoutPositions( this, options, getPos );

    return this; // chaining
  };
  
  // register the layout
  $$(
    'layout', // we're registering a layout
    'random', // the layout name
    RandomLayout // the layout prototype
  );
  
})(cytoscape);

;(function($$){ 'use strict';
  
  var defaults = {
    animate: true, // whether to show the layout as it's running
    maxSimulationTime: 4000, // max length in ms to run the layout
    ungrabifyWhileSimulating: false, // so you can't drag nodes during layout
    fit: true, // whether to fit the viewport to the graph
    padding: 30, // padding on fit
    boundingBox: undefined, // constrain layout bounds; { x1, y1, x2, y2 } or { x1, y1, w, h }
    random: false, // whether to use random initial positions
    infinite: false, // overrides all other options for a forces-all-the-time mode
    ready: undefined, // callback on layoutready
    stop: undefined, // callback on layoutstop

    // springy forces
    stiffness: 400,
    repulsion: 400,
    damping: 0.5
  };

  function SpringyLayout( options ){
    this.options = $$.util.extend(true, {}, defaults, options);
  }
  
  SpringyLayout.prototype.run = function(){
    var layout = this;
    var self = this;
    var options = this.options;

    $$.util.require('Springy', function(Springy){

      var simUpdatingPos = false;

      var cy = options.cy;
      layout.trigger({ type: 'layoutstart', layout: layout });
      
      var eles = options.eles;
      var nodes = eles.nodes().not(':parent');
      var edges = eles.edges();
   
      var bb = $$.util.makeBoundingBox( options.boundingBox ? options.boundingBox : {
        x1: 0, y1: 0, w: cy.width(), h: cy.height()
      } );
      
      // make a new graph
      var graph = new Springy.Graph();

      // make some nodes
      nodes.each(function(i, node){
        node.scratch('springy', {
          model: graph.newNode({
            element: node
          })
        });
      });

      // connect them with edges
      edges.each(function(i, edge){
        var fdSrc = edge.source().scratch('springy').model;
        var fdTgt = edge.target().scratch('springy').model;
        
        edge.scratch('springy', {
          model: graph.newEdge(fdSrc, fdTgt, {
            element: edge
          })
        });
      });
      
      var sim = window.sim = new Springy.Layout.ForceDirected(graph, options.stiffness, options.repulsion, options.damping);

      if( options.infinite ){
        sim.minEnergyThreshold = -Infinity;
      }

      var currentBB = sim.getBoundingBox();
      // var targetBB = {bottomleft: new Springy.Vector(-2, -2), topright: new Springy.Vector(2, 2)};
      
      // convert to/from screen coordinates
      var toScreen = function(p) {
        currentBB = sim.getBoundingBox();

        var size = currentBB.topright.subtract(currentBB.bottomleft);
        var sx = p.subtract(currentBB.bottomleft).divide(size.x).x * bb.w + bb.x1;
        var sy = p.subtract(currentBB.bottomleft).divide(size.y).y * bb.h + bb.x1;

        return new Springy.Vector(sx, sy);
      };

      var fromScreen = function(s) {
        currentBB = sim.getBoundingBox();

        var size = currentBB.topright.subtract(currentBB.bottomleft);
        var px = ((s.x - bb.x1) / bb.w) * size.x + currentBB.bottomleft.x;
        var py = ((s.y - bb.y1) / bb.h) * size.y + currentBB.bottomleft.y;

        return new Springy.Vector(px, py);
      };
      
      var movedNodes = cy.collection();
      
      var numNodes = cy.nodes().size();
      var drawnNodes = 1;
      var fdRenderer = new Springy.Renderer(sim,
        function clear() {
          if( movedNodes.length > 0 && options.animate ){
            simUpdatingPos = true;

            movedNodes.rtrigger('position');

            if( options.fit ){
              cy.fit( options.padding );
            }

            movedNodes = cy.collection();

            simUpdatingPos = false;
          }
        },

        function drawEdge(edge, p1, p2) {
          // draw an edge
        },

        function drawNode(node, p) {
          var v = toScreen(p);
          var element = node.data.element;
          
          if( !element.locked() && !element.grabbed() ){
              element._private.position = {
                x: v.x,
                y: v.y
              };
              movedNodes.merge(element);
          } else {
            //setLayoutPositionForElement(element);
          }
          
          if( drawnNodes == numNodes ){
            layout.one('layoutready', options.ready);
            layout.trigger({ type: 'layoutready', layout: layout });
          } 
          
          drawnNodes++;
        
        }
      );
      
      // set initial node points
      nodes.each(function(i, ele){
        if( !options.random ){
          setLayoutPositionForElement(ele);
        }
      });
      
      // update node positions when dragging
      var dragHandler;
      nodes.on('position', dragHandler = function(){
        if( simUpdatingPos ){ return; }

        setLayoutPositionForElement(this);
      });
      
      function setLayoutPositionForElement(element){
        var fdId = element.scratch('springy').model.id;
        var fdP = fdRenderer.layout.nodePoints[fdId].p;
        var pos = element.position();
        var positionInFd = (pos.x != null && pos.y != null) ? fromScreen(element.position()) : {
          x: Math.random() * 4 - 2,
          y: Math.random() * 4 - 2
        };
        
        fdP.x = positionInFd.x;
        fdP.y = positionInFd.y;
      }
      
      var grabbableNodes = nodes.filter(":grabbable");
      
      function start(){
        // disable grabbing if so set
        if( options.ungrabifyWhileSimulating ){
          grabbableNodes.ungrabify();
        }
        
        fdRenderer.start();
      }
      
      self.stopSystem = function(){
        graph.filterNodes(function(){
          return false; // remove all nodes
        });
        
        if( options.ungrabifyWhileSimulating ){
          grabbableNodes.grabify();
        }

        if( options.fit ){
          cy.fit( options.padding );
        }
        
        nodes.off('drag position', dragHandler);

        layout.one('layoutstop', options.stop);
        layout.trigger({ type: 'layoutstop', layout: layout });

        self.stopSystem = null;
      };
      
      start();
      if( !options.infinite ){
        setTimeout(function(){
          self.stop();
        }, options.maxSimulationTime);
      }

    }); // require

    return this; // chaining
  };

  SpringyLayout.prototype.stop = function(){
    if( this.stopSystem != null ){
      this.stopSystem();
    }

    return this; // chaining
  };
  
  $$('layout', 'springy', SpringyLayout);

  
})(cytoscape);

;(function($$){ 'use strict';
    
  function NullRenderer(options){
    this.options = options;
  }
  
  NullRenderer.prototype.recalculateRenderedStyle = function(){
  };

  NullRenderer.prototype.notify = function(){
    // the null renderer does nothing
  };
  
  $$('renderer', 'null', NullRenderer);
  
})( cytoscape );
