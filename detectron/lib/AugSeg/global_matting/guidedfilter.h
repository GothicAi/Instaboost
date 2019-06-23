#ifndef GUIDED_FILTER_H
#define GUIDED_FILTER_H

#include <opencv2/opencv.hpp>

class GuidedFilterImpl;

class GuidedFilter
{
public:
    GuidedFilter(const cv::Mat &I, int r, double eps);
    ~GuidedFilter();

    cv::Mat filter(const cv::Mat &p, int depth = -1) const;

private:
    GuidedFilterImpl *impl_;
};

cv::Mat guidedFilterWrapper(const cv::Mat &I, cv::Mat &p, const cv::Mat &t, int r, double eps, int depth = -1);

#endif
