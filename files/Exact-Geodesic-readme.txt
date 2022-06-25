If you use this code, please cite the following papers:

[1] Yong-Jin Liu, Zhan-Qing Chen, Kai Tang. 
Construction of Iso-contours, Bisectors and Voronoi Diagrams on Triangulated Surfaces. 
IEEE Transactions on Pattern Analysis and Machine Intelligence. Vol. 33, No. 8, 
pp. 1502-1517, 2011.

[2] Yong-Jin Liu, Qian-Yi Zhou, Shi-Min Hu. 
Handling degenerate cases in exact geodesic computation on triangle meshes. 
The Visual Computer, 23(9-11): 661-668, 2007.

----------------------------------------
This code is developed in Microsoft VC++.net platform, and is running in a console mode.

Detailed usage of the source code package:

ExactGeodesic.exe [filename] [source]

[filename] is the path and file name of the test model, 
[source] is a non-negative integer representing the ID of the source vertex, 0-based.

e.g. ExactGeodesic.exe maxplanck.obj 9999
 or  ExactGeodesic.exe 5000_bunny.obj 0
 
The result will be printed to a text file, listing the distances to all vertices 
from source vertex, and a single line in the end, showing the time cost in miliseconds. 
File name is in the following form:

[filename].[source].dist

where [filename] and [source] are the same as the ones in the command line in your input.

----------------------------------------
More references in computational geometry and graph theory:

[3] Wen-Qi Zhang, Yong-Jin Liu. 
Approximating the Longest Paths in Grid Graphs. 
Theoretical Computer Science, Vol. 412, No. 39, pp. 5340-5350, 2011.

[4] Yong-Jin Liu, Wen-Qi Zhang, Kai Tang. 
Some notes on maximal arc intersection of spherical polygons: its NP-hardness and approximation algorithms. 
The Visual Computer, Vol. 26, No. 4, pp. 287-292, 2010.

[5] Kai Tang, Yong-Jin Liu. 
A geometric method for determining intersection relations between a movable convex object and a set of planar polygons. 
IEEE Transactions on Robotics, Vol. 20, No. 4, pp. 636-650, 2004

[6] Kai Tang, Yong-Jin Liu. 
Maximal intersection of spherical polygons by an arc. 
Computer-Aided Design, Vo. 35, No. 14, pp. 1269-1285, 2003

