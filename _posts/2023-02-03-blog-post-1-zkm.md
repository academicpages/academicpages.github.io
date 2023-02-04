---
title: 'Matlab相机标定'
date: 2023-02-03
permalink: /posts/2023/02/blog-post-1-zkm/
tags:
  - Matlab标定相机
  - 标定板
  - camera calibrate
---

描述Matlab做**相机标定**的过程.

标定板
======
Matlab生成标定板代码：  
```
J = (checkerboard(300,4,5)>0.5);
figure, imshow(J);
```



采集图片
======
保存15-20张不同角度下标定板的姿态照片，尽量把镜头的各个角度都覆盖好。可以直接对着屏幕拍摄。测量好屏幕上每个方格的大小，在标定的时候会用到。  
![png](/images/posts/calibrate.png)

进行标定
------
在MATLAB的Command Window里面输入cameraCalibrator即可调用标定应用。
![png](/images/posts/cameraCalibrator.png)
![png](/images/posts/cameraCalibrator2.png)  
设置标定板方格实际尺寸大小:  
![png](/images/posts/cameraCalibrator3.png)  

选择使用两参数，并且选择错切和桶形畸变。  
![png](/images/posts/coefficients.png)  
点击开始后等待一段时间即可完成标定。  
![png](/images/posts/calibrateshow.png)  


点击show Undistorted即可看到无畸变的图像。  
![png](/images/posts/calibrateshowundistorted.png)  
到这为止，你已经**完成了**标定过程。选择导出参数，即可把参数进行保存。  
![png](/images/posts/export-matlab.png)  
保存后可以退出标定应用，在MATLAB主界面中将保存的Mat文件打开。
![png](/images/posts/MAT-cablibrate.png)  
![png](/images/posts/para-cablibrate.png)  
里面的RadialDistortion对应k1，k2，k3设置为0了。
TangentialDistortion对应p1，p2。
IntrinsicMatrix对应内参，注意这个和OpenCV中是转置的关系，注意不要搞错。
![png](/images/posts/para-matlab.png)  
对应
![png](/images/posts/para-opencv.png)  
