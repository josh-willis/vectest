#include <stdio.h>
#include <stdlib.h>

__attribute__((target_clones("avx2","avx","sse4.2","default")))
void vfunc_fmv(float * __restrict__ a, float * __restrict__ b, float * __restrict__ c, size_t arrlen){
  size_t i;
  float t, d, c1, c2;

  a = __builtin_assume_aligned(a, 32);
  b = __builtin_assume_aligned(b, 32);
  c = __builtin_assume_aligned(c, 32);

  c1 = 3.0;
  c2 = 4.5;

  for (i=0; i<arrlen; i++){
    t = b[i] * c[i];
    d = c[i] * c[i];
    a[i] = b[i] + c1*t + c2*d;
  }
  return;
}

void vfunc(float * __restrict__ a, float * __restrict__ b, float * __restrict__ c, size_t arrlen){
  size_t i;
  float t, d;

  for (i=0; i<arrlen; i++){
    t = b[i] * c[i];
    d = c[i] * c[i];
    a[i] = b[i] + 3.0*t + 4.5*d;
  }
  return;
}

void vfunc_slow(float *a, float *b, float *c, size_t arrlen){
  size_t i;
  float t, d;

  for (i=0; i<arrlen; i++){
    t = b[i] * c[i];
    d = c[i] * c[i];
    a[i] = b[i] + 3.0*t + 4.5*d;
  }
  return;
}

__attribute__((target_clones("avx2","avx","sse4.2","default")))
void vsin_fmv(float * __restrict__ a, size_t arrlen){
  size_t i;

  for (i=0; i<arrlen; i++){
    a[i] = sin(a[i]);
  }
  return;
}
  
void vsin(float * __restrict__ a, size_t arrlen){
  size_t i;

  for (i=0; i<arrlen; i++){
    a[i] = sin(a[i]);
  }
  return;
}
  

