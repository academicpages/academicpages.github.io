var BAR_CHART_WIDTH = 25;
var BAR_CHART_MAXY = 200;
var BAR_CHART_MINY = 74; 

function count_elems(selection) {
    var nodes = selection.filter('.node');
    var edges = selection.filter('.edge');
    var num_nodes = nodes.size();
    var num_edges = edges.size();
    var density = num_nodes === 0 ? 0 : num_edges / num_nodes
    var stats = {num_edges: num_edges, 
                 num_nodes: num_nodes,
                 density: density};
    return stats;
}

function collect_centralities() {
    var nodes = d3.selectAll('.node.highlight');
    var centralities = []
    for (var i = 0; i < nodes[0].length; i++) {
        var id = d3.select(nodes[0][i]).attr('elem_id');
        var elem = graph.collection('node#'+id);
        centralities.push(elem.data('centrality'));
    }
    return centralities;
}

function count_each_bucket(nodes) {
    var buckets = Array(21);
    for (var i = 0; i < 21; i++)
        buckets[i] = 0;

    for (var i = 0; i < nodes.length; ++i) {
        buckets[nodes[i].data('centrality')*20] += 1;
    }
    return buckets;
}

function max_nodes_in_chart(nodes) {
    var buckets = count_each_bucket(nodes);
    var max = 0;
    for (var i = 0; i < 21; i++) {
        max = Math.max(max, buckets[i]);
    }
    return max;
}

var histogram_height = 0;
var histogram_ymax = 0;
var histogram_ymin = 0;
var xScale = null;
var chart_brush = null;

function make_bar_chart(values) {
    var width = 285;
    var height = 300;
    var xBottom = 13;
    histogram_height = height;
    xScale = d3.scale.linear()
        .domain([0, 1])
        .range([xBottom,xBottom+width]);
    var data = d3.layout.histogram()
        .bins(xScale.ticks(20))
        (values);
    histogram_ymax = d3.max(data,function(d){return d.y;});
    var yScale = d3.scale.linear()
       .domain([0, histogram_ymax])
       .range([height, 0]);
    var xAxis = d3.svg.axis().scale(xScale).orient('bottom');
    var yAxis = d3.svg.axis().scale(yScale).orient('left');
    var svg = d3.select('.two').select('svg');
    svg.append('g')
        .attr('transform', 'translate(' + xBottom + ',' + height + ')')
        .attr('id', 'axis')
        .call(xAxis);
    svg.append('g')
        .attr('id', 'axis')
        .attr('transform', 'translate(' + 29 + ', 0)')
        .call(yAxis);
    var bar = svg.selectAll('.bar')
        .data(data)
        .enter()
        .append('g')
        .attr('class', 'bar')
        .attr('transform', function(d) { 
                return 'translate(' + xScale(d.x) + ',' + yScale(d.y) + ')';
        });
    bar.append('rect')
        .attr('x', 1)
        .attr('width', xScale(data[0].dx)/2)// - 1)
        .attr('height', function(d) { return height-yScale(d.y);});
    bar.filter(function(d) {return d.y > 0;})
        .append('text')
        .attr('dy', '.75em')
        .attr('y', 6)
        .attr('x', xScale(data[0].dx) / 2-5)
        .attr('text-anchor', 'middle')
        .attr('fill', '#00ff00')
        .text(function(d) {return d.y;});

    make_chart_brush(xScale);
}

function make_chart_brush(xScale) {
    var edges = d3.select('#svgdiv').select('svg')
                    .selectAll('.edge');
    chart_brush = d3.svg.brush()
                .x(xScale)
                .on('brushstart', function(){
                    d3.select('#svgdiv').select('.brush')
                        .call(svg_brush.clear());
                    svg_brush.extent(null); 
                })
                .on('brush', function() {
                    var extent = d3.event.target.extent();
                    var nodes = d3.selectAll('.node')
                        .classed('highlight', function(d) {
                            var id = read_id_from_node(this);
                            var cent = graph.collection('#'+id).data('centrality');
                            return extent[0] <= cent && cent <= extent[1];
                        });
                    var highlighted_nodes = nodes.selectAll('.highlight');
                    edges.classed('highlight', function() {
                    var node_tags = endpoints_of(this); 

                    var node0 = graph.getElementById(node_tags[0]);
                    var classes = node0.data().node.classList;
                    var node0_highlighted = false;
                    for (var i = 0; i < classes.length; i++) {
                        if (classes[i] === 'highlight') {
                             node0_highlighted = true;
                             break;
                        } 
                    }
            

                    var node1 = graph.getElementById(node_tags[1]);
                    var node1_highlighted = false;
                    classes = node1.data().node.classList;
                    for (var i = 0; i < classes.length; i++)
                        if (classes[i] === 'highlight') {
                             node1_highlighted = true;
                             break;
                         }
                    var stat = node0_highlighted && node1_highlighted; 
                    return stat;
                    });

                    brush_extent = null;
                    update_bar_chart(collect_centralities());
                });
    d3.select('.two').select('svg')
        .append('g')
        .attr('class', 'brush')
        .call(chart_brush)
        .selectAll('rect')
        .attr('y', 0)
        .attr('height', 300);
}

function update_bar_chart(values) {
    var width = 285;
    var height = histogram_height;
    var xBottom = 13;
    //var xScale = d3.scale.linear()
    //    .domain([0, 1])
    //    .range([xBottom,xBottom+width]);
    var data = d3.layout.histogram()
        .bins(xScale.ticks(20))
        (values);
    var yScale = d3.scale.linear()
       .domain([0, histogram_ymax]) 
       .range([height, 0]);
    var xAxis = d3.svg.axis().scale(xScale).orient('bottom');
    var yAxis = d3.svg.axis().scale(yScale).orient('left');

    var svg = d3.select('.two').select('svg');
    svg.select('#axis').remove();
    svg.append('g')
        .attr('transform', 'translate(' + xBottom + ',' + height + ')')
        .attr('id', 'axis')
        .call(xAxis);
    svg.append('g')
        .attr('id', 'axis')
        .attr('transform', 'translate(' + 29 + ', 0)')
        .call(yAxis);
    svg.selectAll('.brushedbar').remove();
    var bar = svg.selectAll('.brushedbar')
        .data(data)
        .enter()
        .append('g')
        .attr('class', 'brushedbar')
        .attr('transform', function(d) { 
                return 'translate(' + xScale(d.x) + ',' + yScale(d.y) + ')';
        });
    bar.append('rect')
        .attr('x', 1)
        .attr('width', xScale(data[0].dx)/2)// - 1)
        .attr('height', function(d) { return height-yScale(d.y);});
}
