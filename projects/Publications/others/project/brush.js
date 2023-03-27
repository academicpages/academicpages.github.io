var brush_func = d3.svg.brush()
    .x(d3.scale.identity().domain([0, width]))
    .y(d3.scale.identity().domain([0, height]))
    .on("brush", function() {
        var extent = d3.event.target.extent();
        node.classed("selected", function(d) {
          return extent[0][0] <= d.x && d.x < extent[1][0]
              && extent[0][1] <= d.y && d.y < extent[1][1];
        });
    })

var brush = svg.append("g")
      .attr("class", "brush")
      .call(brush_func);
