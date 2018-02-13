# vectest
This repository demonstrates using a modern `gcc` to get function multi-versioning from within Cython.

To test, make sure you have `gcc >= 6.0` installed, at least. On the CIT LDG cluster, one can activate this using:
```
scl enable devtoolset-7 bash
```
and then see:
```
$ gcc --version
gcc (GCC) 7.2.1 20170829 (Red Hat 7.2.1-1)
Copyright (C) 2017 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```
To build, you just need to type `make`, from within a Python environment that has `numpy` and `Cython`.
You can check the performance difference by running the test script, yielding for example on a 3.5 GHz Haswell:
```
$ ./test_script.py 
Applying function using non-multiversioned code, vectest.vecfunc(a,b,c):
Value of a is [60.5 60.5 60.5 ... 60.5 60.5 60.5]

Applying function using multiversioned code, vectest.vecfunc_fmv(a,b,c):
Value of a is [60.5 60.5 60.5 ... 60.5 60.5 60.5]

Timing non-multiversioned code:
10000 loops, best of 3: 59.690117836 usec per loop

Timing multiversioned code (simple, no 'restrict', 'assume_aligned', or disabling Python syntax):
10000 loops, best of 3: 15.5333042145 usec per loop

Timing multiversioned code:
10000 loops, best of 3: 14.332485199 usec per loop

Timing slow (no 'restrict', no FMV) code:
10000 loops, best of 3: 59.5462083817 usec per loop

Timing non-multiversioned vector sine:
10000 loops, best of 3: 152.745008469 usec per loop

Timing multiversioned code:
10000 loops, best of 3: 152.74078846 usec per loop
```
The example function itself is a little silly, but just multiplying together two vectors did not give enough arithmetic 
for the advantages of the vectorization to show up in the timing. I've proivded functions to allocate aligned arrays
of zeros or ones, and used those, though for this function, on the platforms I tested, allowing the compiler to assume alignment
didn't make a big difference. The two different multi-versioned implementations of `vecfunc` show various tweaks that in principle
could affect how well the compiler vectorizes, though for this example they did not. But they could be worth exploring,
especially if you find the compiler has not seemed to vectorize your particular application well.

The other example function is two different versions of a function with vector input that computes the sine (element by
element) of its argument. For recent enough compilers, `gcc` can also in principle vectorize this. However, we do not see
any difference above because that requires not only a newer `gcc`, but also a newer `glibc`. That is much more involved to test
and I have not yet done so.

Finally, the build process will also dump the object file. Obviously you wouldn't do this in a regular Cythonized module,
but it allows us to check that there are in fact multiple versions of the `vfunc_fmv` function inside, and only one of the
simple `vfunc` function. One can also inspect to see what has been vectorized and what not, if one wants.
