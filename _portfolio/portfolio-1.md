---
title: "baidu apollo - unreal simulation"
excerpt: "The autonomous driving simulation platform which connect baidu apollo system and uisee driving system <br/><img src='/images/apollo_unreal_2.png'>"
collection: portfolio
---

从Unreal仿真环境中获取车辆的定位信息，底盘信息，抓取仿真环境的传感器信息，如激光雷达的点云、相机的影像等，将上述信息转化为Apollo定义的消息格式并发布出去以作为Apollo系统的输入，然后订阅系统控制模块的输出，包括车辆转角，油门以及刹车，将控制量发送给仿真环境进行车辆控制