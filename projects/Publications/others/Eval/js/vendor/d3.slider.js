d3.slider = function module() {
  "use strict";

  var div, min = 0, max = 100, svg, svgGroup, value, classPrefix, axis, 
  height=40, rect,
  rectHeight = 12,
  tickSize = 6,
  margin = {top: 25, right: 25, bottom: 15, left: 25}, 
  ticks = 0, tickValues, scale, tickFormat, dragger, width, 
  range = false,
  callbackFn, stepValues, focus;

  function slider(selection) {
    selection.each(function() {
      div = d3.select(this).classed('d3slider', true);
      width = parseInt(div.style("width"), 10)-(margin.left 
                                                + margin.right);

      value = value || min; 
      scale = d3.scale.linear().domain([min, max]).range([0, width])
      .clamp(true);
      
      // SVG 
      svg = div.append("svg")
      .attr("class", "d3slider-axis")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + 
            "," + margin.top + ")");

      // Range rect
      svg.append("rect")
      .attr("class", "d3slider-rect-range")
      .attr("width", width)
      .attr("height", rectHeight);
     
      // Range rect 
      if (range) {
        svg.append("rect")
        .attr("class", "d3slider-rect-value")
        .attr("width", scale(value))
        .attr("height", rectHeight);
      }
      
      // Axis      
      var axis = d3.svg.axis()
      .scale(scale)
      .orient("bottom");
      
      if (ticks != 0) {
        axis.ticks(ticks);
        axis.tickSize(tickSize);
      } else if (tickValues) {
        axis.tickValues(tickValues);
        axis.tickSize(tickSize);
      } else {
        axis.ticks(0);
        axis.tickSize(0);
      }
      if (tickFormat) {
        axis.tickFormat(tickFormat);
      }
      
      svg.append("g")
      .attr("transform", "translate(0," + rectHeight + ")")
      .call(axis)
      //.selectAll(".tick")
      //.data(tickValues, function(d) { return d; })
      //.exit()
      //.classed("minor", true);
   
      var values = [value];
      dragger = svg.selectAll(".dragger")
      .data(values)
      .enter()
      .append("g")
      .attr("class", "dragger")
      .attr("transform", function(d) {
        return "translate(" + scale(d) + ")";
      }) 
      
      var displayValue = null;
      if (tickFormat) { 
        displayValue = tickFormat(value);
      } else {
        displayValue = d3.format(",.0f")(value);
      }
      
      dragger.append("text")
      .attr("x", 0)
      .attr("y", -15)
      .attr("text-anchor", "middle")
      .attr("class", "draggertext")
      .text(displayValue);

      dragger.append("circle")
      .attr("class", "dragger-outer")
      .attr("r", 10)
      .attr("transform", function(d) {
        return "translate(0,6)";
      });
      
      dragger.append("circle")
      .attr("class", "dragger-inner")
      .attr("r", 4)
      .attr("transform", function(d) {
        return "translate(0,6)";
      });


      // Enable dragger drag 
      var dragBehaviour = d3.behavior.drag();
      dragBehaviour.on("drag", slider.drag);
      dragger.call(dragBehaviour);
      
      // Move dragger on click 
      svg.on("click", slider.click);

    });
  }

  slider.draggerTranslateFn = function() {
    return function(d) {
      return "translate(" + scale(d) + ")";
    }
  }

  slider.click = function() {
    var pos = d3.event.offsetX || d3.event.layerX;
    slider.move(pos);
  }

  slider.drag = function() {
    var pos = d3.event.x;
    slider.move(pos+margin.left);
  }

  slider.move = function(pos) {
    var l,u;
    var newValue = scale.invert(pos - margin.left);
    // find tick values that are closest to newValue
    // lower bound
    if (stepValues != undefined) {
      l = stepValues.reduce(function(p, c, i, arr){
        if (c < newValue) {
          return c;
        } else {
          return p;
        }
      });

      // upper bound
      if (stepValues.indexOf(l) < stepValues.length-1) {
        u = stepValues[stepValues.indexOf(l) + 1];
      } else {
        u = l;
      }
      // set values
      var oldValue = value;
      value = ((newValue-l) <= (u-newValue)) ? l : u;
    } else {
      var oldValue = value;
      value = newValue;
    }
    var values = [value];

    // Move dragger
    svg.selectAll(".dragger").data(values)
    .attr("transform", function(d) {
      return "translate(" + scale(d) + ")";
    });
    
    var displayValue = null;
    if (tickFormat) { 
      displayValue = tickFormat(value);
    } else {
      displayValue = d3.format(",.0f")(value);
    }
    svg.selectAll(".dragger").select("text")
    .text(displayValue);
   
    if (range) { 
      svg.selectAll(".d3slider-rect-value")
      .attr("width", scale(value));
    }

    if (callbackFn) {
      callbackFn(slider);
    }
  }

  // Getter/setter functions
  slider.min = function(_) {
    if (!arguments.length) return min;
    min = _;
    return slider;
  };

  slider.max = function(_) {
    if (!arguments.length) return max;
    max = _;
    return slider;
  };

  slider.classPrefix = function(_) {
    if (!arguments.length) return classPrefix;
    classPrefix = _;
    return slider;
  }

  slider.tickValues = function(_) {
    if (!arguments.length) return tickValues;
    tickValues = _;
    return slider;
  }
 
  slider.ticks = function(_) {
    if (!arguments.length) return ticks;
    ticks = _;
    return slider;
  }

  slider.stepValues = function(_) {
    if (!arguments.length) return stepValues;
    stepValues = _;
    return slider;
  }
  
  slider.tickFormat = function(_) {
    if (!arguments.length) return tickFormat;
    tickFormat = _;
    return slider;
  } 

  slider.value = function(_) {
    if (!arguments.length) return value;
    value = _;
    return slider;
  } 
  
  slider.showRange = function(_) {
    if (!arguments.length) return range;
    range = _;
    return slider;
  } 

  slider.callback = function(_) {
    if (!arguments.length) return callbackFn;
    callbackFn = _;
    return slider;
  }

  slider.setValue = function(newValue) {
    var pos = scale(newValue) + margin.left;
    slider.move(pos);
  }

  slider.mousemove = function() {
    var pos = d3.mouse(this)[0];
    var val = slider.getNearest(scale.invert(pos), stepValues);
    focus.attr("transform", "translate(" + scale(val) + ",0)");
    focus.selectAll("text").text(val);
  }
  
  slider.getNearest = function(val, arr) {
    var l = arr.reduce(function(p, c, i, a){
      if (c < val) {
        return c;
      } else {
        return p;
      }
    });
    var u = arr[arr.indexOf(l)+1];
    var nearest = ((value-l) <= (u-value)) ? l : u;
    return nearest;
  }

  slider.destroy = function() {
    div.selectAll('svg').remove();
    return slider;
  }

  return slider;

};



