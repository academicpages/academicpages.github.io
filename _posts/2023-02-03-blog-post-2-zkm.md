---
title: 'opencv调用matlab标定参数'
date: 2023-02-03
permalink: /posts/2023/02/blog-post-2-zkm/
tags:
  - 标定
  - Matlab标定相机
  - camera calibrate
---

OpenCV中查看标定的结果，直接上代码。

```C++
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main()
{
    VideoCapture inputVideo(0);
    if (!inputVideo.isOpened())
    {
        cout << "Could not open the input video: " << endl;
        return -1;
    }
    Mat frame;
    Mat frameCalibration;

    inputVideo >> frame;
    Mat cameraMatrix = Mat::eye(3, 3, CV_64F);
    cameraMatrix.at<double>(0, 0) = 4.450537506243416e+02;
    cameraMatrix.at<double>(0, 1) = 0.192095145445498;
    cameraMatrix.at<double>(0, 2) = 3.271489590204837e+02;
    cameraMatrix.at<double>(1, 1) = 4.473690628394497e+02;
    cameraMatrix.at<double>(1, 2) = 2.442734958206504e+02;

    Mat distCoeffs = Mat::zeros(5, 1, CV_64F);
    distCoeffs.at<double>(0, 0) = -0.320311439187776;
    distCoeffs.at<double>(1, 0) = 0.117708464407889;
    distCoeffs.at<double>(2, 0) = -0.00548954846049678;
    distCoeffs.at<double>(3, 0) = 0.00141925006352090;
    distCoeffs.at<double>(4, 0) = 0;

    Mat view, rview, map1, map2;
    Size imageSize;
    imageSize = frame.size();
    initUndistortRectifyMap(cameraMatrix, distCoeffs, Mat(),
        getOptimalNewCameraMatrix(cameraMatrix, distCoeffs, imageSize, 1, imageSize, 0),
        imageSize, CV_16SC2, map1, map2);


    while (1) //Show the image captured in the window and repeat
    {
        inputVideo >> frame;              // read
        if (frame.empty()) break;         // check if at end
        remap(frame, frameCalibration, map1, map2, INTER_LINEAR);
        imshow("Origianl", frame);
        imshow("Calibration", frameCalibration);
        char key = waitKey(1);
        if (key == 27 || key == 'q' || key == 'Q')break;
    }
    return 0;
}

```


镜头的畸变校正效果如下：  
![png](/images/posts/original-image.png)   
![png](/images/posts/calibration-image.png)   

>为什么选2系数而不是3系数。因为。。。。。。。
下面是三系数的修正结果，惨不忍睹啊。
![png](/images/posts/calibration3-image.png)   
