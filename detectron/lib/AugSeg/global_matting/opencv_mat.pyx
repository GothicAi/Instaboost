import numpy as np
cimport numpy as np  # for np.ndarray
from libc.string cimport memcpy
from opencv_mat cimport *

# inspired and adapted from http://makerwannabe.blogspot.ch/2013/09/calling-opencv-functions-via-cython.html

cdef Mat np2Mat3D(np.ndarray ary):
    assert ary.ndim==3 and ary.shape[2]==3, "ASSERT::3channel RGB only!!"
    ary = np.dstack((ary[...,2], ary[...,1], ary[...,0])) #RGB -> BGR

    cdef np.ndarray[np.uint8_t, ndim=3, mode ='c'] np_buff = np.ascontiguousarray(ary, dtype=np.uint8)
    cdef unsigned int* im_buff = <unsigned int*> np_buff.data
    cdef int r = ary.shape[0]
    cdef int c = ary.shape[1]
    cdef Mat m
    m.create(r, c, CV_8UC3)
    memcpy(m.data, im_buff, r*c*3)
    return m

cdef Mat np2Mat2D(np.ndarray ary):
    assert ary.ndim==2, "ASSERT::1 channel grayscale only!!"

    cdef np.ndarray[np.uint8_t, ndim=2, mode ='c'] np_buff = np.ascontiguousarray(ary, dtype=np.uint8)
    cdef unsigned int* im_buff = <unsigned int*> np_buff.data
    cdef int r = ary.shape[0]
    cdef int c = ary.shape[1]
    cdef Mat m
    m.create(r, c, CV_8UC1)
    memcpy(m.data, im_buff, r*c)
    return m


cdef Mat np2Mat(np.ndarray ary):
    if ary.ndim == 2:
        return np2Mat2D(ary)
    elif ary.ndim == 3:
        return np2Mat3D(ary)


cdef object Mat2np(Mat m):
    # Create buffer to transfer data from m.data
    cdef Py_buffer buf_info
    # Define the size / len of data
    cdef size_t len = m.rows*m.cols*m.channels()*sizeof(CV_8UC3)
    # Fill buffer
    PyBuffer_FillInfo(&buf_info, NULL, m.data, len, 1, PyBUF_FULL_RO)
    # Get Pyobject from buffer data
    Pydata  = PyMemoryView_FromBuffer(&buf_info)

    # Create ndarray with data
    shape_array = (m.rows, m.cols, m.channels())
    ary = np.ndarray(shape=shape_array, buffer=Pydata, order='c', dtype=np.uint8)

    # BGR -> RGB
    if ary.ndim == 3 and ary.shape[2] == 3:
        ary = np.dstack((ary[...,2], ary[...,1], ary[...,0]))
    # Convert to numpy array
    pyarr = np.asarray(ary)
    if pyarr.ndim == 3 and pyarr.shape[2] == 1:
        pyarr = np.reshape(pyarr, pyarr.shape[:-1])
    return pyarr


def np2Mat2np(nparray):
    cdef Mat m

    # Convert numpy array to cv::Mat
    m = np2Mat(nparray)

    # Convert cv::Mat to numpy array
    pyarr = Mat2np(m)

    return pyarr

    
def expansion_of_known_regions(img_arr, trimap_arr, niter):
    cdef Mat img_m, trimap_m
    cdef int niter_c = niter

    # Convert numpy array to cv::Mat
    img_m = np2Mat(img_arr)
    trimap_m = np2Mat(trimap_arr)
    
    expansionOfKnownRegionsWrapper(img_m, trimap_m, niter_c)

    # Convert cv::Mat to numpy array
    img_arr = Mat2np(img_m)
    trimap_arr = Mat2np(trimap_m)

    return img_arr, trimap_arr


def global_matting(img_arr, trimap_arr):
    cdef Mat img_m, trimap_m, foreground_m, alpha_m
    alpha_arr = np.zeros(trimap_arr.shape)
    
    img_m = np2Mat(img_arr)
    trimap_m = np2Mat(trimap_arr)
    alpha_m = np2Mat(alpha_arr)
    
    globalMattingWrapper(img_m, trimap_m, foreground_m, alpha_m)
    
    alpha_arr = Mat2np(alpha_m)
    
    return alpha_arr.copy()
    

def guided_filter(img_arr, trimap_arr, alpha_arr, r, eps, depth=-1):
    cdef Mat img_m, trimap_m, alpha_m, outp_m
    
    img_m = np2Mat(img_arr)
    trimap_m = np2Mat(trimap_arr)
    alpha_m = np2Mat(alpha_arr)
    
    outp_m = guidedFilterWrapper(img_m, alpha_m, trimap_m, r, eps, depth)

    outp_arr = Mat2np(outp_m)
    
    return outp_arr.copy()


cdef class PyMat:
    cdef Mat mat

    def __cinit__(self, np_mat):
        self.mat = np2Mat(np_mat)

    def get_mat(self):
        return Mat2np(self.mat)
