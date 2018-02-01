import cython

import numpy
cimport numpy

cdef extern from "vfunc.c":
  void vfunc(float* a, float* b, float* c, size_t alen) 
  void vfunc_fmv(float* a, float* b, float* c, size_t alen) 

@cython.boundscheck(False)
@cython.wraparound(False)
def vecfunc(numpy.ndarray[float, ndim=1, mode="c"] a not None,
            numpy.ndarray[float, ndim=1, mode="c"] b not None,
            numpy.ndarray[float, ndim=1, mode="c"] c not None):
#    if (a.shape != b.shape) or (b.shape != c.shape):
#        raise ValueError("Array size mis-match")

    cdef size_t arrlen
    arrlen = a.shape[0]

    vfunc(&a[0], &b[0], &c[0], arrlen)

    return None

@cython.boundscheck(False)
@cython.wraparound(False)
def vecfunc_fmv(numpy.ndarray[float, ndim=1, mode="c"] a not None,
                numpy.ndarray[float, ndim=1, mode="c"] b not None,
                numpy.ndarray[float, ndim=1, mode="c"] c not None):

#    if (a.shape != b.shape) or (b.shape != c.shape):
#        raise ValueError("Array size mis-match")

    cdef size_t arrlen
    arrlen = a.shape[0]

    vfunc_fmv(&a[0], &b[0], &c[0], arrlen)

    return None

def zeros_aligned(n, dtype, bytes_aligned):
    d = numpy.dtype(dtype)
    nbytes = (d.itemsize)*n
    tmp = numpy.zeros(nbytes+bytes_aligned, dtype=numpy.uint8)
    address = tmp.__array_interface__['data'][0]
    offset = (bytes_aligned - address%bytes_aligned)%bytes_aligned
    return tmp[offset:offset+nbytes].view(dtype=numpy.dtype(dtype))

def ones_aligned(n, dtype, bytes_aligned):
    d = numpy.dtype(dtype)
    nbytes = (d.itemsize)*n
    tmp = numpy.zeros(nbytes+bytes_aligned, dtype=numpy.uint8)
    address = tmp.__array_interface__['data'][0]
    offset = (bytes_aligned - address%bytes_aligned)%bytes_aligned
    tmp2 = tmp[offset:offset+nbytes].view(dtype=numpy.dtype(dtype))
    tmp2[:] = 1
    return tmp2
