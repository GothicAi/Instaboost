cimport numpy as np
import numpy as np

# For cv::Mat usage
cdef extern from "core/core.hpp":
  cdef int  CV_WINDOW_AUTOSIZE
  cdef int CV_8UC3
  cdef int CV_8UC1

cdef extern from "core/core.hpp" namespace "cv":
  cdef cppclass Mat:
    Mat() except +
    void create(int, int, int)
    void* data
    int rows
    int cols
    int channels()  

cdef extern from "globalmatting.h":
    void expansionOfKnownRegionsWrapper(Mat, Mat, int)
    void globalMattingWrapper(Mat, Mat, Mat&, Mat&)
    
cdef extern from "guidedfilter.h":
    Mat guidedFilterWrapper(const Mat&, Mat&, const Mat&, int, double, int)

# For Buffer usage
cdef extern from "Python.h":
    ctypedef struct PyObject
    object PyMemoryView_FromBuffer(Py_buffer *view)
    int PyBuffer_FillInfo(Py_buffer *view, PyObject *obj, void *buf, Py_ssize_t len, int readonly, int infoflags)
    enum:
        PyBUF_FULL_RO

cdef Mat np2Mat(np.ndarray ary)

cdef object Mat2np(Mat mat)