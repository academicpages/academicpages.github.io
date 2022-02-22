---
title: "AI Car in simulation based on hd-map"
excerpt: "The autonomous driving simulation AI Car routing method <br/><img src='/images/apollo_routing.png'>"
collection: portfolio
---

从高精地图中提取车道拓扑信息,即车道的链接,相邻等信息来构建用于寻路的拓扑地图。导航地图在内存中的表示是一种有向图结构,其中道路上的每条车道为有向图中的一个节点(Node),若当前车道节点与前驱车道有链接关系,或者当前车道节点与左侧相邻车道节点允许穿越(即边界线为虚黄线或者虚白线),或者当前车道节点与右侧相邻车道节点允许穿越,则在上述两条车道之间建立边(Edge)加入到表征道路拓扑关系的有向图中。拓扑地图构建完毕后,基于现有的寻路策略进行路径计算,如 Dijkstra 算法,A*算法及其各种变体。