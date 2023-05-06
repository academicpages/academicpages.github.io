#include <opencv2/opencv.hpp>
#include <iostream>

void TemplateMatch(cv::Mat frame, cv::Mat template_image, cv::Mat mask_img) {
  std::vector<cv::Mat> channels;
  cv::split(frame, channels);
  for(size_t i = 0; i < channels.size(); i++) {
    cv::bitwise_and(channels[i], mask_img, channels[i]);
  }
  cv::Mat mask_frame;
  cv::merge(channels, mask_frame);

  // 定义缩放因子,多尺度模版匹配
  vector<double> scale_factors = {1.2, 1.0, 0.8, 0.6};
  double max_val = 0;
  cv::Rect best_rect;
  for (size_t i = 0; i < scale_factors.size(); i++) {
    cv::Mat template_scaled;
    cv::resize(template_image, template_scaled, cv::Size(), scale_factors[i], scale_factors[i]);
    cv::Mat result;
    cv::matchTemplate(mask_frame, template_scaled, result, cv::TM_CCOEFF_NORMED);

    cv::Point loc;
    double val;
    minMaxLoc(result, nullptr, &val, nullptr, &loc);
    if (val > max_val) {
      max_val = val;
      best_rect = cv::Rect(loc.x, loc.y, template_scaled.cols, template_scaled.rows);
    }
    //cv::Rect match_rect(loc.x, loc.y, template_scaled.cols, template_scaled.rows);
    //cv::rectangle(frame, match_rect, cv::Scalar(0, 0, 255 - 20 * i), 2);
  }
  // 大于一定得分阈值的进行输出
  if (max_val > 0.65) {
    cv::line(frame, best_rect.tl(), best_rect.br(), cv::Scalar(255, 0, 0), 2);
    cv::line(frame, best_rect.tl() + cv::Point(best_rect.width, 0),
             best_rect.tl() + cv::Point(0, best_rect.height), cv::Scalar(255, 0, 0), 2);
    std::string area_text = "area: " + std::to_string(best_rect.area());
    cv::putText(frame, area_text, best_rect.tl() - cv::Point(2, 2),
                cv::FONT_HERSHEY_SIMPLEX, 1.0, cv::Scalar(0, 50, 255), 2);
    cv::rectangle(frame, best_rect, cv::Scalar(0, 255, 0), 2);
  }
}

void EdgeBasedMethod(cv::Mat frame) {
  cv::resize(frame, frame, cv::Size(frame.cols / 3, frame.rows / 3));
  cv::Mat gray;
  cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);
  cv::GaussianBlur(frame, frame, cv::Size(3, 3), 0, 0);
  cv::Mat edges;
  cv::Canny(gray, edges, 80, 160);

  std::vector<cv::Vec4i> lines;
  cv::HoughLinesP(edges, lines, 1, CV_PI/180, 10);  // HoughLinesP检测线段

// 筛选近似水平或竖直的线段
  for (size_t i = 0; i < lines.size(); i++) {
    float delta_x = std::abs(lines[i][0] - lines[i][2]);
    float delta_y = std::abs(lines[i][1] - lines[i][3]);
    float slope = delta_y / delta_x;

    if ((slope < 0.1) || (slope > 10)) {  // 斜率在0.1到10之间的线段被排除
      continue;
    }

//    float line_length = std::sqrt(delta_x * delta_x + delta_y * delta_y);
//    if (line_length < 20) {  // 线段长度小于20被排除
//      continue;
//    }
    cv::line(frame, cv::Point(lines[i][0], lines[i][1]),
             cv::Point(lines[i][2], lines[i][3]), cv::Scalar(0, 0, 255), 2, cv::LINE_AA);
  }

  cv::imshow("frame", frame);
  cv::waitKey(0);
}

void ContourBased(cv::Mat frame) {
  // 转换为灰度图像
  cv::Mat gray;
  cv::cvtColor(frame, gray, cv::COLOR_BGR2GRAY);

  // 进行边缘检测
  cv::Mat edges;
  cv::Canny(gray, edges, 50, 150);

  // 查找轮廓
  std::vector<std::vector<cv::Point>> contours;
  std::vector<cv::Vec4i> hierarchy;
  cv::findContours(edges, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);

  // 对每个轮廓进行处理
  for (size_t i = 0; i < contours.size(); i++) {
    // 进行多边形拟合
    std::vector<cv::Point> approx;
    cv::approxPolyDP(contours[i], approx, cv::arcLength(contours[i], true) * 0.02, true);

    // 如果拟合结果是一个四边形，则绘制出来
    if (approx.size() == 4) {
      cv::polylines(frame, approx, true, cv::Scalar(0, 0, 255), 2);
    }
  }
  cv::resize(frame, frame, cv::Size(frame.cols / 3, frame.rows / 3));
  cv::imshow("frame", frame);
  cv::waitKey(0);
}

int main(int argc, char **argv) {
  cv::VideoCapture cap("./output.avi");
  if (!cap.isOpened()) {
    std::cerr << "Error opening video file." << std::endl;
    return -1;
  }
  std::string template_path = "./template.png";
  cv::Mat template_image = cv::imread(template_path);
  cv::Mat mask_img = cv::imread("./mask.png", cv::IMREAD_GRAYSCALE);

  cv::Mat frame;
  int frame_count = 0;
  while (cap.read(frame)) {
    // 处理每一帧图像
    TemplateMatch(frame, template_image, mask_img);
    // 显示当前帧图像
    cv::resize(frame, frame, cv::Size(frame.cols / 2, frame.rows / 2));
    cv::imshow("Frame", frame);
    cv::waitKey(10);
  }

  cap.release();
  cv::destroyAllWindows();
  return 0;
}