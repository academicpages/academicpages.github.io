function read_id_from_node(node) {
    var id = d3.select(node).select('title').text();
    return id; 
}

function node_coordinate(node) {
    var text = d3.select(node).select('text');
    var coord = {x: Number(text[0][0].getAttribute('x')),
                 y: Number(text[0][0].getAttribute('y'))};
    return coord;
}

/*
 * For each pair of nodes `a' and `b' in the list `nodes',
 * computes the shortest path between `a' and `b' and
 * highlights this path. The algorithm used is BFS
 */
function pairwise_shortest_paths(graph, nodes) {
    for (var i = 0; i < nodes.length; i++) {
        var selector = 'node[id = "' + String(nodes[i].data('id')) + '"]';
        var paths = graph.elements().dijkstra(selector);
        for (var j = i+1; j < nodes.length; j++) {
            var path = paths.pathTo(nodes[j]); 
            for (var k = 0; k < path.length; k++) {
                if (k % 2 == 0) { // Is a node
                    //var node = path.path[i].data('node');
                    var node = path[k].data('node');
                    var id = read_id_from_node(node);
                    d3.select(node)
                        .classed('KeepHighlighted', true);
                    //if (id === target) 
                    //    break;
                } else {
                    d3.select(path[k].data('edge'))
                        .classed('KeepHighlighted', true);
                }
            }
        }
    } 
}


