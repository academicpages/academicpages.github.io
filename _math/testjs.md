---
title: "rmarkdown example with external js"
output:
  html_document:
    self_contained: false
    keep_md: true
    includes:  
      in_header: "header_include_d3.html"
---


```{r results='asis'}

cat('
<script>
  d3.select("body").append("p").text("d3 made me")
</script>
')

```

<script>

// from https://www.dashingd3js.com/svg-paths-and-d3js
//The data for our line
 var lineData = [ { "x": 1,   "y": 5},  { "x": 20,  "y": 20},
                  { "x": 40,  "y": 10}, { "x": 60,  "y": 40},
                  { "x": 80,  "y": 5},  { "x": 100, "y": 60}];

 //This is the accessor function we talked about above
 var lineFunction = d3.svg.line()
                          .x(function(d) { return d.x; })
                          .y(function(d) { return d.y; })
                         .interpolate("linear");

//The SVG Container
var svgContainer = d3.select("body").append("svg")
                                    .attr("width", 200)
                                    .attr("height", 200);

//The line SVG Path we draw
var lineGraph = svgContainer.append("path")
                            .attr("d", lineFunction(lineData))
                            .attr("stroke", "blue")
                            .attr("stroke-width", 2)
                            .attr("fill", "none");

</script>
