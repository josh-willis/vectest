

all: vectest.pyx vfunc.c
	python setup.py build_ext --inplace
	objdump -S vectest.so > vectest.S

clean:
	rm -rf build vectest.c vectest.so vectest.S
