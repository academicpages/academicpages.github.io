d3.selection.prototype.size = function() {
    var n = 0;
    //console.log('Calling size');
    //console.log(this);
    this.each(function(d, i) { ++n;});
    return n;
}

function endpoints_of(edge) {
    return d3.select(edge).select('title')
                    .text().split('--');
}

/*
 * `a' and `b' are assume to be objects of the
 * form {m: Number, b: Number}, which defines
 * a line of the form y=mx + b.
 *
 * The result is a point {x: Number, y: Number}
 * where the lines intersect, null if they are
 * parallel.
 */
function lines_intersect(l1, l2) {
    /* TODO: This returns null if the 2 lines are equal */ 
    if (l1.m === l2.m)
       return null;
    var x = (l2.b - l1.b) / (l1.m - l2.m);
    var y = l1.m * x + l1.b;
    return {x:x, y:y};
}

/*
 * 
 */
function point_on_segment(point, left, right) {
    return point > left && point < right;
}

function test_line_extent_intersect() {
    extent = [[1,3], [2,0.5]]
    line = {x1:1.3, y1:.25, x2:1.3, y2:.75}
    console.log(line_extent_intersect(line, extent));

    line = {x1:2.5, y1:1.8, x2:2.5, y2:2.3}
    console.log(line_extent_intersect(line, extent));

    line = {x1:2.5, y1:.25, x2:3.25, y2:.75}
    console.log(line_extent_intersect(line, extent));

    line = {x1:2.8, y1:0.6, x2:3.25, y2:.75}
    console.log(line_extent_intersect(line, extent));

    line = {x1:2.5, y1:.25, x2:2.8, y2:.6}
    console.log(line_extent_intersect(line, extent));

    line = {x1:1.3, y1:.25, x2:1.3, y2:.75}
}

/*
 * Line is a object 
 * {x1: Number, y1: Number, x2: Number, y2: Number}.
 * 
 * We assume `extent' is an open rectangle, so if `line'
 * intersects only at a boundary, we return false.
 */
function line_extent_intersect(line, extent) {
    var left_edge = extent[0][0]; 
    var right_edge = extent[0][1];
    var top_edge = extent[1][0];
    var bottom_edge = extent[1][1];
    //console.log('Line = ')
    //console.log(line)
    // Check for vertical intersection
    if (line.x1 === line.x2) { 
        // Doesn't intersect if to the left or right
        if (line.x1 < left_edge || line.x1 > right_edge) {
            return false;
        } // case (a): Line inside     
        else if (line.y1 > bottom_edge && line.y2 < top_edge) {
            return true;
        }
        // case (b): Line starts inside, ends above
        else if (line.y1 > bottom_edge && line.y1 < top_edge) {
            return true;
        } 
        // case (c): line starts below, ends inside
        else if (line.y2 > bottom_edge && line.y2 < top_edge) {
            return true;
        } 
        // case (d): Line starts below, ends above
        else if (line.y1 <= bottom_edge && line.y2 >= top_edge) {
            return true;
        }
        else {
            return false;
        }
    }
    // Non-vertical intersection
    // Check if intersect on bottom edge
    var m = (line.y1 - line.y2) / (line.x1 - line.x2); 
    var b = line.y1 - m * line.x1;
    line = {m: m, b: b};
    bottom_line = {m: 0, b: bottom_edge};
    var intersect = lines_intersect(line, bottom_line);
    // check point is on segment
    if (line.x > extent[0][0] && line.x < extent[0][1])
        return true;

    // Check if intersect on top edge
    top_line = {m: 0, b: top_edge};
    intersect = lines_intersect(line, top_line);
    // check point is on segment
    if (line.x > extent[0][0] && line.x < extent[0][1])
        return true;

    // Check if intersect on left edge.
    var y = line.m * left_edge + line.b; 
    if (y > bottom_edge && y < top_edge)
       return true; 

    // Check if intersect on right edge.
    y = line.m * right_edge + line.b; 
//    console.log(line)
//    console.log('y = ' + y) 
//    console.log('bottom = ' + bottom_edge) 
//    console.log('top = ' + top_edge) 
    if (y > bottom_edge && y < top_edge)
       return true; 
//    console.log('Left, Top, Right, Bottom')
//    console.log(left_edge, top_line, right_edge, bottom_line)

    return false;
}

function get_path_endpoints(path) {
    var start = path.getPointAtLength(0);
    var end = path.getPointAtLength(path.getTotalLength());
    var transform = path.getCTM();
    start = start.matrixTransform(transform);
    end = end.matrixTransform(transform);
    var points = {x1: start.x, y1: start.y, x2: end.x, y2: end.y};
    // Sort by x coordinate
    if (points.x1 > points.x2) {
        var x = points.x1;
        points.x1 = points.x2;
        points.x2 = x;
    }
    return points;
}
