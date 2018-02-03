#!/usr/bin/env python
# coding: utf-8

import numpy as np
import vectest
from timeit import Timer

nsize = 1024*64
a = vectest.zeros_aligned(nsize, dtype=np.float32, bytes_aligned=32)
b = vectest.ones_aligned(nsize, dtype=np.float32, bytes_aligned=32)
c = vectest.ones_aligned(nsize, dtype=np.float32, bytes_aligned=32)
b *= 2.0
c *= 3.0

def wrapped_nofmv():
    vectest.vecfunc(a,b,c)

def wrapped_fmv():
    vectest.vecfunc_fmv(a,b,c)

def wrapped_sin_nofmv():
    vectest.vecsin(b)

def wrapped_sin_fmv():
    vectest.vecsin_fmv(b)

if __name__ == '__main__':
    import timeit
    print "Applying function using non-multiversioned code, vectest.vecfunc(a,b,c):"
    vectest.vecfunc(a,b,c)
    print "Value of a is {0}\n".format(a)

    print "Applying function using multiversioned code, vectest.vecfunc_fmv(a,b,c):"
    vectest.vecfunc_fmv(a,b,c)
    print "Value of a is {0}\n".format(a)
    
    nloops = 10000
    nrepeats = 3

    print "Timing non-multiversioned code:"
    t1 = Timer(wrapped_nofmv)
    t1_list =t1.repeat(repeat=nrepeats, number = nloops)
    t1best_usec = min(t1_list)*1e6/nloops
    print "{0} loops, best of {1}: {2} usec per loop".format(nloops, nrepeats, t1best_usec)

    print "\nTiming multiversioned code:"
    t2 = Timer(wrapped_fmv)
    t2_list =t2.repeat(repeat=nrepeats, number = nloops)
    t2best_usec = min(t2_list)*1e6/nloops
    print "{0} loops, best of {1}: {2} usec per loop".format(nloops, nrepeats, t2best_usec)

    print "\nTiming non-multiversioned vector sine:"
    t3 = Timer(wrapped_sin_nofmv)
    t3_list =t3.repeat(repeat=nrepeats, number = nloops)
    t3best_usec = min(t3_list)*1e6/nloops
    print "{0} loops, best of {1}: {2} usec per loop".format(nloops, nrepeats, t3best_usec)

    print "\nTiming multiversioned code:"
    t4 = Timer(wrapped_sin_fmv)
    t4_list =t4.repeat(repeat=nrepeats, number = nloops)
    t4best_usec = min(t4_list)*1e6/nloops
    print "{0} loops, best of {1}: {2} usec per loop".format(nloops, nrepeats, t4best_usec)
