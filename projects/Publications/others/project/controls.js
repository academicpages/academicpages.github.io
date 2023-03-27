var actionStatuses = {'pan': true, 'select': false}
var svg_brush = null;
var brush_extent = null;
var brush_xScale = null;
var brush_yScale = null;
var old_transform = {xTranslate: 0, yTranslate: 0, scale: 1};

//This function handles (enables and disables) SELECT and PAN buttons.
// function panStatus(val){
function enablePan(){
    var panZoomTiger = svgPanZoom('#panzoomthis');
    panZoomTiger.enablePan(); 
    var nodes = d3.selectAll('.node');
    var edges = d3.selectAll('.edge');
    add_node_listeners(nodes);
    add_edge_listeners(edges); 
 }
 
function disablePan() {
   var panZoomTiger = svgPanZoom('#panzoomthis');
   panZoomTiger.disablePan(); 
}

function getZoomTransform() {
    var transform_str = d3.select('#panzoomthis').select('.viewport').attr('transform');
    // transform should be a string 'matrix(s, 0, 0, s, tx, ty)', where s is the scale factor
    // and tx, ty are the translations of x and y.
    transform_str = transform_str.slice(7,-1).split(',');
    var transform = {scale: Number(transform_str[0]), 
                    xTranslate: Number(transform_str[4]),
                    yTranslate: Number(transform_str[5])};
    return transform;
}

function applyZoomTransform(x, y, transform) {
    return {x: x*transform.scale + transform.xTranslate,
            y: y*transform.scale + transform.yTranslate};
}

function applyZoomTransformInverse(x, y, transform) {
    return {x: (x-transform.xTranslate) / transform.scale,
            y: (y-transform.yTranslate) / transform.scale}
}

function extentApplyTransformInverse(extent, transform) {
    var new_extent = [[0,0],[0,0]];
    new_extent[0][0] = (extent[0][0]-transform.xTranslate) / transform.scale;
    new_extent[1][0] = (extent[1][0]-transform.xTranslate) / transform.scale;
    new_extent[0][1] = (extent[0][1]-transform.yTranslate) / transform.scale;
    new_extent[1][1] = (extent[1][1]-transform.yTranslate) / transform.scale;
    return new_extent;
}

function extentApplyTransform(extent, transform) {
    var new_extent = [[0,0], [0,0]]
    new_extent[0][0] = extent[0][0]*transform.scale + transform.xTranslate;
    new_extent[1][0] = extent[1][0]*transform.scale + transform.xTranslate;
    new_extent[0][1] = extent[0][1]*transform.scale + transform.yTranslate;
    new_extent[1][1] = extent[1][1]*transform.scale + transform.yTranslate;
    return new_extent;
}

function brush_beforeZoom() {
    old_transform = getZoomTransform();
}

// Give this function to the SVG-Pan-Zoom library for both
// the onZoom and onPan event handlers.
function brush_onZoom() {
    if (!actionStatuses['select'] || brush_extent === null)
        return;
    var transform = getZoomTransform();
    // Find the new domain, which is the currently visible part of SVG space.
    // This involves applying the inverse SVG transformation to the boundaries
    // of the window, to find the extreme portion of the visible SVG window.
    var minrange = applyZoomTransformInverse(0, 0, transform);
    var maxrange = applyZoomTransformInverse(window.innerWidth, window.innerHeight, transform);
    svg_brush.x(brush_xScale.domain([minrange.x, maxrange.x]));
    svg_brush.y(brush_yScale.domain([minrange.y, maxrange.y]));

    if (brush_extent !== null) {
        // We need to keep the same SVG coordinates as before, so we'll copy the current extent 
        // and set the copy as the new extent. This prevents the brush from resizing the extent
        // to match the new domain (why? Only God knows).
        var new_extent = [[brush_extent[0][0], brush_extent[0][1]], 
            [brush_extent[1][0], brush_extent[1][1]]];
        svg_brush.extent(new_extent);
        brush_extent = new_extent;
    old_transform = transform;
    svg_brush(d3.select('.brush'));
    }
}

/*
 * TODO: Disable selecting in the actions window.
 */
var time = 0;
var count = 0;
function enableSelect() {
    actionStatuses['select'] = true;
    var width = window.innerWidth;
    var height = window.innerHeight;

    var nodes = d3.select('#svgdiv').select('svg')
                    .selectAll('.node');
    nodes.classed('KeepHighlighted', false);
    
    var edges = d3.select('#svgdiv').select('svg')
                    .selectAll('.edge');
    edges.classed('KeepHighlighted', false);

    var transform = getZoomTransform();
    var minrange = applyZoomTransformInverse(0, 0, transform);
    var maxrange = applyZoomTransformInverse(window.innerWidth, window.innerHeight, transform);
    brush_xScale = d3.scale.linear().domain([minrange.x, maxrange.x]).range([0,width]); 
    brush_yScale = d3.scale.linear().domain([minrange.y, maxrange.y]).range([0, height]);

    svg_brush = d3.svg.brush()
        .x(brush_xScale)
        .y(brush_yScale)
        .on('brushstart', function() {
            old_transform = getZoomTransform();
            d3.select('.two').select('.brush')
                .call(chart_brush.clear());
        })
        .on("brush", function() {
            brush_extent = d3.event.target.extent();
            nodes.classed("highlight", function(d, i) {
                var transform = this.getCTM(); 
                var point = d3.select('svg')[0][0].createSVGPoint();
                var node = d3.select(this).select('text');
                point.x = node[0][0].x.animVal[0].value;
                point.y = node[0][0].y.animVal[0].value;
                point = point.matrixTransform(transform);
                var stat = brush_extent[0][0] < point.x && brush_extent[1][0] > point.x
                    && brush_extent[0][1] < point.y && brush_extent[1][1] > point.y;
                return stat;
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

            update_bar_chart(collect_centralities());
        })
        .on('brushend', function() {
            //update_bar_chart(collect_centralities());
        });
     
    var svg = d3.select('#svgdiv').select('svg');
    svg.append("g")
          .attr("class", "brush")
          .call(svg_brush);
}

function disableSelect() {
    actionStatuses['select'] = false;
    d3.select('#svgdiv').select('.brush').remove();
    d3.selectAll('.edge, .node').classed('highlight', false)
        .on('mouseover', null)
        .on('mouseout', null)
        .on('dblclick', null);
    update_bar_chart([]);
}

function disableActions() {
   disablePan();
   disableSelect(); 
    /* ... */
}

/*
 * Won't work if a wrong action is passed in.
 */
function selectAction(action) {
    disableActions(action); 
    if (action === 'pan') {
        enablePan(); 
    } else if (action === 'select') {
        enableSelect();
    }
     
}

function clear() {
    var elems = d3.selectAll('.node, .edge');
    elems.classed("KeepHighlighted",false);
    elems.classed("highlight",false);
    if (svg_brush)
        d3.select('.brush').call(svg_brush.clear());
}

function Query() {
    var querybox = d3.select('#query');
    var text = querybox[0][0].value;
    var nodes = d3.select('#svgdiv').selectAll('.node');
    nodes.classed('KeepHighlighted', function() {
            var t = d3.select(this).text().split('\n');
            for (var i = 0; i < t.length; i++)
                if (t[i] === text)
                    return true;
            return false;
        });
}

function query_submit() {
    Query();
    return false;
}

function highlight_shortest_paths() {
    var nodes = d3.selectAll('.node.KeepHighlighted');
    var ids = []
    for (var i = 0; i < nodes[0].length; i++)
        ids.push(read_id_from_node(nodes[0][i]));

    var gnodes = graph.elements(function() {
        var id = this.data('id');
        for (var i = 0; i < ids.length; i++) {
            if (id == ids[i])
                return true;
        }
        return false;
    });
    console.log(gnodes);
    pairwise_shortest_paths(graph, gnodes); 
}
