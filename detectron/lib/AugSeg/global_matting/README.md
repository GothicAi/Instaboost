# Global Matting Algorithm with Cython Interface

This is an global matting algorithm based on [this repository](https://github.com/atilimcetin/global-matting). Its core algorithms are written in c++ to guarantee the speed, and it provides a python interface to integrate it with other data processing methods. Paper of the algorithm:

He, Kaiming, et al. ["A global sampling method for alpha matting."](http://kaiminghe.com/publications/cvpr11matting.pdf) In CVPR’11, pages 2049–2056, 2011.

Together, with an implementation of Cython wrapper to allow the convertion between a `numpy.array` and a `cv::Mat` and the other way arround (`cv::Mat` to `numpy.array`). The Cython wrapper is based on [this repository](https://github.com/solivr/cython_opencvMat).

## Build

First, specify your opencv library path in `setup.py:line 10-13`. For me, the opencv library is in `/usr/lib/x86_64-linux-gnu` and the `prefix` is `/usr`. Note that the `prefix` will be useful again in `setup.py:line 30` for the opencv include path.

To build, run `python3 setup.py build_ext --inplace` and ignore any warnings.

When building is complete, test the algorithm via `python3 test.py`.

You should see a `GT04-alpha.png` with good matting result.

## Notes

The code was built and tested on Ubuntu 14.04, with Python 3.4 and OpenCV 2.4. But it should work with other Python and  OpenCV versions.