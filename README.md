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
You can check the performance difference by running the test script, yielding for example:
```
$ ./test_script.py 
Applying function using non-multiversioned code, vectest.vecfunc(a,b,c):
Value of a is [ 60.5  60.5  60.5 ...,  60.5  60.5  60.5]

Applying function using multiversioned code, vectest.vecfunc_fmv(a,b,c):
Value of a is [ 60.5  60.5  60.5 ...,  60.5  60.5  60.5]

Timing non-multiversioned code:
10000 loops, best of 3: 93.5055017471 usec per loop

Timing multiversioned code:
10000 loops, best of 3: 52.6381015778 usec per loop
```
The example function itself is a little silly, but just multiplying together two vectors did not give enough arithmetic 
for the advantages of the vectorization to show up in the timing. I've proivded functions to allocate aligned arrays
of zeros or ones, and used those, though for this function, on the platforms I tested, allowing the compiler to assume alignment
didn't make a big difference. The things that mattered are the `__restrict__` keywords in the function declaration, and
explicitly declaring the constants as variables which were floats (otherwise they're assumed doubles).  And of course, using 
the `target_clones` attribute before the function definition. But focusing on most of this is a distraction: exactly what has
to be done to coax the compiler to vectorize will vary enormously from function to function (and even different versions of
the compiler).

Finally, the build process will also dump the object file. Obviously you wouldn't do this in a regular Cythonized module,
but it allows us to check that there are in fact multiple versions of the `vfunc_fmv` function inside, and only one of the
simple `vfunc` function. One can also inspect to see what has been vectorized and what not, if one wants.
