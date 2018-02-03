#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("vectest",
                             sources=["vectest.pyx"],
                             extra_compile_args=[ '-O3', '-w', '-fopt-info-vec',
                                                  '-ffast-math', '-ffinite-math-only', '-lm'],                             
                             include_dirs=[numpy.get_include()])],
)
