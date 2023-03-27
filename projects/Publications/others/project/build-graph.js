var graph = null;

var num_nodes = 0;
var num_edges = 0;

function myOnLoad(mapfile) {
    d3.text(mapfile, 
        function(error, svg) {
            var svg_div = d3.select('#svgdiv')
                            .append('svg:svg')
                            .attr('width', window.innerWidth)
                            .attr('height', window.innerHeight);
            svg_div.html(svg);

            var nodes = svg_div.selectAll('.node');
            num_nodes = nodes[0].length;
            var edges = svg_div.selectAll('.edge');
            num_edges = edges[0].length;

            var elems = [];
            // Add nodes
            for (var i = 0; i < nodes[0].length; i++) {
                elems.push({group: 'nodes', 
                    data: {
                        node: nodes[0][i], 
                        id: read_id_from_node(nodes[0][i])
                    }
                });
            }
            nodes.attr('elem_id', function(d,i) { return elems[i].data.id; });
            // Add edges
            for (var i = 0; i < edges[0].length; i++) {
                var edge = make_edge(edges[0][i]);
                elems.push(edge);
            }

            graph = cytoscape({elements: elems});
            add_node_listeners(d3.selectAll('.node'));
            add_edge_listeners(d3.selectAll('.edge'));
            // list of centralities of each node
            centralities = compute_centrality(graph);
            make_bar_chart(centralities);
        });
}

function centrality_of(node_index, elems, paths) {
    var centrality = 0.0;
    for (var i = 0; i < elems.length; ++i) {
        if (elems[i].isEdge() || i === node_index)
            continue;
        var dist = paths.distance(elems[node_index], elems[i]);
        centrality += isFinite(dist) ? dist : 0;
    }
    return 1 / centrality;

}

/*
 * Computes the centrality of each vertex in the graph, and stores
 * this value.
 */
function compute_centrality(graph) {
    var elems = graph.collection('node, edge');
    var paths = elems.floydWarshall();
    var centralities = []
    for (var i = 0; i < elems.length; ++i) {
        if (elems[i].isEdge())
            continue;
        var centrality = centrality_of(i, elems, paths);
        elems[i].data('centrality', centrality);
    }
    var nodes = graph.collection('node');
    var maxc = 0;
    for (var i = 0; i < nodes.length; i++) {
        maxc = Math.max(nodes[i].data('centrality'), maxc);
    }

    for (var i = 0; i < nodes.length; i++) {
        var c = nodes[i].data('centrality');
        c = c / maxc;
        nodes[i].data('centrality', c);
        centralities.push(c);
    }
    return centralities;
}

myOnLoad('a2.svg');

function add_node_listeners(nodes) {
    nodes.on('mouseover', function() {
        d3.select(this).classed('highlight', true);
    })
    .on('mouseout', function() {
        d3.select(this).classed('highlight', false);
    })
    .on('dblclick', function() {
        var n = d3.select(this);
        var curClass = n.classed('KeepHighlighted');
        n.classed('KeepHighlighted', !curClass);
    });
}

function add_edge_listeners(edges) {
        edges.on('mouseover', function() {
                d3.select(this).classed('highlight', true);

                var node_tags = endpoints_of(this);
                var node0 = graph.getElementById(node_tags[0]); 
                d3.select(node0._private.data.node).classed('highlight', true);
                var node1 = graph.getElementById(node_tags[1]); 
                d3.select(node1._private.data.node).classed('highlight', true);
            
        })
        .on('mouseout', function() {
                d3.select(this).classed('highlight', false);

                var node_tags = endpoints_of(this);
                var node0 = graph.getElementById(node_tags[0]); 
                d3.select(node0._private.data.node).classed('highlight', false);
                var node1 = graph.getElementById(node_tags[1]); 
                d3.select(node1._private.data.node).classed('highlight', false);
         })
         .on('dblclick', function() {
                var curClass = d3.select(this).classed('KeepHighlighted');
                d3.select(this).classed('KeepHighlighted', !curClass); 
                var node_tags = endpoints_of(this);
                var node0 = graph.getElementById(node_tags[0]); 
                d3.select(node0._private.data.node)
                    .classed('KeepHighlighted', !curClass);
                var node1 = graph.getElementById(node_tags[1]); 
                d3.select(node1._private.data.node)
                   .classed('KeepHighlighted', !curClass);
                }) ;
}

function make_edge(edge) {
    var nodes = d3.select(edge).select('title').text().split('--');
    var data = {id: d3.select(edge).attr('id'),
                source: nodes[0], target: nodes[1], edge: edge};
    var elem = {group: 'edges', data: data};
    return elem;
}

