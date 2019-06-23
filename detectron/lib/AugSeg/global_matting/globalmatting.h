#ifndef GLOBAL_MATTING_H
#define GLOBAL_MATTING_H

#include <opencv2/opencv.hpp>

void expansionOfKnownRegionsWrapper(cv::Mat img, cv::Mat trimap, int niter = 9);
void globalMattingWrapper(cv::Mat image, cv::Mat trimap, cv::Mat& foreground, cv::Mat& alpha);

#endif
