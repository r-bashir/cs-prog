#!/usr/bin/env python
# coding: utf-8


def fib (n) :
  if n == 0 :
    return 0
  elif n == 1 :
    return 1
  else :
    return fib (n - 1) + fib (n - 2)
    
    
import time
tstart = time . perf_counter ()
fib(40)
tstop = time . perf_counter ()
print(f"Measured time : { tstop - tstart } seconds")
